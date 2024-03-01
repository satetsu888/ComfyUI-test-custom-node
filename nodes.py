
class TestCustomNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "name": ("STRING", {"default": "Test Custom Node"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("name",)
    FUNCTION = "run"
    OUTPUT_NODE = False

    CATEGORY = "sample_node"

    def run(self, name):
        return (name,)
