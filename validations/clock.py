import threading
import time

class ChessClock:
    def __init__(self, time_player1, time_player2, update_callback, increment=0):
        self.time_player1 = time_player1
        self.time_player2 = time_player2
        self.current_player = 1
        self.running = False
        self.update_callback = update_callback
        self.increment = increment

    def switch_player(self):
        if self.current_player == 1:
            self.time_player1 += self.increment
            self.current_player = 2
        else:
            self.time_player2 += self.increment
            self.current_player = 1

    def countdown(self, pause_event):
        while self.running:
            pause_event.wait()
            if self.current_player == 1:
                if self.time_player1 <= 0:
                    self.running = False
                    break
                time.sleep(1)
                self.time_player1 -= 1
                self.update_callback(self.time_player1, self.time_player2)
            else:
                if self.time_player2 <= 0:
                    self.running = False
                    break
                time.sleep(1)
                self.time_player2 -= 1
                self.update_callback(self.time_player1, self.time_player2)
