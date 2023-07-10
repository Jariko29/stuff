def arithmetic_arranger(problems,answer=False):
    arranged_problem = []
    calc = 0
    problem = 0
    for i in problems:
        if(problem >= 5):
            print('Error: Too many problems.',problem)
            break
        space = i.find(' ') + 1
        space2 = i.find(' ',space+1)
        a = (i[:space-1])
        b = (i[space2+1:])
        if(len(a) >= 5 or len(b) >= 5):
            problem += 1
            print('Error: Numbers cannot be more than four digits.')
            continue
        if(a.isdigit() == False or b.isdigit() == False):
            problem += 1
            print('Error: Numbers must only contain digits.')
            continue
        a = int(a)
        b = int(b)
        if(i[space] != '+' and i[space] != '-'):
            problem += 1
            print('Error: Operator must be {} or {}.'.format('+','-'))
            continue
        apandisi = []
        if(answer == True):
            if(i[space] == '-'):
                calc = a - b
            if(i[space] == '+'):
                calc = a + b
            arranged_problem.append([a,b,calc,i[space]])
            for i in arranged_problem:
                if(i[0] > i[1]):
                    prosimo = len(str(i[0]))
                else:
                    prosimo = len(str(i[1]))
                grammes = '-' * (prosimo + 2)
                apandisi.append(f'{i[0]:>{prosimo+2}}\n{i[3]}{i[1]:>{prosimo+1}}\n{grammes}\n{i[2]:>{prosimo+2}}\n')
        if(answer == False):
            arranged_problem.append([a,b,i[space]])
            for i in arranged_problem:
                if(i[0] > i[1]):
                    prosimo = len(str(i[0]))
                else:
                    prosimo = len(str(i[1]))
                grammes = '-' * (prosimo + 2)
                apandisi.append(f'{i[0]:>{prosimo+2}}\n{i[2]}{i[1]:>{prosimo+1}}\n{grammes}\n')
    
    print(apandisi)
    keno = ''
    arranged_problems = keno.join(apandisi)
    return arranged_problems


papia = ''
papia = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True)
print(papia)

quit()
