import os
import subprocess
import logging

class DocumentConverter:
    """Classe responsável por buscar e converter documentos para PDF."""

    def __init__(self, input_directory, output_directory=None):
        """
        Inicializa o conversor.
        
        :param input_directory: Diretório onde os arquivos de entrada estão localizados.
        :param output_directory: Diretório onde os arquivos convertidos serão salvos.
                                Se não informado, usa o mesmo diretório de entrada.
        """
        self.input_directory = input_directory
        self.output_directory = output_directory if output_directory else input_directory
        self.supported_formats = ['.doc', '.docx', '.odt']

    def get_files(self):
        """
        Percorre recursivamente o diretório de entrada e retorna a lista de arquivos suportados.
        
        :return: Lista com os caminhos dos arquivos a serem convertidos.
        """
        files = []
        for root, _, filenames in os.walk(self.input_directory):
            for filename in filenames:
                if any(filename.lower().endswith(ext) for ext in self.supported_formats):
                    files.append(os.path.join(root, filename))
        return files

    def convert_file(self, filepath):
        """
        Converte um arquivo para PDF utilizando o LibreOffice em modo headless.
        
        :param filepath: Caminho completo do arquivo a ser convertido.
        """
        command = [
            'libreoffice',
            '--headless',
            '--convert-to', 'pdf',
            filepath,
            '--outdir', self.output_directory
        ]
        try:
            logging.info("Converting: %s", filepath)
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            logging.info("Converted successfully: %s", filepath)
        except subprocess.CalledProcessError as e:
            error_msg = e.stderr.decode('utf-8').strip()
            logging.error("Error converting %s: %s", filepath, error_msg)

    def convert_all(self):
        """
        Busca todos os arquivos suportados e realiza a conversão para cada um.
        """
        files = self.get_files()
        for filepath in files:
            self.convert_file(filepath)
