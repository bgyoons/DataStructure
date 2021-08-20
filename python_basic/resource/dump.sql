BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY,     username text, email test, phone text, website text, regdate);
INSERT INTO "users" VALUES(1,'Kim','Kim@naver.com','010-2222-2222','kim.com','2021-08-20 17:32:37');
INSERT INTO "users" VALUES(2,'Park','park@mgail.com','010-1341-3214','park.ac.kr','2021-08-20 17:32:37');
INSERT INTO "users" VALUES(3,'Lee','Lee@nav.com','010-3154-3155','Lee.com','2021-08-20 17:32:37');
INSERT INTO "users" VALUES(4,'Cho','Cho@dav.com','010-3999-3155','Cho.com','2021-08-20 17:32:37');
INSERT INTO "users" VALUES(5,'PPP','PPP@qav.com','010-7774-1155','PPP.com','2021-08-20 17:32:37');
COMMIT;
