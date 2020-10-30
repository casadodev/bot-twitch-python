# bot.py
import asyncio
import configparser
import json
import random
import time
from datetime import datetime

import requests
from requests_html import HTMLSession
from twitchio.ext import commands

config = configparser.ConfigParser()
config.read("config.ini")

nick_bot = "casadodevbot"
inicia_canal = "casadodev"


bot = commands.Bot(
    # set up the bot
    irc_token=config["bot"]["token"],
    client_id=config["bot"]["client_id"],
    nick=nick_bot,
    prefix="!",
    initial_channels=[inicia_canal],
)

# globais
counters = {}
pessoas_online = []
count_pessoa = []


@bot.event
async def event_ready():
    "Chama quando o bot está online."
    print(f"@{nick_bot} está online! ")
    ws = bot._ws  # só é chamado no evento inicial

    await ws.send_privmsg(inicia_canal, f"@{nick_bot} está online!")

    while True:
        "Mostrando os comandos disponíveis no bot"

        msg_aleatoria = list(
            open("files/texto_engajamento.txt", encoding="utf-8"),
        )
        comandos = (
            '/me os comandos do bot são "exclamação + :" ban +usuário, '
            "clima +local, piada, traduzir +mensagem, translate +message, "
            "motivar, horoscopo +signo, susto, filme. "
            "Tudo desenvolvido nas lives e em python!"
        )

        await ws.send_privmsg(inicia_canal, comandos)
        await asyncio.sleep(480.0)

        if len(msg_aleatoria) > 0:
            "Mostrando mensagens de engajamento no chat"
            msg_selecionada = random.choice(msg_aleatoria)

            await ws.send_privmsg(inicia_canal, msg_selecionada)
            await asyncio.sleep(20.0)


# Trata todos erros, por exemplo, comando inexistente
@bot.event
async def event_command_error(ctx, error):
    pass


@bot.command(name="steam")
async def fn_steam(ctx):
    link = "https://s.team/p/gdmd-fkhb/fmdrjvgt"
    await ctx.send_me(
        f'Jogue conosco usando o código "1115830096" ou usando o link {link}',
    )


@bot.command(name="bot")
async def fn_bot(ctx):
    link = "https://github.com/casadodev/bot-twitch-python"
    await ctx.send_me(
        f"Deseja ajudar na construção do bot!? acesse o link e torne-se um contribuidor {link}",
    )


@bot.command(name="botwp")
async def fn_whatsapp(ctx):
    await ctx.send_me(
        "Grupo no whatsapp https://chat.whatsapp.com/GjztcHTQiXb0MNZutOhCOY",
    )


@bot.command(name="botdiscord")
async def fn_discord(ctx):
    await ctx.send_me("Grupo no discord https://mercadodeti.com.br/discord")


@bot.command(name="botinstagram")
async def fn_instagram(ctx):
    await ctx.send_me("Perfil no Inta https://instagram.com/casadodev")


@bot.command(name="evento")
async def fn_evento(ctx):
    await ctx.send_me(
        "Dia 23/10 as 17:00h, venha participar do HacktoberFest do CasadoDev - https://casado.dev",
    )


@bot.command(name="horasorteio")
async def fn_horasorteio(ctx):
    await ctx.send_me("HORA DO SORTEIO!!!!!!")
    await ctx.send_me("VENHA PARTICIPAR")
    await ctx.send_me("QUEM SERÁ O SORTUDO DA NOITE Kappa")


@bot.command(name="sorteio")
async def fn_sorteio(ctx):
    await ctx.send_me(
        "Sorteios de cursos da Udemy de até R$40. Subs/Inscritos tem 3x mais chances de ganhar. "
        "O sorteio está disponível apenas para quem segue o canal a mais de 2h, ou inscritos. "
        "Se inscreva gratuitamente com seu Amazon Prime!",
    )


# Super susto do @ChicoCodes
@bot.command(name="tapao")
async def fn_sustoTapao(ctx):
    await ctx.send_me(
        "Veja o clipe do super susto que o @ChicoCodes me deu e "
        "quase tudo https://clips.twitch.tv/CoweringSpunkyMochaSpicyBoy hahaha",
    )


@bot.command(name="fiature")
async def fn_feature(ctx):
    await ctx.send_me(
        "Aprenda a pronunciar feature! https://clips.twitch.tv/SmellyPluckyBubbleteaStinkyCheese",
    )


