-- total fans by country
SELECT  origin,
        SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY 1
ORDER BY 2 DESC;