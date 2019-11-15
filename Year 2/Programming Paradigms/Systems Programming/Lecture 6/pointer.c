#include<stdio.h>
int main(){
	int i, *p, *q, j;
	i=5;
	j=7;
	p=&i;
	q=&j;
	q=p;
	*p=3;
	p=(int *)i;
	printf("%d %d %d %d %p %p\n",i,j,*p,*q,p,q);
	return 0;
}
