# generative-nft

A python based library to help you create unique generative NFT's based on Rarity ⭐️.


## How to use

- Place all your layers in the `layers` folder. Make folders for each traits and add images inside it.
  For example:
  layers
  ├── body
  |    |─── body.png
  ├── cloths                    
  │   ├── red-top.png          
  │   ├── blue-shirt.png         
  │   └── green-top.png                
  └── ...

- Edit the traits in `main.py`. Create `Variant` under each trait and add their respective rarity `(0<= && <=1)`
- Edit the `count` in `main` to the number of Unique NFT you want to generate.
- Edit `minimumDifference` if needed, this is the number of minimum difference in Traits each NFT will have to ensure complete uniqueness. Make sure you don't keep this very high which would end up in a very slow process/infinite loop.
- That's it! Run the `main.py` and wait for the images to be created.

<a href="https://www.buymeacoffee.com/kartikay" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
