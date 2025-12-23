from inspect import cleandoc
from typing import List


class Split:
    """
    Split a string into a list of strings
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
            "optional": {
                "separator": ("STRING", {"default": "\\n", "multiline": False}),
                "unescape": ("BOOLEAN", {"default": True}),
            },
        }


    RETURN_TYPES = ("STRING",)
    OUTPUT_IS_LIST = (True, )
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "split"
    CATEGORY = "Stringer"

    def split(self, string: str, separator: str, unescape: bool):
        if unescape:
            separator = bytes(separator, "utf-8").decode("unicode_escape")
        results = string.split(separator)
        return (results,)


class Join:
    """
    Join a list of strings into a single string
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "strings": ("STRING",),
            },
            "optional": {
                "separator": ("STRING", {"default": ", ", "multiline": False}),
                "unescape": ("BOOLEAN", {"default": False}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "join"
    CATEGORY = "Stringer"

    def join(self, strings: List[str], separator: List[str], unescape: List[bool]):
        unescape: bool = unescape[0]
        separator: str = separator[0]
        if unescape:
            separator = bytes(separator, "utf-8").decode("unicode_escape")
        return (separator.join(strings),)
    

class Dedup:
    """
    Remove duplicates from a list of strings
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "strings": ("STRING",),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    OUTPUT_IS_LIST = (True, )
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "dedup"
    CATEGORY = "Stringer"

    def dedup(self, strings: List[str]):
        return (list(set(strings)),)


class Sort:
    """
    Sort a list of strings
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "strings": ("STRING",),
            },
            "optional": {
                "reverse": ("BOOLEAN", {"default": False}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    OUTPUT_IS_LIST = (True, )
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "sort"
    CATEGORY = "Stringer"

    def sort(self, strings: List[str], reverse: List[bool]):
        reverse: bool = reverse[0]
        return (sorted(strings, reverse=reverse),)
    

class Reverse:
    """
    Reverse a list of strings
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "strings": ("STRING",),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    OUTPUT_IS_LIST = (True, )
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "reverse"
    CATEGORY = "Stringer"

    def reverse(self, strings: List[str]):
        return (strings[::-1],)
    

class Length:
    """
    Get the length of a string
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "strings": ("STRING",),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("INT",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "length"
    CATEGORY = "Stringer"

    def length(self, strings: List[str]):
        return (len(strings),)
    

class Substring:
    """
    Get a substring from a string
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
            "optional": {
                "start": ("INT", {"default": 0, "min": 0, "max": 10000}),
                "end": ("INT", {"default": 10000, "min": 0, "max": 10000}),
            },
        }

    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "substring"
    CATEGORY = "Stringer"

    def substring(self, string: str, start: int, end: int):
        return (string[start:end],)


class Upper:
    """
    Convert a string to uppercase
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "upper"
    CATEGORY = "Stringer"

    def upper(self, string: str):
        return (string.upper(),)


class Lower:
    """
    Convert a string to lowercase
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "lower"
    CATEGORY = "Stringer"

    def lower(self, string: str):
        return (string.lower(),)


class Capitalize:
    """
    Capitalize the first letter of a string
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "capitalize"
    CATEGORY = "Stringer"

    def capitalize(self, string: str):
        return (string.capitalize(),)
    

class Title:
    """
    Convert a string to title case
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "title"
    CATEGORY = "Stringer"

    def title(self, string: str):
        return (string.title(),)
    

class SwapCase:
    """
    Swap the case of a string
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "swap_case"
    CATEGORY = "Stringer"

    def swap_case(self, string: str):
        return (string.swapcase(),)
    

class Strip:
    """
    Strip whitespace from a string
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    DESCRIPTION = cleandoc(__doc__)
    FUNCTION = "strip"
    CATEGORY = "Stringer"

    def strip(self, string: str):
        return (string.strip(),)
