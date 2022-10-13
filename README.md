# SeleniumPHPTravelsGrupo7
Repositorio del Grupo 7, que contiene el webdriver de chrome, asi como archivos de python para realizar distintas pruebas
Instalación de Selenium Web driver en MacOS.

# MacOS

## Requisitos

Primero, debemos instalar Python3.
Para iniciar la instalación de Python3, debemos de instalar un administrador de paquetes utilizado en MacOS el cual se llama Brew. Para instalarlo debemos de abrir una terminal o consola en nuestra computadora.
Seguido a esto debemos ejecutar el siguiente comando, el cual descargara e instalara Brew:
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
Una vez tengamos instalado Brew, procederemos a ejecutar el siguiente comando, el cual instalara Python3.
`brew install python3`

## Instalación de Selenium

Una vez tengamos instalados los requisitos, deberemos descargar Selenium mediante el siguiente comando:
`curl https://files.pythonhosted.org/packages/ed/9c/9030520bf6ff0b4c98988448a93c04fcbd5b13cd9520074d8ed53569ccfe/selenium-3.141.0.tar.gz > selenium.tar.gz`
Luego ejecutamos los siguientes comandos para empezar la instalacion:
`tar -xzvf selenium.tar.gz`
`cd selenium-version#`
`python3 setup.py install`

Una vez termina el proceso de instalación, deberíamos de ser capaces de utilizar selenium.
Para comprobarlo, solo basta con abrir una terminal de Python, lo cual se hace corriendo el comando python3, dentro de una terminal del sistema, y luego ejecutamos esta línea o comando:
`Import Selenium`

En el caso de una instalación correcta, no deberíamos de tener ningún mensaje de error. 

# Instalación de Selenium Web driver en Windows

## Requisitos
Para Windows, debemos de tener instalado Python3, en el caso de no tenerlo, existen varias maneras de instalarlo, ya sea desde la página principal de Python3 o Mediante el Store de Microsoft, etc.…
En este caso utilizaremos el Store de Microsoft.
 


Una vez tenemos instalado Python, podemos empezar con el proceso de instalación de Selenium.
Ejecutando el siguiente comando: 
` python -m pip install selenium`

Y esperamos a que el proceso de instalación termine.

El siguiente paso, es instalar los Web drivers, para esto descargaremos una herramienta que se llama ChromeDriver, buscando la versión que utiliza nuestro sistema operativo dentro del repositorio de ChromeDriver:
` ChromeDriver - WebDriver for Chrome - Downloads (chromium.org)`
Extraemos el contenido del archivo descargado utilizando alguna herramienta como WinRAR:
 
Ahora abrimos las variables de ambiente, y dentro de la variable Path, del sistema, agregamos la ruta del chromedriver.exe:
 
Una vez tenemos esto listo, nuestro ambiente de Selenium estará instalado correctamente.

Para lo siguiente estaremos creando un archivo con el nombre “test.py”.
Y escribiremos el siguiente codigo para probar el funcionamiento.
`
# Programa de Python
# Importamos  el web driver de selenium
from selenium import webdriver

driver = webdriver.Chrome()
# Le decimos al driver que abra la url de Google.
driver.get("https://phptravels.com/demo")
`

Luego, abrimos una terminal de CMD, y ejecutamos el comando:
`python test.py`

El cual despues de unos segundos, abrira una instancia de chrome, con la pagina de Google y un mensaje que nos notifica que un software de testing esta controlando chrome.
 

Para efectos de nuestro proyecto, estaremos utilizando la página de PHPTravels “https://phptravels.com/demo” 

Por lo cual al realizar el cambio abrirá la página de PHP Travels Demo.

 
