"""
@author: satetsu888
@title: test-custom-node
@nickname: test-custom-node
@description: This is a test custom node. It's a simple node that takes a string input and returns it as an output.
"""

from .nodes import TestCustomNode

NODE_CLASS_MAPPINGS = {
    "test-custom-node": TestCustomNode,
}

__all__ = [
    "NODE_CLASS_MAPPINGS",
]

print("\033[34mComfyUI test custom node: \033[92mLoaded\033[0m")