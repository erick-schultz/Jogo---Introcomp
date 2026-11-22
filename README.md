# Jogo Introcomp

Jogo de RPG de batalha por turnos feito em Python com Pygame, desenvolvido durante o Introcomp (2023).

O jogador escolhe três personagens entre cinco classes disponíveis para enfrentar dois inimigos em rodadas ordenadas pela velocidade de cada unidade. Em cada turno, é possível atacar um alvo ou defender para reduzir o dano recebido até o fim da rodada.

## Como executar

Requer Python 3.10 ou superior e a biblioteca `pygame`:

```bash
pip install pygame
python main.py
```

## Classes e atributos

Todos os personagens começam com 100 pontos de vida.

### Personagens jogáveis

| Classe   | Ataque | Defesa | Velocidade |
| -------- | ------ | ------ | ---------- |
| Paladino | 35     | 70     | 3          |
| Ladino   | 80     | 20     | 9          |
| Mago     | 60     | 50     | 6          |
| Caçador  | 70     | 30     | 5          |
| Clérigo  | 55     | 40     | 6          |

### Inimigos

| Inimigo    | Ataque | Defesa | Velocidade |
| ---------- | ------ | ------ | ---------- |
| Necromante | 30     | 70     | 7          |
| Esqueleto  | 70     | 30     | 6          |

O dano de um ataque é calculado por `ataque * (50 / (50 + defesa_alvo))`. A ação de defender dobra a defesa do personagem até o final da rodada.

## Controles

- **Setas direcionais**: navegar no menu de seleção, alternar entre `Atacar` e `Defender` e escolher o inimigo alvo.
- **Z**: confirmar personagem no menu ou confirmar a ação escolhida.
- **Espaço**: confirmar o ataque no inimigo selecionado.
- **X**: cancelar a seleção de alvo e voltar para a escolha de ação.

## Estrutura do projeto

- `main.py`: loop principal do Pygame, menu de seleção, interface de combate e telas finais.
- `batalha.py`: ordenação dos turnos por velocidade, execução de ataques/defesas e verificação de vitória ou derrota.
- `personagem.py`: classe base (`pygame.sprite.Sprite`) com atributos de combate, cálculo de dano e troca de sprite ao ser derrotado.
- `jogador.py`: subclasse de `Personagem` para os personagens controlados pelo jogador.
- `inimigo.py`: subclasse de `Personagem` que espelha o sprite e escolhe aleatoriamente entre atacar e defender.
- `window.py`: configuração das dimensões da janela (`1024x768`) e cor de fundo.
- `versoes_anteriores/`: histórico das versões anteriores do projeto (`v1.0`, protótipo inicial de interface; `v17`, versão intermediária anterior ao menu de seleção; e `v2.0`, versão original com menu e telas finais antes das correções da `v3.0` na raiz).
