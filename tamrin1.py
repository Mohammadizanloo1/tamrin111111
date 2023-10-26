def my_final_grade_calculation(filename):
    results = {}
    

    
    for i, value in enumerate(lines):
        value = value.split(',')
        value[0] = value[0].strip().lower()
        value[1:] = (int(val.strip()) for val in value[1:])
        	q = value[1:7]
        	a = value[7:11]
        	       midterm = value[11]
        	       final = value[12]
        
 

        q = sum(q) / len(q)
        a.remove(min(a))
        a = sum(a) / len(a)
        	result = (q + a + midterm + final) / 4
        	results[value[0]] = 'passed' if result >= 60 else 'fail'
    
    print(results)


my_final_grade_calculation('grades.txt')
