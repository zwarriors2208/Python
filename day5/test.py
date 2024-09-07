def dynamic_report(fname,title, *args, **kwargs):
    f1=open(fname,'a')
    f1.write(f"Report title: {title}\n")
    r = f"Report title: {title}"
    print(r, '='*len(r), sep = "\n")
    f1.write('='*len(r))
    f1.write("\n")
    for keys, values in kwargs.items():
        if keys == 'conclusion':
            continue
        print(f"{keys.capitalize()}: {values}")
        f1.write(f"{keys.capitalize()}: {values} \n")
    print("\n\n")
    f1.write("\n\n")

    print("Report Sections: \n-----------------")
    f1.write("Report Sections: \n-----------------\n")
    for i in range(len(args)):
        if i == 1:
            continue
        print(f"Section {i+1}: {args[i]}")
        f1.write(f"Section {i+1}: {args[i]}\n")

    if 'conclusion' in kwargs.keys():
        print("\nConclusion:\n----------\n", kwargs['conclusion'], sep ="")
        f1.write("\nConclusion:\n----------\n" +  kwargs['conclusion'])

    print("\n")
    f1.close()


dynamic_report('ank','Yearly Sales Report', "Introduction: Overview of sales performance.", "Data Analysis:Breakdown of sales data by region.","Market Trends:Analysis of current market trends.", author=" Adarsh",date="November 2024",conclusion="Overall,sales have increased by 15% compared to the previous month.")