import unittest
import os
import pickle
from selenium import webdriver
from pages.login_page import LoginPage

SESSION_FILE = "session.pkl"


class TestLogin(unittest.TestCase):
    def setUp(self):
        # Inicializar o WebDriver
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)

    # TODO: Comentei temporariamente esta linha:
    # TODO: lembrar de descomentar ao finalizar o projeto
    # TODO: Função fecha automaticamente o navegador
    # def tearDown(self):
    #     self.driver.quit()

    def save_session(self):
        """Salva os cookies da sessão."""
        with open(SESSION_FILE, "wb") as file:
            pickle.dump(self.driver.get_cookies(), file)

    def load_session(self):
        """Carrega os cookies da sessão."""
        if os.path.exists(SESSION_FILE):
            with open(SESSION_FILE, "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)

    def test_login(self):
        """Teste para login com reutilização de sessão."""
        self.login_page.go_to_login_page()

        # Verificar se há uma sessão salva
        if os.path.exists(SESSION_FILE):
            print("Carregando sessão existente...")
            self.load_session()
            self.driver.refresh()
        else:
            print("Sessão não encontrada. Realizando login...")
            self.login_page.login()
            self.save_session()

        # Verificar se o usuário está logado (exemplo)
        self.assertIn(
            "Instagram", 
            self.driver.title, 
            "Login não foi realizado com sucesso."
        )
