import typer
import logging
from docs_to_pdf.converter import DocumentConverter

app = typer.Typer(help="Conversor de arquivos DOC, DOCX e ODT para PDF.")

def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@app.command()
def convert(
    input_directory: str = typer.Argument(..., help="Diretório com os arquivos a converter."),
    output_directory: str = typer.Option(None, help="Diretório para os PDFs convertidos. Se omitido, usa o diretório de entrada.")
):
    setup_logging()
    converter = DocumentConverter(input_directory, output_directory)
    converter.convert_all()

if __name__ == "__main__":
    app()
