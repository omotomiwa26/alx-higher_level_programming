#include "lists.h"

/**
 * check_cycle - Function checks a singly linked list for cycle.
 * @list: A pointer to the head of the linked list.
 * Return: 0 if there is no cycle.
 * Else: 1 if there is a cycle.
 *
 * To check if a singly linked list has a cycle in it,
 * you can use Floyd's cycle-finding algorithm,
 * also known as the "tortoise and hare" algorithm.
 * This algorithm uses two pointers moving at different speeds to traverse
 * the list. If there is a cycle, the two pointers will eventually meet.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		/* Move one step at a time */
		slow = slow->next;

		/* Move two steps at a time */
		fast = fast->next->next;

		/* If the two pointers meet, there is a cycle */
		if (slow == fast)
			return (1);
	}
	/* If the loop completes without meeting, there is no cycle */
	return (0);
}
