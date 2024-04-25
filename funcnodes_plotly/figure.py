from copy import deepcopy
from typing import List, Dict, Tuple, Any, Literal, Optional
import plotly.graph_objects as go
from plotly.basedatatypes import BaseTraceType
import funcnodes as fn

from .utils import clone_trace, clone_figure


@fn.NodeDecorator("plotly.make_figure", name="Make Figure")
def make_figue() -> go.Figure:
    """
    Create a simple figure object.

    Parameters
    ----------
    data : List[go.Scatter]
        The data to be plotted.
    layout : Dict[str, Any]
        The layout of the plot.

    Returns
    -------
    go.Figure
        The figure object.
    """

    return go.Figure()


@fn.NodeDecorator("plotly.add_trace", name="Add Trace to Figure")
def add_trace(figure: go.Figure, trace: BaseTraceType) -> go.Figure:
    """
    Add a trace to a figure object.

    Parameters
    ----------
    figure : go.Figure
        The figure object to add the trace to.
    trace : go.Scatter
        The trace to be added to the figure.

    Returns
    -------
    go.Figure
        The figure object with the added trace.
    """
    # clone the figure object
    figure = clone_figure(figure)
    trace = clone_trace(trace)

    figure.add_trace(trace)
    return figure


@fn.NodeDecorator(
    "plotly.plot", name="Plot", default_render_options={"data": {"src": "figure"}}
)
def plot(figure: go.Figure) -> go.Figure:
    """
    Plot a figure object.

    Parameters
    ----------
    figure : go.Figure
        The figure object to be plotted.
    """
    return figure