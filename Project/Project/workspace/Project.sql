# 1. DataBase 생성: Project

create database Project;
use Project;

####################################################################################

# 2. 테이블 생성: vehicle_registration

-- 1. vehicle_registration
CREATE TABLE vehicle_registration (
    증가량 INT,        -- Increase in the number of vehicles
    계 INT NOT NULL,  -- Total number of vehicles
    년도 YEAR NOT NULL PRIMARY KEY  -- Year (Primary Key)
);

-- 2. hydrogen_station

CREATE TABLE IF NOT EXISTS hydrogen_station (
    번호 INT NOT NULL,
    구축연도 INT NOT NULL,
    충전소명 VARCHAR(255) NOT NULL,
    지역_대분류 VARCHAR(255) NOT NULL,
    주소 VARCHAR(255) NOT NULL,
    용도 VARCHAR(50) NOT NULL,
    위도 DOUBLE NOT NULL,
    경도 DOUBLE NOT NULL,
    PRIMARY KEY (번호)
) DEFAULT CHARSET=utf8mb4;


#################################################################################################

-- 테이블 구조 표시
desc vehicle_registration;
SHOW TABLES;

-- 자료 확인
select *from test;
select *from vihicle_registration;
select *from hydrogen_station;

# Port 확인
SHOW VARIABLES LIKE 'port';
