# Features of the Client Registration App

This document describes the features of the Client Registration App developed using Python's `tkinter` library, with a Material Design-inspired theme.

## Core Features

### 1. **Client Management**
#### **Register Clients**
- Allows users to register new clients by providing the following details:
  - Name
  - Last Name
  - Email
  - Phone Number
- Input validation ensures that all fields are filled before submission.

#### **View Clients**
- Displays all registered clients in a table format using a `Treeview` widget.
- Columns include:
  - ID
  - Name
  - Last Name
  - Email
  - Phone Number

#### **Edit Clients**
- Users can edit the details of an existing client.
- Opens a modal dialog pre-filled with the selected client's information.

#### **Delete Clients**
- Allows users to delete a selected client from the database.

### 2. **Database Integration**
- Uses SQLite as the database backend.
- Automatically creates a `clients` table if it doesn't exist.
- Stores the following fields for each client:
  - ID (Primary Key)
  - Name
  - Last Name
  - Email
  - Phone Number

### 3. **Responsive Design**
- The app uses a responsive grid layout to ensure proper resizing of widgets.
- The `Treeview` widget is scrollable.

### 4. **Fullscreen Mode**
- Users can toggle fullscreen mode using the `F11` key.
- Exit fullscreen mode using the `Escape` key.

### 5. **Material Design Theme**
- Incorporates the `ttkthemes` library to apply a Material Design-inspired theme (\"Arc\").
- Provides a modern and clean user interface.

## Advanced Features

### 6. **Floating Action Button (FAB)**
- Contains quick access buttons for the following actions:
  - Register a new client
  - View all clients
  - Edit the selected client
  - Delete the selected client

### 7. **Modal Dialogs**
- Groups input fields (Name, Last Name, Email, Phone Number) into a modal dialog.
- Modal dialogs are used for:
  - Registering new clients
  - Editing existing clients

### 8. **Dynamic Updates**
- The client list updates dynamically after:
  - Registering a new client
  - Editing a client
  - Deleting a client

### 9. **Data Persistence**
- All client data is stored in a persistent SQLite database (`clients.db`).
- Ensures data is retained between app sessions.

## How to Use the App

1. **Start the Application**:
   - Launch the app, and it will load all existing clients from the database.

2. **Register a New Client**:
   - Click the "Register" button in the floating action button menu.
   - Fill in the required details in the modal dialog and click "Submit".

3. **View Clients**:
   - Clients are displayed in the table format immediately upon startup.
   - Click "View Clients" to refresh the list manually.

4. **Edit a Client**:
   - Select a client from the list and click "Edit Selected".
   - Update the details in the modal dialog and click "Submit".

5. **Delete a Client**:
   - Select a client from the list and click "Delete Selected".
   - Confirm the deletion in the dialog box.

6. **Toggle Fullscreen**:
   - Press `F11` to toggle fullscreen mode.
   - Press `Escape` to exit fullscreen mode.

## Usage from terminal
1. Ensure you have Python 3 installed on your system.
2. Install the required dependencies:
```console
pip install ttkthemes
```
3. Run the application
```console
python client_app.py
```

## Future Enhancements
- Integration with cloud storage for data backup.
- Advanced search and filter options for client records.
- Multi-user support with authentication.

