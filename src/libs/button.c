#include "libs.h"

GtkWidget *
BigButton(char *title, char *description) {
  GtkWidget* big_btn;
  GtkWidget* big_btn_box;
  GtkWidget* big_btn_title_lbl;
  GtkWidget* big_btn_description_lbl;
  char *markup = malloc(sizeof(strlen(title)) + 18);
  sprintf(markup, "<big><b>%s</b></big>", title);

  big_btn = gtk_button_new();
  big_btn_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 2);
  big_btn_title_lbl = gtk_label_new(NULL);
  gtk_label_set_markup(GTK_LABEL(big_btn_title_lbl), markup);
  gtk_label_set_xalign(GTK_LABEL(big_btn_title_lbl), 0);
  big_btn_description_lbl = gtk_label_new(description);
  gtk_label_set_xalign(GTK_LABEL(big_btn_description_lbl), 0);
  gtk_box_pack_start(GTK_BOX(big_btn_box), big_btn_title_lbl, TRUE, TRUE, 1);
  gtk_box_pack_start(GTK_BOX(big_btn_box), big_btn_description_lbl, TRUE, TRUE, 1);
  gtk_container_add(GTK_CONTAINER(big_btn), big_btn_box);
  return big_btn;
}
