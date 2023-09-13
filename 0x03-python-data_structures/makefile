COMPILE = -Wall -Wextra -Werror -pedantic -std=gnu89 -g

MEMORY_LEAK = -s --leak-check=full --show-leak-kinds=all --track-origins=yes 

PYCOMPILE = -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4

betty:
	betty lists.h *.c

run:
	gcc $(COMPILE) *.c -o palindrome

leak:
	valgrind $(MEMORY_LEAK) ./palindrome

compile:
     gcc $(PYCOMPILE) 100-print_python_list_info.c
