select tzl."Borough"
from green_tripdata as gt
left join taxi_zone_lookup as tzl
on gt."PULocationID" = tzl."LocationID"
where lpep_pickup_datetime between '2019-09-18 00:00:00' and '2019-09-18 23:59:59'
group by tzl."Borough"
having sum(gt.total_amount) > 50000
order by sum(gt.total_amount) desc
limit 3