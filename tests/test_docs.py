def test_docs_use_api():
    import os

    files_to_check = []
    for root, _, files in os.walk("../docs"):
        files_to_check.extend(
            os.path.join(root, f) for f in files if f.endswith(".rst")
        )
    pattern = r"(from|import) kartothek\.(?!(api))"
    for file_ in files_to_check:
        with open(file_) as fd:
            content = fd.read()

        import re

        if re.search(pattern, content):
            raise AssertionError(f"Found non-api import in document {file_}")
