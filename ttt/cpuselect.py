import pygame as pg 
import pygame_gui as pgui

from ttt.colors import * 

OPT_HOTSEAT = 'HOTSEAT'
OPT_CPU = 'CPU'

class CpuSelect: 
    '''
    A class that represents the dialog that pops up when the game is first run.
    The dialogue asks the user whether they want to play a hotseat game or 
    against the computer.
    '''

    def __init__(self): 
        '''
        Constructor for the CpuSelect object.
        '''
        self._spawn_dialog()   # idk, maybe doing it in-place inside the constructor is better?


    def is_hotseat(self) -> bool: 
        '''
        Spawns a dialogue that has two buttons:
        + [Hotseat]: PvP mode 
        + [Solo]: PvCPU mode 

        Returns:
            is_hotseat (bool): True if the user clicks [Hotseat]
                               False if the user clicks [Solo]
        '''

        click_result = self._listen_for_clicks()

        self._destroy_dialog() # maybe needed? 
        if click_result == OPT_HOTSEAT: 
            return True 
        else:
            return False


    def _spawn_dialog(self) -> None: 
        '''
        Helper function for spawning the dialog.
        '''
        
        # Wouldn't this conflict with board.py's own init() call? i don't know.
        # Maybe "de-init" the pygame before returning True or False in
        # is_hotseat() to keep it from conflicting? Is that even a thing? 
        pg.init()  
        pg.display.set_caption('Select') 

        window_size = (800, 800)   # change this size later
        self._window = pg.display.set_mode(window_size)

        background = pg.Surface(window_size)
        background.fill(BLACK)

        # TODO: draw buttons and keep their references as instance variables 
        # self._btn_hotseat = 
        # self._btn_cpu = 


    def _listen_for_clicks(self) -> str: 
        '''
        Helper function for listening to clicks. 

        Returns: 
            option (str): OPT_HOTSEAT if [Hotseat] was clicked
                          OPT_CPU if [Solo] was clicked 
        '''

        while True: 
            for event in pg.event.get(): 
                if event.type == pg.USEREVENT:
                    if event.user_type == pgui.UI_BUTTON_PRESSED:
                        if event.ui_element == self._btn_hotseat: 
                            return OPT_HOTSEAT
                        elif event.ui_element == self._btn_cpu: 
                            return OPT_CPU 


    def _destroy_dialog(self) -> None: 
        '''
        Helper function for destroying the current dialogue. 
        Do we have to "de-init" pygame for when Board.py takes over? I don't know. 
        '''
        self._window.quit()   # uhh, does this exist? 

