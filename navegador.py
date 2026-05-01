from playwright.sync_api import sync_playwright
import pandas as pd


def iniciar_navegador(url):
    #Iniciar o playwright
    playwright = sync_playwright().start()
    #Instanciar e abrir o navegador.
    #Headless - Define se eu vejo o navegador ou não.
    browser = playwright.chromium.launch(headless=False)
    #Cria um perfil novo no navegador
 

url = "https://nfe.etransparencia.com.br/sp.bebedouro/nfe/principal.aspx?6Mq+8H81l6bBzU51Aa4BxIysvNcaBQlI0zjF2rJpzQc="

playwright, browser, page = iniciar_navegador(url)