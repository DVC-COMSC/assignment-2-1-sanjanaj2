def main():
    """
    ##################################################
    Complete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """

    male = int(input('Number males: '))
    female = int(input('Number female: '))

    total = male + female

    m_perc = (male / total) * 100
    f_perc = (female / total) * 100

    print("The total number of students: " + str(total))
    print("The number of males and females: " + str(male) + " " + str(female))
    print(f"The percentage of males and females: {m_perc:.2f} \t {f_perc:.2f}")

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
