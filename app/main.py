from flask import Flask
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

app = Flask(__name__)

resource = Resource(attributes={
    SERVICE_NAME: "Python-app"
})

reader = PeriodicExportingMetricReader(
    OTLPMetricExporter(endpoint="http://otel-collector:4317"),
    export_interval_millis=1000
)
meterProvider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(meterProvider)

meter = metrics.get_meter(__name__)

request_counter = meter.create_counter(
    "python_app_requests", description="Number of requests"
)

@app.route("/")
def index():
    request_counter.add(1)
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
