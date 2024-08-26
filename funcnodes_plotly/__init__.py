from typing import Tuple, Any
import plotly.graph_objects as go
from plotly.basedatatypes import BaseTraceType
import funcnodes as fn
from exposedfunctionality.function_parser.types import add_type
from . import plots, layout, figure, express
import os

import funcnodes_pandas  # noqa: F401

add_type(
    go.Figure,
    "plotly.Figure",
)
add_type(
    BaseTraceType,
    "plotly.Trace",
)

add_type(
    Tuple[int, int, int],
    "color",
)


FUNCNODES_RENDER_OPTIONS: fn.RenderOptions = {
    "typemap": {
        go.Figure: "plotly.Figure",
    },
}


def figureencoder(figure: go.Figure, preview: bool = False) -> Tuple[Any, bool]:
    if isinstance(figure, go.Figure):
        return figure.to_plotly_json(), True
    return figure, False


fn.JSONEncoder.add_encoder(figureencoder)


NODE_SHELF = fn.Shelf(
    nodes=[],
    name="Plotly",
    description="A collection of functions for creating plotly plots.",
    subshelves=[
        plots.NODE_SHELF,
        layout.NODE_SHELF,
        figure.NODE_SHELF,
        express.NODE_SHELF,
    ],
)

REACT_PLUGIN = {
    "module": os.path.join(os.path.dirname(__file__), "react_plugin", "js", "main.js"),
}


__version__ = "0.1.7"
