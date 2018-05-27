#selecao dmaior numero dentre 3'

def returns(int value,int case){
    if(case = 1):
        print("nao existe menor valor pois foram insertados valores iguais");
    elif(case = 0){
        print("O menor valor eh {}".format(val));
} 
case = 0;
    
while 1:

    num1 = int(input("Digite o 1^ numero: "));
    num2 = int(input("Digite o 2^ numero: "));
    num3 = int(input("Digite o 3^ numero: "));
   
    if(num1 == num2 or num1 == num3 or num2 == num3):
        case = 1;

    if(num1 > num2 and num1 > num3):
        if(num2 > num3):
            print("O numero {} eh o maior".format(num1));
            returns(num2,case);            
        else:
            print("O numero {} eh o maior".format(num2));
            returns(num3,case);
    elif(num2 > num1 and num2 > num3):
        if(num1 > num3):
            print("O numero {} eh o maior".format(num2));
            returns(num1,case);
        else:
            print("O numero {} eh o maior".format(num2));
            returns(num3,case);
    elif(num3 > num1 and num3 > num2):
        if(num2 > num1):
            print("O numero {} eh o maior".format(num3));
            returns(num2,case);
        else:
            print("O numero {} eh o maior".format(num3));
            returns(num3,case);


            
    
