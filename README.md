## For Linux
1. Install Google Chrome
   ```sh
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   sudo apt-get update
   sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
   rm google-chrome-stable_current_amd64.deb
   ```
2. Verify Installation
   ```sh
   google-chrome --version
   ```
3. Download ChromeDriver<br>
   Go to https://googlechromelabs.github.io/chrome-for-testing/ and check for the version matching the `google-chrome` version, if `not found` then download the closest version. 

   Use the below command to download :
   ```sh
   wget https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.141/linux64/chromedriver-linux64.zip
   ```
   `Replace the link with actual link`

 4. After downloadig the ChromeDriver, unzip the `chromedriver-linux64.zip` file.<br>
    ```sh
    unzip chromedriver-linux64.zip
    ```

    If showing `Unzip : command not found` then first install it via :
    ```sh
    sudo apt install zip unzip
    ```

 5.  From the `chromedriver-linux64` directory, move the `chromedriver` to `/usr/local/bin/`<br>

     ```sh
     sudo mv ~/chromedriver-linux64/chromedriver /usr/local/bin/
     ```
     To confirm its working, use :
     ```sh
     chromedriver --version
     ```
