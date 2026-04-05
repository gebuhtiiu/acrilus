from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Tag:
    name: str


@dataclass
class FileRecord:
    file_name: str
    file_path: str
    category: Optional[str] = None
    document_type: Optional[str] = None
    entity: Optional[str] = None
    lifecycle_state: str = "Inbox"
    tags: List[Tag] = field(default_factory=list)
    note_link: Optional[str] = None
