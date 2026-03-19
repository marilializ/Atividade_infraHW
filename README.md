# Atividade_infraHW
Atividade 19/03

## Distribuicao de tarefas dos membros

### Dupla A - Estrutura do simulador (fetch + loop principal)
- Declarar a memoria (`mem[256]`), registradores (`reg[4]`), `PC`, `ZF`, `running` e `ciclo`.
- Implementar a funcao `fetch()`: ler `mem[PC]`, `mem[PC+1]`, `mem[PC+2]` e avancar `PC` em 3.
- Implementar o loop principal em `main()`: enquanto `running` e `PC < 256`, chamar `fetch -> decode_execute -> trace`.
- Carregar o programa e os dados do Fibonacci no array `mem[]`.

### Dupla B - Decode/Execute
- Implementar o `switch/case` completo com os opcodes: `LOAD`, `STORE`, `ADD`, `SUB`, `MOV`, `CMP`, `JMP`, `JZ`, `JNZ`, `HALT`.
- Garantir a logica correta de cada instrucao (principalmente `JZ`/`JNZ`, que modificam o `PC`).
- Testar cada instrucao isoladamente com casos simples antes de rodar o Fibonacci completo.

### Solo - Trace + Testes
- Implementar a funcao `trace()`: imprimir ciclo, nome da instrucao, valores de `R0-R3`, `PC` e `ZF`.
- Rodar o simulador com o exemplo da secao 5.1 (`MOV + ADD + HALT`) para validar antes do Fibonacci.
- Validar que ao final `mem[0x20] == 13`.
- Preparar a demonstracao para a apresentacao.
