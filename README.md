# Valohai Onboarding - Sample Project :shark::rocket:

## Prerequisites
* Python 3 and pip

## Setup
* `pip install valohai-cli`
* `vh login`
* (optional) Install the Jupyter notebook addon
    * `pip install notebook`
    * `pip install jupyhai`
    * `jupyhai install`

## Snippets

**MNIST Dataset:** s3://onboard-sample/tf-sample/mnist.npz

**Log metadata:**
```python
def logMetadata(epoch, logs):
    print()
    print(json.dumps({
        'epoch': epoch,
        'loss': str(logs['loss']),
        'acc': str(logs['accuracy']),
    }))
```

**Parse arguments:**
```python
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epoch', type=int, default=6)
    return parser.parse_args()

args = parse_args()
```

## Further reading
* 🗄 [Setting up your data store](https://docs.valohai.com/tutorials/cloud-storage/)
* 📈 [Using parameters and Tasks](https://docs.valohai.com/tutorials/valohai/advanced/#use-tasks-for-hyperparameter-optimization)
* 🚰 [Chaining executions in pipelines](https://docs.valohai.com/tutorials/valohai/advanced/#create-a-sequence-of-operations-with-pipelines)
* 🐍 [Migrating an existing Python project to Valohai](https://docs.valohai.com/tutorials/migrating-existing-projects/)
* 🐳 [Setup a private container registry](https://docs.valohai.com/docker-images/#access-private-docker-repositories)