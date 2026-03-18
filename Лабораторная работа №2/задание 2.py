salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

podyushka = 0 # финансовая подушка безопасности

for i in range(months):
    podyushka += spend-salary
    spend *= (1 + increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(podyushka))
