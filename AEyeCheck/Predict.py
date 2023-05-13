import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# Fine-grained Model
class FineGrainedClassifier(nn.Module):
    def __init__(self, pretrained_model):
        super(FineGrainedClassifier, self).__init__()
        self.pretrained = pretrained_model

    def forward(self, x):
        return self.pretrained(x)

# Coarse-grained Model
class CoarseGrainedClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(CoarseGrainedClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        return  self.fc2(self.relu(self.fc1(x)))


class Predict():
    def __init__(self,module,cgPath,fgPath):
        self.module=module
        self.cgPath=cgPath
        self.fgPath=fgPath
        pretrained_model = torch.hub.load('pytorch/vision:v0.9.0', 'resnet50', pretrained=True)
        pretrained_model.fc = nn.Linear(pretrained_model.fc.in_features, 4)

        # fine_grained_classifier = FineGrainedClassifier(pretrained_model)
        # fine_grained_classifier.load_state_dict(torch.load(self.fgPath))
        # fine_grained_classifier.eval()

        coarse_grained_classifier = CoarseGrainedClassifier(4, 64, 4)
        coarse_grained_classifier.load_state_dict(torch.load(self.cgPath))
        coarse_grained_classifier.eval()

    def preprocess(image_path):
        image = Image.open(image_path)
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])
        image = preprocess(image)
        image = torch.unsqueeze(image, 0)
        return image


    def predict(self,image_path):
        if self.module=="DiabeticRetinopathy":
            image = self.preprocess(image_path)
            #fine_output = self.fine_grained_classifier(image)
            coarse_output = self.coarse_grained_classifier(fine_output.detach())
            #_, fine_pred = torch.max(fine_output.data, 1)
            _, coarse_pred = torch.max(coarse_output.data, 1)
            #return fine_pred.item(), coarse_pred.item()
            return coarse_pred.item()
        elif self.module=="Glaucoma":
            return


