{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOnFy7OK0sMZH0prWo6UIxD"
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
      "source": [
        "STEP 1: Generate the Orders Dataset"
      ],
      "metadata": {
        "id": "8QJsFpsN1JCJ"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jNNFNyXn1BqI",
        "outputId": "a9b25eba-d9cb-4e00-d53a-a467c7e5592e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting faker\n",
            "  Downloading faker-37.4.0-py3-none-any.whl.metadata (15 kB)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.11/dist-packages (from faker) (2025.2)\n",
            "Downloading faker-37.4.0-py3-none-any.whl (1.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.9/1.9 MB\u001b[0m \u001b[31m12.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: faker\n",
            "Successfully installed faker-37.4.0\n",
            "   order_id  order_date   ship_date delivery_date region      status  \\\n",
            "0      1000  2025-06-11  2025-06-13    2025-06-18   East   Delivered   \n",
            "1      1001  2025-06-20  2025-06-21    2025-06-23   East  In Transit   \n",
            "2      1002  2025-06-19  2025-06-19    2025-06-24   East        Late   \n",
            "3      1003  2025-05-25  2025-05-27    2025-05-29   East  In Transit   \n",
            "4      1004  2025-05-25  2025-05-27    2025-05-31   West   Delivered   \n",
            "\n",
            "   delay_days  \n",
            "0           2  \n",
            "1           0  \n",
            "2           2  \n",
            "3           0  \n",
            "4           1  \n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "!pip install faker\n",
        "from faker import Faker\n",
        "import random\n",
        "from datetime import timedelta\n",
        "\n",
        "fake = Faker()\n",
        "np.random.seed(42)\n",
        "\n",
        "regions = ['North', 'South', 'East', 'West']\n",
        "statuses = ['Delivered', 'Late', 'In Transit', 'Cancelled']\n",
        "\n",
        "def generate_order_data(n=1000):\n",
        "    data = []\n",
        "    for i in range(n):\n",
        "        order_id = 1000 + i\n",
        "        order_date = fake.date_between(start_date='-60d', end_date='-10d')\n",
        "        ship_date = order_date + timedelta(days=random.randint(0, 2))\n",
        "        delivery_date = ship_date + timedelta(days=random.randint(2, 5))\n",
        "        region = random.choice(regions)\n",
        "        status = random.choices(\n",
        "            statuses, weights=(0.65, 0.15, 0.15, 0.05), k=1\n",
        "        )[0]\n",
        "        expected_delivery = ship_date + timedelta(days=3)\n",
        "        delay_days = (delivery_date - expected_delivery).days\n",
        "        delay_days = delay_days if delay_days > 0 else 0\n",
        "\n",
        "        data.append([\n",
        "            order_id, order_date, ship_date, delivery_date, region, status, delay_days\n",
        "        ])\n",
        "\n",
        "    df = pd.DataFrame(data, columns=[\n",
        "        'order_id', 'order_date', 'ship_date', 'delivery_date',\n",
        "        'region', 'status', 'delay_days'\n",
        "    ])\n",
        "    return df\n",
        "\n",
        "orders_df = generate_order_data(1000)\n",
        "orders_df.to_csv(\"orders.csv\", index=False)\n",
        "print(orders_df.head())\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "STEP 2: Generate the Inventory Dataset"
      ],
      "metadata": {
        "id": "B-ajiOV23jo9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def generate_inventory_data(n=100):\n",
        "    product_ids = [f\"P{1000+i}\" for i in range(n)]\n",
        "    data = []\n",
        "    for pid in product_ids:\n",
        "        region = random.choice(regions)\n",
        "        stock_level = random.randint(50, 200)\n",
        "        reorder_threshold = random.randint(60, 120)\n",
        "        data.append([pid, region, stock_level, reorder_threshold])\n",
        "\n",
        "    df = pd.DataFrame(data, columns=[\n",
        "        'product_id', 'region', 'stock_level', 'reorder_threshold'\n",
        "    ])\n",
        "    return df\n",
        "\n",
        "inventory_df = generate_inventory_data(100)\n",
        "inventory_df.to_csv(\"inventory.csv\", index=False)\n",
        "print(inventory_df.head())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7beGCw5D3kQ7",
        "outputId": "4cbdfd96-13d8-45da-f44f-0eeba9e942a0"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  product_id region  stock_level  reorder_threshold\n",
            "0      P1000  South           58                 75\n",
            "1      P1001  North           91                 71\n",
            "2      P1002   East           50                 85\n",
            "3      P1003   West          140                 81\n",
            "4      P1004   West           63                 95\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Using SQLite to analyse"
      ],
      "metadata": {
        "id": "WoZKtK3U4q89"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import sqlite3"
      ],
      "metadata": {
        "id": "lpdpdLkL3mn1"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "conn = sqlite3.connect(\"logistics.db\")\n",
        "cursor = conn.cursor()\n"
      ],
      "metadata": {
        "id": "173LMiE34wjX"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "orders_df = pd.read_csv(\"orders.csv\")\n",
        "inventory_df = pd.read_csv(\"inventory.csv\")\n",
        "\n",
        "orders_df.to_sql(\"orders\", conn, if_exists=\"replace\", index=False)\n",
        "inventory_df.to_sql(\"inventory\", conn, if_exists=\"replace\", index=False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "go643Rrh4yXZ",
        "outputId": "d61b2f50-e7de-43b3-8f70-da5b319fe5d5"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "100"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Delivery delay performance by region"
      ],
      "metadata": {
        "id": "7rJATIme5lj6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "query = \"\"\"\n",
        "SELECT region,\n",
        "       COUNT(*) AS total_orders,\n",
        "       SUM(CASE WHEN status = 'Late' THEN 1 ELSE 0 END) AS late_orders,\n",
        "       ROUND(AVG(delay_days), 2) AS avg_delay\n",
        "FROM orders\n",
        "WHERE status IN ('Delivered', 'Late')\n",
        "GROUP BY region\n",
        "ORDER BY late_orders DESC;\n",
        "\"\"\"\n",
        "\n",
        "delay_by_region_df = pd.read_sql_query(query, conn)\n",
        "print(delay_by_region_df)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0aDcT0eR48Lx",
        "outputId": "1f18b9ed-16ab-422f-edcc-52b1bbc3aa1b"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  region  total_orders  late_orders  avg_delay\n",
            "0   East           203           43       0.73\n",
            "1  South           207           40       0.70\n",
            "2  North           203           39       0.75\n",
            "3   West           192           33       0.79\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "delay_by_region_df.to_csv('delivery_delay_performance_by_region.csv', index=False)"
      ],
      "metadata": {
        "id": "y7slP-L27--f"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Low Inventory Alert System"
      ],
      "metadata": {
        "id": "zjt5-_iM5nJt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "query = \"PRAGMA table_info(inventory);\"\n",
        "schema_df = pd.read_sql_query(query, conn)\n",
        "print(schema_df)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iGpBEgGZ6a1N",
        "outputId": "e834e74e-a316-4048-dc09-40ea2321edbc"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   cid               name     type  notnull dflt_value  pk\n",
            "0    0         product_id     TEXT        0       None   0\n",
            "1    1             region     TEXT        0       None   0\n",
            "2    2        stock_level  INTEGER        0       None   0\n",
            "3    3  reorder_threshold  INTEGER        0       None   0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query_low_inventory = \"\"\"\n",
        "SELECT\n",
        "    product_id,\n",
        "    region,\n",
        "    stock_level,\n",
        "    reorder_threshold\n",
        "FROM inventory\n",
        "WHERE stock_level < reorder_threshold\n",
        "ORDER BY stock_level ASC;\n",
        "\"\"\"\n",
        "\n",
        "low_inventory_df = pd.read_sql_query(query_low_inventory, conn)\n",
        "display(low_inventory_df)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 886
        },
        "id": "8FI7bfFC6io5",
        "outputId": "1cb5eaa6-d0c0-418b-a68f-8131879ecbe4"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "   product_id region  stock_level  reorder_threshold\n",
              "0       P1002   East           50                 85\n",
              "1       P1060   East           50                116\n",
              "2       P1056  North           51                116\n",
              "3       P1068  South           51                112\n",
              "4       P1084   West           53                 92\n",
              "5       P1040   West           55                115\n",
              "6       P1051   West           55                 85\n",
              "7       P1076   East           57                 94\n",
              "8       P1099  North           57                 82\n",
              "9       P1000  South           58                 75\n",
              "10      P1022   West           58                 66\n",
              "11      P1039  South           59                107\n",
              "12      P1044   West           60                 77\n",
              "13      P1021  North           62                 67\n",
              "14      P1004   West           63                 95\n",
              "15      P1085   East           70                 88\n",
              "16      P1087  South           71                 99\n",
              "17      P1005  North           72                 96\n",
              "18      P1050   West           72                 90\n",
              "19      P1018  North           73                 96\n",
              "20      P1034  North           74                 78\n",
              "21      P1089   East           74                 85\n",
              "22      P1096   West           79                 95\n",
              "23      P1052   East           80                 88\n",
              "24      P1028  South           85                 91\n",
              "25      P1094   West           86                 90\n",
              "26      P1079   West           99                119"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-87474100-3230-4813-b4e0-32f49d6f46bf\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>product_id</th>\n",
              "      <th>region</th>\n",
              "      <th>stock_level</th>\n",
              "      <th>reorder_threshold</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>P1002</td>\n",
              "      <td>East</td>\n",
              "      <td>50</td>\n",
              "      <td>85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>P1060</td>\n",
              "      <td>East</td>\n",
              "      <td>50</td>\n",
              "      <td>116</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>P1056</td>\n",
              "      <td>North</td>\n",
              "      <td>51</td>\n",
              "      <td>116</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>P1068</td>\n",
              "      <td>South</td>\n",
              "      <td>51</td>\n",
              "      <td>112</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>P1084</td>\n",
              "      <td>West</td>\n",
              "      <td>53</td>\n",
              "      <td>92</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>P1040</td>\n",
              "      <td>West</td>\n",
              "      <td>55</td>\n",
              "      <td>115</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>P1051</td>\n",
              "      <td>West</td>\n",
              "      <td>55</td>\n",
              "      <td>85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>P1076</td>\n",
              "      <td>East</td>\n",
              "      <td>57</td>\n",
              "      <td>94</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>P1099</td>\n",
              "      <td>North</td>\n",
              "      <td>57</td>\n",
              "      <td>82</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>P1000</td>\n",
              "      <td>South</td>\n",
              "      <td>58</td>\n",
              "      <td>75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>P1022</td>\n",
              "      <td>West</td>\n",
              "      <td>58</td>\n",
              "      <td>66</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>P1039</td>\n",
              "      <td>South</td>\n",
              "      <td>59</td>\n",
              "      <td>107</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>P1044</td>\n",
              "      <td>West</td>\n",
              "      <td>60</td>\n",
              "      <td>77</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>P1021</td>\n",
              "      <td>North</td>\n",
              "      <td>62</td>\n",
              "      <td>67</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>P1004</td>\n",
              "      <td>West</td>\n",
              "      <td>63</td>\n",
              "      <td>95</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>P1085</td>\n",
              "      <td>East</td>\n",
              "      <td>70</td>\n",
              "      <td>88</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>P1087</td>\n",
              "      <td>South</td>\n",
              "      <td>71</td>\n",
              "      <td>99</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>P1005</td>\n",
              "      <td>North</td>\n",
              "      <td>72</td>\n",
              "      <td>96</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>P1050</td>\n",
              "      <td>West</td>\n",
              "      <td>72</td>\n",
              "      <td>90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>P1018</td>\n",
              "      <td>North</td>\n",
              "      <td>73</td>\n",
              "      <td>96</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>P1034</td>\n",
              "      <td>North</td>\n",
              "      <td>74</td>\n",
              "      <td>78</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>P1089</td>\n",
              "      <td>East</td>\n",
              "      <td>74</td>\n",
              "      <td>85</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>P1096</td>\n",
              "      <td>West</td>\n",
              "      <td>79</td>\n",
              "      <td>95</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>P1052</td>\n",
              "      <td>East</td>\n",
              "      <td>80</td>\n",
              "      <td>88</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>P1028</td>\n",
              "      <td>South</td>\n",
              "      <td>85</td>\n",
              "      <td>91</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>P1094</td>\n",
              "      <td>West</td>\n",
              "      <td>86</td>\n",
              "      <td>90</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26</th>\n",
              "      <td>P1079</td>\n",
              "      <td>West</td>\n",
              "      <td>99</td>\n",
              "      <td>119</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-87474100-3230-4813-b4e0-32f49d6f46bf')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-87474100-3230-4813-b4e0-32f49d6f46bf button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-87474100-3230-4813-b4e0-32f49d6f46bf');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    <div id=\"df-7d6ac182-11c4-42a5-ba30-f309fa39a35d\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-7d6ac182-11c4-42a5-ba30-f309fa39a35d')\"\n",
              "                title=\"Suggest charts\"\n",
              "                style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "      <script>\n",
              "        async function quickchart(key) {\n",
              "          const quickchartButtonEl =\n",
              "            document.querySelector('#' + key + ' button');\n",
              "          quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "          quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "          try {\n",
              "            const charts = await google.colab.kernel.invokeFunction(\n",
              "                'suggestCharts', [key], {});\n",
              "          } catch (error) {\n",
              "            console.error('Error during call to suggestCharts:', error);\n",
              "          }\n",
              "          quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "          quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "        }\n",
              "        (() => {\n",
              "          let quickchartButtonEl =\n",
              "            document.querySelector('#df-7d6ac182-11c4-42a5-ba30-f309fa39a35d button');\n",
              "          quickchartButtonEl.style.display =\n",
              "            google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "        })();\n",
              "      </script>\n",
              "    </div>\n",
              "\n",
              "  <div id=\"id_0c9b7143-d2e2-43bd-80c7-f1258acbacaa\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('low_inventory_df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_0c9b7143-d2e2-43bd-80c7-f1258acbacaa button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('low_inventory_df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "low_inventory_df",
              "summary": "{\n  \"name\": \"low_inventory_df\",\n  \"rows\": 27,\n  \"fields\": [\n    {\n      \"column\": \"product_id\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 27,\n        \"samples\": [\n          \"P1099\",\n          \"P1021\",\n          \"P1000\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"region\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"North\",\n          \"West\",\n          \"East\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"stock_level\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 12,\n        \"min\": 50,\n        \"max\": 99,\n        \"num_unique_values\": 20,\n        \"samples\": [\n          50,\n          85,\n          79\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"reorder_threshold\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 14,\n        \"min\": 66,\n        \"max\": 119,\n        \"num_unique_values\": 20,\n        \"samples\": [\n          85,\n          78,\n          96\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Export low inventory data\n",
        "low_inventory_df.to_csv('low_inventory.csv', index=False)"
      ],
      "metadata": {
        "id": "JMn0skhm8GKi"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Delivery Performance Over Time"
      ],
      "metadata": {
        "id": "9jtJfaoO6lER"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "query = \"PRAGMA table_info(orders);\"\n",
        "orders_schema = pd.read_sql_query(query, conn)\n",
        "print(orders_schema)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pnFFizIH6xjg",
        "outputId": "abe6aa5b-826d-4552-d71c-d4d9cdadb630"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   cid           name     type  notnull dflt_value  pk\n",
            "0    0       order_id  INTEGER        0       None   0\n",
            "1    1     order_date     TEXT        0       None   0\n",
            "2    2      ship_date     TEXT        0       None   0\n",
            "3    3  delivery_date     TEXT        0       None   0\n",
            "4    4         region     TEXT        0       None   0\n",
            "5    5         status     TEXT        0       None   0\n",
            "6    6     delay_days  INTEGER        0       None   0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "query_ontime_performance = \"\"\"\n",
        "SELECT\n",
        "    delivery_date,\n",
        "    COUNT(*) AS total_deliveries,\n",
        "    SUM(CASE WHEN delay_days = 0 THEN 1 ELSE 0 END) AS on_time_deliveries,\n",
        "    ROUND(100.0 * SUM(CASE WHEN delay_days = 0 THEN 1 ELSE 0 END) / COUNT(*), 2) AS on_time_pct\n",
        "FROM orders\n",
        "WHERE status = 'Delivered'\n",
        "GROUP BY delivery_date\n",
        "ORDER BY delivery_date;\n",
        "\"\"\"\n",
        "\n",
        "ontime_df = pd.read_sql_query(query_ontime_performance, conn)\n",
        "\n",
        "# Convert delivery_date to datetime for plotting\n",
        "ontime_df['delivery_date'] = pd.to_datetime(ontime_df['delivery_date'])\n"
      ],
      "metadata": {
        "id": "uZYpVvWm7HEm"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "\n",
        "plt.figure(figsize=(10, 5))\n",
        "plt.plot(ontime_df['delivery_date'], ontime_df['on_time_pct'], marker='o', color='green')\n",
        "plt.title(\"📦 On-Time Delivery % Over Time\")\n",
        "plt.xlabel(\"Delivery Date\")\n",
        "plt.ylabel(\"On-Time %\")\n",
        "plt.xticks(rotation=45)\n",
        "plt.grid(True)\n",
        "plt.tight_layout()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 575
        },
        "id": "K9W3FiY37IQW",
        "outputId": "622bc115-56d5-49e4-b96e-f2a84f645077"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/tmp/ipython-input-14-411159764.py:10: UserWarning: Glyph 128230 (\\N{PACKAGE}) missing from font(s) DejaVu Sans.\n",
            "  plt.tight_layout()\n",
            "/usr/local/lib/python3.11/dist-packages/IPython/core/pylabtools.py:151: UserWarning: Glyph 128230 (\\N{PACKAGE}) missing from font(s) DejaVu Sans.\n",
            "  fig.canvas.print_figure(bytes_io, **kw)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x500 with 1 Axes>"
            ],
            "image/png": "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8VhdHn5l+/bt6tSpk3r06KHXX39dX331lT766CPNmjXL6tJQgqSmpurOO+/UihUrNHv2bC1atIjGuxhLT0/XoEGDdP/99+udd97RggULVL16dZ06dcq/j8PhkNfrtbBKSP875o4cOVLPPPOMjDH68ccftXz5ch04cMDq8vArP/74oxISEtSnTx998MEH+vHHH7Vt2za99NJLVpeG82B6OUqNFStW6OGHH9ann36qGjVqSJIGDRqkChUqyOv1KjY2lilvxURWVpbuuOMOrVmzxn+mNDExUbt27dL69evVrl079erVS6NGjbK2UEg6ndeDDz6o8uXL65///KccDoccDocef/xxLV++XMuWLZPP55PTyfe8uHRer1czZ85UcnKypkyZor/85S86ePCgxo0bp549eyokJISp5sXM+vXrNWDAAC1atEhXX321JGno0KHKyMhQWFiYIiIi9MILL8jlcvEZYSG3263+/ftr0aJF/mvtb731Vh04cEDr169X8+bNdfPNN2vGjBnWFgpJ0smTJzVmzBh5PB49//zzcrlccrlcmjt3rp555hmtW7dOoaGhfBYWM3y6odQICgpSTk6Ofzr5k08+qXnz5snpdOrIkSP6z3/+o379+llcJaTTWT3wwAOKiYnR7bffroSEBOXl5emxxx7TV199pVq1aumtt97Sa6+9ZnWp0OkFkTIzM9WqVSs5nU7/gT4uLk779u1jZgKuCJfLpU6dOunee+9VkyZNtGTJEkVFRenJJ5/UokWL5Ha7OeNdzISHh8vtduvNN99Ubm6uJk+erNdff10NGjRQ9erVtXr1at18882SRMNtoZCQEI0bN04NGjTQDTfcoK5du8rlcunpp5/Wpk2bdPvttys5OVmTJ0+2ulTo9CUZHo9HN910k0JCQuRyuSRJUVFRysjIkNvttrhCnJMBSom0tDTTr18/Ex8fb7p27WpcLpdZuHCh//lXX33V1K1b12zatMnCKuHz+Ywxxpw6dcosWLDAXHXVVaZ169Zm//79/n2OHTtm2rZta/r3729VmfiVPXv2+P87Ly/PGGPMBx98YFq0aFFgv7179wa0LpQsubm5BR673W7TvXt306xZM/Pee+/5n//www+tKA+/cuzYMfPoo4+amjVrmi5dupjg4GDz/vvv+59fvny5iY6ONl9++aWFVZZu+cdcY4xZt26due6660zz5s0LfKbn5OSYQYMGmc6dOxu3221FmfiVM/9NlH/MTUlJMddee63xer3+57Zu3Rrw2nBuQVY3/UBROXbsmNLT0xUZGamyZcsqKipKM2bMUFpamlJTU3X48GG1b9/ev3+tWrXk8/kUHBxsYdWlV15enoKCgvxnqkJDQ9WjRw+FhobK6XSqWrVqkk5PMS1fvryaN2+udevWMSXRIjk5OcrJyVGZMmUUGhqq2NhYSafPeud/6+50OpWVleV/zbhx45SamqqXXnpJZcuWtaRu2MuRI0e0Z88elS1bVtWqVVPFihX9v/N5eXkKCQnRhx9+qF69eunJJ5+U1+vVsmXLtGjRIrVq1UrVq1e3+kcoVc7Mq2rVqqpUqZLGjh2rhx56SHv37tVDDz2ktm3b+vePiIjw/w+B5fF4/P/eMb9cltG0aVO98cYbOnDggKKjoyWdPuaWKVNG11xzjbZs2cKt3iySmZmp9PR0hYaGqnz58oqJiZFU8JibP+vs5MmTCg8P11//+lelpKTovffeU4UKFSysHpJE040SaePGjRo0aJBycnLk8/nUrFkzTZ48WQ0bNlRMTIzy8vIUGhqqjIwMlS9fXpL06aefqmrVqqpSpYrF1Zc+P/74o+bOnauhQ4eqXr16/sY7LCxMXbp0kdPp9B9U8v//4MGDatKkCdcsWWDLli0aNWqU0tLSJEnDhg3TkCFDFBERUeALEGOMsrOzJUnjx4/XtGnT9PXXX9Nwo1A2btyovn37yuv1yu12KyoqSv/85z/9t6ILCgryf5YvXLhQvXv31qBBgxQSEqIVK1bQcAfYr/OqVq2a/vGPf6hNmzYqX768/zN969at/i+8P/jgA5UtW1Y1a9a0uPrSZfv27Zo8ebL++Mc/qnnz5pL+13g3atRIjRo18n+W5x9zd+7cqeuuu05BQbQOgbZ582Y9+OCDSk9Pl8fj0e23365x48apWrVqBY65Ho9HJ06ckNPp1MSJE/3HXBru4oHfHJQ4e/fuVUJCgu666y71799f3377rT7++GO1adNGSUlJuvHGG1WlShXt3LlTI0eOVHx8vDwej9555x0tW7ZMlStXtvpHKFV27typm2++WadOnZLb7daIESN01VVX+ZvpkJCQAvvn5OTob3/7m5KTk5WcnEzTHWDbtm1Tx44dNWDAAA0fPlwff/yx5syZo9atW6tVq1aS/vePN4fDofj4eE2cOFFPP/20UlJS/P/AA35LWlqabr/9dg0YMEBDhw7V1q1b9c4776hdu3Z6/fXXNWDAAEmnG2+v16uQkBDVqlVLERERWrFiha699lqLf4LS5Xx5dejQwZ9XeHi4nE6npkyZon/84x+KjIzUwoUL9cUXXygqKsrqH6HU+Omnn9S1a1edOHFCJ0+e1Pjx49WsWTP/l92/njmWkZGh6dOna/HixUpOTqbpDrAffvhBnTp10qBBg9S7d28lJydr0aJFWrVqlRITEwssHhkSEqK6devqscce0+zZs/XNN9+oRYsWFv8E8LNsYjtQRL744gvTokULk56e7t+2Y8cOc9ddd5kyZcqY7777zhhjzNq1a0337t1N+/btzV133WU2b95sVcmlVlZWlhk4cKC56667zKRJk0yzZs3MiBEjzI4dO865/wcffGDuuusuExMTY9atWxfgapGRkWG6detmHnnkkQLbmzdvbh566KGz9l+0aJFxOBymSpUqZs2aNYEqEyXA999/bxo1amR+/vln/7acnBzzpz/9yYSEhJjFixcbY4z/2sXZs2cbh8PB54JFLpRX/vopW7ZsMcOHDze33nqreeihh7jeNMBycnLM4MGDTZ8+fczs2bNN586dze23337e35ukpCRz3333mdjYWH63LHD8+HFzxx13mAcffLDA9oSEBNO7d++z9v/666+Nw+EwlSpVMmvXrg1UmSgkvq5CiXPs2DGtX7++wIrJV111laZPny6Px6MBAwbos88+U/PmzTV//nz/6qqhoaEWVl06hYaGqn379ipbtqzuueceVapUSS+//LIkadSoUbrqqqsK7N+iRQtt3bpVkydPVt26da0ouVTbt2+fIiMj1b9/f0lSbm6uQkJC1LlzZ6Wnp5+1f/369VW9enUtXbpUjRs3DnS5sLHjx49ry5Yt/pXIfT6fypQpo2nTpunkyZMaOHCg1qxZo3r16kmS+vfvr+7du6tOnTpWll1qXSive+65R99++60aNmyoZ599ViEhIf51PBA4ZcqUUffu3ZWZmalhw4YpOjpazz//vCZOnKhJkyapWbNmBfZv0qSJ9u7dq4kTJ6p27doWVV16HT16VFWqVNFtt90m6X/X4ffs2VNJSUmSVOBMd40aNXTDDTdo7ty5atiwoWV149y4TzdKnLS0NN1xxx3q3Lmzxo4d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2LBBmzdv1hNPPPGb7+tyuTR48GCNHTtW9erVU+vWrS9YS15entLS0uTz+ZSenq7k5GQ98cQTatq0qf7v//5PkhQXF6eQkBD94x//0EMPPaTNmzdrypQpBd6nVq1acjgcWrx4sW655RaVKVNGERER+tOf/qTRo0fL5/Pp5ptv1vHjx7V69WpFRkbqvvvuK9TfFwAARYWF1AAACJCkpCTFxMQoPj5e3bt317JlyzRr1iwtXLhQLpdL0ulbdX388cdq166dhgwZoquvvloDBgxQamqqoqKiCv1nderUSZUqVdL27ds1cODAAs8lJCRo8eLF+vTTT9WqVSvdeOONeu6551SrVq1CvffQoUOVm5urIUOGFGr/LVu2KCYmRnFxcerQoYPeffddjR07VitXrlS5cuUkSVWrVtWrr76q9957Tw0bNtRTTz111u3JatSo4V8ELioqSiNGjJAkTZkyRePHj9fUqVPVoEEDde/eXUuWLPFPXQcAwEoOY4yxuggAAGAfK1euVOfOnbVnz56L+iIAAIDSiKYbAAAUitvt1uHDh3XfffcpOjpa8+bNs7okAACKPaaXAwCAQnn77bdVq1YtHTt2TNOmTbO6HAAAbIEz3QAAAAAAFBHOdAMAAAAAUERougEAAAAAKCI03QAAAAAAFBGabgAAAAAAighNNwAAAAAARYSmGwAAAACAIkLTDQAAAABAEaHpBgAAAACgiNB0AwAAAABQRP4f4ndplpx4Cr8AAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Export on-time delivery performance data\n",
        "ontime_df.to_csv('on_time_delivery_performance.csv', index=False)"
      ],
      "metadata": {
        "id": "Cgk_jFkR8Kzs"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "eA5LAn4z8M00"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}