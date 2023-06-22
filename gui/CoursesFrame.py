import tkinter as tk
from tkinter import messagebox, ttk


class CoursesFrame(ttk.Frame):
    '''Frame that contains the user interface for selecting and adding courses in the ScheduleMaster app.
        Inherits from the ttk.Frame class.'''
    
    def __init__(self, master):
        '''Initializes the courses frame.'''
 
        super().__init__(master)
        self._master = master 
        self._faculty_filter = tk.StringVar()
        self._credits_filter = tk.StringVar()
        self._set_frm_settings()
        self._create_widgets()


    def _set_frm_settings(self):
        '''Sets the frame settings.'''

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


    def _create_widgets(self):
        '''Creates the widgets in the CoursesFrame.'''

        self._create_frm_filters()
        self._create_frm_available_subjects()


    def _create_frm_filters(self):
        '''Creates the filters frame.'''
        
        self._frm_filters = ttk.Frame(self)
        self._frm_filters.grid(row=1, column=0, sticky='nsew')

        lbl_title = ttk.Label(self._frm_filters, text='Filtros', style='Title.TLabel')
        lbl_title.grid(row=0, column=0, sticky='w', padx=(100, 0))

        lbl_faculty = ttk.Label(self._frm_filters, text='Facultad', style='TextBold.TLabel')
        lbl_faculty.grid(row=1, column=0, sticky='w', padx=(100, 0))
        option_menu_faculty = ttk.OptionMenu(self._frm_filters, self._faculty_filter, 'Ingeniería', *['Ingeniería', 'Ciencias', 'Medicina', 'Artes', 'Ciencias políticas', 'Ciencias humanas'], style='Filters.TMenubutton')
        option_menu_faculty.grid(row=1, column=1, sticky='w')

        lbl_credits = ttk.Label(self._frm_filters, text='Créditos', style='TextBold.TLabel')
        lbl_credits.grid(row=2, column=0, sticky='w', padx=(100, 0))
        spin_box_credits = ttk.OptionMenu(self._frm_filters, self._credits_filter, 'Omitir', *['Omitir', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], style='Filters.TMenubutton')
        spin_box_credits.grid(row=2, column=1, sticky='w')

        btn_search = ttk.Button(self._frm_filters, text='Buscar', command=self._show_subjects)
        btn_search.grid(row=3, column=0, sticky='w', padx=(100, 0), pady=15)


    def _create_frm_available_subjects(self):
        '''Creates the available courses frame.'''

        self._frm_available_subjects = ttk.Frame(self)
        self._frm_available_subjects.rowconfigure(1, weight=1)
        self._frm_available_subjects.columnconfigure(0, weight=1)
        self._frm_available_subjects.grid(row=2, column=0, sticky='nsew')
        
        lbl_title = ttk.Label(self._frm_available_subjects, text='Asignaturas', style='Title.TLabel')
        lbl_title.grid(row=0, column=0, sticky='w', padx=(100, 0))


    def _get_filters_dict(self):
        '''Returns a dictionary of filters based on the selected options.'''

        faculties = {'Ingeniería': 1, 'Ciencias': 2, 'Medicina': 3, 'Artes': 4, 'Ciencias políticas': 5, 'Ciencias humanas': 6}
        faculty_id = faculties[self._faculty_filter.get()]

        if self._credits_filter.get() == 'Omitir':
            credits = None
        else:
            credits = self._credits_filter.get()

        return {'FACULTY_ID': faculty_id, 'CREDITS': credits}
    

    def _show_subjects(self):
        '''Shows the available subjects based on the selected filters.'''

        subjects = self._master.controller.get_subjects(self._get_filters_dict())

        self._create_trv_subjects()

        for subject in subjects:
            self._trv_subjects.insert(
                '',
                tk.END,
                text=subject.get_id(),
                values=(subject.get_credits(), subject.get_name())
            )


    def _create_trv_subjects(self):
        '''Creates the Treeview widget to display available subjects.'''

        self._trv_subjects = ttk.Treeview(self._frm_available_subjects, columns=('credits', 'name'))

        self._trv_subjects.column('#0', anchor='w', width=100)
        self._trv_subjects.column('credits', anchor='w', width=100)
        self._trv_subjects.column('name', anchor='w', width=880)
        self._trv_subjects.heading('#0', text='    Id', anchor='w')
        self._trv_subjects.heading('credits', text='Créditos', anchor='w')
        self._trv_subjects.heading('name', text='Nombre', anchor='w')

        self._trv_subjects.bind('<<TreeviewSelect>>', self._show_courses)

        self._trv_subjects.grid(row=1, column=0, sticky='nsew', padx=100, pady=5)


    def _show_courses(self, event):
        '''Shows the available courses for a selected subject.'''

        subject_selected = self._trv_subjects.selection()
        self._subject_id = self._trv_subjects.item(subject_selected, 'text')
        courses = self._master.controller.get_courses(filters={'SUBJECT_ID': self._subject_id})

        self._create_win_courses()

        for course in courses:
            self._trv_courses.insert(
                '',
                tk.END,
                text=course.get_group_number(),
                values=(course.get_professor().get_name(), course.get_time_slot_one(), course.get_time_slot_two())
            )


    def _create_win_courses(self):
        '''Creates the window to display available courses.'''

        self._win_courses = tk.Toplevel(bg='white')
        self._win_courses.geometry('930x270')
        self._win_courses.title('Grupos')
        self._win_courses.rowconfigure(1, weight=1)
        self._win_courses.columnconfigure(0, weight=1)

        self._create_trv_courses()

        self._btn_add_course = ttk.Button(self._win_courses, text='Agregar a mi horario', command=self._add_course)
        self._btn_add_course.grid(row=1, column=0)


    def _create_trv_courses(self):
        '''Creates the Treeview widget to display available courses.'''

        self._trv_courses = ttk.Treeview(self._win_courses, columns=('professor', 'time_slot_one', 'time_slot_two'))

        self._trv_courses.column('#0', anchor='w', width=100)
        self._trv_courses.column('professor', anchor='w', width=300)
        self._trv_courses.column('time_slot_one', anchor='w', width=265)
        self._trv_courses.column('time_slot_two', anchor='w', width=265)
        self._trv_courses.heading('#0', text='    Grupo', anchor='w')
        self._trv_courses.heading('professor', text='Profesor', anchor='w')
        self._trv_courses.heading('time_slot_one', text='Día 1', anchor='w')
        self._trv_courses.heading('time_slot_two', text='Día 2', anchor='w')
        
        self._trv_courses.grid(row=0, column=0, sticky='nsew')


    def _add_course(self):
        '''Adds the selected course to the schedule.'''

        if not self._trv_courses.selection():
            messagebox.showinfo('Aviso', 'Seleccione un curso.')
            return
        
        course_selected = self._trv_courses.selection()
        course_group = self._trv_courses.item(course_selected, 'text')
        course = self._master.controller.get_course(id=(course_group, self._subject_id))
        validation = self._master.controller.course_is_valid(course)

        if validation == 'valid':
            self._master.controller.add_course_to_schedule(course)
            self._master.frm_schedule.update_trv_schedule()
            messagebox.showinfo('Aviso', 'Curso agregado exitosamente.')
        elif validation == 'croice':
            messagebox.showinfo('Aviso', 'No es posible agregar el curso, hay un conflicto de horario con otro curso.')
        else:
            messagebox.showinfo('Aviso', 'No es posible agregar el curso, ya existe un curso con la misma asignatura.')
        self._win_courses.destroy()