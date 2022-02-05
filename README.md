# Discord_PB_Yoinker-GUI
**First** look at my other [projekt](https://github.com/WendelinH/Discord_PB_Yoinker) and install all libraries and configurathe Discord. After you did that you can come back.

## Install libraries
```
pip install pickle
pip install requests
pip install pyqt5
```

## How to use the GUI

There is a table in which the individual users can be seen and with one click you can see their profile picture on the right.

![image](https://user-images.githubusercontent.com/94523690/152661479-319d1d5c-1b06-4589-b27d-cd3c2171f1c5.png)

Clicking on "New" opens a dialog window. In this window you have to enter the DiscordID and then click on "Get PB-Link".

![image](https://user-images.githubusercontent.com/94523690/152661508-3ec88588-de7f-4420-ac20-363cee6aae85.png)

After the link to the user's profile picture has been retrieved from the web, the picture appears very large.
The user can then be saved in the table by clicking on "Save".

![image](https://user-images.githubusercontent.com/94523690/152661528-2f7d0652-2532-4d77-928c-3edadc4be70c.png)

Here you can see how the user is stored in the table.

![image](https://user-images.githubusercontent.com/94523690/152661549-d31b1321-87b8-4ba2-8c2e-676ab90e7934.png)

In this picture you can see that the "Test 2" user was deleted by clicking on him in the table and then on the "Delete" button.

![image](https://user-images.githubusercontent.com/94523690/152661565-6b5f0ffc-5121-4c98-924b-6646d17d5960.png)

When you click on the "Save" button you save the table in a file called "tblDataList.dat". And this file is always read in when the GUI is started.

![image](https://user-images.githubusercontent.com/94523690/152661580-b5dcde05-9cd6-4abb-b734-dd1c3e227c5e.png)
