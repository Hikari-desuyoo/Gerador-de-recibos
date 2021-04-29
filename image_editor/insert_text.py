from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def text_divider(text,max_per_line):
    original=text
    text=text.split(' ')
    breaklines=[]

    line_size=0
    add_text=''
    for x in text:
        if len(x)>max_per_line:
            breaklines.append(x)
        elif len(x)+len(add_text)>max_per_line:
            breaklines.append(add_text[:-1])
            add_text=f'{x} '
        else:
            add_text+=f'{x} '
    breaklines.append(add_text[:-1])
    if ' '.join(breaklines)!=original:
        breaklines=[original]
    return breaklines

            
            
            

'''
Forms is used to insert text into a template
'''
class Forms:
    def __init__(self, template_path):
        #loads image and
        #creates draw object to write text on it later.
        self.image = Image.open(template_path)
        self.draw = ImageDraw.Draw(self.image)
        
    """
    inserts text on image
    """
    def insert(self, text, size, position, color, center):
        #get font from path "data/font_file"
        font = ImageFont.truetype("data/font_file.ttf", size)

        if center:
            w,h = self.draw.textsize(text, font=font)
            W,H = position
            position = W-(w/2),H
        
        #writes on template
        self.draw.text(
            position, text, color, font=font)

    """
    insert all text(from entries_dict) with configurations
    from a txt.
    """
    def insert_all(self, entries_dict, filepath, **text_color):
        #opens data
        with open(filepath) as f:
            insert_info = [x.split(",") for x in f.readlines()]

        backup_dict= entries_dict.copy()
        #inserts each data
        for x in insert_info:
            entries_dict=backup_dict.copy()
            key,size,xpos,ypos,linebreak=x
            center = False
            if 'c' in linebreak:
                linebreak=linebreak.replace('c','')
                center=True
                

            color = text_color[key] \
                    if text_color.get(key)!=None\
                    else (0,0,255)

            while type(entries_dict[key])==list:
                entries_dict[key]=entries_dict[key][0]

            try:
                linebreak = int(linebreak)
                entries_dict[key]=text_divider(entries_dict[key],linebreak)
            except:
                entries_dict[key]=[entries_dict[key]]
            mod=0
            
            for y in entries_dict[key]:
                self.insert(
                    y,
                    int(size),
                    (int(xpos), int(ypos)+mod),
                    color,
                    center
                    )
                mod+=int(size)
                
        
        

if __name__ == "__main__":
    page = Forms("data/page.png")
    test_dict={
        "locatario":"EU",
        "local":"MINHA CASA",
        "periodo":"ALGUNS DIAS",
        "vencimento":"ALGUMA HORA",
        "valor":"R$255",
        "numero":"42",
        "locador_e_cpf":"FULANO DE TAL SILVA CPF. "+"123,456,789-10",
        "inicio":"30/2/-201"
        }
    page.insert_all(test_dict, "data/page_config.txt")
    page.image.show()
