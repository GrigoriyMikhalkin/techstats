import {Injectable} from '@angular/core';
import {Http, Headers} from '@angular/http';
import 'rxjs/add/operator/map';


@Injectable()
export class TechsService{
  constructor (private http:Http) {
    console.log("Techs Service Initialized...");     
  }

  getTechs () {
    return this.http.get('http://localhost:8000/techs')
    	   .map(res => res.json());
  }

}