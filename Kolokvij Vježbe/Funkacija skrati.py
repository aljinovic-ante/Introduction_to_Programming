def skrati(br,naz):
    for i in range (br,1,-1):
        if br%i==0 and naz%i==0:
            br//=i
            naz//=i
            return br,naz

print(skrati(24,36))