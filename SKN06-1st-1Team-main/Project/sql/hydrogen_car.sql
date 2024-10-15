use Project;

drop table if exists hydrogen_car;

select * from hydrogen_car;


CREATE TABLE if not exists hydrogen_car (
    증가량 VARCHAR(255),
    계 VARCHAR(255),
    년도 VARCHAR(255)
);

INSERT INTO hydrogen_car (증가량, 계, 년도) VALUES (NULL, '893', '2018');
INSERT INTO hydrogen_car (증가량, 계, 년도) VALUES ('4190', '5083', '2019');
INSERT INTO hydrogen_car (증가량, 계, 년도) VALUES ('5823', '10906', '2020');
INSERT INTO hydrogen_car (증가량, 계, 년도) VALUES ('8498', '19404', '2021');
INSERT INTO hydrogen_car (증가량, 계, 년도) VALUES ('10219', '29623', '2022');
INSERT INTO hydrogen_car (증가량, 계, 년도) VALUES ('4635', '34258', '2023');
