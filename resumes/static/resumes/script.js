document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("resume-form");

    form.addEventListener("input", function() {
        const preview = document.getElementById("resume-preview");
        preview.innerHTML = `
            <h3>${form.full_name.value}</h3>
            <p>Email: ${form.email.value}</p>
            <p>Phone: ${form.phone.value}</p>
            <p><strong>Summary:</strong> ${form.summary.value}</p>
            <p><strong>Skills:</strong> ${form.skills.value}</p>
            <p><strong>Experience:</strong> ${form.experience.value}</p>
            <p><strong>Education:</strong> ${form.education.value}</p>
        `;
    });
});
