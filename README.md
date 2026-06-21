<!--
  GitHub profile README for potato-20.  Updated 2026-06-05.
-->

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&duration=3200&pause=900&color=00C853&background=00000000&center=true&vCenter=true&width=700&height=42&lines=Information+Security+Research+%26+Engineering;Mobile+%C2%B7+Web+%C2%B7+API+%C2%B7+Network+VAPT;I+build+the+tooling+I+pentest+with;OSS%3A+drozer+%C2%B7+MobSF+%C2%B7+nuclei+%C2%B7+prowler" alt="What I do"/>
</p>

<br>

<p align="center">
  <a href="https://www.linkedin.com/in/mayank---patel/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&labelColor=0d1117&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  &nbsp;&nbsp;
  <a href="mailto:iammayank2082@gmail.com"><img src="https://img.shields.io/badge/iammayank2082%40gmail.com-Email-FF1744?style=flat-square&logo=gmail&logoColor=white&labelColor=0d1117" alt="Email"/></a>
  &nbsp;&nbsp;
  <a href="https://medium.com/@myank2082"><img src="https://img.shields.io/badge/Medium-Writing-00C853?style=flat-square&labelColor=0d1117&logo=medium&logoColor=white" alt="Medium"/></a>
  &nbsp;&nbsp;
  <a href="https://linktr.ee/myank2082"><img src="https://img.shields.io/badge/Linktree-All_Links-00C853?style=flat-square&labelColor=0d1117&logo=linktree&logoColor=white" alt="Linktree"/></a>
</p>

<br>
<br>

<p align="center">
  <img src="assets/whoami.svg?v=4" width="100%" alt="mayank@kali:~$ whoami --verbose — Security Researcher & Engineer · status: ACTIVE"/>
</p>

<br>

> Security researcher and engineer running manual and
> automated penetration tests across **web, API, network, and mobile** targets for
> government and enterprise clients. I build security tooling in Python — currently
> building an **automated mobile (Android & iOS) penetration-testing agent** — and
> I contribute upstream to the tools I actually use: **drozer, MobSF, nuclei-templates**.

<br>
<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0D1117,100:00C853&height=2&section=header" width="100%" alt="---"/>

<br>

### `[ 01 ]`&nbsp;&nbsp; what i do

<br>

- Manual + automated **VAPT** across web, API, network, and mobile, under direct CTO supervision
- Identify **critical & high-severity findings across 20+ client engagements** and deliver remediation guidance
- Build **Python / Docker** security-testing automation for DAST & SAST pipelines
- Threat modeling, risk assessment, and **digital-forensics** investigations
- Triage **1,000+ security events** from DevSecOps tooling; deploy & tune **Cloudflare WAF**
- Operate against **NIST · ISO 27001/27017 · PCI DSS · GDPR** frameworks

<br>
<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0D1117,100:00C853&height=2&section=header" width="100%" alt="---"/>

<br>

### `[ 02 ]`&nbsp;&nbsp; flagship project

<br>

**Autonomous Mobile Penetration Testing Agent.** An LLM-orchestrated pipeline
(**LangGraph + Claude**) that runs static, dynamic, and network assessments across
**Android & iOS**, with a human checkpoint at every stage gate.

- **29 static analyzers** — manifest, secrets, crypto-misuse, native libs, Firebase rules, trackers, deep-links, WebView, and **Ghidra headless** decompilation
- **21 iOS Frida hooks** — SSL unpinning, jailbreak bypass, keychain/biometric capture, NSURLSession & WKWebView logging, anti-debug bypass
- **20 network / API testers** — IDOR, injection, mass-assignment, race conditions, auth/session, TLS, plus **ZAP & mitmproxy** integration
- Findings mapped to **OWASP MASTG / NIAP** · exposed over an **MCP server** · runs on WSL2, Windows, macOS & Linux

<br>

<p align="left">
  <img src="https://img.shields.io/badge/status-in_active_development-FFB300?style=for-the-badge&labelColor=0d1117" alt="status: in active development"/>
  &nbsp;
  <img src="https://img.shields.io/badge/source-private-8b949e?style=for-the-badge&labelColor=0d1117" alt="source: private"/>
</p>

<br>
<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0D1117,100:00C853&height=2&section=header" width="100%" alt="---"/>

<br>

### `[ 03 ]`&nbsp;&nbsp; open-source contributions

<br>

> **I don't just use security tools — I fix and extend them.** <br>
> **14 PRs · 10 projects · 7 merged** — including upstream merges into NSA **Ghidra**, **Prowler**, ProjectDiscovery **nuclei**, **sqlmap** &amp; **testssl**. <br>
> Reaching across **mobile · web · cloud · reverse-engineering · TLS · WAF · SIEM** — patches where it counts.

<br>

<div align="center">

