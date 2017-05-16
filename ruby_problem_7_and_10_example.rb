require "benchmark"


def is_prime?(n)
  #these guys don't play by the rules
  if n == 0 || n == 1
    return "prime"
  end

  array_of_factors = []
  for i in (1..n)

    if n % i == 0
      array_of_factors << i
    end
  end
  if array_of_factors.length == 2
    return "prime"
  else
    return "not prime"
  end
end

def improved_is_prime?(n)
  #these guys don't play by the rules
  if n == 0 || n == 1
    return "prime"
  end

  array_of_factors = []
  for i in (1..Math.sqrt(n).ceil + 1)

    if n % i == 0
      array_of_factors << i
    end
  end
  if array_of_factors.length == 1
    #puts array_of_factors
    return "prime"
  else
    #puts array_of_factors
    return "not prime"
  end
end




n = 100000000
time = Benchmark.realtime do
  puts "#{n} is #{is_prime?(n)}."
end
puts "Our original method took #{time*1000} milliseconds"

time = Benchmark.realtime do
  puts "#{n} is #{improved_is_prime?(n)}."
end
puts "Our improved method took #{time*1000} milliseconds"
