# -*- coding: utf-8 -*-
"""Copy of capacity_of_activationfunction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UDZ-KD0StDNgM7CMiSwWoY6Yhch_PcPr
"""

import math
import itertools
from itertools import *
import numpy as np
import collections
from itertools import groupby
import random
import sys
import copy
import queue
from queue import Queue
from collections import deque

def bandpass(matrix_target,threshold):
    shape = matrix_target.shape
    threshold_m = np.full(shape, threshold)
    result = 1*np.greater(matrix_target,threshold_m)
    return result

def bandpass_inverse(matrix_target,threshold):
    shape = matrix_target.shape
    threshold_m = np.full(shape, threshold)
    result = 1*np.greater(threshold_m,matrix_target)
    return result

def del_same(tar):
    tar01 = [list(t) for t in set(tuple(_) for _ in tar)]
    return tar01


def compare_item(dict01, dict02,dict03,num):
    list_164 = []
    list_256 = []
    for value in dict02[num]:
        if value not in dict01[num]:
            list_164.append(value)
    for value in dict03[num]:
        if value not in dict01[num]:
            list_256.append(value)
    return list_164,list_256

def compare_item_array(array1, array2):
    list1 = array1.tolist()
    list2 = array2.tolist()
    list1 = []
    for value in list1:
        if value not in array2:
            list1.append(value)
    return np.array(list1)

def compare_whole(dict01, dict02,dict03):
    list_g = []
    for i in range(9):
        compare_item(dict01, dict02,dict03,i)

def check_miss_item(dict01, dict02,dict03,num):
    list_256_164 = []
    list_new = []
    for value in dict03[num]:
        if value not in dict02[num]:
            list_256_164.append(value)
    for value in dict01[num]:
        if value in list_256_164:
            list_new.append(value)
    return list_256_164,list_new    


def ori_result(position,num):
    if position >=result.shape[0]:
        position = position-num**2
    
    return result[position]

def exchange(num):
    """
    from the position in get from logic gates in total01 to matrix
    """
    r,c = 0,0
    if num>=result.shape[0]:
        num=num-result.shape[0]
  
    width= result.shape[0]**(1/2)
    r = int(num/width)
    c = int(num%width)
    return [r,c]


def exchange_list(list_tar):
    list_new = []
    for item in list_tar:
        list_new.append(exchange(item) )
    return list_new

def try_thr(result_matrix, start, end,num):
    list_re = []
    thr = np.linspace(start,end,num)
    for item in thr:
        rebp = bandpass(result_matrix,item)
        reivbp = bandpass_inverse(result_matrix, item)
        total01 = np.concatenate((rebp,reivbp),axis = 0)
        total = del_same(total01)
        list_re.append(total)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    return list_re  

def dictionary_outcome(tar,state):
    dict_outcome = { }
    for i in range(state+1):
        dict_outcome[i]=[item for item in tar if np.sum(item)==i]
        
    for key, value in dict_outcome.items():
        print(key,len(value),value)
    return dict_outcome

def get_result(n,x1,y1,x2,y2,x3,y3,x4,y4,mu,num):
    matrix0000, matrix1000, matrix0100, matrix0010, matrix0001, matrix1100, matrix1010, matrix1001,matrix0110, matrix0101, matrix0011, matrix1110, matrix1101, matrix1011, matrix0111, matrix1111= get_probability(n,x1,y1,x2,y2,x3,y3,x4,y4,mu,num)
    whole = np.vstack(((matrix0000, matrix1000, matrix0100, matrix0010, matrix0001, matrix1100, matrix1010, matrix1001,matrix0110, matrix0101, matrix0011, matrix1110, matrix1101, matrix1011, matrix0111, matrix1111 )))
    AHL = whole.T
    result = GFP(whole)
    G = result.T
    return AHL, G

def check_miss_item2(dict01, dict02,num):
    list_new = []
    for value in dict01[num]:
        if value not in dict02[num]:
            list_new.append(value)
    return list_new  

def try_thr01(result_matrix, start1, end1, start2, end2,num1,num2):
    list_re = []
    thr1 = np.linspace(start1,end1,num1)
    thr2 = np.linspace(start2,end2,num2)
    thr = np.hstack((thr1,thr2))
    for item in thr:
        rebp = bandpass(result_matrix,item)
        reivbp = bandpass_inverse(result_matrix, item)
        total01 = np.concatenate((rebp,reivbp),axis = 0)
        total = del_same(total01)
        list_re.append(total)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    return list_re 


