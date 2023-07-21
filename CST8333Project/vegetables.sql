-- This sql script was generated by an online csv to sql converter
-- found here https://tableconvert.com/csv-to-sql
--

-- create vegetable table with the dataset header as columns
DROP TABLE IF EXISTS vegetable;
CREATE TABLE vegetable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ref_date TEXT,
    geo TEXT,
    dguid TEXT,
    type_of_product TEXT,
    type_of_storage TEXT,
    uom TEXT,
    uom_id TEXT,
    scalar_factor TEXT,
    scalar_id TEXT,
    vector TEXT,
    coordinate TEXT,
    value TEXT,
    status TEXT,
    symbol TEXT,
    terminated TEXT,
    decimals TEXT
);

-- Insert 100 records/rows of vegetables retrieved from the dataset file "32100260.csv
INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Canada', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722342', '1.1.1', 1041, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Canada', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722350', '1.2.1', 26341, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Canada', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722358', '1.3.1', 29526, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Canada', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722366', '1.4.1', 1955, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Maritime provinces', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722343', '2.1.1', 725, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Maritime provinces', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722351', '2.2.1', 147, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Maritime provinces', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722359', '2.3.1', 2949, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Maritime provinces', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722367', '2.4.1', 508, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Quebec', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722344', '3.1.1', 95, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Quebec', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722352', '3.2.1', 2631, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Quebec', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722360', '3.3.1', 3271, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Quebec', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722368', '3.4.1', 618, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Ontario', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722345', '4.1.1', 106, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Ontario', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722353', '4.2.1', 22260, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Ontario', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722361', '4.3.1', 21713, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Ontario', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722369', '4.4.1', 112, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Manitoba', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722346', '5.1.1', 0, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Manitoba', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722354', '5.2.1', 81, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Manitoba', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722362', '5.3.1', 105, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Manitoba', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722370', '5.4.1', 54, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Saskatchewan', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722347', '6.1.1', 2, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Saskatchewan', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722355', '6.2.1', 66, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Saskatchewan', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722363', '6.3.1', 22, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Saskatchewan', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722371', '6.4.1', 28, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Alberta', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722348', '7.1.1', 94, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Alberta', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722356', '7.2.1', 102, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Alberta', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722364', '7.3.1', 1007, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'Alberta', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722372', '7.4.1', 196, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'British Columbia', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722349', '8.1.1', 19, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'British Columbia', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722357', '8.2.1', 1055, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'British Columbia', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722365', '8.3.1', 459, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-01', 'British Columbia', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722373', '8.4.1', 437, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Canada', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722342', '1.1.1', 839, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Canada', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722350', '1.2.1', 14238, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Canada', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722358', '1.3.1', 21025, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Canada', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722366', '1.4.1', 1009, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Maritime provinces', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722343', '2.1.1', 604, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Maritime provinces', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722351', '2.2.1', 151, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Maritime provinces', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722359', '2.3.1', 1520, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Maritime provinces', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722367', '2.4.1', 354, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Quebec', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722344', '3.1.1', 56, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Quebec', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722352', '3.2.1', 1380, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Quebec', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722360', '3.3.1', 2642, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Quebec', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722368', '3.4.1', 275, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Ontario', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722345', '4.1.1', 89, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Ontario', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722353', '4.2.1', 11619, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Ontario', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722361', '4.3.1', 15966, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Ontario', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722369', '4.4.1', 85, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Manitoba', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722346', '5.1.1', 0, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Manitoba', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722354', '5.2.1', 159, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Manitoba', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722362', '5.3.1', 91, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Manitoba', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722370', '5.4.1', 64, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Saskatchewan', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722347', '6.1.1', 2, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Saskatchewan', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722355', '6.2.1', 124, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Saskatchewan', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722363', '6.3.1', 36, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Saskatchewan', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722371', '6.4.1', 20, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Alberta', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722348', '7.1.1', 72, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Alberta', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722356', '7.2.1', 276, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Alberta', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722364', '7.3.1', 502, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'Alberta', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722372', '7.4.1', 68, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'British Columbia', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722349', '8.1.1', 16, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'British Columbia', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722357', '8.2.1', 528, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'British Columbia', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722365', '8.3.1', 269, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-02', 'British Columbia', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722373', '8.4.1', 143, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Canada', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722342', '1.1.1', 680, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Canada', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722350', '1.2.1', 9894, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Canada', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722358', '1.3.1', 14966, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Canada', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722366', '1.4.1', 645, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Maritime provinces', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722343', '2.1.1', 503, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Maritime provinces', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722351', '2.2.1', 138, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Maritime provinces', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722359', '2.3.1', 192, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Maritime provinces', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722367', '2.4.1', 106, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Quebec', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722344', '3.1.1', 46, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Quebec', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722352', '3.2.1', 874, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Quebec', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722360', '3.3.1', 997, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Quebec', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722368', '3.4.1', 271, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Ontario', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722345', '4.1.1', 62, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Ontario', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722353', '4.2.1', 7852, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Ontario', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722361', '4.3.1', 13206, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Ontario', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722369', '4.4.1', 76, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Manitoba', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722346', '5.1.1', 0, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Manitoba', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722354', '5.2.1', 113, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Manitoba', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722362', '5.3.1', 181, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Manitoba', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722370', '5.4.1', 32, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Saskatchewan', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722347', '6.1.1', 1, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Saskatchewan', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722355', '6.2.1', 125, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Saskatchewan', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722363', '6.3.1', 33, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Saskatchewan', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722371', '6.4.1', 34, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Alberta', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722348', '7.1.1', 56, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Alberta', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722356', '7.2.1', 286, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Alberta', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722364', '7.3.1', 123, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'Alberta', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722372', '7.4.1', 30, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'British Columbia', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722349', '8.1.1', 12, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'British Columbia', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722357', '8.2.1', 506, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'British Columbia', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722365', '8.3.1', 234, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-03', 'British Columbia', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722373', '8.4.1', 96, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-04', 'Canada', '', 'Potatoes', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722342', '1.1.1', 559, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-04', 'Canada', '', 'Onions', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722350', '1.2.1', 5034, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-04', 'Canada', '', 'Carrots', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722358', '1.3.1', 6525, '', '', '', 0);

INSERT INTO vegetable (ref_date, geo, dguid, type_of_product, type_of_storage, uom, uom_id, scalar_factor, scalar_id, vector, coordinate, value, status, symbol, terminated, decimals)
VALUES ('1970-04', 'Canada', '', 'Cabbage', 'Cold and common storage', 'Tonnes', '288', 'units ', '0', 'v722366', '1.4.1', 474, '', '', '', 0);



