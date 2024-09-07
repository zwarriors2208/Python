def dynamic_report(title, *args, **kwargs):
    r = f"Report title: {title}"
    print(r, '='*len(r), sep = "\n")
    for keys, values in kwargs.items():
        if keys == 'conclusion':
            continue
        print(f"{keys.capitalize()}: {values}")
    print("\n\n")

    print("Report Sections: \n-----------------")

    for i in range(len(args)):
        if i == 1:
            continue
        print(f"Section {i+1}: {args[i]}")

    if 'conclusion' in kwargs.keys():
        print("\nConclusion:\n----------\n", kwargs['conclusion'], sep ="")


    print("\n")


dynamic_report('Yearly Sales Report', "Introduction: Overview of sales performance.", "Data Analysis:Breakdown of sales data by region.","Market Trends:Analysis of current market trends.", author=" Adarsh",date="November 2024",conclusion="Overall,sales have increased by 15% compared to the previous month.")