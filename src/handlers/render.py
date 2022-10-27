RESET = '\033[0m'
def rgb(r,g,b,bg=False):
    """
    Can set text to any color on the rgb spectrum.
    USAGE:
        print("Hello" + rgb(255, 128, 0) + "World!")
    """
    return '\033[{};2;{};{};{}m'.format(48 if bg else 38,r,g,b)

class render:

    @classmethod
    def output(update, type) -> str:
        #: output is not necessary to be worked on yet.
        pass
    
    @classmethod
    def styles(update, _type:str, txt:str) -> str:
        
        #: use type to return correct styling
        if _type.lower() == 'info':
            print(rgb(64, 64, 64) + '[' + rgb(204, 204, 0) + 'INFO' + rgb(64, 64, 64) + ']' + RESET + ': ' + txt)

        if _type.lower() == 'error':
            print(rgb(64, 64, 64) + '[' + rgb(102, 0, 0) + 'ERROR' + rgb(64, 64, 64) + ']' + RESET + ': ' + txt)


render = render()