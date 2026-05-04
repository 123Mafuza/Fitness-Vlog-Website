DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fitness Hub</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
</head>
<body class="bg-gray-200 font-sans">
  <!-- Header -->
  <header class="bg-gradient-to-r from-orange-600 to-orange-400 text-white py-4">
    <div class="container mx-auto px-4 flex justify-between items-center">
      <h1 class="text-3xl font-bold">Fitness Hub</h1>
      <nav>
        <ul class="flex space-x-4">
          <li><a href="#home" class="hover:underline">Home</a></li>
          <li><a href="#categories" class="hover:underline">Categories</a></li>
          <li><a href="#contact" class="hover:underline">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section id="home" class="py-12 bg-white">
    <div class="container mx-auto px-4">
      <h2 class="text-4xl font-bold text-center mb-8 animate-fade-in text-gray-800">Welcome to Fitness Hub</h2>
      <p class="text-center text-lg mb-8 text-gray-600">Your go-to source for fitness articles, videos, and workout routines.</p>
      
      <!-- Article Filter -->
      <div class="mb-6 text-center">
        <label for="category-filter" class="text-lg font-semibold mr-2 text-gray-800">Filter Articles:</label>
        <select id="category-filter" class="p-2 border rounded-lg bg-gray-100 text-gray-800">
          <option value="all">All Categories</option>
          <option value="Yoga">Yoga</option>
          <option value="Cardio">Cardio</option>
          <option value="Strength">Strength Training</option>
        </select>
      </div>

      <!-- Featured Articles -->
      <div class="bg-gradient-to-b from-gray-100 to-white py-8 rounded-lg shadow-lg mb-12">
        <h3 class="text-3xl font-bold text-center mb-6 text-gray-800">Featured Articles</h3>
        <div id="article-container" class="grid grid-cols-1 md:grid-cols-3 gap-6 px-4"></div>
      </div>

      <!-- Featured Videos -->
      <h3 class="text-2xl font-semibold mb-4 text-gray-800">Featured Workout Videos</h3>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="video-card">
          <iframe class="w-full h-64 rounded-lg" src="https://www.youtube.com/embed/hJbRpHZr_d0" title="Cardio Blast" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          <p class="mt-2 text-center text-gray-600">Cardio Blast</p>
        </div>
        <div class="video-card">
          <iframe class="w-full h-64 rounded-lg" src="https://www.youtube.com/embed/hJbRpHZr_d0" title="Yoga Flow" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          <p class="mt-2 text-center text-gray-600">Yoga Flow</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Categories Section -->
  <section id="categories" class="py-12 bg-gray-100">
    <div class="container mx-auto px-4">
      <h2 class="text-3xl font-bold text-center mb-8 animate-fade-in text-gray-800">Fitness Categories</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white p-6 rounded-lg shadow-md category-card">
          <img src="https://images.unsplash.com/photo-1545205597-3d9d02c29597?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Yoga" class="w-full h-40 object-cover rounded-lg mb-4">
          <h3 class="text-xl font-semibold mb-2 text-gray-800">Yoga</h3>
          <p class="text-gray-600">Explore yoga routines for flexibility and mindfulness.</p>
          <a href="#" class="text-orange-600 hover:underline">View Yoga Content</a>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md category-card">
          <img src="https://images.pexels.com/photos/3823039/pexels-photo-3823039.jpeg?auto=compress&cs=tinysrgb&w=800" alt="Cardio" class="w-full h-40 object-cover rounded-lg mb-4">
          <h3 class="text-xl font-semibold mb-2 text-gray-800">Cardio</h3>
          <p class="text-gray-600">High-energy workouts to boost your heart rate.</p>
          <a href="#" class="text-orange-600 hover:underline">View Cardio Content</a>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md category-card">
          <img src="https://images.unsplash.com/photo-1517838277536-f5f99be501cd?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Strength Training" class="w-full h-40 object-cover rounded-lg mb-4">
          <h3 class="text-xl font-semibold mb-2 text-gray-800">Strength Training</h3>
          <p class="text-gray-600">Build muscle with our strength training guides.</p>
          <a href="#" class="text-orange-600 hover:underline">View Strength Content</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="py-12 bg-white">
    <div class="container mx-auto px-4">
      <h2 class="text-3xl font-bold text-center mb-8 animate-fade-in text-gray-800">Get in Touch</h2>
      <div class="max-w-md mx-auto">
        <div id="contact-form" class="space-y-4">
          <div>
            <label for="name" class="block text-sm font-medium text-gray-800">Name</label>
            <input type="text" id="name" class="w-full p-2 border rounded-lg bg-gray-100 text-gray-800" placeholder="Your name">
          </div>
          <div>
            <label for="email" class="block text-sm font-medium text-gray-800">Email</label>
            <input type="email" id="email" class="w-full p-2 border rounded-lg bg-gray-100 text-gray-800" placeholder="Your email">
          </div>
          <div>
            <label for="message" class="block text-sm font-medium text-gray-800">Message</label>
            <textarea id="message" class="w-full p-2 border rounded-lg bg-gray-100 text-gray-800" rows="4" placeholder="Your message"></textarea>
          </div>
          <button id="submit-btn" class="w-full bg-orange-600 text-white p-2 rounded-lg hover:bg-orange-700 transition-colors">Submit</button>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-gradient-to-r from-orange-600 to-orange-400 text-white py-4">
    <div class="container mx-auto px-4 text-center">
      <p>© 2025 Fitness Hub. All rights reserved.</p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
