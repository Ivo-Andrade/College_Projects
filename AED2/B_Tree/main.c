/************************************
	ACH2024 - Algoritmos e Estruturas de Dados II
	Exercicio Programa 2 - Operacoes em Arvores B
	Ivo de Andrade de Deus - 8075238
*************************************/

#include <stdbool.h>   /* variaveis bool assumem valores "true" ou "false" */
#include <stdlib.h>    /* para uso da funcao malloc e atoi */
#include <stdio.h>     /* para uso do tipo FILE */
#include <string.h>    /* para uso da funcao strcmp (comparação de srings) */

#define t 3             /* pre-definição do EP */

typedef int TipoChave;

typedef struct no {
    TipoChave chaves[2*t-1];
    struct no* filhos[2*t];
    int numChaves;
    bool folha;
} NO;

void arvoreB(FILE* entrada, FILE* saida);
NO* inicializa(NO* arvoreB);
NO* inserir(NO* arvoreB, int elemento);
NO* splitFilho(NO* noPai, int indice, NO* noCheio);
NO* inserirNaoCheio(NO* noAtual, int elemento);
NO* removerRaiz(NO* raiz, int elemento);
NO* remover(NO* atual, int elemento);
int obtemEsq(NO* atual);
int obtemDir(NO* atual);
NO* fundir(NO* atual, int indice);
bool busca(NO* arvoreB, int elemento);
void imprime(FILE* saida, NO* arvoreB);
void imprimeC(NO* arvoreB);

void arvoreB(FILE* entrada, FILE* saida){

    NO* arvoreB = (NO*)malloc(sizeof(NO));
    inicializa(arvoreB);

    printf("\nExecutando...\n");

    if(!entrada) return;
    char linha[255];
    int elemento;
    while(fscanf(entrada, "%s", linha)){
        if(!strcmp(linha,"f")) break;
        else if(!strcmp(linha,"i")){
            fscanf(entrada, "%s", linha);
            elemento = atoi(linha);

            printf("\nInserindo %d... ", elemento);
            arvoreB = inserir(arvoreB, elemento);

            printf("OK!", linha);
        }
        else if(!strcmp(linha,"r")){
            fscanf(entrada, "%s", linha);
            elemento = atoi(linha);

            printf("\nRemovendo %d... ", elemento);
            arvoreB = removerRaiz(arvoreB, elemento);

            printf("OK!", linha);
        }
        else if(!strcmp(linha,"p")){

            printf("\nImprimindo arvore...");
            imprimeC(arvoreB);
            imprime(saida, arvoreB);

            printf("OK!\n", linha);
            fprintf(saida, "\n");
        }
    }

    printf("\nFinalizando programa... ");

}

NO* inicializa(NO* arvoreB){
    arvoreB->numChaves = 0;
    arvoreB->folha = true;
    for(int i = 0; i <= 2*t; i++)
        arvoreB->filhos[i] = NULL;
    return arvoreB;
}

NO* inserir(NO* arvoreB, int elemento){
    NO* atual = arvoreB;
    if(atual->numChaves == 2*t - 1){
        NO* novo = (NO*)malloc(sizeof(NO));
        inicializa(novo);
        novo->folha = false;
        novo->numChaves = 0;
        novo->filhos[0] = atual;
        novo = splitFilho(novo, 0, atual);
        novo = inserirNaoCheio(novo, elemento);
        arvoreB = novo;
        return novo;
    }
    else atual = inserirNaoCheio(atual, elemento);
    return atual;
}

NO* splitFilho(NO* noPai, int indice, NO* noCheio){
    NO* novo = (NO*)malloc(sizeof(NO));
    inicializa(novo);
    novo->folha = noCheio->folha;
    novo->numChaves = t - 1;
    for(int j = 0; j < t - 1; j++){
        novo->chaves[j] = noCheio->chaves[j+t];
    }
    if(!noCheio->folha){
        for(int j = 0; j < t; j++){
            novo->filhos[j] = noCheio->filhos[j+t];
        }
    }
    noCheio->numChaves = t - 1;
    int paiChaves = noPai->numChaves;
    for(int j = noPai->numChaves; j >= indice + 1; j--){
        noPai->filhos[j+1] = noPai->filhos[j];
    }
    noPai->filhos[indice+1] = novo;
    for(int j = paiChaves - 1; j >= indice; j--){
        noPai->chaves[j+1] = noPai->chaves[j];
    }
    noPai->chaves[indice] = noCheio->chaves[t-1];
    noPai->numChaves = noPai->numChaves + 1;
    return noPai;
}

