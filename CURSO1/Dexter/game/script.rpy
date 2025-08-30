# The script of the game goes in this file.

# The game starts here.

#Personagens
define d = Character("Dexter", color="#fa0e0e") # detetive/principal
define g = Character("Gracie", color="#1e9e33") # Patricinha/aniversariante
define h = Character("Hope", color="#f82ebb") # Fofa/ Ama o Dexter
define r = Character("Ross", color="#1ac0b2") # vilão/nice guy
define k = Character("Karen", color="#f38226") # Otaku/ irmã do Viktor
define v = Character("Viktor", color="#0d1df0") # Inteligente/Nerd
define l = Character("Lunna", color="#44105c") # Emo/Rock
define c = Character("Karen e Viktor", color="#814a0a") # dupla
define z = Character("", color="#000000") # aleatorio

#Imagens Gracie
image gracie = "images/gracie/gracie.png"
image gracie_feliz = "images/gracie/gracie_feliz.png"
image gracie_timida = "images/gracie/gracie_timida.png"
image gracie_presente = "images/gracie/gracie_presente.png"
image gracie_brava1 = "images/gracie/gracie_brava1.png"
image gracie_brava2 = "images/gracie/gracie_brava2.png"
image gracie_brava3 = "images/gracie/gracie_brava3.png"
image gracie_kill2 = "images/gracie/gracie_kill2.png"
image gracie_triste1 = "images/gracie/gracie_triste1.png"
image gracie_triste2 = "images/gracie/gracie_triste2.png"
image gracie_triste3 = "images/gracie/gracie_triste3.png"

#Imagens Ross
image ross = "images/ross/Ross.png"
image ross_boy1 = "images/ross/ross_boy1.png"
image ross_boy2 = "images/ross/ross_boy2.png"
image ross_boy3 = "images/ross/ross_boy3.png"
image ross_bravo1 = "images/ross/ross_bravo1.png"
image ross_bravo2 = "images/ross/ross_bravo2.png"
image ross_feliz1 = "images/ross/ross_feliz1.png"
image ross_feliz2 = "images/ross/ross_feliz2.png"
image ross_killer1 = "images/ross/ross_killer1.png"
image ross_killer2 = "images/ross/ross_killer2.png"
image ross_killer3 = "images/ross/ross_killer3.png"
image ross_triste1 = "images/ross/ross_triste1.png"
image ross_triste2 = "images/ross/ross_triste2.png"

#Imagens Hope
image hope = "images/hope/hope.png"
image hope_feliz = "images/hope/hope_feliz.png"
image hope_feliz2 = "images/hope/hope_feliz2.png"
image hope_timida = "images/hope/hope_timida.png"
image hope_brava1 = "images/hope/hope_brava1.png"
image hope_brava2 = "images/hope/hope_brava2.png"
image hope_brava3 = "images/hope/hope_brava3.png"
image hope_kill1 = "images/hope/hope_kill1.png"
image hope_kill4 = "images/hope/hope_kill4.png"
image hope_triste1 = "images/hope/hope_triste1.png"
image hope_triste2 = "images/hope/hope_triste2.png"
image hope_triste3 = "images/hope/hope_triste3.png"
 
#Imagens Lunna
image lunna = "images/lunna/lunna.png"
image lunna_feliz1 = "images/lunna/lunna_feliz1.png"
image lunna_feliz2 = "images/lunna/lunna_feliz2.png"
image lunna_feliz3 = "images/lunna/lunna_feliz3.png"
image lunna_feliz4 = "images/lunna/lunna_feliz4.png"
image lunna_beer = "images/lunna/lunna_beer.png"
image lunna_beer1 = "images/lunna/lunna_beer1.png"
image lunna_beer2 = "images/lunna/lunna_beer2.png"
image lunna_brava1 = "images/lunna/lunna_brava1.png"
image lunna_brava2 = "images/lunna/lunna_brava2.png"
image lunna_cake = "images/lunna/lunna_cake.png"
image lunna_triste1 = "images/lunna/lunna_triste1.png"
    
#Imagens Karen
image karen = "images/karen/karen.png"
image karen_feliz1 = "images/karen/karen_feliz1.png"
image karen_feliz2 = "images/karen/karen_feliz2.png"
image karen_doce1 = "images/karen/karen_doce1.png"
image karen_doce2 = "images/karen/karen_doce2.png"
image karen_doce3 = "images/karen/karen_doce3.png"
image karen_cake = "images/karen/karen_cake.png"


