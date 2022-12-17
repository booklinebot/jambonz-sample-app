# Sample Jambonz app

This is a sample [Jambonz](https://github.com/jambonz) application for troubleshooting issues.

You can run this app locally with this poetry script after you have installed its dependencies.

```bash
poetry install
poetry run start
```

This app is also available as a docker image on ghcr.io. You can run it with:

```bash
docker run -p 5000:5000 ghcr.io/booklinebot/jambonz-sample-app:master
```

It can be deployed on a K8s cluster using Helm:

```bash
helm upgrade --install sample-app --create-namespace charts/sample-app
```

Or it can be used directly from the public URL from our development cluster `public-apps.dev.bookline.io`.
