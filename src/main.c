#include "libs/libs.h"
#include "windows/windows.h"

int main(int argc, char* argv[]) {
  gtk_init(&argc, &argv);

  new_project();

  gtk_main();
  return 0;
}
