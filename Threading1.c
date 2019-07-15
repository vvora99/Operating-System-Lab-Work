#include<stdio.h>
#include<pthread.h>

void* ThreadFunc(void* arg);

int main(int argc, char argv[])
{
    pthread_t idThread;
    puts("Let’s create a thread!");
    pthread_create(&idThread, NULL, ThreadFunc, (void*) 5);
    pthread_join(idThread, NULL);
}
    
void* ThreadFunc(void* arg)
{
    int i, n;
    n = (int) arg; /* Get the value of the argument passed in. */
    for (i = 0; i < n; i++)
    {
        printf("Loop Iteration %d\n", i + 1);   
    }
    return NULL;
}
