import ftplib
import os 

def uploadfiletoftp(localFilePath, ftpHost, ftpPort, FtpUserName, ftpPass, uzakCalismaDizini):

    # yüklemenin başarılı olup olmadığını belirten bölüm
    Yukleme_basarili_mi: bool = False

    # dosya adı ve dosya yolunun ayrılması 
    _, hedefDosyaAdi = os.path.split(localFilePath)

    # zaman aşımı 10 saniye ayarlandı 
    ftp = ftplib.FTP(timeout=10)

    # bağlantı ve giriş işlemleri yapıldı 
    ftp.connect(ftpHost, ftpPort)
    ftp.login(FtpUserName, ftpPass)

    # çalışma dizini belli ise değiştir 
    if not (uzakCalismaDizini == None or uzakCalismaDizini.strip() == ""):
        _ = ftp.cwd(uzakCalismaDizini)

    # binary dosya oku 
    with open(localFilePath, "rb") as file:

        # dosyayı FTP sunucusuna yükle ve boyut yüksek ise bloksize arttır
        retCode = ftp.storbinary(f"STOR {hedefDosyaAdi}", file, blocksize = 1024*1024)

    # bağlantı kapatıldı
    ftp.quit()

    #dönüş kodu kullanılarak yüklemenin başarılı olup olmadığı kontrol edildi
    if retCode.startswith('226'):
        Yukleme_basarili_mi = True

    # yükleme durumu döndürüldü
    return Yukleme_basarili_mi 

#bağlantı parametreleri
ftpHost = "localhost"
ftpPort = 21
ftpUserName = "uname"
ftpPass = "pass"
localfile = "test.txt"
uzakKlasor = "dizin/dizin1"
#  dosya yükleme 
Yukleme_basarili_mi = uploadfiletoftp(localfile, ftpHost, ftpPort, ftpUserName, ftpPass, uzakKlasor)

print("yüklem durumu = {0}".format(Yukleme_basarili_mi))