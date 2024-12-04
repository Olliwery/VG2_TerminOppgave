CREATE DATABASE Termin2VG2

USE Termin2VG2

CREATE TABLE Brukere {
    id int NOT NULL AUTO_INCREMENT,
    navn varchar(50) NOT NULL,
    email varchar(100) NOT NULL,
    passord varchar(255) NOT NULL,
    PRIMARY KEY (id)
};

CREATE TABLE snake {
    id int NOT NULL AUTO_INCREMENT,
    score
}

CREATE TABLE kobling {
    id int NOT NULL AUTO_INCREMENT,
    BrukereId int,
    SnakeId int,
    PRIMARY KEY,
    FOREIGN KEY (BrukereId) REFERENCES Brukere(id)
    FOREIGN KEY (SnakeId) REFERENCES Snake(id)

}

INSERT INTO Brukere (navn, email, passord) VALUES ("Bob", "Bob@gmail.com", "Bob123")
