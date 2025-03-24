// JavaScript to fix case-sensitive URLs
document.addEventListener('DOMContentLoaded', function() {
  // Check if current URL contains "/about/" (lowercase)
  var currentPath = window.location.pathname.toLowerCase();
  
  if (currentPath.includes('/about/') && !window.location.pathname.includes('/About/')) {
    // Replace with correct case and redirect
    var correctedPath = window.location.pathname.replace('/about/', '/About/');
    window.location.href = correctedPath;
  }
}); 