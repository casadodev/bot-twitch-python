# bot.py
import asyncio
import configparser
import random
import requests
import time
from requests_html import HTMLSession
from twitchio.ext import commands


config = configparser.ConfigParser()
config.read('config.ini')

nick_bot = 'casadodevbot'
inicia_canal = 'casadodev'


bot = commands.Bot(
    # set up the bot
    irc_token = config['bot']['token'],
    client_id = config['bot']['client_id'],
    nick = nick_bot,
    prefix = '!',
    initial_channels = [inicia_canal]
)


# parou


# globais

latidos = 0
pessoas_online = []
count_pessoa = []


@bot.event
async def event_ready():
    'Chama quando o bot está online.'
    print(f"@{nick_bot} está online!")
    ws = bot._ws  # só é chamado no evento inicial

    await ws.send_privmsg(inicia_canal, 'O bot está online!')

    while True:
        'Mostrando os comandos disponíveis no bot'

        msg_aleatoria = list(open('files/texto_engajamento.txt', encoding='utf-8'))
        comandos = '/me os comandos do bot são: "exclamação +" ban, clima, piada, traduzir (+texto português), translate (+text english), motivar, horoscopo, susto, filme. Tudo desenvolvido nas lives e em python!'

        await ws.send_privmsg(inicia_canal, comandos)
        await asyncio.sleep(500.0)

        if len(msg_aleatoria) > 0:
            'Mostrando mensagens de engajamento no chat'
            msg_selecionada = random.choice(msg_aleatoria)

            await ws.send_privmsg(inicia_canal, msg_selecionada)
            await asyncio.sleep(20.0)


@bot.command(name='points')
async def fn_points(ctx):
    return


@bot.command(name='sh-so')
async def fn_shso(ctx):
    return


@bot.command(name='addpoints')
async def fn_addpoints(ctx):
    return


@bot.command(name='commands')
async def fn_addcommands(ctx):
    return ''


# @bot.command(name='tenhafoco')
# async def fn_pararBesteira(ctx):
#     pessoa = ctx.


# @bot.command(name='ad')
# async def fn_ad(ctx):
#     while True:
#         await ctx.channel.send('/commercial 30')
#         print('Ad iniciado')
#         await ctx.send_me('Eu iniciei um ad. Diz ae se você Tankou :)')
#         await asyncio.sleep(750.0)


@bot.command(name='wp')
async def fn_whatsapp(ctx):
    await ctx.send_me('Grupo no whatsapp https://chat.whatsapp.com/GjztcHTQiXb0MNZutOhCOY')


@bot.command(name='discord')
async def fn_discord(ctx):
    await ctx.send_me('Grupo no discord https://mercadodeti.com.br/discord')

@bot.command(name='instagram')
async def fn_instagram(ctx):
    await ctx.send_me('Perfil no Inta https://instagram.com/casadodev')


@bot.command(name='sorteio')
async def fn_sorteio(ctx):
    await ctx.send_me('Sorteios de cursos da Udemy de até R$40. Subs/Inscritos tem 3x mais chances de ganhar. O sorteio vai ser só para quem segue o canal a mais de 2h, ou inscritos. Se inscreva gratuitamente com seu Amazon Prime!')


# Super susto do @ChicoCodes
@bot.command(name='tapao')
async def fn_sustoTapao(ctx):
    await ctx.send_me('Veja o clipe do super susto que o @ChicoCodes me deu e quase tudo https://clips.twitch.tv/CoweringSpunkyMochaSpicyBoy hahaha')


# TODO: pedido de músicas no canal - por @Super_Feliz
@bot.command(name='musica')
async def fn_adicionaMusica(ctx):

    await ctx.send('Está sendo desenvolvido comando para tocar as músicas no canal')


# TODO: comando solicitado pelo Marlon_Henq
# Cria um comando de correio elegante onde vc pode pedir para o bot mandar uma mensagem para alguém
# frases para enviar https://www.pensador.com/frases_para_correio_elegante/


