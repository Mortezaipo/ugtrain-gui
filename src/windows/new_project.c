/*==========
New Project Window
==========*/

#include "../libs/libs.h"

void new_project() {
  // Declare items
  GtkWidget* window;
  GtkWidget* header;
  GtkWidget* window_box;

  GtkWidget* dynamic_memory_btn;
  GtkWidget* static_memory_btn;
  GtkWidget* pointer_memory_btn;

  GtkWidget* settings_btn;
  GtkWidget* settings_menu;

  // Create items
  window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
  window_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 3);
  header = gtk_header_bar_new();
  gtk_header_bar_set_show_close_button(GTK_HEADER_BAR(header), TRUE);

  dynamic_memory_btn = BigButton("Dynamic Memory", "Some description about this part.");
  static_memory_btn = BigButton("Static Memory", "Some description about this part.");
  pointer_memory_btn = BigButton("Pointer Memory", "Some description about this part.");

  settings_btn = gtk_button_new();
  settings_menu = gtk_popover_menu_new();

  // Item settings and connections
  gtk_container_set_border_width(GTK_CONTAINER(window), 10);
  gtk_header_bar_set_title(GTK_HEADER_BAR(header), "New Project");
  gtk_window_set_titlebar(GTK_WINDOW(window), header);

  gtk_box_pack_start(GTK_BOX(window_box), dynamic_memory_btn, TRUE, TRUE, 1);
  gtk_box_pack_start(GTK_BOX(window_box), static_memory_btn, TRUE, TRUE, 1);
  gtk_box_pack_start(GTK_BOX(window_box), pointer_memory_btn, TRUE, TRUE, 1);

  gtk_container_add(GTK_CONTAINER(window), window_box);

  gtk_widget_show_all(window);

  g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

}
