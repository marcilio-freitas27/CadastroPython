# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
import time
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import sys, os

Builder.load_string('''
<Cadastrar>:
    BoxLayout:
        canvas:
            Color:
                rgb: (0,0,1)
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        Image:
            source: 'logo_ciu.png'
            size_hint_y:None
            height:200
            allow_stretch:True
        Label:
            text: "[b]Cadastro de usuários[b]"
            markup: True
        GridLayout:
            cols: 2
            rows: 3
            Label:
                id : usernm
                text: "[b]Username:[b]"
                markup: True
            TextInput:
                id: user
                multiline: False
            Label:
                id : passwd
                text: "[b]Password:[b]"
                markup: True
            TextInput:
                id: passes
                multiline: False
                password: True

            Button:
                text: "cadastrar usuário e senha"
                background_color: [0,1,1,1]
                on_release: root.cadastro(self)
            Button:
                text: "login"
                background_color: [0,1,1,1]
                on_release: root.manager.current = "login"
        AnchorLayout:
            Label:
                id: tela
                text: "Bem vindos!"
        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'bottom'
            Button:
                background_color: [0,1,1,1]
                text: "exit"
                on_release: root.sair(self)
                size_hint_y: 0.4
                size_hint_x: 0.1

<Login>:
    BoxLayout:
        canvas:
            Color:
                rgb: (1,0,0)
            Rectangle:
                pos: self.pos
                size: self.size

        orientation: 'vertical'
        Image:
            source: 'logo_ciu.png'
            size_hint_y:None
            height:200
            allow_stretch:True
        Label:
            text: "[b]Login[b]"
            markup: True
        GridLayout:
            size_hint_y: 1.3
            size_hint_x: 1
            cols: 2
            rows: 3
            Label:
                id : usernm
                text: "[b]Username:[b]"
                markup: True
            TextInput:
                id: user
                multiline: False
            Label:
                id : passwd
                text: "[b]Password:[b]"
                markup: True
            TextInput:
                id: passes
                multiline: False
                password: True
            Button:
                text: "login"
                background_color: [1,0,0,1]
                on_release: root.login(self)
            Button:
                text: "cadastro"
                background_color: [1,0,0,1]
                on_release: root.manager.current = "cadastrar"

        AnchorLayout:
            padding: 100
            Label:
                id: tela
                size_hint_y: 0.2
                size_hint_x: 0.2
        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'bottom'
            Button:
                background_color: [1,0,0,1]
                text: "exit"
                on_release: root.sair(self)
                size_hint_y: 0.5
                size_hint_x: 0.1


<Conta>:
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas:
            Color:
                rgb: (0,0.5,0)
            Rectangle:
                pos: self.pos
                size: self.size
        GridLayout:
            orientation: 'vertical'
            rows: 4
            cols: 6
            Label:
                text: 'Nome'
            Label:
                id : label
                text: ""
            Label:
                text: 'Idade'
            Label:
                id: label0
            Label:
                text: 'RG'
            Label:
                id: label1
            Label:
                text: 'CPF'
            Label:
                id: label2
            Label:
                text: 'Endereço'
            Label:
                id: label3
            Label:
                text: 'Bairro'
            Label:
                id: label4
            Label:
                text: 'Nº'
            Label:
                id: label5
            Label:
                text: 'Estado'
            Label:
                id: label6
            Label:
                text: 'Cidade'
            Label:
                id: label7

        AnchorLayout:
            anchor_x: 'center'
            anchor_y: 'center'
            Button:
                background_color: [0,1,0,1]
                text: "sair"
                size_hint_y: 0.2
                size_hint_x: 0.2
                on_release: root.manager.current = "login"
                on_press:
        GridLayout:
            id: lista
            orientation: 'vertical'
            rows: 8
            cols: 12
            Label:
                text: 'Nome'
            TextInput:
                id : text0
                multiline: False
                size_hint_y: 0.2
                size_hint_x: 0.2
            Button:
                text: "add"
                background_color: [0,1,0,1]
                on_release: root.add(self)
            Label:
                text: 'Idade'
            TextInput:
                id : text1
                multiline: False
            Button:
                text: "add"
                background_color: [0,1,0,1]
                on_release: root.add0(self)
            Label:
                text: 'RG'
            TextInput:
                id : text2
                multiline: False
            Button:
                text: "add"
                background_color: [0,1,0,1]
                on_release: root.add1(self)
            Label:
                text: 'CPF'
            TextInput:
                id : text3
                multiline: False
            Button:
                text: "add"
                background_color: [0,1,0,1]
                on_release: root.add2(self)
            Label:
                text: 'Endereço'
            TextInput:
                id : text4
                multiline: False
            Button:
                text: "add"
                background_color: [0,1,0,1]
                on_release: root.add3(self)
            Label:
                text: 'Bairro'
            TextInput:
                id : text5
                multiline: False
            Button:
                text: "add"
                background_color: [0,1,0,1]
                on_release: root.add4(self)
            Label:
                text: 'Nº'
            TextInput:
                id : text6
                multiline: False
            Button:
                text: "add"
                background_color: [0,1,0,1]
                on_release: root.add5(self)
            Label:
                text: 'Estado'
            TextInput:
                id : text7
                multiline: False
            Button:
                text: "add"
                background_color: [0,1,0,1]
                on_release: root.add6(self)
<NovaConta>:
    BoxLayout:
        orientation:'vertical'
        padding: 10
        spacing: 10
        canvas:
            Color:
                rgb: (1,1,0)
            Rectangle:
                pos: self.pos
                size: self.size
        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'bottom'
            Button:
                background_color: [1,1,0,1]
                text: "exit"
                on_release: app._exit()
                size_hint_y: 0.4
                size_hint_x: 0.1

        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'top'
            Button:
                background_color: [0,1,0,1]
                text: "sair"
                size_hint_y: 0.2
                size_hint_x: 0.2
                on_release: root.manager.current = "login"
''')

