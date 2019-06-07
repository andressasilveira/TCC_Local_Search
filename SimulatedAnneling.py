# Simulated Annealing for Clustering Problems
import math
import random


TIMES_PROPERTY = "times"
STEP_PROPERTY = "step"
ID_PROPERTY = "id"
ORDER_OF_FIELDS_PROPERTY = "orderOfFields"

class SimulatedAnneling:
    def __init__(self,  num_users, num_fields, initial_state, max_iter, initial_temperature, alpha, final_temperature):
        self.max_iter = max_iter
        self.initial_temperature = initial_temperature
        self.alpha = alpha
        self.final_temperature = final_temperature
        self.initial_state = initial_state
        self.num_users = num_users
        self.num_fields = num_fields

    def execute_simulation(self):
        t = self.initial_temperature  # temperatura inicial
        current_state = self.initial_state.copy()  # estado atual recebe copia do estado inicial
        print("Original State:", current_state)
        # enquanto o t for maior/igual à temperatura final
        while t >= self.final_temperature:
            for i in range(1, self.max_iter):
                # proximo estado recebe resultado do action_on com param do estado atual
                next_state = self.action_on(current_state)
                # proxima variavel recebe o resultado do value (energia/penalidade) com param do proximo estado
                next_value = self.value(next_state)
                # valor atual recebe o resultado do value (energia/penalidade) com param do estado atual
                current_value = self.value(current_state)
                # delta de energia usado para a penalidade é o valor do proximo estado menos o valor do estado atual
                energy_delta = next_value - current_value
                # se o delta for negativo ou fator de probabilidade maior/igual ao numero random
                if (energy_delta < 0) or (math.exp(-energy_delta / t) >= random.randint(0, 10)):
                    current_state = next_state  # troca estado para o proximo
            # temperatura recebe temperatura mult. por alpha
            t = self.alpha * t
        print("Final", current_state)
        print("Energy of final state:", self.value(current_state))

    # calcula energia: quanto maior a energia, pior o resultado
    def value(self, state):
        energy = 0
        # calcula quantidade de metade dos usuarios + 1
        more_equal_avg_user__use_field = (self.num_users / 2) + 1
        # calculo para obter 30% minimo de usuários
        min_users = self.num_users * 0.3
        # media da Ordem dos Campos + 1
        avg_order = (self.num_fields / 2) + 1

        # se o pior caso estiver no topo dos casos, pior será a energia
        for i in range(0, len(state)):
            # posição do estado atual
            position = state[i]
            # nro de vezes que o campo foi acessado nesse estado
            times = position[TIMES_PROPERTY]
            # media da ordem nas telas do estado atual
            position = position[STEP_PROPERTY]

            # Verifica percentual de uso  dos campos

            # [RUIM+] Se a posição do campo na fila é maior/igual que a média da Ordem e o
            # nro de vezes que o campo é acessado é menor que o número mínimo de usuários
            if (position >= avg_order and times < min_users) or (times < min_users):
                penalty = len(state) - i  # Aplica penalidade como o tamanho do estado +1
                energy += penalty  # soma penalidade + 1 ao total de energia
            # [BOM+] Se nro de vezes que o campo é acessado é maior que o número mínimo de usuários
            elif times > more_equal_avg_user__use_field:
                energy += 1  # soma 1 ao total de energia
            # [BOM] Se a posição do campo na fila é menor/igual que a média da Ordem e o
            # nro de vezes que o campo é acessado é maior que o número mínimo de usuários
            elif position <= avg_order and times > min_users:
                energy += 1
            else:
                energy += 1

        return energy

    # Método responsável pela perturbação dos estados: mudança do estado atual para o proximo
    def action_on(self, current_state):
        curr = current_state.copy()  # var que armazena estado atual recebe cópia do estado atual
        next = self.swap(curr, random.randint(0, len(curr)), bool(random.getrandbits(1)))
        return next

    def swap(self, array, position, right):
        copy_array = array.copy()

        first_posi = position - 1 if position == len(array) else position
        replace_posi = self.get_place_to_swap(copy_array, position, right)

        from_old = copy_array[first_posi]
        to_old = copy_array[replace_posi]

        copy_array[first_posi] = to_old
        copy_array[replace_posi] = from_old

        return copy_array

    def get_place_to_swap(self, array, position, right):
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
