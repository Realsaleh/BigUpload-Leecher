
import os
import time

validurl = "http://bigupload.in/download.php?filename="

def Start():
    os.system("title BigUpload Leecher v1.0.0")
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("[+] BigUpload Leecher v1.0.0")
    print ("[+] https://github.com/Realsaleh/BigUpload-Leecher")
    print ("[-] Coded By RealSalehn ")

def Leecher():
    Hash = "2e6af00b84549313f5b55aa537e6c9c7"
    Link = str(input("[+] Lotfan Link Download Khod Ra Vared Konid: "))
    if validurl in Link:
        Dl = Link.split("http://bigupload.in/download.php?filename=")[1]
        Result = "http://dl1.bigupload.in/dl.php?filename=%s&code=%s" % (Dl, Hash)
        print("Link Download Shoma:")
        print(Result)
        print("Shoma 10s Zaman Darid Link Khod Ra Copy Konid!")
        time.sleep(10)
    else:
        print("Address Vared Shode Motabar Nist!")
        print("Nemone Link Dorost 'http://bigupload.in/download.php?filename=series/Mr.Robot/BluRay/Mr.Robot.S01E01.1080p.BluRay.TakMovie.mkv'")
        print("10s Sabr Konid:)")
        time.sleep(10)
    
if __name__ == '__main__':
    while True:
        Start()
        Leecher()
