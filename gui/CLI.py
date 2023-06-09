import os
from tabulate import tabulate

from data.Course import Course
from data.Subject import Subject
from data.Faculty import Faculty
from exceptions.NoRecordsFound import NoRecordsFound


class CLI():
    '''Command line interface for the application'''
    
    def show_menu(self):
        os.system('cls')
        print('Bienvrenido/a a ScheduleMaster CLI version\n')
        print('1 -> Consultar listado de facultades')
        print('2 -> Consultar oferta de cursos')
        print('3 -> Salir de la aplicacion')
        print('Seleccione una opcion')
    
    def get_option(self):
        self.show_menu()
        option = input('>>> ')

        return option

    def ask_filters(self):
        ''''This function will ask user for faculty id and number of credits to show a course, and return the filers dict'''
        os.system('cls')
        faculty_id = input('Id de facultad: ')
        n_credits = input('Numero de creditos de asignatura (deje en blanco si desea omitir este filtro): ')

        filters = {
            'FACULTY_ID': int(faculty_id),
            'CREDITS': int(n_credits) if n_credits != '' else None
        }

        return filters

    def show_subjects(self):
        filters_dict = self.ask_filters()
        os.system('cls')
        subjects = Subject.retrieve_from_database(filters=filters_dict)
        if subjects:
            subjects = [
                [subject.get_id(), subject.get_name(), subject.get_credits(), subject.get_faculty().get_name()]
                for subject in subjects
                ]

            print(tabulate(
                subjects, headers=['id', 'Nombre', 'Creditos', 'Facultad'], tablefmt='presto'
            ))
        else:
            raise NoRecordsFound(
                'No se encontraron asignaturas que cumplan los criterios de seleccion establecidos, por favor vuelva a intentar'
                )
    
    def show_courses(self):
        self.show_subjects()
        subj_id = int(input('Ingrese el id de la asignatura la cual desea consultar oferta: '))
        os.system('cls')
        courses = Course.retrieve_from_database(filters={'SUBJECT_ID': subj_id})
        if courses:
            courses = [
                [course.get_group_number(), course.get_subject().get_name(),
                course.get_credits(), course.get_professor().get_name(), 
                course.get_time_slot_one(), course.get_time_slot_two()]
                for course in courses
            ]

            print(tabulate(
                courses, headers=['Grupo', 'Asignatura', 'Creditos', 'Profesor', 'Dia 1', 'Dia 2'], tablefmt='presto'
            ))
        else:
            raise NoRecordsFound(f'No se encontraron cursos de la materia con id {subj_id}. Por favor revise los datos y vuelva a intentar')


    def show_faculties(self):
        os.system('cls')
        faculties = Faculty.retrieve_from_database()
        faculties = [[faculty.get_id(), faculty.get_name()] for faculty in faculties]
        print(tabulate(
            faculties, headers=['id', 'Nombre'], tablefmt='presto'
        ))



    def run(self):
        while True:
            option = self.get_option()

            try:
                if option == '1':
                    self.show_faculties()
                elif option == '2':
                    self.show_courses()
                elif option == '3':
                    break
                else:
                    print('Opcion invalida')
            except ValueError:
                print('Por favor ingrese solo datos en un formato valido.')
            except NoRecordsFound as e:
                print(e)
            
            input('Presione enter para continuar...')