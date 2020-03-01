import rarfile, csv
rar_path = rarfile.RarFile("divorce.rar")
rarfile.RarFile.extractall(rar_path)


