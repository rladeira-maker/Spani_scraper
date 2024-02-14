from os import system as s
import PySimpleGUI as sg
from scraper_Spani_v1 import main


sg.theme('LightGreen')   # Add a touch of color

pages = [   'biscoitos-e-chocolates',
            'bazar-e-utilidades',
            'bebidas',
            'carnes',
            'cereais-e-farinaceos',
            'frios-e-laticinios',
            'higiene-e-limpeza',
            'hortifruti',
            'limpeza',
            'matinais-e-sobremesas',
            'mercearia',
            'padaria',
            'perfumaria-e-higiene',
            'animais',
         ]
checks = [
    ["Biscoitos e Chocolates", "Bazar", "Bebidas", "Carnes"],

    ["Cereais e Farináceos","Frios e Laticinios", "Higiene e Limpeza", "Hortifruti"],

    ["Limpeza", "Matinais e Sobremesas", "Mercearia"],
    
    ["Padaria", 'Perfumaria e Higiene', "Pet Shop"],
]
column = [
    [[sg.Text('Selecione as seções\ndo mercado que\ndeseja pesquisar:',
            font=('Ubuntu', 11, 'bold'))]]] + [
    [[sg.Checkbox(text, pad=(5, 0), default=True, key=('-'+text+'-')
            )]
    for i, text in enumerate(check)] for j, check in enumerate(checks)
            ]

layout = [[     sg.Column(column[i]) for i in range(5)],
         [[     sg.Checkbox('Mais vendidos', pad=((172,0),(20,20)),
                font=('Ubuntu', 11, 'bold'), key='-+Vendidos-'),
                sg.Checkbox('Ofertas', font=('Ubuntu', 11, 'bold'),
                key='-Ofertas-'), sg.Checkbox('Apaga arquivos anteriores',
                font=('Ubuntu', 11, 'bold'), key='-Apaga-')
            ]],
         [[     sg.Button('Limpa Seleção', pad=((250,0),(0,0))),
                sg.Button('Inicia'),
                sg.Button('Sair'),
            ]]
            ]

window=sg.Window('Preços Spani', layout, font=('Ubuntu\ Condensed',11))

while True:
    event, values = window.read()
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    if event == 'Limpa Seleção':
        for value in values:
            window[value]. Update(value=False)
    if event == 'Inicia':
        for idx, value in enumerate(values):
            if idx == 14: #o último elemento é -Apaga-/não está na lista
                break
            if values.get(value) is False:
                pages[idx] = ''

        pages = [j for i, j in enumerate(pages) if j != '']
        DELETE_FILE = values['-Apaga-'] is True
        if values['-Ofertas-'] is True:
            for item in range(len(pages)):
                pages[item] = 'https://www.spanionline.com.br/produtos/'+'ofertas/departamento/'+pages[item]
        elif values['-+Vendidos-'] is True:
            for item in range(len(pages)):
                pages[item] = 'https://www.spanionline.com.br/produtos/'+'mais-vendidos/'+pages[item]
            # if values.get('-Swift-') is True:
                # pages.append('https://www.spanionline.com.br/produtos/mais-vendidos/loja-swift')
        else:
            print('Você precisa escolher "Oferta" ou "Mais Vendidos"')
            quit()
            
        s('clear')

        if not pages:
            quit()
        main(pages, DELETE_FILE)
        quit()
#
# 
