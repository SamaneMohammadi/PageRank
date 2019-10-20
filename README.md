# PageRank
The power method for Ar = λr
for k = 1, 2, . . . until convergence q(k) = Ar(k−1)

r(k) = q(k)/∥ q(k) ∥

The purpose of normalizing the vector (making it have 1-norm equal to 1) is to avoid having the vector become either very large or very small and thus unrep- resentable in the floating point system. We will see later that normalization is not necessary in the pagerank computation. In this context there is no need to compute an eigenvalue approximation, as the sought eigenvalue is known to be equal to one.

The convergence of the power method depends on the distribution of eigen- values. To make the presentation simpler, we assume that A is diagonalizable, i.e., there exists a nonsingular matrix T of eigenvectors,
T−1AT = diag(λ1,...,λn). The eigenvalues λi are ordered 1 = λ1 > |λ2| ≥ ··· ≥ |λn|. 
Expand the initial approximation r(0) in terms of the eigenvectors,
r(0) =c1t1 +c2t2 +···+cntn,
where c1 ̸= 0 is assumed30 and r = t1 is the sought eigenvector.
Then we have
Akr(0) = c1Akt1 + c2Akt2 + · · · + cnAktn =c1λk1t1 +c2λk2t2 +···+cnλkntn
