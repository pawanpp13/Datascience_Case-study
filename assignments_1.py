{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello from fun\n"
     ]
    }
   ],
   "source": [
    "#1.Write a program which contains one function named as Fun(). That function should display “Hello from Fun” on console.\n",
    "def Fun():\n",
    "   print(\"Hello from fun\")\n",
    "Fun()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input\n",
      "6\n",
      " Even number\n"
     ]
    }
   ],
   "source": [
    "#2.Write a program which contains one function named as ChkNum() which accept one\n",
    "#parameter as number. If number is even then it should display “Even number” otherwise display “Odd number” on console.\n",
    "def ChkNum(num):\n",
    "    if num%2==0:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "def main():\n",
    "    print('Input')\n",
    "    value=int(input())\n",
    "    var=ChkNum(value)\n",
    "    \n",
    "    if var==True:\n",
    "        print(\" Even number\")\n",
    "    else:\n",
    "        print(\" Odd number\")\n",
    "if __name__== \"__main__\":\n",
    "     main()\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter 1st number\n",
      "7\n",
      "Enter 2nd number\n",
      "8\n",
      "Addition is= 15\n"
     ]
    }
   ],
   "source": [
    "#3)Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.\n",
    "def Add(x,y):\n",
    "    return x+y   \n",
    "def main():\n",
    "    print(\"Enter 1st number\")\n",
    "    val1=int(input())\n",
    "    print(\"Enter 2nd number\")\n",
    "    val2=int(input())\n",
    "    var=Add(val1,val2)\n",
    "    print(\"Addition is=\",var)\n",
    "if __name__ == \"__main__\": \n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MARVELLOUS\n",
      "MARVELLOUS\n",
      "MARVELLOUS\n",
      "MARVELLOUS\n",
      "MARVELLOUS\n"
     ]
    }
   ],
   "source": [
    "#4)Write a program which display 5 times Marvellous on screen.\n",
    "def printname():\n",
    "    for i  in range(5):\n",
    "        print(\"MARVELLOUS\")\n",
    "\n",
    "printname()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n",
      "1\n",
      "end for loop\n"
     ]
    }
   ],
   "source": [
    "#5)Write a program which display 10 to 1 on screen.\n",
    "def Display():\n",
    "    i=0\n",
    "    for i in range(10,0,-1):\n",
    "        print(i)\n",
    "    else:\n",
    "        print(\"end for loop\")\n",
    "def main():\n",
    "    Display()\n",
    "    \n",
    "if __name__== \"__main__\":\n",
    "     main()  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the  number:-3\n",
      "Number is  negative\n"
     ]
    }
   ],
   "source": [
    "#6)Write a program which accept number from user and check whether that number is positive or negative or zero.\n",
    "def ChekNum(n):\n",
    "    if n>=0:\n",
    "        print(\"number is positive\")\n",
    "    elif n<=0:\n",
    "         print(\"number is negative\")\n",
    "    else:\n",
    "         print(\"number is zero\")\n",
    "x=(int(input(\"Enter the  number:\")))\n",
    "check_number(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter one number\n",
      "9\n",
      "9 number is not divisible\n"
     ]
    }
   ],
   "source": [
    "#7)Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.\n",
    "def divisible(no): \n",
    "    if no%5==0:   \n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "    \n",
    "def main():\n",
    "    print('Enter one number')\n",
    "    value=int(input())\n",
    "    \n",
    "    var=divisible(value)\n",
    "    \n",
    "    if var==True:\n",
    "        print(\"{} number is divisible\".format(value))\n",
    "    else:\n",
    "        print(\"{} number is not divisible\".format(value))\n",
    "if __name__== \"__main__\":\n",
    "     main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number\n",
      "5\n",
      "* * * * * "
     ]
    }
   ],
   "source": [
    "#8)Write a program which accept number from user and print that number of “*” on screen.\n",
    "def Pattern(x):\n",
    "     for i in range(x):\n",
    "            print(\"*\",end=\" \")\n",
    "def main():\n",
    "    print (\"Enter the number\")\n",
    "    x=int(input())\n",
    "    Pattern(x)\n",
    "if __name__== \"__main__\":\n",
    "     main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "even number\n"
     ]
    }
   ],
   "source": [
    "#9)Write a program which display first 10 even numbers on screen.\n",
    "def Display():\n",
    "    i=0\n",
    "    for i in range(0,11,2):\n",
    "        print(i)\n",
    "    else:\n",
    "        print(\"even number\")\n",
    "def main():\n",
    "    Display()\n",
    "    \n",
    "if __name__== \"__main__\":\n",
    "     main() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter  string marvellous\n",
      "Length of stirng= 10\n"
     ]
    }
   ],
   "source": [
    "#10)Write a program which accept name from user and display length of its name.\n",
    "def String_Length(x):\n",
    "          j=0\n",
    "          for i in x:\n",
    "                    j=j+1\n",
    "          print(\"Length of stirng=\",+j)\n",
    "\n",
    "x=input(\"Enter  string \")\n",
    "String_Length(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
