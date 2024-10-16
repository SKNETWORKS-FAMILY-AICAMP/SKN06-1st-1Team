use Project;

drop table if exists hydrogen_registration_year;

CREATE TABLE if not exists `hydrogen_registration_year` (
    `연도` VARCHAR(255),
    `등록 차량 수` FLOAT,
    `전년 대비 증가량` FLOAT
);
INSERT INTO `hydrogen_registration_year` (`연도`, `등록 차량 수`, `전년 대비 증가량`) VALUES ('2018년', 893, 893);
INSERT INTO `hydrogen_registration_year` (`연도`, `등록 차량 수`, `전년 대비 증가량`) VALUES ('2019년', 5083, 4190);
INSERT INTO `hydrogen_registration_year` (`연도`, `등록 차량 수`, `전년 대비 증가량`) VALUES ('2020년', 10906, 5823);
INSERT INTO `hydrogen_registration_year` (`연도`, `등록 차량 수`, `전년 대비 증가량`) VALUES ('2021년', 19404, 8498);
INSERT INTO `hydrogen_registration_year` (`연도`, `등록 차량 수`, `전년 대비 증가량`) VALUES ('2022년', 29623, 10219);
INSERT INTO `hydrogen_registration_year` (`연도`, `등록 차량 수`, `전년 대비 증가량`) VALUES ('2023년', 34258, 4635);
INSERT INTO `hydrogen_registration_year` (`연도`, `등록 차량 수`, `전년 대비 증가량`) VALUES ('2024년 8월', 36787, 2529);
