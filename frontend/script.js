const uploadBtn = document.getElementById("uploadBtn");
const resumeInput = document.getElementById("resume");
const result = document.getElementById("result");

uploadBtn.addEventListener("click", async () => {

    const file = resumeInput.files[0];

    if (!file) {
        alert("Please select a resume first!");
        return;
    }

    result.innerHTML = "<h3>Analyzing Resume...</h3>";

    const formData = new FormData();
    formData.append("file", file);

    try {

        const response = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        result.innerHTML = `
            <h2>Resume Analysis</h2>

            <p><strong>Prediction:</strong> ${data.prediction}</p>

            <p><strong>ATS Score:</strong> ${data.ats.ats_score}%</p>

            <p><strong>Truth Score:</strong> ${JSON.stringify(data.truth)}</p>

            <p><strong>Skills:</strong></p>

            <ul>
                ${data.skills.map(skill => `<li>${skill}</li>`).join("")}
            </ul>

            <p><strong>AI Feedback:</strong></p>

            <pre style="white-space: pre-wrap; font-family: Arial, sans-serif;">
            ${data.ai_feedback}
            </pre>
        `;

    } catch (error) {

        console.error(error);
        result.innerHTML = `<h3 style="color:red">${error.message}</h3>`;

    }

});