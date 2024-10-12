# 📦 Order Processing Program 

### 🎯 Purpose
This program has two different, yet related, main goals:

1️⃣ Reduce orders processing times by making straight forward the spare part preparation phase.  
2️⃣ Ease the custom and clearence operations on out-of-the-border orders by producing a report speeding up spare parts inspection & recognition.

### 🛠️ How it works
The program functioning is pretty elementary: once the user selects an invoice, it will proceed to display a "report" including a spare part's picture, its code, the quantity that must be added to the order and an interactive checkbox to tick when the product is added.  
To sum up, the main steps are:

&nbsp;&nbsp;1️⃣ The user is prompted to chose an invoice from is local environment once clicking the "select Invoice" button. 
&nbsp;&nbsp;2️⃣ The invoice is retrived and read.  
&nbsp;&nbsp;3️⃣ Products with codes that are within the column named "code" of the invoice will be added to the report.  
&nbsp;&nbsp;4️⃣ The program will retrieve from "img" folder the spare parts' pictures that match the codes in the "codes" column. **Note.** It is fundamental that spare parte pictures are named after their code (i.e A01 for product with code A01), in this way the program will match codes and picture.  
&nbsp;&nbsp;5️⃣ The Invoice "Quantity" column is read. To each spare parts will be assigned its corresponding quantity.  
&nbsp;&nbsp;6️⃣ A "Final Report" will open in a new window. It will include (in order) for every product: picture, code, quantity and interactive checkbox. The report will have a layout of 3x3 and it is intendend to be printed on an A4 paper.
&nbsp;&nbsp;7️⃣ In the new window, a "Save as pdf" button is displayed. By clicking on it, it will save the scrollable window from point 6. into a pdf file on the computer's desktop. This pdf-version should then be printed so the operator can carry it with itself while processing the order.  
&nbsp;&nbsp;(8️⃣) Once the operator ticks all the checkboxes, the program will send an "order is ready" notification to the central administration. (this feature is not yet implemented).

### ➕ To be added (during the first run)
Before running the program, files path should be changes based on the computer it will run on. All of the path below should be defined during the program first run:
* logo path: define where the firm's logo is stored
* img path: define the folder where images are stored. Note: name the product picture after the name they have within the invoices.
* save path: define where pdf saved should be placed.
(coming soon):
* sending e-mail: e-mail from where "order is ready" will be sent
* receiving e-mail: e-mail that will receive the message "order is ready".






