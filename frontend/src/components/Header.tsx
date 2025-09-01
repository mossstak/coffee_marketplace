'use client'
import { useState } from 'react'
import Link from 'next/link'
import {
  LucideHome,
  LucideMenu,
  LucideShoppingCart,
  LucideCircleUserRound,
  LucideStore,
  LucideX,
  Search,
} from 'lucide-react'
import { homePath, shopPath, aboutPath } from '@/paths'
import { buttonVariants } from './ui/button'

const Header = () => {
  const [isOpen, setIsOpen] = useState(false)
  const [search, setSearch] = useState('')

  const toggleMenu = () => {
    setIsOpen(!isOpen)
  }

  const searchItems = () => {
    console.log('Searching For: ', search)
    // Example: filter logic
    // const results = items.filter(item => item.name.toLowerCase().includes(search.toLowerCase()));
    // setFilteredResults(results);
  }

  return (
    <nav className=" bg-[#B17457] fixed top-0 left-0 right-0 z-50 shadow-md shadow-black/50 dark:bg-black">
      <div className="flex items-center justify-between p-4">
        {/* Logo */}
        <Link
          href={homePath()}
          className={buttonVariants({ variant: 'ghost' })}
        >
          <h1 className="text-lg font-semibold"> Coffee Marketplace</h1>
        </Link>

        <div className="hidden md:flex items-center gap-x-2">
          <form
            onSubmit={(e) => {
              e.preventDefault()
              searchItems()
            }}
            className="rounded-xl p-3 w-[500px] border-black border-solid border-3"
          >
            <div className="flex justify-between gap-3">
              <input
                type="text"
                placeholder="Search.."
                className="w-full"
                name="Search"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
              <button
                type="submit"
                className="focus:outline-2 focus:outline-black"
              >
                <Search />
              </button>
            </div>
          </form>
        </div>

        {/* Desktop Menu - Hidden on mobile */}
        <div className="hidden md:flex items-center gap-x-2">
          <Link href={aboutPath()} className={buttonVariants({ variant: 'ghost' })}>
            <h1 className="text-lg font-semibold">About</h1>
          </Link>
          <Link
            href={shopPath()}
            className={buttonVariants({ variant: 'ghost' })}
          >
            <h1 className="text-lg font-semibold">Shop</h1>
          </Link>
          <Link href={'#'} className={buttonVariants({ variant: 'ghost' })}>
            <h1 className="text font-semibold">Login</h1>
          </Link>
        </div>
        {/* Mobile Menu Button - Only visible on mobile */}
        <button
          onClick={toggleMenu}
          className="md:hidden p-2 transition-transform duration-200"
          aria-label="Toggle menu"
        >
          <div
            className={`transition-transform duration-300 ${
              isOpen ? 'rotate-180' : ''
            }`}
          >
            {isOpen ? <LucideX size={24} /> : <LucideMenu size={24} />}
          </div>
        </button>
      </div>

      {isOpen && (
        <div className="md:hidden dark:bg-black border-t h-screen overflow-y-auto transform transition-transform duration-300">
          <div className="transform translate ease-in-out">
            <div className="flex flex-col justify-between items-center p-4">
              <form
                onSubmit={(e) => {
                  e.preventDefault()
                  searchItems()
                }}
                className="rounded-xl p-3 w-[350px] mb-3 border-black border-solid border-3"
              >
                <div className="flex justify-between gap-3">
                  <input
                    type="text"
                    placeholder="Search.."
                    className="w-full"
                    name="Search"
                    value={search}
                    onChange={(e) => setSearch(e.target.value)}
                  />
                  <button
                    type="submit"
                    className="focus:outline-2 focus:outline-black"
                  >
                    <Search />
                  </button>
                </div>
              </form>
              <div className="flex flex-col gap-3 ">
                <Link
                  href={homePath()}
                  className={buttonVariants({ variant: 'outline' })}
                  onClick={() => setIsOpen(false)}
                >
                  <div className="flex gap-3 items-center ">
                    <LucideHome /> <p>Home</p>
                  </div>
                </Link>
                <Link
                  href={aboutPath()}
                  className={buttonVariants({ variant: 'outline' })}
                  onClick={() => setIsOpen(false)}
                >
                  <div className="flex gap-3 items-center ">
                    <LucideCircleUserRound /> <p>About</p>
                  </div>
                </Link>
                <Link
                  href={'#'}
                  className={buttonVariants({ variant: 'outline' })}
                  onClick={() => setIsOpen(false)}
                >
                  <div className="flex gap-3 items-center ">
                    <LucideStore /> <p>Shop</p>
                  </div>
                </Link>
              </div>
            </div>
          </div>
        </div>
      )}
    </nav>
  )
}

export default Header
