#include<stdio.h>
#include<asm-generic/socket.h>

int main(int argc, char *argv[]) {
	#if defined (SO_REUSEPORT)
	printf("SO_REUSEPORT defined\n");
	#endif
	printf("check over\n");
}
