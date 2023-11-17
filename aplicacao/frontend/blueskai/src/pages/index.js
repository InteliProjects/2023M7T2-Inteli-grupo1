import React from 'react';
import { Dashboard } from '@/views/Dashboard';
import { SideBar } from '@/components/SideBar';

export default function Home() {
  return (
    <SideBar>
      <Dashboard/>
    </SideBar>
  );
}