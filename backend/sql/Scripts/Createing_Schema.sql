CREATE SCHEMA IF NOT EXISTS marts;


-- Queries for inspecting data (you can disregard this part in terms of execution)
SELECT * FROM youtube_data.enhetstyp.tabelldata t;
SELECT * FROM youtube_data.geografi.diagramdata d;
SELECT * FROM youtube_data.geografi.totalt t;
SELECT * FROM youtube_data.operativsystem.diagramdata d;
SELECT * FROM youtube_data.operativsystem.totalt t;

CREATE TABLE marts.mart_device AS
SELECT
    Visningar AS Views,
    Enhetstyp AS Device_Type
FROM youtube_data.enhetstyp.tabelldata t;


CREATE TABLE marts.mart_geografi AS
SELECT
    geo1.Geografi AS viewer_location,
    geo1.Visningar AS views,
    STRFTIME('%Y-%m-%d', geo1.Datum) AS date_view
FROM youtube_data.geografi.diagramdata AS geo1  
LEFT JOIN youtube_data.geografi.totalt AS geo2  
ON geo1.Datum = geo2.Datum;


CREATE TABLE marts.operation_systems AS
SELECT
    op1.Operativsystem AS Operating_System,  
    op1.Visningar AS Views,                  
    STRFTIME('%Y-%m-%d', op1.Datum) AS date_view   
FROM youtube_data.operativsystem.diagramdata AS op1  
LEFT JOIN youtube_data.operativsystem.totalt AS op2 
ON op1.Datum = op2.Datum;


CREATE TABLE marts.kpi_dashboard AS
SELECT
    COUNT(DISTINCT Videotitel) AS total_videos,
    SUM(Visningar) AS total_views,
    AVG(Visningar) AS average_views_per_video,
    MAX(Visningar) AS peak_views
FROM youtube_data.innehall.tabelldata;
