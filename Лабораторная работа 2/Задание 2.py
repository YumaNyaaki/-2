from turtledemo.penrose import start

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

lack_of_budget = salary - spend


for _ in range(1, months):
    spend += spend * increase
    lack_of_budget += salary - spend

money_capital = round(lack_of_budget) * -1

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

