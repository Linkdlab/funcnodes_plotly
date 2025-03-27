import { v1_types } from "@linkdlab/funcnodes_react_flow";
import plotly from "plotly.js-dist-min";
import "./style.css";

// Helper to enhance a layout with automatic margins for axes
const enhanceLayout = (layout: Partial<Plotly.Layout> = {}) => {
  // Create a deep copy to avoid side effects
  const newLayout = JSON.parse(JSON.stringify(layout));
  Object.keys(newLayout).forEach((key) => {
    if (key.startsWith("xaxis") || key.startsWith("yaxis")) {
      const axisKey = key.split("_")[0];
      if (!newLayout[axisKey]) {
        newLayout[axisKey] = {};
      }
      newLayout[axisKey].automargin = true;
    }
  });
  return newLayout;
};

// Define your maximum cache size
const MAX_CACHE_SIZE = 50;

class LRUCache<K, V> {
  private cache = new Map<K, V>();

  get(key: K): V | undefined {
    if (!this.cache.has(key)) return undefined;
    const value = this.cache.get(key)!;
    // Mark key as recently used: remove and re-insert it.
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }

  set(key: K, value: V) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    }
    this.cache.set(key, value);
    // Evict the oldest entry if cache size exceeds the maximum
    if (this.cache.size > MAX_CACHE_SIZE) {
      const oldestKey = this.cache.keys().next().value;
      if (oldestKey) this.cache.delete(oldestKey);
    }
  }
}

// Create a global LRU cache instance
const globalPlotlyImageCache = new LRUCache<string, string>();

