#!/usr/bin/python3
import re
import sys
import solve_series as s
def format_solution(sol_dict):
    if not sol_dict:
        print("The above problem is not supported")
        sys.exit(0)
    k = sorted(sol_dict)
    print(k)
    for step in k:
        print(step+" : "+sol_dict[step])

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
            if not series_list[i].isdigit():
                #position of - or _ if present
                #since last item contains ...
                 findPos = i
                 break
            series_list[i] = int(series_list[i])
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
    print("Aptitude Engine v0.1 alpha")
    print("Works for AP,GP and HP series problems")
    ques = input("Question:")
    sol_dict = questionAnalyser(ques)
    format_solution(sol_dict)


if __name__ == '__main__':
    main()
