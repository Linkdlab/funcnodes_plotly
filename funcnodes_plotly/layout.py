import funcnodes as fn
import plotly.graph_objects as go


class UpdateAxisLayout(fn.Node):
    figure = fn.NodeInput(id="figure", description="The figure object.", type=go.Figure)

    axis = fn.NodeInput(id="axis", description="The axis to update.", type=str)

    title = fn.NodeInput(
        id="title", description="The title of the axis.", type=str, default=None
    )

    async def run(self, figure: go.Figure, axis: str, title: str):
        available_axes = figure
