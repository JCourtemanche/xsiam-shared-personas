# xsiam-shared-personas

Shared personas and threat indicators for Cortex XSIAM simulator projects.

## What's inside

| Constant | Description |
|---|---|
| `DOMAIN` | `"business.org"` — fictional company domain |
| `COMPANY_NAME` | `"Business Corp"` |
| `USERS` | 6 personas with name, email, hostname, IP, OS |
| `INTERNAL_IPS` | `192.168.1.1` – `192.168.1.10` |
| `MALICIOUS_IPS` | Fixed list of C2/malicious IPs |
| `MALICIOUS_DOMAINS` | Fixed list of phishing/C2 domains |
| `MALICIOUS_URLS` | Full malicious URLs with paths |
| `MALICIOUS_FILES` | File names + hashes for malware simulation |

## Installation

```bash
pip install git+https://github.com/JCourtemanche/xsiam-shared-personas.git
```

## Usage

```python
from xsiam_shared import USERS, MALICIOUS_IPS, DOMAIN
import random

user = random.choice(USERS)
print(user["email"])        # alice.dupont@business.org
print(user["hostname"])     # BSNS-WIN-ALICE
print(user["internal_ip"])  # 192.168.1.1
```

## Personas

| Name | Email | Hostname | IP | OS |
|---|---|---|---|---|
| Alice Dupont | alice.dupont@business.org | BSNS-WIN-ALICE | 192.168.1.1 | Windows 10 Pro |
| Bob Martin | bob.martin@business.org | BSNS-MAC-BOB | 192.168.1.2 | macOS 13 Ventura |
| Charlie Durant | charlie.durant@business.org | BSNS-WIN-CHARLIE | 192.168.1.3 | Windows 11 Pro |
| David Lefebvre | david.lefebvre@business.org | BSNS-WIN-DAVID | 192.168.1.4 | Windows 10 Pro |
| Emma Leroy | emma.leroy@business.org | BSNS-MAC-EMMA | 192.168.1.5 | macOS 14 Sonoma |
| Flora Moreau | flora.moreau@business.org | BSNS-MOB-FLORA | 192.168.1.6 | iOS 17 |

## Projects using this package

- [proofpoint-tap-simulator](https://github.com/JCourtemanche/proofpoint-tap-simulator)
- [sentinelone-simul](https://github.com/JCourtemanche/sentinelone-simul)
- [cato-networks-simul](https://github.com/JCourtemanche/cato-networks-simul)
