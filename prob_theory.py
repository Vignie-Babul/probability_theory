import decimal
from math import e, factorial


def strd(n: int | float) -> decimal.Decimal:
	"""Правильная конвертация числа в decimal.Decimal"""
	return decimal.Decimal(str(n))

def divide(char: str = '-', length: int = 30) -> None:
	"""Разделитель с символом char и длиной length"""
	print(char * length)

def big_divide(char: str = '=', length: int = 50) -> None:
	"""Большой разделитель по умолчанию с символом '=' и длиной 50"""
	divide(char, length)


# ---------- общее

def C(k: int, n: int) -> decimal.Decimal:
	"""Биномиальный коэффициент"""

	n_fact = strd(factorial(n))
	k_fact = strd(factorial(k))
	nk_fact = strd(factorial(n-k))
	
	c = n_fact / (k_fact * nk_fact)
	return c

def distr_F(xi: tuple[int], pi: tuple[decimal.Decimal]) -> None:
	"""Функция распределения"""

	is_start = True
	sep = ' ' * 3

	if xi[0] == 0:
		pi = (0, *pi)

	p_sum = 0
	cur_p = 0
	for x, p in zip(xi, pi):
		p_sum += p

		if is_start:
			print(f'{f"x <= 0":>11}{sep}F(x) = 0')
			is_start = False
		else:
			if cur_p == 0:
				print(f'{f"{x-1} < x <= {x}":>11}{sep}F(x) = {p}')
			else:
				print(f'{f"{x-1} < x <= {x}":>11}{sep}F(x) = {cur_p} + {p} = {p_sum}')

		cur_p += p

	p = pi[-1]
	p_sum += p
	print(f'{f"x >  {x}":>11}{sep}F(x) = {cur_p} + {p} = {p_sum}\n')


# ---------- распределение Пуассона

def pois_distr(k: int, l: int, t: int = 1) -> decimal.Decimal:
	"""Распределение Пуассона"""

	k_ = strd(k)
	l_ = strd(l)
	t_ = strd(t)

	ltk = (l_*t_) ** k_
	k_fact = strd(factorial(k))
	ltk_k_fact = ltk / k_fact
	elt = strd(e) ** (-l_ * t_)
	result = ltk_k_fact * elt

	lt_ = f'{l}*{t}'
	first_row = f'({lt_})**{k} / {k}! * e**-{lt_}'
	second_row = f'{ltk} / {k_fact} * {elt}'
	print(f'P({k}) = {first_row} =\n= {second_row} =\n= {result}\n')

	return result

def pois_MD(l: int) -> decimal.Decimal:
	return strd(l)

def pois_distr_calc(max_k: int, l: int, t: int = 1, min_k: int = 0) -> None:
	"""Вычисление распределения Пуассона"""

	for k in range(min_k, max_k + 1):
		pois_distr(k, l, t)

	print(f'M(x) = D(x) =', pois_MD(l))
	divide()


# ---------- формула Бернулли

def bern_form(n: int, k: int, p: float) -> decimal.Decimal:
	"""Закон распределения СВ по формуле Бернулли"""

	q = 1 - p
	k_ = strd(k)
	n_fact = strd(factorial(n))
	k_fact = strd(factorial(k))
	nk_fact = strd(factorial(n-k))

	C = n_fact / (k_fact * nk_fact)
	pk = strd(p) ** k_
	qnk = strd(q) ** (strd(n)-k_)
	result = C * pk * qnk

	С_ = f'C({k}, {n})'
	pk_ = f'{p}**{k}'
	qnk_ = f'{q}**({n-k})'

	print(f'P({k}) = {С_} * {pk_} * {qnk_} =')
	print(f'= {result}\n')

	return result

def bern_form_calc(n: int, max_k: int, p: float, min_k: int = 0) -> tuple[decimal.Decimal]:
	"""Вычисление формулы Бернулли от min_k до max_k"""

	Pi = [bern_form(n=n, k=k, p=p) for k in range(min_k, max_k + 1)]

	divide()
	print(f'P sum = {sum(Pi)}\n')

	return Pi

def bern_M(xi: tuple[int], pi: tuple[decimal.Decimal]) -> decimal.Decimal:
	"""Математическое ожидание (Бернулли)
	xi - случайная величина (СВ)
	pi - вероятность СВ
	"""

	result = 0
	for x, p in zip(xi, pi):
		result += strd(x) * strd(p)
	return result

def bern_D(xi: tuple[int], pi: tuple[decimal.Decimal], bern_M_: decimal.Decimal) -> decimal.Decimal:
	"""Дисперсия случайной величины (Бернулли)
	xi      - случайная величина (СВ)
	pi      - вероятность СВ
	bern_M_ - мат ожидание (Бернулли)
	"""

	result = 0
	for x, p in zip(xi, pi):
		result += ((strd(x)-strd(bern_M_)) ** strd(2)) * strd(p)
	return result

