def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    
    
#Get input values from entry field
debt            = '2.2'
bank            = '2.1'
employed        = '2.1'
credit_score    = '2.1'
income          = '2.1'
years_employed  = '2.1'

print(str(debt) + " " + str(bank) + " " + str(employed) + " " + str(years_employed) + " " + str(credit_score) + " " + str(income))


# Check if the input is valid
is_all_numeric = (debt.isnumeric() or isfloat(debt)) and (credit_score.isnumeric() or isfloat(credit_score)) and (income.isnumeric() or isfloat(income)) and (years_employed.isnumeric() or isfloat(years_employed))

print(is_all_numeric)