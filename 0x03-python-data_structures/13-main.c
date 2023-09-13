#include "lists.h"
/**
 * main - check the code for
 *
 * Return: Always 0.
 */
/*int main(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 1);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 17);
	add_nodeint_end(&head, 1);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");

	free_listint(head);

	return (0);
}*/
int main(void)
{
	listint_t *head;
	int i;

	head = NULL;
	for (i = 0; i < 1001; i++)
		add_nodeint_end(&head, i);
	for (i = 1000; i >= 0; i--)
		add_nodeint_end(&head, i);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");

	free_listint(head);

	return (0);
}
