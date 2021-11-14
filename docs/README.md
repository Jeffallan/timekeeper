# User Stories

Generally, There are two types of users Admins (General Contractor) and users (Subcontractor).

## 1) As a General Contractor I need to invite users to the application and manage their status so I can have an accurate accounting of all users and their permissions.

    **Acceptance Criteria**

    - [x] Invite users.
    - [] Update a user's role (General Contractor or Subcontractor).
    - [] Update a user's email.
    - [] Activate and deactivate users.
    - [] Passes unit tests.

    **Misuse**

    As a malicious user I would attempt to change my role in the application to escalate my privileges.

    **Mitigation Criteria**

    A malicious user's activities can be mitigated by:
    - [x] Implementing object level permissions on the relevant API endpoints.
    - [x] Implementing separate API endpoints for changing a user's role that are only accessible by a General Contractor.

## 2) As any type of user I need the ability to contact other users via telephone or email. As a General Contractor I also need access to a Subcontractor's mailing address. This facilitates ease of communication within the organization.

    **Acceptance Criteria**

    - [x] Create a user profile upon new user creation.
    - [x] Implement a list view of the users and their contact information.
    - [x] Implement a detail view where a user can update their contact information.
    - [] Passes unit tests.

    **Misuse**

    As a malicious user I would like to achieve two things. First, edit another user's profile information. Second, access another user's mailing address.

    **Mitigation Criteria**

    A malicous user's activities can be mitigated by:
    - [x] Implementing object level permissions on the relevant API endpoints
    - [x] Providing alternate serializer classes to restrict sensitive information.

## 3) As a Subcontractor I need the ability to update my username (email) and reset my password to facilitate my continued use of this application.

    **Acceptance Criteria**
    - [x] A user can change their password.
    - [] A user can change their email.
    - [] Passes unit tests.

    **Misuse**
    As a malicious user my goal is to change a user's password directly or change a user's email to one that I control to take over another user's account.

    **Mitigation Criteria**
    - [x] Use a third party authentication framework with no known security issues.
    - [x] Use a third party authentication framework that restricts these activities to the correct users by default.
    - [] Restrict CORS requests to only trusted domains.
    - [x] Add CSRF token to all requests.

## 4) As a General Contractor I need to create clients, and their associated locations, to facilitate accurate client billing.

    **Acceptance Criteria**
    - [] Client creation and update API endpoints.
    - [] Client creation and update GUI.
    - [] Passes unit tests.

    **Misuse**
    As a malicious user I would try to access information about a client or location which I am not authorized to view.

    **Mitigation Criteria**
    - [] Restrict client endpoints to only General Contractors.
    - [] Use object level permissions and custom querysets to restrict information about locations.


## 5) As a Genral Contractor I need to create services which I can bill to a client's location to facilitate accurate client billing.

    **Acceptance Criteria**
    - [] Location creation and update API endpoints associated to a client.
    - [] Location creation and update GUI associated to a client.
    - [] Service creation and update API endpoints associated to a client.
    - [] Service creation and update GUI associated to a client.
    - [] Passes unit tests.

**Misuse**

**Mitigation Criteria**

## 6) As a General Contractor I need to approve a Subcontractor to provide services and work at locations to ensure positive client relations.

**Acceptance Criteria**
- [] Subcontractor location approval API endpoints.
- [] Subcontractor location approval GUI.
- [] Subcontractor service approval API endpoints.
- [] Subcontractor service approval GUI.
- [] Passes unit tests.

**Misuse**
As a malicious user I could try giving myself permission to bill at locations I am not authorized or bill for services which I am not authorized to perpetrate fraud.

**Mitigation Criteria**
- [] Restrict location approval endpoints to General Contractors only.
- [] Restrict service approval endpoints to General Contractors only.

## 7) As any User I need to track a service that I provide to an approved location to facilitate accurate client billing.

**Acceptance Criteria**
- [] Work creation and update API endpoint associated to a location and service.
- [] work creation and update GUI associated to a location and service.
- [] Passes unit tests.

**Misuse**
As a malicious user I would try to accomplish three things. First, editing a service which has been already been rendered. Second, accessing services rendered by another Subcontractor. Finally, arbitrarily billing for services which were never rendered.

**Mitigation Criteria**
- [] Implement object level permission restricting a user from editing a service they rendered after a certain time.
- [] Restricting a Subcontractor's view of the data to only services they themselves have rendered.
- [] Concerning arbitrary billing. This would require some sort of audit / integration with a third party scheduling application which is outside the scope of the initial minimum viable product.