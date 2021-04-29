from PIL import Image
def monochrome():
    fp='recibos/'
    recibos=[]
    c=0
    while True:
        try:
            recibo=Image.open(f'{fp}{c}.png').convert('1')
            recibo.save(f'{fp}{c}.png')
            c+=1
        except:
            break
