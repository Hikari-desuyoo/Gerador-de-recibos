'''sets up tkinter GUI for using the program'''
from tkinter import *
from tkinter import colorchooser

#default margin for widgets
PADX=20

class EasyTk():
    def __init__(self,app_title,previous_data_filepath="data/previous_input_data.txt"):
        '''
        getting previous inputed data from txt
        '''
        with open(previous_data_filepath,encoding="ANSI") as f:
            #gets all key:next:value pairs formatted as [key,value]
            pair_list=[x.split(":next:") for x in f.readlines()]
            
            for x in pair_list:
                #if no value, value=""
                if len(x)==1:
                    x.append("")

                #takes out /n from value
                else:
                    x[1]=x[1][:-1]


            #dictionary with previous data
            self.previous_data={
                key:value for key,value in pair_list}

        #list with data to be written on txt later
        self.new_data=[]


        #creates root
        self.root = Tk()
        self.root.title(app_title)
                
        #makes save_data function get called right before window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.save_data)
        #

    '''
    functions to get data from macros
    '''
    def get_entry(self,entry):
        return entry[1].get()
    
    def get_listbox(self,listbox):
        return listbox[1].get(listbox[1].curselection()[0])\
                                if len(listbox[1].curselection())!=0 else ""
    
    def get_date(self,date):
        return "/".join([x.get() for x in date[1]])

    def get_check(self,check):
        return check[1].get()

    def get_color(self,color):
        return color[1]

    def auto_get(self, object1):
        types=["entry","listbox","date","check","color"]
        get_function=[self.get_entry,self.get_listbox,self.get_date,
        self.get_check,self.get_color]

        for i in range(len(types)):
            if object1[2]==types[i]:
                print(get_function[i](object1))
                return get_function[i](object1)

    '''
    saving data on txt when window is closed
    '''
    #function to save data
    def save_data(self):
        for x in self.new_data:
            #getting and formatting elements from listbox
            if x[2]=="listbox":
                x[1]="!next!".join(x[1].get(0, "end"))
                print(x[1])

            #auto getting the rest because no formatation is needed
            else:
                x[1]=str(self.auto_get(x))



        #saves new_data on txt
        with open("data/previous_input_data.txt", "w") as f:
            for x in self.new_data:
                print(f"{x[0]}->{x[1] if x[1]!='' else 'vazio'}")
                f.write(x[0]+":next:"+x[1]+"\n")
                
        #closes window
        self.root.destroy()





    '''
    functions for making multiple
    widgets at the same time
    '''

    #simplifies labels
    def label_macro(self,text, coords,
                    sticky=None, fg="black"):
        label = Label(self.root, text=text, fg=fg)
        label.grid(column=coords[0], row=coords[1], padx=PADX,
                   sticky=sticky)
        return label

    #if  previous_data key doesn't exist, it will be created
    #assistence function for the others
    def retrieve(self,key, default=""):
        value = self.previous_data.get(key, default)
        self.previous_data[key]=value
        return value
        
    #simplifies entry widgets
    def entry_macro(self,title,coords, width=50, sticky=""):
        #label as title 
        self.label_macro(title,coords, sticky=sticky)
        
        #entry box under title
        entry = Entry(self.root, width=width)

        #insert data form previous session
        insert_string=self.retrieve(title)
        entry.insert(0, insert_string)
        
        #grid
        entry.grid(column=coords[0], row=coords[1]+1, padx=PADX, sticky=sticky)

        #return title and created object
        return_value=[title,entry,"entry"]
        self.new_data.append(return_value)
        return return_value



    #simplifies listbox
    def listbox_macro(self,title, coords):
        #label as title
        self.label_macro(title,coords)

        '''listbox widget'''
        #list box under title    
        listbox= Listbox(self.root, width=50, exportselection=0)

        #insert listbox previous contents
        contents=self.retrieve(title).split("!next!")
        
        for i,x in enumerate(contents):
            #x="" is ignored
            listbox.insert(i,x) if x!="" else 0

        #grid
        listbox.grid(column=coords[0], row=coords[1]+1, padx=PADX)
        #
        ''''''
        
        '''scrollbar widgets'''
        #horizontal
        scroll= Scrollbar(self.root, orient="horizontal", command= listbox.xview )
        #grid
        scroll.grid(column=coords[0], row=coords[1]+2, padx=PADX, sticky="W")

        #vertical
        scroll= Scrollbar(self.root, command= listbox.yview )
        #grid
        scroll.grid(column=coords[0], row=coords[1]+1,  sticky="e")
        ''''''

        '''widgets to modify the listbox'''
        #button for removing content
        button = Button(self.root, text="Deletar elemento selecionado",
                        bg="red",fg="white",                    

                        command=\
                        lambda:\
                        listbox.delete(listbox.curselection()[0])\
                        if len(listbox.curselection())!=0 else 1
                        )
        #grid
        button.grid(column=coords[0], row=coords[1]+1, padx=PADX, sticky="SE")
        ####

        #entry box for adding content
        entry = Entry(self.root, width=45)
        #grid
        entry.grid(column=coords[0], row=coords[1]+3, padx=PADX, sticky="W")
        ####

        #button to make entry box work
        button = Button(self.root, text="+",
                        bg="green",fg="white",
                        
                        command=\
                        lambda:[listbox.insert("end",entry.get()),\
                                entry.delete(0,len(entry.get()))])
        #grid    
        button.grid(row=coords[1]+3, column=coords[0], padx=PADX, sticky="E")
        ####

        
        ''''''

        #return title and created object
        return_value=[title,listbox,"listbox"]
        self.new_data.append(return_value)
        return return_value

    #return entry boxes for inserting date
    def date_macro(self,title,coords):
        insert_string=self.retrieve(title,default="//").split("/")    

        #label as title
        self.label_macro(title, coords, sticky="SW")

        '''entry widgets'''
        date_entries=[]
        entry_space=30
        entry_width=[3,3,6]

        
        for i in range(0,3):
            #3 widgets for day,month,year
            date_entries.append(Entry(width=entry_width[i]))
            date_entries[i].insert(0, insert_string[i])
            #grid
            date_entries[-1].grid(
                column=coords[0], row=coords[1]+1,#coords
                padx=PADX+i*entry_space,#spacement
                sticky="SW")#justify
        ''''''


        return_value=[title,date_entries, "date"]
        self.new_data.append(return_value)
        return return_value

    #simplyfies check_button
    def check_macro(self,title, coords, sticky="", padx=PADX):
        check_var= IntVar()
        check = Checkbutton(self.root,text=title, variable = check_var)
        check.select() if self.retrieve(title)== "1" else 0
        #grid
        check.grid(row=coords[1], column=coords[0], padx=padx,
                   sticky=sticky)

        return_value=[title, check_var, "check"]
        self.new_data.append(return_value)
        return return_value

    #simplyfies color picking
    def color_macro(self,title,coords,padx=PADX,sticky=""):
        def color_picker():
            chosen_color=colorchooser.askcolor(color=self.retrieve(title))[1]
            chosen_color="#000000"if chosen_color in (None,"") else chosen_color
            r=int(chosen_color[1:3],16)>132
            g=int(chosen_color[3:5],16)>132
            b=int(chosen_color[5:7],16)>132

            fg_color = "black" if r or g or b else "white"
            self.new_data.append([title,chosen_color,"color"])
            button.config(fg=fg_color,bg=chosen_color)
            
            
        button=Button(self.root,text=title, command=color_picker)
        button.grid(row=coords[1], column=coords[0], padx=padx, sticky=sticky)

        return #DEIXAR PARA AMANHÃ

    def button_macro(self,title,coords,command,fg="",bg="",padx=PADX,sticky=""):
        button=Button(self.root,text=title, command=command,fg=fg,bg=bg)
        #grid
        button.grid(row=coords[1], column=coords[0], padx=padx, sticky=sticky)
        return button
        
        
        
    #breaks line by inserting empty label
    def line_break(self,row):
        self.label_macro("",(0,row))
    #
    '''
    mainloop
    '''
    def start(self):
        self.root.mainloop()