#Imagens Viktor
image viktor = "images/viktor/viktor.png"
image viktor_feliz1 = "images/viktor/viktor_feliz1.png"
image viktor_feliz2 = "images/viktor/viktor_feliz2.png"
image viktor_feliz3 = "images/viktor/viktor_feliz3.png"

#Imagens Cenarios:
image celular = "images/celular.png"
image casa = "images/casa1.jpg"
image sala = "images/sala.png"
image bolo = "images/bolo.png"
image danca = "images/danca.png"
image banheiro = "images/banheiro.png"
image quarto = "images/quarto.png"
image policia = "images/policia.png"

#-------------------------------------------------------------------------
#Jogo começa aqui:

label start:
    stop music

    scene black with fade
    play sound "audio/sms.mp3"
    "Plim...Plim *SMS recebido.*"
    stop sound fadeout 2.0

    scene celular at center:
        zoom 1.3
        yalign 0.1
    with fade
    
    d "Hnmmm..."
    menu:
        "Você se arruma e vai a festa.":
            jump festa

        "você está exausto e vai dormir.":
            # jump hope
            return

label festa:
    scene casa:
        zoom 1.3
        yalign 0.1
    with fade

    play sound "audio/toc_toc.mp3" fadein 1.0
    z "Toc Toc Toc"
    stop sound fadeout 1.0

    show gracie_feliz at left:
        zoom 0.8
    with dissolve

    g "DEXTER!"
    g "Estou muito feliz, que você veio."
    hide gracie_feliz

    menu:
        "Entregar o Presente":
            show gracie_presente at left:
                zoom 0.5
            g "Muito Obrigada!"
            hide gracie_presente

    show gracie_feliz at left:
        zoom 0.8

    g "Venha, vamos entrar!"

