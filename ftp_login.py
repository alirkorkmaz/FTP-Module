import ftplib

# parametreler
ftpHost = 'localhost'
ftpPort = 21  
ftpUname = ''
ftpPass = ''

# zaman aşımı süresi 
ftp = ftplib.FTP(timeout=10)

# ftp sunucusuna bağlanmak için
ftp.connect(ftpHost, ftpPort)

# dosyalara erişmek için
ftp.login(ftpUname, ftpPass)

# sonraki adımlar dosya indirme, yükleme, kaldırma işlemleri

# bağlantının kesilmesi için 
ftp.quit()
print("yürütme tamamlandı...")