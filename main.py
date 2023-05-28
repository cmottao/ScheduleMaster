# import random
# from config.db import engine
# from sqlalchemy.sql import text

# if __name__ == '__main__':
#     subject_ids = [i for i in range(2, 24+1)]
#     professors_ids = [i for i in range(1, 33+1)]
#     tslots_id = [i for i in range(1, 30+1)]
#     query = '''INSERT INTO courses(group_number, subject_id, professor_id, time_slot_1, time_slot_2)
#                VALUES ({}, {}, {}, {}, {});'''
    
#     with engine.connect() as con:
#         for sub in subject_ids:
#             for g in range(1,6):
#                 professor = random.choice(professors_ids)
#                 tslot1, tslot2 = random.sample(tslots_id, 2)
#                 q=text(query.format(g, sub, professor, tslot1, tslot2))
#                 con.execute(q)
#                 con.commit()