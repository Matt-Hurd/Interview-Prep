/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   merge.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mhurd <mhurd@student.42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/01/26 21:14:02 by mhurd             #+#    #+#             */
/*   Updated: 2017/01/26 22:21:03 by mhurd            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

/*
** Norm'd C codegolf was a mistkae
*/

void	e(int *a, int p[3], int *x)
{
	int i;
	int y;
	int z;

	i = p[0] - 1;
	while (++i < p[2] + 1)
		x[i] = a[i];
	y = p[0];
	z = p[1] + 1;
	i = p[0] - 1;
	while (++i < p[2] + 1)
	{
		if (y > p[1])
			a[i] = x[z++];
		else if (z > p[2] || x[y] < x[z])
			a[i] = x[y++];
		else
			a[i] = x[z++];
	}
}

void	r(int *a, int l, int h, int *x)
{
	int p[3];
	int m;

	if (l >= h)
		return ;
	m = l + (h - l) / 2;
	r(a, l, m, x);
	r(a, m + 1, h, x);
	p[0] = l;
	p[1] = m;
	p[2] = h;
	e(a, p, x);
}

void	s(int *a, int n)
{
	int *x;

	x = calloc(n, sizeof(0));
	r(a, 0, n - 1, x);
}

int		main(int c, char **v)
{
	int *a;
	int x;

	a = calloc(c - 1, sizeof(0));
	x = 0;
	while (++x < c)
		a[x - 1] = atoi(v[x]);
	s(a, c - 1);
	x = -1;
	while (++x < c - 1)
		printf("%d ", a[x]);
}
