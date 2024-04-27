USE weed_detector;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

ALTER TABLE users
ADD COLUMN email VARCHAR(255),
ADD COLUMN mobile VARCHAR(20);

select * from users;









