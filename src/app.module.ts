import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ImageAnalyzerModule } from './image-analyzer/image-analyzer.module';

@Module({
  imports: [ImageAnalyzerModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule { }
