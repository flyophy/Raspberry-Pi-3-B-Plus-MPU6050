# Raspberry-Pi-3-B-MPU6050
Raspberry Pi 3 B+ /MPU6050 

![MPU-6050](https://user-images.githubusercontent.com/47052707/70082539-b1bb6d80-161b-11ea-968c-b7c2ae625b00.jpg)

![srdtfyg](https://user-images.githubusercontent.com/47052707/70082768-25f61100-161c-11ea-8289-255e15617e2a.png)

![02](https://user-images.githubusercontent.com/47052707/70083692-f6480880-161d-11ea-92ce-8a6ad73f9eaa.png)


##KURULUM

$ sudo apt-get update

$ sudo apt-get upgrade

$ sudo python setup.py install

I2C'yi etkinleştiriniz.(Ayarlardan)

I2C adresleri sayfasını listeleyelim ve slave olarak çalışacak MPU6050 kaçıncı adreste onu tespit edelim.

sudo i2cdetect -y 1     (Slave cihazları listelemek için komut satırına giriniz.)

LİSTELEME ÖRNEĞİ 

![01](https://user-images.githubusercontent.com/47052707/70083547-a49f7e00-161d-11ea-899e-bf7ae217924a.png)

git clone https://github.com/gadgetsky/Raspberry-Pi-3-B-Plus-MPU6050.git

cd Raspberry-Pi-3-B-Plus-MPU6050

chmod +x MPU6050.py

python3 MPU6050.py


