def r(e, t) :
    r = e[t:2] if t < 2  else e[t-2:t]
    return int(r, 16)
def email_jimi(n,o=0):
    c=""
    i=o+2
    while i<len(n):
        i += 2
        a = r(n, o)
        f = r(n, i) ^ a
        c=c+chr(f)
    return c
if __name__=='__main__':
    email_data='4c347e7a780c04252b24'
    email = email_jimi(email_data)
    print(email)