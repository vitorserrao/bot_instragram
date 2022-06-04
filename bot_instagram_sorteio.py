from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class instagrambot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path= r"C:\Users\vitor\OneDrive\Área de Trabalho\Projetos\bot\chromedriver.exe")


    def login(self):
        # acessa o instaram

        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(1)

        # clica no campo usuario e digita meu @
        campo_usuario = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input") #procurar o botão
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        #clica no campo senha e digita minha senha

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(10)
        self.comentar()

    # função que comenta

    def comentar(self):
        flag = True
        contador = 0
        tempo = 0
        driver = self.driver
        driver.get("https://www.instagram.com/p/CdZVRa4L4LH/")
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # rola pra baixo
        time.sleep(4)

        try:

            comentarios = ["listas de usuarios do instagram", "@user", "@user2"]

            sorteado = 0
            while (flag == True):
                time.sleep(3)
                driver.find_element_by_class_name('Ypffh').click()     # localiza o compo pra comentar e clica
                campo_comentario = driver.find_element_by_class_name('Ypffh')  #atribui o campo achado a variavel
                time.sleep(random.randint(3, 5))
                l = random.sample(comentarios, k = 2)
                campo_comentario.send_keys(l)
                contador = contador + 1
                print(contador)
                print(l)
                # self.digitando(random.choice(comentarios), campo_comentario)
                driver.find_element_by_xpath("//*[contains(text(),'Publicar')]").click()
                time.sleep(60)
        except Exception as e:
            print(e)
            time.sleep(5)


bot = instagrambot('login', 'senha')
bot.login()
