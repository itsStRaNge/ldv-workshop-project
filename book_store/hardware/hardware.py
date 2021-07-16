from lib import qr
from lib import led


class Hardware:
    def __init__(self):
        self.qr = qr.QR()
        self.led = led.Led()

    def wait_for_input(self) -> str:
        msg = self.qr.read()
        msg = self.encode(msg)
        self.validate(msg)
        return msg

    def invalid_code(self):
        self.led.set_color(led.RED)

    def valid_code(self):
        # for better challenge we make this arbitrary complicated (e.g. blinking, stranding, multi color)
        self.led.set_color(led.GREEN)

    def encode(self, msg: str):
        return "decoded-message"

    def validate(self, msg):
        # do some regex matching here
        # throw if does not match
        msg + "-validate"
