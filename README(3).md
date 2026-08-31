# IAM Access Review Tool

A Streamlit-based cybersecurity portfolio project that reviews user access and identifies common Identity and Access Management (IAM) risks such as stale accounts, excessive privileges, missing approvals, and unnecessary access.

## Live Demo

https://iam-access-review-tool.streamlit.app/

---

## What It Does

The tool reviews a user account using common IAM access-review factors:

- User / employee name
- Department
- System or application
- Account status
- Current role / access level
- Manager or access-owner approval
- Days since last login
- Access to sensitive systems or data
- Whether the access is still required

It then produces:

- An overall **LOW, MEDIUM, HIGH, or CRITICAL** risk rating
- IAM findings
- Recommended remediation actions
- A short access-review summary

---

## What I Built

I built a lightweight IAM access-review application that simulates part of a real access certification and recertification workflow.

The application checks for several common IAM risks, including:

- Disabled accounts that still retain access
- Administrator or highly privileged accounts
- Missing manager or access-owner approval
- Stale or inactive accounts
- Access to sensitive systems or data
- Access that is no longer required for the user's job

The goal was to create a small project that demonstrates how security teams review identity access and apply least-privilege principles.

---

## Why It Was Technically Challenging

The main challenge was creating risk logic that considers multiple IAM conditions at the same time instead of treating every issue equally.

For example, an active standard user who logged in recently should not receive the same risk rating as a disabled administrator account that has not been used in 120 days and no longer has a business need.

I created weighted rules so higher-risk IAM conditions contribute more heavily to the final risk score.

---

## What I Learned / Fixed

While building the project, I improved the access-review logic by adding fields that make the review more realistic:

- **System / Application**
- **Manager / Access Owner Approval**
- **Business Need**
- **Sensitive Access**

These additions make the project closer to a real IAM access review because access should be evaluated based on both the permissions assigned and whether those permissions are still approved and required.

I also learned how IAM teams use concepts such as:

- Least privilege
- Privileged access review
- Access certification
- Access recertification
- Deprovisioning
- Stale-account review
- Manager / application-owner approval

---

## How the Risk Decision Works

The application uses deterministic rule-based scoring.

Higher-risk conditions add more points to the review.

Example:

```text
Disabled account                    + risk
Administrator access               + risk
No manager approval                + risk
120 days since last login          + risk
Sensitive access                   + risk
No current business need           + risk
```

The total score is converted into one of four ratings:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

A disabled account with privileged access, no approval, a long period of inactivity, and no valid business need will be rated much higher than an active standard user with approved access.

---

## Example Test Access Review

Use this example to test the application:

```text
User / Employee Name: John Smith
Department: Finance
System / Application: Microsoft 365
Account Status: Disabled
Current Role / Access Level: Administrator
Manager / Access Owner Approval: Not Approved
Days Since Last Login: 120
Access to Sensitive Systems/Data?: Yes
Is the access still required for the user's job?: No
```

Expected result:

```text
Risk Level: CRITICAL

Findings:
- Disabled account still retains elevated access.
- Account has privileged Administrator access.
- Current access does not have manager or access-owner approval.
- Account appears stale: no login for 120 days.
- Account has access to sensitive systems or data.
- Access is no longer required for the user's job.

Recommended Actions:
- Remove any remaining access assigned to the disabled account.
- Confirm Administrator access is necessary.
- Remove or suspend unapproved access.
- Review the stale account.
- Validate access to sensitive systems.
- Remove access that is no longer required.
```

---

## Low-Risk Test

You can also test a normal account:

```text
User / Employee Name: Sarah Lee
Department: Marketing
System / Application: Salesforce
Account Status: Active
Current Role / Access Level: Standard User
Manager / Access Owner Approval: Approved
Days Since Last Login: 5
Access to Sensitive Systems/Data?: No
Is the access still required for the user's job?: Yes
```

Expected result:

```text
Risk Level: LOW
```

---

## Why This Counts as an IAM Portfolio Project

This project demonstrates practical understanding of how security and IAM teams evaluate user access.

It shows familiarity with:

- Identity and Access Management (IAM)
- Least privilege
- Privileged access management concepts
- Access reviews
- Access certification / recertification
- Account deprovisioning
- Stale-account identification
- Security risk prioritization
- Remediation recommendations

The project does not simply display user information. It makes a security decision based on several identity and access risk factors.

---

## Tech Stack

- Python
- Streamlit
- Rule-based IAM risk logic

---

## Run Locally

Install the requirements:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

---

## Limitations

This is an educational cybersecurity portfolio project.

The current version:

- Uses simulated/manual user-access data
- Does not connect directly to Active Directory, Microsoft Entra ID, Okta, or other IAM platforms
- Does not automatically remove or modify user access
- Uses deterministic rule-based scoring rather than an enterprise risk engine
- Does not replace a formal IAM, IGA, PAM, or access-governance platform

In a production environment, findings should be validated against authoritative identity, HR, application-owner, and access-governance data.
