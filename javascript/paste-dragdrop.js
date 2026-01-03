// Fix for Gradio 4.44.1 clipboard paste and drag-drop issues in Chrome

(function() {
    'use strict';

    console.log('Loading paste and drag-drop fix for Gradio 4.44.1');

    function initializeImageUploadHandlers() {
        // Find all image upload components
        const imageInputs = document.querySelectorAll('input[type="file"][accept*="image"]');
        
        imageInputs.forEach(function(input) {
            const container = input.closest('.image-container, [data-testid="image"], .upload-container');
            if (!container) return;
            
            // Prevent duplicate handlers
            if (container.dataset.pasteHandlerAdded) return;
            container.dataset.pasteHandlerAdded = 'true';
            
            console.log('Adding paste and drag-drop handlers to image input');

            // Handle paste events
            container.addEventListener('paste', function(e) {
                console.log('Paste event detected');
                const items = (e.clipboardData || e.originalEvent.clipboardData).items;
                
                for (let i = 0; i < items.length; i++) {
                    if (items[i].type.indexOf('image') !== -1) {
                        e.preventDefault();
                        e.stopPropagation();
                        
                        const blob = items[i].getAsFile();
                        const dataTransfer = new DataTransfer();
                        dataTransfer.items.add(blob);
                        input.files = dataTransfer.files;
                        
                        // Trigger change event
                        const event = new Event('change', { bubbles: true });
                        input.dispatchEvent(event);
                        
                        console.log('Image pasted successfully');
                        break;
                    }
                }
            }, true);

            // Handle drag and drop
            container.addEventListener('dragover', function(e) {
                e.preventDefault();
                e.stopPropagation();
                container.classList.add('drag-over');
            }, true);

            container.addEventListener('dragleave', function(e) {
                e.preventDefault();
                e.stopPropagation();
                container.classList.remove('drag-over');
            }, true);

            container.addEventListener('drop', function(e) {
                console.log('Drop event detected');
                e.preventDefault();
                e.stopPropagation();
                container.classList.remove('drag-over');
                
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    // Filter for image files
                    const imageFiles = Array.from(files).filter(file => file.type.startsWith('image/'));
                    
                    if (imageFiles.length > 0) {
                        const dataTransfer = new DataTransfer();
                        imageFiles.forEach(file => dataTransfer.items.add(file));
                        input.files = dataTransfer.files;
                        
                        // Trigger change event
                        const event = new Event('change', { bubbles: true });
                        input.dispatchEvent(event);
                        
                        console.log('Image dropped successfully');
                    }
                }
            }, true);
        });

        // Also add paste handler to document body for global paste
        if (!document.body.dataset.globalPasteHandlerAdded) {
            document.body.dataset.globalPasteHandlerAdded = 'true';
            
            document.body.addEventListener('paste', function(e) {
                // Only handle if we're not in a text input
                if (e.target.tagName === 'INPUT' && e.target.type === 'text') return;
                if (e.target.tagName === 'TEXTAREA') return;
                if (e.target.isContentEditable) return;
                
                const items = (e.clipboardData || e.originalEvent.clipboardData).items;
                
                for (let i = 0; i < items.length; i++) {
                    if (items[i].type.indexOf('image') !== -1) {
                        console.log('Global paste event with image detected');
                        
                        // Find the visible image input
                        const visibleInputs = Array.from(document.querySelectorAll('input[type="file"][accept*="image"]'))
                            .filter(input => {
                                const rect = input.getBoundingClientRect();
                                return rect.width > 0 && rect.height > 0;
                            });
                        
                        if (visibleInputs.length > 0) {
                            e.preventDefault();
                            e.stopPropagation();
                            
                            const blob = items[i].getAsFile();
                            const dataTransfer = new DataTransfer();
                            dataTransfer.items.add(blob);
                            visibleInputs[0].files = dataTransfer.files;
                            
                            // Trigger change event
                            const event = new Event('change', { bubbles: true });
                            visibleInputs[0].dispatchEvent(event);
                            
                            console.log('Image pasted to visible input');
                            break;
                        }
                    }
                }
            }, true);
        }
    }

    // Initialize on load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeImageUploadHandlers);
    } else {
        initializeImageUploadHandlers();
    }

    // Re-initialize when UI updates (for dynamically loaded components)
    const observer = new MutationObserver(function(mutations) {
        initializeImageUploadHandlers();
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    // Also hook into Gradio's mount event if available
    if (window.gradioApp) {
        const app = window.gradioApp();
        if (app) {
            observer.observe(app, {
                childList: true,
                subtree: true
            });
        }
    }

    console.log('Paste and drag-drop fix loaded successfully');
})();
