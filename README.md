# Probability theory / Теория вероятностей
[en] Python module with functions to calculate base probability theory \
[ru] Python модуль с функциями для вычисления базовой теории вероятностей 

---

**Биноминальный коэффициент**
```math
\mathrm{C}_{n}^{k} = \frac{n!}{k! \left( n \cdot k \right)!}
```

**Функция распределения**
```math
F\left( x \right) = \sum_{x_{i} \le x}^{}p_{i}
```

---

**Распределение Пуассона**
```math
P\left( k \right) = \frac{\left( \lambda t \right)^k}{m!}e^{- \lambda t}, \quad \lambda = n \cdot p_{n}=const
```

---

**Формула Бернулли**
```math
P\left( k \right) = \mathrm{C}_{n}^{k} \cdot p^{k} \cdot q^{n-k}
```

**Математическое ожидание**
```math
M\left( \xi \right) = \sum_{i=1}^{n}x_{i} \cdot p_{i}
```

**Дисперсия**
```math
D\left( x \right) = M\left[ x \ - \ M\left( x \right) \right]^{2}
```

---

**Биноминальное распределение**
```math
P\left( k \right) = \mathrm{C}_{n}^{k} \cdot p^{k} \cdot q^{n-k}
```

**Мат ожидание биноминального распределения**
```math
M\left( \xi \right) = n \cdot p
```

**Дисперсия биноминального распределения**
```math
D\left( \xi \right) = n \cdot p \cdot q
```

---

**Геометрическое распределение**
```math
P\left( k \right) = q^{k-1} \cdot p
```

```math
x_{k} = 1, \ 2, \ 3, \ ..., \ n
```

**Мат ожидание геометрического распределения**
```math
M\left( x \right) = \frac{1}{p}
```

**Дисперсия геометрического распределения**
```math
D\left( x \right) = \frac{q}{p^{2}}
```

---

**Гипергеометрическое распределение**
```math
P\left( k \right) = \frac{\mathrm{C}_{M}^{k} \cdot \mathrm{C}_{N-M}^{n-k}}{\mathrm{C}_{N}^{k}}
```

```math
n,\ N, \ M \in \mathbb{N} \quad \left( \gt 0, \ int \right)
```

```math
n, \ M \le N
```

```math
x_{n} = m \quad \left( m=0, 1, 2, \ ... \ min\! \left( n, \ M \right) \right)
```

**Мат ожидание гипергеометрического распределения**
```math
M\left( x \right) = n \cdot \frac{M}{N}
```

**Дисперсия гипергеометрического распределения**
```math
D\left( x \right) = n \frac{M}{N-1} \left( 1-\frac{M}{N} \right) \left( 1-\frac{n}{N} \right)
```
