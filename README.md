# Jogo Introcomp

Jogo de RPG de batalha por turnos feito em Python com Pygame, desenvolvido durante o Introcomp (2023).

O jogador monta uma equipe de três personagens e enfrenta dois inimigos em rodadas ordenadas pela velocidade de cada unidade. Em cada turno, é possível atacar um alvo ou defender para reduzir o dano recebido até o fim da rodada.

## Versões no repositório

O repositório mantém diferentes etapas do projeto exportadas do Replit:

- **Raiz (`v1.0`)**: protótipo inicial com a janela, sprites e navegação básica de menu, ainda sem o combate integrado à interface.
- **`Jogo-Introcomp-v17 (1)/`** (e `Jogo-Introcomp-v16 (1).zip`): versão intermediária com o combate já integrado entre 3 personagens fixos (Caçador, Paladino e Bispo) e 2 inimigos (Necromante e Esqueleto).
- **`Jogo-Introcomp-v2.0 (2).zip`**: versão mais completa, com menu inicial para escolha de equipe entre 5 classes, trilha sonora (`musica.mp3`) e telas de vitória e derrota.

## Classes e atributos (v2.0)

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

## Como executar

Requer Python 3.10 ou superior e a biblioteca `pygame`:

```bash
pip install pygame
```

Para jogar a versão mais recente (`v2.0`), extraia o `.zip` e execute `main.py` dentro da pasta extraída:

```bash
unzip "Jogo-Introcomp-v2.0 (2).zip" -d jogo-v2
cd jogo-v2
python main.py
```

Para executar a versão intermediária (`v17`) ou o protótipo da raiz (`v1.0`), entre no diretório correspondente e rode:

```bash
python main.py
```

Nota: o `pyproject.toml` veio do template do Replit e lista `dearpygui` (além de `window` na v1.0), mas essas bibliotecas não são utilizadas no código; apenas `pygame` é necessário.

## Estrutura do código

- `main.py`: loop principal do Pygame, interface, menu de seleção e leitura de teclado.
- `batalha.py`: ordenação dos turnos por velocidade, execução de ataques/defesas e verificação de fim de partida.
- `personagem.py`: classe base (`pygame.sprite.Sprite`) com atributos de combate, cálculo de dano e troca de sprite ao ser derrotado.
- `jogador.py`: subclasse de `Personagem` para os personagens controlados pelo jogador.
- `inimigo.py`: subclasse de `Personagem` que espelha o sprite e escolhe aleatoriamente entre atacar e defender.
- `window.py`: configuração das dimensões da janela (`1024x768`) e cor de fundo.
