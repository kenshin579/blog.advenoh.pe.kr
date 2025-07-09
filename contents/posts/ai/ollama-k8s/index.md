---
title: "맥에서 직접 AI 모델 돌려보자! Ollama로 LLM 서버 구축하기"
description: "맥에서 직접 AI 모델 돌려보자! Ollama로 LLM 서버 구축하기"
date: 2025-03-23
update: 2025-03-23
tags:
  - AI
  - ollama
  - LLM
  - ChatGPT
  - llama
---
# Terraform과 Kind로 Kubernetes에 Ollama 배포하기

## 1. 개요

### Ollama 소개
Ollama는 대규모 언어 모델(LLM)을 로컬에서 쉽게 실행할 수 있게 해주는 도구입니다. Docker처럼 간단한 명령어로 다양한 오픈소스 LLM을 다운로드하고 실행할 수 있습니다.

주요 특징:
- 다양한 모델 지원 (Llama, Mistral, Qwen 등)
- REST API 제공
- GPU 가속 지원
- 간편한 모델 관리

### 왜 Kubernetes에서 Ollama를 실행하는가?
OpenAI API는 강력하지만 사용량에 따라 비용이 발생합니다. 간단한 텍스트 생성, 요약, 번역 등의 작업은 Ollama를 통해 무료로 처리할 수 있습니다.

Kubernetes에서 실행하는 이점:
- **확장성**: 필요에 따라 리소스를 조정 가능
- **고가용성**: Pod 재시작 및 자동 복구
- **통합성**: 다른 Kubernetes 애플리케이션과 쉽게 연동
- **리소스 격리**: 네임스페이스를 통한 리소스 관리

## 2. 사전 준비사항

### 필요한 도구들
```bash
# Terraform (IaC 도구)
brew install terraform

# kubectl (Kubernetes CLI)
brew install kubectl

# Kind (Kubernetes in Docker)
brew install kind

# Helm (선택사항, 차트 확인용)
brew install helm
```

### 시스템 요구사항
- macOS (특히 Apple Silicon M1/M4)
- Docker Desktop 설치 및 실행 중
- 최소 8GB RAM (16GB 권장)
- 20GB 이상의 여유 디스크 공간

## 3. Kubernetes에 Ollama 설치

### 3.1 프로젝트 구조 설정
```bash
mkdir ollama-k8s-terraform
cd ollama-k8s-terraform
mkdir -p docs/script
```

### 3.2 Terraform 파일 작성

#### Kind 클러스터 구성 (docs/script/k8s.tf)
Kind 클러스터를 생성하고 NodePort를 설정합니다:

```hcl
# docs/script/k8s.tf
terraform {
  required_providers {
    kind = {
      source  = "tehcyx/kind"
      version = "~> 0.2.1"
    }
  }
}

provider "kind" {}

resource "kind_cluster" "ollama_cluster" {
  name            = "ollama-cluster"
  wait_for_ready  = true
  node_image      = "kindest/node:v1.27.3"
  
  kind_config {
    kind        = "Cluster"
    api_version = "kind.x-k8s.io/v1alpha4"

    node {
      role = "control-plane"
      
      extra_port_mappings {
        container_port = 30025
        host_port      = 30025
        listen_address = "127.0.0.1"
      }
    }

    node {
      role = "worker"
    }
  }
}
```

#### Ollama 배포 (docs/script/infra.tf)
Helm을 통해 Ollama를 배포합니다:

