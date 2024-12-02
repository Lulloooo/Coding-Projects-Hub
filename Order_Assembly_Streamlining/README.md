# 📦 Order Processing & Assembly Streamlining Program 
📩
<a href="mailto:lucagabri98@live.it"><img src="https://img.shields.io/badge/lucagabri98-c71610?style=flat&logo=gmail&logoColor=white" width="80"></a>
<a href="la-databizanalyst"><img src="https://img.shields.io/badge/%40LA-0E76A8?style=flat&logo=linkedin&logoColor=white" width="45"></a>
📩

## 🎯 PURPOSES
This coding-project has two different, yet related, main goals:

&nbsp;&nbsp;1️⃣ Reduce orders processing times by making straight forward the assembly phase.  
&nbsp;&nbsp;2️⃣ Ease the custom and clearence operations for out-of-the-border orders by producing a report speeding up spare parts inspection & recognition through products' pictures.

## 🛠️ WORKFLOW
The worfklow is pretty straightforward: user selects an invoice, the program proceeds to display a "report" including a spare part's picture, its code, the quantity that must be added to the order and an interactive checkbox. The checbox can be ticked, and should be ticked when the user phisically adds that specific product to the order's shipping package. Finally, when all the checkboxes are marked, an "Order is ready" notification pops up. This means the order is all set for shipping.  
🔎 In details, the workflow is as follows:

&nbsp;&nbsp;1️⃣ The user opens the program. The image_display_window will pop up.  
&nbsp;&nbsp;2️⃣ Once the user clicks the "Select Invoice" button, their are prompted to choose and invoice from their local enviroment. Note the invoice can be either in a .pdf or .xlsm/xls format.  
&nbsp;&nbsp;3️⃣ The invoice is retrived and read.  
&nbsp;&nbsp;4️⃣ Goods which code is included in the Invoice's column "Model" are added to the report. A list storing Model and relative quantity for all the product is made.  
&nbsp;&nbsp;5️⃣ The column "quantity" is read too. As such, to each product is assigned its relative quantity.  
&nbsp;&nbsp;6️⃣ A list storing Model along with the relative quantity for all the products is built.  
&nbsp;&nbsp;7️⃣ The program browse the "product_img" folder looking for the goods' picture that match the model in the list created in point 6. **Note** Spare part pictures must be named after their code (ex. A01 must be the name for the A01 img). This way The program is able to match codes with pics.  
&nbsp;&nbsp;8️⃣ The "product_display_window" opens. For each product, it includes (in order): picture, code, quantity and an interactive checbox. The windows has a 3x3 layout and has a "Save as pdf" button on the bottom. **Note** The windows strecthed the img proportion if windows' dimensions are changed.  
&nbsp;&nbsp;9️⃣ The checkboxes are interactive, meaning they can be ticked. The program keeps record for checkboxes, i.e if one is ticked, the "product_display_window" is closed and then re-opened the ticked checkboxes will appear as ticked.  
&nbsp;&nbsp;1️⃣0️⃣ By clicking the "Save as PDF" button, a .pdf file mimicking the "product_display_window" is saved on the desktop. The .pdf keeps the checkboxes status. This file is for printing purposes, so the users can move around with the actual papers while processing the order.  
&nbsp;&nbsp;1️⃣1️⃣ Once the user ticks all the checkboxes and closes the "product_display_window", a message showing that the "order is ready" will pop-up.  

A visual workflow can be found in the "Program_workflow_visual" file. 

## ⚠️ WARNINGS 
### ➕ MUST DO before the first run
Before running the app, there is some customization to do. **Note** By right-clicking on the icon, the user will get to the resources' folder of the app.  
What the user MUST DO before running the app for the first time:

* **Logo**: Store the logo as "logo.jpg" in the "supp_img" folder.
* **Products' pictures**: Pictures of the various products must be added to the folder "product_img".  
&nbsp;&nbsp;&nbsp;&nbsp; - **Note:** A product's picture MUST be named after the name it is usually given in the invoice's "Model" column followed by the .jpg extensions (ex. A01.jpg)(At the moment the program support just .jpg format).

