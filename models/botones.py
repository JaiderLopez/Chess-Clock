import flet as ft

class Control(ft.Container):
   def __init__(self,):
      super().__init__(expand=True, expand_loose= True)
      self.bgcolor = "#2d2d2d"
      self.height = 50
      self.border_radius = 5
      self.border = ft.border.all(1, "black")

      # self.content = ft.Icon(name= icon, color= 'black')
      # self.on_click = fun

class Settings(Control):
   def __init__(self,):
      super().__init__()
      self.icon = ft.Icons.SETTINGS

      self.content = ft.Icon(name= self.icon, color= 'white')

class Play_Pause(Control):
   def __init__(self,):
      super().__init__()
      self.icon1 = ft.Icons.PLAY_CIRCLE_OUTLINE_SHARP
      self.icon2 = ft.Icons.PAUSE_CIRCLE_FILLED_OUTLINED
      self.content = ft.Icon(name= self.icon1, color= '#4caf50')

class Reload_Plus(Control):
   def __init__(self,):
      super().__init__()
      self.icon1 = ft.Icons.RESTART_ALT_OUTLINED
      self.icon2 = ft.Icons.PLUS_ONE
      self.content = ft.Icon(name= self.icon1, color= 'white')