def fun_threshold(input_matrix, threshold):
    result = 1*(input_matrix>threshold)
    return result

def inv_threshold(input_matrix, threshold):
    result = 1*(input_matrix<threshold)
    return result

def reduce_dim(threeD):
    threeD = threeD.reshape(-1, threeD.shape[-1])
    return threeD

def convert(list):
    return (*list, )

def del_same(tar):
    tar01 = [list(t) for t in set(tuple(_) for _ in tar)]
    return tar01

def dictionary_outcome(tar,state):
    dict_outcome = { }
    for i in range(state+1):
        dict_outcome[i]=[item for item in tar if np.sum(item)==i]
        
    for key, value in dict_outcome.items():
        print(key,len(value),value)
    return dict_outcome

def sort_str(str):
    return ''.join(sorted(str))

def join_str(list_tar):
    return ''.join(list_tar)

def create_and_sort(tar):
    l1 = join_str(tar)
    l1 = sort_str(l1)
    return l1

def contains(substring, string):
    if substring == string:
        return False
    else:
        c1 = collections.Counter(string)
        c2 = collections.Counter(substring)
        return not (c2 - c1)

def get_indx(list1,list_for_index):
    list2 = map((lambda x: list_for_index.index(x)), list1)
    return list(list2)


def orderfun(obj, subitem):
    for item in obj:
        if len(item) > len(subitem) and contains(subitem, item):
            if not(obj.index(subitem) < obj.index(item)):
                return False
            return True


def threshold1(array_order, threshold):
    result = 1*np.greater(array_order, threshold)
    return result

def threshold2(array_order, threshold):
    result = 1*np.greater_equal(array_order, threshold)
    return result

def all_threshold(array_order):
    list_re = []
    len = array_order.shape[1]
    for i in range(1,len):
        result1 = threshold1(array_order, i)
        result2 = threshold2(array_order, i)
        result = np.concatenate((result1, result2), axis = 0)
        result = del_same(result)
        list_re.append(result)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    array_re = np.array(list_re)
    return array_re

def bandpass1(array_order, left, right):
    result = 1*np.logical_and(array_order>=left, array_order<=right)
    return result

def bandpass2(array_order, left, right):
    result = 1*np.logical_and(array_order>left, array_order<right)
    return result

def all_bandpass(array_order):
    list_re = []
    len = array_order.shape[1]
    for i in range(1,len-1):
        for j in range(i,len):
            result1 = bandpass1(array_order, i, j)
            result2 = bandpass2(array_order, i, j)
            result = np.concatenate((result1,result2),axis = 0)
            result = del_same(result)
            list_re.append(result)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    array_re = np.array(list_re)
    return array_re

def all_bandpass2(array_order):
    list_re = []
    len = array_order.shape[1]
    for i in range(1,len):
        for j in range(i,len):
            result1 = bandpass1(array_order, i, j)
            result2 = bandpass2(array_order, i, j)
            result = np.concatenate((result1,result2),axis = 0)
            result = del_same(result)
            list_re.append(result)
    list_re = [item for sublist in list_re for item in sublist]
    list_re = del_same(list_re) 
    array_re = np.array(list_re)
    return array_re

"""Create list forward"""

def remain(all_list,list_tar):
    remain = map(lambda item: list(set(all_list)-set(item)), list_tar)
    remain = [list(item) for item in remain]
    return np.array(remain)

def join_str(list_tar):
    return ''.join(list_tar)

def all_possible_combined(current_list):
    next_item_set = [] # the list to put all items aftering combining 
    copy_currentlist = copy.deepcopy(current_list) # decopy the current order so it won't be changing
    for i in range(len(current_list)): 
        for j in range(i, len(current_list)):
            if len(set(current_list[i]) & set(current_list[j])) == 0: # make sure the two items have no same letters
                next_possible = create_and_sort(set(current_list[i]) | set(current_list[j])) # combine the letters and sort in alphabetical order
                if next_possible in current_list:
                    continue # if the otem already existed in the input list, move j to the next and combine with i until the combined element is a new one

                elif next_possible not in copy_currentlist:
                    next_item_set.append(next_possible) # if the item is a new one, add it into next_item_set
                    current_list = current_list[:j] # delete everything after j including j, as the combination of those item with item after current i would be larger than ij
                    break

    re_set = set(next_item_set)-set(copy_currentlist) # make sure no duplicate
    if len(re_set) <= 1: # if there is only 1 or no item possible, no need to filter it, return directly
        return re_set
    else:
        final = filter_states(re_set,copy_currentlist) # if there is more than 1 item, filter the set
        return final


