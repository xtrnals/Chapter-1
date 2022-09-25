{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOWkoOe9+mGUvTkxH76ICxg",
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
        "<a href=\"https://colab.research.google.com/github/xtrnals/Chapter-1/blob/main/Chapter_1_Exercise_3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercise 3: Print date and Time ☑️\n"
      ],
      "metadata": {
        "id": "P7v9eif4Xsn6"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BHMc2hCZXhT9",
        "outputId": "9dc39d66-f392-45f1-b825-4879beb1cfed"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Current time is: \n",
            "25-09-22 11-23-48\n"
          ]
        }
      ],
      "source": [
        "import datetime\n",
        "\n",
        "now = datetime.datetime.now()\n",
        "print(\"Current time is: \")\n",
        "print(now.strftime(\"%d-%m-%y %H-%M-%S\"))"
      ]
    }
  ]
}