
    #trace()

    def trace(self, op, a, b):
        nomes = {
            1: 'LOAD', 2: 'STORE', 3: 'ADD', 4: 'SUB',
            5: 'MOV',  6: 'CMP',   7: 'JMP', 8: 'JZ',
            9: 'JNZ',  10: 'HALT'
        }
        nome = nomes.get(op, '???')
        print(f'Ciclo {self.ciclo}: {nome:5s} {a},{b} |'
              f' R0={self.reg[0]:3d} R1={self.reg[1]:3d}'
              f' R2={self.reg[2]:3d} R3={self.reg[3]:3d}'
              f' | PC={self.pc:3d} ZF={self.zf}')


# testes e validação (fora da classe)

# --- TESTE 1: exemplo simples da seção 5.1 ---
# MOV R0, 10 → ADD R0, R1 → HALT
# Resultado esperado: R0 = 11

print("=== TESTE SIMPLES (seção 5.1) ===")
cpu = MiniCPU()

cpu.mem[0] = 0x05; cpu.mem[1] = 0x00; cpu.mem[2] = 0x0A  # MOV R0, 10
cpu.mem[3] = 0x05; cpu.mem[4] = 0x01; cpu.mem[5] = 0x01  # MOV R1, 1
cpu.mem[6] = 0x03; cpu.mem[7] = 0x00; cpu.mem[8] = 0x01  # ADD R0, R1
cpu.mem[9] = 0x0A; cpu.mem[10] = 0x00; cpu.mem[11] = 0x00  # HALT

cpu.run()
print(f'R0 = {cpu.reg[0]} (esperado: 11) {"✅" if cpu.reg[0] == 11 else "❌"}')


print("\n=== FIBONACCI ===")
cpu2 = MiniCPU()

cpu2.run()

resultado = cpu2.mem[0x20]
print(f'\nResultado: mem[0x20] = {resultado}')
print(f'Esperado:  13')
print('CORRETO!' if resultado == 13 else 'ERRADO!')