import random
import time
from tqdm import tqdm
import math
import pygame

#Colocar linha abaixo do rolando um d20
#Vida do jogador não está aumentando com o passar dos levels

#Dados
dado1d4 = random.randint(1, 4)
dado1d6 = random.randint(1, 6)
dado1d8 = random.randint(1, 8)
dado1d10 = random.randint(1, 10)
dado1d12 = random.randint(1, 12)
dado1d20 = random.randint(1, 20)
rec_hp = random.randint(1, 20)

#Ações
ações = ['Ataque básico','Ataque especial','Recuperar vida']
ações_completa = ('[1] Ataque básico\n[2] Ataque especial\n[3] Recuperar vida(1d20)\n>>>')
ações_sem_pot = ('[1] Ataque básico\n[2] Ataque especial\n>>>')

#Contagens
monstro_derrotado = 0
pontuacao_geral = 0
poções = 5
exp = 0
level_jogador = 1
level_monstros = range(1,10,1)
level_novo = 1

#Atributos dos monstros
monstro_vida = 10+(level_jogador*10)
monstro_armor = 8+round(level_jogador)
monstro_dano = 2+(level_jogador*1.5)
monstro_level = level_jogador
lista_ate_10 = range(1,10,1)
monstroescolhido = []
mestre_vida = 200

#Atributos secundários
dano_ctc = 2
chance_critc_extra = 0
vitalidade = 1
velocidade = 0
magia = 0 #Vai escalar a chance de atk

#Classes e atributos delas
classe=[] #HP, ARMOR, FORÇA, DESTREZA, HABILIDADE, HABILIDADE, NOME DA CLASSE, ARMA, ARMADURA
guerreiro = {'HP':40+(12*vitalidade),
             'ARMOR':11+(math.floor(level_jogador/3)),
             'FORÇA':level_jogador*2+dado1d6,
             'DESTREZA':level_jogador*1+dado1d6,
             'HABILIDADE':level_jogador*1+dado1d6,
             'SKILL':'Ataque enfurecido',
             'NOME':'Guerreiro',
             'ARMA':'Espada+1',
             'ARMADURA':'Armadura básica de couro+2'}

mago = {'HP':25+(10*vitalidade),
        'ARMOR':9+(math.floor(level_jogador/3)),
        'FORÇA':level_jogador*1+dado1d6,
        'DESTREZA':level_jogador*1+dado1d4,
        'HABILIDADE':level_jogador*4+dado1d8,
        'SKILL':'Bola de fogo',
        'NOME':'Mago',
        'ARMA':'Grimório+1',
        'ARMADURA':'Túnica do iniciante+1'}

assassino = {'HP':25+(10*vitalidade),
        'ARMOR':9+(math.floor(level_jogador/3)),
        'FORÇA':level_jogador*2+dado1d6,
        'DESTREZA':level_jogador*4+dado1d8,
        'HABILIDADE':level_jogador*2+dado1d4,
        'SKILL':'Sneak attack',
        'NOME':'Assassino',
        'ARMA':'Par de adagas+1',
        'ARMADURA':'Armadura básica de pano+1'}

monge = {'HP':25+(15*vitalidade),
          'ARMOR':10+(math.floor(level_jogador/3)),
          'FORÇA':level_jogador*1+dado1d6,
          'DESTREZA':level_jogador*4+dado1d8,
          'HABILIDADE':level_jogador*3+dado1d4,
          'SKILL':'Golpe espiritual',
          'NOME':'Monge',
          'ARMA':'Bastão+1',
          'ARMADURA':'Rakusu+1'}

arqueiro = {'HP':25+(10*vitalidade),
        'ARMOR':9+(math.floor(level_jogador/3)),
        'FORÇA':level_jogador*2+dado1d6,
        'DESTREZA':level_jogador*4+dado1d8,
        'HABILIDADE':level_jogador*2+dado1d4,
        'SKILL':'Tiro concentrado',
        'NOME':'Assassino',
        'ARMA':'Arco e flecha+1',
        'ARMADURA':'Armadura básica de pano+1'}



