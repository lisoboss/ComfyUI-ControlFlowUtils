from .nodes import (
    flow,
    stringer,
)


NODES = [
    ## Flow
    # flow.ForEach,
    flow.SwitchCombo,

    ## Stringer
    stringer.ToString,
    stringer.Split,
    stringer.Join,
    stringer.Dedup,
    stringer.Sort,
    stringer.Reverse,
    stringer.Length,
    stringer.Substring,
    stringer.Upper,
    stringer.Lower,
    stringer.Capitalize,
    stringer.Title,
    stringer.SwapCase,
    stringer.Strip,
]

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {f'{node.CATEGORY} {node.__name__}': node for node in NODES}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {}
