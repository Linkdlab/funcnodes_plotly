import plotly.express as px

from typing import Optional, Literal

import funcnodes as fn
import plotly.graph_objects as go

import pandas as pd
import numpy as np

from .colors import ContinousColorScales


@fn.NodeDecorator(
    "plotly.express.scatter",
    name="Scatter Plot",
    description="Create a scatter plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def scatter(
    data: pd.DataFrame,
    x: str,
    y: str,
    color: Optional[str] = None,
    size: Optional[str] = None,
    symbol: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a scatter plot.
    """
    return px.scatter(
        data,
        x=x,
        y=y,
        color=color,
        size=size,
        symbol=symbol,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.line",
    name="Line Plot",
    description="Create a line plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def line(
    data: pd.DataFrame,
    x: str,
    y: str,
    color: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a line plot.
    """
    return px.line(
        data,
        x=x,
        y=y,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.bar",
    name="Bar Plot",
    description="Create a bar plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def bar(
    data: pd.DataFrame,
    x: str,
    y: str,
    color: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a bar plot.
    """
    return px.bar(
        data,
        x=x,
        y=y,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.area",
    name="Area Plot",
    description="Create an area plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def area(
    data: pd.DataFrame,
    x: str,
    y: str,
    color: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create an area plot.
    """
    return px.area(
        data,
        x=x,
        y=y,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.funnel",
    name="Funnel Plot",
    description="Create a funnel plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def funnel(
    data: pd.DataFrame,
    x: str,
    y: str,
    color: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a funnel plot.
    """
    return px.funnel(
        data,
        x=x,
        y=y,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.timeline",
    name="Timeline Plot",
    description="Create a timeline plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def timeline(
    data: pd.DataFrame,
    x_start: str,
    x_end: str,
    y: str,
    color: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a timeline plot.
    """
    return px.timeline(
        data,
        x_start=x_start,
        x_end=x_end,
        y=y,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.pie",
    name="Pie Chart",
    description="Create a pie chart.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def pie(
    data: pd.DataFrame,
    names: str,
    values: str,
    color: Optional[str] = None,
    hole: float = 0,
) -> go.Figure:
    """
    Create a pie chart.
    """
    return px.pie(
        data,
        names=names,
        values=values,
        color=color,
        hole=hole,
    )


@fn.NodeDecorator(
    "plotly.express.sunburst",
    name="Sunburst Chart",
    description="Create a sunburst chart.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def sunburst(
    data: pd.DataFrame,
    names: str,
    values: str,
    parents: str,
    color: Optional[str] = None,
) -> go.Figure:
    """
    Create a sunburst chart.
    """
    return px.sunburst(
        data,
        names=names,
        values=values,
        parents=parents,
        color=color,
    )


@fn.NodeDecorator(
    "plotly.express.treemap",
    name="Treemap",
    description="Create a treemap.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def treemap(
    data: pd.DataFrame,
    names: str,
    values: str,
    parents: str,
    color: Optional[str] = None,
) -> go.Figure:
    """
    Create a treemap.
    """

    return px.treemap(
        data,
        names=names,
        values=values,
        parents=parents,
        color=color,
    )


@fn.NodeDecorator(
    "plotly.express.icicle",
    name="Icicle Plot",
    description="Create an icicle plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def icicle(
    data: pd.DataFrame,
    names: str,
    values: str,
    parents: str,
    color: Optional[str] = None,
) -> go.Figure:
    """
    Create an icicle plot.
    """
    return px.icicle(
        data,
        names=names,
        values=values,
        parents=parents,
        color=color,
    )


@fn.NodeDecorator(
    "plotly.express.funnel_area",
    name="Funnel Area Plot",
    description="Create a funnel area plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def funnel_area(
    data: pd.DataFrame,
    names: str,
    values: str,
    color: Optional[str] = None,
) -> go.Figure:
    """
    Create a funnel area plot.
    """
    return px.funnel_area(
        data,
        names=names,
        values=values,
        color=color,
    )


@fn.NodeDecorator(
    "plotly.express.histogram",
    name="Histogram",
    description="Create a histogram.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def histogram(
    data: pd.DataFrame,
    x: str,
    color: Optional[str] = None,
    pattern_shape: Optional[str] = None,
    barmode: Literal[
        "group",
        "overlay",
        "relative",
    ] = "group",
    marginal: Literal[
        None,
        "rug",
        "box",
        "violin",
    ] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a histogram.
    """
    if marginal not in ["rug", "box", "violin"]:
        marginal = None
    return px.histogram(
        data,
        x=x,
        color=color,
        pattern_shape=pattern_shape,
        barmode=barmode,
        marginal=marginal,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.box",
    name="Box Plot",
    description="Create a box plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def box(
    data: pd.DataFrame,
    x: str,
    y: str,
    color: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a box plot.
    """
    return px.box(
        data,
        x=x,
        y=y,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.violin",
    name="Violin Plot",
    description="Create a violin plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def violin(
    data: pd.DataFrame,
    x: str,
    y: str,
    color: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a violin plot.
    """
    return px.violin(
        data,
        x=x,
        y=y,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.strip",
    name="Strip Plot",
    description="Create a strip plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def strip(
    data: pd.DataFrame,
    x: str,
    y: str,
    color: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a strip plot.
    """
    return px.strip(
        data,
        x=x,
        y=y,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.ecdf",
    name="ECDF Plot",
    description="Create an ECDF plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def ecdf(
    data: pd.DataFrame,
    x: str,
    color: Optional[str] = None,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create an ECDF plot.
    """
    return px.ecdf(
        data,
        x=x,
        color=color,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.density_heatmap",
    name="Density Heatmap",
    description="Create a density heatmap.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def density_heatmap(
    data: pd.DataFrame,
    x: str,
    y: str,
    z: str,
    color_continuous_scale: ContinousColorScales = ContinousColorScales.rdbu,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a density heatmap.
    """
    color_continuous_scale = ContinousColorScales.v(color_continuous_scale)
    return px.density_heatmap(
        data,
        x=x,
        y=y,
        z=z,
        color_continuous_scale=color_continuous_scale,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.density_contour",
    name="Density Contour",
    description="Create a density contour plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def density_contour(
    data: pd.DataFrame,
    x: str,
    y: str,
    color_continuous_scale: ContinousColorScales = ContinousColorScales.rdbu,
    facet_row: Optional[str] = None,
    facet_col: Optional[str] = None,
    facet_col_wrap: Optional[int] = None,
) -> go.Figure:
    """
    Create a density contour plot.
    """
    color_continuous_scale = ContinousColorScales.v(color_continuous_scale)
    return px.density_contour(
        data,
        x=x,
        y=y,
        color_discrete_sequence=color_continuous_scale,
        facet_row=facet_row,
        facet_col=facet_col,
        facet_col_wrap=facet_col_wrap,
    )


@fn.NodeDecorator(
    "plotly.express.imshow",
    name="Image Plot",
    description="Create an image plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def imshow(
    data: np.ndarray,
    scale: ContinousColorScales = ContinousColorScales.rdbu,
    scale_midpoint: Optional[float] = None,
    value_text: bool = False,
) -> go.Figure:
    """
    Create an image plot.
    """
    color_continuous_scale = ContinousColorScales.v(scale)
    if value_text:
        # show values in scientific notation
        value_text = ".2e"

    return px.imshow(
        data,
        color_continuous_scale=color_continuous_scale,
        color_continuous_midpoint=scale_midpoint,
        text_auto=value_text,
    )


@fn.NodeDecorator(
    "plotly.express.scatter_3d",
    name="3D Scatter Plot",
    description="Create a 3D scatter plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def scatter_3d(
    data: pd.DataFrame,
    x: str,
    y: str,
    z: str,
    color: Optional[str] = None,
    symbol: Optional[str] = None,
) -> go.Figure:
    """
    Create a 3D scatter plot.
    """
    return px.scatter_3d(
        data,
        x=x,
        y=y,
        z=z,
        color=color,
        symbol=symbol,
    )


@fn.NodeDecorator(
    "plotly.express.line_3d",
    name="3D Line Plot",
    description="Create a 3D line plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def line_3d(
    data: pd.DataFrame,
    x: str,
    y: str,
    z: str,
    color: Optional[str] = None,
) -> go.Figure:
    """
    Create a 3D line plot.
    """
    return px.line_3d(
        data,
        x=x,
        y=y,
        z=z,
        color=color,
    )


@fn.NodeDecorator(
    "plotly.express.scatter_matrix",
    name="Scatter Matrix",
    description="Create a scatter matrix.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def scatter_matrix(
    data: pd.DataFrame,
    dimensions: Optional[str] = None,
    color: Optional[str] = None,
) -> go.Figure:
    """
    Create a scatter matrix.
    """
    if dimensions is not None:
        dimensions_list = [s.strip() for s in dimensions.split(",")]
    else:
        dimensions_list = list(data.columns)

    if color is not None:
        if color in dimensions_list:
            dimensions_list.remove(color)

    return px.scatter_matrix(
        data,
        dimensions=dimensions_list,
        color=color,
    )


@fn.NodeDecorator(
    "plotly.express.parallel_coordinates",
    name="Parallel Coordinates",
    description="Create a parallel coordinates plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def parallel_coordinates(
    data: pd.DataFrame,
    color: str,
    dimensions: Optional[str] = None,
    color_continuous_scale: ContinousColorScales = ContinousColorScales.rdbu,
    color_continuous_midpoint: Optional[float] = None,
) -> go.Figure:
    """
    Create a parallel coordinates plot.
    """
    if dimensions is not None:
        dimensions_list = [s.strip() for s in dimensions.split(",")]
    else:
        dimensions_list = list(data.columns)

    color_continuous_scale = ContinousColorScales.v(color_continuous_scale)

    return px.parallel_coordinates(
        data,
        color=color,
        dimensions=dimensions_list,
        color_continuous_scale=color_continuous_scale,
        color_continuous_midpoint=color_continuous_midpoint,
    )


@fn.NodeDecorator(
    "plotly.express.parallel_categories",
    name="Parallel Categories",
    description="Create a parallel categories plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def parallel_categories(
    data: pd.DataFrame,
    dimensions: Optional[str] = None,
    color: Optional[str] = None,
    color_continuous_scale: ContinousColorScales = ContinousColorScales.rdbu,
    color_continuous_midpoint: Optional[float] = None,
) -> go.Figure:
    """
    Create a parallel categories plot.
    """
    if dimensions is not None:
        dimensions_list = [s.strip() for s in dimensions.split(",")]
    else:
        dimensions_list = list(data.columns)

    color_continuous_scale = ContinousColorScales.v(color_continuous_scale)

    return px.parallel_categories(
        data,
        dimensions=dimensions_list,
        color=color,
        color_continuous_scale=color_continuous_scale,
        color_continuous_midpoint=color_continuous_midpoint,
    )


@fn.NodeDecorator(
    "plotly.express.scatter_polar",
    name="Polar Scatter Plot",
    description="Create a polar scatter plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def scatter_polar(
    data: pd.DataFrame,
    r: str,
    theta: str,
    color: Optional[str] = None,
    symbol: Optional[str] = None,
) -> go.Figure:
    """
    Create a polar scatter plot.
    """
    return px.scatter_polar(
        data,
        r=r,
        theta=theta,
        color=color,
        symbol=symbol,
    )


@fn.NodeDecorator(
    "plotly.express.line_polar",
    name="Polar Line Plot",
    description="Create a polar line plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def line_polar(
    data: pd.DataFrame,
    r: str,
    theta: str,
    color: Optional[str] = None,
) -> go.Figure:
    """
    Create a polar line plot.
    """
    return px.line_polar(
        data,
        r=r,
        theta=theta,
        color=color,
    )


@fn.NodeDecorator(
    "plotly.express.bar_polar",
    name="Polar Bar Plot",
    description="Create a polar bar plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def bar_polar(
    data: pd.DataFrame,
    r: str,
    theta: str,
    color: Optional[str] = None,
    color_discrete_sequence: ContinousColorScales = ContinousColorScales.rdbu,
) -> go.Figure:
    """
    Create a polar bar plot.
    """
    color_discrete_sequence = ContinousColorScales.v(color_discrete_sequence)
    return px.bar_polar(
        data,
        r=r,
        theta=theta,
        color=color,
        color_discrete_sequence=color_discrete_sequence,
    )


@fn.NodeDecorator(
    "plotly.express.scatter_ternary",
    name="Ternary Scatter Plot",
    description="Create a ternary scatter plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def scatter_ternary(
    data: pd.DataFrame,
    a: str,
    b: str,
    c: str,
    color: Optional[str] = None,
    symbol: Optional[str] = None,
) -> go.Figure:
    """
    Create a ternary scatter plot.
    """
    return px.scatter_ternary(
        data,
        a=a,
        b=b,
        c=c,
        color=color,
        symbol=symbol,
    )


@fn.NodeDecorator(
    "plotly.express.line_ternary",
    name="Ternary Line Plot",
    description="Create a ternary line plot.",
    default_render_options={"data": {"src": "figure"}},
    outputs=[
        {"name": "figure"},
    ],
)
def line_ternary(
    data: pd.DataFrame,
    a: str,
    b: str,
    c: str,
    color: Optional[str] = None,
) -> go.Figure:
    """
    Create a ternary line plot.
    """
    return px.line_ternary(
        data,
        a=a,
        b=b,
        c=c,
        color=color,
    )


BASIC_SHELF = fn.Shelf(
    nodes=[
        scatter,
        line,
        bar,
        area,
        funnel,
        timeline,
    ],
    name="Basic",
    description="Basic plot types.",
    subshelves=[],
)

PART_OF_WHOLE_SHELF = fn.Shelf(
    nodes=[
        pie,
        sunburst,
        treemap,
        icicle,
        funnel_area,
    ],
    name="Part-of-Whole",
    description="Part-of-whole plot types.",
    subshelves=[],
)

DISTRIBUTION_1D_SHELF = fn.Shelf(
    nodes=[
        histogram,
        box,
        violin,
        strip,
        ecdf,
    ],
    name="1D Distributions",
    description="1D distribution plot types.",
    subshelves=[],
)

DISTRIBUTION_2D_SHELF = fn.Shelf(
    nodes=[
        density_heatmap,
        density_contour,
    ],
    name="2D Distributions",
    description="2D distribution plot types.",
    subshelves=[],
)

MATRIX_IMAGE_SHELF = fn.Shelf(
    nodes=[
        imshow,
    ],
    name="Matrix or Image",
    description="Matrix or image input plot types.",
    subshelves=[],
)

THREE_DIMENSIONAL_SHELF = fn.Shelf(
    nodes=[
        scatter_3d,
        line_3d,
    ],
    name="3-Dimensional",
    description="3D plot types.",
    subshelves=[],
)

MULTIDIMENSIONAL_SHELF = fn.Shelf(
    nodes=[
        scatter_matrix,
        parallel_coordinates,
        parallel_categories,
    ],
    name="Multidimensional",
    description="Multidimensional plot types.",
    subshelves=[],
)

POLAR_SHELF = fn.Shelf(
    nodes=[
        scatter_polar,
        line_polar,
        bar_polar,
    ],
    name="Polar Charts",
    description="Polar plot types.",
    subshelves=[],
)

TERNARY_SHELF = fn.Shelf(
    nodes=[
        scatter_ternary,
        line_ternary,
    ],
    name="Ternary Charts",
    description="Ternary plot types.",
    subshelves=[],
)

NODE_SHELF = fn.Shelf(
    nodes=[],
    name="Plotly Express",
    description="A collection of functions for creating plotly express plots.",
    subshelves=[
        BASIC_SHELF,
        PART_OF_WHOLE_SHELF,
        DISTRIBUTION_1D_SHELF,
        DISTRIBUTION_2D_SHELF,
        MATRIX_IMAGE_SHELF,
        THREE_DIMENSIONAL_SHELF,
        MULTIDIMENSIONAL_SHELF,
        POLAR_SHELF,
        TERNARY_SHELF,
    ],
)
