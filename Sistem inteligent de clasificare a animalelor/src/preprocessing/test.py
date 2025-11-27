def predict_image(model, img_path):
    from tensorflow.keras.preprocessing import image
    import numpy as np
    
    img = image.load_img(img_path, target_size=IMG_SIZE)
    arr = image.img_to_array(img)/255.0
    arr = np.expand_dims(arr,0)
    
    species_pred, owner_pred, size_pred = model.predict(arr)
    
    species_label = 'dog' if np.argmax(species_pred[0])==1 else 'cat'
    owner_prob = float(owner_pred[0][0])
    size_label = ['small','medium','large'][int(np.argmax(size_pred[0]))]
    
    if species_label=='cat':
        size_label = None
    
    return {'species':species_label, 'has_owner_prob':owner_prob, 'size':size_label}

# exemplu
result = predict_image(model, IMAGES_DIR / "dog_small/dog_small_001.jpg")
print(result)
