set term pngcairo
set output "lattice_gas.png"

f(x, L) = 4/(4+(L**2+L-4)*exp(-x))

set xrange [0:10]
set yrange [0:1]

p f(x,3) t "L=3"\
, f(x,5) t "L=5"\
, f(x,10) t "L=10"\

