# Math Game

Um jogo de terminal interativo desenvolvido em Python para treinar cálculos matemáticos e raciocínio lógico de forma dinâmica, com níveis de dificuldade progressivos, medição de tempo e acompanhamento de desempenho.

---

## Funcionalidades

* **5 Modos de Jogo:**
  1. **Adição** (`+`)
  2. **Subtração** (`-`)
  3. **Multiplicação** (`x`)
  4. **Divisão** (`/`) — com arredondamento automático para 2 casas decimais e proteção contra divisão por zero.
  5. **Sequências Lógicas** — exibe os 5 primeiros termos de uma progressão aritmética aleatória (razão entre 2 e 4) e desafia o jogador a descobrir o **8º valor**.
* **3 Níveis de Dificuldade:**
  * **Fácil:** números base sorteados entre `1` e `10`.
  * **Médio:** números base sorteados entre `11` e `50`.
  * **Difícil:** números base sorteados entre `51` e `100`.
* **Perguntas Embaralhadas:** Utiliza `random.sample` para gerar as questões de `1` a `10` sem repetição e em ordem aleatória a cada rodada.
* **Cronômetro Integrado:** Mede o tempo exato (em segundos) que o jogador leva para concluir a sessão.
* **Relatório de Desempenho:** Exibe um resumo colorido ao final da partida com o total de **erros**, **acertos** e **tempo gasto**.
* **Interface Estilizada no Terminal:** Utiliza códigos de escape ANSI para destacar títulos, menus, perguntas e feedbacks visuais.
* **Tratamento de Erros e Entradas:** Aceita números decimais tanto com vírgula (`,`) quanto com ponto (`.`), valida opções inválidas e permite encerramento seguro a qualquer momento via `Ctrl + C`.

---

## Tecnologias e Recursos Utilizados

* **Python 3.10+** (utiliza `match / case` estrutural)
* **Bibliotecas Nativas:** `time` e `random` (`sample`, `randint`)
* **Arquitetura Modularizada:** Separação clara entre camada visual (`mathgame.interface`) e regras de negócio (`mathgame.operacao`)

---

## Estrutura do Projeto

```text
math-game/
├── mathgame/
│   ├── interface/
│   │   └── __init__.py             # Estilização ANSI, títulos, menu principal e níveis
│   ├── operacao/
│   │   └── __init__.py             # Lógica das operações, dificuldades e sequências lógicas
│   └── __init__.py
├── web-version/
│   └── multiplication-game-web.py  # Versão web em desenvolvimento
├── math-game.py                    # Arquivo principal de execução do jogo
├── .gitignore
└── README.md
```

---

## Como Executar

### Pré-requisitos
* **Python 3.10 ou superior** instalado (necessário devido ao uso da estrutura `match/case`).

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/jhonatasg01/math-game
   ```

2. **Acesse a pasta do projeto:**
   ```bash
   cd math-game
   ```

3. **Execute o jogo:**
   ```bash
   python3 math-game.py
   ```

---


## Versão

* **Build Version:** 1.5
