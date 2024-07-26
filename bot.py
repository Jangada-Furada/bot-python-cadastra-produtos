from botcity.web import WebBot, Browser, By
from botcity.web.browsers.firefox import default_options

user_dir = r"C:\Users\gianl\AppData\Roaming\Mozilla\Firefox\Profiles\58phoxiq.default-release"

entrada = 'Você poderia gerar no formato json com o nome "produtos" os dados de 3 produtos eletrônicos contendo informações de nome, \
categoria, codigo, identificador, descricao, preco e quantidade?'

def coleta_dados_produtos():
    # Instanciando o WebBot
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.FIREFOX
    bot.driver_path = r"C:\Users\gianl\Downloads\geckodriver-v0.34.0-win-aarch64.zip"

    # Configurando opções customizadas no navegador
    def_options = default_options(headless=bot.headless, user_data_dir=user_dir)
    bot.options = def_options

    # Acessando o site para iniciar o chat 
    bot.browse("https://flowgpt.com/chat")
    bot.maximize_window()
    bot.wait(2000)



    bot.stop_browser()


def main():
    coleta_dados_produtos()


if __name__ == '__main__':
    main()