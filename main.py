from prob_theory import (
	strd,
	divide,
	distr_F,
	bern_analysis,
	hypergeom_distr_calc,
	frac_hypergeom_distr_calc,
)


bern_analysis(
	max_k=5,
	n=5,
	p=0.1,
)
divide()

distr_F(
	[0, 1, 2, 3],
	[
		strd(0.123),
		strd(0.43),
		strd(0.369),
		strd(0.0769),
	],
)
divide()

hypergeom_distr_calc(15, 7, 3)
divide()

frac_hypergeom_distr_calc(15, 7, 3)