money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget = money_capital + salary - spend

S=1

while budget > 0:
    spend += spend * increase
    budget += salary - spend
    if budget < 0:
        break
    else:
        S += 1

print("Количество месяцев, которое можно протянуть без долгов:", S)