```hcl
# docs/script/infra.tf
terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.11"
    }
  }
}

# Kubernetes Provider 설정
provider "kubernetes" {
  config_path = "~/.kube/config"
  config_context = "kind-ollama-cluster"
}

# Helm Provider 설정
provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
    config_context = "kind-ollama-cluster"
  }
}

# 네임스페이스 생성
resource "kubernetes_namespace" "ollama" {
  metadata {
    name = "ollama"
  }
}

# Ollama Helm Chart 배포
resource "helm_release" "ollama" {
  name       = "ollama"
  namespace  = kubernetes_namespace.ollama.metadata[0].name
  repository = "https://helm.otwld.com/"
  chart      = "ollama"
  version    = "0.61.1"

  values = [
    yamlencode({
      # 이미지 설정
      image = {
        repository = "ollama/ollama"
        tag        = "latest"
        pullPolicy = "IfNotPresent"
      }

      # 서비스 설정
      service = {
        type     = "NodePort"
        port     = 11434
        nodePort = 30025
      }

      # 리소스 설정 (작은 모델용)
      resources = {
        requests = {
          cpu    = "1"
          memory = "4Gi"
        }
        limits = {
          cpu    = "2"
          memory = "8Gi"
        }
      }

      # 스토리지 설정
      persistentVolume = {
        enabled      = true
        size         = "20Gi"
        storageClass = "standard"
      }

      # 환경 변수
      ollama = {
        gpu = {
          enabled = false  # CPU 모드
        }
      }

      # Probe 설정
      livenessProbe = {
        enabled             = true
        path                = "/"
        initialDelaySeconds = 60
        periodSeconds       = 10
        timeoutSeconds      = 5
        successThreshold    = 1
        failureThreshold    = 3
      }

      readinessProbe = {
        enabled             = true
        path                = "/"
        initialDelaySeconds = 30
        periodSeconds       = 5
        timeoutSeconds      = 3
        successThreshold    = 1
        failureThreshold    = 3
      }
    })
  ]

  wait    = true
  timeout = 600
}
```

#### Makefile (docs/script/Makefile)
편리한 명령어 실행을 위한 Makefile:

```makefile
# docs/script/Makefile
.PHONY: help init plan apply destroy clean test

help: ## 도움말 표시
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

init: ## Terraform 초기화
	terraform init

plan: ## 배포 계획 확인
	terraform plan

apply: ## Ollama 클러스터 배포
	terraform apply -auto-approve

destroy: ## 클러스터 삭제
	terraform destroy -auto-approve

clean: destroy ## 모든 리소스 정리
	rm -rf .terraform*
	rm -f terraform.tfstate*

test: ## Ollama API 테스트
	@echo "Ollama API 상태 확인..."
	@curl -s http://localhost:30025/api/tags | jq '.' || echo "API가 아직 준비되지 않았습니다."

logs: ## Ollama Pod 로그 확인
	kubectl logs -n ollama -l app.kubernetes.io/name=ollama -f

status: ## 클러스터 상태 확인
	@echo "=== Nodes ==="
	@kubectl get nodes
	@echo "\n=== Pods ==="
	@kubectl get pods -n ollama
	@echo "\n=== Services ==="
	@kubectl get svc -n ollama
```

### 3.3 배포 실행

1. 터미널에서 script 디렉토리로 이동:
```bash
cd docs/script
```

2. Terraform 초기화:
```bash
make init
```

3. 배포 계획 확인:
```bash
make plan
```

4. Ollama 배포:
```bash
make apply
```

배포가 완료되면 약 2-3분 정도 소요됩니다.

## 4. 트러블슈팅 가이드

### 문제 1: PostStartHook 타임아웃
**증상**: Pod가 `PostStartHookError` 상태로 계속 재시작됨

**원인**: Helm 차트의 기본 설정이 시작 시 모델을 자동으로 다운로드하려고 하는데, 큰 모델의 경우 타임아웃 발생

**해결방법**:
```hcl
# infra.tf에서 models 섹션 제거 또는 주석 처리
# models = {
#   pull = ["llama3:8b"]
# }
```

### 문제 2: 메모리 부족으로 인한 스케줄링 실패
**증상**: `FailedScheduling` 이벤트와 함께 `Insufficient memory` 메시지 표시

**원인**: 노드의 가용 메모리보다 많은 메모리를 요청

**해결방법**:
```hcl
resources = {
  requests = {
    cpu    = "1"
    memory = "4Gi"  # 8Gi에서 4Gi로 감소
  }
  limits = {
    cpu    = "2"
    memory = "8Gi"  # 12Gi에서 8Gi로 감소
  }
}
```

### 문제 3: PVC 생성 실패
**증상**: Pod가 `Pending` 상태에서 멈춤

**원인**: StorageClass가 없거나 PVC가 생성되지 않음

