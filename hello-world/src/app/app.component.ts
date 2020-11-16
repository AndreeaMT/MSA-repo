import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  parasites = [{name: 'test'}];

  constructor(private api: ApiService) {
    this.getParasites();
  }

  getParasites = () => {
    this.api.getAllParasites().subscribe(
      data => {
        this.parasites = data;
      },
      error => {
        console.log(error);
      }
    )
  }
}
