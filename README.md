Artificial Neural Network (ANN) with Tanh Activation

## 📌 Project Overview
This project implements a simple feedforward Artificial Neural Network (ANN) 
using the hyperbolic tangent (tanh) activation function.

The network architecture consists of:
- **2 Input neurons**
- **2 Hidden neurons**
- **2 Output neurons**
- Fully connected layers
- Random weight initialization in the range [-0.5, 0.5]
- Bias values:
  - Hidden layer bias (b1) = 0.5
  - Output layer bias (b2) = 0.7

---

## 🧠 Network Architecture

Input Layer (2 neurons)  
↓  
Hidden Layer (2 neurons, tanh activation)  
↓  
Output Layer (2 neurons, tanh activation)

---

## ⚙️ Mathematical Formulation

Hidden layer computation:

net_h = (X · W1) + b1  
h = tanh(net_h)

Output layer computation:

net_o = (h · W2) + b2  
output = tanh(net_o)