def filter_states(set_tar,current_order):
    # new_set = set_tar
    list_tar = list(set_tar)
    # copy_listtar = copy.deepcopy(list_tar)
    # new_set = [set(item) for item in set_tar]
    for i in range(len(list_tar)):
        for j in range(i,len(list_tar)):
            if set(list_tar[i]) != set(list_tar[j]) and len(set(list_tar[i])& set(list_tar[j])) != 0 and list_tar[i] in set_tar and list_tar[j] in set_tar: # when two items have intersection,
                set1 = set(list_tar[i]) - set(list_tar[j])
                set2 = set(list_tar[j]) - set(list_tar[i])
                print(current_order,list_tar[i],list_tar[j],set1,set2)
                if set1 == set2 == set():
                    continue
                elif set1 == set():
                    set_tar.remove(list_tar[j])

                elif set2 == set():
                    set_tar.remove(list_tar[i])

                else:
                    str1 = create_and_sort(set1)
                    str2 = create_and_sort(set2)
                    if current_order.index(str1) < current_order.index(str2):
                        set_tar.remove(list_tar[j])


                    else:
                        set_tar.remove(list_tar[i])

    return set_tar

def generate_orders_v1(single_input_list, input):
    # to add the next possible states in the dictionary 'move' to the current list
    single_input = set(single_input_list)
    if len(input) == 0:
        input = [[]]

    input1 = [[]]
    for item in input:
        move = {0: (single_input - set(item)), 1: all_possible_combined(item)}
        if len(move[0]) == 0 and len(move[1]) == 0:
            return [item for item in input if len(item) == (2**(len(single_input))-1)]
            # return input
        else:
            for i in move:
                for j in move[i]:
                    new = copy.deepcopy(item)
                    new.append(j)
                    input1.append(new)

            input[:] = input1[:]
            # print(input)

def generate_orders1(single_input_list, input):
    single_input = set(single_input_list)
    if len(input) == 0:
        input = [[]]

    input1 = [['a']] # start with a single input

    for item in input:
        move = {0: (single_input - set(item)), 1: all_possible_combined(item)}
        if len(move[0]) == 0 and len(move[1]) == 0:
            return [item for item in input if len(item) == (2**(len(single_input))-1)]
            # return input
        else:
            for i in move:
                for j in move[i]:
                    new = copy.deepcopy(item)
                    new.append(j)
                    input1.append(new)

            input[:] = input1[:]
            # print(input)

def add_zero(list_tar):
    re_array = np.array(list_tar)
    zero = np.full((re_array.shape[0],1),'0')
    re_array = np.hstack((zero,re_array))
    return re_array

def add_zero_array(array_tar):
    zero = np.full((array_tar.shape[0],1),'0')
    re_array = np.hstack((zero,array_tar))
    return re_array

def get_all_index(state_list, all_order_array):
    index = []
    all_order_list = all_order_array.tolist()
    for item in all_order_list:
        ree = get_indx(state_list, item)
        index.append(ree)
    index_array = np.array(index)
    return index_array

def process_steps_combined(index_array):
    bp = all_bandpass2(index_array)
    ivbp = 1*np.less(bp,1)
    all_gate = np.concatenate((bp, ivbp),axis = 0)
    all_gate = del_same(all_gate)
    all1 = np.array(all_gate)
    return all1

def process_steps_combined_threshold(index_array):
    thr = all_threshold(index_array)
    invthr = 1*np.less(thr,1)
    all_gate = np.concatenate((thr, invthr),axis = 0)
    all_gate = del_same(all_gate)
    all1 = np.array(all_gate)
    return all1

