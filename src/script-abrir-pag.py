import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Redireciona a saída de erro para um arquivo de log
log_file = open("error_log.txt", "w")
sys.stderr = log_file

# Redireciona a saída do console do Chromium para um arquivo
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-logging")

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def barra_de_preenchimento(total, intervalo=1):
    for i in range(1, total + 1):
        print(i, end='.')
        time.sleep(intervalo)
    print()

def imprimir_com_mensagem(mensagem):
    linha_superior = "█" * 30  # Linha superior de caracteres sólidos
    linha_vazia = "█" + " " * 28 + "█"  # Linha vazia com caracteres sólidos nas extremidades
    mensagem_formatada = f"█{mensagem:^28}█"  # Mensagem centralizada com caracteres sólidos nas extremidades

    print(linha_superior)
    print(linha_vazia)
    print(mensagem_formatada)
    print(linha_vazia)
    print(linha_superior)

def imprimir_erro(mensagem):
    linha_superior = "█" * 30  # Linha superior de caracteres sólidos
    linha_vazia = "█" + " " * 28 + "█"  # Linha vazia com caracteres sólidos nas extremidades
    mensagem_formatada = f"█ ERRO: {mensagem:^16}█"  # Mensagem de erro centralizada com caracteres sólidos nas extremidades

    print(linha_superior)
    print(linha_vazia)
    print(mensagem_formatada)
    print(linha_vazia)
    print(linha_superior)

imprimir_com_mensagem("ABRINDO A APLICAÇÃO")

# Função para abrir todos os links de uma lista ul com base em seu id
def abrir_links_da_lista(driver, lista_id):
    ul_element = None
    try:
        ul_element = driver.find_element(By.ID, lista_id)
    except Exception as e:
        imprimir_erro(str(e))
        return

    links = ul_element.find_elements(By.TAG_NAME, 'a')
    for link in links:
        link_url = link.get_attribute('href')
        driver.execute_script("window.open('" + link_url + "', '_blank');")
        time.sleep(2)  # Aguarde um tempo entre a abertura de cada link

# Número de vezes que você deseja abrir e fechar o navegador

num_ciclos = 50

for _ in range(num_ciclos):
    driver = webdriver.Edge()
    driver.get('https://gazetamorena.com.br/categoria/policia/')
    limpar_console()
    time.sleep(1)
    imprimir_com_mensagem("EXECUTANDO SEGUNDA VEZ")
    time.sleep(3)
    limpar_console()
    
    # Localize o segundo elemento alvo usando um seletor CSS diferente
    segundo_link = None
    try:
        segundo_link = driver.find_element(By.CSS_SELECTOR, 'body > div.jeg_viewport > div.jeg_main > div > div.jeg_content > div.jeg_section > div > div.jeg_cat_content.row > div.jeg_main_content.jeg_column.col-sm-8 > div > div.jnews_category_content_wrapper > div > div.jeg_block_container > div.jeg_posts.jeg_load_more_flag > article:nth-child(2) > div.jeg_postblock_content > h3 > a').get_attribute('href')
    except Exception as e:
        imprimir_erro(str(e))
        driver.quit()
        continue

    # Abra o segundo link extraído em uma nova aba
    driver.execute_script("window.open('" + segundo_link + "', '_blank');")

    # Aguarde um tempo para permitir que a nova aba seja carregada

    imprimir_com_mensagem("EXECUTANDO TERCEIRA VEZ")
    time.sleep(5)
    limpar_console()

    # Mude o foco para a nova aba
    driver.switch_to.window(driver.window_handles[-1])

    imprimir_com_mensagem("ABRINDO CADA PÁGINA $")
    

    # Procure e abra todos os links da lista com id "recent-posts-2"
    abrir_links_da_lista(driver, 'recent-posts-2')

    # Feche a nova aba (segundo link)
    driver.close()
    limpar_console()
    # Volte para a aba anterior (página principal)
    driver.switch_to.window(driver.window_handles[0])
    imprimir_com_mensagem("FECHANDO A APLICAÇÃO")
    time.sleep(2)

    limpar_console()
    # Feche o navegador
    driver.quit()

    time.sleep(1)
    limpar_console()

# Fecha o arquivo de log
log_file.close()
