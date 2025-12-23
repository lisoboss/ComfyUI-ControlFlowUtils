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
