from textwrap import dedent


QNA_EXAMPLE = dedent(
    """\
    ### 요구사항 분석:
    - **온프레미스에서 AWS로 이전**하여 성능을 개선하려는 다중 계층 애플리케이션
    - **RESTful 서비스 기반**으로 계층 간 통신
    - 특정 계층이 과부하되면 **트랜잭션이 손실됨**
    - **문제 해결 및 애플리케이션 현대화** 필요

    ### 각 선택지 분석:
    #### (A) **Amazon API Gateway + AWS Lambda + Amazon SQS**
    - **정답 후보**
    - **AWS Lambda를 애플리케이션 계층으로 사용**하여 서버리스 방식으로 운영, **운영 효율성(Operational Efficiency) 증가**
    - **SQS를 통한 비동기 메시징**을 활용하여 트랜잭션 손실 방지 및 확장성 확보
    - **RESTful API와 잘 맞음**: API Gateway는 RESTful 서비스와 자연스럽게 통합 가능
    - **서버리스 솔루션을 적용하여 관리 부담을 줄일 수 있음**

    #### (B) **EC2 인스턴스 크기 증가**
    - **오답**
    - EC2 인스턴스 크기를 늘리는 것은 **수직 확장(Vertical Scaling)**이며, 과부하 발생 시 확장성이 부족하고, 애플리케이션 현대화라는 요구사항에도 부합하지 않음
    - 부하 증가에 유연하게 대응하지 못할 가능성이 있음

    #### (C) **SNS + EC2 Auto Scaling + CloudWatch**
    - **오답**
    - SNS는 **푸시 기반 메시징 서비스**로, **비동기 큐잉을 통한 트랜잭션 손실 방지** 기능이 부족함
    - 트랜잭션이 손실되는 문제를 해결하려면 **SNS가 아닌 SQS** 같은 메시지 대기열이 더 적합

    #### (D) **SQS + EC2 Auto Scaling + CloudWatch**
    - **부분 정답**이지만 (A)보다 **운영 효율성이 낮음**
    - SQS를 사용하여 계층 간 메시징을 해결하고, **CloudWatch 기반의 Auto Scaling을 통해 확장성 확보** 가능
    - 하지만 EC2 기반의 아키텍처는 **서버 관리 부담이 있으며, AWS로 마이그레이션하면서 서버리스로 현대화하는 전략에 부합하지 않음**

    ### 최종 정답:
    ✅ **(A) Amazon API Gateway + AWS Lambda + Amazon SQS**
    - 서버리스 아키텍처를 활용하여 **운영 효율성 극대화**
    - SQS를 사용한 **비동기 메시징**으로 **트랜잭션 손실 방지**
    - **RESTful 서비스와 자연스럽게 통합** (API Gateway + Lambda)
    - **가장 현대적인 클라우드 네이티브 솔루션**"""
)

NOTE_CONTENT_DESCRIPTION = dedent(
    """\
    - For *each* service or comparison topic listed above, please provide the following information. Structure the output clearly using markdown lists and bold headings for each section:

        1.  **Core Concept:**
            *   Provide a brief (1-2 sentence) explanation of what the service is and its primary purpose.
        2.  **Key Differentiators (Compared to Alternatives):**
            *   List 3-5 critical features or characteristics that distinguish this service from its common alternatives (e.g., SQS vs SNS, Lambda vs EC2, Aurora vs RDS MySQL, Security Groups vs NACLs).
            *   Focus on aspects like processing model, scaling behavior, use case suitability, state management, or access patterns.
        3.  **Common Misconceptions & SAA Pitfalls:**
            *   Highlight 4-5 frequent misunderstandings or common mistakes candidates make regarding this service on the SAA exam.
            *   Examples: Incorrectly choosing a service based on a misunderstanding of its limits, confusing configuration options, misinterpreting security responsibilities, or overlooking cost implications of a specific feature.
        4.  **When to Choose This Service (Decision Criteria):**
            *   Clearly state 1-3 key scenarios or requirements where this service is *distinctly* the correct choice over alternatives.
            *   Focus on the "trigger" conditions that should make a Solutions Architect select this specific service (e.g., "Choose SQS when you need reliable decoupling and message durability for asynchronous tasks," or "Choose Kinesis Data Streams for real-time processing of ordered records").
        5.  **Critical Configuration/Integration Notes:**
            *   Mention 1-3 crucial configuration aspects or integration points that are frequently tested or easily confused (e.g., SQS visibility timeout, Lambda concurrency limits, EBS volume types and performance characteristics, Security Group statefulness).
        
    - Write in Korean, following the format shown in the examples field."""
)

