{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOACgr/u5vtuxH7YiCcDtR4",
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
        "<a href=\"https://colab.research.google.com/github/xtrnals/Chapter-1/blob/main/Chapter_1_Exercises.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercise 1: Print Strings☑️"
      ],
      "metadata": {
        "id": "ORuJnK0agPBu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print (\"Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I \\nwonder what you are\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "egcpweL9gR8_",
        "outputId": "3001188e-4a6c-4c5c-9858-d1395a2a518d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I \n",
            "wonder what you are\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercise 2: Print the Version of Python ☑️\n"
      ],
      "metadata": {
        "id": "tiJyVtb9hm_I"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!python --version"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CRzEntBshouz",
        "outputId": "820719fb-bb37-4565-ed6e-511c6e9d041b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Python 3.7.14\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercise 3: Print date and Time ☑️\n"
      ],
      "metadata": {
        "id": "axsLMe2-iTuG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from datetime import datetime\n",
        "now = datetime.now()\n",
        "print(\"now =\", now)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iuFzt8uciVan",
        "outputId": "d7b07c64-36f4-4814-fe94-10f96b613b75"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "now = 2022-09-24 17:39:26.317551\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercise 4: Strings Concatination ☑️\n"
      ],
      "metadata": {
        "id": "SNpvV7g0laWv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "color = \"red\"\n",
        "animal = \"dog\"\n",
        "name = \"johnny\"\n",
        "print(color, animal, name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "18euyvF1liRo",
        "outputId": "834b0b21-0e18-457e-c37d-cedda4d3e444"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "red dog johnny\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Exercise 5: Compute area of Circle ☑️\n"
      ],
      "metadata": {
        "id": "b3dUUHRAmBcE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "radius = int(input(\"Radius of circle: \"))\n",
        "area = 3.14 * radius ** 2\n",
        "print (area)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QDMt3jOamC4U",
        "outputId": "5da8b042-c316-4956-f84d-0d969be5810a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Radius of circle: 5\n",
            "78.5\n"
          ]
        }
      ]
    }
  ]
}