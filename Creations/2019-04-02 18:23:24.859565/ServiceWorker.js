const CACHE = 'TODO';
const TITLE = 'TODO';
const EXPECTED_CACHE = [CACHE];
/* Service Worker Lifecycle
 *      - Download
 *      - Install
 *      - Activate
 */

// Install
self.addEventListener('install', event => {
	// The service worker will have to be in the same parent folder as index.html
	// We will keep this as one file, so this file doesn't have to be changed
    var index = new Request('index.html');
    event.waitUntil(
        fetch(index).then(response => {
            return caches.open(CACHE).then(cache => {       // This returns a promise, then caches page
                console.log(TITLE + 'Cached: ' + response.url);
                return cache.put(index, response);                  // Actually caches page
            });
        }).catch(error => console.log(TITLE + 'An error occured: ' + error))
    );
});

// Activate
// Clean up caches
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => Promise.all(
            keys.map(key => {
                if (!EXPECTED_CACHE.includes(key)) {
                    return caches.delete(key);
                }
            })
        ))//.then(() => console.log(TITLE + 'Cache cleaned; Ready to handle fetches'))
    );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Cache hit - return response
        if (response) {
          return response;
        }
        return fetch(event.request);
      }
    )
  );
});
