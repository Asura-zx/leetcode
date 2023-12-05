
'''You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

    pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].

Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.

 

Example 1:

Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
Explanation: From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.

Example 2:

Input: pref = [13]
Output: [13]
Explanation: We have pref[0] = arr[0] = 13.'''
def findArray(self, pref):
    reqarr=[]
    preflen=len(reqarr)
    temp=0
    for i in pref:
        temp=temp^i 
        reqarr.append(temp)
        temp=i
    return reqarr

pref=[13]
print(findArray(0,pref))
'''
how to solve: 
0 xor x(anynumber)= x
so we xor first element of pref with temp=0 and append it to requested array. here temp=0 can act as pref[-1]. we them store next element of pref into temp.

the important pattern to notice is: pref[i-1]^pref[i]=>reqarr[i] which is also true for pref[i-1]^reqarr[i]=>pref[i].
 so to find req[i], we find pref[i-1]^pref[i], both of whose value can be obtained from pref and stored in temp.

 suppose at current iteration we store pref[i] in temp, in next iteration it can act as pref[i-1]
'''

'''---completed---'''
