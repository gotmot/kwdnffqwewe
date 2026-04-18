import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_date DATE,
    email TEXT UNIQUE,
    course_name TEXT NOT NULL,
    enrollment_date DATE
)
''')

students_data = [
    ('Иван Иванов', '2001-05-15', 'ivan@example.com', 'Математика', '2023-09-01'),
    ('Анна Петрова', '2002-03-20', 'anna@example.com', 'Программирование', '2023-09-01'),
    ('Сергей Сидоров', '2001-11-10', 'sergey@example.com', 'Математика', '2023-09-02'),
    ('Елена Кузнецова', '2003-01-25', 'elena@example.com', 'Физика', '2023-09-03'),
    ('Дмитрий Волков', '2002-07-12', 'dmitry@example.com', 'Программирование', '2023-09-05'),
    ('Мария Морозова', '2001-09-30', 'maria@example.com', 'Математика', '2023-09-05')
]

cursor.executemany('''
INSERT INTO Students (name, birth_date, email, course_name, enrollment_date)
VALUES (?, ?, ?, ?, ?)
''', students_data)
conn.commit()

query = '''
SELECT course_name, COUNT(*) as student_count
FROM Students
GROUP BY course_name
HAVING COUNT(*) > 1
'''

cursor.execute(query)
results = cursor.fetchall()

print("Записи :")
for row in results:
    print(f"Курс {row[0]} Студентов: {row[1]}")

conn.close()

