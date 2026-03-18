money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

money_capital -= spend
money_capital += salary
n = 1 #количество месяцев
while (money_capital+salary) > (spend*(1+increase)):
    spend *= (1+increase)
    money_capital -= spend
    money_capital += salary
    n+=1

print("Количество месяцев, которое можно протянуть без долгов:", n)
