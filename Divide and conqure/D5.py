#FIND MAX_MIN


def findMaxMin(arr,start,end):
    if start==end:
        return arr[start],arr[end]
    else:
        mid=(start+end)//2
        left_min,left_max=findMaxMin(arr,start,mid)
        right_min,right_max=findMaxMin(arr,mid+1,end)




        return min(left_min, right_min),max(left_max,right_max)







def main():

    n=int(input("Enter the size of the arr:"))
    arr=[]
    for i in range(n):

        value=int(input("Enter value:"))
        arr.append(value)

        min_val,max_val = findMaxMin(arr,0,len(arr)-1)
        print('Max:',max_val )
        print('Min:', min_val)

main()