import type { Metadata, Viewport } from 'next';
import './globals.css';

const siteOrigin = 'https://thane-rush.saurabhsalunkhe.chatgpt.site';

export const metadata: Metadata = {
  metadataBase: new URL(siteOrigin),
  title: 'Thane Rush — Lakeside to Hillside',
  description:
    'A free original 3D arcade driving game inspired by Upvan Lake, Yeoor Hills, and the streets of Thane.',
  openGraph: {
    title: 'Thane Rush — Lakeside to Hillside',
    description:
      'Race from Upvan Lake to Yeoor Hills in this original 3D arcade driving game.',
    url: siteOrigin,
    siteName: 'Thane Rush',
    images: [
      {
        url: `${siteOrigin}/og.png`,
        width: 1440,
        height: 900,
        alt: 'Thane Rush arcade driving game menu',
      },
    ],
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Thane Rush — Lakeside to Hillside',
    description:
      'Race from Upvan Lake to Yeoor Hills in this original 3D arcade driving game.',
    images: [`${siteOrigin}/og.png`],
  },
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  themeColor: '#142924',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
