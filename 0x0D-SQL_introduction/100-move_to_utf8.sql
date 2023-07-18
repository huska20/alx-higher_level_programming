-- Convert hbtn_0c_0 database to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the first_table table to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Modify the name field/column in the first_table table to utf8mb4 character set and utf8mb4_unicode_ci collation
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
