PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS students_in_classes;

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE students_in_classes (
    student_id INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(class_id) REFERENCES classes(id)
);
