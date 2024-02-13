import json

# Path to your original JSONL file
input_file_path = 'data/parallel_process.jsonl'
# Path to the new file with modified entries
output_file_path = 'data/parallel_processed.jsonl'

# Open the original file for reading and the new file for writing
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        # Since the new format does not rely on the original content, it's ignored here
        # Construct the new JSON structure as per the provided specifications
        modified_data = {
            "model": "gpt-4",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a retail ecommerce assistant. You are capable of extracting the relevant attribute values from a given description of a product and expected attribute list. You ground yourself in the relevant ecommerce and category knowledge to come up with values from the given description and expected attributes.\nYou may be given an array of up to 5 products, you must iterate through the array, and output the id, product and attribute values as JSON."
                },
                {
                    "role": "user",
                    "content": "[{\n    \"id\": \"00a6128da9fceb4b981c10ea2fc45daf\",\n    \"title\": \"Bulbrite Dimmable MR16 Halogen Gu5.3 Colored Base Light Bulb - 8 pk.\",\n    \"description\": \"Dimming to your delight, the Bulbrite Dimmable MR16 Halogen Gu5.3 Colored Base Light Bulb - 8 pk. is ready to set the mood in nearly any setting. This fine halogen bulb comes in your choice of color to suit your needs. Bulbrite Since 1971, our commitment to deliver the ?Bulbrite Promise? is a company-wide focus to create an amazing customer experience. Our values-driven team finds solutions to everyday lighting needs from energy saving general purpose light bulbs to the widest range of Nostalgic vintage bulb styles and even the award-winning innovative LED retrofit system, ELEVA.Our team also delivers 99% same day shipment with a 95% fulfillment rate so you can get your product when you want it. If you find yourself asking a lot of questions about light bulbs, we?re here to help . One of our certified lighting professionals can answer your questions so feel free to give us a call or you can check out our online educational resource Lightopedia.com.Our corporate office and East Coast distribution center is located in Moonachie, NJ and our West Coast distribution center is located in Fontana, CA. Our showroom and educational training center is located in Dallas, TX.\",\n    \"primary_category\": \"Household Essentials\",\n    \"sub_category_1\": \"Light Bulbs\",\n    \"sub_category_2\": \"Halogen Bulbs\",\n    \"sub_category_3\": \"\",\n    \"sub_category_4\": \"\",\n    \"sub_category_5\": \"\",\n    \"sub_category_6\": \"\",\n    \"attributes\": \n    {\n      \"Type\": \"\",\n      \"Brand\": \"\",\n      \"Model\": \"\",\n      \"Wattage\": \"\",\n      \"Voltage\": \"\",\n      \"Base Type\": \"\",\n      \"Brightness (Lumens)\": \"\",\n      \"Light Color\": \"\",\n      \"Color Temperature\": \"\",\n      \"Dimmable\": \"\",\n      \"Life Span\": \"\",\n      \"Shape\": \"\",\n      \"Size\": {\n        \"Diameter\": \"\",\n        \"Length\": \"\"\n      },\n      \"Energy Efficiency\": \"\",\n      \"Beam Angle\": \"\",\n      \"Usage\": \"\",\n      \"Package Quantity\": \"\",\n      \"Indoor/Outdoor Use\": \"\",\n      \"Certifications\": \"\",\n      \"Warranty\": \"\"\n      }\n    },\n    {\n    \"id\": \"00bc7ff292e2ae80ba7442b05d21c7c6\",\n    \"title\": \"Krator Z Bars Replacement Handlebars Custom Bobber Harley Triumph Black 1\\\" Inch Zee Zed for Victory Hammer 8-Ball\",\n    \"description\": \"Features: 1\\\" Black Motorcycle Handlebar Features Early Chopper Styling Specification: Color: Black Style: Z-Bar Bar Size: 1\\\" Material: Heavy Duty Steel Condition: 100% Brand New Fitment: Complete Custom Application, Modification May Be Required Diameter: 1\\\" Width: 25 1/2\\\" Rise: 3 1/2\\\" Pullback: 4 1/2\\\" Center Width: 5-1/2\\\" Package Includes: 1x Black Handlebar (1\\\" Diameter) Instructions not included Victory Hammer 8-Ball Color: Black Style: Z-Bar Material: Heavy Duty Steel |1\\\" Black Motorcycle Handlebar Features Early Chopper Styling|Color: Black|Style: Z-Bar|Bar Size: 1\\\"|Material: Heavy Duty Steel|Condition: 100% Brand New|Complete Custom Application, Modification May Be Required|Diameter: 1\\\"|Width: 25 1/2\\\"|Rise: 3 1/2\\\"|Pullback: 4 1/2\\\"|Center Width: 5-1/2\\\"|1x Black Handlebar (1\\\" Diameter)|Instructions not included|Color: Black|Style: Z-Bar|Material: Heavy Duty Steel\",\n    \"primary_category\": \"Sports & Outdoors\",\n    \"sub_category_1\": \"Bikes\",\n    \"sub_category_2\": \"Bike Components\",\n    \"sub_category_3\": \"All Bike Components\",\n    \"sub_category_4\": \"\",\n    \"sub_category_5\": \"\",\n    \"sub_category_6\": \"\",\n    \"attributes\":\n    {\n  \"Component Type\": \"\",\n  \"Brand\": \"\",\n  \"Model\": \"\",\n  \"Material\": \"\",\n  \"Compatibility\": {\n    \"Bike Type\": \"\",\n    \"Brand & Model Specific\": \"\"\n  },\n  \"Weight\": \"\",\n  \"Dimensions\": \"\",\n  \"Color\": \"\",\n  \"Installation\": \"\",\n  \"Maintenance\": \"\",\n  \"Features\": \"\",\n  \"Part Number\": \"\",\n  \"Warranty\": \"\",\n  \"Package Contents\": \"\"\n}       \n\n]"             }
            ],
            "temperature": 1,
            "max_tokens": 800,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
        
        # Write the modified JSON object to the new file
        output_file.write(json.dumps(modified_data) + '\n')