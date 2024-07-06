import sys


input_length = input()
input_list_str = input().split()

# DEBUG - SHOW INPUTS
print(input_list_str, file=sys.stderr, flush=True)


if input_length == "0":
    print(input_length)

else:
    # CONVERT INPUT INTO INTEGERS
    input_list_int = [int(i) for i in input_list_str]


    # GET THE NEAREST TO 0 IN ABSOLUTE VALUE
    input_min = min([abs(int(x)) for x in input_list_int])


    if input_min in input_list_int:
        print(input_min)
    else:
        print(-input_min)

