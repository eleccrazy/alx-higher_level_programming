#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: A pointer to the head of the list
 * @number: The data to be inserted
 *
 * Return: Returns the address of the new node, or null in failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *traverse = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	while (traverse->next)
	{
		if ((traverse->next)->n > number)
		{
			new_node->next = traverse->next;
			traverse->next = new_node;
			return (new_node);
		}
		traverse = traverse->next;
	}

	new_node->next = NULL;
	traverse->next = new_node;

	return (new_node);
}
