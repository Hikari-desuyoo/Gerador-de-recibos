'''
recibo() makes all the final image and saves them
'''
from insert_text import *
from date_manager import *
from PIL import Image

with open("data/format_data.txt") as f:
    format_data=[x.split(",") for x in f.readlines()]

a4_x=int(format_data[0][0])
a4_y=int(format_data[0][1])
    
def recibo(data_dict, cover_flag):
    '''
    data_dict keys:
    locador
    cpf
    locatario
    local
    valor
    agua
    inicio
    vencimento
    numero
    '''
    recibo_list=[]
    #creates blank A4 formatted image
    base = Image.new("RGB", [a4_x, a4_y], color="white")

    #fixing data_dict to use it on insert_all()
    data_dict["data"]=data_dict["inicio"]
    data_dict["locador_e_cpf"]=data_dict["locador"]+" CPF. "+\
                                data_dict["cpf"]
    
    #generate all images for recibo_list first
    if cover_flag:
        '''creates cover'''
        pass

    for number in range(1, int(data_dict["numero"])+1):
        '''creates pages'''

        #fix current number and formatting stuff
        data_dict["periodo"]=data_dict["data"]+"A"+\
                              data_dict["vencimento"]
        data_dict["numero"]=str(number)
        
        #insert all
        form = Forms("data/page.png")
        form.insert_all(data_dict, "data/page_config.txt")

        #fix date
        data_dict["data"]=up_month(1,data_dict["data"])
        data_dict["vencimento"]=up_month(
            1,data_dict["vencimento"])
    
        form.image.show()

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


