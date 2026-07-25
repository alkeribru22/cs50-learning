"""
name = input("What is your name? ").strip().title().split()

print(f"Hello, {name}")

#.      second section

x = float(input("add a number: "))
y = float(input("add a number: "))

#z = round(x / y, 2)
z = x / y

print(f"{z:.2f}")


#       Third section

def hello(to="world"):
    print("hello,", to)

hello()
name = input("what is your name? ")
hello(name)



#         Fourth section

def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n, 2)

main()

"""

# Watching classes doesn't mean you'll understand everything.

# In my case, I first watch the class, then I write the code myself and analyse it.

# After reviewing my code, I come up with a lot of questions, so I watch the class again.

# In the last code, I didn't understand `return`, so I used GPT to help me understand it.

# My point is, you need to write the code on your own to truly understand it.

#  If you get stuck, use GPT or another AI chatbot for help.

