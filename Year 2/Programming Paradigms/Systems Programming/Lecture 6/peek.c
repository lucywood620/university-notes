#include <stdio.h>
int sub(int a, int b);

int main(){
  int x,y;
  x = 5;
  y = 7;

  int *z = &x;

  printf("x, y\n");
  printf(" %d \n\n", sub(x, y));
  printf("x, *z\n");
  printf(" %d \n\n", sub(x, *z));

  z--;
  printf("Before x %d\n", *z);
  z+=2;
  printf("After x %d\n", *z);

  z = &x - 5;
  while(z - &x <10){
    printf("At %p %d\n", z, *z);
    printf("At %p %p\n", &z, z);
    z++;
  }
  return 0;
}

int sub(int a, int b){
  int *p = &a;
  p--;
  printf("Before a %d\n", *p);
  p++;
  printf("At a %d\n", *p);
  p++;
  printf("After a %d\n", *p);
  return b-a;
}

