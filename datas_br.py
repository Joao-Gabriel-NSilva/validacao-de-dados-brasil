from datetime import datetime, timedelta

class Cadastro:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        lista_meses = [
           "janeiro", "fevereiro", "março",
            "abril", "maio", "junho", "julho",
            "agosto", "setembro", "outubro"
            "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month -1
        return lista_meses[mes_cadastro]

    def dia_da_semana_cadastro(self):
        lista_dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sabádo"]
        dia_semana_cadastro = self.momento_cadastro.weekday()
        return lista_dias_semana[dia_semana_cadastro]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y  %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro


