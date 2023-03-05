

import cgi
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

def error_page(message):
    print("Content-type: text/html\n")
    print("<html>")
    print("<head><title>Error</title></head>")
    print("<body>")
    print("<h1>Error</h1>")
    print("<p>{}</p>".format(message))
    print("</body>")
    print("</html>")

def factor_page(n, factors):
    print("Content-type: text/html\n")
    print("<html>")
    print("<head><title>Factorization of {}</title></head>".format(n))
    print("<body>")
    print("<h1>Prime factorization of {}</h1>".format(n))
    if factors:
        print("<p>{0} = {1}</p>".format(n, " × ".join(str(f) for f in factors)))
    else:
        print("<p>{0} is prime.</p>".format(n))
    print("<form method='get' action='{}'>".format(cgi.escape("http://localhost/cgi-bin/td3")))
    print("<p>Enter a natural number: <input type='text' name='n'></p>")
    print("<p><input type='submit' value='Factorize'></p>")
    print("</form>")
    print("</body>")
    print("</html>")

def parse_query_string(query_string):
    query = cgi.parse_qs(query_string)
    if 'n' not in query:
        error_page("Missing 'n' parameter.")
        return None
    n = query['n'][0]
    try:
        n = int(n)
    except ValueError:
        error_page("Invalid 'n' parameter: not an integer.")
        return None
    if n <= 0:
        error_page("Invalid 'n' parameter: not a positive integer.")
        return None
    return n

def main():
    query_string = os.environ.get('QUERY_STRING', '')
    n = parse_query_string(query_string)
    if n is not None:
        factors = prime_factors(n)
        factor_page(n, factors)

if __name__ == '__main__':
    main()
