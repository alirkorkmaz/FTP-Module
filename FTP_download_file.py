import ftplib
import os 

def downloadFileFromFTP(bolgeselDosyaYolu, hedefDosyaYolu, \
    ftpHost, ftpPort, ftpUserName, ftpPass, uzaktanCalismaDizini):

    indirme_basarili_mi: bool = False

    ftp = ftplib.FTP(timeout = 30)

    ftp.connect(ftpHost, ftpPort)
    
    ftp.login(ftpUserName, ftpPass)


    if not (uzaktanCalismaDizini == None or uzaktanCalismaDizini.strip() == ""):

        _ = ftp.cwd(uzaktanCalismaDizini)

    for fItr in range(len(hedefDosyaYolu)):
        hedefDosyaYolu = hedefDosyaYolu[fItr]

        bolgeselDosyaYolu = os.path.join(bolgeselDosyaYolu, hedefDosyaYolu)
        print("downloading file {0}".format(hedefDosyaYolu))

        with open(bolgeselDosyaYolu, "wb") as file:
            retCode = ftp.retrbinary("RETR " + hedefDosyaYolu, file.write)

    ftp. quit()


    if retCode.startswith('226'):
        indirme_basarili_mi = True

    return indirme_basarili_mi

ftpHost = "localhost"
ftpPort = 21
ftpUserName = "uname"
ftpPass = "pass"
bolgeselDosyaYolu = ""
uzakDosya = ["ali.txt"]
uzaktanCalismaDizini = ["test.txt"]

indirme_basarili_mi = downloadFileFromFTP(
    bolgeselDosyaYolu, uzaktanCalismaDizini, ftpHost, ftpPort, ftpUserName, ftpPass, uzakDosya
)

print("indirme durumu = {0}".format(indirme_basarili_mi))