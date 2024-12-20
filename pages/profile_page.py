from selenium.webdriver.common.by import By
from pages.base_page import BasePage

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys


class ProfilePage(BasePage):
    SEARCH_ICON = (By.CSS_SELECTOR, 'svg[aria-label="Pesquisa"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[aria-label="Entrada da pesquisa"]')
    USER_PROFILE_LINK = (By.XPATH, 
                         "//a[contains(@href, '/eu_mattosoliveira/')]")
    CLOSE_BUTTON_SELECTOR = (By.XPATH, "//svg[@aria-label='Fechar']")

    def click_search_icon(self):
        """Clica no ícone de pesquisa."""
        self.click(self.SEARCH_ICON)

    def search_user(self, username):
        """Digita o nome de usuário no campo de pesquisa."""
        self.input_text(self.SEARCH_INPUT, username)

    def click_user_profile(self):
        """Clica no link do perfil do usuário."""
        self.click(self.USER_PROFILE_LINK)

    def click_dynamic_content(self, content_id, max_scroll_attempts=10):
        dynamic_link_xpath = f"//a[contains(@href, '{content_id}')]"
        attempts = 0
        while attempts < max_scroll_attempts:
            try:
                # Tenta localizar o link com o content_id
                dynamic_link = self.driver.find_element(By.XPATH, 
                                                        dynamic_link_xpath)
                # Clica no link
                dynamic_link.click()
                return
            except NoSuchElementException:
                # Se não encontrar o link, rola para baixo
                actions = ActionChains(self.driver)
                actions.scroll_by_amount(0, 500).perform()
                time.sleep(1)  # Aguarda um pouco antes de tentar novamente
                attempts += 1

        raise Exception(f"Elemento com ID {content_id}")
    
    def close_video(self):
        """Fecha o vídeo após 5 segundos, pressionando a tecla ESC."""
        try:
            # Pressiona a tecla 'Esc' para fechar o vídeo/modal
            self.press_escape_key()
            print("Vídeo fechado com a tecla Esc.")
        except Exception as e:
            print(f"Erro ao tentar pressionar a tecla ESC: {e}")
    
    def press_escape_key(self):
        """Pressiona a tecla 'Esc' para fechar o vídeo/modal."""
        try:
            # Pressiona a tecla 'Esc' usando ActionChains ou send_keys
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            print("Fechando o vídeo com a tecla Esc.")
        except Exception as e:
            print(f"Erro ao tentar pressionar a tecla ESC: {e}")
    
    def watch_and_close_video_loop(self, content_id, repetitions=10):
        """Assiste ao vídeo por 5 segundos e fecha, 
        repetindo o processo pelo numero de vezes especificado."""
        for _ in range(repetitions):
            self.click_dynamic_content(content_id)  # Abre o vídeo
            time.sleep(5)  # Assiste por 5 segundos
            self.close_video()  # Fecha o vídeo usando a tecla Esc
            time.sleep(3)  # Aguardar um pouco antes de tentar novamente