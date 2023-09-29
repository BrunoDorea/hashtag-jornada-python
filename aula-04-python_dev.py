import flet as ft


def main(pagina):

    texto = ft.Text('Bate papo #Hashtag')
    chat = ft.Column()
    nome_user = ft.TextField(label='Digite seu nome')


    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem['tipo']
        if tipo == 'mensagem':
            usuario_mensagem = mensagem['usuario']
            texto_mensagem = mensagem['texto']
            chat.controls.append(ft.Text(f'{usuario_mensagem}: {texto_mensagem}'))
        else:
            usuario_mensagem = mensagem['usuario']
            chat.controls.append(ft.Text(f'{usuario_mensagem} entrou no chat', size = 12, italic = True, color = ft.colors.GREEN_500))
            
        pagina.update()


    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(e):
        pagina.pubsub.send_all({ 'texto': campo_mensagem.value, 'usuario': nome_user.value, 'tipo': 'mensagem' })
        campo_mensagem.value = ''
        pagina.update()


    campo_mensagem = ft.TextField(label='Digite uma mensagem', on_submit = enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click = enviar_mensagem)


    def entrar_popup(e):
        pagina.pubsub.send_all({ 'usuario': nome_user.value, 'tipo': 'entrada' })
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()


    popup = ft.AlertDialog(
        open = False,
        modal = True,
        title = ft.Text('Bem vindo ao chatbot'),
        content = nome_user,
        actions = [ ft.ElevatedButton('Entrar', on_click = entrar_popup) ],
    )


    def entrar_chat(e):
            pagina.dialog = popup
            popup.open = True
            pagina.update()


    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click = entrar_chat)


    pagina.add(texto)
    pagina.add(botao_iniciar)


ft.app(
    target = main,
    view = ft.WEB_BROWSER,
    )