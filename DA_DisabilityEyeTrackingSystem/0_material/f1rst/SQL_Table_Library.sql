CREATE TABLE 5AHET_Ibesich_Machal_Braunstingl_Bücher (
    BookId INT PRIMARY KEY,
    title text,
    genre text,
    releaseYear timestamp,
    FOREIGN KEY (AuthorId) REFERENCES 5AHET_Ibesich_Machal_Braunstingl_Autoren(AuthorId) 
);

CREATE TABLE 5AHET_Ibesich_Machal_Braunstingl_Autoren (
    AuthorId INT PRIMARY KEY,
    name text,
    nationality text
);

CREATE TABLE 5AHET_Ibesich_Machal_Braunstingl_Mitglieder (
    MemberId INT PRIMARY KEY,
    name text,
    address text,
    entryDate timestamp
);

CREATE TABLE 5AHET_Ibesich_Machal_Braunstingl_Ausleihen (
    LendId INT PRIMARY KEY,
    FOREIGN KEY (MemberId) REFERENCES 5AHET_Ibesich_Machal_Braunstingl_Mitglieder(MemberId),
    lendDate timestamp,
    returnDate timestamp
);

CREATE TABLE 5AHET_Ibesich_Machal_Braunstingl_AusleihPaket (
    FOREIGN KEY (LendId) REFERENCES 5AHET_Ibesich_Machal_Braunstingl_Ausleihen(LendId),
    FOREIGN KEY (BookId) REFERENCES 5AHET_Ibesich_Machal_Braunstingl_Bücher(BookId)
)