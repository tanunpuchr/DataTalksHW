select cast(lpep_pickup_datetime as date)
from green_tripdata
order by trip_distance desc
limit 1;