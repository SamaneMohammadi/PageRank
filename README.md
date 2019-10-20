# PageRank

In view of the huge dimensions of the Google matrix, it is nontrivial to compute
the matrix-vector product y = Az, where A = αP + (1 − α) 1 eeT . Recall that P n
was constructed from the actual link matrix Q as P = Q + 1 edT ,
n
where the row vector d has an element 1 in all those positions that correspond to Web pages with no outlinks (see (12.5)). This means that to form P, we insert a large number of full vectors into Q, each of the same dimension as the total number of Web pages. Consequently, we cannot afford to store P explicitly. Let us look at the multiplication y = Az in more detail:
y=α Q+nedT z+ n e(eTz)=αQz+βne
where:
β = αdT z + (1 − α)eT z.
We do not need to compute β from this equation. Instead we can use in
       combination with:
1 = eT (αQz) + βeT 1 e = eT (αQz) + β.
Thus, we have β = 1−∥αQz∥1. An extra bonus is that we do not use the vector d at all, i.e., we need not know which pages lack outlinks.