#Outros
membros_do_corpo = ['no seu ombro', 'na sua cabeça', 'no seu braço', 'na sua perna', 'no seu joelho', 'no seu peito']
rec_hp = random.randint(1,20)  #Poção de HP


#Inimigos
monstros0 = ['Nada','Nenhum']
monstros1 = ['Goblin','Morcego','Zumbi', 'Javali', 'Lobo', 'Escorpião']
monstros2 = ['Coronavírus','Gárgula', 'Gnomo','ET Bilu','Esqueleto', 'Goblin','Aranha','Morcego','Zumbi', 'Javali', 'Lobos', 'Escorpião']

monstros3 = ['Golem', 'Troll','Salamandra', 'Lobo do Ártico', 'Morcegos Gigantes']
monstros4 = ['Elefante de ferro','Morcego','Panteras', 'Leões das Cavernas', 'Golem', 'Troll','Salamandra', 'Lobo do Ártico', 'Morcegos Gigantes']

monstros5 = ['Guarda','Bruxa','Minotauro', 'Guerreiro decaptado', 'Cavaleiro da morte', 'Espantalho macabro']
monstros6 = ['Gavião','Ladrão','Troglodita', 'Devorador de Mentes','Guarda','Bruxa','Minotauro', 'Guerreiro decaptado', 'Cavaleiro da morte', 'Espantalho macabro']

monstros7 = ['Pseudodragão','Harpia','Medusa']
monstros8 = ['Demônio','Dragão','Basilisco']

monstros9 = ['Dragão de fogo','Hidra', 'Dragão de gelo', 'Dragão celestial','Ragnir']
monstros10 = ['Dragão negro', 'Dragão ancião branco', 'Zeus']

monstros11 = ['Cristo Redentor', 'Esfinge', 'Estátua da liberdade']

monstros12 = ['Mestre da mesa']
monstros = [monstros0, monstros1, monstros2, monstros3, monstros4, monstros5, monstros6, monstros7, monstros8, monstros9, monstros10, monstros11, monstros12]

monstroescolhido =  random.choice(monstros[level_jogador])



conquistas = []
                
#Linha
linha = '='*20



#============================================= RODANDO O JOGO =============================================================
def carregando_jogo():
    print('''\n\n\n\n\n\n\n\n\n
8888888b.                                                                                      888        8888888b.         888   888                              
888  "Y88b                                                                                     888        888   Y88b        888   888                              
888    888                                                                                     888        888    888        888   888                              
888    888888  88888888b.  .d88b.  .d88b.  .d88b. 88888b. .d8888b          8888b. 88888b.  .d88888        888   d88P888  88888888888888b.  .d88b. 88888b. .d8888b  
888    888888  888888 "88bd88P"88bd8P  Y8bd88""88b888 "88b88K                 "88b888 "88bd88" 888        8888888P" 888  888888   888 "88bd88""88b888 "88b88K      
888    888888  888888  888888  88888888888888  888888  888"Y8888b.        .d888888888  888888  888        888       888  888888   888  888888  888888  888"Y8888b. 
888  .d88PY88b 888888  888Y88b 888Y8b.    Y88..88P888  888     X88        888  888888  888Y88b 888        888       Y88b 888Y88b. 888  888Y88..88P888  888     X88 
8888888P"  "Y88888888  888 "Y88888 "Y8888  "Y88P" 888  888 88888P'        "Y888888888  888 "Y88888        888        "Y88888 "Y888888  888 "Y88P" 888  888 88888P' 
                               888                                                                                       888                                       
                          Y8b d88P                                                                                  Y8b d88P                                       
                           "Y88P"                                                                                    "Y88P"                                        
 ''')
    print('Carregando a masmorra...')
    time.sleep(1)
    print('Carregando as classes...')
    time.sleep(1)
    print('Pegando as fichas...')
    time.sleep(1)
    print('Pedindo um lanche...')
    time.sleep(1)
    print('Bolando um pra começar a mesa...')
    time.sleep(2)
    print('')
    print('                    C A R R E G A N D O  O  J O G O')
    for i in tqdm(range(200)):
        time.sleep(0.01)
    print('')
    print('')

