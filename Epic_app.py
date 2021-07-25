
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from datetime import date
today = date.today()

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Year: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Month: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Day: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        self.insides = GridLayout()
        self.insides.cols = 2

        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        # print("Name:", name, "Last Name:", last, "Email:", email)
        # self.name.text = ""
        # self.lastName.text = ""
        # self.email.text = ""
        name = int(name)
        last = int(last)
        email = int(email)
        age = today.year - name - ((today.month, today.day) < (last, email)), today.month - last, today.day - email
        age = str(age)
        self.add_widget(self.insides)
        self.insides.add_widget(Label(text="Age: "))
        self.insides.add_widget(Label(text=f"your age in year month and day{age}",font_size='20sp',color=[0.1,4.9,98.1,1]))
        Return = Button(text="", font_size=30)
        self.remove_widget(self.submit)
        self.add_widget(Return)

        Return.bind(on_press=MyGrid)
        self.remove_widget(Return)
        self.add_widget(self.submit)









class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()