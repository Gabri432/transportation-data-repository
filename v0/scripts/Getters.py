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
import json

from TransportLine import TransportLine

class Getters:
    @staticmethod
    def get_json_data(path_to_json: str) -> list[TransportLine]:
        with open(path_to_json, 'r') as autog:
            data = json.load(autog)
            return [TransportLine(**transportation_line) for transportation_line in data["lines"]]

    @staticmethod
    def get_company_1_lines_data() -> list[TransportLine]:
        """
        Returns a list of transportation lines related to company 1 (currently just one).
        """
        return Getters.get_json_data('v0/company_1.json')
    
    @staticmethod    
    def get_company_2_lines_data() -> list[TransportLine]:
        """
        Returns a list of transportation lines related to company 2 (currently just one).
        """
        return Getters.get_json_data('v0/company_2.json')