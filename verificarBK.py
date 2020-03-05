import csv, os

entrada = open('tabelaEntrada.csv')
terminais = csv.DictReader(entrada)


for terminal in terminais:
    host = terminal["IP"]
    retorno = os.system("ping -c 1 " + host)
    
    if retorno == 0:
        saida = open('tabelaSaida.csv', 'a')
        try:
            writer = csv.writer(saida)
            writer.writerow( (terminal["IP"], terminal["ID"], 'ON') )
        finally:
            saida.close()

    else:
        saida = open('tabelaSaida.csv', 'a')
        try:
            writer = csv.writer(saida)
            writer.writerow( (terminal["IP"], terminal["ID"], 'OFF') )
        finally:
            saida.close()
