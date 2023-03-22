from mss import mss
from pynput import mouse


class ColorScanner():
    def __init__(self, hex: bool = False, callback=None) -> None:
        self.hex = hex
        self.callback = callback
        self.rgb = (0, 0, 0)

    def _scan(self, x: int, y: int, dx: int = 0, dy: int = 0) -> bool:
        area = {
            "left": x,
            "top": y,
            "width": 1,
            "height": 1
        }
        image = mss().grab(area)
        self.rgb = tuple(bytes(image.rgb))
        if not self.callback:
            return False
        if self.hex:
            self.callback('#%02x%02x%02x' % self.rgb)
        else:
            self.callback(self.rgb)

    def stop(self, x: int, y: int, dx: int, dy: int) -> bool:
        return False

    def scan(self) -> tuple | str:
        if not self.callback:
            with mouse.Listener(on_click=self._scan) as listener:
                listener.join()
            if self.hex:
                return '#%02x%02x%02x' % self.rgb
            return self.rgb
        with mouse.Listener(on_click=self.stop, on_move=self._scan) as listener:
            listener.join()
        if self.hex:
            return '#%02x%02x%02x' % self.rgb
        return self.rgb
