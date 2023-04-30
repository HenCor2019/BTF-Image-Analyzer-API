import { Module } from '@nestjs/common';
import { ImageAnalyzerController } from './controllers';

@Module({
  controllers: [ImageAnalyzerController],
})
export class ImageAnalyzerModule { }
