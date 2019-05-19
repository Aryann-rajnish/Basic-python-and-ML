def fib(n):
 f = 0*[n+1]
 f[1] = 1
 for i in Xrange (2 , n+1):
    f[i] = f[i-1]+f[i-2]
    return f[n]
def main():
 n = 10;
 print "The fibonacci number of n:",fib(n)
 def __name__ == "__main__":
  main()
