import streamlit as st
import streamlit.components.v1 as components

def mic_recorder(key=None):
    """Streamlit microphone recorder using JavaScript + HTML5"""
    html_code = f"""
        <script>
        let recorder, stream;
        const sleep = (time) => new Promise(resolve => setTimeout(resolve, time));
        const b64toBlob = (b64Data, contentType='', sliceSize=512) => {{
            const byteCharacters = atob(b64Data);
            const byteArrays = [];
            for (let offset = 0; offset < byteCharacters.length; offset += sliceSize) {{
                const slice = byteCharacters.slice(offset, offset + sliceSize);
                const byteNumbers = new Array(slice.length);
                for (let i = 0; i < slice.length; i++) {{
                    byteNumbers[i] = slice.charCodeAt(i);
                }}
                const byteArray = new Uint8Array(byteNumbers);
                byteArrays.push(byteArray);
            }}
            return new Blob(byteArrays, {{type: contentType}});
        }};

        async function record() {{
            stream = await navigator.mediaDevices.getUserMedia({{ audio: true }});
            recorder = new MediaRecorder(stream);
            let data = [];
            recorder.ondataavailable = (event) => data.push(event.data);
            recorder.start();

            recorder.onstop = async () => {{
                const blob = new Blob(data, {{ type: 'audio/webm' }});
                const reader = new FileReader();
                reader.readAsDataURL(blob);
                reader.onloadend = () => {{
                    const base64data = reader.result.split(',')[1];
                    window.parent.postMessage({{ isStreamlitMessage: true, type: "streamlit:setComponentValue", value: base64data }}, "*");
                }};
            }};
        }}

        function stop() {{
            recorder.stop();
            stream.getTracks().forEach(track => track.stop());
        }}
        </script>

        <button onclick="record()">Start Recording</button>
        <button onclick="stop()">Stop Recording</button>
    """
    return components.html(html_code, height=100)