NOTE_EXAMPLE = dedent(
    """\
    ## Amazon Cognito

    ### 핵심 개념

    - Amazon Cognito: 웹 및 모바일 애플리케이션을 위한 사용자 가입, 로그인 및 접근 제어를 제공하는 완전 관리형 서비스입니다. 인증, 인가 및 사용자 디렉토리 관리를 지원합니다.

    ### 주요 차별점

    - **서버리스 사용자 디렉토리 (Serverless User Directory):** AWS 리소스용 IAM이나 맞춤형 ID 솔루션과 달리, Cognito는 (AWS 사용자가 아닌) 앱 사용자를 위한 관리형 사용자 디렉토리를 제공합니다.
    - **연동 자격 증명 (Federated Identity):** 소셜 ID 공급자 (Google, Facebook, Apple), SAML 및 OpenID Connect를 지원하여 싱글 사인온(SSO)을 가능하게 합니다.
    - **앱 인증용 토큰 (Tokens for App Authentication):** 앱에서 안전하고 표준 기반의 인증을 위해 JWT 토큰(ID, 액세스, 리프레시)을 발급합니다.
    - **세분화된 접근 제어 (Fine-Grained Access Control):** IAM 역할과 통합되어 사용자에게 리소스 접근을 위한 임시 AWS 자격 증명을 부여합니다.
    - **사용자 풀 vs 자격 증명 풀 (User Pools vs Identity Pools):** 사용자 풀은 인증과 사용자 프로필을 관리하고, 자격 증명 풀은 AWS 서비스 접근을 위한 AWS 자격 증명을 제공합니다.

    ### 일반적인 오해 및 함정

    - **사용자 풀과 자격 증명 풀 혼동:** 사용자 풀 = 인증 (당신은 누구인가?); 자격 증명 풀 = 인가 (AWS에서 무엇에 접근할 수 있는가?).
    - **IAM vs Cognito:** Cognito를 AWS 사용자 관리를 위한 IAM의 대체제로 착각하는 경우. Cognito는 애플리케이션 최종 사용자를 위한 것이지, AWS 계정 관리를 위한 것이 아닙니다.
    - **연동 범위:** Cognito가 소셜 로그인만 지원한다고 가정하는 경우. SAML 및 기업 ID 공급자도 지원합니다.
    - **토큰 저장:** 클라이언트 애플리케이션에서 토큰 만료 및 갱신 처리를 간과하는 경우.
    - **보안 설정 오류:** 앱 클라이언트 보안 암호를 보호하지 않거나 콜백 URL을 잘못 구성하여 애플리케이션을 무단 접근에 노출시키는 경우.

    ### 결정 기준

    - **앱 사용자 인증:** 모바일 또는 웹 애플리케이션을 위한 사용자 가입/로그인 및 인증 관리가 필요할 때, 특히 연동 자격 증명 옵션이 필요할 때.
    - **앱 사용자를 위한 임시 AWS 접근:** 애플리케이션 사용자가 각 사용자마다 IAM 사용자를 생성하지 않고 AWS 리소스(예: S3, DynamoDB)에 대한 제어된 임시 접근이 필요할 때.

    ### 중요 구성 참고 사항

    - **사용자 풀 (User Pool) vs 자격 증명 풀 (Identity Pool) 선택:** 인증에는 사용자 풀을 사용하고, AWS 자격 증명을 부여하려면 자격 증명 풀을 사용합니다. 종종 두 가지 모두 함께 사용됩니다.
    - **앱 클라이언트 설정:** 보안 취약점을 방지하기 위해 허용된 콜백 URL, 로그아웃 URL 및 OAuth 흐름을 안전하게 구성해야 합니다."""
)
