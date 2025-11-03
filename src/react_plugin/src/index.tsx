import * as React from "react";
// TYPE-ONLY import to avoid bundling plotly; we load from CDN at runtime
import type * as Plotly from "plotly.js";
import {
  FuncNodesReactPlugin,
  LATEST_VERSION,
  RenderPluginFactoryProps,
  RendererPlugin,
  DataViewRendererType,
  DataViewRendererProps,
  DataViewRendererToDataPreviewViewRenderer,
} from "@linkdlab/funcnodes-react-flow-plugin";
import "./style.css";

// Minimum delay between renders in milliseconds
const RENDER_DELAY_MS = 1000;

declare global {
  interface Window {
    Plotly: any; // runtime Plotly from CDN
  }
}

let LOAD_PLOTLY_PROMISE: Promise<void> | null = null;

async function importPlotly() {
  if (LOAD_PLOTLY_PROMISE) return LOAD_PLOTLY_PROMISE;

  if (typeof window === "undefined") {
    // SSR guard: nothing to do during server render
    return Promise.resolve();
  }

  if (typeof window.Plotly === "undefined") {
    const script = document.createElement("script");

    script.src = "https://cdn.plot.ly/plotly-3.1.0.min.js";
    script.async = true;
    document.head.appendChild(script);
    LOAD_PLOTLY_PROMISE = new Promise<void>((resolve) => {
      script.onload = () => resolve();
    });
    return LOAD_PLOTLY_PROMISE;
  }

  return Promise.resolve();
}

function normalizePlotlyLayout(
  layout: Plotly.Layout | undefined
): Plotly.Layout {
  const out: Plotly.Layout = { ...layout } as Plotly.Layout;
  out.autosize = true;
  out.font = { ...(out.font || {}), family: "Arial, Helvetica, sans-serif" };

  return out;
}

/**
 * Core hook that renders a Plotly figure into a DIV without <Plot>.
 * Handles:
 *   - debounced updates
 *   - CDN loading
 *   - responsive resize
 *   - cleanup/purge
 */
function usePlotlyDivRenderer({
  value,
  staticMode,
}: {
  value: unknown;
  staticMode: boolean;
}) {
  const containerRef = React.useRef<HTMLDivElement | null>(null);
  const latestValueRef = React.useRef(value);
  const timeoutRef = React.useRef<number | null>(null);
  const lastRenderTimeRef = React.useRef<number>(0);
  const roRef = React.useRef<ResizeObserver | null>(null);
  const isMountedRef = React.useRef(false);

  const scheduleRender = React.useCallback(() => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    const now = Date.now();
    const timeSinceLastRender = now - lastRenderTimeRef.current;
    const delay = Math.max(0, RENDER_DELAY_MS - timeSinceLastRender);

    timeoutRef.current = window.setTimeout(async () => {
      // Load Plotly if needed
      // await importPlotly();
      if (!isMountedRef.current) return;

      const v: any = latestValueRef.current;
      if (!v || typeof v !== "object" || !("data" in v) || !("layout" in v)) {
        return;
      }

      const data = (v.data || []) as Plotly.Data[];
      const layout = normalizePlotlyLayout(v.layout as Plotly.Layout);
      const config: Partial<Plotly.Config> = {
        staticPlot: staticMode,
        displayModeBar: !staticMode,
        responsive: true,
        scrollZoom: false,
        doubleClick: false,
      };

      const gd = containerRef.current;
      if (!gd || typeof window === "undefined" || !window.Plotly) return;

      try {
        // Plotly.react will create or update the plot efficiently
        await window.Plotly.react(gd, data, layout, config);
      } catch (err) {
        // Fail fast — no silent errors
        // eslint-disable-next-line no-console
        console.error("Plotly.react failed:", err);
      }

      lastRenderTimeRef.current = Date.now();
      timeoutRef.current = null;
    }, delay);
  }, [staticMode]);

  React.useEffect(() => {
    isMountedRef.current = true;

    // Set up resize observer for responsiveness
    const gd = containerRef.current;
    const attachResize = () => {
      if (!gd) return;
      roRef.current = new ResizeObserver(() => {
        if (gd && window.Plotly) {
          try {
            window.Plotly.Plots.resize(gd);
          } catch {
            /* ignore */
          }
        }
      });
      roRef.current.observe(gd);
    };

    attachResize();
    // initial draw attempt
    scheduleRender();

    return () => {
      isMountedRef.current = false;
      if (timeoutRef.current) clearTimeout(timeoutRef.current);
      if (roRef.current) roRef.current.disconnect();
      if (gd && window.Plotly) {
        try {
          window.Plotly.purge(gd);
        } catch {
          /* ignore */
        }
      }
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  React.useEffect(() => {
    latestValueRef.current = value;
    scheduleRender();
  }, [value, scheduleRender]);

  return containerRef;
}

const PreviewPlotlyImageRenderer: DataViewRendererType = ({
  value,
}: DataViewRendererProps) => {
  const containerRef = usePlotlyDivRenderer({ value, staticMode: true });

  // SSR guard
  if (typeof window === "undefined") return <></>;

  // Basic shape checks to avoid flashing an empty div
  if (
    !value ||
    typeof value !== "object" ||
    !("data" in (value as any)) ||
    !("layout" in (value as any))
  ) {
    return <></>;
  }

  return (
    <div
      className="funcnodes_plotly_container"
      style={{ width: "100%", height: "100%", pointerEvents: "none" }}
    >
      <div ref={containerRef} style={{ width: "100%", height: "100%" }} />
    </div>
  );
};

const PlotlyImageRenderer: DataViewRendererType = ({
  value,
}: DataViewRendererProps) => {
  const containerRef = usePlotlyDivRenderer({ value, staticMode: false });

  if (typeof window === "undefined") return <></>;

  if (
    !value ||
    typeof value !== "object" ||
    !("data" in (value as any)) ||
    !("layout" in (value as any))
  ) {
    return <></>;
  }

  return (
    <div
      className="funcnodes_plotly_container"
      style={{ width: "100%", height: "100%" }}
    >
      <div ref={containerRef} style={{ width: "100%", height: "100%" }} />
    </div>
  );
};

const renderpluginfactory = ({}: RenderPluginFactoryProps) => {
  const MyRendererPlugin: RendererPlugin = {
    data_preview_renderers: {
      "plotly.Figure": DataViewRendererToDataPreviewViewRenderer(
        PreviewPlotlyImageRenderer
      ),
    },
    data_view_renderers: {
      "plotly.Figure": PlotlyImageRenderer,
    },
  };

  return MyRendererPlugin;
};

const Plugin: FuncNodesReactPlugin = {
  renderpluginfactory,
  v: LATEST_VERSION,
};

export default Plugin;
