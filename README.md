# Azure Functions with Serverless Framework

## prepare job

- Node.js 8.x이상 설치
- npm i -g serverless (serverless 설치)

## prepare azure creadential

### 1. Download the Azure CLI or use the Azure Cloud Shell

- https://learn.microsoft.com/en-us/cli/azure/install-azure-cli

### 2. Login To Azure & Get your subscription ad tenant id

```sh
$ az login
$ az account list
{
  "cloudName": "AzureCloud",
  "id": "<subscriptionId>",
  "isDefault": true,
  "name": "My Azure Subscription",
  "registeredProviders": [],
  "state": "Enabled",
  "tenantId": "5bc10873-159c-4cbe-a7c9-bce05cb065c1",
  "user": {
    "name": "hello@example.com",
    "type": "user"
  }
}
```

### 3. set subscription

```sh
$ az account set -s <subscriptionId>
```

### 4. Create a service principal

```sh
$ az ad sp create-for-rbac
```

### 5. Create .env

```sh
cp .env.sample .env
# 키 작성
OPENAI_API_KEY=YOUR_API_KEY
OPENAI_ENDPOINT=YOUR_ENDPOINT
OPENAI_MODEL_NAME=YOUR_MODEL_NAME
```

### 6. deploy function

```sh
$ sls deploy -s dev
```

Refer to [Serverless docs](https://serverless.com/framework/docs/providers/azure/guide/intro/) for more information.
