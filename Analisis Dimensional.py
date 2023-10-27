# JOSE JAVIER TORRES VANSTRAHLEN - SCRIPT PARA CALCULO DE ANALISIS DIMENCIONAL


from sympy import symbols, Eq, solve, sqrt

a, b, c, d, e, h, P, rho, mu = symbols('a b c d e h P rho mu')

eq1 = Eq(-3 * a + e, -b + c - 3 * d)
eq2 = Eq(-e, b + d)
eq3 = Eq(-2 * b, a + e)

sol = solve((eq1, eq2, eq3), (a, b, c, d, e))

h_expr = sqrt(P / rho) * sqrt(mu**2 / (P**2 * rho))

final_expr = h_expr.subs(sol)


print("Resultado:", final_expr)