def process_single_activation_function(index_array):
    re1 = all_threshold(index_array)
    re2 = 1*np.less(re1,1)
    re3 = all_bandpass2(index_array)
    re4 = 1*np.less(re3,1)
    all_gate = np.concatenate((re1, re2, re3, re4),axis = 0)
    all_gate = del_same(all_gate)
    all1 = np.array(all_gate)
    return all1

def process_single_activation_function_3(index_array,func_num):
    re1 = all_threshold(index_array)
    re2 = 1*np.less(re1,1)
    re3 = all_bandpass2(index_array)
    re4 = 1*np.less(re3,1)
    if func_num == 123:
        all_gate = np.concatenate((re1, re2, re3),axis = 0)
    elif func_num == 124:
        all_gate = np.concatenate((re1, re2, re4),axis = 0)
    elif func_num == 134:
        all_gate = np.concatenate((re1, re3, re4),axis = 0)
    elif func_num == 234:
        all_gate = np.concatenate((re2, re3, re4),axis = 0)

    all_gate = del_same(all_gate)
    all1 = np.array(all_gate)
    return all1

def process_activation_function_2(index_array,func_num):
    re1 = all_threshold(index_array)
    re2 = 1*np.less(re1,1)
    re3 = all_bandpass2(index_array)
    re4 = 1*np.less(re3,1)
    if func_num == 12:
        all_gate = np.concatenate((re1, re2),axis = 0)
    elif func_num == 13:
        all_gate = np.concatenate((re1, re3),axis = 0)
    elif func_num == 14:
        all_gate = np.concatenate((re1, re4),axis = 0)
    elif func_num == 23:
        all_gate = np.concatenate((re2, re3),axis = 0)
    elif func_num == 24:
        all_gate = np.concatenate((re2, re4),axis = 0)
    elif func_num == 34:
        all_gate = np.concatenate((re3, re4),axis = 0)


    all_gate = del_same(all_gate)
    all1 = np.array(all_gate)
    return all1

def toint(array_tar):
  m,n = array_tar.shape 
  a = 2**np.arange(n)[::-1]  # -1 reverses array of powers of 2 of same length as bits
  return array_tar @ a  # this matmult is the key line of code

def process_one_activation_function(index_array,functionname):
    if functionname == 'thr':
        re = all_threshold(index_array)
    elif functionname == 'invthr':
        re1 = all_threshold(index_array)
        re = 1*np.less(re1,1)
    elif functionname == 'bdp':
        re = all_bandpass2(index_array)
    elif functionname == 'invbdp':
        re3 = all_bandpass2(index_array)
        re = 1*np.less(re3,1)

    ree = del_same(re)
    ree_array = np.array(ree)
    return ree_array

position1 = ['a', 'b', 'c','d','e']
position2 = itertools.combinations(position1,2)
position3 = itertools.combinations(position1,3)
position4 = itertools.combinations(position1,4)
position5 = itertools.combinations(position1,5)
lst2 = [list(item) for item in position2]
lst3 = [list(item) for item in position3]
lst4 = [list(item) for item in position4]
lst5 = [list(item) for item in position5]

lst = lst2+lst3+lst4+lst5
new_list = []
for item in lst:
    new_list.append(''.join(item))



all_position = ['0']+position1 +new_list
print(all_position)

