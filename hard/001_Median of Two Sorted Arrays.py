#-----------------------------------------
#-----------------------------------------
import math
def findMedianSortedArrays( nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    #print(nums1)
    len_num = len(nums1)
    #print("len : " , len_num)
    if len_num % 2  != 0 :
        #print("len : " , len_num)
        x = round(len_num / 2)
        #print("x : " , x)
        #print("nums : ",nums1[x-1])
        return nums1[x]
    else :
        y = int(len_num / 2)
        #print("y : ",y)
        m = (nums1[y-1] + nums1[y])/2
        #print("m : ",m)
        return m




def findMedianSortedArrays( nums1, nums2):
    print("len nums1 : ",len(nums1))
    print("len nums2 : ",len(nums2))
    
    l =[]
    mini_length = min(len(nums1),len(nums2))
    count = 0
    if len(nums1) == 0 :
        l = nums2
    elif len(nums2) == 0 :
        l = nums1
    else:
            while count < mini_length :
                # [1,3], [2,7]
                if len(l) == 0:
                        l.append(min(nums1[count],nums2[count]))
                        l.append(max(nums1[count],nums2[count]))
                else:
                    x = l[-1]
                    mini_ii = min(nums1[count],nums2[count])
                    max_ii  = max(nums1[count],nums2[count])
                    max_l = max(x , mini_ii)
                    l[-1] = min(x ,mini_ii )
                    l.append(min(max_l ,max_ii))
                    l.append(max(x,max_ii))

                count +=1
            
            print(l)
            print("COUNT:",count)
            if len(l) != (len(nums1)+len(nums2)):
                        if count == len(nums1):
                            y = l[-1]
                            z = l[-2]
                            print("y :",y)
                            if y >= nums2[-1]:
                                    print("hello1")
                                    if l[-2] >= nums2[-1]:
                                        if count == len(nums2)-1:
                                                print("yallahwee")
                                                l[-2] = nums2[count]
                                                l[-1] = z
                                                l.append(y)
                                        else:
                                            print("yadey el nella")
                                            l[-2] = nums2[count]
                                            l[-1] = nums2[count+1]
                                            l.extend(nums2[count+2:])
                                            l.append(z)
                                            l.append(y)
                                    elif l[-2] >= nums2[count]:
                                        print("lamiaa")
                                        l[-2] = nums2[count]
                                        i1 = count+1
                                        p = 0
                                        for i1 in range(count+1 , len(nums2)):
                                            if z >= nums2[i1]:
                                                l[len(l)-1+p] = nums2[i1]
                                                p+=1
    
                                            else:
                                                l[len(l)-1+p] = z
                                                break
                                        if  len(l) != (len(nums1)+len(nums2)):
                                            l.extend(nums2[i1:])
                                            l.append(y)
                                        else:
                                            l.append(y)
                                        
                                    else:
                                        l[-1] = nums2[count]
                                        l.extend(nums2[count+1:])
                                        l.append(y)



                            elif y < nums2[count]:
                                print("hello2")
                                l.extend(nums2[count:])
                            else :
                                print("hello3")
                                l[-1] = nums2[count]
                                i = count+1
                                for i in range(count+1 , len(nums2)):
                                    if y >= nums2[i]:
                                        l.append(nums2[i])
                                    else:
                                        l.append(y)
                                        break
                                print("i :",i)
                                if len(l) != (len(nums1)+len(nums2)):
                                    l.extend(nums2[i:])
                                
                        else:
                            y1 = l[-1]
                            z1 = l[-2]
                          
                            if y1 >= nums1[-1]:
                                    print("hello1dash")
                                    if l[-2] >= nums1[-1]:
                                        if count == len(nums1)-1:
                                                print("yallahwee")
                                                l[-2] = nums1[count]
                                                l[-1] = z1
                                                l.append(y1)
                                        else:
                                            l[-2] = nums1[count]
                                            1[-1] = nums1[count+1]
                                            l.extend(nums1[count+2:])
                                            l.append(z1)
                                            l.append(y1)
                                    elif l[-2] >= nums1[count]:
                                        
                                            l[-2] = nums1[count]
                                            i1 = count+1
                                            p = 0
                                            for i1 in range(count+1 , len(nums1)):
                                                if z1 >= nums1[i1]:
                                                    l[len(l)-1+p] = nums1[i1]
                                                    p+=1
        
                                                else:
                                                    l[len(l)-1+p] = z1
                                                    break
                                            if  len(l) != (len(nums1)+len(nums2)):
                                                l.extend(nums1[i1:])
                                                l.append(y1)
                                            else:
                                                l.append(y1)
                                    else:
                                        l[-1] = nums1[count]
                                        l.extend(nums1[count+1:])
                                        l.append(y1)



                            elif y1 < nums1[count]:
                                print("hello2dash")
                                l.extend(nums1[count:])
                            else :
                                print("hello3dash")
                                l[-1] = nums1[count]
                                i = count+1
                                for i in range(count+1 , len(nums1)):
                                    if y1 >= nums1[i]:
                                        l.append(nums1[i])
                                    else:
                                        l.append(y1)
                                        break
                                print("i :",i)
                                if len(l) != (len(nums1)+len(nums2)):
                                    l.extend(nums1[i:])

    print(l)

    if len(l) % 2 != 0 :    # odd
        m = len(l)//2 
        return float(l[m])
    else :                  # even
        n = int(len(l) / 2)
        median = (l[n]+l[n-1]) / 2
        return median



def findMedianSortedArrays( nums1, nums2):
    l=[]
    l = nums1
    l.extend(nums2)
    l.sort()
    if len(l) % 2 != 0 :    # odd
        m = len(l)//2 
        return float(l[m])
    else :                  # even
        n = int(len(l) / 2)
        median = (l[n]+l[n-1]) / 2
        return median

print(findMedianSortedArrays( [4,5] , [1,2,3,6,7] ))

    