### 🔝 ENSURING PEAK PERFORMANCES
To be sure the program runs as smooth as it can, check the following details:  
* **Logo**:  
&nbsp;&nbsp;&nbsp;&nbsp; - **Format**: At the moment, the only accepted format is .jpg. (Further formats support will be available soon).  
&nbsp;&nbsp;&nbsp;&nbsp; - **Dimensions**: Width 1359 x Height 319  
* **Product Pictures**:  
&nbsp;&nbsp;&nbsp;&nbsp; - **Naming**: Name the pic after the name used in the Invoice "Model" column.  
&nbsp;&nbsp;&nbsp;&nbsp; - **Format**: At the moment, the only accepted format is .jpg. (Further formats support will be available soon).  
&nbsp;&nbsp;&nbsp;&nbsp; - **Dimensions**: Width 53 x Height 72  
&nbsp;&nbsp;&nbsp;&nbsp; - **Layout**: An example of the ideal layout is shown in the "product_image_template".
* **Invoice**:  
&nbsp;&nbsp;&nbsp;&nbsp; - **Naming**: No rules, just name it with the usual firm's policy.  
&nbsp;&nbsp;&nbsp;&nbsp; - **Format**: Accepted formats are: pdf, xlsm, xls.  
&nbsp;&nbsp;&nbsp;&nbsp; - **Layout**: The same as the one showed in the "Invoice_template" file. If needed, an xlsm template can be provided upon request.    
* **Invoice PDF Output**: this is the file resulting from clicking the "Save as pdf" button:  
&nbsp;&nbsp;&nbsp;&nbsp; - **Storing**: Desktop.  
&nbsp;&nbsp;&nbsp;&nbsp; - **Naming**: The .pdf file will have the same name of the Inovce + "_parts.pdf".  
&nbsp;&nbsp;&nbsp;&nbsp; - **Layout**: The invoiceName_parts.pdf file shows the final layout for the .pdf file.

## 🗂️ REPO'S DESCRIPTION
This folder comprise all the material regarding a coding project I did for a manufacturing firm.
In this repository it can be found (not considering this ReadMe):  

&nbsp; &nbsp; &nbsp; &nbsp; 1️⃣. a .py file that is the complete code snipped.  
&nbsp; &nbsp; &nbsp; &nbsp; 2️⃣. An "App_and_exe" folder containing the code already wrapped both for iOS and WIndows.  
&nbsp; &nbsp; &nbsp; &nbsp; 3️⃣. A "templates&canvas" folder showing the app windows and the optimal layout for the input documents (as referenced above).  
&nbsp; &nbsp; &nbsp; &nbsp; 4️⃣. A "supp_img" folder including the images used in the program's aesthetic (as the logo).  
&nbsp; &nbsp; &nbsp; &nbsp; 5️⃣. A "product_img" folder where the image of the product should be added.  
&nbsp; &nbsp; &nbsp; &nbsp; 6️⃣. A "icon" folder contains the icns file for the app.  
&nbsp; &nbsp; &nbsp; &nbsp; 7️⃣. A .json file storing data about checkboxes status (ticked/unticked).  
&nbsp; &nbsp; &nbsp; &nbsp; 8️⃣. A .txt file showing all the .py packages needed to let the code work.  


## 📪 GET IN TOUCH
Feel free to reach out for suggesting changes and improvements. I'll be happy to chat about it and implement them. 💬  
Be sure to let me know if you plan to employ this program and cite me whenever you use it. 🖋️  
<a href="mailto:lucagabri98@live.it"><img src="https://img.shields.io/badge/lucagabri98-c71610?style=flat&logo=gmail&logoColor=white" width="80"></a>
<a href="la-databizanalyst"><img src="https://img.shields.io/badge/%40LA-0E76A8?style=flat&logo=linkedin&logoColor=white" width="45"></a>

**Note**: Any work-related projects has been approved for posting, and all sensitive information and data are omitted to protect privacy. Projects containing sensitive data has not been posted. 



