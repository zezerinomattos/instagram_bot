import pickle
import os

SESSION_FILE = "session.pkl"


def save_session(driver):
    """Salva cookies da sessão."""
    with open(SESSION_FILE, "wb") as file:
        pickle.dump(driver.get_cookies(), file)


def load_session(driver):
    """Carrega cookies da sessão."""
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "rb") as file:
            cookies = pickle.load(file)
            for cookie in cookies:
                driver.add_cookie(cookie)
