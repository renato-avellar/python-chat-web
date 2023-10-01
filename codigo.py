import flet as ft

def main(page):
    text = ft.Text('HASHZAP')
    chat = ft.Column()
    username = ft.TextField(label= "Digite seu nome")
    message = ft.TextField(label= "Digite uma mensagem")
    
    def tunnel_send_message(msg):
        if msg["type"] == 'message':
            user = msg["user"]
            text = msg["text"]
            chat.controls.append(ft.Text(f"{user}: "))
            chat.controls.append(ft.Text(text))
        else:
            user = msg["user"] 
            chat.controls.append(ft.Text(f"{user} entrou na sala. ", size = 12, italic=True, color = ft.colors.GREEN_400))   
        page.update()
    
    page.pubsub.subscribe(tunnel_send_message)
        
    def send_message(e):
        page.pubsub.send_all({"text":message.value, "user":username.value, "type": "message"})
        message.value = ""
        page.update()
        
    
    
        
    button_send_message = ft.ElevatedButton('Enviar mensagem', on_click=send_message)
    
    def enter_chat(e):
        page.pubsub.send_all({"user": username.value, 'type': ''})
        page.update()
        popup.open = False
        page.remove(start_button)
        page.add(chat)
        page.add(ft.Row([message, button_send_message]))
        page.remove(text)
        page.update()
        
    popup = ft.AlertDialog(
        open = False,
        modal= True,
        title = ft.Text('Bem vindo ao Hashzap'),
        content= username,
        actions= [ft.ElevatedButton('Entrar', on_click=enter_chat)],
    )
    
    def open_popup(e):
      page.dialog = popup
      popup.open = True
      page.update()
      
    start_button = ft.ElevatedButton('Iniciar chat', on_click=open_popup)
    
    page.add(text)
    page.add(start_button)

ft.app(target = main, view=ft.WEB_BROWSER)
#ft.app(target = main)