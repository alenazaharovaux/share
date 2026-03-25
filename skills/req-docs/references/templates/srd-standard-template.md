# SRD — [Software Name]

## Overview
- **Software Name:**
- **Author:**
- **Date:**
- **Version:**
- **Status:** Draft / In Review / Approved
- **Related PRD:** [link]
- **Related FRD:** [link]

## 1. Introduction

### Purpose
What this document specifies and what software it describes.

### Scope
What is covered and what is explicitly excluded.

### Definitions and Acronyms
| Term | Definition |
|------|-----------|
|      |           |

### References
- PRD: [link]
- FRD: [link]
- Architecture doc: [link]
- Design system: [link]

### Document Overview
How this document is organized and how to read it.

## 2. Overall Description

### Product Perspective
How this software fits into the larger system. Is it standalone, part of a suite, or replacing an existing system?

### User Classes and Characteristics
| User Class | Description | Access Level | Technical Skill |
|-----------|-------------|-------------|----------------|
|           |             |             |                |

### Operating Environment
| Parameter | Specification |
|-----------|--------------|
| Browsers |              |
| Devices |               |
| Operating systems |     |
| Cloud provider |        |
| Runtime |               |

### Design and Implementation Constraints
- [Technology constraints]
- [Regulatory constraints]
- [Budget constraints]
- [Timeline constraints]

### Assumptions
- [What you assume to be true]

### Dependencies
| Dependency | Type | Owner | Risk if Unavailable |
|-----------|------|-------|-------------------|
|           | Service / Library / Team |  |  |

## 3. Functional Requirements

Use "shall" for must-have, "should" for optional requirements.

| ID | Requirement | Priority | Source | Acceptance Criteria |
|----|------------|----------|--------|-------------------|
| FR-001 |        | Must / Should | PRD §X |                   |
| FR-002 |        |          |        |                   |

### FR-001: [Requirement Name]
**Description:** [Detailed behavior description]
**Input:** [What triggers this behavior]
**Output:** [What the system produces]
**Business Rules:**
- [Rule 1]
- [Rule 2]
**Error States:**
- [What happens when X fails]
- [What happens when Y is invalid]
**Acceptance Criteria:**
- [Testable condition 1]
- [Testable condition 2]

## 4. Non-Functional Requirements

| ID | Category | Requirement | Target | Measurement |
|----|----------|-------------|--------|-------------|
| NFR-001 | Performance |     |        |             |
| NFR-002 | Security |        |        |             |
| NFR-003 | Availability |    |        |             |
| NFR-004 | Scalability |     |        |             |
| NFR-005 | Reliability |     |        |             |
| NFR-006 | Maintainability |  |        |             |
| NFR-007 | Accessibility |   |        |             |

## 5. External Interface Requirements

### User Interface
- [UI specifications, screen flows, validation rules]
- [Link to wireframes/mockups in appendix]

### Software Interfaces
| System | Protocol | Data Format | Direction | Authentication |
|--------|----------|-------------|-----------|---------------|
|        | REST / gRPC / MQ |    | Inbound / Outbound / Both | |

### Hardware Interfaces
| Device | Protocol | Data Format | Purpose |
|--------|----------|-------------|---------|
|        |          |             |         |

### Communication Interfaces
| Interface | Protocol | Port | Security |
|-----------|----------|------|----------|
|           | HTTPS / WSS / AMQP | |  |

## 6. Data Requirements

### Data Model
[Entity-relationship description or diagram reference]

### Data Dictionary
| Entity | Field | Type | Required | Constraints | Description |
|--------|-------|------|----------|------------|------------|
|        |       |      | Yes / No |            |            |

### Data Retention
| Data Category | Retention Period | Archival Policy | Deletion Policy |
|--------------|-----------------|----------------|----------------|
|              |                 |                |                |

### Data Migration
[If replacing an existing system, describe data migration requirements]

## 7. System Architecture

### Architecture Overview
[High-level architecture diagram reference]

### Component Descriptions
| Component | Responsibility | Technology | Interfaces |
|-----------|---------------|------------|-----------|
|           |               |            |           |

### Deployment Topology
[Deployment diagram reference — environments, regions, scaling]

### Observability
| Aspect | Tool | Configuration |
|--------|------|--------------|
| Logging |     |              |
| Monitoring |  |              |
| Alerting |    |              |
| Tracing |     |              |

### API Contracts
[Reference to OpenAPI specs or inline endpoint definitions]

## 8. Appendices

### A. Glossary
| Term | Definition |
|------|-----------|
|      |           |

### B. Use Case Diagrams
[Links or embedded images]

### C. State Diagrams
[System state transitions]

### D. Open Questions (TBD)
| ID | Question | Owner | Target Date |
|----|----------|-------|-------------|
|    |          |       |             |

### E. Change Log
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0     |      |        | Initial draft |

### F. Sign-off
| Role | Name | Date | Signature |
|------|------|------|-----------|
|      |      |      |           |