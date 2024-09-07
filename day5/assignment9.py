def dynamic_report(filename,title, *args, **kwargs):
    file = open(filename, 'a')
    file.write(f"Report title: {title}\n")

    file.write('='*len(f"Report title: {title}"))
    for keys, values in kwargs.items():
        if keys == 'conclusion':
            continue
        file.write(f"\n{keys.capitalize()}: {values}")
    file.write("\n\n")

    file.write("Report Sections: \n-----------------")

    for i in range(len(args)):
        if i == 1:
            continue
        file.write(f"\nSection {i+1}: {args[i]}")

    if 'conclusion' in kwargs.keys():
        t = f"\nConclusion:\n----------\n{kwargs['conclusion']}"
        file.write(t)



    file.write("\n")
    file.close()


dynamic_report('repo__rt.txt','Yearly Sales Report', "Introduction: Overview of sales performance.", "Data Analysis:Breakdown of sales data by region.","Market Trends:Analysis of current market trends.", author=" Adarsh",date="November 2024",conclusion="Overall,sales have increased by 15% compared to the previous month.")