def introducao():
    print('Seja muito bem vindo a Dungeon and Pythons.')
    time.sleep(1)
    print('Dungeons and Pythons é um jogo de combate em turnos no maior estilo Dungeons and Dragons.')
    time.sleep(1)
    print('Aqui, você percorrerá uma masmorra infinita, eliminando o maior número de inimigos que conseguir.')
    time.sleep(1)
carregando_jogo()
introducao()

escolha_inicial = input('''Aceitas o desafio, meu nobre jogador???
[1] Sim     [2] Não
>>> ''')

conquistas = []

if escolha_inicial == '1':
#    pygame.mixer.init()
#    pygame.mixer.music.load('musiquinha braba.mp3')
#    pygame.mixer.music.play()
    #Introdução do jogo
    print('Obrigado por aceitar o desafio')
    print(' ')
    time.sleep(1)
    print('---------- nova conquista: Coragem ------------\n')
    conquistas.append('Coragem')
    time.sleep(1)
    #Escolher classe
    c = input('''Qual classe voce deseja escolher?
[1]Guerreiro [2]Mago [3]Assassino [4]Monge [5] Arqueiro
>>>''')
    print(' ')
    if c == '1':
      classe = guerreiro
      print('Voce escolheu a classe GUERREIRO. Empunhe sua espada e vamos à luta!!')
      pygame.mixer.music.load('Efeitos sonoros\espada3.mp3')
    elif c == '2':
      classe =  mago
      print('Você escolheu a classe MAGO. Pegue seu grimório e vamos ao combate!!')
    elif c == '3':
      classe = assassino
      print('Voce escolheu a classe ASSASSINO. Com suas adagas elimine a maior quantidade de inimigos que conseguir')
    elif c == '4':
      classe = monge
      print('Você escolheu a classe MONGE. Sua sabedoria foi forjada nas montanhas mais altas')
    elif c == '5':
      classe = arqueiro
      print('Você escolheu a classe ARQUEIRO. Vamos à batalha')

    time.sleep(2)

    #Atributos da classe
    HP = classe['HP'] + vitalidade
    ARMOR = classe['ARMOR'] + int(classe['ARMADURA'].split('+')[1])
    FOR = classe['FORÇA'] + int(classe['ARMADURA'].split('+')[1])
    DES = classe['DESTREZA']
    HAB = classe['HABILIDADE'] + magia
    jogador_vida = HP
    arma = classe['ARMA'].split('+')[0]
    armadura = classe['ARMADURA'].split('+')[0]
    atk_spc = classe['SKILL']




    print('Atributos do personagem:')
    print(f'HP: {HP}')       #HP
    print(f'ARMOR: {ARMOR}') #ARMADURA
    print(f'FOR: {FOR}')     #FORÇA
    print(f'DES: {DES}')     #DESTREZA
    print(f'HAB: {HAB}')     #HABILIDADE
    print(f'Arma equipada: {arma}')
    print('=-='*20)
    time.sleep(2)

    time.sleep(2)

    print('''Escolha sua raça:
Humano: com sua inteligência e capacidade de organização, criaram melhores equipamentos e armaduras: Armor + 1

Elfo: seu mundo ligado à magia fez com que você dominasse certas habilidades e melhorasse seus ataques especiais: Habilidade + 2

Orc: A brutalidade é algo relevante em toda jornada que um Orc faz: Força + 2

Anão: Seu treinamento de resistência será útil para aguentar longas jornadas, como por exemplo uma dungeon infinita: HP + 10
''')
    print(' ')
    time.sleep(1)
    raça = input('''[1] Humano  [2] Elfo  [3] Orc  [4] Anão
>>> ''')
    if raça == '1':
        ARMOR += 1
        raça_jogador = 'Humano'
    elif raça == '2':
        HAB += 2
        raça_jogador = 'Elfo'
    elif raça == '3':
        FOR += 2
        raça_jogador = 'Orc'
    elif raça == '4':
        HP += 10
        raça_jogador = 'Anão'
    else:
        print('Botão errado, tente novamente!')
        raça = input('''[1] Humano  [2] Elfo  [3] Orc  [4] Anão
        >>> ''')

    #print('Agora escolha sua habilidade de classe')
    #atk_spc_escolha = input(f'[1] {atk_spc}')
    #if atk_spc_escolha == '1':
    #    atk_spc = atk_spc_lista[0]
    #elif atk_spc_escolha == '2':
    #    atk_spc = atk_spc_lista[1]

    #Sistema de level
    tabela_xp_antigo = [2, 5, 8, 12, 17, 23, 30, 38, 50]

    #Escolher nome + inicio da batalha
    nome = input('Nome do personagem:\n>>>')
    print(' ')
    time.sleep(1)

    print(f'Sua ficha:')
    print('=-='*20)
    print(f'[Nome:{nome} / classe:{classe["NOME"]} / raça:{raça_jogador} ]')
    print('Atributos do personagem:')
    print(f'HP: {HP}')       #HP
    print(f'ARMOR: {ARMOR}') #ARMADURA
    print(f'FOR: {FOR}')     #FORÇA
    print(f'DES: {DES}')     #DESTREZA
    print(f'HAB: {HAB}')     #HABILIDADE
    print(f'Arma equipada: {arma}')
    print('=-='*20)
    time.sleep(2)

    mochila = {arma : 1, armadura : 1}
    
   
    print(f'{nome}, este é nosso calabouço. Boa aventura, lute com sabedoria!')
    print(' ')
    time.sleep(2)
    print(f'{monstroescolhido} apareceu!')

    #=========================================================BATALHA ROLANDO====================================================
    while jogador_vida >= 1:
        dado1d4 = random.randint(1,4)
        dado1d6 = random.randint(1,6)
        dado1d8 = random.randint(1,8)
        dado1d10 = random.randint(1,10)
        dado1d12 = random.randint(1,12)
        dado1d20 = random.randint(1,20)
        rec_hp = random.randint(1, 20)


        def ficha(par):
          print(f'Sua{par}ficha:')
          print('=-=' * 20)
          print(f'[Nome:{nome} ({level_jogador})/ classe:{classe["NOME"]} / raça:{raça_jogador} ]')
          print('Atributos do personagem:')
          print(f'HP: {HP}')  # HP
          print(f'ARMOR: {ARMOR}')  # ARMADURA
          print(f'FOR: {FOR}')  # FORÇA
          print(f'DES: {DES}')  # DESTREZA
          print(f'HAB: {HAB}')  # HABILIDADE
          print(f'Arma equipada: {arma}')
          print('=-=' * 20)
          time.sleep(2)

        def conquistas_menu():
          print('\nSuas conquistas')
          print('=-=' * 20)
          print(f'{conquistas}')

        def mochila_menu():
          print('\nSua mochila')
          print('=-=' * 20)
          print(f'{mochila}')

        def menu():
            while True:
                print('\n MENU DO JOGO')
                print('=-=' * 20)
                op_menu = input('[1] Visualizar sua ficha\n[2] Ver conquistas\n[3] Abrir mochila\n[Qualquer botão]Voltar à dungeon')
                if op_menu == '1':
                    ficha(' ')
                    for i in range(5):
                        time.sleep(1)
                        print(5 - i)
                elif op_menu == '2':
                    conquistas_menu()
                    for i in range(5):
                        time.sleep(1)
                        print(5 - i)
                elif op_menu == '3':
                    mochila_menu()
                    for i in range(5):
                        time.sleep(1)
                        print(5 - i)

                else:
                    break

        def pocao(condicao = 'normal'):
            if condicao == 'critico':
                time.sleep(1)
                print(f'{nome} bebeu uma poção (mágica) e recuperou {(rec_hp*2 + HP*0.2)} de HP!')
                jogador_vida += ((rec_hp*2) + HP*0.2)
                time.sleep(1)
                print(f'{nome} ({level_jogador}) tem {jogador_vida} HP agora!')
                if jogador_vida > HP: #Limite de HP
                    print(f'Não é possível aumentar seu HP além de {HP}\n')
                    jogador_vida = HP

            elif condicao == 'normal':
                if poções > 0:
                    time.sleep(1)
                    print(f'{nome} ({level_jogador}) bebeu uma poção e recuperou {(rec_hp)} de HP!')
                    jogador_vida += rec_hp
                    poções -= 1
                    time.sleep(1)
                elif poções <= 0:
                    ações_completa = ações_sem_pot
                    jogador_vida = jogador_vida
                    poções = 0
                    rec_hp = 0
                    print('Voce nao possui mais poções')
                    if jogador_vida >= HP: #Limite de HP
                        jogador_vida = HP
                        time.sleep(1)
                        print(f'Não é possível aumentar seu HP além de {HP}')
                else:
                    print(f'{nome}({level_jogador}) tem {jogador_vida} HP agora!')
            elif condicao == 'falha_critica':
                time.sleep(1)
                poções -= 1
                print('Ih mané, tirou 1 no dado, se fodeu')
                print(f'Agora voce tem {poções} poções')


        print('='*20)
        print(' ')
        time.sleep(1)
        print(f'{nome} ({level_jogador}) HP: {jogador_vida}\n{monstroescolhido} HP: {monstro_vida}')
        print(' ')
        time.sleep(1)

        #JOGADA DO JOGADOR
        print(f'''                                                   
        {nome}, escolha sua jogada:
                                                                                        
        [1] Ataque básico                                                                        
        [2] {atk_spc} [50% de chance de funcionar após o d20]                              
        [3] Recuperar vida (1d20) [{poções} poções]
        [4] Abrir menu''')
        
        jogada = input('>>> ')
        print(' ')
        time.sleep(2)

        if jogador_vida > 1:
        # Atk normal
            if jogada == '1':
                print('Rolando um d20...')
                roll = random.randint(1,20) + round(DES/3)
                if roll >= 20: # Critico
                    pontuação += dado1d6 * 2 + FOR
                    time.sleep(2)
                    print('DANO CRÍTICO')
                    time.sleep(1)
                    print(f'{nome} ({level_jogador}) causou {(dado1d6*2 + FOR)} de dano com ataque básico!!')
                    monstro_vida = monstro_vida - (dado1d6*2) - FOR
                    time.sleep(1)
                    print(f'{monstroescolhido} tem {monstro_vida} HP agora!\n')
                elif monstro_armor <= roll < 20: # Quando pega
                    print(f'O ataque pegou! ({roll} na rolagem)')
                    time.sleep(1)
                    print(f'{nome} causou {(dado1d6+FOR)} de dano com ataque básico')
                    monstro_vida = monstro_vida - dado1d6 - FOR
                    time.sleep(1)
                    print(f'{monstroescolhido} tem {monstro_vida} HP agora!')
                    time.sleep(1)
                elif roll == 1: # Falha critica
                    print('Ih mané, tirou 1 no dado, se fodeu')
                    print('Você tropeçou e bateu de cabeça no chão, -3 HP')
                    jogador_vida -= 3
                else:
                    time.sleep(1)
                    print(f'O ataque NÃO pegou, tirou {roll} no dado')
            # Atk magico
            elif jogada == '2':
                print('Rolando um d20...')
                roll = random.randint(1,20) + round(DES/3)
                if roll >= (20 - chance_critc_extra): # Critico
                    pontuação += dado1d6 * 2 + FOR
                    print('DANO CRÍTICO')
                    time.sleep(1)
                    chance = 1
                    print(f'{nome} ({level_jogador}) causou {(dado1d10*2 + FOR + HAB*2)} de dano com {atk_spc}!!')
                    monstro_vida = monstro_vida - (dado1d10*2) - FOR - HAB*2
                    time.sleep(1)
                    print(f'{monstroescolhido} tem {monstro_vida} HP agora!\n')
              
                elif monstro_armor <= roll < (20 - chance_critc_extra): # Quando pega
                    print(f'O ataque pegou! ({roll} na rolagem)')
                    time.sleep(1)
                    chance = random.randint(1,2)
                #Funcionou
                    if chance == 1:
                        print(f'O ataque especial ({atk_spc}) de {nome} funcionou\n{nome} ({level_jogador}) causou {(dado1d10+FOR+HAB)} de dano')
                        monstro_vida = monstro_vida - dado1d10 - FOR - HAB
                        time.sleep(1)
                        print(f'{monstroescolhido} tem {monstro_vida} HP agora!\n')
                #Não funcionou
                    else:
                        print(f'O ataque especial ({atk_spc}) de {nome} falhou')
              
                elif roll == 1:
                    print('Ih mané, tirou 1 no dado, se fodeu')
                    print('Você tropeçou e bateu de cabeça no chão, -3 HP')
                    jogador_vida -= 3
                else:
                    time.sleep(1)
                    print(f'O ataque especial NÃO pegou, tirou {roll} no dado')
            # Pocao
            elif jogada == '3':
                  #Critico
                if roll == 20:
                    time.sleep(1)
                    print(f'{nome} bebeu uma poção (mágica) e recuperou {(rec_hp*2 + HP*0.2)} de HP!')
                    jogador_vida = jogador_vida + (rec_hp*2) + HP*0.2
                    time.sleep(1)
                    print(f'{nome} ({level_jogador}) tem {jogador_vida} HP agora!')
                    if jogador_vida > HP: #Limite de HP
                        print(f'Não é possível aumentar seu HP além de {HP}\n')
                        jogador_vida = HP
                # Normal
                elif monstro_armor <= roll < 20:
                    if poções > 0:
                        time.sleep(1)
                        print(f'{nome} ({level_jogador}) bebeu uma poção e recuperou {(rec_hp)} de HP!')
                        jogador_vida += rec_hp
                        poções -= 1
                        time.sleep(1)
                elif poções <= 0:
                    ações_completa = ações_sem_pot
                    jogador_vida = jogador_vida
                    poções = 0
                    rec_hp = 0
                    print('Voce nao possui mais poções')
                    if jogador_vida >= HP: #Limite de HP
                        jogador_vida = HP
                        time.sleep(1)
                        print(f'Não é possível aumentar seu HP além de {HP}')
                    else:
                        print(f'{nome}({level_jogador}) tem {jogador_vida} HP agora!')
                elif roll == '1':
                    time.sleep(1)
                    poções -= 1
                    print('Ih mané, tirou 1 no dado, se fodeu')
                    print(f'Agora voce tem {poções} poções')
                # Menu
            elif jogada == '4':
                menu()
            else:
                print('Apertou o botao errado')
        #ATAQUE INIMIGO
        if monstro_vida > 0:
            time.sleep(1.5)
            print(linha)
            print(" ")
            print(f' É a vez do {monstroescolhido}!')
            time.sleep(1)
            print(" ")
            ataqueinimigo = random.randint(1,3)
            roll = random.randint(1,20)
            time.sleep(2)

          #Dano crítico inimigo
            if roll >= 20:
                time.sleep(1)
                print('DANO CRÍTICO')
                #Ataque normal 1 crítico
                if ataqueinimigo == 1:
                    time.sleep(1)
                    print(f'{monstroescolhido} causou {dado1d4*2+monstro_dano*2} de dano!')
                    jogador_vida = jogador_vida - dado1d4*2-monstro_dano*2
                    time.sleep(1)
                    print(f'{nome}({level_jogador}) tem {jogador_vida} HP agora!')
                    print(" ")
                #Ataque normal 2 crítico
                elif ataqueinimigo == 2:
                    time.sleep(1)
                    print(f'{monstroescolhido} causou {dado1d6*2+monstro_dano*2} de dano!')
                    jogador_vida = jogador_vida - dado1d6*2-monstro_dano*2
                    time.sleep(1)
                    print(f'{nome}({level_jogador}) tem {jogador_vida} HP agora!')
                    print(" ")
                #Ataque especial crítico
                elif ataqueinimigo == 3:
                    time.sleep(1)
                    chance = random.randint(1,2)
                    #Se o ataque especial pegar
                    if chance == 1:
                        time.sleep(1)
                        print(f'{monstroescolhido} causou {dado1d8*2+monstro_dano*2} de dano!')
                        jogador_vida = jogador_vida - dado1d8*2-monstro_dano*2
                        time.sleep(1)
                        print(f'{nome}({level_jogador}) tem {jogador_vida} HP Agora!')
                        print(" ")
                        #Se o ataque especial não pegar
                    else:
                        time.sleep(1)
                        print(f'O ataque especial de {monstroescolhido} falhou')

              #Quando o ataque do inimigo pegar
            elif ARMOR <= roll < 20:
                time.sleep(1)
                print(f'O ataque pegou, tirou {roll} no dado')
                if ataqueinimigo == 1:
                    time.sleep(1)
                    print(f'{monstroescolhido} causou {dado1d4+monstro_dano} de dano!')
                    jogador_vida = jogador_vida - dado1d4-monstro_dano
                    time.sleep(1)
                    print(f'{nome}({level_jogador}) tem {jogador_vida} HP agora!')
                    print(" ")

                elif ataqueinimigo == 2:
                    time.sleep(1)
                    print(f'{monstroescolhido} causou {dado1d6+monstro_dano} de dano!')
                    jogador_vida = jogador_vida - dado1d6-monstro_dano
                    time.sleep(1)
                    print(f'{nome}({level_jogador}) tem {jogador_vida} HP agora!')
                    print(" ")

                #Ataque especial
                elif ataqueinimigo == 3:
                    time.sleep(1)
                    chance = random.randint(1,2)
                    if chance == 1:
                        time.sleep(1)
                        print(f'{monstroescolhido} causou {dado1d8+monstro_dano} de dano!')
                        jogador_vida = jogador_vida - dado1d8-monstro_dano
                        time.sleep(1)
                        print(f'{nome}({level_jogador}) tem {jogador_vida} HP Agora!')
                        print(" ")
                    else:
                        time.sleep(1)
                        print(f'O ataque especial de {monstroescolhido} falhou')

              #Falha critica
            elif roll == 1:
                time.sleep(1)
                print(f'FALHA CRÍTICA\n{monstroescolhido} tirou 1 no dado!')
                jogador_vida = jogador_vida + dado1d6
                time.sleep(1)
                print(f'O ataque curou {nome}, que tem {jogador_vida} HP agora!')
                print(" ")
              #Quando o ataque inimigo não pegar
            else:
                time.sleep(1)
                print(f'O ataque não pegou, tirou {roll} no dado')

        #Vitória ou derrota
        if jogador_vida < 1:
            time.sleep(1)
            print(' ')
            print(f'{nome} Perdeu...')
            time.sleep(2)
            print(f'''Monstros derrotados: {monstro_derrotado}
            FIM DE JOGO''')
            pontuacao_geral = pontuacao_geral + (monstro_derrotado)*10 + total_critc + total_dano + total_miss
            print(f'Você obteve: {pontuacao}')
            #Acabou o jogo

        if monstro_vida < 1:
            if monstroescolhido == 'Mestre da mesa':
                print('Parabéns, voce finalizou o jogo')
                pontuacao_geral = pontuacao_geral + (monstro_derrotado)*10 + total_critc + total_dano + total_miss
                print(f'Você obteve: {pontuacao}')
            else:
                time.sleep(1)
                print(' ')
                print(f'{nome} Venceu!!')
                time.sleep(2)
                monstro_derrotado +=1
                print(f'Monstros derrotados: {monstro_derrotado}')
                print('='*20)
                time.sleep(2)
                con_menu = input('[Qualquer botão] Continuar a dungeon      [2] Abrir menu\n>>>')
                if con_menu == '2':
                    menu()
                else:
                    print(' ')

        #SISTEMA DE LEVEL
            tabela_exp = range(0, 50, 1)
            tabela_xp = [[0], [1], [2, 2], [3, 3], [4, 4, 4], [5, 5, 5], [6, 6, 6, 6], [7, 7, 7, 7], [8, 8, 8, 8, 8],
                 [9, 9, 9, 9, 9, 9], [10, 10, 10, 10, 10, 10, 10], [11, 11, 11, 11, 11, 11, 11],
                 [12, 12, 12, 12, 12, 12, 12], [13, 13, 13, 13, 13, 13, 13, 13], [14, 14, 14, 14, 14, 14, 14, 14],
                 [15, 15, 15, 15, 15, 15, 15], [16, 16, 16, 16, 16, 16, 16, 16, 16], [17, 17, 17, 17, 17, 17, 17, 17, 17],
                 [18, 18, 18, 18, 18, 18, 18, 18, 18], [19, 19, 19, 19, 19, 19, 19, 19, 19, 19],
                 [20, 20, 20, 20, 20, 20, 20, 20, 20, 20], [21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
                 [22, 22, 22, 22, 22, 22, 22, 22, 22, 22], [23, 23, 23, 23, 23, 23, 23, 23, 23, 23],
                 [24, 24, 24, 24, 24, 24, 24, 24, 24, 24], [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]]

            for i in tabela_exp:
                if monstro_derrotado >= i:
                    level_jogador = len(tabela_xp[i])
                    if level_jogador > 0:
                        if level_novo == level_jogador - 1:
                            print(' ')
                            print('********************'*2)
                            print(f'PARABÉNS, {nome}! PASSOU PARA O LEVEL {level_jogador}')
                            print('********************'*2)
                            level_novo +=1
                            jogador_vida = HP
                            monstro_vida = 10 + (level_jogador * 10)
                            ficha(' ')
                            print('Você ganhou 1 ponto para distribuir em qualquer atributo, escolha um:\n[1]Vitalidade   [2]Força   [3]Destreza   [4]Habilidade')
                            dist = input('>>> ')
                            if dist == '1':
                                HP += 10
                            elif dist == '2':
                                FOR += 1
                            elif dist == '3':
                                DES += 1
                            elif dist == '4':
                                HAB += 1
                            else:
                                dist = input('Botao, errado, tente novamente')
                            ficha('nova ')

                else:
                    level_jogador += 0
    monstroescolhido =  random.choice(monstros[level_jogador])
    print(' ')
    print(f'{monstroescolhido} apareceu!!')
    time.sleep(1)
    monstro_vida = 10 + (level_jogador * 10)

elif escolha_inicial == '2':
   print('\n\n\n\n\n\n')
   time.sleep(1)
   print('Obrigado, volte sempre!')
   def sair(s):
       for i in range(1,s):
           time.sleep(1)
           print(s-i)
   sair(4)
else:
    escolha_inicial = input('Alternativa desconhecida, por favor tente novamente\n>>> ')
