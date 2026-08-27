#include <stdio.h>

// Function for iterative factorial
int factorial_iterative(int n)
{
    int fact = 1;

    for (int i = 1; i <= n; i++)
    {
        fact = fact * i;
    }

    return fact;
}

// Function for recursive factorial
int factorial_recursive(int n)
{
    if (n == 0 || n == 1)
    {
        return 1;
    }

    return n * factorial_recursive(n - 1);
}

int main()
{
    int n;

    // User input
    printf("Enter a number: ");
    scanf("%d", &n);

    // Check for negative number
    if (n < 0)
    {
        printf("Factorial is not possible for negative numbers.\n");
    }
    else
    {
        // Display results
        printf("\nFactorial using Iterative Method = %d\n",
               factorial_iterative(n));

        printf("Factorial using Recursive Method = %d\n",
               factorial_recursive(n));

        // Time analysis
        printf("\nTime Complexity:\n");
        printf("Iterative Method: O(n)\n");
        printf("Recursive Method: O(n)\n");
    }

    return 0;
}