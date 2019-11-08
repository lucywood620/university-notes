#include <stdio.h>

int search (int a [], int n, int x) {
    int r, c;
    for (int l = 0, r = n - 1; l <= r;) {
        c = l + (r - l) / 2;
        if (a [c] > x) r = c - 1;
        else if (a [c] < x) l = c + 1;
        else return c;
    }
    return -1;
}

void bubbleSort(int numbers[], int array_size)
{
    int i, j, temp;
// i loops down the array
    for (i = (array_size - 1); i > 0; i--)
    {
//  j loops up the array
        for (j = 1; j <= i; j++)
        {
// if a number is greater than it's neighbour then swap it
            if (numbers[j-1] > numbers[j])
            {
                temp = numbers[j-1];
                numbers[j-1] = numbers[j];
                numbers[j] = temp;
            }
        }
    }
}

void printarray(int array[], int array_size) {
    int loop;
//    Just loops over the array and prints out each number
    for (loop = 0; loop < array_size; loop++) {
        printf("%d ", array[loop]);
    }
}

int main() {
    int arr[7] = {1,6,3,5,7,8,9};
    bubbleSort((int *) arr, 3);
//    printarray(arr,3);
    printf("%d",search(arr,7,8));
    return 0;
}






 
