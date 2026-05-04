from playwright.sync_api import sync_playwright
import pandas as pd
import time
import os
from dotenv import load_dotenv



load_dotenv()

class EmissorNFE:
    #Preparar o ambiente web e ligar o motor playwright.
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://nfe.etransparencia.com.br/sp.bebedouro/nfe/principal.aspx?6Mq+8H81l6bBzU51Aa4BxIysvNcaBQlI0zjF2rJpzQc=")

    def Login(self,usuario,senha):
        #Localiza dentro da tag <a> um texto que contém "Login" e clica nele.
        self.page.locator("a:has-text('Login')").click()
        self.page.fill('#W0045vUSUARIO',usuario)
        self.page.fill('#W0045vSENHA', senha)
        self.page.wait_for_timeout(3000)
   

    def captcha(self):
        #page.locator('#LOGIN_MPAGE')
        print("Preencha o Captcha para prosseguirmos...")
        #Usado o wait_for_selector, para que a automação continue apenas quando um dos seletores da proxima
        #etápa apareça.
        self.page.wait_for_selector("#LOGIN_MPAGE")


if __name__ == "__main__":
    bot = EmissorNFE()

    cpf = os.getenv("CPF")
    senha = os.getenv("SENHA")
    bot.Login(usuario=cpf, senha=senha)
    bot.captcha()
