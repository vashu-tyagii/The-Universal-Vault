# Python Fundamentals: Practice Sheet (30 Levels of Logic)

Yeh practice sheet un 9 core topics par based hai jo aapne abhi cover kiye hain: **Introduction, Applications, Input/Output, Variables, Operators, Keywords, Data Types, Conditional Statements, aur Loops**. Isme koi advanced data structures (Lists, Dicts, etc.) ya functions use nahi kiye gaye hain taaki aapka basic logic aur math foundation strong ho sake.

---

## 🟢 Easy Level (10 Questions)

*Basic syntax, Input/Output, Type Casting, simple If-Else, and basic Loops.*

1. **User Greeting & Type Check**
   * **Task:** User se unka name aur age `input()` lo. Age me $+5$ add karke print karo: `"In 5 years, <name> will be <age+5> years old."`
   * **Hint:** `input()` hamesha string deta hai, toh age ko `int()` mein convert karna mat bhoolna.

2. **Swap Variables**
   * **Task:** Do variables $a = 10$ aur $b = 20$ hain. Bina teesre variable (3rd variable) ke, inki values ko swap karo aur print karo.
   * **Hint:** Python ka multiple assignment syntax (`a, b = b, a`) use kar sakte ho.

3. **Simple Even/Odd**
   * **Task:** User se ek integer input lo aur check karo ki number Even hai ya Odd.
   * **Hint:** Modulus operator (`% 2`) ka use karke remainder check karo ki zero hai ya nahi.

4. **Temperature Converter**
   * **Task:** User se Celsius me temperature input lo aur use Fahrenheit me convert karo using formula: $F = (C \times 9/5) + 32$.
   * **Hint:** Input ko `float()` mein cast karna taaki decimal values accurate aayein.

5. **Simple Counter**
   * **Task:** `while` loop ka use karke 1 se lekar 20 tak saare numbers print karo.
   * **Hint:** Ek counter variable `i = 1` banao aur loop me `i += 1` chalate jao jab tak `i <= 20` ho.

6. **Table Generator**
   * **Task:** User se ek number input lo aur `for` loop ka use karke us number ki multiplication table (1 se 10 tak) print karo.
   * **Hint:** `for i in range(1, 11):` loop ke andar `num * i` print karo.

7. **Find the Maximum**
   * **Task:** Teen (3) numbers user se input lo aur `if-elif-else` conditions ka use karke sabse bada (maximum) number print karo.
   * **Hint:** Nested `if` ya `and` operator ka use karke comparisons karo (`a > b and a > c`).

8. **Simple Interest Calculator**
   * **Task:** User se Principal ($P$), Rate ($R$), aur Time ($T$) float inputs lo aur Simple Interest calculate karke output do: $SI = (P \times R \times T) / 100$.
   * **Hint:** Saare inputs ko `float()` mein lena zaroori hai.

9. **Leap Year Checker**
   * **Task:** Input year lo aur check karo ki wo leap year hai ya nahi.
   * **Hint:** Condition: `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`.

10. **Print Square Pattern**
    * **Task:** User se number $N$ input lo aur $N \times N$ ka `*` (asterisk) grid print karo nested loops se.
    * **Hint:** Outer loop row ke liye aur inner loop column ke liye `end=" "` ke sath `print("*")` use karega.

---

## 🟡 Medium Level (10 Questions)

*Nested Loops, Bitwise & Logical Operators, Complex Conditions, and Mathematical Logic.*

 1. **Reverse a Number**
    * **Task:** User se ek integer lo (e.g., `1234`) aur arithmetic operations (`%` aur `//`) aur loop ka use karke use reverse karo (`4321`). *String conversion forbidden!*
    * **Hint:** `rev = rev * 10 + num % 10` aur `num //= 10` logic ko `while num > 0` tak run karo.

 2. **Sum of Digits**
    * **Task:** User se ek number input lo aur uske saare digits ka sum calculate karo loop se. (e.g., $125 \rightarrow 1 + 2 + 5 = 8$).
    * **Hint:** Har iteration mein last digit nikalne ke liye `% 10` aur number chota karne ke liye `// 10` use karo.

 3. **Prime Number Check**
    * **Task:** User se ek number input lo aur check karo ki wo Prime hai ya Composite.
    * **Hint:** 2 se lekar `number - 1` tak loop chalao; agar kisi se bhi divide ho jaye toh prime nahi hai.

 4. **Fibonacci Series**
    * **Task:** User se $N$ input lo aur pehle $N$ terms ki Fibonacci series print karo (`0, 1, 1, 2, 3, 5, 8...`).
    * **Hint:** Do variables `a, b = 0, 1` rakho, aur loop me `a, b = b, a + b` update karte jao.

 5. **Factorial Calculator**
    * **Task:** `while` loop ka use karke kisi number ka Factorial ($N!$) calculate karo.
    * **Hint:** Ek accumulator variable `fact = 1` rakho aur loop mein `fact *= i` karo.

 6. **Count Digits in an Integer**
    * **Task:** User se ek integer input lo aur loop se count karo ki usme kitne total digits hain.
    * **Hint:** Jab tak `num > 0`, number ko `// 10` se reduce karte jao aur ek counter `count += 1` badhate jao.

 7. **Divisible by 3 and 5 but not both**
    * **Task:** 1 se 100 tak ke numbers me se wahi numbers print karo jo ya toh 3 se divisible ho YA 5 se, lekin **dono se ek saath divisible Na ho**.
    * **Hint:** `(i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0)` condition use karo (ya XOR operator `^`).

 8. **Right-Angled Triangle Pattern**
    * **Task:** Nested `for` loop ka use karke right-angled triangle pattern print karo for $N=5$.
    * **Hint:** Outer loop `i` ranges from 1 to $N+1$, inner loop ranges from 1 to `i+1`.

 9. **Calculate Power without `**` Operator**
    * **Task:** User se `base` aur `exponent` input lo aur loop ka use karke $base^{exponent}$ calculate karo (`**` ya `pow()` use nahi karna hai).
    * **Hint:** Result variable ko `1` se initialize karo aur `exponent` times loop chala kar multiply karte jao.

