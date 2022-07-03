#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about python lists
 *
 * @p: A pyObject list
 *
 */

void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p), a = ((PyListObject *)p)->allocated, index = 0;
	PyObject *o;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", a);

	while (index < size)
	{
		o = PyList_GetItem(p, index);
		printf("Element %d: ", index);
		printf("%s\n", Py_TYPE(o)->tp_name);
		index++;
	}
}
