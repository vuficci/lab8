def calculate_investment_amount(principal, interest_rate, years):
    """
    Функция для расчета итоговой суммы инвестиции с учетом простого процента.

    :param principal: начальная сумма инвестиции
    :param interest_rate: процентная ставка (в виде десятичной дроби)
    :param years: количество лет инвестирования
    :return: итоговая сумма инвестиции после указанного количества лет
    """
    amount = principal * (1 + interest_rate * years)
    return amount

def main():
    principal = float(input("Введите начальную сумму: "))
    interest_rate = float(input("Введите процентную ставку (в виде десятичной дроби): "))
    years = int(input("Введите количество лет: "))

    final_amount = calculate_investment_amount(principal, interest_rate, years)
    print(f"Через {years} лет ваша инвестиция вырастет до: {final_amount:.2f}")

if __name__ == "__main__":
    main()