**해결방법**:
```bash
# Kind는 기본적으로 standard StorageClass를 제공
# PVC 상태 확인
kubectl get pvc -n ollama

# 필요시 수동으로 PVC 생성
kubectl apply -f - <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ollama
  namespace: ollama
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: standard
  resources:
    requests:
      storage: 20Gi
EOF
```

## 5. 모델 다운로드 및 테스트

### 5.1 모델 선택 가이드

| 모델 | 크기 | 용도 | 메모리 요구사항 |
|------|------|------|-----------------|
| qwen2.5:0.5b | 400MB | 간단한 텍스트 생성 | 2GB |
| llama3.2:1b | 1.3GB | 기본 대화 | 4GB |
| llama3.2:3b | 2GB | 일반적인 사용 | 6GB |
| llama3:8b | 4.7GB | 고급 작업 | 8-10GB |

### 5.2 모델 다운로드
```bash
# 작은 모델 다운로드 (권장)
curl -X POST http://localhost:30025/api/pull \
  -d '{"name": "qwen2.5:0.5b"}'

# 모델 목록 확인
curl http://localhost:30025/api/tags | jq '.'
```

### 5.3 API 테스트
```bash
# 텍스트 생성
curl -X POST http://localhost:30025/api/generate \
  -d '{
    "model": "qwen2.5:0.5b",
    "prompt": "Kubernetes란 무엇인가요?",
    "stream": false
  }' | jq '.response'
```

### 5.4 Python 예제
```python
import requests
import json

def ollama_generate(prompt, model="qwen2.5:0.5b"):
    url = "http://localhost:30025/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(url, json=payload)
    return response.json()['response']

# 사용 예시
result = ollama_generate("Python으로 Hello World 출력하는 코드를 보여줘")
print(result)
```

## 6. 운영 팁

### 6.1 리소스 모니터링
```bash
# Pod 리소스 사용량 확인
kubectl top pod -n ollama

# 로그 확인
kubectl logs -n ollama -l app.kubernetes.io/name=ollama --tail=50
```

### 6.2 모델 관리
```bash
# 사용하지 않는 모델 삭제
curl -X DELETE http://localhost:30025/api/delete \
  -d '{"name": "모델명"}'

# 모델 정보 확인
curl http://localhost:30025/api/show \
  -d '{"name": "qwen2.5:0.5b"}' | jq '.'
```

### 6.3 성능 최적화
- **CPU 모드**: GPU가 없는 환경에서는 CPU 모드 사용
- **모델 선택**: 용도에 맞는 적절한 크기의 모델 선택
- **동시 요청 제한**: 리소스에 맞게 동시 요청 수 제한

## 7. 마무리

### 전체 아키텍처
```
┌─────────────────┐
│   사용자 요청    │
└────────┬────────┘
         │ HTTP (30025)
┌────────▼────────┐
│  Kind NodePort  │
└────────┬────────┘
         │
┌────────▼────────┐
│  Ollama Service │
└────────┬────────┘
         │
┌────────▼────────┐
│   Ollama Pod    │
│  ┌───────────┐  │
│  │   Model   │  │
│  │   Cache   │  │
│  └───────────┘  │
└─────────────────┘
         │
┌────────▼────────┐
│       PVC       │
│    (20GB)       │
└─────────────────┘
```

### 정리
Terraform과 Kind를 사용하여 로컬 Kubernetes 환경에 Ollama를 성공적으로 배포했습니다. 이 설정을 통해:
- OpenAI API 비용 없이 LLM 사용 가능
- 다양한 오픈소스 모델 실험 가능
- Kubernetes의 장점을 활용한 안정적인 운영

### 다음 단계
- GPU 지원 추가 (NVIDIA GPU가 있는 경우)
- Prometheus/Grafana를 통한 모니터링
- Ingress 설정으로 외부 접근 허용
- 여러 모델 동시 운영

## 참고 자료
- [Ollama 공식 문서](https://ollama.ai/)
- [Ollama Helm Chart](https://github.com/otwld/ollama-helm)
- [Kind 문서](https://kind.sigs.k8s.io/)
- [Terraform Kubernetes Provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs)

