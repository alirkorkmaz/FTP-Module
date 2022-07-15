from ast import Try
import ftplib 

def FtpFileName(ftpHost, ftpPort, FtpUserName, ftpPass, uzakCalismaDizini):
    
    # yavaş bağlantılar için timeout 10 saniye belirlendi
    ftp = ftplib.FTP(timeout =10)

    #sunucu bağlantısı gerçekleştirildi
    ftp.connect(ftpHost, ftpPort)
    
    # sunucuya giriş yapıldı
    ftp.login(FtpUserName, ftpPass)

    # mevcut dizin belirtilmiş ise değiştirildi
    if not (uzakCalismaDizini == None or uzakCalismaDizini.strip() == "" ):
        _ = ftp.cwd(uzakCalismaDizini)

        # doysa adları boş listeye kaydedildi
        fnames = []

    try:
        # dosya adlarının listesini almak için nlist() kullanıldı
        fnames = ftp.nlst()

    except ftplib.error_perm as resp:
        if str(resp) == "550 no files found":
            fnames = []

        else: 
            raise 

    # bağlantı kesildi
    ftp.quit()

    # dosya adlarının listesi döndürüldü
    return fnames

# bağlantı parametreleri girildi
fnames = FtpFileName(ftpHost="localhost", ftpPort="21", FtpUserName="uname", ftpPass="pass", uzakCalismaDizini="dizin/dizin1")   
print(fnames)