

Your pasted file has broken quotes — that's why GitHub shows error. The `"` inside code need escaping.

I fixed it. *Copy this CORRECT version — replace your file with this:*

Go to GitHub App > Open `SWID_Python_and_Git_Recap.ipynb` > Tap pencil ✏️ > Select All > Delete > Paste this fixed version > Commit:
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# SWID Python & Git Recap Portfolio\n",
        "Author: Pearl Chantal Nkeng Mbah | Douala, Cameroon\n",
        "Solavise Women in Data (SWID)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 1. Basic String Printing\n",
        "name = \"Pearl\"\n",
        "favourite_city = \"Cameroon\"\n",
        "print(name)\n",
        "print(favourite_city)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 2. Variables and f-string\n",
        "name = \"Pearl\"\n",
        "print(f\"My name is {name}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 3. Modulo and Comparison\n",
        "print(7 % 2)\n",
        "print(7 % 2 == 1)\n",
        "print(8 % 2 == 0)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 4. Arithmetic Operators\n",
        "a = 25\n",
        "b = 4\n",
        "print(f\"{a} + {b} = {a+b}\")\n",
        "print(f\"{a} - {b} = {a-b}\")\n",
        "print(f\"{a} * {b} = {a*b}\")\n",
        "print(f\"{a} / {b} = {a/b}\")\n",
        "print(f\"{a} // {b} = {a//b}\")\n",
        "print(f\"{a} % {b} = {a%b}\")\n",
        "print(f\"{a} ** {b} = {a**b}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 5. Type Conversion\n",
        "value = 3.99\n",
        "print(int(value))\n",
        "print(type(12))\n",
        "print(type(1.73))\n",
        "print(type(\"Hello\"))\n",
        "print(type(True))"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 6. String Slicing & Replace Upper\n",
        "text = \"data science\"\n",
        "print(text[0])\n",
        "print(text[-1])\n",
        "print(text[0:4])\n",
        "phrase = \"Hello Python\"\n",
        "print(phrase.replace(\"Python\", \"World\").upper())\n",
        "company = \"solavise tech\"\n",
        "print(company.replace(\"tech\", \"data\").upper())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 7. Conditional Architecture\n",
        "number = 15\n",
        "if number > 0:\n",
        "    print(\"Positive\")\n",
        "elif number < 0:\n",
        "    print(\"Negative\")\n",
        "else:\n",
        "    print(\"Zero\")\n",
        "score = 55\n",
        "if score >= 80:\n",
        "    print(\"You have an A\")\n",
        "elif score >= 70:\n",
        "    print(\"You have a B\")\n",
        "elif score >= 60:\n",
        "    print(\"You have a C\")\n",
        "elif score >= 50:\n",
        "    print(\"You have a D\")\n",
        "else:\n",
        "    print(\"Average! You can do better\")\n",
        "age = 20\n",
        "if age >= 18:\n",
        "    print(\"Adult\")\n",
        "else:\n",
        "    print(\"Minor\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "# 8. Python Lists\n",
        "cities = [\"Douala\", \"Yaoundé\", \"Garoua\", \"Bamenda\", \"Maroua\"]\n",
        "print(f\"First city: {cities[0]}\")\n",
        "print(f\"Last city: {cities[-1]}\")\n",
        "cities.append(\"Limbe\")\n",
        "cities.remove(\"Yaoundé\")\n",
        "print(cities)\n",
        "print(len(cities))"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.11.0"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 4
}
This one will render perfectly on GitHub. After you commit, paste your repo link here — I'll check it.