label sala:
    scene sala at center:
        zoom 1.3
        yalign 0.1
    with fade
    
    show ross_boy3 at left:
        zoom 0.8
    with dissolve
    r "E aí mano, você realmente veio..."
    hide ross_boy3

    show ross_boy1 at left:
        zoom 0.8
    with dissolve
    r "...Podia ter ficado em casa."
    hide ross_boy1

    menu:
        "O que você disse?":
            show ross_bravo2 at left:
                zoom 0.8
            r "Nada não mano..."
            hide ross_bravo2
    z "*...Ross sai revirando os olhos*"

    show karen_feliz1 at center:
        zoom 0.7
    with dissolve

    show viktor_feliz2 at left:
        zoom 0.8
    with dissolve
    c "Oi Dexter!"
    c "Quem bom que veio"
    c "Você estava sumido..."
    hide karen_feliz1
    hide viktor_feliz2

    show viktor_feliz3 at left:
        zoom 0.8
    with dissolve

    show karen_doce2 at center:
        zoom 0.7
    with dissolve
    k "Amigo, quer doce?"
    k "Eu trouxe vários."
    hide karen_doce2
    hide viktor_feliz3

    menu:
        "Aceitar o Doce":
            show karen_doce1 at center:
                zoom 0.7
            show viktor_feliz1 at left:
                zoom 0.8
            k "Eu trouxe o bolo também, está tudo delicioso!"
            hide karen_doce1
            hide viktor_feliz1

        "Recusar o Doce":
            show karen_doce3 at center:
                zoom 0.7
            show viktor at left:
                zoom 0.5
            k "Quando quiser é só ir pegar!"
            hide karen_doce3
            hide viktor
    
    z "*Viktor e Karen saem para se divertir...*"

    show lunna_feliz4 at left:
        zoom 0.8
    with dissolve
    l "Ei moleque, ainda bem que você chegou."
    hide lunna_feliz4

    show lunna_brava1 at left:
        zoom 0.8
    with dissolve
    l "Tá um porre essas músicas..."
    hide lunna_brava1

    show lunna_feliz1 at left:
        zoom 0.8
    with dissolve
    l "Aproveita e pega uma cerveja aí..."
    hide lunna_feliz1

    menu:
        "Pegar a  cerveja de vocês":
            show lunna_feliz3 at left:
                zoom 0.8
            l "Bem gelada, heim!"
            hide lunna_feliz3

        "Dizer não e ir buscar apenas a sua.":
            show lunna_brava1 at left:
                zoom 0.8
            l "Tu é um porre moleque!"
            hide lunna_brava1

    "*Você vai pegar cerveja...*"

    show hope_feliz at left:
        zoom 0.8
    with dissolve
    h "Oi lindo! Amei sua roupa."
    hide hope_feliz

    menu:
        "Oi Cheirosa!":
            z ""

        "Linda é você.":
            z ""
    
    show hope_timida at left:
        zoom 0.8
    with dissolve
    h "Hahah, bobinho"
    h "Depois do parabéns, queria te mostrar uma coisa..."
    hide hope_timida

    show hope_feliz2 at left:
        zoom 0.8
    with dissolve
    h "no banheiro."
    h "Vou lhe esperar..."
    hide hope_feliz2

    "*Hope sai corada e tímida.*"

    show lunna_beer1 at left:
        zoom 0.8
    with dissolve        
    l "Ei, Moleque!"
    hide lunna_beer1

    show lunna_beer2 at left:
        zoom 0.8
    with dissolve    
    l "Aquele Ross é um saco!"
    l "Não sai do lado da Gracie"
    l "Tá na cara que ela não quer ele."
    hide lunna_beer2

    menu:
        "Concordo, vou falar com ela":
            z ""

    show gracie_feliz at left:
        zoom 0.8
    with dissolve
    g "Dexter!"
    g "Está gostando da festa?"
    hide gracie_timida

    show ross_boy1 at right:
        zoom 0.8
    with dissolve
    "*Ross encarando, tentando entender a conversa.*"
    hide ross_boy1

    show gracie_feliz at left:
        zoom 0.8
    with dissolve
    g "Queria muito conversar com você"
    g "Depois do parabéns, vou te esperar no meu quarto."
    hide gracie_timida

    scene black with fade
    "*Karen aumenta o volume da música*"
    scene danca at center:
        zoom 1.3
        yalign 0.1
    with fade
    "*Todos vão dançar*"

    scene sala:
        zoom 1.3
        yalign 0.1
    with fade

    show hope_feliz at left:
        zoom 0.8
    with dissolve
    h "Dança comigo?"
    hide hope_feliz

    show gracie_timida at center:
        zoom 0.8
    with dissolve
    g "Amiga!?"
    hide gracie_timida

    show gracie_brava1 at center:
        zoom 0.8
    with dissolve
    g "..."
    g "Ele vai dançar comigo!"
    hide gracie_brava1

    show ross_boy2 at right:
        zoom 0.8
    with dissolve
    r "Urgh!"
    r "Ele nem sabe dançar."
    hide ross_boy2

    show gracie_brava2 at center:
        zoom 0.8
    with dissolve
    g "E você sabe?"
    hide gracie_brava2

    show ross_bravo2 at right:
        zoom 0.8
    with dissolve
    r "Eu sei te fazer feliz!"
    hide ross_bravo2

    show ross_feliz1 at right:
        zoom 0.8
    with dissolve
    r "...Serve?"
    hide ross_feliz1

    show gracie_brava1 at center:
        zoom 0.8
    with dissolve
    g "..."
    hide gracie_brava1


    show gracie_feliz at center:
        zoom 0.8
    with dissolve
    g "Vamos cortar o bolo"
    hide gracie_feliz


label bolo:
    scene bolo at center:
        zoom 1.3
        yalign 0.1
    with fade

    play sound "audio/parabens.mp3" fadein 1.0
    "*Todos cantam parabéns.*"
    v "Parabéns Gracie!"
    l "Uhuuul!"
    k "*Batendo palmas*"
    h "Isso aí, amiga!"
    r "..."
    stop sound fadeout 1.0

    scene sala:
        zoom 1.3
        yalign 0.1
    with fade

    "*Gracie se retira e vai ao quarto.*"

    show lunna_cake at right:
        zoom 0.5
    with dissolve
    l "Que bolo delicioso!"
    hide lunna_cake

    "*Hope te olha e sai em direção ao banheiro.*"

    show karen_cake at right:
        zoom 0.5
    with dissolve
    k "Está uma delícia mesmo."
    hide karen_cake

    menu:
        "Seguir a Gracie":
            jump gracie
        "Seguir a Hope":
            jump hope
    
