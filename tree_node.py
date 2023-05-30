from dataclasses import dataclass, field
import json
from typing import Any


@dataclass
class TreeNode:
    op: str
    args: list[Any]
    scope: list[str] = field(default_factory=lambda:['globals'])

    def toJSON(self):
        return str(json.dumps(self, default=lambda o: o.__dict__, indent=4))

    def __repr__(self) -> str:
        return self.toJSON()
