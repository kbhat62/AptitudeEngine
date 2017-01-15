#!/usr/bin/python3
import re
import sys
def format_solution(sol_dict,findPos,tp):
    #note: sol_dict dictionary is of the following format
    #{"res":"25","ser":"AP","formula":"tn = a+(n-1)d"}
    #sx is the suffix for num ex 1"st" 2"nd"
    if not sol_dict:
        print("The above series is not supported")
        sys.exit(0)
    sx ="th"
    if ( findPos == 1 ):
        sx="st"
    elif ( findPos == 2 ):
        sx="nd"
    elif ( findPos == 3 ):
        sx="rd"

    #tp = 0 nth term problem
    #tp = 1 summation problem
    if ( tp == 0):
        pref = "The "+str(findPos)+sx+" term in the series is "+str(sol_dict['res'])
    else:
        pref = "The sum of first "+str(findPos)+" terms in the series is"+str(sol_dict['res'])
    print("The above series is in "+sol_dict['ser'])
    print("Formula used is : "+sol_dict['formula'])
    print(pref)

def main():
    print("Aptitude Engine v0.1 alpha")
    print("Works for AP,GP and HP series problems")
    ques = input("Question:")
    findPos = -1
    tp = 0
    if re.search(r" sum ",ques,re.I|re.M):
        tp = 1
    #extract the part which contains series 1.2.3._,5,.....
    matchObj = re.search(r"(((\d+|_|\-)\,)+)",ques,re.I|re.M)
    if matchObj:
        #series found
        series = matchObj.group(1);
        series_list = series.split(',')
        for i in range(len(series_list)-1):
            if not series_list[i].isdigit():
                #position of - or _ if present
                #since last item contains ...
                 findPos = i+1
                 break
        if ( findPos != -1 ) :
            #odict = helperfunc(series_list,findPos,tp)
            odict = {"res":"25","ser":"AP","formula":"tn = a+(n-1)d"}
        else:
            matchObj = re.search(r"(\d+)(st|nd|rd|th) term",ques)
            #position for tn present like 1st term,2nd term ,3rd term ,4th term extract
            if matchObj:
                #position found
                findPos = int(matchObj.group(1))
                #odict = helperfunc(series_list,findPos,tp)
            else:
                print("Invalid question")
                sys.exit(0)
        #note: odict dictionary is of the following format
        #{"res":"25","ser":"AP","formula":"tn = a+(n-1)d"}
        odict = {"res":"25","ser":"AP","formula":"tn = a+(n-1)d"}
        format_solution(odict,findPos,tp)
    else:
        print("Question not supported")
if __name__ == '__main__':
    main()
