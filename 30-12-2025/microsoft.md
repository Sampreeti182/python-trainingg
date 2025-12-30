



## 1. What is Microsoft Entra?
Microsoft Entra is the modern identity and access management solution from Microsoft. It is the **new name for Azure Active Directory (AAD)**, which was previously used for identity services in Azure.

### Key Features of Microsoft Entra
- **Identity Management**: Provides secure access to applications and resources.
- **Access Control**: Ensures only authorized users can access sensitive data.
- **Cloud Integration**: Works seamlessly with Microsoft 365, Azure services, and third-party apps.
- **Zero Trust Security**: Implements strong authentication and conditional access policies.

---

## 2. What is Authentication and Authorization?
These are two fundamental concepts in identity and access management:

- **Authentication**:
  - Verifies **who you are**.
  - Example: Logging in with username and password, or using Multi-Factor Authentication (MFA).
  - Ensures the identity of the user or application.

- **Authorization**:
  - Determines **what you can do** after authentication.
  - Example: A user may log in successfully but only have read access to certain files.
  - Controls permissions and access levels.

**In short**:  
- Authentication = Identity verification.  
- Authorization = Permission assignment.

---

## 3. What are Users and Groups in Microsoft Entra?
- **Users**:
  - Individual identities in the directory.
  - Can be employees, external partners, or service accounts.
  - Each user has attributes like name, email, roles, and permissions.

- **Groups**:
  - Collections of users.
  - Used to simplify permission management.
  - Example: A “Finance” group can have access to financial applications without assigning permissions individually.

### Benefits of Groups
- Easier administration.
- Role-based access control (RBAC).
- Consistent security policies.

---

## 4. How do you register an application in Microsoft Entra?
Application registration allows apps to integrate with Microsoft identity platform for authentication and authorization.

### Steps to Register an Application
1. **Sign in to Microsoft Entra Admin Center**:
   - Go to [ttps://entra.microsoft.com.
2. **Navigate to App Registrations**:
   - Select **App registrations** from the left menu.
3. **Click on “New Registration”**:
   - Provide:
     - **Name** of the application.
     - **Supported account types** (Single tenant or Multi-tenant).
     - **Redirect URI** (for web apps).
4. **Configure Permissions**:
   - Assign API permissions (Microsoft Graph, custom APIs).
5. **Generate Client Secret or Certificates**:
   - Used for secure authentication.
6. **Save and Use Application ID**:
   - Application (client) ID and tenant ID are required for integration.

---

