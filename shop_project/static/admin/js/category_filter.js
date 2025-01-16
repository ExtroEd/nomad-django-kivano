document.addEventListener('DOMContentLoaded', function () {
    const categoryField = document.querySelector('#id_category');
    const subcategoryField = document.querySelector('#id_subcategory');
    const subsubcategoryField = document.querySelector('#id_subsubcategory');

    function updateSubcategories() {
        const categoryId = categoryField.value;
        if (!categoryId) {
            subcategoryField.innerHTML = '<option value="">---------</option>';
            subsubcategoryField.innerHTML = '<option value="">---------</option>';
            return;
        }

        fetch(`/admin/get_subcategories/?category_id=${categoryId}`)
            .then(response => response.json())
            .then(data => {
                subcategoryField.innerHTML = '<option value="">---------</option>';
                data.subcategories.forEach(sub => {
                    const option = document.createElement('option');
                    option.value = sub.id;
                    option.textContent = sub.name;
                    subcategoryField.appendChild(option);
                });
                subsubcategoryField.innerHTML = '<option value="">---------</option>';
            });
    }

    function updateSubSubcategories() {
        const subcategoryId = subcategoryField.value;
        if (!subcategoryId) {
            subsubcategoryField.innerHTML = '<option value="">---------</option>';
            return;
        }

        fetch(`/admin/get_subsubcategories/?subcategory_id=${subcategoryId}`)
            .then(response => response.json())
            .then(data => {
                subsubcategoryField.innerHTML = '<option value="">---------</option>';
                data.subsubcategories.forEach(sub => {
                    const option = document.createElement('option');
                    option.value = sub.id;
                    option.textContent = sub.name;
                    subsubcategoryField.appendChild(option);
                });
            });
    }

    categoryField.addEventListener('change', updateSubcategories);
    subcategoryField.addEventListener('change', updateSubSubcategories);
});
