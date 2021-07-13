from lib.qr import QR
from lib.led import Led


class Hardware:
    def __init__(self):
        self.qr = QR()
        self.led = Led()

    def wait_for_input(self):
        # read qr code
        # validate code
        # throw exception if invalid
        # return if valid
        return

    def invalid_code(self):
        # show invalid light
        pass

    def valid_code(self):
        # show valid light
        # for better challenge we make this arbitrary complicated (e.g. blinking, stranding, multi color)
        pass
