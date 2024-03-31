import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import HomePage from '../components/HomePage'
import AlbumDetails from '../components/AlbumDetails/AlbumDetails';
import AlbumFormPage from '../components/AlbumFormPage/AlbumFormPage.jsx';
import PlaylistFormPage from '../components/PlaylistFormPage/PlaylistFormPage.jsx';
import MusicPlayer from "../components/MusicPlayer/MusicPlayer.jsx";
import ManageAlbums from '../components/ManageAlbums/ManageAlbums.jsx';
import AllPlaylists from '../components/AllPlaylistsCurrentUser/AllPlaylistsCurrentUser.jsx';
import PlaylistDetails from '../components/PlaylistDetails/PlaylistDetails.jsx';
import Layout from './Layout';
import EditAlbumForm from '../components/EditAlbumForm/EditAlbumForm.jsx';
import LikedTracks from '../components/LikedTracks/LikedTracks.jsx';
import EditPlaylistForm from '../components/EditPlaylistForm/EditPlaylistForm.jsx';
import TrackFormPage from '../components/TrackFormPage/index.js';


export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      {
        path: "/login",
        element: <LoginFormPage />,
      },
      {
        path: "/signup",
        element: <SignupFormPage />,
      },
      {
        path: '/player',
        element: <MusicPlayer/>,
      },
      {
        path: '/albums/:albumId',
        element: <AlbumDetails />
      },
      {
        path: '/albums/new',
        element: <AlbumFormPage />
      },
      {
        path: '/playlists/new',
        element: <PlaylistFormPage />
      },
      {
        path: '/albums/manage',
        element: <ManageAlbums />
      },
      {
        path: '/albums/:albumId/edit',
        element: <EditAlbumForm />
      },
      {
        path: '/albums/:albumId/tracks/new',
        element: <TrackFormPage />
      },
      {
        path: '/playlists/:playlistId/edit',
        element: <EditPlaylistForm />
      },
      {
        path: '/liked',
        element: <LikedTracks />
      },
      {
        path: '/playlists',
        element: <AllPlaylists />
      },
      {
        path: '/playlists/:playlistId',
        element: <PlaylistDetails />
      }
    ],
  },
]);
