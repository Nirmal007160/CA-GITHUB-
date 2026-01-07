{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMtZlinpbn3GOEH85dzJbPr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Nirmal007160/CA-GITHUB-/blob/main/4.%20ANN%20using%20backpropagation.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "def sigmoid(x):\n",
        "    return 1 / (1 + np.exp(-x))\n",
        "\n",
        "def sigmoid_derivative(x):\n",
        "    return x * (1 - x)\n",
        "\n",
        "class NeuralNetwork:\n",
        "    def __init__(self, input_size, hidden_size, output_size):\n",
        "        self.weights_input_hidden = np.random.rand(input_size, hidden_size)\n",
        "        self.biases_hidden = np.zeros((1, hidden_size))\n",
        "        self.weights_hidden_output = np.random.rand(hidden_size, output_size)\n",
        "        self.biases_output = np.zeros((1, output_size))\n",
        "\n",
        "    def forward(self, inputs):\n",
        "        self.hidden = sigmoid(np.dot(inputs, self.weights_input_hidden) + self.biases_hidden)\n",
        "        self.output = sigmoid(np.dot(self.hidden, self.weights_hidden_output) + self.biases_output)\n",
        "        return self.output\n",
        "\n",
        "    def backward(self, inputs, targets, learning_rate):\n",
        "        output_error = targets - self.output\n",
        "        output_delta = output_error * sigmoid_derivative(self.output)\n",
        "\n",
        "        hidden_error = output_delta.dot(self.weights_hidden_output.T)\n",
        "        hidden_delta = hidden_error * sigmoid_derivative(self.hidden)\n",
        "\n",
        "        self.weights_hidden_output += self.hidden.T.dot(output_delta) * learning_rate\n",
        "        self.biases_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate\n",
        "        self.weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate\n",
        "        self.biases_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate\n",
        "\n",
        "    def train(self, inputs, targets, epochs, learning_rate):\n",
        "        for _ in range(epochs):\n",
        "            for i in range(len(inputs)):\n",
        "                self.forward(inputs[i:i+1])\n",
        "                self.backward(inputs[i:i+1], targets[i:i+1], learning_rate)\n",
        "\n",
        "    def predict(self, inputs):\n",
        "        return self.forward(inputs)\n",
        "\n",
        "# Example dataset (you can modify this as needed)\n",
        "inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])\n",
        "targets = np.array([[0], [1], [1], [0]])\n",
        "\n",
        "# Create and train the neural network\n",
        "neural_network = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)\n",
        "neural_network.train(inputs, targets, epochs=10000, learning_rate=0.1)\n",
        "\n",
        "# Test the neural network\n",
        "for i in range(len(inputs)):\n",
        "    prediction = neural_network.predict(inputs[i:i+1])\n",
        "    print(f\"Input: {inputs[i]}, Target: {targets[i]}, Prediction: {prediction}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3B_tilf3ifaO",
        "outputId": "ab29f7d7-81ff-4361-de50-a66765c319b4"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Input: [0 0], Target: [0], Prediction: [[0.06130112]]\n",
            "Input: [0 1], Target: [1], Prediction: [[0.94531063]]\n",
            "Input: [1 0], Target: [1], Prediction: [[0.94544531]]\n",
            "Input: [1 1], Target: [0], Prediction: [[0.05626587]]\n"
          ]
        }
      ]
    }
  ]
}