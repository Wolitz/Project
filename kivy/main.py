
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty,BooleanProperty


 
class WidgetExample(GridLayout):
    my_text = StringProperty("0")
    count_enbl = BooleanProperty(False)
    #slider_value_txt= StringProperty("0")

    def on_button_click(self):
        if self.count_enbl == True: 
            a = int(self.my_text)
            self.my_text = str(a + 1)

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enbl = False
        else:
            widget.text = "ON"
            self.count_enbl = True
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    #def on_slider_value(self, widget):
        #self.slider_value_txt = str(int(widget.value))


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "lr-bt"
        for i in range(100):
            size = dp(100)
            b = Button(text=str(i+1), size_hint =(None,None), size =(size,size))
            self.add_widget(b)

# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text ="A")
    #     b2 = Button(text ="B")
    #     b3 = Button(text = "C")
    #     self.orientation = "vertical"
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget(Widget): 
    pass  

class TheLabApp(App):
    pass

TheLabApp().run()