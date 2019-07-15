#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#define MAX 3   /* # of item  to produce */

pthread_mutex_t the_mutex;
pthread_cond_t condc, condp;
int consumeTimes[MAX] = { 1, 4, 3 };
int toConsume = 0;

void* producer(void *ptr) {
    int i;

    for (i = 0; i < MAX; i++) {
        pthread_mutex_lock(&the_mutex); 
        printf("Producer: Produced item %d \n", i);
        toConsume++;
        pthread_cond_signal(&condc); /* wake up consumer */
        pthread_mutex_unlock(&the_mutex); 
        sleep(3);

    }
    pthread_exit(0);
}

void* consumer(void *ptr) {
    int i;
    for (i = 0; i < MAX; i++) {
        pthread_mutex_lock(&the_mutex); 
        while (toConsume <= 0) 
            pthread_cond_wait(&condc, &the_mutex);
	    pthread_mutex_unlock(&the_mutex); 

        sleep(consumeTimes[i]);

        pthread_mutex_lock(&the_mutex); 
        printf("Consumer: Consumed item %d\n", i);
        toConsume--;
        pthread_mutex_unlock(&the_mutex); 
    }
    pthread_exit(0);
}

int main(int argc, char **argv) {
    pthread_t pro, con;

    // Initialize the mutex and condition variables
    /* What's the NULL for ??? */
    pthread_mutex_init(&the_mutex, NULL);
    pthread_cond_init(&condc, NULL); /* Initialize consumer condition variable */
    pthread_cond_init(&condp, NULL); /* Initialize producer condition variable */

    // Create the threads
    pthread_create(&con, NULL, consumer, NULL);
    pthread_create(&pro, NULL, producer, NULL);

    // Wait for the threads to finish
    // Otherwise main might run to the end
    // and kill the entire process when it exits.
    pthread_join(con, NULL);
    pthread_join(pro, NULL);

    // Cleanup -- would happen automatically at end of program
    pthread_mutex_destroy(&the_mutex); /* Free up the_mutex */
    pthread_cond_destroy(&condc); /* Free up consumer condition variable */
    pthread_cond_destroy(&condp); /* Free up producer condition variable */

}