# TODO: pedido de músicas no canal - por @Super_Feliz
@bot.command(name="musica")
async def fn_adicionaMusica(ctx):
    await ctx.send("Está sendo desenvolvido comando para tocar as músicas no canal")


# TODO: comando solicitado pelo Marlon_Henq
# Cria um comando de correio elegante onde vc pode pedir para o bot mandar uma mensagem para alguém
# frases para enviar https://www.pensador.com/frases_para_correio_elegante/


def create_counter(*, name, prefix, singular="vez", plural="vezes"):
    @bot.command(name=name)
    async def _counter(ctx):
        date = datetime.now()
        with open("files/counters.json") as current_json:
            raw_json = json.load(current_json)
            amount = raw_json[name]["qtd"] = raw_json[name]["qtd"] + 1
            current_list_dates = raw_json[name]["dates"]
            current_list_dates.append(date.strftime("%d/%m/%Y %H:%M:%S"))

        suffix = plural if amount > 1 else singular
        await ctx.send_me(f"{prefix} {amount} {suffix}")

        with open("files/counters.json", "w") as file_write:
            json.dump(raw_json, file_write)


create_counter(name="cachorro", prefix="O cachorro já latiu")
create_counter(name="risada", prefix="A Mirele já riu")
create_counter(name="taxado", prefix="O Casado já foi taxado")
create_counter(name="breja", prefix="O Casado já bebeu")
create_counter(name="chat", prefix="O Casado não leu o chat")


# TODO: comando solicitado pelo @Tairritadotio
@bot.command(name="dica")
async def fn_dica(ctx):
    await ctx.send_me(
        "Se der erro no seu código poder ser que algo esteja errado ou algo não esteja certo.",
    )


@bot.command(name="raid")
async def fn_raid(ctx):
    await ctx.send_me(
        """Kappa PogChamp PogChamp Kappa PogChamp  Kappa PogChamp
        PogChamp Kappa PogChamp Kappa PogChamp PogChamp Kappa PogChamp""",
    )


# comando para dicas de filmes
@bot.command(name="filme")
async def fn_filme(ctx):
    filme_indicado = "Qualquer um do Nicolas Cage"
    print(f"Filme indicado: {filme_indicado}")
    await ctx.send_me(f"Nosso bot te indica o filme: {filme_indicado}")


# TODO: biscoito / robson - por @ChicoCodes
@bot.command(name="robson")
async def fn_robson(ctx):
    await ctx.send_me(
        f"@{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN. Chico disse, ta DITOOO!",
    )


# TODO: biscoito / robson - por @ChicoCodes
@bot.command(name="biscoito")
async def fn_biscoito(ctx):
    await ctx.send_me(
        f"@{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN. Chico disse, ta DITOOO!",
    )


# TODO: traduzir texto por - PO: @ChicoCodes, com grande ajuda do MechanicallyDev
@bot.command(name="traduzir")
async def fn_traduzir(ctx):
    "Traduz o texto para inglês"
    texto_solicitado = "+".join(ctx.content.split(" ")[1:])

    session = HTMLSession()
    url = "https://www.google.com/search?q=translate+to+english+"

    url_unificado = f"{url}{texto_solicitado}"

    req_selecionada = session.get(url_unificado)
    texto_traduzido = req_selecionada.html.find("#tw-target-text")[0].text
    print(f"Tradução: {texto_traduzido}")

    await ctx.send_me(f"translate: {texto_traduzido}")


# TODO: traduzir texto por - PO: @ChicoCodes, com grande ajuda do MechanicallyDev
@bot.command(name="translate")
async def fn_translate(ctx):
    "Traduz o texto para portugues"
    texto_solicitado = "+".join(ctx.content.split(" ")[1:])

    session = HTMLSession()
    url = "https://www.google.com/search?q=translate+to+portuguese+"

    url_unificado = f"{url}{texto_solicitado}"

    req_selecionada = session.get(url_unificado)
    texto_traduzido = req_selecionada.html.find("#tw-target-text")[0].text
    print(f"Tradução: {texto_traduzido}")

    await ctx.send_me(f"translate: {texto_traduzido}")


