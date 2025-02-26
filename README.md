Project for the exploring your phone photos with embeddings and computer vision


1. Make sure Postgres is set up as the embedding store
2. Load photos
   2. Without Exif
   3. With Exif
4. Find blurry and overexposed photos
3. Load Models
4. Calculate embeddings
5. Vizualize the embeddings
   6. Resnet - two different training sets
   7. OpenClip
   8. Aimv2 
      9. https://medium.com/voxel51/visual-understanding-with-aimv2-76c58dcd68f9 
      10. https://medium.com/voxel51/aimv2-outperforms-clip-on-synthetic-dataset-imagenet-d-4452760b624c
   11. Concat embeddings and visualize
6.  Word Cloud - https://github.com/harpreetsahota204/janus-vqa-fiftyone
7. Zero Shot Prediction  - object recognition 
8. Train to recognize: Aya, Hedy, Bo, Disco, Me 
9. Train it to find Tess and look at her embeddings over time