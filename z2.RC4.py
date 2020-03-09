import os,sys

# Code by Chunye Gong
# Free to use

class RC4():
    N9=8

    def rc4_init(self,key,Len,NNN):
        kk=[0 for i  in range(NNN)]
        s=[i for i  in range(NNN)]
        
        for i in range(NNN):
            kk[i]=key[i%Len]
            
        j=0
        for i  in range( NNN ):
            j=(j + s[i] + kk[i]) % NNN
            tmp=s[i]
            s[i]=s[j]
            s[j]=tmp                    
        return s

    def rc4_crypt(self,s,Data,Len,NNN):
        i=0;j=0;t=0
        for k in range(Len):
            i=(i+1)%NNN
            j=(j+s[i])%NNN
            tmp=s[i]
            s[i]=s[j]
            s[j]=tmp
            t=(s[i]+s[j])%NNN
            Data[k] = Data[k] ^ s[t]
        return Data

    def run(self):

        sskey="A"
        key=list()
        for i in range(len(sskey)):
            key.append(ord(sskey[i]))
        lenKey=len(key)

        ssinput="addd."
        ori_data=list()
        for i in range(len(ssinput)):
            ori_data.append(ord(ssinput[i]))
        print('key=',sskey)
        print('input str=',ssinput)
        # print(ori_data)

        sbox=self.rc4_init(key,lenKey,self.N9)
        enc_data=self.rc4_crypt(sbox,ori_data,lenKey,self.N9)
        # print(enc_data)
        
        sbox=self.rc4_init(key,lenKey,self.N9)
        dec_data=self.rc4_crypt(sbox,enc_data,lenKey,self.N9)
        # print(dec_data)
        self.chk_result(ori_data,dec_data)
    
    def chk_result(self,ori_data,dec_data):
        #chk result
        bSame=True
        ss=''
        for i in range(len(ori_data)):
            ss=ss+chr(dec_data[i])
            if ori_data[i]!=dec_data[i]:
                bOK=bSame
                print("Error1234:",i,ori_data[i],dec_data[i])
                break
        
        print('decry str=',ss)
        if bSame:
            print("Successful!")
        else:
            print("Failed!")
        


        

obj=RC4()
obj.run()


