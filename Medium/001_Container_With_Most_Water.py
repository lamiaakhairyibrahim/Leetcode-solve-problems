#//////// way (1)  have aproblem ==>  o(n^2)Time Limit Exceeded///////////
"""def most_water(l):
    w = 0
    for i in range(len(l)):
        j = i + 1
        for j in range( i+1 , len(l)):
            if l[i] <= l[j] :
                x = l[i] * (j-i)
                if x >= w :
                    w = x 
            else:
                x = l[j] * (j-i)
                if x >= w :
                    w = x 
    return w


l = [1,1]
print(most_water(l))"""

#////// way(2) //////  o(n)
def cont_water(height): 
                area = 0
                j = 0
                i = 1
                while(j != (len(height)-i)):
                    x = ((len(height)-i)-j) * min(height[j],height[len(height)-i])
                    area = max(x , area)
                    if height[j] <= height[len(height)-i]:
                        j = j+1
                    else:
                        i = i+1
                return area


l = [1,8,6,2,5,4,8,3,7]
print(cont_water(l))