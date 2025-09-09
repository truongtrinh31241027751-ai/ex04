# a)Convert two lists into a dictionary
from urllib.parse import non_hierarchical


def bai_1():
    a = input("nhap key").split()
    b = input("nhap value").split()
    c = dict(zip(a,b))
    return c
# b)Merge two Python dictionaries into one
def bai_2():
    d1 = {"a":1, "b":2}
    d2 = {"c":3,"d":4}
    e = d1.copy()
    e.update(d2)
    return e
# c)Print the value of key ‘history’ from the below dict
def bai_3():
    d  =  {"id":4, "history" : 2 , "price": 73}

    return  list(d.values())[1]
#
# a)Initialize dictionary with default values
def bai_4():
    k = ["a","b","c"]
    dv = 1
    a = dict.fromkeys((k,dv))
    return a

# b)Create a dictionary by extracting the keys from a given dictionary
def bai_5():
    a = {"a":1,"b":2,"c":3,"d":4}
    b = ["a","b"]
    c = {k: a[k] for k in b if k in a}
    return c
# c)Delete a list of keys from a dictionary
def bai_6():
    a = {"a":1,"b":2,"c":3,"d":4}
    key_delete = ["a","b"]
    for k in key_delete:
        a.pop(k,None)
    print(a)
# d)Check if a value exists in a dictionary
def bai_7():
    a = input("nhap key").split()
    b = input("nhap value").split()
    c = dict(zip(a, b))
    val = input("Nhap value can kiem tra: ")
    if val in c.values():
            print(f"value {val} ton tai ")
    else:
            print(f"value khong ton tai")
    return ()


# e)Rename key of a dictionary
def bai_8():
    d = {"a": 1, "b": 2, "c": 3}

    old_key = "b"
    new_key = "x"

    if old_key in d:
        d[new_key] = d.pop(old_key)

    return d
def bai_9():
    a = {"a":4, "b":18, "c":73}
    b = min(a,key=a.get)
    return b
def bai_10():
    n = {'outer': {'inner': {'key': 10}}}
    n = ['outer']['inner']['key'] = 20

    return n
def bai_11():
    text = input("Nhập đoạn văn bản: ")
    stats = {}
    pos = 0
    for ch in text:
        count = 1
        if stats.get(ch) is None:
            item = {'count': count, 'positions': [pos]}
            stats[ch] = item
        else:
            count = int(stats[ch]['count']) + 1
            poss = list(stats[ch]['positions'])
            poss.append(pos)
            stats[ch] = {'count': count, 'positions': poss}
        pos += 1
    keys = sorted(stats.keys())
    for key in keys:
        print(f"Character '{key}' appears {stats[key]['count']} times, at {stats[key]['positions']}")


def bai_12():
    N = int(input("Nhập giá trị N: "))
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    p = {}
    index = 1
    for i in range(2, N):
        if is_prime(i):
            p[index] = i
            index += 1
    print("Dict các số nguyên tố nhỏ hơn", N, ":")
    print(p)
def main():
    while True:
        print("\n===== MENU =====")
        for i in range(1,13): print(f"{i}. Bài {i}")
        print("0. Thoát")
        chon=input("Chọn bài: ").strip()
        if chon=="0":break
        try: print(globals()[f"bai_{chon}"]())
        except: print("Lỗi hoặc lựa chọn không hợp lệ.")
if __name__=="__main__": main()