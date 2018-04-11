osoby = int(input('Pocet osob: '))
rozpocet = int(input('Rozpocet na osobu: '))
studenti = int(input('Pocet studentu: '))
pivo = int(input('Cena piva: '))
zastupce = input('Jmeno zodpovedne osoby: ')
sleva = 0.20

# výpočty
zlevneno = (1 - sleva) * pivo
nestudenti = osoby - studenti
cenastud = studenti * rozpocet
cenaostat = nestudenti * rozpocet
studpiva = cenastud / zlevneno
ostatpiva = cenaostat / pivo

print(zastupce, ' zaplati za ', studpiva + ostatpiva, ' piv ', cenastud + cenaostat, ' korun.')
