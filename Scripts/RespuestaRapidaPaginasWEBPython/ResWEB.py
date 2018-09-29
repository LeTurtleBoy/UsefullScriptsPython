#'WC=Cookie Wechall'
import requests
import sys
 
def main():
    if len(sys.argv) != 2:
        print "Indica el valor de la Cookie"
        exit()
    cookie = {'WC': sys.argv[1]}
    r = requests.get("http://www.wechall.net/challenge/training/programming1/index.php?action=request", cookies=cookie)
    r2 = requests.get("http://www.wechall.net/challenge/training/programming1/index.php?answer=%s" % r.text, cookies=cookie)
    print r2.text
if __name__ == "__main__":
    main()
