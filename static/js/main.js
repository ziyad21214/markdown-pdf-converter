        function showFileInfo() {
            const fileInput = document.getElementById('fileInput');
            const fileInfo = document.getElementById('fileInfo');
            const fileName = document.getElementById('fileName');
            const fileSize = document.getElementById('fileSize');
            const convertBtn = document.getElementById('convertBtn');
            const errorMessage = document.querySelector('.error');
            
            if (fileInput.files.length > 0) {
                const file = fileInput.files[0];
                
                const allowedTypes = ['md', 'markdown', 'txt'];
                const fileExt = file.name.split('.').pop().toLowerCase();
                
                if (!allowedTypes.includes(fileExt)) {
                    if (errorMessage) {
                        errorMessage.textContent = 'Please upload .md, .markdown, or .txt files only';
                        errorMessage.classList.add('show');
                    }
                    convertBtn.disabled = true;
                    fileInfo.classList.remove('show');
                    return;
                }
                
                if (errorMessage) {
                    errorMessage.classList.remove('show');
                }
                
                fileName.textContent = file.name;
                fileSize.textContent = formatFileSize(file.size);
                fileInfo.classList.add('show');
                convertBtn.disabled = false;
            } else {
                convertBtn.disabled = true;
                fileInfo.classList.remove('show');
            }
        }
        
        function formatFileSize(bytes) {
            if (bytes === 0) return '0 Bytes';
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
        }
        
        document.getElementById('uploadForm').addEventListener('submit', function(e) {
            const convertBtn = document.getElementById('convertBtn');
            const originalText = convertBtn.innerHTML;
            
            convertBtn.disabled = true;
            convertBtn.innerHTML = '<span class="spinner"></span> Converting...';
            
        });
        
        const uploadArea = document.querySelector('.upload-area');
        
        if (uploadArea) {
            ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                uploadArea.addEventListener(eventName, preventDefaults, false);
            });
            
            function preventDefaults(e) {
                e.preventDefault();
                e.stopPropagation();
            }
            
            ['dragenter', 'dragover'].forEach(eventName => {
                uploadArea.addEventListener(eventName, highlight, false);
            });
            
            ['dragleave', 'drop'].forEach(eventName => {
                uploadArea.addEventListener(eventName, unhighlight, false);
            });
            
            function highlight() {
                uploadArea.style.borderColor = '#667eea';
                uploadArea.style.background = '#f0f4ff';
            }
            
            function unhighlight() {
                uploadArea.style.borderColor = '#ddd';
                uploadArea.style.background = '#f9f9f9';
            }
            
            uploadArea.addEventListener('drop', handleDrop, false);
            
            function handleDrop(e) {
                const dt = e.dataTransfer;
                const files = dt.files;
                
                if (files.length > 0) {
                    document.getElementById('fileInput').files = files;
                    showFileInfo();
                }
            }
        }
        
        window.addEventListener('load', function() {
            const convertBtn = document.getElementById('convertBtn');
            const fileInput = document.getElementById('fileInput');
            
            if (fileInput && fileInput.files.length > 0) {
                showFileInfo();
            }
            

            if (convertBtn) {
                convertBtn.disabled = true;
                convertBtn.innerHTML = '<i class="fas fa-bolt"></i> Convert to PDF';
            }
        });