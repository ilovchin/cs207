#include <stdlib.h>
#include <stdio.h>

// function declaration
int fib(int n);

int fib(int n) {
  if (n == 1) {
    return 0;
    }
  if (n == 2) {
    return 1;
    }
  return fib(n-1) + fib(n-2);
}

int main(int argc, char** argv)
{
  int num = atoi(argv[1]);
  printf( "Fibonacci Number: %d\n", fib(num));
}
