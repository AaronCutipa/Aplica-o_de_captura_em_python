import mysql.connector
import psutil
import platform
import time
from datetime import datetime

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "1964",
    database = "monitoramentoTotem"
)

mycursor = cnx.cursor()

# Quantidade de núcleos lógicos e físicos da máquina
nucleos_logicos = psutil.cpu_count(logical=True)
nucleos_fisicos = psutil.cpu_count(logical=False)
# Frequência da CPU em MHz
cpu_frequencia = psutil.cpu_freq().max / 1000
# Total de memória RAM em GB
memoria_total = psutil.virtual_memory().total / (1024 ** 3)
# Total de disco em GB
disco_total = psutil.disk_usage('/').total / (1024 ** 3)
# Nome do processador
processador = platform.processor()
# Arquitetura do sistema (32 bits ou 64 bits)
arquitetura = platform.machine()
# Nome do sistema operacional
sistema_operacional = platform.system()
# Versão do sistema operacional
versao_sistema = platform.version()


def menu_inicial():
    print("=====================================")
    print(" ###                                       #             \n  #  #    # #    #  ####  #    #   ##     # #   # #####  \n  #  ##   # ##   # #    # #    #  #  #   #   #  # #    # \n  #  # #  # # #  # #    # #    # #    # #     # # #    # \n  #  #  # # #  # # #    # #    # ###### ####### # #####  \n  #  #   ## #   ## #    #  #  #  #    # #     # # #   #  \n ### #    # #    #  ####    ##   #    # #     # # #    # \n                                                         \n")
    print("    Bem-vindo ao Sistema de Monitoramento   ")
    print("            InnovaAir - Versão 1.0            ")
    print("=====================================")
    print("\nEstamos prontos para começar!")
    inicio = input('Digite "Y" para iniciar o monitoramento ou qualquer outra tecla para encerrar: ').strip().lower()

    return inicio

def coleta_nome_usuario():
    print("\nPerfeito! Vamos começar.")
    nome = input("Por favor, informe o seu nome: ").strip()

    return nome

def escolha_usuario(nome):
    print("\nOlá, {}! O que você deseja fazer?".format(nome))
    escolha = input("""
    1. Ver informações da minha máquina
    2. Iniciar monitoramento em tempo real
    3. Encerrar o serviço
    Escolha uma opção (1, 2 ou 3): """).strip()

    return escolha

def menu_informacoes_maquina():
    print("\n=========================================================================")
    print("Dados da Máquina")
    print("Número de núcleos lógicos: {}".format(nucleos_logicos))
    print("Número de núcleos físicos: {}".format(nucleos_fisicos))
    print("Frequência máxima da CPU: {:.2f} MHz".format(cpu_frequencia))
    print("Memória total: {:.2f} GB".format(memoria_total))
    print("Espaço total do disco: {:.2f} GB".format(disco_total))
    print("Processador: {}".format(processador))
    print("Arquitetura do sistema: {}".format(arquitetura))
    print("Sistema operacional: {}".format(sistema_operacional))
    print("Versão do sistema operacional: {}".format(versao_sistema))
    print("=========================================================================")

def monitoramento_em_tempo_real():
    print("\nIniciando monitoramento em tempo real...")
    print("Coletando dados de monitoramento...")
    while True:
        # Porcentagem de uso da CPU nos últimos 1 segundo
        cpu_porcentagem = psutil.cpu_percent(interval=1)
        # Porcentagem de memória RAM atualmente em uso
        memoria_porcentagem = psutil.virtual_memory().percent
        # Porcentagem de espaço utilizado no disco principal
        disco_percentagem = psutil.disk_usage('/').percent
        # Dados de tráfego de rede  
        rede = psutil.net_io_counters()
        # Quantidade total de bytes enviados pela rede desde a inicialização do sistema
        bytes_enviados = rede.bytes_sent  
        # Quantidade total de bytes recebidos pela rede desde a inicialização do sistema
        bytes_recebidos = rede.bytes_recv  
        # Número total de pacotes enviados pela rede desde a inicialização do sistema
        pacotes_enviados = rede.packets_sent  
        # Número total de pacotes recebidos pela rede desde a inicialização do sistema
        pacotes_recebidos = rede.packets_recv  

        print("=========================================================================")
        print("Dados de monitoramento")
        print("Uso da CPU: {:.2f}%".format(cpu_porcentagem))
        print("Uso da Memória RAM: {:.2f}%".format(memoria_porcentagem))
        print("Uso do Disco: {:.2f}%".format(disco_percentagem))
        print("Total de bytes enviados pela rede: {} bytes".format(bytes_enviados))
        print("Total de bytes recebidos pela rede: {} bytes".format(bytes_recebidos))
        print("Total de pacotes enviados pela rede: {}".format(pacotes_enviados))
        print("Total de pacotes recebidos pela rede: {}".format(pacotes_recebidos))
        print("=========================================================================")


        if cpu_porcentagem > 70 or memoria_porcentagem > 80 or disco_percentagem > 90:    
            sql = "INSERT INTO dadosComp (cpu_porcentagem, memoria_porcentagem, disco_porcentagem, bytes_enviados, bytes_recebidos, pacotes_enviados, pacotes_recebidos, data_coleta, fkMaquina) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (cpu_porcentagem, memoria_porcentagem, disco_percentagem, bytes_enviados, bytes_recebidos, pacotes_enviados, pacotes_recebidos, datetime.now(), 1)

        mycursor.execute(sql,val)
        cnx.commit()

        time.sleep(1)

def encerrar_servico():
    print("\nServiço encerrado. Obrigado por usar o sistema da InnovaAir.")
    exit()


def executar():
    inicio = menu_inicial()

    if inicio == 'y':
        nome = coleta_nome_usuario()

        escolha = escolha_usuario(nome)

        if escolha == '1':
            menu_informacoes_maquina()
            encerrar_servico()

        elif escolha == '2':
            monitoramento_em_tempo_real()

        elif escolha == '3':
            encerrar_servico()

        else:
            print("\nOpção inválida! O serviço será encerrado.")
            encerrar_servico()
    else:
        encerrar_servico()

executar()

cnx.commit()
print(mycursor.rowcount, "record inserted.")
cnx.close()