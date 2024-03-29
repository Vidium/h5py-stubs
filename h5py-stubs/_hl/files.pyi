from typing import Any

from .group import Group

class File(Group):
    def close(self) -> None: ...
    def __enter__(self) -> File: ...
    def __exit__(self, *args: Any) -> None: ...
    @property
    def filename(self) -> str: ...
    def flush(self) -> None: ...
