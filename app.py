import flet as ft
from math import pi

class Player(ft.Container):
   def __init__(self, number: int, time):
      super().__init__(expand= True)
      if number == 1:
         main_color = "#ffffff"
         second_color = "#000000"
      elif number == 2:
         main_color = "#000000"
         second_color = "#ffffff"
         self.rotate = ft.transform.Rotate(pi)

      self.bgcolor = main_color
      self.alignment = ft.alignment.bottom_center
      self.border = ft.border.all(1, second_color)
      self.width = 250
      self.height = 280

      self.minutes = time//60
      self.seconds = time%60
      self.texto = time
      self.clock = ft.Text(self.texto, size= 30, color= second_color)
      self.update_texto()

      self.content = ft.Column(controls=[
            ft.Text(f"Player {number}", color= second_color),
            ft.Container(width= self.width * 0.7, height= 66, bgcolor= ft.Colors.with_opacity(0.33, "#828282"), 
                        margin= ft.margin.only(bottom= 10), alignment= ft.alignment.center,
                        content= self.clock
            ) 
         ], 
      alignment= ft.MainAxisAlignment.END, horizontal_alignment= ft.CrossAxisAlignment.CENTER)

   def update_texto(self,):
      self.seconds %= 60
      self.texto = f"{self.minutes} : {self.seconds}" if self.seconds > 9 else f"{self.minutes} : 0{self.seconds}"
      self.clock.value = self.texto

class Control(ft.Container):
   def __init__(self,):
      super().__init__(expand=True, expand_loose= True)
      # self.bgcolor = "#438589"
      self.gradient = ft.LinearGradient(colors= ["#f6f6f6" ,"#828282",])
      self. width = 70
      self.height = 50
      self.border_radius = 5
      self.border = ft.border.all(1, "black")

      # self.content = ft.Icon(name= icon, color= 'black')
      # self.on_click = fun

class Settings(Control):
   def __init__(self,):
      super().__init__()
      self.icon = ft.Icons.SETTINGS

      self.content = ft.Icon(name= self.icon, color= 'black')

class Play_Pause(Control):
   def __init__(self,):
      super().__init__()
      self.icon1 = ft.Icons.PLAY_CIRCLE_OUTLINE_SHARP
      self.icon2 = ft.Icons.PAUSE_CIRCLE_FILLED_OUTLINED
      self.content = ft.Icon(name= self.icon1, color= 'black')

class Reload_Plus(Control):
   def __init__(self,):
      super().__init__()
      self.icon1 = ft.Icons.RESTART_ALT_OUTLINED
      self.icon2 = ft.Icons.PLUS_ONE
      self.content = ft.Icon(name= self.icon1, color= 'black')



class App(ft.Container):
# ---------------------------------------- CONTROLES ----------------------------------------
   def __init__(self, page):
      super().__init__()
      self.page = page
      self.colors_list = {
         "player1": "#ffffff",
         "player2": "#000000",
         "clock_bg": "#828282",
         "controls": "#438589",
         # "bg": "#828282",
         "bg": "#B3B7A6",
         "random": "#a72f66",
      }
      #  players
      self.time_player1 = 0
      self.time_player2 = 0
      self.player1 = Player(1, self.time_player1)
      self.player2 = Player(2, self.time_player2)
      
      #controls
      self.controls_list = ft.Row(controls=[
         Settings(),
         Play_Pause(),
         Reload_Plus(),
      
      ], alignment= ft.MainAxisAlignment.CENTER, spacing= 20
      )
      self.content = ft.Text('Hello World', size= 28, text_align= 'center', style= ft.TextStyle(italic= True))
 
# ---------------------------------------- GRAPHICS ---------------------------------------- 
   def build(self):
      self.page.window.width = 380
      self.page.window.height = 680
      self.page.padding = 0
      self.page.bgcolor = self.colors_list['bg']
      self.page.add(ft.Column(
         controls= [
            self.player2,
            self.controls_list,
            self.player1,
         ], horizontal_alignment= ft.CrossAxisAlignment.CENTER,
         alignment= ft.MainAxisAlignment.CENTER,
      ))
   
   def prueba(self, e):
      print("click")
      self.player1.seconds-=1
      self.player1.update_texto()
      self.page.update()
 
# ---------------------------------------- FUNCIONES ---------------------------------------- 
 
 
def main(page: ft.Page):
   app = App(page)
   app.build()
 
if __name__ == '__main__':
   ft.app(target = main)
