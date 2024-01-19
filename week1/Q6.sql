select tzl2."Zone" as "DOZone"
from green_tripdata as gt
inner join taxi_zone_lookup as tzl
on gt."PULocationID" = tzl."LocationID"
and tzl."Zone" = 'Astoria'
left join taxi_zone_lookup as tzl2
on gt."DOLocationID" = tzl2."LocationID"
where gt.lpep_pickup_datetime between '2019-09-01 00:00:00' and '2019-09-30 23:59:59'
order by gt.tip_amount desc
limit 1;