# TODO: mostrar horóscopo
@bot.command(name="horoscopo")
async def fn_horoscopo(ctx):
    "Mostra o signo solicitado, com base no site Capricho"

    session = HTMLSession()
    url_signos = "https://capricho.abril.com.br/horoscopo/signo-"
    signo_solicitado = ctx.content.split(" ")[1]

    req_selecionada = session.get(f"{url_signos}{signo_solicitado}/")
    signo_selecionado = req_selecionada.html.find(".previsao_dia")[0].text

    await ctx.send_me(f"{signo_solicitado}: {signo_selecionado}")


# TODO: Tratar localization
# comando de previsão do tempo - pedido do @MechanicallyDev
@bot.command(name="clima")
async def fn_climaTempo(ctx):
    # Mostrar a previsão do tempo da região
    session = HTMLSession()

    cidade_solicitada = "+".join(ctx.content.split(" ")[1:])

    req_selecionada = session.get(
        f"https://www.google.com.br/search?q=tempo+{cidade_solicitada}",
    )

    cidade_selecionada = req_selecionada.html.find("#wob_loc")[0].text
    temperatura_atual = req_selecionada.html.find("#wob_tm")[0].text
    horario_atual = req_selecionada.html.find("#wob_dts")[0].text
    tipo_clima = req_selecionada.html.find("#wob_dc")[0].text

    # as unidades são especificadas em spans, precisamos inspecionar qual está
    # visível
    spans_unidade = req_selecionada.html.find(".wob-unit > span.wob_t")
    unidade = "ºC"
    for span_unidade in spans_unidade:
        if span_unidade.attrs["style"] == "display:inline":
            unidade = span_unidade.text

    print(f"Clima agora em {cidade_selecionada}: {temperatura_atual}")

    await ctx.send(
        f"/me Agora na cidade {cidade_selecionada}, é {horario_atual} "
        f"e está {temperatura_atual}{unidade}, com um clima {tipo_clima}",
    )
    # await ctx.send('Está frio pra caramba em Itajaí! - teste em produção com sucesso')


# TODO: filtrar palavras para blacklist e frases já liberadas pelo id
# foi um ótimo resgate realizado pelo @MechanicallyDev
@bot.command(name="piada")
async def fn_piadas(ctx):
    # https://api-de-charadas.fredes.now.sh/

    # piada_selecionada = requests.get(
    #     'https://us-central1-kivson.cloudfunctions.net/charada-aleatoria',
    #     headers={
    #         'Accept': 'application/json',
    #         'Content-type': 'application/json'
    #     }).json()

    piada_selecionada = requests.get(
        "https://api-de-charadas.fredes.now.sh",
    ).json()

    print(f"pergunta: {piada_selecionada['question']}")
    print(f"resposta: {piada_selecionada['answer']}")

    pergunta = piada_selecionada["question"]
    resposta = piada_selecionada["answer"]

    await ctx.send_me(f"Pergunta: {pergunta}")

    time.sleep(15)
    await ctx.send_me(f"Resposta: {resposta}")


@bot.command(name="motivar")
async def fn_motivacao(ctx):
    "Mensagem motivacional para o chat"
    session = HTMLSession()
    req_selecionada = session.get("https://motivaai.nandomoreira.dev/")

    motivacao_selecionada = req_selecionada.html.find("blockquote")[
        0
    ].text.split("\n")

    frase = motivacao_selecionada[0]
    autor = motivacao_selecionada[1]

    print(f"Frase de {autor}: {frase}")

    await ctx.send_me(f'"{frase}", por {autor}')


@bot.command(name="addengajar")
async def fn_add_mensagem_engajamento(ctx):
    if len(ctx.content) > 30:
        # gravar a mensagem de ban comprada pelo usuário
        arquivo_texto_engajamento = open(
            "files/texto_engajamento.txt",
            "a+",
            encoding="utf-8",
        )

        arquivo_texto_engajamento.write(f"{ctx.content.lower()[12:]} \n")
        # TODO: CRIAR MÉTODO PARA ADICIONAR EM VOTAÇÃO NO CHAT
        arquivo_texto_engajamento.close()

        print(f"texto de engajamento adicionado por @{ctx.author.name}")
        await ctx.send_me("Mensagem de engajamento adicionada. aguardando aprovação.")

    if len(ctx.content) < 30:
        await ctx.send_me("Mensagem precisa ter pelo menos 30 caracteres.")


