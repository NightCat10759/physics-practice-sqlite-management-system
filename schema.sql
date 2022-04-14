
CREATE TABLE Exercises (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    chapter_num TEXT NOT NULL,
    exercise_title TEXT NOT NULL UNIQUE,
    exercise_content TEXT NOT NULL
);
CREATE INDEX i1 ON Exercises(chapter_num);


CREATE TABLE Chapter (
    chapter_num TEXT NOT NULL PRIMARY KEY ASC,
    chapter_title TEXT NOT NULL UNIQUE,
    FOREIGN KEY (chapter_num) REFERENCES Chapter(chapter_num) ON DELETE CASCADE
);


CREATE TABLE Tag (
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    chapter_num TEXT NOT NULL,
    exercise_title TEXT NOT NULL UNIQUE,
    tag TEXT NOT NULL,
    FOREIGN KEY (chapter_num) REFERENCES Chapter(chapter_num),
    FOREIGN KEY (exercise_title) REFERENCES Exercises(exercise_title)
);