def or_operation_for2_v5(array_tar):  # original, create square matrix
    # array_tar = array_tar[0:20000]
    arr_bin = toint(array_tar)
    # print(arr_bin.shape)
    len1 = arr_bin.shape[0]
    n = (len1 // 5000) + 1
    arr_bin = arr_bin.reshape(len1, 1)
    # np.array_split(arr_bin, n)
    resu_array = np.array([0])
    for i in range(n):
        for j in range(i, n):
            l1 = np.array_split(arr_bin, n)[i].shape[0]
            l2 = np.array_split(arr_bin, n)[j].shape[0]

            array1 = np.full((l1, l2), np.array_split(arr_bin, n)[i])
            array2 = np.full((l1, l2), np.array_split(arr_bin, n)[j].T)
            or_re = np.bitwise_or(array1, array2)
            resu = np.unique(or_re)
            if resu_array.shape[0] == 1:
                resu_array = np.hstack((resu_array, resu))
                resu_array = resu_array[1:]

            else:
                resu_array = np.hstack((resu_array, resu))
                resu_array = np.unique(resu_array)
                print(resu_array.shape,j)

    # resu_array = np.unique(resu_array)
    return resu_array

def or_operation_for3_v2(array_tar,result_1_or): # original, create square matrix
    arr_bin = toint(array_tar)
    # print(arr_bin.shape)
    len1 = arr_bin.shape[0]
    len2 = result_1_or.shape[0]

    n = (len1 // 5000) + 1
    m = (len2 // 5000) + 1
    arr_bin = arr_bin.reshape(len1, 1)
    arr_bin_1or = result_1_or.reshape(len2, 1)
    
    resu_array = np.array([0])
    for i in range(m):
        for j in range(n):
            l1 = np.array_split(arr_bin_1or, m)[i].shape[0]
            l2 = np.array_split(arr_bin, n)[j].shape[0]

            array1 = np.full((l1, l2), np.array_split(arr_bin_1or, m)[i])
            array2 = np.full((l1, l2), np.array_split(arr_bin, n)[j].T)
            or_re = np.bitwise_or(array1, array2)
            resu = np.unique(or_re)
            if resu_array.shape[0] == 1:
                resu_array = np.hstack((resu_array, resu))
                resu_array = resu_array[1:]

            else:
                resu_array = np.hstack((resu_array, resu))
                resu_array = np.unique(resu_array)

    # resu_array = np.unique(resu_array)
    return resu_array

def ProducerThread_v2(single_input_list):
    single_input = set(single_input_list)
    global queue_order
    global queue_next_item
    while True:
        item = queue_order.get()
        move = {0: (single_input - set(item)), 1: all_possible_combined(item)}
        if move[0] == set() and move[1] == set():
            queue_order.put(item)
            return list(queue_order.queue)

        else:
            new_set = move[0] | move[1]
            new_list = [item for item in new_set]
            for next_item in new_list:
                queue_order.put(item+[next_item])
            # print(list(queue_order.queue))

def produce_position(position1_list):
    position2 = itertools.combinations(position1_list,2)
    position3 = itertools.combinations(position1_list,3)
    position4 = itertools.combinations(position1_list,4)
    position5 = itertools.combinations(position1_list,5)
    lst2 = [list(sort_str(item)) for item in position2]
    lst3 = [list(sort_str(item)) for item in position3]
    lst4 = [list(sort_str(item)) for item in position4]
    lst5 = [list(sort_str(item)) for item in position5]

    lst = lst2+lst3+lst4+lst5
    new_list = []
    for item in lst:
        new_list.append(''.join(item))

    all_position = ['0']+position1_list +new_list
    return all_position

from queue import Queue

single = ['a', 'b', 'c']
queue_order = Queue(maxsize=0)
queue_order.put([])
queue_next_item = Queue(maxsize=0)



re = ProducerThread_v2(single)

l = add_zero(re)
po3 = ['0', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
index = get_all_index(po3 ,np.array(l))

res1 = process_one_activation_function(index,'thr')
res2 = process_one_activation_function(index,'invthr')
res3 = process_one_activation_function(index,'bdp')
res4 = process_one_activation_function(index,'invbdp')

print(res1.shape,res2.shape,res3.shape,res4.shape)

res12 = process_activation_function_2(index,12)
res13= process_activation_function_2(index,13)
res14 = process_activation_function_2(index,14)
res23 = process_activation_function_2(index,23)
res24= process_activation_function_2(index,24)
res34= process_activation_function_2(index,34)

print(res12.shape,res13.shape,res14.shape,res23.shape,res24.shape,res34.shape)

res123 = process_single_activation_function_3(index,123)
res124= process_single_activation_function_3(index,124)
res134 = process_single_activation_function_3(index,134)
res234 = process_single_activation_function_3(index,234)

print(res123.shape,res124.shape,res134.shape,res234.shape)

"""----------------------------------------------------OR----------------------------------------------"""

def process_or_2or_3or(array):
    result1or = or_operation_for2_v5(array)
    result2or = or_operation_for3_v2(array,result1or)
    result3or = or_operation_for3_v2(array,result2or)
    return [array.shape,result1or.shape,result2or.shape,result3or.shape]

r = process_or_2or_3or(res123)
print(r)

"""-------------------------------------------------------"""