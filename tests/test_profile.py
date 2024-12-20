import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.scroll_util import ScrollUtil


class TestProfile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.profile_page = ProfilePage(self.driver)

    def tearDown(self):
        """Realiza scrolls pela página antes de fechar o navegador."""
        try:
            # Instancia a classe ScrollUtil
            scroll_util = ScrollUtil(self.driver)
            
            # Executa a sequência de scrolls
            scroll_util.perform_scroll_sequence()
            
            # Agora encerra o navegador
            self.driver.quit()
        except Exception as e:
            print(f"Erro ao realizar o tearDown: {e}")

    def login_to_instagram(self):
        """Realiza o login no Instagram."""
        self.login_page.go_to_login_page()
        self.login_page.login()

    def search_user(self, username):
        """Realiza a pesquisa por um usuário."""
        self.profile_page.click_search_icon()
        self.profile_page.search_user(username)
        self.profile_page.click_user_profile()

    def test_dynamic_content(self):
        """Teste para buscar e clicar em um conteúdo dinâmico."""
        self.login_to_instagram()
        self.search_user("eu_mattosoliveira")

        # ID dinâmico do conteúdo que você deseja clicar
        content_id = "C2xVPYdrWdK"
        repetitions = 10  # Quantas vezes o loop vai se repetir
        self.profile_page.watch_and_close_video_loop(content_id, repetitions)

        # Adicione uma verificação simples (exemplo)
        self.assertIn(
            "Instagram",
            self.driver.title,
            "A pesquisa não foi iniciada corretamente."
        )
