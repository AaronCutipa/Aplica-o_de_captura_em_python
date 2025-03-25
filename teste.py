import psutil
import datetime

print("=========================================================================")
# CPU
print("Dados da CPU")
print(psutil.cpu_count())
print("=========================================================================")

# Memória 
print("Dados da memória")
mem = psutil.virtual_memory()
total_Memoria =  mem.total / (1024 ** 3)
total_Disponivel =  mem.available / (1024 ** 3)
total_Porcento =  mem.percent

print("Memória total: {:.2f} GB".format(total_Memoria))
print("Memória disponível: {:.2f} GB".format(total_Disponivel))
print("Porcentagem usada: {:.2f}%".format(total_Porcento))
print("=========================================================================")

# Disco
print("Dados de disco")
disk = psutil.disk_usage('/')
total_Disk = disk.total / (1024 ** 3)
usado_Disk = disk.used / (1024 ** 3)
disponivel_Disk = disk.free / (1024 ** 3)
porcentagem_Disk = disk.percent

print("Memória total do disco: {:.2f} GB".format(total_Disk))
print("Memória de disco usado: {:.2f} GB".format(usado_Disk))
print("Memória de disco disponível: {:.2f} GB".format(disponivel_Disk))
print("Porcentagem de disco usado: {:.2f}%".format(porcentagem_Disk))
print("=========================================================================")

# Redes
print("Dados de Rede")
rede = psutil.net_io_counters()
envRede = rede.bytes_sent / (1024 ** 2)
recRede = rede.bytes_recv / (1024 ** 2)
packEnv = rede.packets_sent
packRec = rede.packets_recv

print("Megabytes enviados: {:.2f} MB".format(envRede))
print("Megabytes recebidos: {:.2f} MB".format(recRede))
print("Pacotes enviados: ", packEnv)
print("Pacotes recebidos: ", packRec)
print("=========================================================================")

#Bateria 
print("Dados da Bateria")
bateria = psutil.sensors_battery()
porBat = bateria.percent
if bateria.power_plugged == False:
    estado = "Desconectado"
else: 
    estado = "Conectado"

if bateria and bateria.secsleft != psutil.POWER_TIME_UNLIMITED:
    horas = bateria.secsleft // 3600
    minutos = (bateria.secsleft % 3600) // 60
    print("Tempo restante estimado da bateria: {}h {}min".format(horas, minutos))
else:
    print("A bateria está conectada ou o tempo restante é indefinido.")

print("Porcentagem: {:.2f}%".format(porBat))
print("Carregador:", estado)
print("=========================================================================")