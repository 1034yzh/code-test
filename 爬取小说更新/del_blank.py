def delblankline(infile,outfile='result.txt'):
    infopen = open(infile,'r')
    outfopen = open(outfile,'w')
    lines = infopen.readlines()
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")
    infopen.close()
    outfopen.close()
