# Odoo 17 Development — Learning Repository
 
Personal learning repository following a **Odoo 17 Development Course**

---
 
## Setup
 
- **Odoo version:** 17.0 (Community) 
- **Python:** 3.10.11
- **Database:** PostgreSQL 18
- **IDE:** PyCharm Community
- **OS:** Windows 11
### How to run
 
1. Make sure PostgreSQL is running
2. Open the project in PyCharm
3. Press the Run button (configuration already set up)
4. Open `http://localhost:8069` in your browser
5. Login: `admin` / `admin`
### Project structure
 
```
odoo-Development/
├── odoo17/              # Odoo 17 source code (do not edit)
├── custom_addons/       # All custom modules go here
│   └── ...
├── .venv/               # Python virtual environment
└── odoo.conf            # Odoo configuration file
```
 
---
 
## Custom Modules
 
| Module | Description | Status |
|--------|-------------|--------|
| — | — | — |
 
*(This table will be updated as modules are built throughout the course)*

 
## Notes
 
- Custom modules are built inside `custom_addons/` — never edit the `odoo17/` source
- After modifying Python files, restart the server
- After modifying XML views only, upgrade the module from Apps menu
- To install a new module: Apps → Update Apps List → search → Install
---
 
## About
**Mohamed Tarek** | Cairo, Egypt.