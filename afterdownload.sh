echo "Setting up ciphor.py to be executed from anywhere"
sudo cp ciphor.py /usr/bin
sudo chmod +x /usr/bin/ciphor.py
sudo cp rsaHex.py /usr/bin
sudo chmod +x /usr/bin/rsaHex.py

echo "Enabling ssh"
sudo systemctl enable ssh
sudo systemctl start ssh

echo "Enabling SPI and I2C"
sudo sed -i "/dtparam=spi=on/s/^#//g" /boot/config.txt
sudo sed -i "/dtparam=i2c_arm=on/s/^#//g" /boot/config.txt

sudo apt update
sudo apt install -y snapd
sudo snap install core
sudo snap install john-the-ripper
sudo pip3 install mfrc522

# Disabling WIFI
sudo ifconfig wlan0 down
