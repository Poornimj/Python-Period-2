from flask import Flask, request, jsonify

app = Flask(__name__)

def get_prime_factors(n):
    """Get all prime factors of n"""
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def is_prime(num):
    """Check whether a number is prime or not"""
    if num < 2:
        return False
    factors = get_prime_factors(num)
    unique_factors = set(factors)
    for factor in unique_factors:
        count = factors.count(factor)
        if count > 1:
            return False
    return True

@app.route('/prime_number/<int:number>', methods=['GET'])
def prime_check(number):
    """Check whether a number is prime or not"""
    result = {"Number": number, "isPrime": is_prime(number)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')