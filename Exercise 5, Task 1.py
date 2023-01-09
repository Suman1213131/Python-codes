def get_total_sales(sales: list):
    summary = 0.0
    for i in range(0,len(sales)):
        summary += sales[i]
    return summary

def get_average_sales(sales: list):
    total = get_total_sales(sales)
    months = 12
    average = total / months
    return average

def get_maximum_sales(sales: list):
    biggest_sale = 0.0
    index_of_biggest_sale = 0
    for i in range(0,len(sales)):
        if sales[i] > biggest_sale:
            biggest_sale = sales[i]
            index_of_biggest_sale = i

    return (index_of_biggest_sale,biggest_sale)

def get_minimum_sales(sales: list):
    biggest_sale = max(sales)
    index_of_lowest_sale = 0
    for i in range(0,len(sales)):
        if sales[i] < biggest_sale:
            biggest_sale = sales[i]
            index_of_lowest_sale = i

    return (index_of_lowest_sale,biggest_sale)

def main():
    print("Sales report")
    
    months = ["January","February","March","April","May","June","July","August","September","October","November", "December"]
    sales = []
    
    year_of_sales = input("Input the year the sales report is for> ")

    for i in range(0,len(months)):
        sale_input = input(f"Please enter the sales for month {months[i]} > £")
        while str(sale_input) == "":
            sale_input = input(f"Please enter the sales for month {months[i]} > £")
        else:
            sale_input = float(sale_input)
        sales.append(sale_input)
    
    total = get_total_sales(sales)
    average = get_average_sales(sales)
    index_max_sale,max_sale = get_maximum_sales(sales)
    index_min_sale,min_sale = get_minimum_sales(sales)
    
    print(f"\nThe total sales for {year_of_sales} are £ {total}")
    print(f"The average monthly sales for {year_of_sales} was £ {average}")
    print(f"The month number with maximum sales was {months[index_max_sale]} with £ {max_sale}")
    print(f"The month number with minimum sales was {months[index_min_sale]} with £ {min_sale}")

if __name__ == "__main__":
    main()
