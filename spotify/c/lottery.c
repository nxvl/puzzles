/*
 * Solves: http://www.spotify.com/es/jobs/tech/ticket-lottery/
 * Author:
 *     Nicolas Valcarcel <nvalcarcel@gmail.com>
 */

#include <stdio.h>

int get_needed_winners(int* t, int* p)
{
    int ret;
    if (*t >= *p) {
        return 1;
    } else if (*p % *t == 0) {
        return *p / *t;
    } else {
        return (*p / *t) + 1;
    }
}

long int get_bc(int a,int b)
{
    /*
     * Binomial Coefficient
     * http://en.wikipedia.org/wiki/Binomial_coefficient
     */
    long int ret = 1;
    int i = 1;

    if (b > (a - b)){
        b = a - b;
    }

    for (i; i <= b; i++) {
        ret *= a - (b - i);
        ret /= i;
    }

    return ret;
}

float get_probability(int* m, int* n, int* p, int* x)
{
    /*
     * http://en.wikipedia.org/wiki/Binomial_coefficient
     */
    float a = 0.0;
    int i = *x;
    for (i; i <= *p; i++ ){
        a += (float)(get_bc(*p, i) * get_bc(*m - *p, *n - i)) / (float)(get_bc(*m, *n));
    }

    return a;
}

int main()
{
    int m, n, t, p, x;

    scanf("%i %i %i %i", &m, &n, &t, &p);
    x = get_needed_winners(&t, &p);
    printf("%f\n", get_probability(&m, &n, &p, &x));


    return 0;
}
