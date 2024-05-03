from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def verProceso(res = 0):
    while(res == 0):
        proceso = input('\nVer proceso S/N: ').upper()
        
        if(proceso == 'S'):
            res = 1
        if(proceso == 'N'):
            res = 2
    return res

# Ocultar Navegador
def sinNav():
    chromeOptions = Options()
    chromeOptions.add_argument('--headless')
    # Abrir Navegador
    driver = webdriver.Chrome(chromeOptions)
    # Abrir Pagina web
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    return driver
# Mostrar Navegador
def conNav():
     # Abrir Navegador
    driver = webdriver.Chrome()
    # Abrir Pagina web
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")   
    return driver