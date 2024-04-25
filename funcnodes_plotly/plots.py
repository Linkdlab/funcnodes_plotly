from typing import List, Literal, Optional
import plotly.graph_objects as go
import funcnodes as fn


@fn.NodeDecorator("plotly.make_scatter", name="Make Scatter Plot")
def make_scatter(
    y: List[float],
    x: Optional[List[float]] = None,
    mode: Literal["lines", "markers", "lines+markers"] = "lines+markers",
) -> go.Scatter:
    """
    Create a scatter plot with the given x and y values.

    Parameters
    ----------
    y : List[float]
        The y values of the scatter plot.
    x : Optional[List[float]], optional
        The x values of the scatter plot, by default None. If None, the x values will be the indices of the y values.
    mode : Literal["lines", "markers", "lines+markers"], optional
        The mode of the scatter plot, by default "lines+markers".
    figure : Optional[go.Figure], optional
        The figure object to add the scatter plot to, by default None.


    Returns
    -------
    go.Scatter
        The scatter plot object.
    """

    return go.Scatter(
        x=x,
        y=y,
        mode=mode,
    )


@fn.NodeDecorator("plotly.make_bar", name="Make Bar Plot")
def make_bar(
    y: List[float],
    x: Optional[List[float]] = None,
) -> go.Bar:
    """
    Create a bar plot with the given x and y values.

    Parameters
    ----------
    y : List[float]
        The y values of the bar plot.
    x : Optional[List[float]], optional
        The x values of the bar plot, by default None. If None, the x values will be the indices of the y values.

    Returns
    -------
    go.Bar
        The bar plot object.
    """

    return go.Bar(
        x=x,
        y=y,
    )
