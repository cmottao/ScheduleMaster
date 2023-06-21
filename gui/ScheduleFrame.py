import tkinter as tk
from tkinter import ttk


class ScheduleFrame(ttk.Frame):
    '''Frame that contains the user's schedule in the ScheduleMaster app. Inherits from the ttk.Frame class.'''
    
    def __init__(self, master):
        '''Initializes the schedule frame of the ScheduleMaster app.'''

        super().__init__(master)
        self._master = master
        self._set_frm_settings()
        self._create_widgets()


    def _set_frm_settings(self):
        '''Sets the frame settings.'''

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)


    def _create_widgets(self):
        '''Create the widgets in the ScheduleFrame.'''

        lbl_title = ttk.Label(self, text='Mi horario', style='Title.TLabel')
        lbl_title.grid(row=0, column=0, sticky='w', padx=(100, 0))

        self._create_trv_schedule()

        btn_remove_course = ttk.Button(self, text='Remover curso', command=self._remove_course)
        btn_remove_course.grid(row=2, column=0)


    def _create_trv_schedule(self):
        '''Creates the Treeview widget to display the user's schedule.'''

        self._trv_schedule = ttk.Treeview(self, columns=('id', 'group', 'professor', 'time_slot_one', 'time_slot_two'))

        self._trv_schedule.column('#0', anchor='w', width=300)
        self._trv_schedule.column('id', anchor='w', width=30)
        self._trv_schedule.column('group', anchor='w', width=60)
        self._trv_schedule.column('professor', anchor='w', width=290)
        self._trv_schedule.column('time_slot_one', anchor='w', width=200)
        self._trv_schedule.column('time_slot_two', anchor='w', width=200)
        self._trv_schedule.heading('#0', text='    Asignatura', anchor='w')
        self._trv_schedule.heading('id', text='Id', anchor='w')
        self._trv_schedule.heading('group', text='Grupo', anchor='w')
        self._trv_schedule.heading('professor', text='Profesor', anchor='w')
        self._trv_schedule.heading('time_slot_one', text='Día 1', anchor='w')
        self._trv_schedule.heading('time_slot_two', text='Día 2', anchor='w')

        self._trv_schedule.grid(row=1, column=0, sticky='nsew', padx=100, pady=5)


    def _remove_course(self):
        '''Removes the selected course from the schedule.'''

        if not self._trv_schedule.selection():
            return

        course_selected = self._trv_schedule.item(self._trv_schedule.selection())
        course_group = course_selected['values'][1]
        subject_id = course_selected['values'][0]

        self._master.controller.remove_course_from_schedule(course_group, subject_id)
        self._master.frm_schedule.update_trv_schedule()


    def update_trv_schedule(self):
        '''Updates the Treeview widget with the current schedule.'''

        courses = self._master.controller.get_courses_from_schedule()
        self._create_trv_schedule()

        for course in courses:
            self._trv_schedule.insert(
                '',
                tk.END,
                text=course.get_subject().get_name(),
                values=(course.get_subject().get_id(), course.get_group_number(), course.get_professor().get_name(), course.get_time_slot_one(), course.get_time_slot_two())
            )