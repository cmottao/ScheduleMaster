import tkinter as tk
from tkinter import ttk


class ButtonsFrame(ttk.Frame):
    '''Frame that contains the main buttons of the ScheduleMaster app. Inherits from the ttk.Frame class.'''

    def __init__(self, master):
        '''Initializes the buttons frame of the ScheduleMaster app.'''

        super().__init__(master)
        self._master = master
        self._set_frm_settings()
        self._create_buttons()
        
    
    def _set_frm_settings(self):
        '''Sets the frame settings.'''

        self.grid(row=0, column=0, sticky='ew')


    def _create_buttons(self):
        '''Creates the buttons in the ButtonsFrame.'''

        btn_schedule = ttk.Button(self, text='Seleccionar cursos', command=self._master._show_frm_courses)
        btn_schedule.grid(row=0, column=0, sticky='w', padx=(100, 5), pady=20)

        btn_schedule = ttk.Button(self, text='Mi horario', command=self._master._show_frm_schedule)
        btn_schedule.grid(row=0, column=1, sticky='w', padx=5, pady=20)

        btn_schedule = ttk.Button(self, text='Descargar horario', command=self._master.download_schedule)
        btn_schedule.grid(row=0, column=2, sticky='w', padx=5, pady=20)