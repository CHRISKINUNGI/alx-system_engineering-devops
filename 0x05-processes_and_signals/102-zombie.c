#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 *
 * Return: Always 0.
 */
int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == 0)
		{
			/* Child process */
			exit(0); /* Child process exits immediately */
		}
		else if (child_pid > 0)
		{
			/* Parent process */
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
		{
			/* Fork failed */
			perror("Fork failed");
			exit(1);
		}
	}

	/* Call infinite_while function to keep the program running */
	infinite_while();

	return (0);
}
