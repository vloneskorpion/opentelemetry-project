To run the project, you need to have docker installed on your machine.

```bash
   docker compose up --build
```

You can access grafana on http://localhost:3000 and prometheus on http://localhost:9090
In grafana go to dashboards -> Python-App dashboard to see metrics

To generate request metrics:
```bash
   curl http://localhost:8080
```

To generate load which will raise grafana alarm:
```bash
    while true; do curl http://localhost:8080; sleep 0.5; done
```
