#include <stdio.h> 
#include <stdlib.h>
#include <math.h>

// int * sieve(int n){
//     int p[n];
//     p[0] = 2;

//     int len = 1;
//     int i = 3;

//     while(len<n){
//         int x = 0;

//         while(i%p[x]!=0 && x<len){
//             x ++;
//         }

//         if(x==len){
//             p[len+1] = i;
//             // printf("sieve %d\n", i);
//             len ++;
//         }
        
//         i+=2;

//     }

//     return p;

// }

int getRandom(int n){
    int upper = pow(2, n) -1;
    int lower = pow(2, n-1) -1;
    int num = (rand() % (upper - lower + 1)) + lower;
    return num;
}

int lowLevelPrimeCheck(int prime_list[], int prime_candidate){
    int cond = 1;
    int ind = 0;
    int len = sizeof(prime_list) / sizeof(int);
    while(cond == 1 && ind<len){
        if(prime_candidate%prime_list[ind]==0){
            cond=0;
        }
        ind++;
    }

    return cond;
}

int main(){

    int n = 100;

    // int *primes = sieve(num_primes);

    int p[n];
    p[0] = 2;

    int len = 0;
    int i = 3;

    while(len<n){
        int x = 0;
        while(i%p[x]!=0 && x<len){
            x ++;
        }

        if(x==len){
            len ++;
            p[len] = i;            
        }
        
        i+=2;
    }

    for (int j=0; j<100; j++){
        printf("%d %d\n", lowLevelPrimeCheck(p, j), j);
    }

    // printf("%d", getRandom(10));
    
    return 0;
}