# IAM Access Review Tool

A small cybersecurity portfolio project that reviews user access for common Identity and Access Management (IAM) risks.

The tool helps identify issues such as disabled accounts that still have access, privileged accounts, stale users, missing approval, unnecessary access, and access to sensitive systems.

## Features

- Reviews account status
- Reviews the system or application being accessed
- Identifies privileged or elevated roles
- Checks manager or access-owner approval
- Detects inactive or stale accounts
- Flags unnecessary access
- Reviews access to sensitive systems or data
- Assigns an overall risk level
- Provides recommended remediation actions

## Example

### Example Input

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

### Example Output

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
- Confirm Administrator access is necessary for the user's job responsibilities.
- Remove or suspend unapproved access until the appropriate owner validates it.
- Verify whether the account is still needed and consider disabling stale access.
- Confirm the user is authorized to access sensitive systems or data.
- Remove access that is no longer required.
```

## How It Works

The application uses simple rule-based logic to evaluate several IAM risk indicators.

Higher-risk conditions add more weight to the final score. The score is then converted into one of four risk levels:

- LOW
- MEDIUM
- HIGH
- CRITICAL

## Technologies Used

- Python
- Streamlit

## Run Locally

Install the required package:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

## How to Test It

Use this high-risk sample record:

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

Click **Review Access**.

You should receive a **CRITICAL** risk result with multiple IAM findings and recommended remediation actions.

You can also test a low-risk account:

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

This should produce a **LOW** risk result.

## Cybersecurity Skills Demonstrated

This project demonstrates practical understanding of:

- Identity and Access Management (IAM)
- Least privilege
- Privileged access review
- User access reviews
- Access certification / recertification
- Manager and access-owner approval
- Stale account identification
- Deprovisioning
- Security risk assessment
- Remediation recommendations

## Disclaimer

This project is for educational and portfolio purposes. It uses simplified rule-based logic and is not a replacement for enterprise IAM, IGA, PAM, or access governance platforms.
