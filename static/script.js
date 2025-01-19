async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    // Display user message in chat box
    const chatBox = document.getElementById('chat-box');
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'user-message';
    userMessageDiv.textContent = userInput;
    chatBox.appendChild(userMessageDiv);

    // Clear input field
    document.getElementById('user-input').value = '';

    // Send message to server
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        });
        const data = await response.json();
        const chatbotResponse = data.response;

        // Display chatbot response in chat box
        const chatbotMessageDiv = document.createElement('div');
        chatbotMessageDiv.className = 'chatbot-message';
        chatbotMessageDiv.innerHTML = chatbotResponse.replace(/\n/g, '<br>');
        chatBox.appendChild(chatbotMessageDiv);

        // Scroll chat box to the bottom
        chatBox.scrollTop = chatBox.scrollHeight;
    } catch (error) {
        console.error('Error:', error);
    }
}