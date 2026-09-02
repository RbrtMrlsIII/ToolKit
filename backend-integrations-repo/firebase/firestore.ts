// Firestore — generic authority
import { getFirestore, collection, addDoc } from 'firebase/firestore';
import { firebaseApp } from './firebase-config';

export const db = getFirestore(firebaseApp);
export const projectsCol = collection(db, 'projects');
export const knowledgeCol = collection(db, 'knowledge');
