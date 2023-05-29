from dataclasses import dataclass
import json
from typing import Any


@dataclass
class TreeNode:
    op: str
    args: list[Any]

    def toJSON(self):
        return str(json.dumps(self, default=lambda o: o.__dict__, indent=4))

    def __repr__(self) -> str:
        return self.toJSON()
