# QRD — [Product Name]

## Overview
- **Product Name:**
- **Author:**
- **Date:**
- **Version:**
- **Status:** Draft / In Review / Approved
- **Related SRD:** [link]
- **Related PRD:** [link]
- **Related Test Plan:** [link]

## 1. Introduction

### Purpose
What this document defines: the quality standards, acceptance criteria, and quality process for [product name].

### Scope
What quality aspects are covered (performance, security, usability, accessibility, reliability) and what is excluded.

### Quality Objectives
- [Objective 1: e.g., "Zero critical bugs at release"]
- [Objective 2: e.g., "P95 response time under 300ms"]
- [Objective 3: e.g., "WCAG 2.2 AA compliance"]

## 2. Quality Attributes

| ID | Attribute | Definition | Target | Measurement Method | Frequency |
|----|-----------|-----------|--------|-------------------|-----------|
| QA-PERF-01 | Response Time | Server response time at P95 | < 300ms | Load test (k6/Locust) | Each release |
| QA-PERF-02 | Throughput | Requests handled per second | > 1,000 rps | Load test | Each release |
| QA-REL-01 | Uptime | System availability | 99.9% monthly | Production monitoring | Monthly |
| QA-REL-02 | Error Rate | Server error rate (5xx) | < 0.1% | Production monitoring | Daily |
| QA-SEC-01 | Vulnerabilities | Known CVEs in dependencies | 0 critical, 0 high | SAST + dependency scan | Each release |
| QA-SEC-02 | Penetration Test | Resistance to OWASP Top 10 | No critical findings | External pen test | Quarterly |
| QA-USE-01 | Task Completion | Users complete primary task | > 90% | Usability test, N=10 | Before launch |
| QA-ACC-01 | Accessibility | WCAG compliance level | 2.2 AA | Automated + manual audit | Each release |
| QA-MNT-01 | Test Coverage | Automated test coverage | > 80% lines | CI pipeline | Each commit |
| QA-MNT-02 | Code Complexity | Cyclomatic complexity | < 15 per function | SonarQube | Each commit |
| QA-CMP-01 | Browser Support | Cross-browser compatibility | Chrome, Firefox, Safari, Edge (last 2) | Cross-browser test | Each release |

## 3. Acceptance Criteria (Release Readiness)

### Blocking Criteria
These must pass before the product can be released to production.

| ID | Criterion | Threshold | Verified By |
|----|-----------|-----------|------------|
| AC-001 | All P0 requirements pass automated tests | 100% pass | CI pipeline |
| AC-002 | No open P0 (critical) or P1 (high) bugs | 0 open | Bug tracker |
| AC-003 | Performance targets met under expected load | All QA-PERF targets pass | Load test report |
| AC-004 | Security scan clean | 0 critical/high CVEs | Security scan report |
| AC-005 | Accessibility audit passes | WCAG 2.2 AA | Audit report |
| AC-006 | Data migration verified (if applicable) | 100% data integrity | Migration test |
| AC-007 | Rollback procedure tested | Successful rollback within [X] minutes | Rollback drill |

### Advisory Criteria
These are tracked but do not block release. Failures require a follow-up plan.

| ID | Criterion | Target | Actual | Follow-up Plan |
|----|-----------|--------|--------|---------------|
| AC-008 | Code coverage | > 80% |        |               |
| AC-009 | Documentation complete | All features documented | |  |
| AC-010 | Localization reviewed | All strings checked |   |   |

## 4. Quality Process

### Definition of Done (per user story / task)
- [ ] Code reviewed and approved by at least [N] reviewers
- [ ] Unit tests written and passing
- [ ] Integration tests written and passing (where applicable)
- [ ] No new linting errors or warnings
- [ ] Documentation updated (if user-facing changes)
- [ ] Accessibility checked (if UI changes)

### Quality Gates

| Gate | When | Criteria | Decision Maker |
|------|------|----------|---------------|
| Sprint Review | End of each sprint | All stories meet Definition of Done | Tech Lead |
| Staging Deployment | Before staging deploy | All blocking AC pass on staging | QA Lead |
| Release Readiness | Before production deploy | All blocking AC pass, advisory reviewed | Product + QA + Tech Lead |

### Defect Severity Classification
| Severity | Definition | Response Time | Resolution Time |
|----------|-----------|---------------|----------------|
| P0 — Critical | System down, data loss, security breach | 1 hour | 4 hours |
| P1 — High | Major feature broken, no workaround | 4 hours | 24 hours |
| P2 — Medium | Feature impaired, workaround exists | 1 business day | 1 sprint |
| P3 — Low | Cosmetic issue, minor inconvenience | Next sprint planning | Best effort |

### Testing Strategy
| Test Type | Scope | Tool | When | Owner |
|-----------|-------|------|------|-------|
| Unit | Individual functions | [framework] | Each commit | Developers |
| Integration | Service interactions | [framework] | Each PR | Developers |
| End-to-End | User flows | Playwright / Cypress | Before release | QA |
| Performance | Load and stress | k6 / Locust | Before release | QA / SRE |
| Security | Vulnerability scan | [tool] | Before release | Security |
| Accessibility | WCAG compliance | axe / Lighthouse + manual | Before release | QA |

## 5. Quality Debt Tracking

| ID | Description | Severity | Identified Date | Plan | Target Date |
|----|------------|----------|----------------|------|------------|
|    |            |          |                |      |            |

## 6. Appendices

### A. Quality Metrics Dashboard
[Link to monitoring dashboard or describe the metrics tracked]

### B. Compliance Checklist
[If applicable: SOC 2, HIPAA, GDPR, PCI-DSS compliance requirements]

### C. Glossary
| Term | Definition |
|------|-----------|
|      |           |

### D. Change Log
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0     |      |        | Initial draft |