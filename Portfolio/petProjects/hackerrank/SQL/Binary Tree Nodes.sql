-- https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
select
bst.n
,
case
    when bst.p is null
    then 'Root'
    when bst.n in (select distinct p from bst)
    then 'Inner'
    else 'Leaf'
end

from
bst

order by
bst.n