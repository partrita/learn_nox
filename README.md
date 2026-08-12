# learn_nox

> nox는 tox와 유사하게 여러 Python 환경에서 테스트를 자동화하는 명령줄 도구입니다. tox와 달리 Nox는 설정을 위해 표준 Python 파일(noxfile.py)을 사용합니다.

## 설치

```bash
pip install nox
```

## 사용법

noxfile.py에 세션을 정의한 후, 다음 명령어로 실행합니다.

```bash
# 모든 세션 실행
nox

# 특정 세션만 실행 (예: tests)
nox -s tests

# 특정 Python 버전으로 실행
nox -p 3.11
```

## 프로젝트 구성

이 프로젝트는 `pyproject.toml`로 의존성을 관리하고,
`noxfile.py`로 테스트/린트 세션을 정의합니다.

- **lint**: Ruff로 소스 코드 린트 및 포맷 체크
- **tests**: pytest로 테스트 실행

## 요구사항

- Python >= 3.11
- 의존성: `uv sync` 또는 `pip install .`로 설치

## 참고

- [Nox 공식 문서](https://nox.thea.codes/)

