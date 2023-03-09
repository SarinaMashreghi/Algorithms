#include <stdio.h> 
#include <stdlib.h>
#include <math.h>

double getRandom(int lower, int upper){
    double num = (double)(rand() % (upper - lower + 1)) + lower;
    return num;
}

int main(){
    int n; 
    int k;
    printf("prime candidate:");
    scanf("%d", &n);
    printf("number of tests: ");
    scanf("%d", &k);

    // get r and s -> n = 2^r * s

    int s = n-1;
    int r = 0;
    while(s%2==0){
        r++;
        s /=2;
    }

    // printf("r: %d \ns: %d", r, s);

    int prime_check = 0;
    int composite_check = 0;

    for(int i=0; i<k && prime_check==0 && composite_check==0; i++){
        int rand_num = (int)(rand()%n);

        int t = pow(rand_num, s);

        if(t%n==1 || t%n==n-1){
            prime_check = 1;
        } 
        
        else{

            t = t%n;
            for(int j=1; j<=r && prime_check==0 && composite_check==0; j++){

                // printf("base:%d\n", t);
                // printf("power:%d\n",(int)pow(2, j)*s);
                // printf("mod:%d\n", (int)pow(rand_num, (int)pow(2, j)*s)%n);
                // printf("numbner: %d\n", (int)pow(rand_num, (int)pow(2, j)*s));
                t = (t*t)%n;
               if(t%n==n-1){
                    prime_check = 1;
                } else if(t%n==1){
                    composite_check = 1;
                }
            }
        }
    }

    if(prime_check==1){
        printf("prime");
    } else{
        printf("composite");
    }



    return 0;
}