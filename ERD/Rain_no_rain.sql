CREATE TABLE "Rainfall" (
    "Date" Date   NOT NULL,
    "TempAvgºF" float   NOT NULL,
    "TempMinºF" float   NOT NULL,
    "TempMaxºF" float   NOT NULL,
    "RainTotal" float   NOT NULL,
    "WindSpeed" float   NOT NULL,
    "Pressure" float   NOT NULL,
    "Raining" boolean   NOT NULL,
    CONSTRAINT "pk_Rainfall" PRIMARY KEY (
        "Date"
     )
);

CREATE TABLE "Humidity" (
    "Date" Date   NOT NULL,
    "HumidityMax" float   NOT NULL,
    "HumidityAvg" float   NOT NULL,
    "HumidityMin" float   NOT NULL,
    CONSTRAINT "pk_Humidity" PRIMARY KEY (
        "Date"
     )
);

ALTER TABLE "Humidity" ADD CONSTRAINT "fk_Humidity_Date" FOREIGN KEY("Date")
REFERENCES "Rainfall" ("Date");