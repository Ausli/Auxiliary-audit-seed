import execjs
def email_jimi(email_data):
    #邮箱解密
    j = '''
        function e(e) {
            try {
                if ("undefined" == typeof console)
                    return;
                "error"in console ? console.error(e) : console.log(e)
            } catch (e) {}
        }
        function t(e) {
            return e.replace(/"/g, "&quot;")
        }
        function r(e, t) {
            var r = e.substr(t, 2);
            return parseInt(r, 16)
        }
        function n(n, o) {
            for (var c = "", a = r(n, o), i = o + 2; i < n.length; i += 2) {
                var f = r(n, i) ^ a;
                c += String.fromCharCode(f)
            }
            try {
                c = decodeURIComponent(escape(c))
            } catch (l) {
                e(l)
            }
            return t(c)
        }
        '''
    p =execjs.compile(j)
    return p.call('n',email_data,0)
if __name__=='__main__':
    email_data='4c347e7a780c04252b24'
    email = email_jimi(email_data)
    print(email)