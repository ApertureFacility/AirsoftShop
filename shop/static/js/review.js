document.addEventListener('DOMContentLoaded', function() {
    // Обработчики для модального окна
    const modal = document.getElementById('reviewModal');
    if (!modal) return;
    
    const closeBtn = modal.querySelector('.close');
    
    // Вешаем обработчики на все кнопки "Читать полностью"
    document.querySelectorAll('.read-more-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const text = this.dataset.text;
            const author = this.dataset.author;
            const date = this.dataset.date;
            const id = this.dataset.id;
            
            showFullReview(text, author, date, id);
        });
    });
    
    // Функция показа модального окна (теперь принимает id как параметр)
    function showFullReview(text, author, date, id) {
        document.getElementById('modalText').textContent = text;
        document.getElementById('modalAuthor').textContent = author;
        document.getElementById('modalDate').textContent = date;
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
        
        // Добавляем ID отзыва в URL
        if (id) {
            history.pushState(null, null, `#review-${id}`);
        }
    }
    
    // Закрытие модального окна
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
        history.replaceState(null, null, ' ');
    });
    
    // Закрытие при клике вне модального окна
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
            history.replaceState(null, null, ' ');
        }
    });
    
    // Закрытие по ESC
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
            history.replaceState(null, null, ' ');
        }
    });
    
    // Обработка открытия модалки по хэшу в URL
    if (window.location.hash && window.location.hash.startsWith('#review-')) {
        const reviewId = window.location.hash.replace('#review-', '');
        const btn = document.querySelector(`.read-more-btn[data-id="${reviewId}"]`);
        if (btn) {
            const text = btn.dataset.text;
            const author = btn.dataset.author;
            const date = btn.dataset.date;
            showFullReview(text, author, date, reviewId);
        }
    }
});