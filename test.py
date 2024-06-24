{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f259e96f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-100\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "def sub(a,b):\n",
    "    print(a-b)\n",
    "sub(100,200)\n",
    "sub(200,100)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "26a1756a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello jay good morning\n",
      "hello jay good morning\n"
     ]
    }
   ],
   "source": [
    "def wish(name,msg):\n",
    "    print(\"hello\",name,msg)\n",
    "wish(name=\"jay\",msg=\"good morning\")\n",
    "wish(msg=\"good morning\",name=\"jay\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "54b1dc9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello jay good morning\n",
      "hello guest good morning\n"
     ]
    }
   ],
   "source": [
    "def wish(name=\"guest\"):\n",
    "    print(\"hello\",name,\"good morning\")\n",
    "wish(\"jay\")\n",
    "wish()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "762ba739",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the sum= 10\n",
      "the sum= 10\n",
      "the sum= 30\n",
      "the sum= 10\n",
      "the sum= 30\n",
      "the sum= 60\n",
      "the sum= 100\n"
     ]
    }
   ],
   "source": [
    "def sum(*n):\n",
    "    total=0\n",
    "    for n1 in n:\n",
    "        total=total+n1\n",
    "        print(\"the sum=\",total)\n",
    "sum()\n",
    "sum(10)\n",
    "sum(10,20)\n",
    "sum(10,20,30,40)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9e573290",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter no of rows4\n",
      "0 1 1 2 "
     ]
    }
   ],
   "source": [
    "n=int(input(\"enter no of rows\"))\n",
    "n1=0\n",
    "n2=1\n",
    "print(n1,n2,end=\" \")\n",
    "while(n-2)!=0:\n",
    "    n3=n1+n2\n",
    "    n1=n2\n",
    "    n2=n3\n",
    "    print(n3,end=\" \")\n",
    "    n=n-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "99e2fef0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the factorial of 1 is : 1\n",
      "the factorial of 2 is : 2\n",
      "the factorial of 3 is : 6\n",
      "the factorial of 4 is : 24\n"
     ]
    }
   ],
   "source": [
    "def fact(num):\n",
    "    result=1\n",
    "    while num>=1:\n",
    "        result=result*num\n",
    "        num=num-1\n",
    "    return result\n",
    "for i in range(1,5):\n",
    "    print(\"the factorial of\",i,\"is :\",fact(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "0bb9cafe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "123\n",
      "123\n"
     ]
    }
   ],
   "source": [
    "a=123\n",
    "def fun1():\n",
    "    print(a)\n",
    "def fun2():\n",
    "    print(a)\n",
    "fun1()\n",
    "fun2()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "f35d0bee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "23\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'b' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_3040/4294465711.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mf1\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mf2\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_3040/4294465711.py\u001b[0m in \u001b[0;36mf2\u001b[1;34m()\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0mf2\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[0mf1\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[0mf2\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'b' is not defined"
     ]
    }
   ],
   "source": [
    "def f1():\n",
    "    b=23\n",
    "    print(b)\n",
    "def f2():\n",
    "    print(b)\n",
    "f1()\n",
    "f2()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "24ec9fcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "123\n",
      "123\n",
      "23\n"
     ]
    }
   ],
   "source": [
    "a=123\n",
    "def fun1():\n",
    "    global b\n",
    "    b=23\n",
    "    print(a)\n",
    "def fun2():\n",
    "    print(a)\n",
    "    print(b)\n",
    "fun1()\n",
    "fun2()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "58f4a49d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "345\n",
      "50\n"
     ]
    }
   ],
   "source": [
    "a=50\n",
    "def f1():\n",
    "    a=345\n",
    "    print(a)\n",
    "    print(globals()['a'])\n",
    "f1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "ccedc20f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "coffee is prepared\n"
     ]
    }
   ],
   "source": [
    "def home():\n",
    "    x=\"coffee powder\"\n",
    "    x1=x\n",
    "    if x in x1:\n",
    "         print(\"coffee is prepared\")\n",
    "    else:\n",
    "        print(\"coffee is not prepared\")\n",
    "home()        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "fa590cd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "juice is prepared\n"
     ]
    }
   ],
   "source": [
    "def home():\n",
    "    x=\"mango juice\"\n",
    "    x1=x\n",
    "    if x in x1:\n",
    "         print(\"juice is prepared\")\n",
    "    else:\n",
    "        print(\"juice is not prepared\")\n",
    "home()        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a757f82",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