const renderpluginfactory = ({ React }: v1_types.RenderPluginFactoryProps) => {
  const RenderFigure = ({
    data,
    layout,
    staticPlot = false,
  }: {
    data: Plotly.Data[];
    layout: Partial<Plotly.Layout>;
    staticPlot?: boolean;
  }) => {
    const plotRef = React.useRef<HTMLDivElement>(null);

    // Memoize replot function to avoid unnecessary re-renders
    const replot = React.useCallback(() => {
      if (!plotRef.current) return;
      // console.log("Rendering plot");
      plotly.react(
        plotRef.current,
        data,
        { ...layout, autosize: true },
        {
          displayModeBar: !staticPlot,
          staticPlot,
          responsive: true,
        }
      );
    }, [data, layout, staticPlot]);

    // Effect for updating the plot on dependency changes
    React.useEffect(() => {
      if (plotRef.current) {
        replot();
      }
    }, [replot]);

    // // Effect for cleanup only when the component unmounts
    // React.useEffect(() => {
    //   return () => {
    //     if (plotRef.current) {
    //       plotly.purge(plotRef.current);
    //     }
    //   };
    // }, []);

    return (
      <div className="funcnodes_plotly_container" ref={plotRef}>
        {" "}
      </div>
    );
  };

  const PlotlyOverlayRenderer: v1_types.DataOverlayRendererType = ({
    value,
    preValue,
  }: v1_types.DataOverlayRendererProps) => {
    const usevalue = value ?? preValue;

    const ref = React.useRef<HTMLDivElement>(null);
    if (usevalue === undefined) {
      return <div>Plotly figure not found</div>;
    }
    const layout = value.layout ?? {};
    // React.useEffect(() => {
    //   if (!ref.current) return;
    //   ref.current.style.minHeight = (ref.current.clientWidth * 2) / 3 + "px";

    //   const observer = new ResizeObserver((entries) => {
    //     for (let entry of entries) {
    //       if (entry.target === ref.current) {
    //         ref.current.style.height = ref.current.clientWidth + "px";
    //       }
    //     }
    //   });
    //   // observer.observe(ref.current);
    //   return () => observer.disconnect();
    // }, []);
    return (
      <div ref={ref}>
        <RenderFigure data={value.data} layout={layout} />
      </div>
    );
  };

  // const PreviewPlotlyRenderer = ({ io }: { io: IOType }) => {
  //   let value = io.fullvalue;
  //   const ref = React.useRef<HTMLDivElement>(null);
  //   if (value == undefined) value = io.value;
  //   if (value === undefined) {
  //     value = {};
  //   }

  //   const layout = JSON.parse(JSON.stringify(value.layout || {}));
  //   //make deep copy of layout

  //   React.useEffect(() => {
  //     if (!ref.current) return;
  //     ref.current.style.height = ref.current.clientWidth + "px";

  //     const observer = new ResizeObserver((entries) => {
  //       for (let entry of entries) {
  //         if (entry.target === ref.current) {
  //           ref.current.style.height = ref.current.clientWidth + "px";
  //         }
  //       }
  //     });
  //     observer.observe(ref.current);
  //     return () => observer.disconnect();
  //   }, []);

  //   layout.margin = { l: 10, r: 10, t: 10, b: 10 };
  //   layout.legend = {
  //     yanchor: "top",
  //     y: 0.99,
  //     xanchor: "left",
  //     x: 0.01,
  //   };

  //   const axes: string[] = [];
  //   for (const layoutkey in layout) {
  //     if (layoutkey.startsWith("xaxis") || layoutkey.startsWith("yaxis")) {
  //       const axis = layoutkey.split("_")[0];
  //       if (!axes.includes(axis)) {
  //         axes.push(axis);
  //       }
  //     }
  //   }

  //   for (const axis of axes) {
  //     if (layout[axis] === undefined) {
  //       layout[axis] = {};
  //     }
  //     layout[axis].automargin = true;
  //   }
  //   if (layout.title?.text) layout.margin.t += 40;

  //   return (
  //     <div style={{ width: "100%", maxHeight: "60vw" }} ref={ref}>
  //       <RenderFigure data={value.data} layout={layout} staticPlot={true} />
  //     </div>
  //   );
  // };

  const RenderImageFigure = ({
    data,
    layout,
    width = 800,
    height = 800,
  }: {
    data: Plotly.Data[];
    layout: Partial<Plotly.Layout>;
    width?: number;
    height?: number;
  }) => {
    const dummyRef = React.useRef<HTMLDivElement>(null);
    const [imgSrc, setImgSrc] = React.useState<string | undefined>(undefined);

    // call Effect as soon as the lazy laoded Plotly is available
    React.useEffect(() => {
      async function render() {
        if (!dummyRef.current) return;
        const key = JSON.stringify({ data, layout, width, height });
        const cached = globalPlotlyImageCache.get(key);
        if (cached) {
          setImgSrc(cached);
          return;
        }
        // console.log("Rendering image", key.length);
        const plot = await plotly.react(dummyRef.current, data, layout);
        const url = await plotly.toImage(plot, {
          format: "png",
          width: width,
          height: height,
        });
        // destroy plot
        // Purge the dummy plot
        // Cache the generated image

        globalPlotlyImageCache.set(key, url);
        setImgSrc(url);
        try {
          plotly.purge(dummyRef.current);
        } catch (e) {}
      }
      render();
    }, [data, layout, width, height]);
    return (
      <>
        {imgSrc && (
          <img src={imgSrc} style={{ width: "100%" }} alt="Plotly chart" />
        )}
        <div ref={dummyRef} style={{ display: "none" }} />
      </>
    );
  };

  const PreviewPlotlyImageRenderer: v1_types.DataViewRendererType = ({
    value,
    preValue,
    width = 800,
    height = 800,
  }: v1_types.DataViewRendererProps & {
    width?: number;
    height?: number;
  }) => {
    const usevalue = value ?? preValue;
    if (usevalue === undefined) {
      return <div>Plotly figure not found</div>;
    }
    const layout = enhanceLayout(value.layout ?? {});

    return (
      <RenderImageFigure
        data={value.data}
        layout={layout}
        width={width}
        height={height}
      />
    );
  };

  // const HandlePlotlyRenderer: v1_types.DataPreviewViewRendererType = ({
  //   iostore,
  // }: v1_types.DataPreviewViewRendererProps) => {
  //   return (
  //     <div style={{ width: "200px" }}>
  //       <PreviewPlotlyImageRenderer iostore={iostore} />
  //     </div>
  //   );
  // };

  return {
    // handle_preview_renderers: {
    //   "plotly.Figure": HandlePlotlyRenderer,
    // },
    data_overlay_renderers: {
      "plotly.Figure": PlotlyOverlayRenderer,
    },
    // data_preview_renderers: {
    //   "plotly.Figure": PreviewPlotlyImageRenderer,
    // },
    data_view_renderers: {
      "plotly.Figure": PreviewPlotlyImageRenderer,
    },
  };
};

const Plugin: v1_types.FuncNodesReactPlugin = {
  renderpluginfactory: renderpluginfactory,
  v: 1,
};

export default Plugin;
