import ftplib
  
ftpHost = "localhost"
ftpPort = 21 
ftpUname = "uname"
ftpPass = "pass"

ftp = ftplib.FTP_TLS(timeour=10)

ftp.connect(ftpHost,ftpPort)

ftp.login(ftpUname,ftpPass)

# güvenli veri bağlantısı için 
ftp.prot_p()

# çalışma dizinini değiştirmek için 
ftp.cwd("dizin/dizin1")

ftp.quit()
