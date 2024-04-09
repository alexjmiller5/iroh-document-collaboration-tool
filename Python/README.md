# Iroh Document Collaboration Tool

The Iroh Document Collaboration Tool is a simple, decentralized application built using the Iroh framework, allowing users to create, join, and collaboratively edit documents in real-time. This Python-based tool leverages the power of Iroh's sublinear scaling and interoperability features for document synchronization and editing in a peer-to-peer manner.

## Features

- **Decentralized Document Creation and Joining**: Users can start new collaborative documents or join existing ones using unique document tickets.
- **Real-time Editing and Synchronization**: Participants can edit documents in real-time, with changes synced across all nodes.
- **Simple CLI Interface**: Easy-to-use command-line interface for document operations such as create, join, edit, and sync.

## Requirements

- Python 3.6 or higher
- Access to the `iroh` Python package and its dependencies

## Installation

Before you start, ensure you have Python installed on your system. Then, follow these steps to set up the Iroh Document Collaboration Tool:

1. **Clone the Repository**:
   git clone https://github.com/alexjmiller5/iroh-test-app.git.
   cd iroh-test-app/Python
1. **Install Dependencies**:
Ensure the iroh package and any other dependencies are properly installed. Installation instructions for the iroh package are located [here](https://github.com/n0-computer/iroh-ffi/blob/main/README.md).

## Usage
The Iroh Document Collaboration Tool operates through a command-line interface. Here's how to use it:

### Start a New Document
To create a new document and start a collaboration session, run the script without any arguments:

```python3 collaboration_tool.py```

Upon creation, the script will output a ticket (document ID) that you can share with others to collaborate on the document.

### Join an Existing Document
To join and collaborate on an existing document, run the script with the document's ticket (ID) as an argument:

bash
Copy code
```python3 collaboration_tool.py <document_ticket>```

### Document Editing Commands
Once inside a document session, the following commands are available:

- **Edit**: Enter `edit` to modify the document. You will be prompted to enter a key (identifier for a piece of content) and its corresponding content.
- **Sync**: Enter `sync` to synchronize changes with other collaborators. This command displays the latest content of the document.
- **View**: Enter `view` to display the current content of the document without editing or syncing. This is useful for quickly checking the document's state.
- **Exit**: Enter `exit` to leave the document session.

## Contributing
Contributions to the Iroh Document Collaboration Tool are welcome! Whether it's bug reports, feature requests, or code contributions, please feel free to make your suggestions known by creating issues or pull requests on the project's repository.

## License
None so far
