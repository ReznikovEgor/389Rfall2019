#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <openssl/rand.h>

#include "crypto.h"
#include "common.h"

#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)


int main(int argc, char **argv) {
    int fd, check = 0;
    unsigned char fd_key_hash[16];
    char arr[] = "aaaa";
    char alph[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    int a, b, c, d;
    unsigned char *key;
    unsigned char *key_hash;
    fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
    read(fd, fd_key_hash, 16);
        for(a = 0; a < 62; a++){
            for(b = 0;b < 62; b++){
                for(c = 0; c < 62; c++){
                    for(d = 0; d < 62; d++){
                        arr[0] = alph[a];
                        arr[1] = alph[b];
                        arr[2] = alph[c];
                        arr[3] = alph[d];

                        key = md5_hash(arr, strlen(arr));
                        memset(key+2, 0, 14);
                        key_hash = md5_hash(key, 2);
                        
                        if(memcmp(key_hash, fd_key_hash, 16) == 0){
                            printf("The key is %s\n", arr);
                            return 1;
                        }
                    }
                }
            }
        }
    printf("fail");
        return -1;



    close(fd);

}


