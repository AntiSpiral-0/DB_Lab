SELECT * FROM youtube_data.innehall.tabelldata t offset 1;
SELECT * FROM youtube_data.innehall.totalt t offset 1;
SELECT * FROM youtube_data.geo.totalt t offset 1;

SELECT 
    COUNT(*) AS total_rows,         
    SUM(Visningar) AS total_visningar  
FROM youtube_data.innehall.totalt t ;  


SELECT 
    COUNT(*) AS total_rows,         
    SUM(Visningar) AS total_visningar  
FROM youtube_data.innehall.tabelldata t;  



WITH 
    date_table AS (SELECT * FROM innehall.tabelldata OFFSET 1),
    date_total AS (SELECT * FROM innehall.totalt OFFSET 1)
SELECT 
    STRFTIME('%Y-%m-%d', tot."Datum") AS formatted_date, 
    tot.visningar AS total_visningar,   
    tab."visningstid (timmar)",        
    tab.Videotitel AS video_title      
FROM date_table tab
LEFT JOIN date_total tot
ON tot.visningar = tab.visningar;   


WITH 
    date_table AS (SELECT * FROM geografi.tabelldata OFFSET 1),
    date_total AS (SELECT * FROM geografi.totalt OFFSET 1)
SELECT 
    STRFTIME('%Y-%m-%d', tot."Datum") AS formatted_date, 
    tot.visningar AS total_visningar,   
    tab."visningstid (timmar)",           
FROM date_table tab
LEFT JOIN date_total tot
ON tot.visningar = tab.visningar;   


