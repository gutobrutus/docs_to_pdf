import pytest
from docs_to_pdf.converter import DocumentConverter

def test_convert_all(monkeypatch):
    # Lista de arquivos simulados a serem convertidos.
    dummy_files = ["file1.doc", "file2.odt", "file3.docx"]

    converter = DocumentConverter("dummy_input", "dummy_output")

    # Substitui o método get_files para retornar a lista simulada.
    monkeypatch.setattr(converter, "get_files", lambda: dummy_files)

    # Lista para registrar os arquivos que o método convert_file foi chamado.
    called_files = []

    def fake_convert_file(filepath):
        called_files.append(filepath)

    # Substitui o método convert_file pelo fake que registra os arquivos.
    monkeypatch.setattr(converter, "convert_file", fake_convert_file)

    # Executa o método que deve iterar sobre todos os arquivos e chamar convert_file.
    converter.convert_all()

    # Verifica se o convert_file foi chamado para cada arquivo na lista dummy.
    assert called_files == dummy_files
