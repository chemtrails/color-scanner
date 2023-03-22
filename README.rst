.. code-block:: python

    from scanner import ColorScanner

    def callback(color):
        print(color)

    color_pick = ColorScanner(hex=True, callback=callback).scan()
