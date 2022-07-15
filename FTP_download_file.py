import ftplib
import os 

def downloadFileFromFTP(bolgeselDosyaYolu, hedefDosyaYolu, \
    ftpHost, ftpPort, ftpUserName, ftpPass, uzaktanCalismaDizini):

    #indirmenin başarılı olup olmadığını berlirtir
    indirme_basarili_mi: bool = False

    ftp = ftplib.FTP(timeout = 30)

    # sunucuya bağlantı sağlar
    ftp.connect(ftpHost, ftpPort)
    
    #sunucuya giriş sağlar
    ftp.login(ftpUserName, ftpPass)

    # ftp dizini belirli ise dizini değiştirir
    if not (uzaktanCalismaDizini == None or uzaktanCalismaDizini.strip() == ""):

        _ = ftp.cwd(uzaktanCalismaDizini)

    # uzak dosya adını değiştirir
    for fItr in range(len(hedefDosyaYolu)):
        hedefDosyaYolu = hedefDosyaYolu[fItr]

        # yerel dosya yoluna uzak dosya adını ekleyerek yeni ad üretir
        bolgeselDosyaYolu = os.path.join(bolgeselDosyaYolu, hedefDosyaYolu)
        print("downloading file {0}".format(hedefDosyaYolu))

        #ftp dosyasının indirilmesi
        with open(bolgeselDosyaYolu, "wb") as file:
            retCode = ftp.retrbinary("RETR " + hedefDosyaYolu, file.write)

    ftp. quit()

    # indirme işleminin başarılı olup olmadığı kontrol edildi
    if retCode.startswith('226'):
        indirme_basarili_mi = True

    return indirme_basarili_mi

# bağlantı parametreleri
ftpHost = "localhost"
ftpPort = 21
ftpUserName = "uname"
ftpPass = "pass"
bolgeselDosyaYolu = ""
uzakDosya = ["ali.txt"]
uzaktanCalismaDizini = ["test.txt"]

# FTP sunucusunda dosyaları indirmek için işlev
indirme_basarili_mi = downloadFileFromFTP(
    bolgeselDosyaYolu, uzaktanCalismaDizini, ftpHost, ftpPort, ftpUserName, ftpPass, uzakDosya
)

print("indirme durumu = {0}".format(indirme_basarili_mi))