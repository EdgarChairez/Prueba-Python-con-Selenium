from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from funciones import *
import time

# Pide usuario y contraseña
user = input("Usuario: ")
pas = input("Contraseña: ")

res = verProceso()

if(res==1):
   # Funcion para mostrar navegador
   driver = conNav()
else:
   # Funcion para no mostrar navegador
   driver = sinNav()

# Obtener Titulo de la Pagina
print('INICIA EL PROCESO')
title = driver.title
print('Ingresa a la pagina: ' + title)

# Se ingresa Usuario
usuario = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
usuario.send_keys(user)
# Se ingresa Contraseña
contrasenia = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@type,'password')]")))
contrasenia.send_keys(pas)
# Click Boton 'Iniciar Sesion'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# Valida se ingrese Usuario y Contraseña
try: 
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(.,'Required')])")))
    try: # Valida se ingrese Usuario
       WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span")))
       print('*Usuario Requerido')
    except:
       print('Ingreso Usuario')
    try: # Valida se ingrese Contraseña
       WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span")))
       print('*Contraseña Requerida')
    except:
       print('Ingreso Contraseña')
except:
    try:
        ingresa = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(//div[contains(.,'Invalid credentials')])[9]")))
        print('Credenciales Incorrectas')
    except:
        print('-Ingresa al Sistema')


time.sleep(0.5)     # Esperar (Segundos)
print('FINALIZA EL PROCESO')
driver.quit()       # Salir del Navegador