document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('reviewModal');
    if (!modal) return;
    
    const closeBtn = modal.querySelector('.close');
    
    document.querySelectorAll('.read-more-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const text = this.dataset.text;
            const author = this.dataset.author;
            const date = this.dataset.date;
            const id = this.dataset.id || '';
  
            console.log('Opening modal for:', author, date, id);
            
            showFullReview(text, author, date, id);
        });
    });
    
    function showFullReview(text, author, date, id) {
        document.getElementById('modalText').textContent = text;
        document.getElementById('modalAuthor').textContent = author;
        document.getElementById('modalDate').textContent = date;
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
        
        if (id) {
            history.pushState(null, null, `#review-${id}`);
        }
    }
    

    closeBtn.addEventListener('click', closeModal);
    window.addEventListener('click', closeModalIfOutside);
    document.addEventListener('keydown', closeOnEscape);
    
    function closeModal() {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
        history.replaceState(null, null, ' ');
    }
    
    function closeModalIfOutside(event) {
        if (event.target === modal) closeModal();
    }
    
    function closeOnEscape(event) {
        if (event.key === 'Escape' && modal.style.display === 'block') closeModal();
    }
});