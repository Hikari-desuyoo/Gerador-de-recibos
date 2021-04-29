'''sets up tkinter GUI widgets using easytk script'''
from gui.easytk import EasyTk

class GUI_recibo:
    def __init__(self):
        pass
    def start_gui(self,commands):
        gui=EasyTk("Gerador de Recibos")
        gui.root.iconbitmap('data/icon.ico')

        title_to_key={
            'Locador':"locador",
            'CPF':"cpf",
            'Endereço':"local",
            'Locatário':"locatario",
            'Ínicio do primeiro recibo':"inicio",
            'Vencimento do primeiro recibo':"vencimento",
            'O primeiro recibo':"primeiro_numero",
            'Serão gerados':"numero",
            'Registro da água':"agua",
            'Cidade                                ':"cidade",
            'Custo do aluguel               ':"valor",
            'Capa':"capa",
            'Escolher cor':"cor"
        }
        data_dict={}

        #set the GUI widgets and return [title,object]
        locador=gui.entry_macro("Locador",(0,0))
        cpf=gui.entry_macro("CPF",(2,0))

        gui.line_break(2)

        local=gui.listbox_macro("Endereço",(0,3))
        locatario=gui.listbox_macro("Locatário",(2,3))
        gui.color_macro("Escolher cor",(2,3),sticky="E")

        gui.line_break(7)
        gui.label_macro("Datas:",(0,8),
                    sticky="SW")

        inicio=gui.date_macro("Ínicio do primeiro recibo",(0,9))
        vencimento=gui.date_macro("Vencimento do primeiro recibo",(0,11))

        gui.label_macro("será o Nº"+" "*7,(0,9),sticky="SE")
        recibo_first=gui.entry_macro("O primeiro recibo",(0,8),
                                 sticky="SE",width=3)


        numero=gui.entry_macro("Serão gerados",(0,11),
                           sticky="SE", width=12)
        gui.label_macro(" recibos",(0,12),
                    sticky="SE")

        agua=gui.entry_macro("Registro da água", (2,8),
                         sticky="WN", width=22)
        cidade=gui.entry_macro("Cidade"+" "*32, (2,8),
                           sticky="EN",width=22)
        valor=gui.entry_macro("Custo do aluguel"+" "*15,(2,10),
                          sticky="EN",width=22)

        capa= gui.check_macro("Capa",(2,11),sticky="WN")

        #buttons for manipulating gathered data
        def criar_recibos(entry_object,coords,sticky=""):
            try:
                commands[0](
                    {title_to_key[x[0]]:gui.auto_get(x)\
                            for x in gui.new_data})
                msg="Recibo criado com sucesso!"+" "*40
                color="green"
            except:
                msg="Ocorreu um erro. Verifique os dados colocados."
                color="red"
            gui.label_macro(msg, coords,
            sticky=sticky,
            fg=color)
            


        button=gui.button_macro("Criar recibos",(2,12),
                         lambda: criar_recibos(button,(2,13),sticky="SW"),#data goes here
                     sticky="W",fg="#000000",bg="#b0ceff")

        
        gui.button_macro("Tirar cores",(2,12),commands[1],
                     fg="#000000",bg="#b0ceff")
        gui.button_macro("Visualizar recibos",(2,12),commands[2],
                     sticky="E",fg="#000000",bg="#b0ceff")



        gui.line_break(13)

        gui.start()