NO* inserirNaoCheio(NO* noAtual, int elemento){
    int i = noAtual->numChaves;
    if(noAtual->folha){
        while(i >= 0 && elemento < noAtual->chaves[i]){
            noAtual->chaves[i+1] = noAtual->chaves[i];
            i = i - 1;
        }
        noAtual->chaves[i+1] = elemento;
        noAtual->numChaves = noAtual->numChaves + 1;
    }
    else{
        while(i >= 0 && elemento < noAtual->chaves[i]){
            i = i - 1;
        }
        i = i + 1;
        NO* noFilho =  noAtual->filhos[i];
        if(noFilho->numChaves == 2*t - 1){
            splitFilho(noAtual, i, noFilho);
            if(elemento > noAtual->chaves[i]){
                noFilho = noAtual->filhos[i+1];
            }
        }
        noFilho = inserirNaoCheio(noFilho, elemento);
    }
    return noAtual;
}

NO* removerRaiz(NO* raiz, int elemento){
    if(!busca(raiz, elemento)) return raiz;
    if(raiz->numChaves == 1 && raiz->folha){
        raiz->numChaves = 0;
        return raiz;
    }
    return remover(raiz, elemento);
}

NO* remover(NO* atual, int elemento){
    int i = 0;
    while(i < atual->numChaves && atual->chaves[i] < elemento){
        i = i + 1;
    }
    if(i < atual->numChaves && atual->chaves[i] == elemento){
        if(atual->folha){
            atual->numChaves = atual->numChaves - 1;
            for( ; i < atual->numChaves; i++){
                atual->chaves[i] = atual->chaves[i+1];
            }
        }
        else{
            NO* filhoEsq = atual->filhos[i];
            NO* filhoDir = atual->filhos[i+1];
            int elemMovido = -1;
            if(filhoEsq->numChaves >= t){
                elemMovido = obtemEsq(filhoEsq);
                filhoEsq = remover(filhoEsq, elemMovido);
                atual->chaves[i] = elemMovido;
                return atual;
            }
            else if(filhoDir->numChaves >= t){
                elemMovido = obtemDir(filhoDir);
                filhoDir = remover(filhoDir, elemMovido);
                atual->chaves[i] = elemMovido;
                return atual;
            }
            else{
                atual = fundir(atual, i);
                atual->filhos[i] = remover(atual->filhos[i], elemento);
                if(atual->numChaves == 0) atual = atual->filhos[i];
            }
        }
    }
    else{
        NO* filho = atual->filhos[i];
        if(filho->numChaves == t - 1){
            NO* filhoEsq;
            NO* filhoDir;
            if(i > 0) filhoEsq = atual->filhos[i-1];
            else filhoEsq = NULL;
            if(i < atual->numChaves) filhoDir = atual->filhos[i+1];
            else filhoDir = NULL;
            if(filhoEsq && filhoEsq->numChaves >= t){
                for(int j = filho->numChaves; j > 0; j--){
                    filho->chaves[j] = filho->chaves[j-1];
                }
                filho->chaves[0] = atual->chaves[i-1];
                if(!filhoEsq->folha){
                    for(int j = filho->numChaves + 1; j > 0; j--){
                        filho->filhos[j] = filho->filhos[j-1];
                    }
                    filho->filhos[0] = filhoEsq->filhos[filho->numChaves];
                }
                filho->numChaves = filho->numChaves + 1;
                atual->chaves[i-1] = filhoEsq->chaves[filhoEsq->numChaves-1];
                imprimeC(atual);
                filhoEsq->numChaves = filhoEsq->numChaves - 1;
            }
            else if(filhoDir && filhoDir->numChaves >= t){
                printf("\n ATUAL 1 =");
                imprimeC(atual);
                printf("\n");
                filho->chaves[filho->numChaves] = atual->chaves[i];
                filho->numChaves = filho->numChaves + 1;
                atual->chaves[i] = filhoDir->chaves[0];
                filhoDir->numChaves = filhoDir->numChaves - 1;
                for(int j = 0; j < filhoDir->numChaves; j++){
                    filhoDir->chaves[j] = filhoDir->chaves[j+1];
                }
                if(!filhoDir->folha){
                    filho->filhos[filho->numChaves] = filhoDir->filhos[0];
                    for(int j = 0; j <= filhoDir->numChaves; j++){
                        filhoDir->filhos[j] = filhoDir->filhos[j+1];
                    }
                }
                printf("\n ATUAL 3 =");
                imprimeC(atual);
                printf("\n");
            }
            else if(filhoEsq){
                atual = fundir(atual, i - 1);
                filho = filhoEsq;
            }
            else if(filhoDir){
                atual = fundir(atual, i);
            }
        }
        filho = remover(filho, elemento);
    }
    return atual;
}

