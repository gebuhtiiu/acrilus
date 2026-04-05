from models import FileRecord


class AcrilusEngine:
    def __init__(self) -> None:
        self.files: list[FileRecord] = []

    def add_file(self, record: FileRecord) -> None:
        self.files.append(record)

    def search_by_entity(self, entity: str) -> list[FileRecord]:
        term = entity.lower().strip()
        return [r for r in self.files if (r.entity or "").lower() == term]


if __name__ == "__main__":
    engine = AcrilusEngine()
    engine.add_file(
        FileRecord(
            file_name="Invoice - Internet Service - Comcast - 2026-03.pdf",
            file_path="/Financial/Reference/Invoice - Internet Service - Comcast - 2026-03.pdf",
            category="Financial",
            document_type="Invoice",
            entity="Comcast",
            lifecycle_state="Reference",
        )
    )
    print(engine.search_by_entity("Comcast"))
