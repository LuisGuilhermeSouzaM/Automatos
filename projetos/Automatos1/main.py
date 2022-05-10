'''
DFA Simulator: 
    Equipe Shaolin:
        Enrico Giannobile RA: 19.00610-0
        Guilherme de Campos RA: 20.00089-8
        Luis Guilherme de Souza Munhoz RA: 20.01937-8

'''


from pydoc import Doc


def simulate_dfa(dfa, input):
    dfa_list = list(dfa.values())  # criando uma lista com os valores do dicionário dfa para fácil manipulação

    state = dfa_list[1]   # estado inicial 
    accept = False
    initial_input = input # armazenando a cadeia para mostrar se ela foi aceita ou rejeitada
    input = list(input)   # transformando a cadeia digitada pelo usuário em uma lista para fácil manipulação
    while(len(input) > 0):

        c = input.pop(0)

        if(c not in dfa_list[2]):
            # Insere c de volta na cadeia, exibe mensagem de erro e sai do loop se c não está no alfabeto do dfa
            input.insert(0, c)
            print(f"o símbolo {c} não pertence ao alfabeto do autômato!")
            break

        if(state not in dfa_list[0]):
            # Se o estado não estiver na lista de estados do dfa exibe mensagem de erro e sai do loop
            print(f"o estado {state} não pertence conjunto de estados do autômato!")
            break
        try:
            # Tenta exibir os estados transitados durante a simulação
            print(f"({state}, '{c}') ->  {dfa_list[3][(state,c)]}")
            state = dfa_list[3][(state, c)]
        except KeyError:
            # Caso não conseguir exibe mensagem de erro e sai do loop
            print(f"Não foi possível realizar a transição do estado {state} com entrada {c}")
            break
    if (state in dfa_list[4] and len(input) == 0):
        # Verifica se o estado atual está na lista de estados finais e se a cadeia toda foi percorrida
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
            # Entrada da cadeia a ser simulada pelo dfa
            user_input = input("Digite a cadeia de entrada do autômato: ")
            print()
            simulate_dfa(dfa, user_input)
            print()
    except KeyboardInterrupt:
        print()
        print("Programa finalizado pelo usuário")
        print()
        print("=" * 80)

## Entrada do nome do arquivo do dfa pelo usuário
file_name = input("Digite o nome do arquivo: ")

with open(file_name) as dfa_file:
    dfa_data = dfa_file.read()

dfa = eval(dfa_data)


main()
