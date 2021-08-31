def score(* values, status=False):
    """
    -> Function to analyzing score and situations of students.
    :param values: One or more scores of students (accept alots)
    :param stauts: Optional value, show the status of class average
    :return: dictionary with alot of informations about the class status
    """
    studentClass = dict()

    studentClass['total'] = len(values)
    studentClass['highest'] = max(values)
    studentClass['lowest'] = min(values)
    studentClass['average'] = sum(values) / len(values)

    if status == True:
        if studentClass['average'] > 7:
            studentClass['status'] = 'Good situation!'
        elif studentClass['average'] >= 5:
            studentClass['status'] = 'Normal situation!'    
        else:
            studentClass['status'] = 'Bad situation!' 

    return studentClass
        
anwser = score(9, 10, 5.5, 2.5, 8.5, status=True)
print(f'{anwser}')    
help(score)