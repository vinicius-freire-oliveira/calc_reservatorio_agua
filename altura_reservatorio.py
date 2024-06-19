# Importar o módulo math para cálculos matemáticos
import math

# Definir a classe Edificacao
class Edificacao:
    def __init__(self, num_pavimentos=None, num_apartamentos_por_pavimento=None, num_pessoas_por_apartamento=None,
                 consumo_per_capita_diario=None, area_reservatorio=None):
        # Atributos da classe
        self.num_pavimentos = num_pavimentos
        self.num_apartamentos_por_pavimento = num_apartamentos_por_pavimento
        self.num_pessoas_por_apartamento = num_pessoas_por_apartamento
        self.consumo_per_capita_diario = consumo_per_capita_diario
        self.area_reservatorio = area_reservatorio

    # Método para calcular a população total do edifício
    def calcular_populacao(self):
        return self.num_pavimentos * self.num_apartamentos_por_pavimento * self.num_pessoas_por_apartamento

    # Método para calcular o consumo diário total de água no edifício
    def calcular_consumo_diario_total(self):
        populacao = self.calcular_populacao()
        return populacao * self.consumo_per_capita_diario

    # Método para calcular o volume necessário do reservatório de água
    def calcular_volume_reservatorio(self):
        consumo_diario_total = self.calcular_consumo_diario_total()
        return 0.6 * 2 * consumo_diario_total

    # Método para calcular a área do reservatório
    def calcular_area_reservatorio(self):
        return self.area_reservatorio

    # Método para calcular a altura necessária do reservatório
    def calcular_altura_reservatorio(self):
        volume_reservatorio = self.calcular_volume_reservatorio()
        area_base = self.calcular_area_reservatorio()
        altura = volume_reservatorio / (area_base * 1000)  # Convertendo litros para metros cúbicos
        return round(altura, 2), round(volume_reservatorio / 1000, 2)  # Convertendo litros para metros cúbicos

# Função para solicitar os dados do usuário
def solicitar_dados():
    num_pavimentos = int(input("Informe o número de pavimentos (opcional - se não souber deixe em branco): ") or 0)
    num_apartamentos_por_pavimento = int(input("Informe o número de apartamentos por pavimento (opcional - se não souber deixe em branco): ") or 0)
    num_pessoas_por_apartamento = int(input("Informe o número de pessoas por apartamento (opcional - se não souber deixe em branco): ") or 0)
    populacao = int(input("Informe a população (opcional - se não souber deixe em branco): ") or 0)
    consumo_per_capita_diario = float(input("Informe o consumo per capita diário de água (em litros): "))
    acrescimo_consumo_diario_porcentagem = float(input("Informe o acréscimo sobre o consumo diário (em porcentagem): "))
    area_reservatorio = float(input("Informe a área destinada ao reservatório (em m²): "))

    return num_pavimentos, num_apartamentos_por_pavimento, num_pessoas_por_apartamento, consumo_per_capita_diario, area_reservatorio

# Função principal
def main():
    # Obter os dados do usuário
    num_pavimentos, num_apartamentos_por_pavimento, num_pessoas_por_apartamento, consumo_per_capita_diario, area_reservatorio = solicitar_dados()

    # Criar uma instância da classe Edificacao
    edificacao = Edificacao(num_pavimentos, num_apartamentos_por_pavimento, num_pessoas_por_apartamento,
                            consumo_per_capita_diario, area_reservatorio)

    # Calcular a altura e o volume necessários do reservatório
    altura_reservatorio, volume_reservatorio = edificacao.calcular_altura_reservatorio()

    # Imprimir os resultados
    print("\nO volume do reservatório necessário é de:", volume_reservatorio, "metros cúbicos.")
    print("\nA altura do reservatório necessária é de:", altura_reservatorio, "metros.")

# Verificar se o script está sendo executado diretamente
if __name__ == "__main__":
    main()
