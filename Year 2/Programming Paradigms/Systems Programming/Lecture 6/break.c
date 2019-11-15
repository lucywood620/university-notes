#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(){

  int x = 1;
  int *p = &x;
  int i = 1;

  srand(time(NULL));
  // seed random numbers
  // from stdlib.h

  while(-1){
    p += rand()%200 -100;
    // rand() returns number betwen 0 and RAND_MAX
    // using % is cheap way of getting in a range
    // but it skews the distribution

    // using this instead might take longer to break
    //  p++;

    *p = rand();
     
      // using this gives more predictable results?
      //      *p = 27;
    
    // less offensive to read than write ?
    //    printf("Content is %d\n", *p);

    printf ("Ok so far %d accessing %p \n", i, p);
    i++;
  }
  
  return 0;
}
