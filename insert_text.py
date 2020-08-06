from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

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
    def insert(self, text, size, position, color=(0,0,255)):
        #get font from path "data/font_file"
        font = ImageFont.truetype("data/font_file.ttf", size)
        
        #writes on template
        self.draw.text(
            position, text, color, font=font)

    """
    insert all text(from entries_dict) with configurations
    from a txt.
    """
    def insert_all(self, entries_dict, filepath):
        #opens data
        with open(filepath) as f:
            insert_info = [x.split(",") for x in f.readlines()]

        #inserts each data
        for x in insert_info:
            key,size,xpos,ypos=x
            
            self.insert(
                entries_dict[key],
                int(size),
                (int(xpos), int(ypos))
                )
            
        
        

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
