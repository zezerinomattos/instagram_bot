from selenium.webdriver.common.keys import Keys
import time


class ScrollUtil:
    def __init__(self, driver):
        self.driver = driver

    def scroll_down(self, delay=0):
        """Faz o scroll para baixo na página e espera o tempo especificado."""
        body = self.driver.find_element("tag name", "body")
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(delay)

    def scroll_up(self, delay=0):
        """Faz o scroll para cima na página e espera o tempo especificado."""
        body = self.driver.find_element("tag name", "body")
        body.send_keys(Keys.PAGE_UP)
        time.sleep(delay)

    def perform_scroll_sequence(self):
        """Executa a sequência de scrolls definida no requisito."""
        try:
            # Primeiro scroll para baixo e espera 5 segundos
            self.scroll_down(5)
            
            # Segundo scroll para baixo e espera 5 segundos
            self.scroll_down(5)
            
            # Scroll para cima e espera 4 segundos
            self.scroll_up(4)
            
            # Último scroll para baixo e espera 6 segundos
            self.scroll_down(6)

        except Exception as e:
            print(f"Erro ao realizar o scroll: {e}")
