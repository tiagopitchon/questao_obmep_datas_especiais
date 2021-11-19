'''
O código fornece uma solução "força bruta" para o problema de análise combinatória da questão
da provada OBMEP (2021) para a sexta série.

[Enunciado aproximado] No período de 2000 a 2100 tem quantos anos com dia especial? Dia 
especial tem os digitos 0, 1, 2, 3, 4 e 5, sem repetição de digito. Formato da data dd/mm/aa.
Exemplo: 03/12/45

PS.: Não tive acesso a prova para obter o enunciado exato.
'''
# 1) Listar todas as opções possíveis.
digitos = '012345'
list_data_text = []
for dig1 in digitos :
    digitos_menos_dig1 = digitos.replace(dig1, '')
    for dig2 in digitos_menos_dig1 :
        digitos_menos_dig1dig2 = digitos_menos_dig1.replace(dig2, '')
        for dig3 in digitos_menos_dig1dig2 :
            digitos_menos_dig1dig2dig3 = digitos_menos_dig1dig2.replace(dig3, '')
            for dig4 in digitos_menos_dig1dig2dig3 :
                digitos_menos_dig1dig2dig3dig4 = digitos_menos_dig1dig2dig3.replace(dig4, '')
                for dig5 in digitos_menos_dig1dig2dig3dig4 :
                    dig6 = digitos_menos_dig1dig2dig3dig4.replace(dig5, '')
                    data_text = dig1+dig2+dig3+dig4+dig5+dig6
                    list_data_text.append(data_text)

# 2) Avaliar, dentre as opções, aquelas que são uma data válida. Separar anos únicos em uma lista à parte.
lista_anos = []
lista_datas = []
for data in list_data_text :
    dia = int(data[0:2])
    mes = int(data[2:4])
    ano = int(data[4:6])
    if (dia<=31) and (mes<=12) :
        if ((dia<=30) and (mes%2 == 0)) or (mes%2 == 1) :
            lista_datas.append(data)
            if ano not in lista_anos :
                lista_anos.append(ano)

# 3) Imprimir o tamanho da lista com os anos.
# print(lista_datas)
print(len(lista_anos))
