This folder contains several sample dashboards created with Apache Superset. You can view this dashboard by using Superset's import function. In order for the visualizations to work, data sources must be configured as well.

![Screenshot from 2019-06-05 14-12-15](https://user-images.githubusercontent.com/35980900/58979608-67585180-879c-11e9-96d8-f613c02aa519.png)

The first dashboard is just an example to show the variety of visualizations included with superset. The data used is a collection of datasets included with the Superset installation as well as a google play store dataset on kaggle.
The dashboard should look something like this:

![Screenshot from 2019-06-05 14-12-37](https://user-images.githubusercontent.com/35980900/58979664-8820a700-879c-11e9-93b7-2679909dd145.png)

The remaining dashboards are intended to demonstrate some potential use cases for Superset.  `cpu_insights.json` visualizes a number of metrics from a CPU dataset. The data used here is for internal use only.

![Screenshot from 2019-06-24 16-24-32](https://user-images.githubusercontent.com/35980900/61555520-99acce00-aa2d-11e9-9e71-49f2ab1babc7.png)

Both `ceph_dashboard.json` and `ceph_interactive.json` are intended to be used with an ongoing project to predict hard drive failures.  `ceph_dashboard.json` provides a general overview of the dataset including some basic counts of failures, distributions of hard drive providers, and time series plots of drive failures.  `ceph_interactice` provides an interactive dashboard for examining potential differences in SMART metrics between working drives and failed ones.  The dataset comes from backblaze and can be found at https://www.backblaze.com/b2/hard-drive-test-data.html.

![Screenshot from 2019-07-19 13-38-33](https://user-images.githubusercontent.com/35980900/61555464-7b46d280-aa2d-11e9-8b2a-1f6c02825dd7.png)

![Screenshot from 2019-07-19 13-37-50](https://user-images.githubusercontent.com/35980900/61555490-8d287580-aa2d-11e9-8723-965601c95055.png)