def bern_MD_calc(xi: tuple[int], pi: tuple[decimal.Decimal]) -> None:
	"""Мат ожидание и дисперсия (Бернулли)"""

	bern_M_ = bern_M(xi, pi)
	bern_D_ = bern_D(xi, pi, bern_M_)

	print(f'M(x) = {bern_M_}')
	print(f'D(x) = {bern_D_}\n')

def bern_analysis(n: int, max_k: int, p: int) -> None:
	"""Закон распределения СВ (Бернулли),
	мат ожидание (Бернулли), дисперсия (Бернулли),
	функция распределения
	"""

	xi = range(max_k + 1)
	pi = bern_form_calc(n, max_k, p)

	bern_MD_calc(xi, pi)
	distr_F(xi, pi)


# ---------- геометрическое распределение

def geom_distr(p: float, k: int) -> decimal.Decimal:
	"""Геометрическое распределение"""

	p_ = strd(p)
	q = 1 - p
	q_ = strd(1) - p_
	qk = q_ ** strd(k-1)
	result = qk * p_

	print(f'P({k}) = {q}**{k-1} * {p} =\n{result}\n')
	return result

def geom_distr_M(p: float) -> decimal.Decimal:
	"""Мат ожидание геометрического распределения"""
	return strd(1) / strd(p)

def geom_distr_D(p: float) -> decimal.Decimal:
	"""Дисперсия геометрического распределения"""

	p_ = strd(p)
	q_ = 1 - p_
	result = q_ / (p_**2)

	return result.quantize(strd(1)) # убирает экспоненту

def geom_distr_calc(p: float, max_k: int) -> None:
	"""Вычисление геометрического распределения от 1 до max_k"""

	for k in range(1, max_k + 1):
		geom_distr(p, k)

	divide()
	print(f'M(x) =', geom_distr_M(p))
	print(f'D(x) =', geom_distr_D(p))


# ---------- гипергеометрическое распределение

def hypergeom_distr(N: int, M: int, n: int, k: int) -> decimal.Decimal:
	"""Гипергеометрическое распределение"""

	first = C(k, M)
	second = C(n-k, N-M)
	third = C(n, N)
	result = (first*second) / third

	print(f'P({k}) = {result}')
	return result

def hypergeom_distr_M(N: int, M: int, n: int) -> decimal.Decimal:
	"""Мат ожидание гипергеометрического распределения"""
	return strd(n) * strd(M)/strd(N)

def hypergeom_distr_D(N: int, M: int, n: int) -> decimal.Decimal:
	"""Дисперсия гипергеометрического распределения"""

	N_ = strd(N)
	M_ = strd(M)
	n_ = strd(n)

	first = n_ * M_/(N_-1)
	second = 1 - M_/N_
	third = 1 - n_/N_

	return first * second * third

def hypergeom_distr_calc(N: int, M: int, n: int) -> None:
	"""Вычисление гипергеометрического распределения от 1 до max_k"""

	max_k = min(n, M)
	for k in range(max_k + 1):
		hypergeom_distr(N, M, n, k)

	divide()
	print('M(x) =', hypergeom_distr_M(N, M, n))
	print('D(x) =', hypergeom_distr_D(N, M, n))


# ----- гипергеометрическое распределение в дробях

def frac_hypergeom_distr(N: int, M: int, n: int, k: int) -> decimal.Decimal:
	"""Гипергеометрическое распределение в дробях"""

	first = C(k, M)
	second = C(n-k, N-M)
	third = C(n, N)

	top_frac = first * second
	result = (first, second, third)

	print(f'P({k}) = {first}*{second} / {third} =\n{top_frac} / {third}\n')
	return result

def frac_hypergeom_distr_M(N: int, M: int, n: int) -> decimal.Decimal:
	"""Мат ожидание гипергеометрического распределения в дробях"""
	return f'{n} * {M}/{N}'

def frac_hypergeom_distr_D(N: int, M: int, n: int) -> decimal.Decimal:
	"""Дисперсия гипергеометрического распределения в дробях"""

	N_ = strd(N)
	M_ = strd(M)
	n_ = strd(n)

	first = n_ * M_/(N_-1)
	second = 1 - M_/N_
	third = 1 - n_/N_

	return f'{first} * {second} * {third}'

def frac_hypergeom_distr_calc(N: int, M: int, n: int) -> None:
	"""Вычисление гипергеометрического распределения от 1 до max_k в дробях"""

	max_k = min(n, M)
	for k in range(max_k + 1):
		frac_hypergeom_distr(N, M, n, k)

	divide()
	print('M(x) =', frac_hypergeom_distr_M(N, M, n))
	print('D(x) =', frac_hypergeom_distr_D(N, M, n))