import asyncio
import configparser
import json
import random
import time
import traceback
from datetime import datetime

import pyttsx3
import requests
from requests_html import HTMLSession
from twitchio.ext import commands


# globais
counters = {},
# pessoas_online = {},
count_pessoa = [],

# Acessar o arquivo e recuperar os comandos anteriormente criados.
with open("files/commands.json", 'r', encoding='UTF-8') as file:
    namecommand = json.load(file)
    print('Comandos recuperados:', namecommand)


class Bot(commands.Bot):

    def __init__(self):

        config = configparser.ConfigParser()
        config.read("config.ini")

        nick_bot = config.get("bot", "username")
        inicia_canal = config.get("bot", "channel")

        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(
            token=config.get("bot", "oauth_token"),
            nick=nick_bot,
            prefix=config.get("bot", "command_prefix"),
            initial_channels=[inicia_canal]
        )


    async def event_ready(self):
        "Chama quando o bot casadodev está online."
        print(f'Logado como: {self.nick}')
        print(f"@{self.nick} está online! ")


    async def event_message(self, ctx):
        "Roda toda vez que uma mensagem no chat é enviada."

        # remove do log as mensagens do streamer
        # if ctx.author.name.lower() == self.nick.lower():
        #     return

        if ctx.echo:
            return

        userBot = [
            'streamelements'
        ]

        if not(ctx.author.name in userBot):
            print(f'{ctx.author.name}: {ctx.content}')

        # TODO: quantas letras a pessoa escreveu no chat
        # pessoas_online.append(ctx.author.name)


        if "bom dia" in ctx.content.lower():
            await ctx.channel.send(f"Bom dia, @{ctx.author.name}! Como você está?")

        elif "boa tarde" in ctx.content.lower():
            await ctx.channel.send(f"Boa tarde, @{ctx.author.name}! Como você está?")

        elif "boa noite" in ctx.content.lower():
            await ctx.channel.send(f"Boa noite, @{ctx.author.name}! Como você está?")

        elif "boa madrugada" in ctx.content.lower():
            await ctx.channel.send(
                f"Boa madrugada aeew, @{ctx.author.name}! Como você está?",
            )

        # culpa do @Super_Feliz - o teclado dele o trolou
        elif "boa note" in ctx.content.lower():
            await ctx.channel.send(
                f"Boa noite, @{ctx.author.name}! Como você está? Seu teclado te trolou...",
            )

        if "salve" in ctx.content.lower():
            await ctx.channel.send(f"Ta salvado, @{ctx.author.name}! Como você está?")

        if "ctrl + s" in ctx.content.lower():
            await ctx.channel.send(f"Ta salvado, @{ctx.author.name}! Como você está?")

        if "aoba" in ctx.content.lower():
            await ctx.channel.send(f"Aoooba, @{ctx.author.name}! Como você está?")

        if "lurk" in ctx.content.lower():
            await ctx.channel.send(
                f"Opa @{ctx.author.name}! Tamo junto ae no lurk. Já ajuda pakas.",
            )

        if "bolacha" in ctx.content.lower():
            await ctx.channel.send(
                f"@{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN. Chico disse, ta DITOOO!",
            )

        if "biscoito" in ctx.content.lower():
            await ctx.channel.send(
                f"@{ctx.author.name} Errado o correto é bolacha, BO-LA-CHA, patoGordin disse ",
            )

        if "sextou" in ctx.content.lower():
            await ctx.channel.send("SEXTOUUUUUUU DIA DE FAZER PUSH NA MASTER!!!")

        # Para rodar os comandos criados pelo !comando
        if "!" == ctx.content.split()[0][0]:
            comando = ctx.content.split()[0]

            for command, message in namecommand.items():
                if comando.replace("!", "") == command:
                    name = command
                    msg = message
                    print(f"Comando chamado:'{name}' -> '{msg}'")

                    await ctx.channel.send(msg)

        await bot.handle_commands(ctx)


    @commands.command(name="xxstartxx")
    async def fn_start(self, ctx: commands.Context):
        # Mostrando os comandos disponíveis no bot
        while True:
            msg_aleatoria = list(
                open("files/texto_engajamento.txt", encoding="utf-8"),
            )
            comandos = (
                '/me os comandos do bot são "exclamação + :" ban +usuário, '
                "clima +local, piada, traduzir +mensagem, translate +message, "
                "motivar, horoscopo +signo, susto, filme. "
                "Tudo desenvolvido nas lives e em python!"
            )

            # await ws.send_privmsg(inicia_canal, comandos)
            await ctx.send(f"oi => {comandos}")
            await asyncio.sleep(460.0)

            if len(msg_aleatoria) > 0:
                "Mostrando mensagens de engajamento no chat"
                msg_selecionada = random.choice(msg_aleatoria)

                # await ws.send_privmsg(inicia_canal, msg_selecionada)
                await ctx.send(f"{msg_selecionada}")
                await asyncio.sleep(240.0)


    @commands.command(name="hello")
    async def fn_hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')


    @commands.command(name="steam")
    async def fn_steam(ctx):
        link = "https://s.team/p/gdmd-fkhb/fmdrjvgt"
        await ctx.send(
            f'Jogue conosco usando o código "1115830096" ou usando o link {link}',
        )


    @commands.command(name="bot")
    async def fn_bot(self, ctx: commands.Context):
        link = "https://github.com/casadodev/bot-twitch-python"
        await ctx.send(
            f"Deseja ajudar na construção do bot!? acesse o link e torne-se um contribuidor {link}",
        )


    @commands.command(name="whatsapp")
    async def fn_whatsapp(self, ctx: commands.Context):
        await ctx.send(
            "Grupo no whatsapp https://chat.whatsapp.com/GjztcHTQiXb0MNZutOhCOY",
        )


    @commands.command(name="discord")
    async def fn_discord(self, ctx: commands.Context):
        await ctx.send("Grupo no discord https://mercadodeti.com.br/discord")


    @commands.command(name="instagram")
    async def fn_instagram(self, ctx: commands.Context):
        await ctx.send("Perfil no Inta https://instagram.com/casadodev")


    @commands.command(name="horadosorteio")
    async def fn_horasorteio(self, ctx: commands.Context):
        await ctx.send("HORA DO SORTEIO!!!!!!")
        await ctx.send("VENHA PARTICIPAR")
        await ctx.send("QUEM SERÁ O SORTUDO DA NOITE Kappa")


    @commands.command(name="sorteio")
    async def fn_sorteio(self, ctx: commands.Context):
        await ctx.send(
            "Sorteios de cursos da Udemy de até R$40. Subs/Inscritos tem 3x mais chances de ganhar. "
            "O sorteio está disponível apenas para quem segue o canal a mais de 2h, ou inscritos. "
            "Se inscreva gratuitamente com seu Amazon Prime!",
        )


    # TODO: pedido de músicas no canal - por @Super_Feliz
    @commands.command(name="musica")
    async def fn_adicionaMusica(self, ctx: commands.Context):
        await ctx.send("Está sendo desenvolvido comando para tocar as músicas no canal")


    # TODO: comando solicitado pelo Marlon_Henq
    # Cria um comando de correio elegante onde vc pode pedir para o bot mandar uma mensagem para alguém
    # frases para enviar https://www.pensador.com/frases_para_correio_elegante/


    def create_counter(*, name, prefix, singular="vez", plural="vezes"):
        @commands.command(name=name)
        async def _counter(self, ctx: commands.Context):
            date = datetime.now()
            with open("files/counters.json") as current_json:
                raw_json = json.load(current_json)
                amount = raw_json[name]["qtd"] = raw_json[name]["qtd"] + 1
                current_list_dates = raw_json[name]["dates"]
                current_list_dates.append(date.strftime("%d/%m/%Y %H:%M:%S"))

            suffix = plural if amount > 1 else singular
            await ctx.send(f"{prefix} {amount} {suffix}")

            with open("files/counters.json", "w") as file_write:
                json.dump(raw_json, file_write)


    create_counter(name="cachorro", prefix="O cachorro já latiu")
    create_counter(name="risada", prefix="A Mirele já riu")
    create_counter(name="taxado", prefix="O Casado já foi taxado")
    create_counter(name="breja", prefix="O Casado já bebeu")
    create_counter(name="chat", prefix="O Casado não leu o chat")
    create_counter(name="aviao", prefix="O avião já passou")

    # TODO: comando solicitado pelo @Tairritadotio

    @commands.command(name="dica")
    async def fn_dica(self, ctx: commands.Context):
        await ctx.send(
            "Se der erro no seu código poder ser que algo esteja errado ou algo não esteja certo.",
        )


    @commands.command(name="raid")
    async def fn_raid(self, ctx: commands.Context):
        await ctx.send(
            """Kappa PogChamp PogChamp Kappa PogChamp  Kappa PogChamp
            PogChamp Kappa PogChamp Kappa PogChamp PogChamp Kappa PogChamp""",
        )


    # comando para dicas de filmes
    @commands.command(name="filme")
    async def fn_filme(self, ctx: commands.Context):
        filme_indicado = "Qualquer um do Nicolas Cage"
        print(f"Filme indicado: {filme_indicado}")
        await ctx.send(f"Nosso bot te indica o filme: {filme_indicado}")


    # TODO: biscoito / robson - por @ChicoCodes
    @commands.command(name="robson")
    async def fn_robson(self, ctx: commands.Context):
        await ctx.send(
            f"@{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN. Chico disse, ta DITOOO!",
        )


    # TODO: biscoito / robson - por @ChicoCodes
    @commands.command(name="biscoito")
    async def fn_biscoito(self, ctx: commands.Context):
        await ctx.send(
            f"@{ctx.author.name} o correto é Biscoito! SE MANDAR BOLACHA É BAN. Chico disse, ta DITOOO!",
        )


    # TODO: traduzir texto por - PO: @ChicoCodes, com grande ajuda do MechanicallyDev
    @commands.command(name="traduzir")
    async def fn_traduzir(self, ctx: commands.Context, *, texto):
        "Traduz o texto para inglês"

        session = HTMLSession()
        url = "https://www.google.com/search?q=translate+to+english+"

        url_unificado = f"{url}{texto}"

        req_selecionada = session.get(url_unificado)
        texto_traduzido = req_selecionada.html.find("#tw-target-text")[0].text

        print(f"Traduzir: {texto}")
        print(f"Tradução: {str(texto_traduzido)}")

        await ctx.send(f"translate: 🫡 {texto_traduzido}")


    # TODO: traduzir texto por - PO: @ChicoCodes, com grande ajuda do MechanicallyDev
    @commands.command(name="translate")
    async def fn_translate(self, ctx: commands.Context, *, texto):
        "Traduz o texto para portugues"
        # texto_solicitado = "+".join(ctx.content.split(" ")[1:])

        session = HTMLSession()
        url = "https://www.google.com/search?q=translate+to+portuguese+"

        url_unificado = f"{url}{texto_solicitado}"

        req_selecionada = session.get(url_unificado)
        texto_traduzido = req_selecionada.html.find("#tw-target-text")[0].text
        print(f"Tradução: {texto}")
        print(f"Traduzir: {texto_traduzido}")

        await ctx.send(f"translate: 🫡 {texto_traduzido}")


    # TODO: mostrar horóscopo
    @commands.command(name="horoscopo")
    async def fn_horoscopo(self, ctx: commands.Context):
        "Mostra o signo solicitado, com base no site Capricho"

        session = HTMLSession()
        url_signos = "https://capricho.abril.com.br/horoscopo/signo-"
        signo_solicitado = ctx.content.split(" ")[1]

        req_selecionada = session.get(f"{url_signos}{signo_solicitado}/")
        signo_selecionado = req_selecionada.html.find(".previsao_dia")[0].text

        await ctx.send(f"{signo_solicitado}: {signo_selecionado}")


    # TODO: Tratar localization
    # comando de previsão do tempo - pedido do @MechanicallyDev
    @commands.command(name="clima")
    async def fn_climaTempo(self, ctx: commands.Context):
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
    @commands.command(name="piada")
    async def fn_piadas(self, ctx: commands.Context):
        # if not (ctx.author.is_subscriber | ctx.author.is_mod):
        #    return await ctx.send_me("Comando liberado para subs e os melhores mods! Peça piada com os pontos do canal.")

        # https://api-de-charadas.fredes.now.sh/

        # piada_selecionada = requests.get(
        #     'https://us-central1-kivson.cloudfunctions.net/charada-aleatoria',
        #     headers={
        #         'Accept': 'application/json',
        #         'Content-type': 'application/json'
        #     }).json()

        dados_selecionada = requests.get(
            "https://api-de-charadas.fredes.now.sh",
        )

        if('A server error has occurred' in dados_selecionada.text):
            return await ctx.send("O servidor de piadas de pal. Que piada né, foi mal!")
        else:
            piada_selecionada = dados_selecionada.json()

        if 'loira' in piada_selecionada['question']:
            print('veio piada de loira, refazer!')
            print(piada_selecionada)
            return await ctx.send("Deu azar, veio piada de loira")

        print(f"pergunta: {piada_selecionada['question']}")
        print(f"resposta: {piada_selecionada['answer']}")

        pergunta = piada_selecionada["question"]
        resposta = piada_selecionada["answer"]

        await ctx.send(f"Pergunta: {pergunta}")

        time.sleep(15)
        await ctx.send(f"Resposta: {resposta}")


    @commands.command(name="motivar")
    async def fn_motivacao(self, ctx: commands.Context):
        "Mensagem motivacional para o chat"
        session = HTMLSession()
        req_selecionada = session.get("https://motivaai.nandomoreira.dev/")

        motivacao_selecionada = req_selecionada.html.find("blockquote")[0].text.split("\n")

        frase = motivacao_selecionada[0]
        autor = motivacao_selecionada[1]

        print(f"Frase de {autor}: {frase}")

        await ctx.send(f'"{frase}", por {autor}')


    @commands.command(name="addengajar")
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
            await ctx.send("Mensagem de engajamento adicionada. aguardando aprovação.")

        if len(ctx.content) < 30:
            await ctx.send("Mensagem precisa ter pelo menos 30 caracteres.")


    # # foi uma ótima idéia do @Falvern_
    @commands.command(name="unban")
    async def fn_unBan(self, ctx: commands.Context):
        # TODO: implementar o método anti-ban durante a Hacktoberfest
        frase = "invoca carta imbanivel e não pode ser banido!"
        await ctx.send(f"@{ctx.author.name} {frase}")


    @commands.command(name="ban")
    async def fn_ban(self, ctx: commands.Context):
        if len(ctx.content.split(" ")[1]) < 4:
            await ctx.send("para banir alguém, é preciso incluir o nome o usuário")

        if len(ctx.content.split(" ")[1]) > 3:
            lista_ban = open("files/texto_bans.txt", encoding="utf-8")

            _, _, alvo = ctx.content.lower().partition(" ")
            tipo_ban = random.choice(list(lista_ban))

            print(
                f"comando de banir executado por @{ctx.author.name} para o @{alvo}",
            )

            await ctx.send(f"{alvo} {tipo_ban}")


    @commands.command(name="humildao")
    async def fn_humildao(self, ctx: commands.Context):
        if len(ctx.content.split(" ")[1]) < 4:
            await ctx.send("Me diga quem é o Humildão, marca ele ai ResidentSleeper ")

        if len(ctx.content.split(" ")[1]) > 3:
            _, _, alvo = ctx.content.lower().partition(" ")
            await ctx.send(f"{alvo} FOI HUMILDÃOOOOO PogChamp PogChamp PogChamp ")


    @commands.command(name="addban")
    async def fn_addban(self, ctx: commands.Context):
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
            await ctx.send("Mensagem de ban adicionada. aguardando aprovação.")


    # Correio elegante com voz no chat, ativado manualmente por moderador
    @commands.command(name="correioelegante")
    async def fn_correioElegante(self, ctx: commands.Context):
        if not (ctx.author.is_subscriber | ctx.author.is_mod):
            return await ctx.send("Comando liberado para subs! Agradeça usando os pontos do canal.")

        mensagem = ctx.content.lower()[17:]
        print(f"@{ctx.author.name}: {mensagem}")

        moderando = input("Aceita o correio elegante? ")

        if moderando == "s":
            print("Correio elegante aceito...")
            engine = pyttsx3.init()
            engine.say(mensagem)
            engine.runAndWait()
            return await ctx.send("Só love SingsNote SingsNote SingsNote <3")
        else:
            print("correio elegante não aceito")
            return await ctx.send(f"@{ctx.author.name} seu correio elegante não foi aprovado. :(")


    # Correio elegante com voz no chat, ativado manualmente por moderador
    @commands.command(name="agradecimento")
    async def fn_agradecimento(self, ctx: commands.Context):
        if not (ctx.author.is_subscriber | ctx.author.is_mod):
            return await ctx.send("Comando liberado para subs! Agradeça usando os pontos do canal.")

        mensagem = ctx.content.lower()[15:]
        print(f"@{ctx.author.name}: {mensagem}")

        moderando = input("Aceita o agradecimento? ")

        if moderando == "s":
            print("Agradecimento aceito...")
            engine = pyttsx3.init()
            engine.say(mensagem)
            engine.runAndWait()
            return await ctx.send("Agradecido HeyGuys")
        else:
            print("agradecimento não aceito")
            return await ctx.send(f"@{ctx.author.name} seu agradecimento não foi aceito. :(")


    # Para poder adicionar/editar/deletar comandos pelo chat (apenas gerados pelo !comando)
    @commands.command(name='comando')
    async def add_commando(self, ctx: commands.Context):
        if not ctx.author.is_mod:
            return

        global namecommand

        def save_file(save=dict):  # Salvar no arquivo as alterações
            with open("files/commands.json", 'w+', encoding='utf-8') as file:
                comandos = json.dumps(save, indent=True, ensure_ascii=False)
                file.write(comandos)
                print("comando salvo")

        comando = ctx.content.split()[2]
        msg = " ".join(ctx.content.split()[3:])
        if ctx.content.split()[1] == 'add':  # Adicionar o comando novo
            namecommand[comando] = msg
            print(f"Comando {comando} adicionado por {ctx.author.name}. Lista de comando adicionados {namecommand}")
            save_file(namecommand)
            mensagem = f"Comando '{comando}' com a mensagem '{msg}' foi adicionada com sucesso."

        elif ctx.content.split()[1] == 'edit':  # Editar um comando
            for command, message in namecommand.items():
                if command == comando:
                    namecommand[command] = msg
                    print(f"A mensagem do comando '{comando}' foi alterado para '{message}'")
                    save_file(namecommand)
                    mensagem = f"A mensagem do comando '{comando}' foi alterado para '{msg}' com sucesso."

        elif ctx.content.split()[1] == 'del':  # Deletar um comando
            namecommand.pop(comando)
            save_file(namecommand)
            mensagem = f"O comando '{comando}' foi deletado com sucesso."

        await ctx.channel.send(mensagem)


bot = Bot()
bot.run()
