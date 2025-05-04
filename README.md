# EdgeAI_FinalProject

# 🐤 "BIRD VOICE RECOGNITION WITH DEEP LEARNING MODELS ON ARDUINO 33 BLE SENSE"

# Team Member:
### 1- Shivam Dwivedi, SrNo- 23889, M.Tech AI- 
    - Data Collection - Asean Koel
    - Deep Neural Network model development
    - Report Preparation



### 2- Benjamin Debabarma, SrNo- 22554, M.Tech AI- 
    - Data Collection - Hen
    - Quantization and .tflite conversion
    - Power Point slides preparation
  


### 1- Arun, SrNo- 23037, M.Tech CSA- 
    - Data Collection - Crow
    - Model deployment on Edge device
    - Github repo formulation


### 1- Suraj Kisku, SrNo- 23019, M.Tech AI- 
   - Data Collection - Parakeet
   - Web dashboard development
   - Github repo formulation



Classifies bird calls (sparrow, crow, pigeon) + background using onboard mic and TensorFlow Lite Micro.


## 🚀 Features
- Real-time MFCC + inference on-device
- Quantized model (~<20KB RAM)
- Open-source, extendable with more species

## 📦 Folder Structure

- Bird_voice_classifiert/
│
├── `/Arduino/` – FFT and MFCC model codes and deployable aurdino model code
├── `/data/` – .WAV recordings (refer to the readme file inside dataset foled for detailed description)
└── `/model/` – deployable app.py
├── requirement.txt
├── PPT
└── report
└── readme.txt



## 🔧 Tools Used
- Arduino IDE + Arduino_TensorFlowLite
- TensorFlow (Python)
- PDM mic (onboard)
- Flask + Flask-SocketIO + Eventlet 


## Links:
- Demo Video Link: https://drive.google.com/drive/folders/1eOMqtQF8vd44R0bCNtAWpf3L7OouHOOJ?usp=drive_link 
 

## Acknowledgment 
- Prof Pandaraswamy Arjunan for hiw valuable guidance 
- [xeno-canto](https://xeno-canto.org/) — xeno-canto is a website dedicated to sharing wildlife sounds from all over the world. We have used their recordings to prepare this dataset.

- [Edge Impulse](https://edgeimpulse.com/) — Platform used to prepare and process the dataset.