| Project | PR | Contribution | State |
|---|---|---|:--:|
| **NSA / ghidra** | [#9249](https://github.com/NationalSecurityAgency/ghidra/pull/9249) | Sanitize generated label name in AutoRenameSimpleLabels | **merged ✓** |
| **prowler** | [#11471](https://github.com/prowler-cloud/prowler/pull/11471) | AWS FSBP **ELB.4** — ALB drop-invalid-header-fields check | **merged ✓** |
| **nuclei-templates** | [#16339](https://github.com/projectdiscovery/nuclei-templates/pull/16339) | Homarr Dashboard exposed-panel detection template | **merged ✓** |
| **sqlmap** | [#6066](https://github.com/sqlmapproject/sqlmap/pull/6066) | Fix no-op `chardet` patch in `dirtyPatches()` | **merged ✓** |
| **testssl.sh** | [#3049](https://github.com/testssl/testssl.sh/pull/3049) | Fix `--mx host:port` parsing + no-MX message | **merged ✓** |
| **testssl.sh** | [#3050](https://github.com/testssl/testssl.sh/pull/3050) | Report additional modern security headers (INFO) | **merged ✓** |
| **ReversecLabs / drozer** | [#500](https://github.com/ReversecLabs/drozer/pull/500) | Fix infinite loop in `fs.md5sum` / `fs.sha1sum` on Python 3 | open |
| **ReversecLabs / drozer** | [#499](https://github.com/ReversecLabs/drozer/pull/499) | Add initial `pytest` unit-test suite + CI | open |
| **MobSF** | [#2618](https://github.com/MobSF/Mobile-Security-Framework-MobSF/pull/2618) | Android WebView mixed-content detection rule | open |
| **nmap** | [#3379](https://github.com/nmap/nmap/pull/3379) | NATS server version detection (+ MongoDB mis-ID fix) | open |
| **sqlmap** | [#6067](https://github.com/sqlmapproject/sqlmap/pull/6067) | CockroachDB error-based fingerprints (PostgreSQL fork) | open |
| **OWASP CRS** | [#4655](https://github.com/coreruleset/coreruleset/pull/4655) | Decode URL-encoded payloads in header RCE rules | open |
| **SigmaHQ / sigma** | [#6055](https://github.com/SigmaHQ/sigma/pull/6055) | Detect content-discovery tool User-Agents (ffuf/gobuster) | open |
| **testssl.sh** | [#3060](https://github.com/testssl/testssl.sh/pull/3060) | HSTS preload-list check via hstspreload.org | **merged ✓** |

</div>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/potato-20/potato-20/output/snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/potato-20/potato-20/output/snake.svg" />
    <img src="https://raw.githubusercontent.com/potato-20/potato-20/output/snake-dark.svg" width="100%" alt="A snake eating my GitHub contribution grid" />
  </picture>
</p>

<br>
<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0D1117,100:00C853&height=2&section=header" width="100%" alt="---"/>

<br>

### `[ 04 ]`&nbsp;&nbsp; skills

<br>

<p align="center">
  <img src="assets/skill_monitor.svg?v=4" width="100%" alt="skillmon — language load meters, tool process list, and research activity"/>
</p>

<br>

<p align="center">
  <img src="https://img.shields.io/badge/Frida-00BCD4?style=flat-square" alt="Frida"/>
  &nbsp;
  <img src="https://img.shields.io/badge/objection-546E7A?style=flat-square" alt="objection"/>
  &nbsp;
  <img src="https://img.shields.io/badge/MobSF-FF6F00?style=flat-square" alt="MobSF"/>
  &nbsp;
  <img src="https://img.shields.io/badge/drozer-D32F2F?style=flat-square" alt="drozer"/>
  &nbsp;
  <img src="https://img.shields.io/badge/pymobiledevice3-8E8E93?style=flat-square" alt="pymobiledevice3"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Ghidra-FF4500?style=flat-square&logo=ghidra&logoColor=white" alt="Ghidra"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Burp_Suite-5C4EF0?style=flat-square&logo=burpsuite&logoColor=white" alt="Burp Suite"/>
  &nbsp;
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=FFD43B" alt="Python"/>
</p>

<br>
<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0D1117,100:00C853&height=2&section=header" width="100%" alt="---"/>

<br>

### `[ 05 ]`&nbsp;&nbsp; stats

<br>

<p align="center">
  <img src="assets/stats.svg?v=12" width="100%" alt="stats — commits, repos contributed, upstream OSS PRs"/>
</p>

<br>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=potato-20&bg_color=0d1117&color=00ff41&line=00ff41&point=ffffff&area=true&area_color=003b00&hide_border=true&custom_title=Contribution%20Activity" width="100%" alt="Contribution activity graph"/>
</p>

<br>

<p align="center"><sub>Built in the open · tested only with authorization · India</sub></p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C853,55:0a3d2a,100:0D1117&height=140&section=footer" width="100%" alt="footer"/>
</p>
