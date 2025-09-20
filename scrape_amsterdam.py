#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import json

def scrape_amsterdam_results():
    url = "https://swimrun.amsterdam/de-wedstrijd/uitslagen2025/"
    
    try:
        print(f"Scraping: {url}")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Zoek naar uitslagen data
        results = []
        
        # Zoek naar tabellen of lijsten met uitslagen
        tables = soup.find_all('table')
        lists = soup.find_all(['ul', 'ol'])
        
        print(f"Gevonden {len(tables)} tabellen en {len(lists)} lijsten")
        
        # Zoek naar tekst die lijkt op uitslagen
        text_content = soup.get_text()
        
        # Zoek naar patronen die lijken op uitslagen
        patterns = [
            r'(\d+)\s+([A-Za-z\s]+)\s+(\d+:\d+:\d+)',  # Positie Naam Tijd
            r'([A-Za-z\s]+)\s+(\d+:\d+:\d+)',  # Naam Tijd
            r'(\d+)\s+([A-Za-z\s]+)',  # Positie Naam
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text_content)
            if matches:
                print(f"Gevonden {len(matches)} matches met patroon: {pattern}")
                for match in matches[:10]:  # Toon eerste 10 matches
                    print(f"  {match}")
        
        # Zoek naar specifieke tekst die uitslagen bevat
        lines = text_content.split('\n')
        result_lines = []
        
        for line in lines:
            line = line.strip()
            if any(keyword in line.lower() for keyword in ['uitslag', 'result', 'tijd', 'plaats', 'naam']):
                result_lines.append(line)
        
        print(f"\nGevonden {len(result_lines)} relevante regels:")
        for line in result_lines[:20]:  # Toon eerste 20 relevante regels
            print(f"  {line}")
        
        # Zoek naar JSON data of andere gestructureerde data
        scripts = soup.find_all('script')
        for script in scripts:
            if script.string and ('result' in script.string.lower() or 'uitslag' in script.string.lower()):
                print(f"Gevonden script met uitslagen data: {script.string[:200]}...")
        
        return results
        
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

if __name__ == "__main__":
    results = scrape_amsterdam_results()
    print(f"\nTotaal {len(results)} resultaten gevonden")
