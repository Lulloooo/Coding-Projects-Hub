# 📦 Order Processing Program 

### 🎯 Scope
This program has two different, yet related, main goals:

1️⃣ Reduce orders processing times by making straight forward the spare part preparation phase.  
2️⃣ Ease the custom and clearence operations on out-of-the-border orders by producing a report speeding up spare parts inspection & recognition.

### 🛠️ How it works
The program functioning is pretty elementary: once the user selects an invoice, it will proceed to display a "report" including a spare part's picture, its code, the quantity that must be added to the order and an interactive checkbox to tick when the product is added.  
To sum up, the main steps are:

1️⃣ The user is prompted to chose an invoice from is local environment once clicking the "select Invoice" button. 
2️⃣ The invoice is retrived and read.  
3️⃣ Products with codes that are within the column named "code" of the invoice will be added to the report.  
4️⃣ The program will retrieve from "img" folder the spare parts' pictures that match the codes in the "codes" column. **Note.** It is fundamental that spare parte pictures are named after their code (i.e A01 for product with code A01), in this way the program will match codes and picture.  
5️⃣ The Invoice "Quantity" column is read. To each spare parts will be assigned its corresponding quantity.  
6️⃣ A "Final Report" will open in a new window. It will include (in order) for every product: picture, code, quantity and interactive checkbox. The report will have a layout of 3x3 and it is intendend to be printed on an A4 paper.
7️⃣ In the new window, a "Save as pdf" button is displayed. By clicking on it, it will save the scrollable window from point 6. into a pdf file on the computer's desktop. This pdf-version should then be printed so the operator can carry it with itself while processing the order.




