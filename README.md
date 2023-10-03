# Python Wifi Monitor

Want to record all wifi outages because your annoyed by your ISP? This code is for you!

I designed this code to run on a RaspberryPi, a 2 model B in my case. My setup is also using a 3.5 480x320 screen so there are some pieces speficially fo this screen size.

## Specific Steps

### Changing Font Size

To change the terminal font size, start with the command `sudo dpkg-reconfigure console-setup`. Select the option `UTF-8`, `Guess optimal character set`, `Terminus` then finally `8x16`.
This will take a moment to update, then you are good. If you receive the error `_curses.error: addwstr() returned ERR`, this means the screen is too small for the display.

### Install 3.5 LCD

To install the LCD code, use the following code

```bash
sudo rm -rf LCD-show
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show/
sudo ./LCD35-show
sudo ./LCD35-show 180 # flip screen 180 degree
```

For more details check out this [page](http://www.lcdwiki.com/3.5inch_RPi_Display).