# TODO: comando solicitado pelo @ccesar88
# coloca javaxpython pra vc comentar o que é melhor ou pior das linguagens, não sei , o que acha?
@bot.command(name='javaxpython')
async def fn_comparaJavaPython(ctx):
    await ctx.send(f'/me comparando java x python - desenvolvendo')


#Comando cachorro
@bot.command(name='cachorro')
async def fn_cachorro(ctx):
    latidos = latidos + 1
    await ctx.send(f'/me O cachorro já latiu {latidos} vez(es)')


# TODO: comando solicitado pelo @Tairritadotio
@bot.command(name='dica')
async def fn_dica(ctx):
    await ctx.send('/me Se der erro no seu código poder ser que algo esteja errado ou algo não esteja certo.')


# comando para dicas de filmes
@bot.command(name='filme')
async def fn_filme(ctx):

    filme_indicado = 'Qualquer um do Nicolas Cage'

    print(f'Filme indicado: {filme_indicado}')

    await ctx.send(f'/me Nosso bot te indica o filme: {filme_indicado}')


# TODO: traduzir texto por - PO: @ChicoCodes, com grande ajuda do MechanicallyDev
'ENTREGA DO MPV 1 PARA O CHICOCODES'
@bot.command(name='traduzir')
async def fn_traduzir(ctx):
    'Traduz o texto para inglês'
    texto_solicitado = '+'.join(ctx.content.split(' ')[1:])

    session = HTMLSession()
    url = 'https://www.google.com/search?q=translate+to+english+'

    url_unificado = f'{url}{texto_solicitado}'

    req_selecionada = session.get(url_unificado)
    texto_traduzido = req_selecionada.html.find('#tw-target-text')[0].text
    print(f'Tradução: {texto_traduzido}')

    await ctx.send(f'/me translate: {texto_traduzido}')


# TODO: vai levar timeout de 30 segundos na próxima
# TODO: biscoito / robson - por @ChicoCodes
@bot.command(name='robson')
async def fn_robson(ctx):
    await ctx.send(f'/me @{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN. Chico disse, ta DITOOO!')


# TODO: biscoito / robson - por @ChicoCodes
@bot.command(name='biscoito')
async def fn_biscoito(ctx):
    await ctx.send(f'/me @{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN. Chico disse, ta DITOOO!')


# TODO: traduzir texto por - PO: @ChicoCodes, com grande ajuda do MechanicallyDev
'ENTREGA DO MPV 1 PARA O CHICOCODES'
@bot.command(name='translate')
async def fn_translate(ctx):
    'Traduz o texto para portugues'
    texto_solicitado = '+'.join(ctx.content.split(' ')[1:])

    session = HTMLSession()
    url = 'https://www.google.com/search?q=translate+to+portuguese+'

    url_unificado = f'{url}{texto_solicitado}'

    req_selecionada = session.get(url_unificado)
    texto_traduzido = req_selecionada.html.find('#tw-target-text')[0].text
    print(f'Tradução: {texto_traduzido}')

    await ctx.send(f'/me translate: {texto_traduzido}')


# TODO: mostrar horóscopo
@bot.command(name='horoscopo')
async def fn_horoscopo(ctx):
    'Mostra o signo solicitado, com base no site Capricho'

    session = HTMLSession()
    url_signos = 'https://capricho.abril.com.br/horoscopo/signo-'
    signo_solicitado = ctx.content.split(' ')[1]

    req_selecionada = session.get(f'{url_signos}{signo_solicitado}/')
    signo_selecionado = req_selecionada.html.find('.previsao_dia')[0].text

    await ctx.send(f'/me {signo_solicitado}: {signo_selecionado}')


