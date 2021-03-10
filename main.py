import numpy as np
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 12, 30)

# preturi = web.DataReader('AAPL', 'yahoo', start, end)['Close']
# preturi = web.DataReader('MSFT', 'yahoo', start, end)['Close']
preturi = web.DataReader('TSLA', 'yahoo', start, end)['Close']
schimbari = preturi.pct_change()  # derapajele de la o zi la alta exprimate procentual

print(schimbari)

primul_pret = preturi[-1]

#Numarul de simulari
nr_simulari = 1000
nr_zile = 365

simulare_df = pd.DataFrame()

marja_fluctuatie = schimbari.std()
print(marja_fluctuatie)

for x in range(nr_simulari):

    # Vector cu preturile generate pe cele 365 de zile aferente simularii x
    preturile_simularii = []

    # Pretul intr-o anumita zi se genereaza ca pretul zilei anterioare, la care se adauga un 'derapaj' aleator intre 0
    # si derapajul mediu (obtinut din anul trecut).
    # Ca pret de plecare vom folosi pretul primei zi din anul trecut
    price = primul_pret * (1 + np.random.normal(0, marja_fluctuatie))

    preturile_simularii.append(price)

    for y in range(nr_zile):

        # Calculam pretul zilei y din simularea x
        price = preturile_simularii[y] * (1 + np.random.normal(0, marja_fluctuatie))
        preturile_simularii.append(price)

    # Construim dataframe-ul linie cu linie
    simulare_df[x] = preturile_simularii

fig = plt.figure()
plt.plot(simulare_df)
plt.axhline(y=int(primul_pret), color='r', linestyle='-')
plt.xlabel('Zi')
plt.ylabel('Pret')

plt.show()
