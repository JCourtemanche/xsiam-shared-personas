"""
Shared personas and threat data for XSIAM simulator projects.

Single source of truth for the fictional company "Business Corp" (business.org).
All simulators (ProofPoint TAP, SentinelOne, Cato Networks, etc.) import from here
so that the same users, machines, IPs, and threat indicators appear consistently.
"""

DOMAIN = "business.org"
COMPANY_NAME = "Business Corp"
ACCOUNT_ID = "BC-42781"

# ---------------------------------------------------------------------------
# Internal users / personas
# Each user has every field needed by any simulator:
#   name, first_name, last_name, username, email,
#   hostname, internal_ip, os_type, os_name
# ---------------------------------------------------------------------------
USERS = [
    {
        "name": "Alice Dupont",
        "first_name": "Alice",
        "last_name": "Dupont",
        "username": "alice.dupont",
        "email": "alice.dupont@business.org",
        "hostname": "BSNS-WIN-ALICE",
        "internal_ip": "192.168.1.1",
        "os_type": "windows",
        "os_name": "Windows 10 Pro",
        "machine_type": "laptop",
    },
    {
        "name": "Bob Martin",
        "first_name": "Bob",
        "last_name": "Martin",
        "username": "bob.martin",
        "email": "bob.martin@business.org",
        "hostname": "BSNS-MAC-BOB",
        "internal_ip": "192.168.1.2",
        "os_type": "macos",
        "os_name": "macOS 13 Ventura",
        "machine_type": "laptop",
    },
    {
        "name": "Charlie Durant",
        "first_name": "Charlie",
        "last_name": "Durant",
        "username": "charlie.durant",
        "email": "charlie.durant@business.org",
        "hostname": "BSNS-WIN-CHARLIE",
        "internal_ip": "192.168.1.3",
        "os_type": "windows",
        "os_name": "Windows 11 Pro",
        "machine_type": "desktop",
    },
    {
        "name": "David Lefebvre",
        "first_name": "David",
        "last_name": "Lefebvre",
        "username": "david.lefebvre",
        "email": "david.lefebvre@business.org",
        "hostname": "BSNS-WIN-DAVID",
        "internal_ip": "192.168.1.4",
        "os_type": "windows",
        "os_name": "Windows 10 Pro",
        "machine_type": "desktop",
    },
    {
        "name": "Emma Leroy",
        "first_name": "Emma",
        "last_name": "Leroy",
        "username": "emma.leroy",
        "email": "emma.leroy@business.org",
        "hostname": "BSNS-MAC-EMMA",
        "internal_ip": "192.168.1.5",
        "os_type": "macos",
        "os_name": "macOS 14 Sonoma",
        "machine_type": "laptop",
    },
    {
        "name": "Flora Moreau",
        "first_name": "Flora",
        "last_name": "Moreau",
        "username": "flora.moreau",
        "email": "flora.moreau@business.org",
        "hostname": "BSNS-MOB-FLORA",
        "internal_ip": "192.168.1.6",
        "os_type": "ios",
        "os_name": "iOS 17",
        "machine_type": "mobile",
    },
]

# ---------------------------------------------------------------------------
# Internal network
# ---------------------------------------------------------------------------
INTERNAL_SUBNET = "192.168.1"
INTERNAL_IPS = [f"192.168.1.{i}" for i in range(1, 11)]

# Convenience: map hostname → user dict
USERS_BY_HOSTNAME = {u["hostname"]: u for u in USERS}
USERS_BY_EMAIL = {u["email"]: u for u in USERS}

# ---------------------------------------------------------------------------
# Threat indicators — same across all simulators
# ---------------------------------------------------------------------------
MALICIOUS_IPS = [
    "185.15.56.11",
    "93.12.33.44",
    "45.22.11.99",
    "103.45.67.89",
    "193.143.1.15",
    "134.19.179.155",
    "193.106.191.253",
]

MALICIOUS_DOMAINS = [
    "evil-phishing.com",
    "malware-download.xyz",
    "c2-server-botnet.net",
    "xtrg.gtrsiss.icu",
    "tufozequwyd.eu",
    "volugomymet.eu",
]

MALICIOUS_URLS = [
    "http://evil-phishing.com/login.php",
    "http://malware-download.xyz/download/payload.exe",
    "http://c2-server-botnet.net/update",
    "http://xtrg.gtrsiss.icu/auth",
    "http://tufozequwyd.eu/invoice.html",
    "http://volugomymet.eu/tracking.php",
]

MALICIOUS_FILES = [
    {"name": "invoice_payload.exe", "hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"},
    {"name": "update_setup.msi",    "hash": "a87ff679a2f3e71d9181a67b7542122c9aa1f6e9"},
    {"name": "document_scan.pdf.exe", "hash": "d41d8cd98f00b204e9800998ecf8427e"},
]
