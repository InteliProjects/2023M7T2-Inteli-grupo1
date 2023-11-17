import Head from 'next/head'
import Image from 'next/image'
import styles from '@/styles/Home.module.css'
import { LoginPage } from '@/views/LoginPage'

export default function Home() {
  return (
    <>
     <LoginPage/>
    </>
  )
}
