#include <stdio.h>
void sprawdzianie(int n){
    int i =0;
    int a =0;
    int l =0;
    int j=0;
    int z=1;
    for(i=1;i<30;i++){
    for(a=1;a<30;a++){
    for(l=1;l<30;l++){
    for(j=1;j<30;j++){
        if(i*i==n&& z==1){
        printf("%d^2+0^2+0^2+0^2",i);
        z=0;
        }
        else if(i*i+a*a==n && z==1){
            printf("%d^2+%d^2+0^2+0^2",i,a);
            z=0;
        }
        else if(i*i+a*a+l*l==n&& z==1){
        printf("%d^2+%d^2+%d^2+0^2",i,a,l);
                z=0;
        }
        else if(i*i+a*a+l*l+j*j==n&& z==1){
        printf("%d^2+%d^2+%d^2+%d^2",i,a,l,j);
                z=0;
        }
        }
        }
        }
        }
}
int main()
{
    sprawdzianie(310);
}
