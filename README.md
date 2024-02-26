```
# Install the packages
! pip3 install --quiet --upgrade google-cloud-aiplatform \
                                 google-cloud-storage
```

Uncomment the following cell to restart the kernel
```
# Automatically restart kernel after installs so that your environment can access the new packages
# import IPython

# app = IPython.Application.instance()
# app.kernel.do_shutdown(True)
```

Set your project ID
If you don't know your project ID, try the following:

Run gcloud config list.
Run gcloud projects list.
See the support page: https://support.google.com/googleapi/answer/7014113

So basically once the above i installed you should be able to use this

```
Python 3.11.7 (main, Dec  4 2023, 18:10:11) [Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from google.cloud import aiplatform
>>> import vertexai.preview
>>> your code here ......
```
