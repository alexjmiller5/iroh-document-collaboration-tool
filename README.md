# Iroh Document Collaboration Tool

The Iroh Document Collaboration Tool is a versatile application capable of both local and remote document collaboration. It allows users to create, join, and collaboratively edit documents in real-time. This Python-based tool can operate in a decentralized local environment using the Iroh framework or connect to a remote Iroh network via HTTP API for enhanced collaboration features.

## Features

- **Dual Collaboration Modes**: Choose between local decentralized document management and remote collaborative sessions through the Iroh network.
- **Real-time Editing and Synchronization**: Engage in real-time document editing with changes synchronized either across a local network or through the Iroh remote server.
- **Comprehensive CLI Interface**: Manage documents through a robust command-line interface with commands tailored for both local and remote document operations.

## Requirements

- Python 3.6 or higher
- Access to the `iroh` Python package and its dependencies for local operations
- Internet connection and credentials for operations via the HTTP API

## Installation

Ensure Python is installed on your system. Follow these steps to set up the Iroh Document Collaboration Tool:

1. Clone the Repository:

```git clone https://github.com/alexjmiller5/iroh-test-app.git```

```cd iroh-test-app/Python```

2. Install Dependencies:
Ensure the `iroh` package and any other dependencies are properly installed. Installation instructions for the `iroh` package are located [here](https://github.com/n0-computer/iroh-ffi/blob/main/README.md).

## Usage

The Iroh Document Collaboration Tool operates through a command-line interface. Here are the basic usage instructions:

### Local Mode
1. Start a New Document:

```python3 collaboration-tool-local.py```

This command creates a new local document and outputs a ticket (document ID) that you can share with others to collaborate on the document locally.

2. Join an Existing Document:

```python3 collaboration-tool-local.py <document_ticket>```

### Remote Mode
1. Start or Join a Remote Document:

```python3 collaboration-tool-http-api.py```

This script manages both document creation and joining on the remote server. You can share and collaborate on documents using the remote Iroh network.

### Common Document Editing Commands
Once inside a document session, either locally or remotely, you can use commands like `edit`, `view`, `sync`, and `exit` to manage document interactions.

## Contributing
Contributions to the Iroh Document Collaboration Tool are welcome! Whether it's bug reports, feature requests, or code contributions, please feel free to make your suggestions known by creating issues or pull requests on the project's repository.

## License
None so far