# foi uma ótima idéia do @Falvern_
@bot.command(name="unban")
async def fn_unBan(ctx):
    # TODO: implementar o método anti-ban durante a Hacktoberfest
    frase = "invoca carta imbanivel e não pode ser banido!"
    await ctx.send_me(f"@{ctx.author.name} {frase}")


@bot.command(name="ban")
async def fn_ban(ctx):
    if len(ctx.content.split(" ")[1]) < 4:
        await ctx.send_me("para banir alguém, é preciso incluir o nome o usuário")

    if len(ctx.content.split(" ")[1]) > 3:
        lista_ban = open("files/texto_bans.txt", encoding="utf-8")

        _, _, alvo = ctx.content.lower().partition(" ")
        tipo_ban = random.choice(list(lista_ban))

        print(
            f"comando de banir executado por @{ctx.author.name} para o @{alvo}",
        )

        await ctx.send_me(f"{alvo} {tipo_ban}")


@bot.command(name="humildao")
async def fn_humildao(ctx):
    if len(ctx.content.split(" ")[1]) < 4:
        await ctx.send_me("Me diga quem é o Humildão, marca ele ai ResidentSleeper ")

    if len(ctx.content.split(" ")[1]) > 3:
        _, _, alvo = ctx.content.lower().partition(" ")
        await ctx.send_me(f"{alvo} FOI HUMILDÃOOOOO PogChamp PogChamp PogChamp ")


@bot.command(name="addban")
async def fn_addban(ctx):
    if len(ctx.content) > 30:
        # gravar a mensagem de ban comprada pelo usuário

        arquivo_texto_bans = open(
            "files/texto_moderacao_bans.txt",
            "a+",
            encoding="utf-8",
        )

        arquivo_texto_bans.write(f"{ctx.content.lower()[8:]} \n")
        # TODO: CRIAR MÉTODO PARA ADICIONAR EM VOTAÇÃO NO CHAT
        arquivo_texto_bans.close()

        print(f"texto de ban adicionado por @{ctx.author.name}")
        await ctx.send_me("Mensagem de ban adicionada. aguardando aprovação.")


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
    "Roda toda vez que uma mensagem no chat é enviada."

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == nick_bot.lower():
        return

    # TODO: quantas letras a pessoa escreveu no chat
    pessoas_online.append(ctx.author.name)

    await bot.handle_commands(ctx)

    if "bom dia" in ctx.content.lower():
        await ctx.channel.send_me(f"Bom dia, @{ctx.author.name}! Como você está?")

    if "boa tarde" in ctx.content.lower():
        await ctx.channel.send_me(f"Boa tarde, @{ctx.author.name}! Como você está?")

    if "boa noite" in ctx.content.lower():
        await ctx.channel.send_me(f"Boa noite, @{ctx.author.name}! Como você está?")

    if "boa madrugada" in ctx.content.lower():
        await ctx.channel.send_me(
            f"Boa madrugada aeew, @{ctx.author.name}! Como você está?",
        )

    # culpa do @Super_Feliz - o tecladod ele o trolou
    if "boa note" in ctx.content.lower():
        await ctx.channel.send_me(
            f"Boa noite, @{ctx.author.name}! Como você está? Seu teclado te trolou...",
        )

    if "salve" in ctx.content.lower():
        await ctx.channel.send(f"Ta salvado, @{ctx.author.name}! Como você está?")

    if "ctrl + s" in ctx.content.lower():
        await ctx.channel.send_me(f"Ta salvado, @{ctx.author.name}! Como você está?")

    if "aoba" in ctx.content.lower():
        await ctx.channel.send_me(f"Aoooba, @{ctx.author.name}! Como você está?")

    if "lurk" in ctx.content.lower():
        await ctx.channel.send_me(
            f"Opa @{ctx.author.name}! Tamo junto ae no lurk. Já ajuda pakas.",
        )

    if "bolacha" in ctx.content.lower():
        await ctx.channel.send_me(
            f"@{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN. Chico disse, ta DITOOO!",
        )

    if "biscoito" in ctx.content.lower():
        await ctx.channel.send_me(
            f"@{ctx.author.name} Errado o correto é bolacha, BO-LA-CHA, patoGordin disse ",
        )

    if "sextou" in ctx.content.lower():
        await ctx.channel.send_me("SEXTOUUUUUUU DIA DE FAZER PUSH NA MASTER!!!")


if __name__ == "__main__":
    bot.run()
