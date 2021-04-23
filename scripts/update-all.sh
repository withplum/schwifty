#!/bin/bash

main() {
  for country in "at" "be" "cz" "de" "es" "fi" "hr" "lv" "nl" "pl" "si" "sk"; do
    echo "---> Updating bank registry for: $country";
    python scripts/get_bank_registry_$country.py
  done
}

main
