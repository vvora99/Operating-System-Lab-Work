#include <stdio.h>
#include <string.h>
#include <pthread.h>

void* ThreadFunc(void* arg){

int n, i, flag = 0;
n = (int) arg;

    for(int i = 2; i <= n/2; ++i)
    {
        if(n%i == 0)
        {
            flag = 1;
            break;
        }
    }

    if (n == 1) 
    {
      printf("1 is neither a prime nor a composite number.");
    }
    else 
    {
        if (flag == 0)
          printf("%d is a prime number.\n", n);
        else
          printf("%d is not a prime number.\n", n);
    }
    
    return 0;
}

int main(int argc, char argv[]){
pthread_t idThread;
puts("Prime Number");
pthread_create(&idThread, NULL, ThreadFunc, (void*) 5);
pthread_join(idThread, NULL);
}
