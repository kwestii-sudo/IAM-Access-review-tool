import streamlit as st

st.set_page_config(
    page_title="IAM Access Review Tool",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 IAM Access Review Tool")
st.write(
    "Review user access for common IAM risks such as disabled accounts with access, "
    "privileged roles, stale accounts, missing approval, and excessive permissions."
)

st.divider()

name = st.text_input("User / Employee Name", placeholder="John Smith")
department = st.text_input("Department", placeholder="Finance")
system_app = st.text_input(
    "System / Application",
    placeholder="Microsoft 365, Azure, Salesforce, Finance System"
)

account_status = st.selectbox("Account Status", ["Active", "Disabled"])

role = st.selectbox(
    "Current Role / Access Level",
    ["Standard User", "Power User", "Administrator", "Global Administrator"]
)

manager_approval = st.selectbox(
    "Manager / Access Owner Approval",
    ["Approved", "Not Approved", "Unknown"]
)

last_login = st.number_input(
    "Days Since Last Login",
    min_value=0,
    max_value=3650,
    value=30,
    step=1
)

has_sensitive_access = st.selectbox(
    "Access to Sensitive Systems/Data?",
    ["No", "Yes"]
)

business_need = st.selectbox(
    "Is the access still required for the user's job?",
    ["Yes", "No", "Unknown"]
)

if st.button("Review Access", use_container_width=True):
    findings = []
    recommendations = []
    score = 0

    # Account status
    if account_status == "Disabled" and role != "Standard User":
        findings.append("Disabled account still retains elevated access.")
        recommendations.append("Remove any remaining access assigned to the disabled account.")
        score += 4
    elif account_status == "Disabled":
        findings.append("Disabled account should be reviewed for remaining access.")
        recommendations.append("Confirm the account has been fully deprovisioned.")
        score += 2

    # Privileged access
    if role == "Global Administrator":
        findings.append("Account has highly privileged Global Administrator access.")
        recommendations.append(
            "Confirm this level of privilege is required and follows least-privilege principles."
        )
        score += 4
    elif role == "Administrator":
        findings.append("Account has privileged Administrator access.")
        recommendations.append(
            "Confirm Administrator access is necessary for the user's job responsibilities."
        )
        score += 3
    elif role == "Power User":
        findings.append("Account has elevated Power User access.")
        recommendations.append("Confirm elevated access is still required.")
        score += 1

    # Approval
    if manager_approval == "Not Approved":
        findings.append("Current access does not have manager or access-owner approval.")
        recommendations.append(
            "Remove or suspend unapproved access until the appropriate owner validates it."
        )
        score += 4
    elif manager_approval == "Unknown":
        findings.append("Approval status for the current access is unknown.")
        recommendations.append(
            "Validate the access with the user's manager or application owner."
        )
        score += 2

    # Stale account
    if last_login >= 90:
        findings.append(f"Account appears stale: no login for {last_login} days.")
        recommendations.append(
            "Verify whether the account is still needed and consider disabling stale access."
        )
        score += 3
    elif last_login >= 60:
        findings.append(f"Account has been inactive for {last_login} days.")
        recommendations.append("Review the account for possible stale or unnecessary access.")
        score += 2
    elif last_login >= 30:
        findings.append(f"Account has not logged in for {last_login} days.")
        score += 1

    # Sensitive access
    if has_sensitive_access == "Yes":
        findings.append("Account has access to sensitive systems or data.")
        recommendations.append(
            "Confirm the user is authorized to access sensitive systems or data."
        )
        score += 2

    # Business need
    if business_need == "No":
        findings.append("Access is no longer required for the user's job.")
        recommendations.append("Remove access that is no longer required.")
        score += 4
    elif business_need == "Unknown":
        findings.append("Business need for this access has not been confirmed.")
        recommendations.append(
            "Validate business need with the user's manager or system owner."
        )
        score += 2

    # Risk rating
    if score >= 10:
        risk = "CRITICAL"
    elif score >= 6:
        risk = "HIGH"
    elif score >= 3:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    st.divider()
    st.subheader("Access Review Result")
    st.metric("Risk Level", risk)

    st.markdown("### Review Details")
    st.write(f"**User:** {name or 'Not provided'}")
    st.write(f"**Department:** {department or 'Not provided'}")
    st.write(f"**System / Application:** {system_app or 'Not provided'}")
    st.write(f"**Account Status:** {account_status}")
    st.write(f"**Role:** {role}")
    st.write(f"**Approval:** {manager_approval}")

    if findings:
        st.markdown("### Findings")
        for finding in findings:
            st.write(f"- {finding}")
    else:
        st.success("No obvious IAM access risks were identified.")

    if not recommendations:
        recommendations.append("Continue normal periodic access reviews.")

    st.markdown("### Recommended Actions")
    for rec in dict.fromkeys(recommendations):
        st.write(f"- {rec}")

    st.markdown("### Review Summary")
    st.write(
        f"{name or 'This user'} is a **{account_status.lower()}** account with "
        f"**{role}** access to **{system_app or 'the reviewed system'}**. "
        f"The access review identified an overall **{risk}** IAM risk level."
    )

st.divider()
st.caption(
    "Educational portfolio project. This tool uses simplified rule-based logic "
    "and does not replace a formal enterprise IAM or access certification process."
)