# TODO: Tratar localization
# comando de previsão do tempo - pedido do @MechanicallyDev
@bot.command(name='clima')
async def fn_climaTempo(ctx):
    # Mostrar a previsão do tempo da região
    session = HTMLSession()

    cidade_solicitada = '+'.join(ctx.content.split(' ')[1:])

    req_selecionada = session.get(f'https://www.google.com.br/search?q=tempo+{cidade_solicitada}')

    cidade_selecionada = req_selecionada.html.find('#wob_loc')[0].text
    temperatura_atual = req_selecionada.html.find('#wob_tm')[0].text
    horario_atual = req_selecionada.html.find('#wob_dts')[0].text
    tipo_clima = req_selecionada.html.find('#wob_dc')[0].text

    # as unidades são especificadas em spans, precisamos inspecionar qual está
    # visível
    spans_unidade = req_selecionada.html.find('.wob-unit > span.wob_t')
    unidade = 'ºC'
    for span_unidade in spans_unidade:
        if span_unidade.attrs['style'] == 'display:inline':
            unidade = span_unidade.text

    print(f'Clima agora em {cidade_selecionada}: {temperatura_atual}')

    await ctx.send(f'/me Agora na cidade {cidade_selecionada}, é {horario_atual} e está {temperatura_atual}{unidade}, com um clima {tipo_clima}')
    # await ctx.send('Está frio pra caramba em Itajaí! - teste em produção com sucesso')


# TODO: filtrar palavras para blacklist e frases já liberadas pelo id
# foi um ótimo resgate realizado pelo @MechanicallyDev
@bot.command(name='piada')
async def fn_piadas(ctx):
    # https://api-de-charadas.fredes.now.sh/

    # piada_selecionada = requests.get(
    #     'https://us-central1-kivson.cloudfunctions.net/charada-aleatoria',
    #     headers={
    #         'Accept': 'application/json',
    #         'Content-type': 'application/json'
    #     }).json()

    piada_selecionada = requests.get('https://api-de-charadas.fredes.now.sh').json()

    print(f"pergunta: {piada_selecionada['question']}")
    print(f"resposta: {piada_selecionada['answer']}")

    pergunta = piada_selecionada['question']
    resposta = piada_selecionada['answer']

    await ctx.send(f'/me Pergunta: {pergunta}')

    time.sleep(15)
    await ctx.send(f'/me Resposta: {resposta}')


@bot.command(name='motivar')
async def fn_motivacao(ctx):
    'Mensagem motivacional para o chat'
    session = HTMLSession()
    req_selecionada = session.get('https://motivaai.nandomoreira.dev/')

    motivacao_selecionada = req_selecionada.html.find(
        'blockquote')[0].text.split('\n')

    frase = motivacao_selecionada[0]
    autor = motivacao_selecionada[1]

    print(f"Frase de {autor}: {frase}")

    await ctx.send(f'/me "{frase}", por {autor}')


@bot.command(name='addengajar')
async def fn_add_mensagem_engajamento(ctx):
    if len(ctx.content) > 30:
        # gravar a mensagem de ban comprada pelo usuário
        arquivo_texto_engajamento = open(
            'files/texto_engajamento.txt', 'a+', encoding='utf-8')

        arquivo_texto_engajamento.write(f"{ctx.content.lower()[12:]} \n")
        # TODO: CRIAR MÉTODO PARA ADICIONAR EM VOTAÇÃO NO CHAT
        arquivo_texto_engajamento.close()

        print(f"texto de engajamento adicionado por @{ctx.author.name}")
        await ctx.send('Mensagem de engajamento adicionada. aguardando aprovação.')

    if len(ctx.content) < 30:
        await ctx.send('Mensagem precisa ter pelo menos 30 caracteres.')


# foi uma ótima idéia do @Falvern_
@bot.command(name='unban')
async def fn_unBan(ctx):
    frase = 'invoca carta imbanivel e não pode ser banido!'
    await ctx.send(f"@{ctx.author.name} {frase}")


