{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "56ff8931",
   "metadata": {},
   "outputs": []
   "source": [
    "# Add Matplotlib inline magic command\n",
    "%matplotlib inline\n",
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "\n",
    "# File to Load (Remember to change these)\n",
    "city_data_to_load = \"Resources/city_data.csv\"\n",
    "ride_data_to_load = \"Resources/ride_data.csv\"\n",
    "\n",
    "# Read the City and Ride Data\n",
    "city_data_df = pd.read_csv(city_data_to_load)\n",
    "ride_data_df = pd.read_csv(ride_data_to_load)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "id": "eed1673f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>city</th>\n",
       "      <th>date</th>\n",
       "      <th>fare</th>\n",
       "      <th>ride_id</th>\n",
       "      <th>driver_count</th>\n",
       "      <th>type</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Lake Jonathanshire</td>\n",
       "      <td>1/14/2019 10:14</td>\n",
       "      <td>13.83</td>\n",
       "      <td>5.739410e+12</td>\n",
       "      <td>5</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>South Michelleport</td>\n",
       "      <td>3/4/2019 18:24</td>\n",
       "      <td>30.24</td>\n",
       "      <td>2.343910e+12</td>\n",
       "      <td>72</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Port Samanthamouth</td>\n",
       "      <td>2/24/2019 4:29</td>\n",
       "      <td>33.44</td>\n",
       "      <td>2.005070e+12</td>\n",
       "      <td>57</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rodneyfort</td>\n",
       "      <td>2/10/2019 23:22</td>\n",
       "      <td>23.44</td>\n",
       "      <td>5.149250e+12</td>\n",
       "      <td>34</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>South Jack</td>\n",
       "      <td>3/6/2019 4:28</td>\n",
       "      <td>34.58</td>\n",
       "      <td>3.908450e+12</td>\n",
       "      <td>46</td>\n",
       "      <td>Urban</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                 city             date   fare       ride_id  driver_count  \\\n",
       "0  Lake Jonathanshire  1/14/2019 10:14  13.83  5.739410e+12             5   \n",
       "1  South Michelleport   3/4/2019 18:24  30.24  2.343910e+12            72   \n",
       "2  Port Samanthamouth   2/24/2019 4:29  33.44  2.005070e+12            57   \n",
       "3          Rodneyfort  2/10/2019 23:22  23.44  5.149250e+12            34   \n",
       "4          South Jack    3/6/2019 4:28  34.58  3.908450e+12            46   \n",
       "\n",
       "    type  \n",
       "0  Urban  \n",
       "1  Urban  \n",
       "2  Urban  \n",
       "3  Urban  \n",
       "4  Urban  "
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Combine the data into a single dataset\n",
    "pyber_data_df = pd.merge(ride_data_df, city_data_df, how=\"left\", on=[\"city\", \"city\"])\n",
    "\n",
    "# Display the DataFrame\n",
    "pyber_data_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "id": "6cfdc9a4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural        125\n",
       "Suburban     625\n",
       "Urban       1625\n",
       "Name: ride_id, dtype: int64"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 1 Get the number of rides for urban cities. 5.3.2\n",
    "total_rides_by_type = pyber_data_df.groupby([\"type\"]).count()[\"ride_id\"]\n",
    "total_rides_by_type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "98dee274",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural         78\n",
       "Suburban     490\n",
       "Urban       2405\n",
       "Name: driver_count, dtype: int64"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 2 ** Get the total drivers for each city type\n",
    "total_drivers_by_type = city_data_df.groupby([\"type\"]).sum()[\"driver_count\"]\n",
    "total_drivers_by_type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "2c6d9eca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural        4327.93\n",
       "Suburban    19356.33\n",
       "Urban       39854.38\n",
       "Name: fare, dtype: float64"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 3 Get the total amount of fares for each city type\n",
    "total_fares_by_type = pyber_data_df.groupby([\"type\"]).sum()[\"fare\"]\n",
    "total_fares_by_type"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "50262c3c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural       34.623440\n",
       "Suburban    30.970128\n",
       "Urban       24.525772\n",
       "Name: fare, dtype: float64"
      ]
     },
     "execution_count": 134,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 4 Average fare per ride by city type\n",
    "avg_fare_per_ride = pyber_data_df.groupby([\"type\"]).mean()[\"fare\"]\n",
    "avg_fare_per_ride"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "7e1e6259",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "type\n",
       "Rural       55.486282\n",
       "Suburban    39.502714\n",
       "Urban       16.571468\n",
       "dtype: float64"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 5. Get the average fare per driver for each city type. \n",
    "avg_fare_per_driver = total_fares_by_type / total_drivers_by_type\n",
    "avg_fare_per_driver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "2642c321",
   "metadata": {},
   "outputs": []
   "source": [
    "# 6 create a PyBer summary DataFrame with all the data gathered from Steps 1-5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "14616c5e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Total Rides</th>\n",
       "      <th>Total Drivers</th>\n",
       "      <th>Total Fares</th>\n",
       "      <th>Average Fare per Ride</th>\n",
       "      <th>Average Fare per Driver</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>type</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Rural</th>\n",
       "      <td>125</td>\n",
       "      <td>78</td>\n",
       "      <td>4327.93</td>\n",
       "      <td>34.623440</td>\n",
       "      <td>55.486282</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Suburban</th>\n",
       "      <td>625</td>\n",
       "      <td>490</td>\n",
       "      <td>19356.33</td>\n",
       "      <td>30.970128</td>\n",
       "      <td>39.502714</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Urban</th>\n",
       "      <td>1625</td>\n",
       "      <td>2405</td>\n",
       "      <td>39854.38</td>\n",
       "      <td>24.525772</td>\n",
       "      <td>16.571468</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Total Rides  Total Drivers  Total Fares  Average Fare per Ride  \\\n",
       "type                                                                       \n",
       "Rural             125             78      4327.93              34.623440   \n",
       "Suburban          625            490     19356.33              30.970128   \n",
       "Urban            1625           2405     39854.38              24.525772   \n",
       "\n",
       "          Average Fare per Driver  \n",
       "type                               \n",
       "Rural                   55.486282  \n",
       "Suburban                39.502714  \n",
       "Urban                   16.571468  "
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary_df = pd.DataFrame({\"Total Rides\": total_rides_by_type, \n",
    "                           \"Total Drivers\": total_drivers_by_type, \n",
    "                           \"Total Fares\": total_fares_by_type, \n",
    "                           \"Average Fare per Ride\": avg_fare_per_ride, \n",
    "                           \"Average Fare per Driver\": avg_fare_per_driver})\n",
    "summary_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "79502206",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>Total Rides</th>\n",
       "      <th>Total Drivers</th>\n",
       "      <th>Total Fares</th>\n",
       "      <th>Average Fare per Ride</th>\n",
       "      <th>Average Fare per Driver</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Rural</th>\n",
       "      <td>125</td>\n",
       "      <td>78</td>\n",
       "      <td>$4327.93</td>\n",
       "      <td>$34.62</td>\n",
       "      <td>$55.49</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Suburban</th>\n",
       "      <td>625</td>\n",
       "      <td>490</td>\n",
       "      <td>$19356.33</td>\n",
       "      <td>$30.97</td>\n",
       "      <td>$39.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Urban</th>\n",
       "      <td>1625</td>\n",
       "      <td>2405</td>\n",
       "      <td>$39854.38</td>\n",
       "      <td>$24.53</td>\n",
       "      <td>$16.57</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Total Rides  Total Drivers Total Fares Average Fare per Ride  \\\n",
       "Rural             125             78    $4327.93                $34.62   \n",
       "Suburban          625            490   $19356.33                $30.97   \n",
       "Urban            1625           2405   $39854.38                $24.53   \n",
       "\n",
       "         Average Fare per Driver  \n",
       "Rural                     $55.49  \n",
       "Suburban                  $39.50  \n",
       "Urban                     $16.57  "
      ]
     },
     "execution_count": 138,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "summary_df = pd.DataFrame({\"Total Rides\": total_rides_by_type, \n",
    "                           \"Total Drivers\": total_drivers_by_type, \n",
    "                           \"Total Fares\": total_fares_by_type, \n",
    "                           \"Average Fare per Ride\": avg_fare_per_ride, \n",
    "                           \"Average Fare per Driver\": avg_fare_per_driver})\n",
    "summary_df.index.name = None\n",
    "summary_df[\"Total Fares\"] = summary_df[\"Total Fares\"].map(\"${:.2f}\".format)\n",
    "summary_df[\"Average Fare per Ride\"] = summary_df[\"Average Fare per Ride\"].map(\"${:.2f}\".format)\n",
    "summary_df[\"Average Fare per Driver\"] = summary_df[\"Average Fare per Driver\"].map(\"${:.2f}\".format)\n",
    "summary_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "34a41f56",
   "metadata": {},
   "outputs": []
   "source": [
    "# Deliverable 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "id": "8f86bcc5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th></th>\n",
       "      <th>fare</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>type</th>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">Rural</th>\n",
       "      <th>1/1/2019 9:45</th>\n",
       "      <td>43.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/11/2019 4:39</th>\n",
       "      <td>16.42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/14/2019 15:58</th>\n",
       "      <td>54.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/14/2019 7:09</th>\n",
       "      <td>18.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/15/2019 21:44</th>\n",
       "      <td>30.26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"5\" valign=\"top\">Urban</th>\n",
       "      <th>5/8/2019 1:54</th>\n",
       "      <td>32.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/8/2019 2:31</th>\n",
       "      <td>41.33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/8/2019 4:20</th>\n",
       "      <td>21.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/8/2019 4:39</th>\n",
       "      <td>18.45</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5/8/2019 7:29</th>\n",
       "      <td>18.55</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2364 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                        fare\n",
       "type  date                  \n",
       "Rural 1/1/2019 9:45    43.69\n",
       "      1/11/2019 4:39   16.42\n",
       "      1/14/2019 15:58  54.10\n",
       "      1/14/2019 7:09   18.05\n",
       "      1/15/2019 21:44  30.26\n",
       "...                      ...\n",
       "Urban 5/8/2019 1:54    32.69\n",
       "      5/8/2019 2:31    41.33\n",
       "      5/8/2019 4:20    21.99\n",
       "      5/8/2019 4:39    18.45\n",
       "      5/8/2019 7:29    18.55\n",
       "\n",
       "[2364 rows x 1 columns]"
      ]
     },
     "execution_count": 140,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Step 1, create a new DataFrame with multiple indices using the groupby() function on the \"type\" and \"date\" columns of the pyber_data_df\n",
    "new_df = pyber_data_df.groupby([\"type\", \"date\"]).sum()[[\"fare\"]]\n",
    "new_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "id": "0932e6ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>type</th>\n",
       "      <th>date</th>\n",
       "      <th>fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Rural</td>\n",
       "      <td>1/1/2019 9:45</td>\n",
       "      <td>43.69</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Rural</td>\n",
       "      <td>1/11/2019 4:39</td>\n",
       "      <td>16.42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Rural</td>\n",
       "      <td>1/14/2019 15:58</td>\n",
       "      <td>54.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Rural</td>\n",
       "      <td>1/14/2019 7:09</td>\n",
       "      <td>18.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Rural</td>\n",
       "      <td>1/15/2019 21:44</td>\n",
       "      <td>30.26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    type             date   fare\n",
       "0  Rural    1/1/2019 9:45  43.69\n",
       "1  Rural   1/11/2019 4:39  16.42\n",
       "2  Rural  1/14/2019 15:58  54.10\n",
       "3  Rural   1/14/2019 7:09  18.05\n",
       "4  Rural  1/15/2019 21:44  30.26"
      ]
     },
     "execution_count": 141,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Step 2, use the provided code snippet to reset the index\n",
    "new_df = new_df.reset_index()\n",
    "new_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "8201c979",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['type', 'date', 'fare'], dtype='object')"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "new_df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "id": "ed37bbd2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>type</th>\n",
       "      <th>Rural</th>\n",
       "      <th>Suburban</th>\n",
       "      <th>Urban</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1/1/2019 0:08</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>37.91</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/1/2019 0:46</th>\n",
       "      <td>NaN</td>\n",
       "      <td>47.74</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/1/2019 12:32</th>\n",
       "      <td>NaN</td>\n",
       "      <td>25.56</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/1/2019 14:40</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/1/2019 14:42</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/1/2019 14:52</th>\n",
       "      <td>NaN</td>\n",
       "      <td>31.15</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/1/2019 17:22</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>42.11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/1/2019 21:04</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>11.71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/1/2019 2:07</th>\n",
       "      <td>NaN</td>\n",
       "      <td>24.07</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1/1/2019 3:46</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>7.57</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "type            Rural  Suburban  Urban\n",
       "date                                  \n",
       "1/1/2019 0:08     NaN       NaN  37.91\n",
       "1/1/2019 0:46     NaN     47.74    NaN\n",
       "1/1/2019 12:32    NaN     25.56    NaN\n",
       "1/1/2019 14:40    NaN       NaN   5.42\n",
       "1/1/2019 14:42    NaN       NaN  12.31\n",
       "1/1/2019 14:52    NaN     31.15    NaN\n",
       "1/1/2019 17:22    NaN       NaN  42.11\n",
       "1/1/2019 21:04    NaN       NaN  11.71\n",
       "1/1/2019 2:07     NaN     24.07    NaN\n",
       "1/1/2019 3:46     NaN       NaN   7.57"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Step 3, use the pivot() function to convert the DataFrame \n",
    "new_df_pivot = new_df.pivot(index= \"date\", columns= \"type\", values= \"fare\")\n",
    "new_df_pivot.head(10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "id": "86fbd797",
   "metadata": {},
   "outputs": []
   "source": [
    "new_df_pivot.index = pd.to_datetime(new_df_pivot.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "82495bd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 4, create a new DataFrame by using the loc method\n",
    "new_df_pivot = new_df_pivot.loc[\"2019-01-01\":\"2019-04-28\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "id": "8896e0be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',\n",
       "               '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08',\n",
       "               '2019-01-09', '2019-01-10'],\n",
       "              dtype='datetime64[ns]', freq='D')"
      ]
     },
     "execution_count": 146,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Step 5, use the provided code snippet to reset the index of the DataFrame\n",
    "index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "41e1158d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "DatetimeIndex: 2182 entries, 2019-01-01 00:08:00 to 2019-04-09 09:17:00\n",
      "Data columns (total 3 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   Rural     114 non-null    float64\n",
      " 1   Suburban  570 non-null    float64\n",
      " 2   Urban     1501 non-null   float64\n",
      "dtypes: float64(3)\n",
      "memory usage: 68.2 KB\n"
     ]
    }
   ],
   "source": [
    "# Step 6, use the provided code snippet, df.info()\n",
    "new_df_pivot.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 148,
   "id": "96218ef9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
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
       "      <th>type</th>\n",
       "      <th>Rural</th>\n",
       "      <th>Suburban</th>\n",
       "      <th>Urban</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2019-01-06</th>\n",
       "      <td>187.92</td>\n",
       "      <td>721.60</td>\n",
       "      <td>1661.68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-13</th>\n",
       "      <td>67.65</td>\n",
       "      <td>1105.13</td>\n",
       "      <td>2050.43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-20</th>\n",
       "      <td>306.00</td>\n",
       "      <td>1218.20</td>\n",
       "      <td>1939.02</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-01-27</th>\n",
       "      <td>179.69</td>\n",
       "      <td>1203.28</td>\n",
       "      <td>2129.51</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-02-03</th>\n",
       "      <td>333.08</td>\n",
       "      <td>1042.79</td>\n",
       "      <td>2086.94</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-02-10</th>\n",
       "      <td>115.80</td>\n",
       "      <td>974.34</td>\n",
       "      <td>2162.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-02-17</th>\n",
       "      <td>95.82</td>\n",
       "      <td>1045.50</td>\n",
       "      <td>2235.07</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-02-24</th>\n",
       "      <td>419.06</td>\n",
       "      <td>1412.74</td>\n",
       "      <td>2466.29</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-03-03</th>\n",
       "      <td>175.14</td>\n",
       "      <td>858.46</td>\n",
       "      <td>2218.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-03-10</th>\n",
       "      <td>303.94</td>\n",
       "      <td>925.27</td>\n",
       "      <td>2470.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-03-17</th>\n",
       "      <td>163.39</td>\n",
       "      <td>906.20</td>\n",
       "      <td>2044.42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-03-24</th>\n",
       "      <td>189.76</td>\n",
       "      <td>1122.20</td>\n",
       "      <td>2368.37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-03-31</th>\n",
       "      <td>199.42</td>\n",
       "      <td>1045.06</td>\n",
       "      <td>1942.77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-04-07</th>\n",
       "      <td>501.24</td>\n",
       "      <td>1010.73</td>\n",
       "      <td>2356.70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-04-14</th>\n",
       "      <td>269.79</td>\n",
       "      <td>784.82</td>\n",
       "      <td>2390.72</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-04-21</th>\n",
       "      <td>214.14</td>\n",
       "      <td>1149.27</td>\n",
       "      <td>2303.80</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019-04-28</th>\n",
       "      <td>191.85</td>\n",
       "      <td>1357.75</td>\n",
       "      <td>2238.29</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "type         Rural  Suburban    Urban\n",
       "date                                 \n",
       "2019-01-06  187.92    721.60  1661.68\n",
       "2019-01-13   67.65   1105.13  2050.43\n",
       "2019-01-20  306.00   1218.20  1939.02\n",
       "2019-01-27  179.69   1203.28  2129.51\n",
       "2019-02-03  333.08   1042.79  2086.94\n",
       "2019-02-10  115.80    974.34  2162.64\n",
       "2019-02-17   95.82   1045.50  2235.07\n",
       "2019-02-24  419.06   1412.74  2466.29\n",
       "2019-03-03  175.14    858.46  2218.20\n",
       "2019-03-10  303.94    925.27  2470.93\n",
       "2019-03-17  163.39    906.20  2044.42\n",
       "2019-03-24  189.76   1122.20  2368.37\n",
       "2019-03-31  199.42   1045.06  1942.77\n",
       "2019-04-07  501.24   1010.73  2356.70\n",
       "2019-04-14  269.79    784.82  2390.72\n",
       "2019-04-21  214.14   1149.27  2303.80\n",
       "2019-04-28  191.85   1357.75  2238.29"
      ]
     },
     "execution_count": 148,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Step 7, create a new DataFrame by applying the resample() \n",
    "new_df_pivot = new_df_pivot.resample(\"W\").sum()\n",
    "new_df_pivot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "30d04e12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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h759++Lll19GUFAQAODEiROwWCwYPHiwbf+IiAi0adMGBw8exJAhQ3Do0CG0adPGrrv5kCFDYDKZcOLECfTv37/WnxMhhBBCbp7JZML169cxb948jBkzBpGRke4OiRBCCCFuUqmkRrNmzWo6DqeGDh2KsWPHonnz5rh69SreeustjBs3Djt37oROp7NdoQkICLC7X1BQENLS0gCoV3GKkiBFAgICIAiCbR9n4uLiXP+ECCF1Cr3OSWOk1+uh0+ncHUa1fP/993juuefQoUMHLFmyBEajscx9yxtrSHJycso9ryGENEx0LkMag5iYmHLHK11+UhaLxYIjR47g2rVriImJQceOHat7SJu7777b9nOHDh3QuXNnxMbGYuvWrRg3bpzLHseZiv7hCCH1W1xcHL3OSaOUnZ0NvV7v7jCqZerUqZg6dWq5+2RlZcFoNNb751pZvr6+NGOFkEaGzmUIUVVqSZPff/8dTzzxBK5fv263PT4+Hn369MHo0aMxffp09O/fH9OmTXNYds1VwsLCEB4ejosXLwJQa2FlWUZGRobdfunp6QgODrbtk56ebjeekZEBWZZt+xBCCCGEEEIIIaT+qVRS47vvvsNff/2FwMBAu+3/+te/EB8fj/vuuw8LFy7E0KFDsWHDBnz22Wc1EmxGRgZSUlJsjUM7d+4MjUaDHTt22PZJSkrCuXPn0KtXLwBAz549ce7cObtlXnfs2AGdTofOnTvXSJyEEEIIIYQQQgipeZUqPzl+/DjGjh1rt+306dM4duwY7r77bnzyyScAgEceeQQjR47EDz/8YFsHvjx5eXm2WReKoiAxMRF//fUX/P394e/vjwULFmDcuHEICQnB1atX8cYbbyAoKAhjxowBAPj5+WHKlCl49dVXERQUZFvStUOHDhg4cCAAYPDgwWjXrh0ee+wxvPXWW7hx4wZeeeUVPPjgg7TyCSGEEEIIIYQQUo9VaqZGWloaWrZsabft999/B8dxDsuojR49GvHx8ZV68OPHj6N///7o378/CgsLMX/+fPTv3x9vv/02BEHAmTNnMHHiRHTv3h0zZsxAdHQ0tm3bBh8fH9sx5s+fj9GjR2PatGkYMWIEvLy88P3330MQBACAIAhYs2YNPD09MWLECEybNg1jx47FW2+9VakYCSGEEEIIIYQQUjdVaqaGXq936B5+4MABcByH7t27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y7TfQYzpEIA9IyIiIiIiijAyORyDR8IxeGSg94SCDEMNH5Sr3my0TNRGw/LAb2C/djQgCAHYKyIiIiIiIiKqw1DjCtn7XQvLjCcgdogP9K4QERERERERERhqNElUa2G5/1HYr7+ZozOIiIiIiIiIgghDDT/svQfB8tBTEDslBnpXiIiIiIiIiOgyDDV8ME//Pewj7+DoDCIiIiIiIqIgxVDDB/uNdwZ6F4iIiIiIiIjID0mgd4CIiIiIiIiIqCUYahARERERERFRSGKoQUREREREREQhiaEGEREREREREYUkhhpEREREREREFJIYahARERERERFRSGKoQUREREREREQhiaEGEREREREREYUkhhpEREREREREFJIYahARERERERFRSGKoQUREREREREQhiaEGEREREREREYUkhhpEREREREREFJIYahARERERERFRSGKoQUREREREREQhiaEGEREREREREYUkhhpEREREREREFJIYahARERERERFRSArqUGPBggWIi4tr8JGVleVZL4oiFixYgJycHCQlJeG2225Dfn5+g8eoqqrC7NmzkZqaitTUVMyePRtVVVXt/EyIiIiIiIiIqLUFdagBAJmZmSgoKPB8bNu2zbPujTfewJIlS7Bw4UL88MMPSEhIwLhx41BbW+vZZtasWTh06BDWrl2LtWvX4tChQ5gzZ04gngoRERERERERtSJZoHegKTKZDDqdrtFyURTx97//Hb/97W9x1113AQD+/ve/IzMzE2vXrsWMGTNQUFCA77//Hv/973+Rl5cHAHj99ddxyy23oLCwEJmZme36XIiIiIiIiFpKFEX852czXj9ci8KLaowtrsTMHC2GJCogCEKgd48oIIJ+pMapU6eQk5ODvn37YubMmTh16hQA4PTp0ygpKcGoUaM826rVagwdOhQ7d+4EAOzatQtRUVEYMmSIZ5trr70WWq3Wsw0REREREVGw23LBgjFflWHKD5XYU2ZDtV3Ax0Um3Pyfcgz7rBTv5utRY3UGejeJ2l1Qj9QYNGgQ3nrrLWRmZqK8vByvvfYaxowZgx07dqCkpAQAkJCQ0OBnEhIScP78eQBAaWkpOnXq1CC1FAQB8fHxKC0t9fu7CwsLW/nZEFGw4eucKPzxdU5Eoa5AL2DJaQW2X5T63OZIlR1P7qjGH3dVYWyCA/d0tiEnSmzHvSRq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QyaT4e6778bFixc927zxxhtYsmQJFi5ciB9++AEJCQkYN24camtrPdtYLBbcfvvtmDt3rtffc/jwYUycOBEjR47Epk2bsGzZMnz99deYP39+Wz9FIiIiIiIiInIL60aher0eqampWLVqFW655RaIooicnBw8/PDDeOKJJwAAJpMJmZmZePHFFzFjxowGP79u3TpMmzYNVVVVDZa/8MIL+O6777B582bPsq+//hozZsxAYWEhoqOj2/y5EREREREREUW6sBqpcTm9Xg+n0+kpITl9+jRKSkowatQozzZqtRpDhw7Fzp07r/hxLRYLVCpVg2VqtRpmsxkHDhxojV0nIiIiIiIioiaEdagxb948XHPNNcjLywMAlJSUAAASEhIabJeQkIDS0tIrftzRo0djz549WLNmDex2O4qLi7Fw4cIGv4OIiIiIiIiI2lbYhhrPPvssduzYgRUrVkAqlbbqY48aNQovvvginnzySeh0OgwaNAhjxowBAEgkYftPSkRERERERBRUwvIK/JlnnsG//vUvfP7550hLS/Ms1+l0AICysrIG25eVlSExMbFZv+PRRx/F6dOn8dNPP+HEiRO49dZbAaDB7yMiIiIiIiKithN2ocbTTz/tCTSysrIarOvWrRt0Oh02bNjgWWY2m7F9+3YMGTKk2b9LEAR07twZarUaa9euRUpKCvr163fVz4GIiIiIiIiImiYL9A60pieeeAJr1qzBypUrERcX5+lvodVqERUVBUEQMHfuXCxevBiZmZnIyMjAokWLoNVqMWHCBM/jnDlzBhcvXsTPP/8MADh06BAAID09HVFRUQCAv/71rxg9ejQkEgm++OIL/OUvf8Hy5ctbvdSFiIiIiIiIiLwLqyld62Y5udzTTz+NZ555BgAgiiJeeeUVvP/++6iqqkJubi4WLVqEXr16ebafO3cuVq9e3ehxvvjiC1x//fUAgDvuuAMHDx6E1WpFnz598PTTT+Omm25q/SdFRERERERERF6FVahBRERERERERJEj7HpqEBEREREREVFkYKhBRERERERERCGJoQYRERERERERhSSGGkREREREREQUkhhqEBEREREREVFIYqhBRERERERERCGJoQYRERERERERhSSGGkREREREREQUkhhqEBERUVBZtWoV4uLiPB86nQ45OTkYP348/vGPf6C2trZFj3v06FEsWLAAp0+fbuU9JiIiokCRBXoHiIiIiLyZN28eunfvDpvNhtLSUmzZsgXPPPMMlixZgtWrV6NPnz7NeryCggIsXLgQw4cPR7du3dpor4mIiKg9MdQgIiKioDR69GgMHjzY8/3vf/97/Pjjj5g8eTLuu+8+7Nq1C2q1OoB7SERERIHG8hMiIiIKGSNGjMCTTz6JM2fO4OOPPwYA/PTTT/jVr36F/v37Q6fTIT09HTNnzsSZM2c8P7dq1SpMmzYNAHDHHXd4SltWrVrl2Wbfvn2YOHEiUlNTkZSUhJtvvhmbNm1q3ydIREREzcJQg4iIiELKpEmTAAA//PADAGDDhg04fvw4Jk+ejFdffRUPPvggvv/+e9x+++0wGo0AgGHDhmHOnDkAgMcffxxvv/023n77bQwbNgwAsGXLFtxyyy24ePEinnzyScyfPx8WiwXjx4/H5s2bA/AsiYiI6EoIVVVVYqB3goiIiKjOqlWr8Mgjj+C7775rUH5SX2pqKtLS0rBp0yYYjUZoNJoG63fu3ImxY8fi7bff9oQg69atw7Rp0/DFF1/g+uuv92wriiLy8vKQnJyMzz77DIIgAACsVituuOEGxMTE4Ntvv22jZ0tERERXgyM1iIiIKORERUVBr9cDQINAQ6/Xo7KyEhkZGYiNjcWBAweafKzDhw+jsLAQEyZMQGVlJSoqKlBRUYHa2lqMHDkSe/bs8Yz4ICIiouDCRqFEREQUcvR6PeLj4wEAVVVVmD9/PtatW4eLFy822K6mpqbJxzpx4gQA4LHHHsNjjz3mdZvKyspGo0GIiIgo8BhqEBERUUg5d+4campqkJ6eDgCYPn06du7ciUceeQR9+/ZFdHQ0BEHAzJkz4XQ6m3y8um3mz5+P/v37e92mLkAhIiKi4MJQg4iIiELKmjVrAACjRo1CVVUVNm7ciHnz5mHevHmebcxmM6qqqq7o8bp37w7AVdIycuTI1t5dIiIiakPsqUFEREQh48cff8Rrr72Gbt264d5774VE4jqVEcWGfc/feuutRqM0tFotADQKO/r374/09HQsWbIEtbW1jX5neXl5Kz4DIiIiak0cqUFERERBaf369SgqKoLdbkdZWRk2bdqEDRs2oGvXrli9ejVUKhVUKhWGDx+Ov/71r7DZbOjatSu2b9+Obdu2oWPHjg0er2/fvpBKpXj99ddRXV0NtVqN3NxcpKWl4c0338SECRNw7bXXYsqUKejSpQvOnz+PrVu3QhRFfPnllwH6VyAiIiJ/GGoQERFRUHrllVcAAAqFAh06dECvXr2wYMECTJkyBdHR0Z7tli5dinnz5mH58uWw2+0YOnQoPv/8c9x1110NHi8xMRFvvPEGFi9ejN/85jdwOBxYsmQJ0tLSMGzYMHz33Xd47bXX8N5776G2thaJiYkYOHAgHnzwwXZ93kRERHTlhKqqKrHpzYiIiIiIiIiIggt7ahARERERERFRSGKoQUREREREREQhiaEGEREREREREYUkhhpEREREREREFJIYahARERERERFRSGKoQUREREREREQhiaEGEREREREREYUkhhpEREREREREFJIYahARERERERFRSPr/LjEOdzFHV0YAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 1152x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Step 8, graph the resampled DataFrame from Step 7\n",
    "new_df_pivot.plot(figsize=(16,5))\n",
    "plt.style.use('fivethirtyeight')\n",
    "#new_df_pivot_df.plot\n",
    "# Create the plot with ax.plt()\n",
    "plt.xlabel(\"Date\")\n",
    "plt.ylabel(\"Fare($USD)\")\n",
    "plt.title(\"Total Fare by City Type\")\n",
    "plt.savefig(\"PyBer_fare_summary.png\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e2b2946",
   "metadata": {},
   "outputs": []
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
