{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNWGq89eRud4PG1Cs3UBKH2",
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
        "<a href=\"https://colab.research.google.com/github/Nirmal007160/CA-GITHUB-/blob/main/2.%20Candidate%20elimination.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import copy\n",
        "\n",
        "def initialize_hypotheses(n):\n",
        "    hypotheses = []\n",
        "    specific_hypothesis = ['0'] * n\n",
        "    general_hypothesis = ['?'] * n\n",
        "    hypotheses.append(specific_hypothesis)\n",
        "    hypotheses.append(general_hypothesis)\n",
        "    return hypotheses\n",
        "\n",
        "def candidate_elimination(training_data):\n",
        "    num_attributes = len(training_data[0]) - 1\n",
        "    hypotheses = initialize_hypotheses(num_attributes)\n",
        "\n",
        "    # Note: The original candidate_elimination implementation provided has significant logical flaws\n",
        "    # that would prevent it from correctly implementing the Candidate Elimination algorithm, particularly\n",
        "    # in how it handles specific and general hypotheses and the early return statement.\n",
        "    # The primary goal here is to fix the IndentationError to make the code runnable, while preserving\n",
        "    # the original (logically flawed) structure as much as possible to address the user's direct query.\n",
        "\n",
        "    for example in training_data:\n",
        "        if example[-1] == 'Yes':  # Positive example\n",
        "            # Update specific hypothesis (hypotheses[0])\n",
        "            for i in range(num_attributes):\n",
        "                if hypotheses[0][i] != '0' and hypotheses[0][i] != example[i]:\n",
        "                    hypotheses[0][i] = '?'\n",
        "\n",
        "            # Remove inconsistent general hypotheses (from hypotheses[1:])\n",
        "            # Create a new list for general hypotheses to avoid modifying while iterating\n",
        "            new_general_hypotheses = []\n",
        "            for h in hypotheses[1:]:\n",
        "                is_consistent = True\n",
        "                for i in range(num_attributes):\n",
        "                    if h[i] != '?' and h[i] != example[i]:\n",
        "                        is_consistent = False\n",
        "                        break\n",
        "                if is_consistent:\n",
        "                    new_general_hypotheses.append(h)\n",
        "            hypotheses = [hypotheses[0]] + new_general_hypotheses\n",
        "\n",
        "        else:  # Negative example\n",
        "            # The logic for negative examples in the original code is complex and non-standard for\n",
        "            # Candidate Elimination. It seems to attempt to remove specific hypotheses or generate new ones\n",
        "            # in a way that doesn't fully align with the standard algorithm's bounds update.\n",
        "            temp_hypotheses = copy.deepcopy(hypotheses)\n",
        "            hypotheses_to_remove = []\n",
        "            hypotheses_to_add = []\n",
        "\n",
        "            for h in temp_hypotheses:\n",
        "                # This condition is from the original flawed code logic\n",
        "                if h[:-1] != example[:-1] + ['?']:\n",
        "                    if h in hypotheses:\n",
        "                        hypotheses_to_remove.append(h)\n",
        "\n",
        "                    # This nested loop also reflects the original (potentially flawed) logic\n",
        "                    for i in range(num_attributes):\n",
        "                        if example[i] != h[i] and h[i] != '?':\n",
        "                            new_hypothesis = copy.deepcopy(h)\n",
        "                            new_hypothesis[i] = '?'\n",
        "                            if new_hypothesis not in hypotheses_to_add and new_hypothesis not in hypotheses:\n",
        "                                hypotheses_to_add.append(new_hypothesis)\n",
        "\n",
        "            # Apply collected removals and additions\n",
        "            for h_rem in hypotheses_to_remove:\n",
        "                if h_rem in hypotheses:\n",
        "                    hypotheses.remove(h_rem)\n",
        "            for h_add in hypotheses_to_add:\n",
        "                if h_add not in hypotheses:\n",
        "                    hypotheses.append(h_add)\n",
        "\n",
        "            # IMPORTANT: The original code had 'return hypotheses' here, which would cause the function\n",
        "            # to exit after the first negative example, leading to incorrect results. Removed for now\n",
        "            # to allow the loop to complete, but the overall CE logic for negative examples is still problematic.\n",
        "\n",
        "    return hypotheses\n",
        "\n",
        "# Training data and function calls are placed outside the function definitions.\n",
        "training_data = [\n",
        "    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Rainy', 'Cold', 'High', 'Weak', 'Cool', 'Change', 'No'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']\n",
        "]\n",
        "\n",
        "result_hypotheses = candidate_elimination(training_data)\n",
        "print(\"Result Hypotheses:\")\n",
        "for h in result_hypotheses:\n",
        "    print(h)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H1_uDzPBhYjv",
        "outputId": "52eba1a8-3af0-45a5-dd68-37ac55124988"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result Hypotheses:\n",
            "['?', '0', '0', '0', '0', '0']\n"
          ]
        }
      ]
    }
  ]
}