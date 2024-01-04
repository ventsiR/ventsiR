-- https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true
with numsList as (
    --base query
    (
        select
        2 as nums
    )
    union all
    --iterative query
    (
        select nums + 1

        from numsList

        where 
        nums < 1000
    )
)
select
--concatenate
string_agg(convert(varchar(999), nums), '&') as ans

from
numsList

where
nums not in
--list of non-primes
(
    select
    a.nums
    from
    numsList a
    inner join
    (select * from numsList where nums < sqrt(1000)) b
    on
    (
    a.nums%b.nums = 0
    and
    a.nums != b.nums
    )
)
option(maxrecursion 1000)