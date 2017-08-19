#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    return printf("%s => %p\n", argv[1], getenv(argv[1]));
}