NO* fundir(NO* atual, int indice){
    NO* filhoEsq = atual->filhos[indice];
    NO* filhoDir = atual->filhos[indice+1];
    filhoEsq->numChaves = 2*t - 1;
    filhoEsq->chaves[t-1] = atual->chaves[indice];
    for(int i = 0; i < t - 1; i++){
        filhoEsq->chaves[t+i] = filhoDir->chaves[i];
    }
    if(!filhoEsq->folha){
        for(int i = 0; i < t; i++){
            filhoEsq->filhos[t+i] = filhoDir->filhos[i];
        }
    }
    atual->numChaves = atual->numChaves - 1;
    for(int i = indice; i <= atual->numChaves + 1; i++){
        atual->chaves[i] = atual->chaves[i+1];
        atual->filhos[i+1]= atual->filhos[i+2];
    }
    free(filhoDir);
    if(atual->numChaves == 0){
        free(atual);
    }
    return atual;
}

int obtemEsq(NO* atual){
    int numChaves = atual->numChaves;
    if(!atual->folha) return obtemEsq(atual->filhos[numChaves]);
    else{
        return atual->chaves[numChaves-1];
    }
}

int obtemDir(NO* atual){
    if(!atual->folha) return obtemDir(atual->filhos[0]);
    else{
        return atual->chaves[0];
    }
}

bool busca(NO* arvoreB, int elemento){
    if(!arvoreB) return false;
    if(arvoreB->numChaves == 0) return false;
    for(int i = 0; i < arvoreB->numChaves; i++){
        if(arvoreB->chaves[i] == elemento) return true;
        if(arvoreB->chaves[i] > elemento) return busca(arvoreB->filhos[i], elemento);
    }
}

void imprime(FILE* saida, NO* arvoreB){
    fprintf(saida, "(");
    int i = 0;
    int chave;
    if(arvoreB->folha){
        if(arvoreB->numChaves > 0){
            chave = arvoreB->chaves[0];
            fprintf(saida, "%d", chave);
        }
        for(int j = 1; j < arvoreB->numChaves; j++){
            chave = arvoreB->chaves[j];
            fprintf(saida, " %d", chave);
        }
    }
    else{
        while(i <= arvoreB->numChaves){
            if(arvoreB->filhos[i]){
                imprime(saida, arvoreB->filhos[i]);
                if(i < arvoreB->numChaves){
                    chave = arvoreB->chaves[i];
                    fprintf(saida, " %d ", chave);
                }
                i = i + 1;
            }
            else break;
        }
    }
    fprintf(saida, ")", chave);
}

void imprimeC(NO* arvoreB){
    printf("(");
    int i = 0;
    int chave;
    if(arvoreB->folha){
        if(arvoreB->numChaves > 0){
            chave = arvoreB->chaves[0];
            printf("%d", chave);
        }
        for(int j = 1; j < arvoreB->numChaves; j++){
            chave = arvoreB->chaves[j];
            printf(" %d", chave);
        }
    }
    else{
        while(i <= arvoreB->numChaves){
            if(arvoreB->filhos[i]){
                imprimeC(arvoreB->filhos[i]);
                if(i < arvoreB->numChaves){
                    chave = arvoreB->chaves[i];
                    printf(" %d ", chave);
                }
                i = i + 1;
            }
            else break;
        }
    }
    printf(")", chave);
}

int main( int argc, const char* argv[] ){

    printf("\n/************************************\n");
	printf("\nACH2024 - Algoritmos e Estruturas de Dados II\n");
	printf("\nExercicio Programa 2 - Operacoes em Arvores B\n");
	printf("\nIvo de Andrade de Deus - 8075238\n");
    printf("\n*************************************/\n");

    printf("\nInicializando...\n");

    FILE* entrada = fopen(argv[1], "r");
    FILE* saida = fopen(argv[2], "w+");
	arvoreB(entrada, saida);
	fclose(entrada);
	fclose(saida);

    printf("Tchau!\n");
}
