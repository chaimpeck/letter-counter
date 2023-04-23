import base64
import io
import matplotlib.pyplot as plt

import matplotlib

matplotlib.use("agg")


def get_dist_plot(dist, format="png"):
    plt.clf()

    names = list(dist.keys())
    values = [v * 100 for v in dist.values()]
    plt.bar(names, values)
    plt.ylabel("%")

    bytes = io.BytesIO()
    plt.savefig(bytes, format=format)
    bytes.seek(0)
    return base64.b64encode(bytes.read()).decode()
