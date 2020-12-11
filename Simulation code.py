import numpy as np
import math
import matplotlib.pyplot as plt



def plotting():                                                         # Graph plotting 
    
    plt.xlim(0, T)
    plt.xticks(np.linspace(0, T, 11))
    plt.ylim(-1, 1)
    plt.yticks(np.linspace(-1, 1, 11))
  
    plt.xlabel('Time')
    plt.title('Simulation - Prime Numbers and Brownian Motion')
    
    plt.axhline(0, linewidth = 0.8, linestyle = '--', color='black')
    plt.grid(color='grey', linestyle='--', linewidth = 0.2)

    x = np.linspace(0, T, time_steps+1)                                 # x-coordinates
    y = BM_primedivisors                                                # y-coordinates
   
    plt.plot(x, y, 'tab:red')
    
    plt.show()
   



def BMSimuation(N, primes, T, time_steps, delta_t):                     # Path simulation
    
    sample_size = 20
    samples = np.random.randint(2, N, sample_size)
    BM_values = [0]

    for i in range(1, time_steps+1):
        
        time = delta_t * i                                             
        bound = math.exp(math.log(N)**time)
        value = 0 
        
        for p in primes:
            if p <= bound:
                for n in samples:
                    if n % p == 0:
                        value += 1-1/p
                    else:
                        value += -1/p
            else:
                break

        value /= sample_size * math.sqrt(math.log(math.log(N)))
        BM_values.append(round(value, 4))
        
    return BM_values



def PrimeList(N):                                     # Generate primes that less than N
    
    prime_list = []
    
    for n in range(2, N+1):
        is_prime = True
        for p in prime_list:
            if n % p == 0:
                is_prime = False
                break
            elif p > math.sqrt(n):
                break
        if is_prime:
            prime_list.append(n)
   
    return prime_list





# Main program

'''
This program is a simulation of Billingsley's result [Prime Numbers and Brownian Motion, pg. 1108-1114].
In the following, We shall use the function 
    f(n) = 1/sqrt(log log N) * sum_{p <= e^((log N)^t)} dirac_p(n) - 1/p,
where p is a prime number and n is an integer sample in the range [2, N], to generate relevant Brownian Motion paths.

Set-up:

N                       Integer

T                       Time
time_steps              Number of time steps
delta_t                 Difference between two time steps
       
'''

N = 1000000
primes = PrimeList(N)                                                               # List of prime numbers that not greater than N

T = 1 
time_steps = 10
delta_t = T / time_steps

BM_primedivisors = BMSimuation(N, primes, T, time_steps, delta_t)                   # Generated Brownian Motion path  

plotting()