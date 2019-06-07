# Simulated Annealing for Clustering Problems
import math
import os


from SimulatedAnneling import SimulatedAnneling
from FileCluster import FileCluster

files_to_be_used = os.listdir('./testcases/')
num_fields = 32  # numero total de campos
num_users = len(files_to_be_used)

# estado inicial
initial_state = []
unused_fields = []

# parametros para mudar a temperatura: uso e ordem
# maior numero de uso e menor for a ordem mais energia
num_cost_increases = 100  # valor de aumento do custo
avg_cost_increase = 200  # valor médio de aumento do custo
acc_ratio = 0.75  # taxa de aceitação (acceptance ratio) entre 0 e 1
prob_e = 0.00000000001  # fator de probabilidade
beta = 0.125  # valor de 0< beta < 1
max_iter = 4 * num_fields  # número maximo de iterações é o número de fields * 4
num_temperature = 200  # temperatura

# calculo de temperatura incial
initial_temperature = avg_cost_increase / math.log(
    num_cost_increases / ((num_cost_increases * acc_ratio) - (1 - acc_ratio) * (max_iter - num_cost_increases)))
# calculo da temperatura final
final_temperature = -beta * avg_cost_increase / math.log(prob_e)
# taxa de diminuição da temperatura
alpha = math.pow(final_temperature / initial_temperature, 1 / num_temperature)

# clusteriza as informações dos arquivos
fileCluster = FileCluster(files_to_be_used)
initial_state = fileCluster.cluster_files()

if __name__ == "__main__":
    simulated_annealing = SimulatedAnneling(num_users, num_fields, initial_state, max_iter, initial_temperature, alpha, final_temperature)
    simulated_annealing.execute_simulation()