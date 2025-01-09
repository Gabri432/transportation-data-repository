#
# Copyright 2025 Gabriele Gatti
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from enum import Enum

class PeriodEnum(Enum):
    WEEKDAYS = "weekdays"
    SATURDAYS = "saturdays"
    HOLIDAYS = "holidays"


class CityEnum(Enum):
    CITY_1 = "City_1"
    CITY_2 = "City_2"
    CITY_3 = "City_3"
    CITY_4 = "City_4"

class VehicleEnum(Enum):
    BUS = "bus"
    TRAM = "tram"
    TRAIN = "train"
    AIRPLANE = "airplane"
    SHIP = "ship"
    TAXI = "taxi"