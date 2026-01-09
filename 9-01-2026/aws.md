## **Brief about AWS and how it is different from Azure**



Amazon Web Services (AWS) is a broad, mature public cloud platform launched in 2006 that offers hundreds of services across compute, storage, networking, databases, analytics, AI/ML, security, and developer tools. It’s known for breadth of services, fine‑grained controls, global scale, and multiple pricing models (On‑Demand, Reserved, Spot, Savings Plans). 



Microsoft Azure (launched in 2010) provides comparable capabilities but is optimized for organizations already invested in Microsoft technologies—tight integration with Windows Server, SQL Server, Active Directory/Entra ID, Office/M365, and strong hybrid tooling (Azure Arc). 



#### Key differences :



* **Ecosystem alignment:** AWS emphasizes open APIs and a vast third‑party ecosystem; Azure emphasizes seamless integration with Microsoft products and hybrid management. 



* **Networking constructs:** AWS uses VPC with explicit public/private subnet design and manual configuration (IGW, NAT, route tables); Azure uses VNet with slightly different segmentation/managed services emphasis.

&nbsp;

* **Containers:** AWS offers ECS (proprietary orchestrator) and EKS (managed Kubernetes); Azure provides AKS for managed Kubernetes and Container Instances for serverless containers. 



* **Market position:** AWS remains the largest provider by IaaS/PaaS share; Azure is a strong second and often preferred in Microsoft‑centric enterprises. 



* **Takeaway:** Choose based on your workload, team skills, and ecosystem commitments—AWS for granular control and service breadth; Azure for Microsoft integration and hybrid scenarios.





## What is IaaS, PaaS, and SaaS on AWS?



### **Infrastructure as a Service (IaaS)**



##### Definition:

Fundamental building blocks—compute (VMs/bare metal), networking, storage—giving the highest flexibility and management control. 



##### Common AWS examples:



* Amazon EC2 (virtual servers/instances)
* Amazon VPC (isolated networking)
* Amazon EBS (block storage), Amazon S3 (object storage for many IaaS scenarios)
* Elastic Load Balancing (traffic distribution)
* IAM for access control



#### **Platform as a Service (PaaS)**



##### Definition:

Managed platforms that abstract infrastructure so you focus on app deployment and lifecycle (no OS/patching).

&nbsp;

#### Common AWS examples:



* AWS Elastic Beanstalk (managed PaaS for web apps/APIs)
* Amazon RDS (managed relational databases)
* AWS Lambda (serverless functions—often grouped under FaaS but considered PaaS by many comparisons)
* Amazon ECS with Fargate (serverless container execution)

&nbsp;



#### **Software as a Service (SaaS)**



##### Definition:



Fully managed applications operated by the vendor; customers consume the app without managing infrastructure.



##### Examples in/around AWS:



Third‑party SaaS delivered via AWS Marketplace; some first‑party services are “SaaS‑like” experiences (e.g., Amazon QuickSight BI, Amazon WorkMail), though AWS primarily positions itself as an IaaS/PaaS provider.





#### **Map the Services of Azure to AWS (core examples)**







VM → EC2 (Azure VM ↔ AWS EC2): Virtual machine compute in IaaS. 



Container → ECS: AWS’s native container orchestration; often simpler than Kubernetes for small/medium services and integrates with Fargate. 



AKS → EKS: Managed Kubernetes equivalents. Migration patterns and service‑by‑service mappings are documented by Microsoft. \[learn.microsoft.com], 



Blob → S3 Bucket: Object storage equivalents (Azure Blob “containers” vs AWS S3 “buckets”). Comparative guidance available from Microsoft’s Architecture Center







































