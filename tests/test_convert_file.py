import subprocess
import logging
import pytest
from docs_to_pdf.converter import DocumentConverter

def fake_run_success(command, stdout, stderr, check):
    return subprocess.CompletedProcess(args=command, returncode=0)

def fake_run_failure(command, stdout, stderr, check):
    raise subprocess.CalledProcessError(returncode=1, cmd=command, stderr=b"Fake error")

def test_convert_file_success(monkeypatch, caplog):
    converter = DocumentConverter("dummy_input", "dummy_output")
    monkeypatch.setattr(subprocess, "run", fake_run_success)
    caplog.set_level(logging.INFO)
    
    converter.convert_file("dummy_file.doc")
    assert "Converted successfully" in caplog.text

def test_convert_file_failure(monkeypatch, caplog):
    converter = DocumentConverter("dummy_input", "dummy_output")
    monkeypatch.setattr(subprocess, "run", fake_run_failure)
    caplog.set_level(logging.INFO)
    
    converter.convert_file("dummy_file.doc")
    assert "Error converting" in caplog.text
