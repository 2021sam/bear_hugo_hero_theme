
---

### ✅ Step 1: **List all services**

See if there’s a similarly named service:

```bash
systemctl list-units --type=service | grep gunicorn
```

This will help you spot any typos or similar names (e.g., `gunicorn`, `gunicorn_zyxe_app`, etc.)

---

### ✅ Step 2: **Check for service files**

Look in the systemd directory for your service file:

```bash
ls /etc/systemd/system/ | grep gunicorn
```

Or:

```bash
sudo find /etc/systemd/system -name '*gunicorn*'
```

---

### ✅ Step 3: **If it’s missing, you need to create it**

If you don’t have a `gunicorn_zyxe.service`, create one. Here's a basic example:

```ini
# /etc/systemd/system/gunicorn_zyxe.service
[Unit]
Description=gunicorn daemon for Zyxe
After=network.target

[Service]
User=pi
Group=www-data
WorkingDirectory=/home/pi/zyxe
ExecStart=/home/pi/zyxe/venv/bin/gunicorn --workers 3 --bind unix:/home/pi/zyxe/zyxe.sock wsgi:app

[Install]
WantedBy=multi-user.target
```

Make sure you replace paths, usernames, and `wsgi:app` according to your project.

Then reload and enable:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable gunicorn_zyxe
sudo systemctl start gunicorn_zyxe
```

---

Let me know if you’re trying to serve a **Hugo** site — in that case, you don’t need Gunicorn at all. Hugo is a static site and can be served directly by Nginx.



Thanks — that clears it up!

Your active service is named:

```
zyxe_gunicorn.service
```

### ✅ 🔁 Use:

```bash
sudo systemctl restart zyxe_gunicorn
```

If you're not sure whether the name is correct, you can also do:

```bash
sudo systemctl status zyxe_gunicorn
```

That will confirm it's the correct and currently active Gunicorn service.

Let me know if you want to **rename** the service to `gunicorn_zyxe.service` — it's totally doable, but optional.
