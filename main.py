def main():
    ##################################################
    # Comlete your code here
    ##################################################
    val1 = int(input('input a value '))
    val2 = int(input('input a value '))
    val3 = int(input('input a value '))
    total = val1 + val2 + val3 
    average = total/3
    print ('Values:', val1, val2, val3)
    print (f'Total: \t\t {total}')
    print (f'Average: \t {average:.2f}')
    """
    Use following variables to save your result
    total 
    average
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return total, average


if __name__ == '__main__':
    main()
    
