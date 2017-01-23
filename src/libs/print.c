/*
Print out Library.
*/

#include "libs.h"

void print(char *msg_type, char *msg_text) {
  printf("%s%s%s", msg_type, msg_text, RESET);
}

void printl(char *msg_type, char *msg_text) {
  char* tmp_msg_text = malloc(sizeof(msg_text) + 1);
  sprintf(tmp_msg_text, "%s\n", msg_text);
  print(msg_type, tmp_msg_text);
}
