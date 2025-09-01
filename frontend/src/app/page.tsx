import Image from 'next/image'

export default function Home() {
  return (
    <div className="font-sans min-h-screen w-full flex flex-col gap-16 p-8 sm:p-20">
      
      {/* Hero Section */}
      <section className="w-full mt-12 bg-gradient-to-r from-amber-200 to-amber-300 rounded-xl shadow-lg flex flex-col items-center justify-center text-center py-20">
        <h1 className="text-4xl md:text-5xl font-bold text-brown-900">
          Marketplace for Great Coffee
        </h1>
        <p className="mt-4 text-lg md:text-xl text-brown-700 max-w-2xl">
          Freshly roasted beans, artisanal blends, and brewing essentials — delivered straight to your door.
        </p>
        <button className="mt-8 bg-brown-700 text-white px-6 py-3 rounded-lg shadow hover:bg-brown-800 transition">
          Shop Now
        </button>
      </section>

      {/* Image Slideshow */}
      <section className="w-full bg-gray-200 flex items-center justify-center h-80 rounded-md">
        <p className="text-xl font-bold">Image Slideshow</p>
      </section>

      {/* Featured Items */}
      <section className="w-full">
        <h2 className="text-2xl font-semibold mb-4">Featured Items</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 w-full">
          <div className="bg-white p-4 shadow rounded">Item 1</div>
          <div className="bg-white p-4 shadow rounded">Item 2</div>
          <div className="bg-white p-4 shadow rounded">Item 3</div>
          <div className="bg-white p-4 shadow rounded">Item 4</div>
        </div>
      </section>

      {/* All Products */}
      <section className="w-full mb-12">
        <h2 className="text-2xl font-semibold mb-4">All Products</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 w-full">
          <div className="bg-white p-4 shadow rounded">Product A</div>
          <div className="bg-white p-4 shadow rounded">Product B</div>
          <div className="bg-white p-4 shadow rounded">Product C</div>
          <div className="bg-white p-4 shadow rounded">Product D</div>
        </div>
      </section>
    </div>
  )
}
