from inspect import cleandoc


class ForEach:

    """
    for each string in string_list
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "items": ("*",),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("*",)
    OUTPUT_IS_LIST = (True, )
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "for_each"
    CATEGORY = "Flow"

    def for_each(self, items): 
        return (items,)


class SwitchCombo:
    """
    Simple switch combo node:
    - Outputs a boolean based on the selected value ("yes" / "no")
    - Returns the corresponding branch value (yes_value / no_value)
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "value": (["no","yes"], {"default": "yes"}),
            },
            "optional": {
                "yes_value": ("STRING", {"default": "yes"}),
                "no_value": ("STRING", {"default": "no"}),
            },
        }

    RETURN_TYPES = ("BOOLEAN", "*",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "switch"
    CATEGORY = "Flow"

    def switch(self, value: str, yes_value: str, no_value: str):
        if value == "yes":
            return (True, [yes_value])
        else:
            return (False, [no_value])
