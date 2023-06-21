import tkinter as tk
from tkinter import ttk

from business.Controller import Controller

from .ButtonsFrame import ButtonsFrame
from .CoursesFrame import CoursesFrame
from .ScheduleFrame import ScheduleFrame


class MainWindow(tk.Tk):
    '''Main window of the ScheduleMaster app. Inherits from the tkinter.Tk class.'''

    def __init__(self):
        '''Initializes the main window of the ScheduleMaster app.'''

        super().__init__()
        self.controller = Controller()
        self._set_win_settings()
        self._create_widgets()
        self._set_icon()
        self._set_widgets_styles()
        self._show_frm_courses()
        

    def _set_win_settings(self):
        '''Sets the window settings.'''

        self.title('ScheduleMaster')
        self.geometry('1280x720')
        self.configure(bg='white')
        self.resizable(False, False)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)


    def _create_widgets(self):
        '''Creates the widgets in the MainWindow.'''

        self.frm_buttons = ButtonsFrame(self)
        self.frm_courses = CoursesFrame(self) 
        self.frm_schedule = ScheduleFrame(self)


    def _set_icon(self):
        '''Sets the window icon.'''

        icon_image = tk.PhotoImage(file='./resources/schedule_master_icon.png')
        self.iconphoto(True, icon_image)


    def _set_widgets_styles(self):
        '''Configures the styles of various widgets using the ttk.Style class.'''

        style = ttk.Style()
        style.configure('TFrame', background='white')
        style.configure('Title.TLabel', font=('San Francisco', 16, 'bold'), background='white')
        style.configure('TextBold.TLabel', font=('San Francisco', 12, 'bold'), background='white')
        style.configure('Text.TLabel', font=('San Francisco', 12), background='white')
        style.configure('Filters.TMenubutton', font=('San Francisco', 12))
        style.configure('TButton', font=('San Francisco', 12))
        style.configure('Treeview', font=('San Francisco', 10))
        style.configure('Treeview.Heading', font=('San Francisco', 12, 'bold'))
        style.configure('TSpinbox', font=('San Francisco', 12))


    def _show_frm_courses(self):
        '''Hides the ScheduleFrame and displays the CoursesFrame.'''

        self.frm_schedule.grid_remove()
        self.frm_courses.grid(row=1, column=0, sticky='nsew')


    def _show_frm_schedule(self):
        '''Hides the CoursesFrame and displays the ScheduleFrame.'''

        self.frm_courses.grid_remove()
        self.frm_schedule.grid(row=1, column=0, sticky='nsew')


    def download_schedule(self):
        '''Downloads the schedule that the user has set up.'''

        pass


    def run(self):
        '''Runs the mainloop of the ScheduleMaster app.'''

        self.mainloop()