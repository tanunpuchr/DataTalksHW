select count(*) from green_tripdata
where lpep_pickup_datetime >= '2019-09-18 00:00:00'
and lpep_dropoff_datetime <= '2019-09-18 23:59:59';