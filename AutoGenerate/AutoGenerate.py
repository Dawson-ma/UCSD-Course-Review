import os
import pandas as pd
from ordered_set import OrderedSet
from collections import defaultdict

def AutoGenerate(csv_file_path):
    '''
    Generate .md file from course review csv file
    '''
    # Initialization
    summary_list = []

    # Read csv file
    df = pd.read_csv(csv_file_path)

    # Rename columns
    df = df.rename(columns={
        "課號 (e.g. 228)": "Course_Number", 
        "課程名稱 (e.g. Machine Learning for Physical Application)": "Course_Name",
        "選課原因": "Reason",
        "整體推薦程度": "Rating",
        "Year (e.g. 2024)": "Year",
        "Quarter (Fall/Winter/Spring/Summer)": "Quarter",
        "Professor (e.g. Gabriel M. Rebeiz)": "Professor",
        "Grading Structure (e.g. HW: 50%,Final: 50%,...；照這個格式打我們會感激你的)": "Grading_Structure",
        "課程內容 (上什麼)": "Content",
        "詳細評價 (教學方式、口音etc)": "Review",
        "成績平均": "Average_Grade",
        "姓名 (我們會把你列在Contibutors)": "Contributor",
        "課程科系碼 (e.g. ECE)": "Department",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [A+]": "A+",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [A]": "A",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [A-]": "A-",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [B+]": "B+",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [B]": "B",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [B-]": "B-",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [C+]": "C+",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [C]": "C",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [C-]": "C-",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [D]": "D",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [F]": "F",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [S]": "S",
        "成績分布 (Academic History可查詢)(e.g. A+:5%, ..., B+:10%, ...) [U]": "U",
    })

    # Get unique departments
    depts = OrderedSet(df['Department'])
    dept_dict = defaultdict(list)
    for dept in depts:
        category_dict = defaultdict(list)
        # Report if department name contains '/'
        if '/' in dept:
            for timestamp in df[df['Department'] == dept]['Timestamp']:
                print(f"The response's  department name {dept} at {timestamp} contains '/', please manually update the .md file.")
            continue
        
        # Get unique courses in the department
        courses = OrderedSet(df[df['Department'] == dept]['Course_Number'])

        # Write to .md file for each course
        for course in courses:
            # Report if course name contains '/'
            if '/' in course:
                for timestamp in df[(df['Department'] == dept) & (df['Course_Number'] == course)]['Timestamp']:
                    print(f"The response's  course name {dept} {course} at {timestamp} contains '/', please manually update the .md file.")
                continue
            
            # Get category for the course
            course_name = df[(df['Department'] == dept) & (df['Course_Number'] == course)]['Course_Name'].iloc[0]
            course_num = ''
            for cha in course:
                if cha.isdigit():
                    course_num += cha
            if int(course_num) < 100:
                category = f'{dept}1-99'
            elif int(course_num) < 200:
                category = f'{dept}100-199'
            else:
                category = f'{dept}200+'
            category_dict[category].append(f'* [{dept} {course} {course_name}](/Department/{dept}/{category}/{dept}{course}.md)')

            # Get unique years for the course
            years = OrderedSet(df[(df['Department'] == dept) & (df['Course_Number'] == course)]['Year'])

            # Create directory if not exist
            if not os.path.exists(f'./Department/{dept}'):
                os.makedirs(f'./Department/{dept}')
            if not os.path.exists(f'./Department/{dept}/{category}'):
                os.makedirs(f'./Department/{dept}/{category}')
            
            # Write to .md file
            with open(f'./Department/{dept}/{category}/{dept}{course}.md', 'w', encoding='utf-8') as f:
                f.write(f"# {dept} {course} {course_name}\n")
                f.write(f"- Average Rating: {df[(df['Department'] == dept) & (df['Course_Number'] == course)]['Rating'].mean()}\n")
                f.write(f"- Average Grading: {df[(df['Department'] == dept) & (df['Course_Number'] == course)]['Grading'].mean()}\n")
                f.write(f"- Average Loading: {df[(df['Department'] == dept) & (df['Course_Number'] == course)]['Loading'].mean()}\n")
                
                for year in years.__reversed__():
                    f.write(f"## {year}\n")
                    for quarter in ['Summer', 'Spring', 'Winter', 'Fall']:
                        responses = df[(df['Department'] == dept) & (df['Course_Number'] == course) & (df['Year'] == year) & (df['Quarter'] == quarter)]
                        if responses.shape[0] == 0:
                            continue

                        f.write(f"### {quarter}\n")
                        for _, response in responses.iterrows():
                            grading_list = response['Grading_Structure'].split(',')

                            f.write(f"- Professor: {response['Professor']}\n")
                            f.write(f"- Rating: {response['Rating']}/10\n")
                            f.write(f"- Grading: {response['Grading']}/10\n")
                            f.write(f"- Loading: {response['Loading']}/10\n")
                            f.write(f"- Grade:\n")
                            if not pd.isnull(response['Average_Grade']):
                                f.write(f"  - Avg: {response['Average_Grade']}\n")
                            if not pd.isnull(response['A+']):
                                f.write(f"  - A+: {response['A+']}%\n")
                            if not pd.isnull(response['A']):
                                f.write(f"  - A: {response['A']}%\n")
                            if not pd.isnull(response['A-']):
                                f.write(f"  - A-: {response['A-']}%\n")
                            if not pd.isnull(response['B+']):
                                f.write(f"  - B+: {response['B+']}%\n")
                            if not pd.isnull(response['B']):
                                f.write(f"  - B: {response['B']}%\n")
                            if not pd.isnull(response['B-']):
                                f.write(f"  - B-: {response['B-']}%\n")
                            if not pd.isnull(response['C+']):
                                f.write(f"  - C+: {response['C+']}%\n")
                            if not pd.isnull(response['C']):
                                f.write(f"  - C: {response['C']}%\n")
                            if not pd.isnull(response['C-']):
                                f.write(f"  - C-: {response['C-']}%\n")
                            if not pd.isnull(response['D']):
                                f.write(f"  - D: {response['D']}%\n")
                            if not pd.isnull(response['F']):
                                f.write(f"  - F: {response['F']}%\n")
                            if not pd.isnull(response['S']):
                                f.write(f"  - S: {response['S']}%\n")
                            if not pd.isnull(response['U']):
                                f.write(f"  - U: {response['U']}%\n")
                            f.write(f"- Reason for Taking this Course: {response['Reason']}\n")
                            f.write(f"- Grading Structure:\n")
                            for grading in grading_list:
                                f.write(f"  - {grading}\n")
                            f.write(f"- Course Content:  \n")
                            f.write(f"{response['Content']}\n")
                            f.write(f"- Review:  \n")
                            f.write(f"<details>\n")
                            f.write(f"{response['Review']}\n")
                            f.write(f"</details>\n")

        try: 
            for category in sorted(category_dict.keys()):
                with open(f'./Department/{dept}/{category}/README.md', 'w', encoding='utf-8') as f:
                    f.write(f"# {category[:len(dept)]} {category[len(dept):]}\n")
                    for course in category_dict[category]:
                        f.write(course + '\n')
            
            with open(f'./Department/{dept}/README.md', 'w', encoding='utf-8') as f:
                f.write(f"# {dept}\n")
                for category in sorted(category_dict.keys()):
                    f.write(f"* [{category[:len(dept)]} {category[len(dept):]}](/Department/{dept}/{category}/README.md)\n")
                    for course in category_dict[category]:
                        f.write('  ' + course + '\n')
        except FileNotFoundError:
            print(f"Error: {dept} {category} README.md not found.")
            pass

        dept_dict[dept] = category_dict

    with open(f'./Department/README.md', 'w', encoding='utf-8') as f:
        f.write("# Department\n")
        for dept in sorted(dept_dict.keys()):
            f.write(f"* [{dept}](/Department/{dept}/README.md)\n")
    
    # Write to summary.md
    with open('./SUMMARY.md', 'w', encoding='utf-8') as f:
        f.write("# Summary\n")
        f.write("* [Introduction](README.md)\n")
        f.write("* [Preface](Preface/README.md)\n")
        f.write("* [Department](Department/README.md)\n")
        for dept in sorted(dept_dict.keys()):
            f.write(f"  * [{dept}](/Department/{dept}/README.md)\n")
            for category in sorted(dept_dict[dept].keys()):
                f.write(f"    * [{category[:len(dept)]} {category[len(dept):]}](/Department/{dept}/{category}/README.md)\n")
                for course in dept_dict[dept][category]:
                    f.write('      ' + course + '\n')
        f.write("* [Editors](Editors/README.md)\n")
        f.write("* [Contributors](Contributors/README.md)")

if __name__ == '__main__':
    AutoGenerate('../raw/UCSDCourseReview.csv')