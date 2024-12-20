import os
from dotenv import load_dotenv
import chromedriver_autoinstaller

# Carregar variáveis do arquivo .env
load_dotenv()

# Instalar automaticamente a versão correta do ChromeDriver
chromedriver_autoinstaller.install()

# Configurações globais
INSTAGRAM_URL = "https://www.instagram.com"
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
USERNAMESEARCH = os.getenv("INSTAGRAM_USERNAMESEARCH")