label gracie:
    scene black:
        "*Você segue em direção ao quarto.*"
    scene quarto:
        zoom 1.3
        yalign 0.1
    with fade

    show ross_killer2 at left:
        zoom 0.8
    with dissolve
    r "..."
    hide ross_killer2

    show ross_killer3 at left:
        zoom 0.8
    with dissolve
    r "Eu...Eu...Não fiz nada"
    r "Não foi eu..."
    hide ross_killer3

    show gracie_kill2 at right:
        yalign 0.7
        zoom 0.8
    with dissolve
    "..."
    "*Ross sai do local correndo*"
    
    show viktor at left:
        zoom 0.5
    with dissolve
    "*Viktor está assustado"
    hide viktor

    show karen at left:
        zoom 0.5
    with dissolve
    k "..."
    k "GRACIE?"
    hide karen

    show lunna_triste1 at left:
        zoom 0.5
    with dissolve
    l "...MEU DEUS"
    l "NÃOOOOOOO"
    hide lunna_triste1

    scene black with fade
    menu:
        "Acusar Ross":
            "..."
        "Chamar a polícia":
            jump policia


    scene sala:
            zoom 1.3
            yalign 0.1
    with fade

    d "O QUE VOCÊ FEZ? SEU MALDITO!"

    show ross_killer1 at left:
        zoom 0.8
    with dissolve
    r "EU NÃO FIZ NADA CARA..."
    hide ross_killer1

    show ross_killer2 at left:
        zoom 0.8
    with dissolve
    r "EU JURO!"
    hide ross_killer2

    d "VOCÊ VAI PAGAR POR ISSO!"

    menu:
        "Agredir Ross":
            d"VOCÊ VAI MORRER!"
                
        "Chamar a polícia":
            jump policia

    show ross_triste2 at left:
        zoom 0.8
    with dissolve
    "*Ross chorando*"
    hide ross_triste2

    show hope_kill1 at right:
        zoom 0.8
    with dissolve
    h "..."
    hide hope_kill1


    return
   

label hope:
    scene black:
        "*Você segue em direção ao banheiro.*"
    scene banheiro:
        zoom 1.3
        yalign 0.1
    with fade

    show ross_killer2 at left:
        zoom 0.8
    with dissolve
    r "..."
    hide ross_killer2

    show ross_killer3 at left:
        zoom 0.8
    with dissolve
    r "Eu...Eu...Não fiz nada"
    r "Não foi eu..."
    hide ross_killer3

    show hope_kill4 at right:
        yalign 0.7
        zoom 0.6
    with dissolve
    "..."
    "*Ross sai do local correndo*"
    
    show viktor at left:
        zoom 0.5
    with dissolve
    "*Viktor está assustado"
    hide viktor

    show karen at left:
        zoom 0.5
    with dissolve
    k "..."
    k "HOPE?"
    hide karen

    show lunna_triste1 at left:
        zoom 0.5
    with dissolve
    l "...MEU DEUS"
    l "NÃOOOOOOO"
    hide lunna_triste1

    scene black with fade
    menu:
        "Acusar Ross":
            "..."
        "Chamar a polícia":
            jump policia

    scene sala:
            zoom 1.3
            yalign 0.1
    with fade

    d "O QUE VOCÊ FEZ? SEU MALDITO!"

    show ross_killer1 at left:
        zoom 0.8
    with dissolve
    r "EU NÃO FIZ NADA CARA..."
    hide ross_killer1

    show ross_killer2 at left:
        zoom 0.8
    with dissolve
    r "EU JURO!"
    hide ross_killer2

    d "VOCÊ VAI PAGAR POR ISSO!"

    menu:
        "Agredir Ross":
            d"VOCÊ VAI MORRER!"
                
        "Chamar a polícia":
            jump policia

    show ross_triste2 at left:
        zoom 0.8
    with dissolve
    "*Ross chorando*"
    hide ross_triste2

    show gracie_triste2 at right:
        zoom 0.8
    with dissolve
    h "..."
    hide gracie_triste2

    return

label policia:
        scene policia:
            zoom 1.3
            yalign 0.1
        with fade
        "*Ross é preso.*"

        return

    # return



