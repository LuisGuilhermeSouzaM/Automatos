'''
DFA Simulator: 
    Equipe Shaolin:
        Enrico Giannobile RA: 19.00610-0
        Guilherme de Campos RA: 20.00089-8
        Luis Guilherme de Souza Munhoz RA: 20.01937-8

'''


def simulate_dfa(dfa, input):
    dfa_list = list(dfa.values())

    state = dfa_list[1]
    accept = False
    initial_input = input
    input = list(input)
    while(len(input) > 0):

        c = input.pop(0)

        if(c not in dfa_list[2]):
            input.insert(0, c)
            print(f"o símbolo {c} não pertence ao alfabeto do autômato!")
            break

        if(state not in dfa_list[0]):
            print(
                f"o estado {state} não pertence conjunto de estados do autômato!")
            break
        try:
            print(f"({state}, '{c}') ->  {dfa_list[3][(state,c)]}")
            state = dfa_list[3][(state, c)]
        except KeyError:
            print('Não foi possível realizar a transição do estado ' +
                  str(state) + ' com entrada ' + c)
            break
    if (state in dfa_list[4] and len(input) == 0):
        accept = True
    if(accept):
        print()
        print(f"A cadeia {initial_input} foi aceita pelo autômato!")
        print()
    else:
        print()
        print(f"A cadeia {initial_input} foi rejeitada pelo autômato!")
        print()


def main():
    try:
        print()
        print("=" * 80)
        while(True):
            print()
            user_input = input("Digite a cadeia de entrada do autômato: ")
            print()
            simulate_dfa(dfa, user_input)
            print()
    except KeyboardInterrupt:
        print()
        print("Programa finalizado pelo usuário")
        print()
        print("=" * 80)


file_name = input("Digite o nome do arquivo: ")

with open(file_name) as dfa_file:
    dfa_data = dfa_file.read()

dfa = eval(dfa_data)


main()
