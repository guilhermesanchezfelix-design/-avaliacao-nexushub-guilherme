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