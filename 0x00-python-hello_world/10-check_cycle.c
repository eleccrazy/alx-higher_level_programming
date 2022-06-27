#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 *
 * @list: A pointer to the head of the list
 *
 * Return: Returns 0 if no cycle, 1 if there is cycle.
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow && fast && fast->next)
	{
		if (slow ==  fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
