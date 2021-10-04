class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)


keys = Bunch(
    DOWN='\x1b[B',
    UP='\x1b[A',
    LEFT='\x1b[D',
    RIGHT='\x1b[C',
    ENTER='\x0d',  # ControlM  (Identical to '\r')
    ESCAPE='\x1b',
    CONTROLC='\x03',
    BACK='\x7f'
)