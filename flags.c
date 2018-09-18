/* flags.c – Source file */

#include <stdio.h>
#include "flags.h"

int gFlag = 0;
char *text;

void welcome_msg(char *msg) {
printf("%s\n", msg);
return;
}

char *echo(char *msg) {
	text = msg;
return text;
}

int get_flag() {
return gFlag;
}

void set_flag(int flag) {
gFlag = flag;
return;
}