/*======================
General variables and methods list.
======================*/

#ifndef _UGTRAIN_GUI_HEADER
#define _UGTRAIN_GUI_HEADER
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <gtk/gtk.h>
#include <gdk/gdk.h>
#define ERROR "\033[91m"
#define WARNING "\033[93m"
#define SUCCESS "\033[92m"
#define INFO "\033[94m"
#define RESET "\033[0m"
#endif

GtkWidget *BigButton(char *, char *);
void print(char *, char *);
void printl(char *, char *);
