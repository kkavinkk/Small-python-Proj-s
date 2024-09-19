items = {
    "Apple" : 1.00,
    "Orange" : 1.15,
    "Banana" : 0.99,
    "Pineapple" : 4.98
}

def gather_items(a,o,b,p):

    apt = (a) * items["Apple"]
    ort = (o) * items["Orange"]
    bat = (b) * items["Banana"]
    pit = (p) * items["Pineapple"]

    total = apt + ort + bat + pit
    total = total * 1.05
    return (a, apt), (o, ort), (b, bat), (p, pit), round(total, 2)

def main():
    
    apple = int(input("How many apples?:"))
    orange = int(input("How many oranges?:"))
    banana = int(input("How many bananas?:"))
    pineapple = int(input("How many pineapples?:"))
    
    (a_qty, a_cost), (o_qty, o_cost), (b_qty, b_cost), (p_qty, p_cost), total = gather_items(apple, orange, banana, pineapple)

    # Print each item in the specified format
    print(f"{a_qty:<5} Apple      {a_cost:.2f}")
    print(f"{o_qty:<5} Orange     {o_cost:.2f}")
    print(f"{b_qty:<5} Banana     {b_cost:.2f}")
    print(f"{p_qty:<5} Pineapple  {p_cost:.2f}")
    
    # Print the separator line
    print('—' * 30)
    
    # Calculate the total quantity
    total_quantity = a_qty + o_qty + b_qty + p_qty
    # Print the total line
    print(f"{total_quantity:<5} {total:.2f}(inlcuding tax)")

if __name__ =="__main__":
    main()