CC = gcc
CFLAGS = `pkg-config --cflags gtk+-3.0`
LDFLAGS = `pkg-config --libs gtk+-3.0`

default = ugtrain-gui

ugtrain-gui: ugtrain-gui
	gcc src/libs/*.c src/windows/*.c src/main.c $(CFLAGS) $(LDFLAGS) -o bin/ugtrain-gui

clean:
	-rm -f bin/ugtrain-gui
