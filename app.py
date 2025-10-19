import flet as ft
import threading
import time

#models
from models.botones import *
from models.player import Player
from validations.clock import ChessClock

class App(ft.Container):
    # ---------------------------------------- CONTROLES ----------------------------------------
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.dialog = None
        self.colors_list = {
            "player1": "#ffffff",
            "player2": "#000000",
            "clock_bg": "#2d2d2d",
            "controls": "#2d2d2d",
            "bg": "#1e1e1e",
            "accent": "#4caf50",
        }
        #  players
        self.time_player1 = 300
        self.time_player2 = 300
        self.increment = 0
        self.player1 = Player(1, self.time_player1)
        self.player1.col = {"xs": 12, "sm": 12, "md": 4, "lg": 4}
        self.player2 = Player(2, self.time_player2)
        self.player2.col = {"xs": 12, "sm": 12, "md": 4, "lg": 4}

        self.player1.on_click = self.switch_player_turn
        self.player2.on_click = self.switch_player_turn

        # clock
        self.chess_clock = ChessClock(self.time_player1, self.time_player2, self.update_ui, self.increment)
        self.game_started = False
        self.pause_event = threading.Event()

        #controls
        self.settings_button = Settings()
        self.settings_button.on_click = self.open_settings
        self.play_pause_button = Play_Pause()
        self.play_pause_button.on_click = self.play_pause
        self.reload_button = Reload_Plus()
        self.reload_button.on_click = self.reload_game
        
        self.controls_list = ft.ResponsiveRow(controls=[
            self.settings_button,
            self.play_pause_button,
            self.reload_button,
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20
        )
        self.content = ft.ResponsiveRow(
            controls=[
                self.player2,
                self.controls_list,
                self.player1,
            ], alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

    # ---------------------------------------- FUNCIONES ----------------------------------------
    def play_pause(self, e):
        if not self.game_started:
            self.game_started = True
            self.chess_clock.running = True
            self.pause_event.set()
            timer_thread = threading.Thread(target=self.chess_clock.countdown, args=(self.pause_event,))
            timer_thread.start()
            self.play_pause_button.content.name = self.play_pause_button.icon2
        else:
            if self.pause_event.is_set():
                self.pause_event.clear()
                self.play_pause_button.content.name = self.play_pause_button.icon1
            else:
                self.pause_event.set()
                self.play_pause_button.content.name = self.play_pause_button.icon2
        self.page.update()

    def reload_game(self, e):
        self.chess_clock.running = False
        self.game_started = False
        self.chess_clock = ChessClock(self.time_player1, self.time_player2, self.update_ui, self.increment)
        self.update_ui(self.time_player1, self.time_player2)
        self.play_pause_button.content.name = self.play_pause_button.icon1
        self.page.update()

    def open_settings(self, e):
        def set_time(new_time, new_increment=0):
            self.time_player1 = new_time
            self.time_player2 = new_time
            self.increment = new_increment
            self.reload_game(None)
            self.close_dialog()

        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Settings", color="white"),
            content=ft.Column([
                ft.ElevatedButton("1 min", on_click=lambda _: set_time(60, 0), bgcolor=self.colors_list["controls"], color="white"),
                ft.ElevatedButton("3 min", on_click=lambda _: set_time(180, 0), bgcolor=self.colors_list["controls"], color="white"),
                ft.ElevatedButton("3 | 2", on_click=lambda _: set_time(180, 2), bgcolor=self.colors_list["controls"], color="white"),
                ft.ElevatedButton("10 min", on_click=lambda _: set_time(600, 0), bgcolor=self.colors_list["controls"], color="white"),
                ft.ElevatedButton("15 min", on_click=lambda _: set_time(900, 0), bgcolor=self.colors_list["controls"], color="white"),
            ], tight=True),
            actions=[ft.TextButton("Close", on_click=self.close_dialog, style=ft.ButtonStyle(color=self.colors_list["accent"]))],
            actions_alignment=ft.MainAxisAlignment.END,
            bgcolor=self.colors_list["bg"]
        )
        self.page.overlay.append(self.dialog)
        self.dialog.open = True
        self.page.update()

    def close_dialog(self, e=None):
        if self.dialog and self.dialog in self.page.overlay:
            self.dialog.open = False
            self.page.update()
            # Let the close animation finish before removing, you can adjust the time
            time.sleep(0.1)
            self.page.overlay.remove(self.dialog)
            self.page.update()

    def switch_player_turn(self, e):
        if self.game_started:
            self.chess_clock.switch_player()
            self.update_ui(self.chess_clock.time_player1, self.chess_clock.time_player2)

    def update_ui(self, time_player1, time_player2):
        self.player1.minutes = time_player1 // 60
        self.player1.seconds = time_player1 % 60
        self.player1.update_texto()

        self.player2.minutes = time_player2 // 60
        self.player2.seconds = time_player2 % 60
        self.player2.update_texto()

        self.page.update()


def main(page: ft.Page):
    page.padding = 0
    page.bgcolor = "#1e1e1e"

    app = App(page)
    page.add(app)

if __name__ == '__main__':
    ft.app(target=main)