10. **Sum of Even Numbers in Range**
    * **Task:** User se start aur end number lo, aur unke beech ke saare Even numbers ka sum print karo.
    * **Hint:** Loop chala kar `if i % 2 == 0:` check karo aur sum variable mein add karo.

---

## 🔴 Hard Level (10 Questions)

*Tricky mathematical logic, Deep Nested Loops, Optimization, Bitwise tricks, Edge-case debugging.*

 1. **Armstrong Number**
    * **Task:** Check karo ki input integer Armstrong Number hai ya nahi using loops & math operations. (E.g., $153 \rightarrow 1^3 + 5^3 + 3^3 = 153$).
    * **Hint:** Pehle total digits count karo (power ke liye), fir har digit ki power nikal kar sum mein add karo.

 2. **Palindrome Number**
    * **Task:** Check karo ki koi number Palindrome hai ya nahi (e.g., $1221 \rightarrow 1221$). *Pure math logic se solve karo.*
    * **Hint:** Original number ko store karke, Q11 ki tarah number ko reverse karo aur check karo ki reverse original ke barabar hai ya nahi.

 3. **Diamond Star Pattern**
    * **Task:** Nested loops ka use karke $N=5$ ke liye centered Diamond pattern render karo.
    * **Hint:** Isko do parts mein todo—pehle upper pyramid (increasing stars), fir lower inverted pyramid (decreasing stars).

 4. **GCD (HCF) of Two Numbers**
    * **Task:** Euclidean algorithm ya simple reduction loop ka use karke do inputs ka Greatest Common Divisor (GCD) nikalo.
    * **Hint:** `while b != 0:` loop chalao aur `a, b = b, a % b` update karo; jab `b == 0` ho toh `a` GCD hoga.

 5. **LCM of Two Numbers**
    * **Task:** Do numbers ka Least Common Multiple (LCM) nikalo.
    * **Hint:** Formula use karo: `LCM = (num1 * num2) // GCD(num1, num2)`.

 6. **Pyramid Number Pattern**
    * **Task:** Nested loops ka use karke symmetric number pyramid print karo:

      ```text
          1
         121
        12321
       1234321
      ```

    * **Hint:** Spaces ke liye aur ascending/descending numbers print karne ke liye alag-alag inner loops lagenge.

 7. **Binary to Decimal Conversion**
    * **Task:** User se binary number (e.g., `1011`) input lo aur pure mathematical loop se usko Decimal integer ($11$) me convert karo.
    * **Hint:** `% 10` se digit nikalo, use `2 ** power` se multiply karke sum mein add karo, fir `// 10` aur power increment karo.

 8. **Find All Prime Numbers in a Range**
    * **Task:** User se `start` aur `end` range lo aur unke beech ke **saare prime numbers** print karo using nested loops.
    * **Hint:** Range ke har number ke liye ek nested loop chalao jo check kare ki wo prime hai ya nahi.

 9. **Bitwise Parity & Power of 2 Check**
    * **Task:** Bina direct arithmetic operators (`+`, `-`, `*`, `/`) ke, sirf **Bitwise Operators** (`&`, `|`, `^`, `<<`, `>>`) ka use karke check karo ki koi given number $N$ Power of 2 hai ya nahi.
    * **Hint:** Classic bitwise trick: `(n & (n - 1) == 0)` aur `n > 0` check karo.

10. **Collatz Conjecture Simulation**
    * **Task:** User se positive integer $N$ lo. Agar $N$ Even hai toh $N = N // 2$, agar $N$ Odd hai toh $N = 3 \times N + 1$. Is process ko repeat karo jab tak $N$ 1 na ho jaye. Total kitne steps lage, print karo.
    * **Hint:** `while n != 1:` loop chalao, andar `if-else` condition se $N$ update karo, aur ek step counter maintain karo.
