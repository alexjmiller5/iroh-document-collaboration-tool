import sys
from iroh import IrohNode, Query
import iroh

# Initialize an IrohNode. This represents your node in the network.
node = IrohNode("./iroh_data_dir")

def view_document(doc):
    entries = doc.get_many(Query.all(None))
    if entries:
        print("Current document content:")
        for entry in entries:
            key = entry.key().decode('utf-8')
            content = entry.content_bytes(doc).decode('utf-8')
            print(f"{key}: {content}")
    else:
        print("The document is currently empty.")

def create_document():
    # Create a new document
    doc = node.doc_create()
    print(f"Document created with ID: {doc.id().to_string()}")
    # Share the document to get a ticket that others can use to join
    ticket = doc.share(iroh.ShareMode.WRITE)
    print(f"Share this ticket to collaborate: {ticket.to_string()}")

def join_document(ticket_string):
    try:
        doc_ticket = iroh.DocTicket.from_string(ticket_string)
        doc = node.doc_join(doc_ticket)
        print(f"Joined document: {doc.id().to_string()}")
        return doc
    except Exception as e:
        print(f"Failed to join document: {str(e)}")

def edit_document(doc):
    key = input("Enter the key: ").encode('utf-8')
    content = input("Enter the content: ").encode('utf-8')
    author = node.author_create()  # Create or reuse an author ID
    doc.set_bytes(author, key, content)
    print("Content saved.")

def sync_document(doc):
    entries = doc.get_many(Query.all(None))
    for entry in entries:
        key = entry.key().decode('utf-8')
        # Correctly read the content from the entry
        content = entry.content_bytes(doc).decode('utf-8')
        print(f"{key}: {content}")

def main():
    if len(sys.argv) == 1:
        create_document()
    elif len(sys.argv) == 2:
        doc = join_document(sys.argv[1])
        while True:
            command = input("Enter command (edit, sync, view, exit): ")
            if command == "edit":
                edit_document(doc)
            elif command == "sync":
                sync_document(doc)
            elif command == "view":
                view_document(doc)
            elif command == "exit":
                break
            else:
                print("Unknown command.")

if __name__ == "__main__":
    main()
