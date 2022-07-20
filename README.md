# Bump Helm Depdendencies

Bump Helm Depdendencies using YAML configuration

## Assumptions

- The dependencies exist under Chart.yaml

## Full Example usage

```yaml
- name: Bump Helm Depdendencies
  uses: explorium-ai/bump-helm-dependencies-action@main
  with:
    charts: >-
      path/to/my/chart:
        dependencies:
          - name: redis
            version: 1.0.4
      path/to/my/second/chart:
        dependencies:
          - name: test
            version: 2.3.4
          - name: test2
            version: 3.4.5
```
