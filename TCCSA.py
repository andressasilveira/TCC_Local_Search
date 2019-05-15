# Simulated Annealing for Clustering Problems
import math
import random
import json

# carregar dados de json
# with open("user1.json") as json_file:
#    json_data = json.load(json_file)
#    print(json_data)

## clusterizar entre campos usados e não usados
# parametros para mudar a temperatura: uso e ordem
# maior numero de uso e menor for a ordem mais energia
num_fields = 5  # numero total de campos
num_users = 10  # número de usuários
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

# considerando 10 usuários
field1 = {"times": 8, "avg_order": 4}
field2 = {"times": 1, "avg_order": 5}
field3 = {"times": 7, "avg_order": 3}
field4 = {"times": 2, "avg_order": 2}
field5 = {"times": 8, "avg_order": 1}

# estado inicial
initial_state = [field1, field2, field3, field4, field5]
unused_fields = []


def simulated_annealing(max_iter, initial_temperature, alpha, final_temperature, initial_state):
    t = initial_temperature  # temperatura inicial
    current_state = initial_state.copy()  # estado atual recebe copia do estado inicial
    # enquanto o t for maior/igual à temperatura final
    while t >= final_temperature:
        print("Original State:", current_state)
        for i in range(1, max_iter):
            # proximo estado recebe resultado do action_on com param do estado atual
            next_state = action_on(current_state)
            # proxima variavel recebe o resultado do value (energia/penalidade) com param do proximo estado
            next_value = value(next_state)
            # valor atual recebe o resultado do value (energia/penalidade) com param do estado atual
            current_value = value(current_state)
            # delta de energia usado para a penalidade é o valor do proximo estado menos o valor do estado atual
            energy_delta = next_value - current_value
            print("For index " + str(i) + ": Calculate " + str(next_value) + " - " + str(current_value) + " = " + str(
                energy_delta))
            # se o delta for negativo ou fator de probabilidade maior/igual ao numero random
            if (energy_delta < 0) or (math.exp(-energy_delta / t) >= random.randint(0, 10)):
                current_state = next_state  # troca estado para o proximo
        # temperatura recebe temperatura mult. por alpha
        t = alpha * t
    print("Final", current_state)
    print("Energy of final state:", value(current_state))


# calcula energia: quanto maior a energia, pior o resultado
def value(state):
    energy = 0
    # calcula quantidade de metade dos usuarios + 1
    more_equal_avg_user__use_field = (num_users / 2) + 1
    # calculo para obter 30% minimo de usuários
    min_users = num_users * 0.3
    # media da Ordem dos Campos + 1
    avg_order = (num_fields / 2) + 1

    # se o pior caso estiver no topo dos casos, pior será a energia
    for i in range(0, len(state)):
        # posição do estado atual
        position = state[i]
        # nro de vezes que o campo foi acessado nesse estado
        times = position['times']
        # media da ordem nas telas do estado atual
        position = position['avg_order']

        # Verifica percentual de uso  dos campos

        # [RUIM+] Se a posição do campo na fila é maior/igual que a média da Ordem e o
        # nro de vezes que o campo é acessado é menor que o número mínimo de usuários
        if (position >= avg_order and times < min_users) or (times < min_users):
            penalty = len(state) - i  # Aplica penalidade como o tamanho do estado +1
            print('Penalty resulted by ' + str(len(state)) + '-' + str(i) + ' resulted in ' + str(penalty))
            energy += penalty  # soma penalidade + 1 ao total de energia
        # [BOM+] Se nro de vezes que o campo é acessado é maior que o número mínimo de usuários
        elif times > more_equal_avg_user__use_field:
            energy += 1  # soma 1 ao total de energia
        # [BOM] Se a posição do campo na fila é menor/igual que a média da Ordem e o
        # nro de vezes que o campo é acessado é maior que o número mínimo de usuários
        elif position <= avg_order and times > min_users:
            energy += 1

        print('This is my result: ' + str(energy))

    return energy


# Método responsável pela perturbação dos estados: mudança do estado atual para o proximo
def action_on(current_state):
    curr = current_state.copy()  # var que armazena estado atual recebe cópia do estado atual
    next = swap(curr, random.randint(0, len(curr)), bool(random.getrandbits(1)))
    return next


def swap(array, position, right):
    copy_array = array.copy()

    first_posi = position - 1 if position == len(array) else position
    replace_posi = get_place_to_swap(copy_array, position, right)

    from_old = copy_array[first_posi]
    to_old = copy_array[replace_posi]

    copy_array[first_posi] = to_old
    copy_array[replace_posi] = from_old

    return copy_array


def get_place_to_swap(array, position, right):
    if right and len(array) == position:
        return 0
    elif not right and position == 0:
        return len(array) - 1
    elif right:
        if position + 1 == len(array):
            return position
        else:
            return position + 1
    else:
        if position == 0:
            return len(array) - 1
        else:
            return position - 1


if __name__ == "__main__":
    simulated_annealing(max_iter, initial_temperature, alpha, final_temperature, initial_state)
