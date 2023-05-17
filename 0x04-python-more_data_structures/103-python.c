#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Outputs bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int length, i, max_length;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	length = ((PyVarObject *)(p))->ob_length;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  length: %ld\n", length);
	printf("  trying string: %s\n", string);

	if (length >= 10)
		max_length = 10;
	else
		max_length = length + 1;

	printf("  first %ld bytes:", max_length);

	for (i = 0; i < max_length; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - Outputs list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int length, i;
	PyListObject *list;
	PyObject *obj;

	length = ((PyVarObject *)(p))->ob_length;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", length);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < length; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
