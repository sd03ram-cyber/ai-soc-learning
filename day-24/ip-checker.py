#!/usr/bin/env python3
"""
IP Reputation Checker — Query AbuseIPDB and VirusTotal APIs.
Requires: pip install requests
Free API keys: AbuseIPDB (3000 queries/day), VirusTotal (free tier has limits)
"""

import requests
import sys
import os
from typing import Optional


def check_abuseipdb(ip: str, api_key: Optional[str] = None) -> dict:
    """Query AbuseIPDB for IP reputation."""
    if not api_key:
        api_key = os.getenv("ABUSEIPDB_API_KEY")
    
    if not api_key:
        return {"error": "AbuseIPDB API key not found. Set ABUSEIPDB_API_KEY env var."}
    
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90,
        "verbose": ""
    }
    headers = {
        "Key": api_key,
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "ip": ip,
                "abuse_confidence_score": data["data"].get("abuseConfidenceScore", "N/A"),
                "total_reports": data["data"].get("totalReports", 0),
                "is_whitelisted": data["data"].get("isWhitelisted", False),
            }
        else:
            return {"error": f"AbuseIPDB error: {response.status_code}"}
    except Exception as e:
        return {"error": f"AbuseIPDB exception: {str(e)}"}


def check_virustotal(ip: str, api_key: Optional[str] = None) -> dict:
    """Query VirusTotal for IP reputation."""
    if not api_key:
        api_key = os.getenv("VIRUSTOTAL_API_KEY")
    
    if not api_key:
        return {"error": "VirusTotal API key not found. Set VIRUSTOTAL_API_KEY env var."}
    
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": api_key}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            stats = data["data"]["attributes"]["last_analysis_stats"]
            return {
                "ip": ip,
                "malicious": stats.get("malicious", 0),
                "undetected": stats.get("undetected", 0),
                "total_vendors": sum(stats.values()),
                "last_analysis_date": data["data"]["attributes"].get("last_analysis_date", "N/A"),
            }
        else:
            return {"error": f"VirusTotal error: {response.status_code}"}
    except Exception as e:
        return {"error": f"VirusTotal exception: {str(e)}"}


def print_report(ip: str, abuse_result: dict, vt_result: dict):
    """Print reputation report."""
    print(f"\n[IP Reputation Report: {ip}]\n")
    
    if "error" not in abuse_result:
        print(f"AbuseIPDB:")
        print(f"  Abuse Confidence Score: {abuse_result['abuse_confidence_score']}%")
        print(f"  Total Reports: {abuse_result['total_reports']}")
        print(f"  Whitelisted: {abuse_result['is_whitelisted']}")
    else:
        print(f"AbuseIPDB: {abuse_result['error']}")
    
    print()
    
    if "error" not in vt_result:
        print(f"VirusTotal:")
        print(f"  Malicious Vendors: {vt_result['malicious']}")
        print(f"  Undetected: {vt_result['undetected']}")
        print(f"  Total Vendors: {vt_result['total_vendors']}")
        print(f"  Last Analysis: {vt_result['last_analysis_date']}")
    else:
        print(f"VirusTotal: {vt_result['error']}")
    
    print()
    print("Interpretation:")
    if "error" not in abuse_result and abuse_result['abuse_confidence_score'] > 75:
        print(f"  ⚠️  HIGH RISK: {ip} shows strong abuse signals.")
    elif "error" not in vt_result and vt_result['malicious'] > 10:
        print(f"  ⚠️  MALICIOUS: {vt_result['malicious']} vendors flag this as malicious.")
    else:
        print(f"  ✓ LOW RISK: {ip} appears clean (or insufficient data).")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ip-checker.py <IP_ADDRESS>")
        print("Example: python3 ip-checker.py 203.0.113.5")
        print("\nRequires API keys:")
        print("  ABUSEIPDB_API_KEY - get free at https://www.abuseipdb.com")
        print("  VIRUSTOTAL_API_KEY - get free at https://www.virustotal.com")
        sys.exit(1)
    
    ip = sys.argv[1]
    print(f"Checking {ip}...")
    
    abuse_result = check_abuseipdb(ip)
    vt_result = check_virustotal(ip)
    
    print_report(ip, abuse_result, vt_result)
