select id
from (
    select *,
           lag(recordDate) over (order by recordDate) as prev_date,
           lag(temperature) over (order by recordDate) as prev_temp
    from Weather
) t
where datediff(recordDate, prev_date) = 1 and temperature > prev_temp;