@bot.command(name='ban')
async def fn_ban(ctx):
    if len(ctx.content.split(' ')[1]) < 4:
        await ctx.send("para banir alguém, é preciso incluir o nome o usuário")

    if len(ctx.content.split(' ')[1]) > 3:
        lista_ban = open('files/texto_bans.txt', encoding='utf-8')

        banido = ctx.content.lower().split(' ')[1]
        tipo_ban = random.choice(list(lista_ban))

        print(
            f"comando de banir executado por @{ctx.author.name} para o @{banido}")

        await ctx.send(f"{banido} {tipo_ban}")
        # await Messageable.timeout(banido, 15, tipo_ban)
        # await ctx.send(f"/timeout {banido} 20")
        # await ctx.send(f".timeout {banido} 20")


@bot.command(name='addban')
async def fn_addban(ctx):
    if len(ctx.content) > 30:
        # gravar a mensagem de ban comprada pelo usuário

        arquivo_texto_bans = open(
            'files/texto_moderacao_bans.txt', 'a+', encoding='utf-8')

        arquivo_texto_bans.write(f"{ctx.content.lower()[8:]} \n")
        # TODO: CRIAR MÉTODO PARA ADICIONAR EM VOTAÇÃO NO CHAT
        arquivo_texto_bans.close()

        print(f"texto de ban adicionado por @{ctx.author.name}")
        await ctx.send('Mensagem de ban adicionada. aguardando aprovação.')


# @bot.command(name='atividade')
# async def fn_chat(ctx, nick='casadodevbot'):
    # 'QUANTIDADE DE MENSAGENS QUE A PESSOA ENVIOU NA LIVE'
    # msg_pessoas = open('files/quantidade_pessoas.txt', encoding='utf-8')

    # sets = set(pessoas_online)

    # a = [1,2,3,4,5]
    # b = [4,5,6,7,8]

    # for pessoa in sets:
        # for count in count_pessoa:
        # if count
        # count_pessoa.append([])
        # print(f'online {count_pessoa}')

    # await ctx.send(f'{1 + 5}')


@bot.event
async def event_message(ctx):
    'Roda toda vez que uma mensagem no chat é enviada.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == nick_bot.lower():
        return

    # TODO: quantas letras a pessoa escreveu no chat
    pessoas_online.append(ctx.author.name)

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if 'bom dia' in ctx.content.lower():
        await ctx.channel.send(f"Bom dia, @{ctx.author.name}! Como você está?")

    if 'boa tarde' in ctx.content.lower():
        await ctx.channel.send(f"Boa tarde, @{ctx.author.name}! Como você está?")

    if 'boa noite' in ctx.content.lower():
        await ctx.channel.send(f"Boa noite, @{ctx.author.name}! Como você está?")

    if 'boa madrugada' in ctx.content.lower():
        await ctx.channel.send(f"Boa madrugada aeew, @{ctx.author.name}! Como você está?")

    # culpa do @Super_Feliz - o tecladod ele o trolou
    if 'boa note' in ctx.content.lower():
        await ctx.channel.send(f"Boa noite, @{ctx.author.name}! Como você está? Seu teclado te trolou...")

    if 'salve' in ctx.content.lower():
        await ctx.channel.send(f"Ta salvado, @{ctx.author.name}! Como você está?")

    if 'ctrl + s' in ctx.content.lower():
        await ctx.channel.send(f"Ta salvado, @{ctx.author.name}! Como você está?")

    if 'aoba' in ctx.content.lower():
        await ctx.channel.send(f"Aoooba, @{ctx.author.name}! Como você está?")

    if 'lurk' in ctx.content.lower():
        await ctx.channel.send(f"Opa @{ctx.author.name}! Tamo junto ae no lurk. Já ajuda pakas.")

    if 'bolacha' in ctx.content.lower():
        await ctx.channel.send(f'/me @{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN. Chico disse, ta DITOOO!')

@bot.command(name='test')
async def test(ctx):
    await ctx.send('teste passou.')


if __name__ == "__main__":
    bot.run()