usuarios = []
senhas = []
loguser = []
logpass = []
#test
alfabeto = ['a','b','c','ç','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
algarismos = [0,1,2,3,4,5,6,7,8,9]
caracteres = ['.',',',';',':','!','?','@','#','$','*']

class Cadastrar(Screen):
    def cadastro(self, obj):
        popup = Popup(title='Info',content=Label(text='Cadastro feito.'),size_hint=(0.3,0.3), title_color=(0,1,1,1))
        if self.ids.user.text in usuarios:
            self.ids.tela.text = "Usuário já cadastrado."
        elif len(self.ids.passes.text) == 0:
            self.ids.tela.text = "Digite uma senha"
        #test
        #elif self.ids.passes.text in senhas:
            #for i in list(senhas[0]):
                #if i not in alfabeto and algarismos and caracteres:
                    #print("senha fraca. Digite uma dentro dos padrões.")
					
        else:
            usuarios.append(self.ids.user.text)
            senhas.append(self.ids.passes.text)
            print(usuarios)
            print(list(senhas[0]))
            popup.open()
            self.manager.current = "login"
			
    def sair(self, obj):
        os._exit(0)
	

class Login(Screen):
    def login(self, obj):
        popup = Popup(title='Info',content=Label(text="Bem vindo {}".format(self.ids.user.text)),size_hint=(0.3,0.3), title_color=(1,0,0,1))
        if self.ids.user.text in usuarios and self.ids.passes.text in senhas:
            self.ids.tela.text = "Bem vindo {}".format(self.ids.user.text)
            loguser.append(self.ids.user.text)
            logpass.append(self.ids.passes.text)
            print(len(loguser))
            popup.open()
            self.manager.current = "conta"
            #self.manager.current = "nova"

        elif self.ids.user.text not in usuarios:
            self.ids.tela.text = "Usuário não cadastrado."
        else:
            self.ids.tela.text = "Senha incorreta"
			
    def sair(self, obj):
        os._exit(0)
			
class Conta(Screen):
    if len(loguser) != 0:
        self.ids.label.text = loguser[0]
    def add(self, obj):
        if len(self.ids.text0.text) != 0:
            #self.remove_widget(self.ids.text1)
            self.ids.label.text = self.ids.text0.text
    def add0(self, obj):
        if len(self.ids.text1.text) != 0:
            #self.remove_widget(self.ids.text1)
            self.ids.label0.text = self.ids.text1.text
    def add1(self, obj):
        if len(self.ids.text2.text) != 0:
            #self.remove_widget(self.ids.text1)
            self.ids.label1.text = self.ids.text2.text
    def add2(self, obj):
        if len(self.ids.text3.text) != 0:
            #self.remove_widget(self.ids.text1)
            self.ids.label2.text = self.ids.text3.text
    def add3(self, obj):
        if len(self.ids.text4.text) != 0:
            #self.remove_widget(self.ids.text1)
            self.ids.label3.text = self.ids.text4.text
    def add4(self, obj):
        if len(self.ids.text5.text) != 0:
            #self.remove_widget(self.ids.text1)
            self.ids.label4.text = self.ids.text5.text
    def add5(self, obj):
        if len(self.ids.text6.text) != 0:
            #self.remove_widget(self.ids.text1)
            self.ids.label5.text = self.ids.text6.text
    def add6(self, obj):
        if len(self.ids.text7.text) != 0:
            #self.remove_widget(self.ids.text1)
            self.ids.label6.text = self.ids.text7.text
    def sair(self, obj):
        loguser.remove(self.ids.user.text)
        logpass.remove(self.ids.passes.text)
        print(loguser)

class NovaConta(Screen):
    def redraw(self, obj):
        self.add_widget(Label(text="nova conta"))
	
    def sair(self, obj):
        os._exit(0)

sm = ScreenManager()
sm.add_widget(Cadastrar(name="cadastrar"))
sm.add_widget(Login(name="login"))
sm.add_widget(Conta(name="conta"))
sm.add_widget(NovaConta(name="nova"))

class Iniciar(App):
    def build(self):
        return sm

if __name__ == '__main__':
    Iniciar().run()
