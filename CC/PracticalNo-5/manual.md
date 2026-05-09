# Procedure / Steps

## Step 1 — Login to Salesforce Developer Edition

- Open the Salesforce login page.
- Enter your username and password.
- Sign in to your Developer Edition account.

## Step 2 — Open Lightning Experience

- After login, ensure Lightning Experience is enabled.
- The Lightning interface dashboard will open.

## Step 3 — Open Setup

- Click the ⚙️ Gear icon at the top-right corner.
- Select **Setup**.

## Step 4 — Create Custom Object

In Setup, open **Object Manager** → Click **Create → Custom Object** and fill the details below.

| Field | Value |
|---|---|
| Label | Comment |
| Plural Label | Comments |
| Record Name | Comment Name |
| Data Type | Text |
| Check | Allow Reports |

Click **Save**.

**Result**

A custom object named **Comment** is created successfully.

## Step 5 — Create Custom Fields

Open the `Comment` object → **Fields & Relationships → New** and create the following fields. Click **Save** after creating each field.

| Field Name | Data Type |
|---|---|
| User_Name | Text |
| Message | Long Text Area |
| Rating | Number |

## Step 6 — Create Custom Tab

Search **Tabs** in the Setup search bar and open **Tabs**. Under **Custom Object Tabs** click **New**.

- Select object: **Comment**
- Choose a tab style/icon
- Click **Next → Next → Save**

## Step 7 — Add Records

Open the **App Launcher**, search for **Comments**, click **New**, and add sample records.

Example:

| User_Name | Message | Rating |
|---|---|---|
| Vedant | Good Service | 5 |
| Rahul | Nice UI | 4 |

## Step 8 — Create Apex Class

Open **Setup → Apex Classes → New** and paste the following Apex code, then click **Save**:

```apex
public class CommentController {
    public String message { get; set; }

    public CommentController() {
        message = 'Welcome to Comment App';
    }
}
```

## Step 9 — Create Visualforce Page

Open **Setup → Visualforce Pages → New**, paste the following, and save the page:

```html
<apex:page controller="CommentController">
    <h1>{!message}</h1>
</apex:page>
```

**Output**

The Visualforce page displays:

Welcome to Comment App

## Conclusion

A simple custom application was successfully created in Salesforce Developer Edition using a Custom Object, Custom Fields, an Apex Class, and a Visualforce Page.