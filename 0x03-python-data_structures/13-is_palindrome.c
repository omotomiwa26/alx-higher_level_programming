#include "lists.h"
/**
 * is_palindrome - function checks if a singly linked list is a palindrome
 * @head: double pointer of first node of listint_t list
 * Return: 1 - If is a palindrome
 * Else - 0
 */
int is_palindrome(listint_t **head)
{
	int i, len, values[MAX_SIZE];
	listint_t *current;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	len = 0;
	current = *head;

	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	if (len > MAX_SIZE)
	{
		return (0);
	}

	current = *head;
	i = 0;

	while (current != NULL)
	{
		values[i] = current->n;
		i++;
		current = current->next;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (values[i] != values[len - i - 1])
		{
			return (0);
		}
	}
	return (1);
}
