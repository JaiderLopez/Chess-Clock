import flet as ft
from math import pi

class Player(ft.Container):
   def __init__(self, number: int, time, **kwargs):
      super().__init__(expand= True, **kwargs)
      if number == 1:
         main_color = "#ffffff"
         second_color = "#000000"
      elif number == 2:
         main_color = "#000000"
         second_color = "#ffffff"
         self.rotate = ft.transform.Rotate(pi)

      self.bgcolor = main_color
      self.alignment = ft.alignment.bottom_center

      self.minutes = time//60
      self.seconds = time%60
      self.texto = time
      self.clock = ft.Text(self.texto, size= 30, color= second_color)
      self.update_texto()

      self.content = ft.Column(controls=[
            ft.Text(f"Player {number}", color= second_color),
            ft.Container(expand=True, bgcolor= ft.colors.TRANSPARENT, 
                        margin= ft.margin.only(bottom= 10), alignment= ft.alignment.center,
                        content= self.clock
            ) 
         ], 
      alignment= ft.MainAxisAlignment.END, horizontal_alignment= ft.CrossAxisAlignment.CENTER)

   def update_texto(self,):
      self.seconds %= 60
      self.texto = f"{self.minutes} : {self.seconds}" if self.seconds > 9 else f"{self.minutes} : 0{self.seconds}"
      self.clock.value = self.texto

