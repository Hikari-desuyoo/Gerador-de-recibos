'''
recibo() makes all the final image and saves them
'''
import os
from image_editor.insert_text import *
from image_editor.date_manager import *
from PIL import Image

class Recibo():
    def __init__(self):
        pass
    
    def recibo(self, data_dict):
        '''
        data_dict keys:
        primeiro_numero
        locador
        cpf
        locatario
        local
        valor
        agua
        inicio
        vencimento
        numero
        cor
        cidade
        '''
        #if color was not chosen
        if data_dict.get('cor')==None:
            data_dict['cor']=None

        #if cover is needed
        cover_flag=data_dict["capa"]

        #fixing data_dict to use it on insert_all()
        data_dict["data"]=data_dict["inicio"]
        data_dict["locador_e_cpf"]=data_dict["locador"]+" CPF. "+\
                                    data_dict["cpf"]

        recibo_list=[]
        #generate all images for recibo_list first
        if cover_flag:
            '''creates cover'''
            #insert all
            form = Forms("data/cover.png")
            form.insert_all(data_dict, "data/cover_config.txt", locatario=data_dict['cor'])


            recibo_list.append(form.image)

        #deals with pages

        original_data=data_dict.copy()
        first = int(data_dict["primeiro_numero"])
        for number in range(first,
                            first+int(data_dict["numero"])):
            '''creates pages'''

            #fix date
            data_dict["data"]=up_month(number-1,original_data["data"])
            data_dict["vencimento"]=up_month(
                number-1,original_data["vencimento"])

            #fix current number and formatting stuff
            data_dict["periodo"]=data_dict["data"]+" A "+\
                                  up_month(1,data_dict["data"])
            data_dict["numero"]=str(number)
            
            #insert all
            form = Forms("data/page.png")
            form.insert_all(data_dict, "data/page_config.txt")
            
            recibo_list.append(form.image)
            
        #data with a4 sheet sizes
        with open("data/format_data.txt") as f:
            format_data=[x.split(",") for x in f.readlines()]

        a4_x=int(format_data[0][0])
        a4_y=int(format_data[0][1])


        #creates blank A4 formatted image
        base = [Image.new("RGB", [a4_x, a4_y], color="white")]*\
               (int(len(recibo_list)/4)+1)

        #delete previous recibos
        c=0
        while True:
            try:
                os.remove(f"recibos/{c}.png")
                c+=1
                
            except:
                break

        #join recibos into a4 pages
        c=0
        for x in range(len(base)):
            h=0

            base[x].paste((255,255,255),(0,0,base[x].size[0],base[x].size[1]))
            for y in range(4):
                try:
                    base[x].paste(recibo_list[c],box=(0,h))
                    h+=recibo_list[y*(x+1)].size[1]
                    c+=1
                except:
                    break
                    
            base[x].save('recibos/'+str(x)+".png")

        
            

if __name__ == "__main__":
    recibo({
        "locatario":"EU",
        "local":"MINHA CASA",
        "periodo":"ALGUNS DIAS",
        "vencimento":"23/1/2020",
        "valor":"R$255",
        "numero":"42",
        "locador":"FULANO DE TAL SILVA",
        "cpf":"123,456,789-10",
        "agua":"23123",
        "numero":"3",
        "inicio":"2/1/2020"
        },False)


