#include <stdio.h>
#define MAXCHAR 1000
int readdata(char* filename)
{
    FILE *fp;
    char str[MAXCHAR];
    fp = fopen(filename, "r");
    if (fp == NULL){
        printf("Could not open file %s",filename);
        return 1;
    }
    while (fgets(str, MAXCHAR, fp) != NULL)
        printf("%s", str);
    fclose(fp);
    return 0;
}

int writedata()
{
    FILE *fp;
    fp = fopen("test.txt", "w+");
    fprintf(fp, "This is testing for fprintf...\n");
    fputs("This is testing for fputs...\n", fp);
    fclose(fp);
}



int main( )
{
//    readdata("read.txt");
    writedata();
    return 0;
}
