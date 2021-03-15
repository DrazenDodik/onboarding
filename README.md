# Valohai Onboarding - Sample Project :shark::rocket:

## Prerequisites
* Python 3 and pip

## Setup
* `pip3 install valohai-cli`
* `vh login`
* Install the Python helper library `pip3 install valohai-utils` 
* (optional) Install the Jupyter notebook addon
    * `pip3 install notebook`
    * `pip3 install jupyhai`
    * `jupyhai install`

## Snippets

**MNIST Dataset:** https://onboard-sample.s3-eu-west-1.amazonaws.com/tf-sample/mnist.npz
```python
default_inputs = {
  'mnist': 'https://onboard-sample.s3-eu-west-1.amazonaws.com/tf-sample/mnist.npz'
}
```

And use it like `valohai.inputs('mnist').path()`

**Log metadata:**
```python
def logMetadata(epoch, logs):
  with valohai.metadata.logger() as logger:
		logger.log("epoch", epoch)
		logger.log("accuracy", logs['accuracy'])
		logger.log("loss", logs['loss'])
```

**Parse arguments:**
```python
default_parameters = {
  'epoch': 6
}
```
And use it like `valohai.parameters('epoch').value`

**Create step:**
```python
valohai.prepare(step='train', default_parameters=default_parameters, default_inputs=default_inputs)
```

And run `vh yaml step train.py`

**Deployment (yaml):**
```yaml
- endpoint:
    name: digit-predict
    description: predict digits from image inputs
    image: tensorflow/tensorflow:2.0.1
    wsgi: predict:mypredictor
    files:
        - name: model
          description: Model output file from TensorFlow
          path: model.h5
```

**Pipeline:**

* Create a new deployment in your project called `mydeployment`

```yaml

- pipeline:
    name: Train and deploy pipeline
    nodes:
      - name: train-node
        type: execution
        step: Train MNIST model
      - name: deploy-node
        type: deployment
        deployment: mydeployment
        endpoints:
          - digit-predict
    edges:
      - [train-node.output.model*, deploy-node.file.digit-predict.model]

```

## Further reading
* 🗄 [Setting up your data store](https://docs.valohai.com/tutorials/cloud-storage/)
* 📈 [Using parameters and Tasks](https://docs.valohai.com/tutorials/valohai/advanced/#use-tasks-for-hyperparameter-optimization)
* 🚰 [Chaining executions in pipelines](https://docs.valohai.com/tutorials/valohai/advanced/#create-a-sequence-of-operations-with-pipelines)
* 🐍 [Migrating an existing Python project to Valohai](https://docs.valohai.com/tutorials/migrating-existing-projects/)
* 🐳 [Setup a private container registry](https://docs.valohai.com/docker-images/#access-private-docker-repositories)