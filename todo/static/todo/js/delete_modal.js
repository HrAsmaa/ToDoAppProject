window.onload = function() {
    const deleteModel = document.getElementById('deleteModel')
    if (deleteModel) {
      deleteModel.addEventListener('show.bs.modal', event => {
        // Button that triggered the modal
        const button = event.relatedTarget
        // Extract info from data-bs-* attributes
        const recipient = button.getAttribute('data-bs-whatever').split(" ")
        const title = recipient.slice(1, -1).toString()
        const id = recipient[0]
        // If necessary, you could initiate an Ajax request here
        // and then do the updating in a callback.

        // Update the modal's content.
        const modalTitle = deleteModel.querySelector('.modal-title')
        modalTitle.textContent = `Are you sure you want to delete ${title} ?`
      })
    }
}