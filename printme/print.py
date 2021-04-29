import os
from PIL import Image
def imprimir():
    fp='recibos/'
    final_fp="recibo_pdf.pdf"
    recibos=[]
    c=0
    while True:
        try:
            recibos.append(Image.open(f'{fp}{c}.png').convert('RGB'))
            c+=1
        except:
            break

    recibos[0].save(final_fp, save_all=True,
                    append_images=recibos[1:])
    print(os.getcwd())
    os.startfile( final_fp)
