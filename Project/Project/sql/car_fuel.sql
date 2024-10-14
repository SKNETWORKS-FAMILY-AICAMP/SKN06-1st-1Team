use Project;
SELECT * FROM car_fuel;

CREATE TABLE car_fuel (
    년도 INT PRIMARY KEY,          -- 연도
    전기 INT,               -- 전기
    천연가스 INT,               -- 천연가스
    하이브리드 INT,                    -- 하이브리드
    수소 INT,                  -- 수소
    기타 INT,                     -- 기타
    합계 INT                      -- 합계
);
-- 2018부터 2024년까지의 데이터 삽입
INSERT INTO car_fuel (년도, 전기, 천연가스, 하이브리드, 수소, 기타, 합계)
VALUES
(2018, 46038, 2094485, 374666, 466, 2, 2515657),
(2019, 80902, 2045369, 476478, 3436, 2, 2876185),
(2020, 124409, 2028853, 612577, 9494, 1, 2775334),
(2021, 201520, 1989786, 844563, 17076, 2, 3052947),
(2022, 347395, 1950764, 1103642, 26719, 5, 3428525),
(2023, 501485, 1879088, 1434619, 33501, 4, 3848697),
(2024, 647446, 1878220, 1878615, 36979, 2, 4441262);
