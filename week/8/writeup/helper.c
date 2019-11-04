#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

#define PASS_SIZE 16

FILE *fp;

int main(void) {
    int i;
    /* password for admin to provide to dump flag */
    char *password;

    /* seed random with time so that we can password */
    srand(time(0));
    password = calloc(1, PASS_SIZE+1);
    for (i = 0; i < PASS_SIZE; i++) {
        password[i] = rand() % ('z'-' ') + ' ';
    }
    password[PASS_SIZE] = 0;

    printf("%s", password);
    
    
}
