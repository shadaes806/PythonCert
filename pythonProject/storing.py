import Student, pickle

stds = [Student.Student(10,'dae', 'cs'), Student.Student(44, 'love', 'psyc'), Student.Student(90, 'poe', 'edu')]

with open('students.data', 'wb') as f:
    for s in stds:
        pickle.dump(s,f)