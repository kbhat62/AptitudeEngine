#!/usr/bin/python3
common_diff = 0;
def ap(series,index):
	i=0;
	global common_diff
	if(index != 0 and index < len(series)):
		n=index-1;
	elif(index>=len(series)):
		n = len(series)-1;
	else:
		n=0;
	flag=0;
	if((index!=1 and index!=0)):
		d=(series[1]-series[0]);
	else:
		d=(series[len(series)-1]-series[len(series)-2]);
	while (i<=n and flag<=1):
		if(i!=n):
			if((series[i+1]-series[i])!=d):
				return False;
			else:
				i=i+1;
		else:
			i=index+1;
			n=len(series)-1;
			flag=flag+1;
	common_diff=d;

	if index == 0:
		series[0] = series[1] - d;
	else:
		series[index] = series[index - 1] + d
	return series[index];


def hp(series,index):
	i=0;
	global common_diff
	if(index != 0 and index <= len(series)):
		n=index-1;
	elif(index>len(series)-1):
		n = len(series)-1;
	else:
		n=0;
	flag=0;
	if(index!=1 and index!=0):
		d=((1/series[1])-(1/series[0]));
	else:
		d=((1/series[len(series)-1])-(1/series[len(series)-2]));
	while (i<=n and flag<=1):
		if(i!=n):
			if(round((1/series[i+1])-(1/series[i]),2)!=round(d,2)):
				return False;
			else:
				i=i+1;
		else:
			i=index+1;
			n=len(series)-1;
			flag=flag+1;
	common_diff=d;
	if index == 0:
		series[0] = series[1] - round(1/d,2)
	else:
		series[index] = series[index -1] + round(1/d,2)
	return series[index];


def gp(series,index):
	i=0;
	global common_diff
	if(index != 0 and index <= len(series)):
		n=index-1;
	elif(index>len(series)-1):
		n = len(series)-1;
	else:
		n=0;
	flag=0;
	if(index!=0 and index!=1):
		r=series[1]/series[0];
	else:
		r=series[3]/series[2];
	if index == 0:
		series[0] = series[1] / r
	else:
		series[index] = series[0] * pow(r,index)

	while(i < len(series) - 1):
		if(series[i+1]/series[i]!=r):
			return False
		else:
			i = i + 1
	common_diff = r
	return series[index];


def addap(series,type,index):
	dict = {'result':' ','steps':' ','type':' ','stype':' '}
	if(type == 0):
			list = ['Series is in Arithmetic Progression']
			if(index == 0):
				term = series[1] - common_diff
				list.append("Formula to find 1st term : a2 - d")
				list.append('a2 = '+str(series[1])+', d = '+ str(common_diff))
				list.append(''+str(series[1])+' - '+str(common_diff))
			else:
				term = series[0] + index * common_diff
				list.append("Formula to find "+str(index + 1)+"th term is :a + (n - 1) d")
				list.append("a = "+str(series[0])+", d = "+ str(common_diff)+", n = "+str(index + 1))
				list.append(''+str(series[0])+' + '+'( '+str(index+1)+' ) * '+str(common_diff))
			list.append(''+str(index+1)+'Ans is '+str(term))
			dict['result'] = 'Ans is '+str(term)
	elif(type == 1):
			sum = ((index+1) * (2 * series[0] + index  * common_diff))/2
			list=['Series is in Arithmetic Progression',
			'Formula to find sum upto '+str(index + 1)+'th term is : S = n/2[2a + (n - 1)d]',
			'a = '+str(series[0])+', d = '+ str(common_diff)+', n = '+str(index + 1),
			'S = '+str(index+1)+'/2[2*'+str(series[0])+' + ('+str(index + 1)+' - 1)'+str(common_diff),
			'Sum = '+str(sum)]
			dict['result'] = 'Sum = '+str(sum)
	dict['steps'] = list
	return dict



def addgp(series,type,index):
	dict = {'result':' ','steps':' ','type':' ','stype':' '}
	if(type == 0):
			list = ['Series is in Geometric Progression']
			if(index == 0):
				term = series[1] / common_diff
				list.append('Formula to find '+str(index + 1)+'th term is = a2 / r')
				list.append('a2= '+str(series[1])+', r = '+ str(common_diff))
				list.append(''+str(series[1])+' / '+str(common_diff))
			else:
				term = series[0] * common_diff ** (index+1-1)
				list.append('Formula to find '+str(index + 1)+'th term is = a * r^(n - 1)')
				list.append('a = '+str(1/series[0])+', r = '+ str(common_diff)+', n = '+str(index + 1))
				list.append(''+str(series[0])+' * '+str(common_diff)+'^('+str(index+1)+' - 1)')
			list.append(''+str(index+1)+'th term is '+ str(term))
			dict['result'] = ''+str(index+1)+'th term is '+ str(term)
	if(type == 1):
			sum = (series[0] * (1 - common_diff ** (index+1)))/(1 - common_diff)
			list = ['Series is in Harmonic Progression',
			'Formula to Sum upto '+str(index + 1)+'th term is : Sn = [ a (1 - r^n) ] / [ 1 - r ]',
			'a = '+str(series[0])+', r = '+ str(common_diff)+', n = '+str(index + 1),
			'[ '+str(series[0])+'( 1 - '+str(common_diff)+'^'+str(index+1)+' ) ] / [ 1 - '+str(common_diff)+' ]',
			'Sum is '+ str(sum)]
			dict['result'] = 'Sum is '+ str(sum)
	dict['steps'] = list
	return dict


def addhp(series,type,index):
	dict = {'result':' ','steps':' ','type':' ','stype':' '}
	if(type == 0):
			list = ['Series is in Harmonic Progression']
			if(index == 0):
				term = 1/(1/series[1] - common_diff)
				list.append('Formula to find '+str(index + 1)+'th term is : 1 / [a2 - d]')
				list.append('a2 = '+str(1/series[1])+', d = '+ str(common_diff))
				list.append('1 / ['+str(1/series[1])+' - '+str(common_diff)+']')
			else:
				term = 1/(1/series[0] + index * common_diff)
				list.append('Formula to find '+str(index + 1)+'th term is : 1 / [a + (n - 1) d]')
				list.append('a = '+str(1/series[0])+', d = '+ str(common_diff)+', n = '+str(index + 1))
				list.append('1 / ['+str(1/series[0])+' + '+'( '+str(index+1)+' ) * '+str(common_diff)+']')
			if(isinstance(term,float)):
				term_str ="1 /"+str(int(1/term))+" or "+str(term);
			else:
				term_str = str(term);
			list.append(''+str(index+1)+'th term is  = '+ term_str)
			dict['result'] = ''+str(index+1)+'th term is  = '+ term_str
	if(type == 1):
			# pending
			print ("yet to code");
	dict['steps'] = list
	return dict


# function to find
def solveSeries(series,index,type):
	# type = 0, find nth;find missing number; type = 1, find the sum
	#index starts from 0
	if index < len(series) :
		series[index]='x'
	n = len(series)
	if(ap(series,index)):
		d = addap(series,type,index)
		if(n==4 and (index==1 or index==2)):
			if(not (series[index]-series[index-1]!=common_diff or series[index+1]-series[index]!=common_diff)):
				return d
		else:
			return d


			#print (sum);
	if(hp(series,index)):
		d = addhp(series,type,index)
		return d


	if(gp(series,index)):
		d = addgp(series,type,index)
		return d
	else:
		return False
		# not a AP, HP, GP
