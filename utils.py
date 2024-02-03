import subprocess
import platform
from io import BytesIO
import tempfile
import pyautogui, pyperclip,time

def from_buffer(stream):
    """Read the buffer and return the data."""
    return stream

def from_path(path):
    """Read the file and return the data."""
    with open(path, 'rb') as stream:
        return from_buffer(BytesIO(stream.read()))

def _openChromePDF(stream):
    """Open the PDF in Chrome."""
    # Leitura dos dados do stream sem fechar o arquivo
    data = stream.read()
    if platform.system() == 'Windows':
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        command = [chrome_path, '-']
    elif platform.system() == 'Darwin':
        command = ['open', '-na', 'Google Chrome', '--args', '-']
    elif platform.system() == 'Linux':
        with tempfile.NamedTemporaryFile(suffix=".pdf",mode='wb') as temp:
            temp.write(data)
            temp.flush()
            command = ['xdg-open', temp.name]
            process = subprocess.run(command, input=data, check=True, capture_output=True)
            copy_text()
            print(process.stdout)
            print(process.stderr)
    else:
        raise NotImplementedError('Your OS is not supported.')

    if platform.system() != 'Linux':
        process = subprocess.run(command, input=data, check=True, capture_output=True)
        print(process.stdout)
        print(process.stderr)

def copy_text():
    # Ajuste as coordenadas conforme necessário para a posição do texto no PDF
    pyautogui.moveTo(500, 500)  # Ajuste as coordenadas conforme necessário
    pyautogui.click()

    # Seleciona todo o texto (Ctrl + A)
    pyautogui.hotkey('ctrl', 'a')

    # Copia o texto (Ctrl + C)
    pyautogui.hotkey('ctrl', 'c')

def paste_to_file(file_path):
    # Pausa para dar tempo de copiar o texto
    time.sleep(1)

    # Cola o texto em um arquivo
    pyautogui.hotkey('ctrl', 'v')

    # Salva o arquivo (Ctrl + S)
    pyautogui.hotkey('ctrl', 's')
    pyautogui.write(file_path)
    pyautogui.press('enter')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver
import time

# Iniciar o WebDriver do Selenium
driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')

# URL do PDF ou link para um arquivo PDF
url_pdf = 'file:///home/lordwaif/PyJPDF/teste2.pdf'

# Navegar até o link do PDF
driver.get(url_pdf)

# Esperar alguns segundos para garantir que o PDF seja carregado
time.sleep(5)

# Fechar o navegador
driver.quit()


if __name__ == '__main__':
    #_openChromePDF(from_path('teste.pdf'))
    #paste_to_file('teste.txt')
    ...

