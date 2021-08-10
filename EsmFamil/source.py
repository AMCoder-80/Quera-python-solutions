import csv

answers = dict()
correct_ans = dict()
fields = ['esm', 'famil', 'keshvar', 'rang', 'ashia', 'ghaza']

def ready_up():
    with open('esm_famil_data.csv', 'r') as f:
        content = csv.reader(f)
        next(content)
        content = list(content)
        for i in fields:
            correct_ans[i] = [content[n][fields.index(i)].replace(" ", "") for n in range(len(content)) \
                if content[n][fields.index(i)]!= '']

def add_participant(*args, **kwargs):
    answers[kwargs.get('participant')] = kwargs.get('answers')
    

def calculate_all():
    grades = {i:0 for i in answers.keys()}
    
    for field in fields:
        current_user = list()
        current_ans = list()
        
        if all([ans[field].replace(" ", "") for ans in answers.values()]):
            for users, ans in answers.items():
                if ans[field].replace(" ", "") not in correct_ans[field]:
                    continue
                else:
                    current_user.append(users)
                    current_ans.append(ans[field].replace(" ", ""))

            for val in range(len(current_ans)):
                if current_ans.count(current_ans[val]) > 1:
                    grades[current_user[val]] += 5
                else:
                    grades[current_user[val]] += 10
                    
        else:
            for users, ans in answers.items():
                if ans[field].replace(" ", "") not in correct_ans[field]:
                    continue
                else:
                    current_user.append(users)
                    current_ans.append(ans[field].replace(" ", ""))

            for val in range(len(current_ans)):
                if current_ans.count(current_ans[val]) > 1:
                    grades[current_user[val]] += 10
                else:
                    grades[current_user[val]] += 15
    return grades

# ready_up()
# # print(correct_ans)
# add_participant(participant = 'salib', answers = {'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس', 'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالیپلو'})
# add_participant(participant = 'kianoush', answers = {'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل', 'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
# add_participant(participant = 'sajjad', answers = {'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما', 'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
# add_participant(participant = 'farhad', answers = {'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب', 'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})

# print(calculate_all())
    