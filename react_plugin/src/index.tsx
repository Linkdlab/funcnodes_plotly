import React, { useEffect, useRef, useState } from "react";
import useResizeObserver from "@react-hook/resize-observer";
import {
  IOType,
  RendererPlugin,
  FuncNodesReactPlugin,
} from "@linkdlab/funcnodes_react_flow";
import Plot from "react-plotly.js";
import plotly from "plotly.js-dist-min";

const RenderFigure = ({
  data,
  layout,
  staticPlot = false,
}: {
  data: Plotly.Data[];
  layout: Partial<Plotly.Layout>;
  staticPlot?: boolean;
}) => {
  return (
    <div style={{ width: "100%", height: "100%" }}>
      <Plot
        data={data}
        layout={{
          ...layout,
          ...{
            responsive: true,
            autosize: true,
          },
        }}
        useResizeHandler={true}
        style={{ width: "100%", height: "100%" }}
        config={{
          displayModeBar: !staticPlot,
          staticPlot: staticPlot,
        }}
      />
    </div>
  );
};

const RenderImageFigure = ({
  data,
  layout,
}: {
  data: Plotly.Data[];
  layout: Partial<Plotly.Layout>;
}) => {
  const dummyref = useRef<HTMLDivElement>(null);
  const [imgSrc, setImgSrc] = useState<string | undefined>(undefined);

  // call Effect as soon as the lazy laoded Plotly is available
  useEffect(() => {
    async function render() {
      if (plotly === undefined) return;
      if (dummyref.current === null) return;
      const plot = await plotly.newPlot(dummyref.current, data, layout);
      const url = await plotly.toImage(plot, {
        format: "png",
        width: 800,
        height: 800,
      });
      // destroy plot
      if (dummyref.current) plotly.purge(dummyref.current);
      setImgSrc(url);
    }
    render();
  }, [plotly, dummyref, data, layout]);
  return (
    <>
      <img
        src={imgSrc}
        style={{
          width: "100%",
        }}
      />
      <div ref={dummyref} style={{ display: "none" }}>
        {" "}
      </div>
    </>
  );
};

const PlotlyOverlayRenderer = ({ io }: { io: IOType }) => {
  let value = io.fullvalue;
  if (value == undefined) value = io.value;
  if (value === undefined) {
    value = {};
  }

  const layout = value.layout || {};

  return (
    <div>
      <RenderFigure data={value.data} layout={layout} />
    </div>
  );
};

const PreviewPlotlyRenderer = ({ io }: { io: IOType }) => {
  let value = io.fullvalue;
  const ref = useRef<HTMLDivElement>(null);
  if (value == undefined) value = io.value;
  if (value === undefined) {
    value = {};
  }

  const layout = JSON.parse(JSON.stringify(value.layout || {}));
  //make deep copy of layout

  useEffect(() => {
    if (ref.current) {
      // set max height to width
      ref.current.style.height = ref.current.clientWidth + "px";
    }
  }, [ref]);

  useResizeObserver<HTMLDivElement>(ref, () => {
    // set height to width
    if (ref.current) ref.current.style.height = ref.current.clientWidth + "px";
  });

  layout.margin = { l: 10, r: 10, t: 10, b: 10 };
  layout.legend = {
    yanchor: "top",
    y: 0.99,
    xanchor: "left",
    x: 0.01,
  };

  const axes: string[] = [];
  for (const layoutkey in layout) {
    if (layoutkey.startsWith("xaxis") || layoutkey.startsWith("yaxis")) {
      const axis = layoutkey.split("_")[0];
      if (!axes.includes(axis)) {
        axes.push(axis);
      }
    }
  }

  for (const axis of axes) {
    if (layout[axis] === undefined) {
      layout[axis] = {};
    }
    layout[axis].automargin = true;
  }
  if (layout.title?.text) layout.margin.t += 40;

  return (
    <div style={{ width: "100%", maxHeight: "60vw" }} ref={ref}>
      <RenderFigure data={value.data} layout={layout} staticPlot={true} />
    </div>
  );
};
const PreviewPlotlyImageRenderer = ({ io }: { io: IOType }) => {
  let value = io.fullvalue;
  if (value == undefined) value = io.value;
  if (value === undefined) {
    value = {};
  }

  const layout = JSON.parse(JSON.stringify(value.layout || {}));
  //make deep copy of layout

  const axes: string[] = [];
  for (const layoutkey in layout) {
    if (layoutkey.startsWith("xaxis") || layoutkey.startsWith("yaxis")) {
      const axis = layoutkey.split("_")[0];
      if (!axes.includes(axis)) {
        axes.push(axis);
      }
    }
  }

  for (const axis of axes) {
    if (layout[axis] === undefined) {
      layout[axis] = {};
    }
    layout[axis].automargin = true;
  }

  return <RenderImageFigure data={value.data} layout={layout} />;
};

const HandlePlotlyRenderer = ({ io }: { io: IOType }) => {
  return (
    <div style={{ width: "200px" }}>
      <PreviewPlotlyRenderer io={io} />
    </div>
  );
};

const PlotlyRendererPlugin: RendererPlugin = {
  handle_preview_renderers: {
    "plotly.Figure": HandlePlotlyRenderer,
  },
  data_overlay_renderers: {
    "plotly.Figure": PlotlyOverlayRenderer,
  },
  data_preview_renderers: {
    "plotly.Figure": PreviewPlotlyImageRenderer,
  },
  data_view_renderers: {
    "plotly.Figure": PreviewPlotlyImageRenderer,
  },
  input_renderers: {},
};

const Plugin: FuncNodesReactPlugin = {
  RendererPlugin: PlotlyRendererPlugin,
};

export default Plugin;
