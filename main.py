# CyberPulse Tech

startup = {
    "nome": "CyberPulse Tech",
    "segmento": "Segurança da Informação",
    "ano_adesao": "2026"
}

# Soluções ativas
solucoes_ativas = ["Firewall IA", "Scan de Vulnerabilidades"]

# Exibição dos dados
print("Startup:", startup["nome"])
print("Segmento:", startup["segmento"])
print("Primeiro produto:", solucoes_ativas[0])

# Matriz 2D das bancadas
bancadas = [
    [1, 0],  # Setor Norte: N1 ocupada, N2 livre
    [0, 1]   # Setor Sul: S1 livre, S2 ocupada
]

# Exibição das bancadas
print("\nStatus das bancadas:")
print("Bancada N1:", bancadas[0][0])
print("Bancada N2:", bancadas[0][1])
print("Bancada S1:", bancadas[1][0])
print("Bancada S2:", bancadas[1][1])

print("\nLegenda: 1 = Ocupado | 0 = Livre")

# Leitura sequencial do arquivo de custos Cloud sem usar laços
with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    linha_1 = arquivo.readline()
    linha_2 = arquivo.readline()
    linha_3 = arquivo.readline()
    linha_4 = arquivo.readline()

print("\n=== Leitura do arquivo custos_cloud.csv ===")
print(cabecalho.strip())
print(linha_1.strip())
print(linha_2.strip())
print(linha_3.strip())
print(linha_4.strip())

# Consolidação dos dados do custo da infraestrutura Cloud
with open("custos_cloud.csv", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.read().splitlines()

recurso_1, custo_1 = linhas[1].split(",")
recurso_2, custo_2 = linhas[2].split(",")
recurso_3, custo_3 = linhas[3].split(",")
recurso_4, custo_4 = linhas[4].split(",")

custo_1 = float(custo_1)
custo_2 = float(custo_2)
custo_3 = float(custo_3)
custo_4 = float(custo_4)

total = custo_1 + custo_2 + custo_3 + custo_4

print("\n=== Painel Final ===")
print(f"Nome da startup: {startup['nome']}")
print("Bancada alocada: Bancada N1")
print(f"Valor total da infraestrutura Cloud: R$ {total:.2f}")