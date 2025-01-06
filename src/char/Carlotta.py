import time

from src.char.BaseChar import BaseChar, Priority


class Carlotta(BaseChar):
    def do_perform(self):
        self.bullet = 0
        if self.has_intro:
            self.logger.debug('has_intro wait click 1.2 sec')
            self.bullet = 1
            self.continues_normal_attack(1.2)
        self.continues_normal_attack(0.31)
        self.switch_next_char()
