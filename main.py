from prob_theory import (
	strd, divide, big_divide,
	C, distr_F,
	pois_distr_calc,
	bern_analysis,
	geom_distr_calc,
	hypergeom_distr_calc,
	frac_hypergeom_distr_calc,
)


distr_F(
	[0, 1, 2, 3],
	[
		strd(0.123),
		strd(0.43),
		strd(0.369),
		strd(0.0769),
	],
)

pois_distr_calc(2, 2.5)

bern_analysis(5, 5, 0.1)

geom_distr_calc(0.4, 4)

hypergeom_distr_calc(15, 7, 3)

frac_hypergeom_distr_calc(15, 7, 3)