lst_date = ['2018.01.02', '2018.01.03', '2018.01.04', '2018.01.05']

lst_dow = ["화", "수", "목", "금"]
lst_price = [2479.65, 2486.35, 2466.46, 2497.52]

kospi_price = [{}, {}, {}, {}]
print(kospi_price)

print(lst_dow[0])

for i in range(0, 4):
    kospi_price[i]["dow"] = lst_dow[i]
    kospi_price[i]["price"] = lst_price[i]

for i in range(0, 4):
    kospi_price[i]["date"] = lst_date[i]

for i in range(1, 4):
    kospi_price[i]["diff"] = kospi_price[i]["price"] - kospi_price[i - 1]["price"]

print(kospi_price)

print(kospi_price[3]["date"], "의 price_diff : ", kospi_price[3]["diff"])

print("최대값 : ", max(lst_price), "최소값 : ", min(lst_price))
