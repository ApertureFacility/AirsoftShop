document.addEventListener('DOMContentLoaded', function() {
    // Обработчики для модального окна
    const modal = document.getElementById('reviewModal');
    const closeBtn = document.querySelector('.close');
    
    // Вешаем обработчики на все кнопки "Читать полностью"
    document.querySelectorAll('.read-more-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const text = this.dataset.text;
            const author = this.dataset.author;
            const date = this.dataset.date;
            
            showFullReview(text, author, date);
        });
    });
    
    // Функция показа модального окна
    function showFullReview(text, author, date) {
        document.getElementById('modalText').textContent = text;
        document.getElementById('modalAuthor').textContent = author;
        document.getElementById('modalDate').textContent = date;
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
    
    // Закрытие модального окна
    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    });
    
    // Закрытие при клике вне модального окна
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });
    
    // Закрытие по ESC
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });
});
// Если вы хотите открывать отзывы в модальном окне при переходе по ссылке
document.addEventListener('DOMContentLoaded', function() {
    // Проверяем, есть ли в URL хэш с ID отзыва
    if (window.location.hash && window.location.hash.startsWith('#review-')) {
        const reviewId = window.location.hash.replace('#review-', '');
        // Здесь можно загрузить отзыв через AJAX или показать уже загруженный
    }
});