#include<fcntl.h>
int main()
{
 int pid;
 pid=fork();
 if (pid<0)
	printf("Fork Failed!\n");
 else if(pid==0)
	{
		printf("Succ\n");
		printf("I'm a child, processId:%d\n",getpid());
		printf("Child's parent processId:%d\n",getppid());
	}
 else
	{
		printf("I'm a parent, my process ID:%d\n",getpid());
		printf("Parent processID:%d\n",getppid());
	} 
}
