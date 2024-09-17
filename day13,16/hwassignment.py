import re
def convert_date(t):
    s = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', t)
    for i in s:
        p = rf'\b{i}\b'
        t = re.sub(p, f'{i[-2:]}/{i[-5:-3]}/{i[0:4]}', t)
    return t

t = '''The project start date was 2024-01-15, which marked the beginning of the initial phase.
The preliminary review took place on 2024-03-22, where key objectives were evaluated.
The final submission deadline was set for 2024-06-30, by which all deliverables were required.
A follow-up meeting was scheduled for 2024-09-10 to assess progress and outline next steps.
The project completion date was finally confirmed as 2024-12-25, which concluded the year-long initiative.'''

print(convert_date(t))