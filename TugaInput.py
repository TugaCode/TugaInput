from googletrans import Translator

class TugaInput:
    def __init__(self, lang="en"):
        self.translator = Translator()
        self.lang = lang

    def traduzir_para_portugues(self, texto):
        traducao = self.translator.translate(texto, src=self.lang, dest="pt")
        return traducao.text

    def input_pt(self, mensagem):
        entrada = input(mensagem)
        return self.traduzir_para_portugues(entrada)

