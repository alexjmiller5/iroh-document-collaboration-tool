import iroh
import os
import sys
import tempfile

IROH_DATA_DIR = "./iroh-data"

# Ensure the IROH_DATA_DIR exists
if not os.path.exists(IROH_DATA_DIR):
    os.makedirs(IROH_DATA_DIR)

# Initialize Iroh Node
node = iroh.IrohNode(IROH_DATA_DIR)
print(f"Started Iroh node with ID: {node.node_id()}")

class ImportCallback(iroh.DocImportFileCallback):
    def progress(self, progress):
        # Handle different types of progress updates
        if progress.type() == iroh.DocImportProgressType.FOUND:
            print("Found file for import.")
        elif progress.type() == iroh.DocImportProgressType.PROGRESS:
            print("Importing file...")
        elif progress.type() == iroh.DocImportProgressType.INGEST_DONE:
            print("File import completed.")
        elif progress.type() == iroh.DocImportProgressType.ABORT:
            print("File import aborted due to an error.")
        elif progress.type() == iroh.DocImportProgressType.ALL_DONE:
            print("All done with the file import.")


def main():
    # Check command-line arguments for joining or creating a document
    if len(sys.argv) > 1:
        doc_ticket_str = sys.argv[1]
        doc_ticket = iroh.DocTicket.from_string(doc_ticket_str)
        doc = node.doc_join(doc_ticket)
        print(f"Joined existing document: {doc.id()}")
    else:
        doc = node.doc_create()
        print(f"Created new document: {doc.id()}")

    # Create an author
    author = node.author_create()
    print(f"Author ID: {author.to_string()}")

    callback = ImportCallback()

    while True:
        action = input("Enter 'import' to add a file, 'export' to save a file, 'share' to get a shareable ticket, or 'exit': ")
        if action == 'import':
            file_path = input("Enter the absolute file path to import: ")
            file_dir = os.path.dirname(file_path)
            file_name = os.path.basename(file_path)
            # Use the correct arguments for path_to_key
            doc_key = iroh.path_to_key(file_name, prefix="", root=file_dir)
            # Adjusted import_file call with the callback
            doc.import_file(author, doc_key, file_path, iroh.WrapOption.no_wrap(), callback)
            print(f"File imported: {file_path}")
        elif action == 'export':
            # Export a file from the document
            doc_key = input("Enter the document key for the file to export: ")
            export_path = tempfile.mkdtemp()
            full_export_path = os.path.join(export_path, doc_key)
            entry = doc.get_exact(author, doc_key)
            if entry:
                doc.export_file(entry, full_export_path)
                print(f"File exported to: {full_export_path}")
            else:
                print("File not found in the document.")
        elif action == 'share':
            # Generate a shareable ticket
            doc_ticket = doc.share([iroh.ShareMode.WRITE])
            print(f"Shareable ticket: {doc_ticket.to_string()}")
        elif action == 'exit':
            break

if __name__ == "__main__":
    main()