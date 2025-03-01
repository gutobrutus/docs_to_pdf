import os
import tempfile
import pytest
from docs_to_pdf.converter import DocumentConverter

def test_get_files(tmp_path):
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    file1 = subdir / "test.doc"
    file1.write_text("dummy content")
    file2 = subdir / "test.txt"
    file2.write_text("dummy content")
    
    converter = DocumentConverter(str(tmp_path))
    files = converter.get_files()
    
    assert any("test.doc" in f for f in files)
    assert not any("test.txt" in f for f in files)
