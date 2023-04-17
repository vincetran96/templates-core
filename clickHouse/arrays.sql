with
    t as (
        select 
        [([1,1,1],['a1','a2','a3']), ([2,2],['b1','b2'])] as c,
        [(['u1','u2','u3'],), (['w1','w2'],)] as d
    )

-- select arrayMap(x,y,z -> arrayZip(x,y,z), c.1, c.2, d.1)  
-- from t

select arrayMap(x,y -> arrayZip(x.1, x.2, y.1), c, d)
from t
