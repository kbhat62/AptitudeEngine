#!/usr/bin/python3
import re
import sys
import solve_series as s

#used to format the solution dictionary
def format_solution(sol_dict):
    if not sol_dict:
        print("The above problem is not supported")
        sys.exit(0)
    if sol_dict == -1:
        print("Invalid Question")
    if sol_dict == -2:
        print("The above series is not yet supported")
    print(sol_dict['result'])
    steps = sol_dict['steps']
    for i in range(len(steps)):
        print("Step"+str(i+1)+" : "+steps[i])

#analyses the question and calls the solution module
def questionAnalyser(ques):
    findPos = -1
    tp = 0
    if re.search(r" sum ",ques,re.I|re.M):
        tp = 1
    #extract the part which contains series 1,2,3,_,5,.....
    matchObj = re.search(r"(((\d+|_|\-|\d+\/\d+)\,)+)",ques,re.I|re.M)
    if matchObj:
        #series found
        series = matchObj.group(1);
        series_list = series.split(',')
        series_list = series_list[:len(series_list)-1]
        for i in range(len(series_list)):
            if series_list[i] == '-' or series_list[i] == '_' or isinstance(eval(series_list[i]),str):
                #position of - or _ if present
                #since last item contains ...
                 findPos = i
            else:
                series_list[i] = eval(series_list[i])
        if ( findPos != -1 ) :
            #if missing number is present in series
            odict = s.solveSeries(series_list,findPos,tp)
        else:
            #else if nth series problem
            matchObj = re.search(r"(\d+)(st|nd|rd|th) term",ques)
            #position for tn present like 1st term,2nd term ,3rd term ,4th term extract
            if matchObj:
                #position found
                findPos = int(matchObj.group(1))-1
                odict = s.solveSeries(series_list,findPos,tp)
            else:
                return -1;
        return odict
    else:
        return -2;
def main():
    print("Aptitude Engine v0.2 alpha")
    print("Works for AP,GP and HP series problems")
    ques = input("Question:")
    sol_dict = questionAnalyser(ques)
    format_solution(sol_dict)


if __name__ == '__main__':
    main()
