from typing import Tuple, Any
import plotly.graph_objects as go
from plotly.basedatatypes import BaseTraceType
import funcnodes as fn
from exposedfunctionality.function_parser.types import add_type

add_type(
    go.Figure,
    "plotly.Figure",
)
add_type(
    BaseTraceType,
    "plotly.Trace",
)

from .plots import make_scatter, make_bar
from .figure import make_figue, add_trace, plot


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
    nodes=[
        make_scatter,
        make_bar,
        make_figue,
        add_trace,
        plot,
    ],
    name="Plotly",
    description="A collection of functions for creating plotly plots.",
    subshelves=[],
)


__version__ = "0.1.1"
