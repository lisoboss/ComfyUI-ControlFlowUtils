from .nodes import *



NODES = [
    ## Flow
    # ForEach,

    ## Stringer
    Split,
    Join,
    Dedup,
    Sort,
    Reverse,
    Length,
    Substring,
    Upper,
    Lower,
    Capitalize,
    Title,
    SwapCase,
    Strip,
]

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {f'{node.CATEGORY} {node.__name__}': node for node in NODES}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {}
