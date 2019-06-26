#include <stdio.h>
void main()
{

    int n = 0;
    int i = 0;
    double fi;
    double fimenos1 = 1;
    double fimenos2 = 2;
    double gi;
    double gimenos1 = 2;
    double gimenos2 = 1;
    double fnmenos2;
    double gnmenos2;

	printf("n = ");

	scanf("%d",&n);

	if(n <= 2){
        printf("Entrada invalida.");
        return;
	}

	if(n == 3){
        fnmenos2 = fimenos2;
        gnmenos2 = gimenos2;
        i = 1;
	}

	else if(n == 4){
        fnmenos2 = fimenos1;
        gnmenos2 = gimenos1;
        i = 2;
	}

    else{
        i = 3;
        for(int j = 3; j <= (n-2); j++){
            fi = fimenos1*2 + gimenos2;
            gi = gimenos1 + 3*fimenos2;
            fimenos2 = fimenos1;
            fimenos1 = fi;
            gimenos2 = gimenos1;
            gimenos1 = gi;
            i++;
        }
        fnmenos2 = fimenos1;
        gnmenos2 = gimenos1;
	}

	if(i == 1){
        n = 203;
        i = 3;
	}

	else if(i == 2){
        n = 204;
        i = 3;
	}

	else n = n + 202;

	for(int k = i ; k <= n; k++){
        fi = fimenos1*2 + gimenos2;
        gi = gimenos1 + 3*fimenos2;
        fimenos2 = fimenos1;
        fimenos1 = fi;
        gimenos2 = gimenos1;
        gimenos1 = gi;
	}

	double soma1 = fnmenos2 + gimenos1;
	double soma2 = fimenos1 - gnmenos2;

	printf("F(n-2) + G(n+200) = %.3e e ", soma1);
	printf("F(n+200) - G(n-2) = %.3e\n", soma2);

	return;

}