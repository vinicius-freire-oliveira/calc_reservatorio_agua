# Importar o módulo math para cálculos matemáticos
import math

# Definir a classe Edificacao
class Edificacao:
    def __init__(self, num_pavimentos=None, num_apartamentos_por_pavimento=None, num_pessoas_por_apartamento=None,
                 populacao=None, consumo_per_capita_diario=None, acrescimo_consumo_diario_porcentagem=None, 
                 dias_reservatorio_superior=None, dias_reservatorio_inferior=None, reserva_incendio=None):
        # Atributos da classe
        self.num_pavimentos = num_pavimentos
        self.num_apartamentos_por_pavimento = num_apartamentos_por_pavimento
        self.num_pessoas_por_apartamento = num_pessoas_por_apartamento
        self.populacao = populacao
        self.consumo_per_capita_diario = consumo_per_capita_diario
        self.acrescimo_consumo_diario_porcentagem = acrescimo_consumo_diario_porcentagem
        self.dias_reservatorio_superior = dias_reservatorio_superior
        self.dias_reservatorio_inferior = dias_reservatorio_inferior
        self.reserva_incendio = reserva_incendio

    # Método para calcular a população total
    def calcular_populacao(self):
        if self.populacao is not None:
            return self.populacao
        elif self.num_pavimentos is not None and self.num_apartamentos_por_pavimento is not None and self.num_pessoas_por_apartamento is not None:
            return self.num_pavimentos * self.num_apartamentos_por_pavimento * self.num_pessoas_por_apartamento
        else:
            print("População não fornecida e informações insuficientes para calcular.")
            return None

    # Método para calcular o consumo diário total de água
    def calcular_consumo_diario_total(self):
        populacao = self.calcular_populacao()
        if populacao is not None:
            consumo_diario = populacao * self.consumo_per_capita_diario
            if self.acrescimo_consumo_diario_porcentagem is not None:
                acrescimo = consumo_diario * (self.acrescimo_consumo_diario_porcentagem / 100)
                consumo_diario += acrescimo
            return consumo_diario
        else:
            return None

    # Método para calcular o volume do reservatório superior necessário
    def calcular_volume_reservatorio_superior(self):
        consumo_diario_total = self.calcular_consumo_diario_total()
        if consumo_diario_total is not None and self.dias_reservatorio_superior is not None:
            return consumo_diario_total * self.dias_reservatorio_superior

    # Método para calcular o volume do reservatório inferior necessário
    def calcular_volume_reservatorio_inferior(self):
        consumo_diario_total = self.calcular_consumo_diario_total()
        if consumo_diario_total is not None and self.dias_reservatorio_inferior is not None:
            return consumo_diario_total * self.dias_reservatorio_inferior

    # Método para calcular o volume necessário da reserva de incêndio
    def calcular_volume_reserva_incendio(self):
        if self.reserva_incendio is not None:
            return self.reserva_incendio * self.dias_reservatorio_superior if self.dias_reservatorio_superior else self.reserva_incendio * self.dias_reservatorio_inferior

# Função para solicitar os dados do usuário
def solicitar_dados():
    num_pavimentos = int(input("Informe o número de pavimentos (opcional - se não souber deixe em branco): ") or 0)
    num_apartamentos_por_pavimento = int(input("Informe o número de apartamentos por pavimento (opcional - se não souber deixe em branco): ") or 0)
    num_pessoas_por_apartamento = int(input("Informe o número de pessoas por apartamento (opcional - se não souber deixe em branco): ") or 0)
    populacao = int(input("Informe a população (opcional - se não souber deixe em branco): ") or 0)
    consumo_per_capita_diario = float(input("Informe o consumo per capita diário de água (em litros): "))
    acrescimo_consumo_diario_porcentagem = float(input("Informe o acréscimo sobre o consumo diário (em porcentagem): "))
    dias_reservatorio_superior = int(input("Informe o número de dias para o reservatório superior armazenará de água: "))
    dias_reservatorio_inferior = int(input("Informe o número de dias para o reservatório inferior armazenará de água: "))
    reserva_incendio = float(input("Informe a reserva de incêndio (em litros): "))

    return num_pavimentos, num_apartamentos_por_pavimento, num_pessoas_por_apartamento, populacao, consumo_per_capita_diario, \
           acrescimo_consumo_diario_porcentagem, dias_reservatorio_superior, dias_reservatorio_inferior, reserva_incendio

# Função principal
def main():
    # Obter os dados do usuário
    num_pavimentos, num_apartamentos_por_pavimento, num_pessoas_por_apartamento, populacao, consumo_per_capita_diario, \
    acrescimo_consumo_diario_porcentagem, dias_reservatorio_superior, dias_reservatorio_inferior, reserva_incendio = solicitar_dados()

    # Criar uma instância da classe Edificacao
    edificacao = Edificacao(num_pavimentos, num_apartamentos_por_pavimento, num_pessoas_por_apartamento, populacao,
                            consumo_per_capita_diario, acrescimo_consumo_diario_porcentagem, dias_reservatorio_superior,
                            dias_reservatorio_inferior, reserva_incendio)

    # Calcular os volumes necessários dos reservatórios e da reserva de incêndio
    volume_reservatorio_superior = edificacao.calcular_volume_reservatorio_superior()
    volume_reservatorio_inferior = edificacao.calcular_volume_reservatorio_inferior()
    volume_reserva_incendio = edificacao.calcular_volume_reserva_incendio()

    # Imprimir os resultados
    print("\nO volume do reservatório superior necessário sem a reserva de incêndio é de:", volume_reservatorio_superior, "litros.")
    print("\nO volume do reservatório superior necessário para um dia de consumo com a reserva de incêndio é de:", volume_reservatorio_superior + volume_reserva_incendio, "litros.")
    print("\nO volume do reservatório inferior necessário para dois dias de consumo é de:", volume_reservatorio_inferior, "litros.")

# Verificar se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
