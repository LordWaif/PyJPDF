import subprocess
import platform,os
from io import BytesIO
import tempfile
import pyperclip
import time,requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile,os

def convertPDF(pdf_path_input, pdf_path_output = None,max_tries=3,executable_path=None,options_list=[],time_beetwen_tries=1,encoding='utf-8'):
    """
    Converts a PDF file to text using a headless Chrome browser.

    Args:
        pdf_path_input (str): The path to the input PDF file.
        pdf_path_output (str, optional): The path to save the output text file. If not provided, the text will be returned as a string. Defaults to None.
        max_tries (int, optional): The maximum number of tries to copy the text from the PDF. Defaults to 3.
        executable_path (str, optional): The path to the ChromeDriver executable. If not provided, the default ChromeDriver will be used. Defaults to None.
        options_list (list, optional): Additional options to pass to the Chrome browser. Defaults to [].
        time_beetwen_tries (int, optional): The time to wait between each try to copy the text. Defaults to 1.
        encoding (str, optional): The encoding to use when saving the output text file. Defaults to 'utf-8'.

    Returns:
        str: The extracted text from the PDF file, if pdf_path_output is not provided.

    Raises:
        Exception: If the text cannot be extracted from the PDF file after the maximum number of tries.
    """
    options = webdriver.ChromeOptions() 
    for i in options_list:
        options.add_argument(i)
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    options.add_argument("--window-size=50,50")
    if executable_path is None:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    else:
        driver = webdriver.Chrome(executable_path=executable_path, options=options)
    # Obatain absolute path
    pdf_path_input = os.path.abspath(pdf_path_input)
    driver.get('file:///'+pdf_path_input)
    driver.minimize_window()

    chrome_version = driver.capabilities['chrome']['chromedriverVersion']
    # print(f"Versão do ChromeDriver: {chrome_version}")
 
    embed_elemento = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'embed'))
    )
    driver.execute_script("arguments[0].click();", embed_elemento)

    texto_copiado = 'Não copiei nada'
    pyperclip.copy('Não copiei nada')
    max_tries = 3
    while True:
        webdriver.ActionChains(driver).move_to_element(embed_elemento).click().perform()

        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

        texto_copiado = pyperclip.paste()

        if texto_copiado == 'Não copiei nada':
            time.sleep(time_beetwen_tries)
        else:
            break
        max_tries -= 1
        if max_tries == 0:
            raise Exception('Não foi possível obter o texto do PDF')
    if pdf_path_output is None:
        return texto_copiado
    else:
        with open(pdf_path_output, 'w', encoding=encoding) as f:
            f.write(texto_copiado)
    driver.quit()

def from_buffer(stream,*args, **kwargs):
    """
    Read the buffer and return the data.

    Parameters:
    - stream: The buffer to read from.

    Returns:
    - pdf_content: The content of the PDF file.
    """
    # Criar tempfile
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(stream.read())
        temp_path = temp.name
    pdf_content = convertPDF(temp_path,*args, **kwargs)
    os.remove(temp_path)
    return pdf_content

def from_path(path,*args, **kwargs):
    """
    Read the file from the given path and return the data.

    Args:
        path (str): The path to the file.

    Returns:
        The data read from the file.
    """
    return convertPDF(path,*args, **kwargs)

def from_url(url,*args, **kwargs):
    """
    Read the file from the given URL and return the data.

    Parameters:
    url (str): The URL of the file to be read.
    *args: Additional positional arguments to be passed to the `from_buffer` function.
    **kwargs: Additional keyword arguments to be passed to the `from_buffer` function.

    Returns:
    The data read from the file.
    """
    response = requests.get(url)
    return from_buffer(BytesIO(response.content),*args, **kwargs)

if __name__ == '__main__':
    path = 'C:/Users/bibil/Documents/PyJPDF/teste2.pdf'
    import io
    from_buffer(io.BytesIO(open(path, 'rb').read()),'teste_saida.txt')