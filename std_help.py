import pyttsx3
import kivy
from kivy.app import App
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
    def __init__(self, **kwargs):
        super(called, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols=2

        self.inside.add_widget(Label(text="Repeat"))
        self.Num = TextInput(multiline=False)
        self.inside.add_widget(self.Num)

        self.inside.add_widget(Label(text="Enter your text"))
        self.txt = TextInput(multiline=True)
        self.inside.add_widget(self.txt)

        self.add_widget(self.inside)
        self.submit1 = Button(text="Called Text", font_size=40)
        self.submit1.bind(on_press=self.pressed1)
        self.add_widget(self.submit1)

        self.submit2 = Button(text="Open File", font_size=20,size_hint=(0.2,0.1))
        #self.submit2.bind(on_press=self.pressed2)      1
        self.submit2.bind(on_press=self.pressed2)
        self.add_widget(self.submit2)

    def pressed1(self,intance):
        self.inside1 = GridLayout()
        self.inside1.cols = 2
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

    def pressed2(self,ints):
        self.remove_widget(self.inside)
        self.remove_widget(self.submit1)
        self.remove_widget(self.submit2)
        self.cols = 1

        self.inside2 = GridLayout()
        self.inside2.cols = 2

        self.inside2.add_widget(Label(text="Open or Create File"))
        self.F_name = TextInput(multiline=False)
        self.inside2.add_widget(self.F_name)

        self.add_widget(self.inside2)

        self.submit3 = Button(text="Open File", font_size=20, size_hint=(0.2, 0.1))
        self.submit3.bind(on_press=self.opt)
        self.add_widget(self.submit3)

    def opt(self,inpl):
        self.remove_widget(self.inside2)
        self.remove_widget(self.submit3)
        self.cols = 1

        self.insideX = GridLayout()
        self.insideX.cols = 2

        self.insideX.add_widget(Label(text="File Handle"))


        self.create = Button(text="Create New File or Edit Existing File", font_size=20)
        self.create.bind(on_press=self.pressed3)
        self.add_widget(self.create)

        self.Read = Button(text="Read File", font_size=20)
        self.Read.bind(on_press=self.pressed5)
        self.add_widget(self.Read)

        self.add_widget(self.insideX)

    def pressed3(self,inp):
        self.remove_widget(self.insideX)
        self.remove_widget(self.create)

        self.cols =1
        self.inside3 = GridLayout()
        self.inside3.cols = 2

        try:
            F_name = self.F_name.text
            F = open(f"{F_name}.txt", 'rb')

        except:
            F_name = self.F_name.text
            F = open(f"{F_name}.txt", 'a')

        self.inside3.add_widget(Label(text="Write Question"))
        self.Ques = TextInput(multiline=True)
        self.inside3.add_widget(self.Ques)

        #Ques = self.Ques.text
        #print(Ques)
        self.Name_file  = open(f'{F_name}.txt', 'a')
        #Name_file.write(f"Question - {Ques}")

        self.inside3.add_widget(Label(text="Write Ans"))
        self.Ans = TextInput(multiline=True)
        self.inside3.add_widget(self.Ans)

        #Ans = self.Ans.text
        self.Name_file  = open(f"{F_name}.txt", 'a')
        #Name_file.write(f"\nAnswer - {Ans}\n\n")


        self.submit4 = Button(text="save", font_size=20, size_hint=(0.2, 0.1))
        self.submit4.bind(on_press=self.pressed4)
        self.add_widget(self.inside3)
        self.add_widget(self.submit4)

    def pressed4(self,inps):
        self.remove_widget(self.submit4)
        self.remove_widget(self.inside3)
        self.remove_widget(self.inside2)

        Ques = self.Ques.text
        self.Name_file.write(f"Question - {Ques}")
        Ans = self.Ans.text
        self.Name_file.write(f"\nAnswer - {Ans}\n\n")
        Name_File = self.Name_file
        Name_File.close()
        self.add_widget(self.inside)
        self.add_widget(self.submit1)

    def pressed5(self,ipsl):
        self.remove_widget(self.insideX)
        self.remove_widget(self.create)

        self.cols = 1
        self.inside5 = GridLayout()
        self.inside5.cols = 2
        ans_sheet = ()

        self.inside5.add_widget(Label(text="Write File Name"))
        self.rd_ex = TextInput(multiline=False)
        self.inside5.add_widget(self.rd_ex)

        try:
            rd_ex = self.rd_ex.text
            data = open(f"{rd_ex}.txt", 'r')
            data = list(data)
            self.inside5.add_widget(Label(text="Write Exixting Question or Question Key :"))
            self.inp = TextInput(multiline=False)
            self.inside5.add_widget(self.inp)
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
                                self.inside5.add_widget(Label(text=k))
                                friend.say(k)
                                friend.runAndWait()
                            continue
                else:
                    r = r + 1

        except:
            if FileNotFoundError:
                print(f"{rd_ex}.txt >>> Such Of This File Is Not Exist ! Try Different Name.")
            print("Thank You For Visit")

        self.add_widget(self.inside5)




class MyApp(App):
    def build(self):
        return called()


if __name__ == "__main__":
    MyApp().run()
# def Revision():
#     ans_sheet = ()
#     rd_ex = input("Enter File Name")
#     try:
#         data  = open(f"{rd_ex}.txt",'r')
#         data = list(data)
#         inp = input("enter your question key")
#         inp.strip()
#         inp = list(inp.split(" "))
#         r = 0
#         for i in data:
#             for j in inp:
#                 if j in i:
#                     if data[r] in ans_sheet:
#                         pass
#                     else:
#                         ans_sheet = (data[r], data[r + 1])
#                         for k in ans_sheet:
#                             print(k)
#                             friend.say(k)
#                             friend.runAndWait()
#                         continue
#             else:
#                 r = r + 1
#
#     except:
#         if FileNotFoundError:
#             print(f"{rd_ex}.txt >>> Such Of This File Is Not Exist ! Try Different Name.")
#         print("Thank You For Visit")
#

# if __name__ == '__main__':
#     print("Choose one of them : ")
#     print("Press 1 for Calling Text \nPress 2 for Add More Practice Set. \nPress 3 for Revision \n")
#     choice = int(input("What you want to do : "))
#     # if choice==1:
#     #     print("hello")
#     #     called()
#     # elif choice==2:
#     #     add_new()
#     # elif choice==3:
#     called()
#     # else:
#     #     print("Enter Correct Choice")








