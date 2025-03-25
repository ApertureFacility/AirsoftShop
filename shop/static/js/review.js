document.addEventListener('DOMContentLoaded', function() {
    // Обработчики для модального окна
    const modal = document.getElementById('reviewModal');
    if (!modal) return;
    
    const closeBtn = modal.querySelector('.close');
    
    // Вешаем обработчики на все кнопки "Читать полностью"
    document.querySelectorAll('.button--secondary').forEach(btn => {
        btn.addEventListener('click', function() {
            const text = this.dataset.text;
            const author = this.closest('.review-card').querySelector('.review-author').textContent;
            const date = this.closest('.review-card').querySelector('.review-date').textContent;
            const id = this.dataset.id || ''; // id может отсутствовать
            
            showFullReview(text, author, date, id);
        });
    });
    
    // Функция показа модального окна
    function showFullReview(text, author, date, id) {
        document.getElementById('modalText').textContent = text;
        document.getElementById('modalAuthor').textContent = author;
        document.getElementById('modalDate').textContent = date;
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
        
        // Добавляем ID отзыва в URL, если он есть
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
        const btn = document.querySelector(`.button--secondary[data-id="${reviewId}"]`);
        if (btn) {
            const text = btn.dataset.text;
            const author = btn.closest('.review-card').querySelector('.review-author').textContent;
            const date = btn.closest('.review-card').querySelector('.review-date').textContent;
            showFullReview(text, author, date, reviewId);
        }
    }
});
document.querySelectorAll('.button--secondary').forEach(btn => {
    btn.addEventListener('click', function() {
        const text = this.dataset.text;
        const reviewElement = this.closest('.review'); // Исправленный селектор
        const author = reviewElement.querySelector('.review__author').textContent;
        const date = reviewElement.querySelector('.review__date').textContent;
        const id = this.dataset.id || '';

        showFullReview(text, author, date, id);
    });
});
