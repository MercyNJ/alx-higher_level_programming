#include "lists.h"
#include <stdlib.h>

/**
 * insert_node -  Inserts num into sorted singly linked list
 * @head: singly list head
 * @number: number to insert
 *
 * Return: address of new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newn;
	listint_t *current;

	current = *head;

	newn = malloc(sizeof(listint_t));
	if (newn == NULL)
		return (NULL);

	newn->n = number;

	if (*head == NULL)
		*head = newn;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
				break;

			current = current->next;
		}
		newn->next = current->next;
		current->next = newn;
	}

	return (newn);
}
