import pyttsx3
import kivy
from kivy.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button




friend = pyttsx3.init()
"""VOICE"""
voices = friend.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
friend.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#What type of work completed : 1 - called text to speech of any line , {but not save only for increasing listing ability .  2- Add File Completed


class called(GridLayout):
    def __init__(self, **kwargs,):
        super(called, self).__init__(**kwargs)
        self.cols = 1

        self.inside_main = GridLayout()
        self.inside_main.cols=2

        self.inside_main.add_widget(Label(text="Repeat"))
        self.Num = TextInput(multiline=False)
        self.inside_main.add_widget(self.Num)

        self.inside_main.add_widget(Label(text="Enter your text"))
        self.txt = TextInput(multiline=True)
        self.inside_main.add_widget(self.txt)

        self.add_widget(self.inside_main)
        self.sub_rep = Button(text="Called Text", font_size=30,size_hint=(0.9,0.5))
        self.sub_rep.bind(on_press=self.Repeat)
        self.add_widget(self.sub_rep)

        self.File_option = Button(text="Go to File", font_size=30,size_hint=(0.9,0.5))
        self.File_option.bind(on_press=self.File_Opt)
        self.add_widget(self.File_option)

    def Repeat(self,intance):
        N = self.Num.text
        Txt = self.txt.text
        try:
            N = int(N)
            for i in range(N):
                friend.say(Txt)
                friend.runAndWait()
        except:
            for i in range(1):
                friend.say(Txt)
                friend.runAndWait()

    def File_Opt(self,inpl):
        try:
            self.remove_widget(self.Back1)
            self.remove_widget(self.Back2)
            self.remove_widget(self.inside_main)
            self.remove_widget(self.sub_rep)
            self.remove_widget(self.File_option)
            self.remove_widget(self.inside_Edit_File)
            self.remove_widget(self.file_opn)
            self.remove_widget(self.inside_File_Opt)
            self.remove_widget(self.inside_Edit_File_This)
        except:
            pass

        try:
            self.remove_widget(self.inside_Read_File)
            self.remove_widget(self.Read_x)
            self.remove_widget(self.Back4)
            self.remove_widget(self.Back3)

        except:
            pass


        self.remove_widget(self.inside_main)
        self.remove_widget(self.File_option)
        self.remove_widget(self.sub_rep)

        self.cols = 1

        self.inside_File_Opt = GridLayout()
        self.inside_File_Opt.cols = 3

        #self.inside_File_Opt.add_widget(Label(text="File Handle" ,font_size=40, pos_hint=(100,100)))


        self.File_create_Ex = Button(text="Create New File or Edit Existing File", font_size=20,size_hint =(1,.7))
        self.File_create_Ex.bind(on_press=self.Edit_File)
        self.add_widget(self.File_create_Ex)

        self.Read = Button(text="Read File", font_size=20,size_hint =(2,.7))
        self.Read.bind(on_press=self.Read_File)
        self.add_widget(self.Read)


        self.Back1 = Button(text="Return1", font_size=20, size_hint=(2, .7))
        self.Back1.bind(on_press=self.Main)
        self.add_widget(self.Back1)

        self.add_widget(self.inside_File_Opt)

    def Edit_File(self,ints):
        self.remove_widget(self.inside_main)
        self.remove_widget(self.sub_rep)
        self.remove_widget(self.inside_File_Opt)
        self.remove_widget(self.File_create_Ex)
        self.remove_widget(self.Read)

        try:
            self.remove_widget(self.Back1)
            self.remove_widget(self.Back3)
            self.remove_widget(self.inside_Edit_File)
            self.remove_widget(self.inside_Edit_File_This)
            self.remove_widget(self.Save_File)
        except:
            pass

        self.cols = 1

        self.inside_Edit_File = GridLayout()
        self.inside_Edit_File.cols = 2

        self.inside_Edit_File.add_widget(Label(text="Open or Create File"))
        self.F_name = TextInput(multiline=False)
        self.inside_Edit_File.add_widget(self.F_name)

        self.add_widget(self.inside_Edit_File)

        self.file_opn = Button(text="Open File", font_size=20, size_hint=(0.2, 0.1))
        self.file_opn.bind(on_press=self.Edit_File_This)
        self.add_widget(self.file_opn)

        self.Back2 = Button(text="Return2", font_size=20, size_hint=(2, .7))
        self.Back2.bind(on_press=self.File_Opt)
        self.add_widget(self.Back2)




    def Edit_File_This(self,inp):
        try:
            self.remove_widget(self.file_opn)
            self.remove_widget(self.Back2)
            self.remove_widget(self.Back3)
            self.remove_widget(self.inside_Edit_File)
        except:
            pass

        self.cols =1
        self.inside_Edit_File_This = GridLayout()
        self.inside_Edit_File_This.cols = 2

        try:
            F_name = self.F_name.text
            F = open(f"{F_name}.txt", 'rb')

        except:
            F_name = self.F_name.text
            F = open(f"{F_name}.txt", 'a')

        self.inside_Edit_File_This.add_widget(Label(text="Write Question"))
        self.Ques = TextInput(multiline=True)
        self.inside_Edit_File_This.add_widget(self.Ques)

        self.Name_file  = open(f'{F_name}.txt', 'a')

        self.inside_Edit_File_This.add_widget(Label(text="Write Ans"))
        self.Ans = TextInput(multiline=True)
        self.inside_Edit_File_This.add_widget(self.Ans)


        self.Name_file  = open(f"{F_name}.txt", 'a')

        self.add_widget(self.inside_Edit_File_This)


        self.Save_File = Button(text="save", font_size=20, size_hint=(0.2, 0.1))
        self.Save_File.bind(on_press=self.Saved_File)

        self.add_widget(self.Save_File)

        self.Back3 = Button(text="Return3", font_size=20, size_hint=(0.2, 0.1))
        self.Back3.bind(on_press=self.Edit_File)
        self.add_widget(self.Back3)

    def Saved_File(self,inps):
        self.remove_widget(self.inside_Edit_File)
        self.remove_widget(self.inside_Edit_File_This)
        self.remove_widget(self.Save_File)
        self.remove_widget(self.inside_main)
        self.remove_widget(self.Back3)



        Ques = self.Ques.text
        self.Name_file.write(f"Question - {Ques}")
        Ans = self.Ans.text
        self.Name_file.write(f"\nAnswer - {Ans}\n\n")
        Name_File = self.Name_file
        Name_File.close()
        self.add_widget(self.inside_main)
        self.add_widget(self.sub_rep)
        self.add_widget(self.File_option)

    def Read_File(self,pks):
        self.remove_widget(self.File_create_Ex)
        self.remove_widget(self.inside_main)
        self.remove_widget(self.Read)
        self.remove_widget(self.inside_File_Opt)
        try:
            self.remove_widget(self.Back1)
            self.remove_widget(self.Back4)
            self.remove_widget(self.Back_last)

        except:
            pass

        try:
            self.remove_widget(self.rd_ex)
            self.remove_widget(self.Read_x)
            self.remove_widget(self.inside_Read_File)
        except:
            pass

        self.cols = 1
        self.inside_Read_File = GridLayout()
        self.inside_Read_File.cols = 2


        self.inside_Read_File.add_widget(Label(text="Write File Name"))
        self.rd_ex = TextInput(multiline=False)
        self.inside_Read_File.add_widget(self.rd_ex)

        self.inside_Read_File.add_widget(Label(text="Question or Questtion Key"))
        self.inp= TextInput(multiline=False)
        self.inside_Read_File.add_widget(self.inp)

        self.add_widget(self.inside_Read_File)

        self.Read_x = Button(text="Read", font_size=20)
        self.Read_x.bind(on_press=self.Read_File_Speak)
        self.add_widget(self.Read_x)



        self.Back4 = Button(text="Return4", font_size=20)
        self.Back4.bind(on_press=self.File_Opt)
        self.add_widget(self.Back4)

    def Read_File_Speak(self,pls):
        try:
            self.remove_widget(self.Read_x)
            self.remove_widget(self.Back4)
            self.remove_widget(self.Back_last)
        except:
            pass
        self.remove_widget(self.File_create_Ex)
        self.remove_widget(self.Read_x)
        self.inside_Read_File_Speak = GridLayout()
        self.inside_Read_File_Speak.cols = 1

        try:
            ans_sheet = ()
            rd_ex = self.rd_ex.text
            data = open(f"{rd_ex}.txt", 'r')
            data = list(data)
            inp = self.inp.text
            inp.strip()
            inp = list(inp.split(" "))
            r = 0
            for i in data:
                for j in inp:
                    if j in i:
                        if data[r] in ans_sheet:
                            pass
                        else:
                            ans_sheet = (data[r], data[r + 1])
                            for k in ans_sheet:
                                self.remove_widget(self.inside_Read_File)
                                self.inside_Read_File_Speak.add_widget(Label(text=k))
                                friend.say(k)
                                friend.runAndWait()
                            continue
                else:
                    r = r + 1

        except:
            rd_ex = self.rd_ex.text
            if FileNotFoundError:
                self.inside_Read_File_Speak.add_widget(Label(text = f"{rd_ex}.txt >>> Such Of This File Is Not Exist ! Try Different Name."))

            self.remove_widget(self.inside_Read_File)
            self.inside_Read_File_Speak.add_widget(Label(text = "----Thank You For Visit----"))



        self.Back_last = Button(text="Return5", font_size=20)
        self.Back_last.bind(on_press=self.Read_File)
        self.add_widget(self.Back_last)
        self.add_widget(self.inside_Read_File_Speak)
        self.remove_widget(self.inside_Read_File_Speak)

    def Main(self,ops):
        try:
            self.remove_widget(self.Read)
            self.remove_widget(self.Back1)
            self.remove_widget(self.File_create_Ex)
            self.remove_widget(self.inside_File_Opt)
            self.add_widget(self.inside_main)
            self.add_widget(self.sub_rep)
            self.add_widget(self.File_option)

            # self.add_widget(self.inside_Edit_File)
            # self.add_widget(self.inside_Edit_File_This)
            # self.add_widget(self.)
        except:
            pass




class MyApp(App):
    def build(self):
        self.title = "Kids Pocket Book"
        self.icon = 'book_Kivy.png'
        return called()


if __name__ == "__main__":
    MyApp().run()






