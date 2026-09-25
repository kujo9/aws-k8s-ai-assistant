# AWS and Kubernetes chat assistants

Two chat assistants that answer questions about real infrastructure and never change it.

| Folder | Reads | Through |
|--------|-------|---------|
| [kubernetes-assistant/](./kubernetes-assistant/) | A Kubernetes cluster | A Kubernetes MCP server on your laptop |
| [aws-assistant/](./aws-assistant/) | An AWS account | The AWS MCP Server |

Both folders start empty. You build each app file by file, following its lab guide in
[docs/](./docs/).

## Get started

```bash
git clone https://github.com/kserge2001/aws-k8s-ai-chat-assistant.git
cd aws-k8s-ai-chat-assistant
```

Then open [docs/kubernetes-assistant-lab.pdf](./docs/kubernetes-assistant-lab.pdf) and start at step 0.

## Settings and credentials

Each folder gets its own `.env` file, because each app reads different settings. You create it
during the lab.

Git ignores every `.env` and every `kubeconfig` in this repository. Never commit either one: they
hold your Anthropic key and your cluster token.
