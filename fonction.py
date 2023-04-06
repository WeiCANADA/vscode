
'''
def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None
    
# First check to see if the list exists (if it has data in it).  If it does, return the -1 item (last item).  Otherwise, return None.

def last_element(l):
    if l:
        return l[-1]
    return None

'''
def single_letter_count(str_, chr_):
    return str_.lower().count(chr_)

print(single_letter_count("Hello World", "h"))
