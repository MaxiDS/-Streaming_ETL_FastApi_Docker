    use pi_henry_etl;
   
   #1-Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])
SELECT title as Titulo,platform as platform, release_year as año, duration as Maxima_duracion, type_duration
FROM streaming 
WHERE platform = "hulu" and release_year= 2018 and type_duration="min"
ORDER BY duration desc
limit 1;
   
   
   #2-Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)
SELECT count(*) as Cantidad,platform, category
FROM streaming
WHERE platform = "netflix"
GROUP BY category;
   
   
   
    #3-Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')
    #Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.
    
select s.platform,count(s.platform) as cantidad 
from genre_table g 
join streaming s ON (s.idStream = g.idStream)
where g.genre ='Comedy'
group by s.platform order by cantidad DESC 
limit 1;
    
    
    #4-Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)
SELECT count(*)as apariciones,c.cast, s.platform, s.release_year
FROM cast_table c
INNER JOIN streaming s on (c.idStream=s.idStream)
WHERE s.platform="netflix" and s.release_year=2018 and c.cast != "sin dato"
GROUP BY c.cast
ORDER BY 1 DESC
LIMIT 1;



    
