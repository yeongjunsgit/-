<template>
  <div>
    <div id="menu_wrap">
      <form @submit.prevent="searchBanksNearby">
        <input type="text" v-model="location" placeholder="위치" />
        <input type="text" v-model="bankName" placeholder="은행명" />
        <button type="submit">검색</button>
      </form>
    </div>
    <div id="map"></div>
    <div id="placesList"></div>
    <div id="pagination"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      location: "",
      bankName: "",
      markers: [],
      map: null,
      infowindow: null,
    };
  },
  mounted() {
    this.loadKakaoMapScript();
  },
  methods: {
    async loadKakaoMapScript() {
      if (window.kakao && window.kakao.maps) {
        // 이미 로드되어 있다면 바로 초기화
        this.initMap();
      } else {
        // Kakao 지도 API 스크립트 로드
        await new Promise((resolve) => {
          const script = document.createElement("script");
          script.onload = () => {
            window.kakao.maps.load(() => {
              resolve();
            });
          };
          script.src =
            "//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=515518f4fc322125ee5a59b92e14d7b6&libraries=services,clusterer,drawing";
          document.head.appendChild(script);
        });

        // 초기화
        this.initMap();
      }
    },
    initMap() {
      const container = document.getElementById("map");
      const options = {
        center: new window.kakao.maps.LatLng(37.566826, 126.9786567),
        level: 3,
      };

      this.map = new window.kakao.maps.Map(container, options);
      this.infowindow = new window.kakao.maps.InfoWindow({ zIndex: 1 });
    },
    searchBanksNearby() {
      const location = this.location.trim();
      const bankName = this.bankName.trim();

      if (!location || !bankName) {
        alert("위치와 은행명을 입력해주세요!");
        return;
      }

      // 검색을 위한 로직을 추가하세요.
      // 위치와 은행명을 이용하여 검색하고 결과를 처리하세요.
      // 예시로 주변 은행을 검색하는 함수를 호출하도록 작성했습니다.
      this.searchNearbyBanks(location, bankName);
    },
    searchNearbyBanks(location, bankName) {
      // 여기에 위치와 은행명을 이용하여 검색하는 로직을 추가하세요.
      // 검색된 결과를 this.displayPlaces 메서드로 전달하여 표시하세요.
      const ps = new window.kakao.maps.services.Places();
      const keyword = `${location} ${bankName}`;
      ps.keywordSearch(keyword, this.placesSearchCB);
    },
    placesSearchCB(data, status, pagination) {
      if (status === window.kakao.maps.services.Status.OK) {
        this.displayPlaces(data);
        this.displayPagination(pagination);
      } else if (status === window.kakao.maps.services.Status.ZERO_RESULT) {
        alert("검색 결과가 존재하지 않습니다.");
      } else if (status === window.kakao.maps.services.Status.ERROR) {
        alert("검색 결과 중 오류가 발생했습니다.");
      }
    },
    displayPlaces(places) {
      const listEl = document.getElementById("placesList"),
        bounds = new window.kakao.maps.LatLngBounds();

      // 기존 마커 및 목록 삭제
      this.removeMarker();
      this.removeAllChildNodes(listEl);

      places.forEach((place, index) => {
        const placePosition = new window.kakao.maps.LatLng(place.y, place.x);
        const marker = this.addMarker(placePosition, index);
        const itemEl = this.getListItem(index, place);

        bounds.extend(placePosition);

        itemEl.addEventListener("mouseover", () => {
          this.displayInfowindow(marker, place.place_name);
        });

        itemEl.addEventListener("mouseout", () => {
          this.infowindow.close();
        });

        listEl.appendChild(itemEl);
      });

      this.map.setBounds(bounds);
    },
    addMarker(position, idx) {
      const imageSrc =
        "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png";
      const imageSize = new window.kakao.maps.Size(36, 37);
      const imgOptions = {
        spriteSize: new window.kakao.maps.Size(36, 691),
        spriteOrigin: new window.kakao.maps.Point(0, (idx * 46) + 10),
        offset: new window.kakao.maps.Point(13, 37),
      };

      const markerImage = new window.kakao.maps.MarkerImage(
        imageSrc,
        imageSize,
        imgOptions
      );

      const marker = new window.kakao.maps.Marker({
        position: position,
        image: markerImage,
      });

      marker.setMap(this.map);
      this.markers.push(marker);

      return marker;
    },
    removeMarker() {
      this.markers.forEach((marker) => marker.setMap(null));
      this.markers = [];
    },
    displayInfowindow(marker, title) {
      const content = '<div style="padding:5px;z-index:1;">' + title + "</div>";
      this.infowindow.setContent(content);
      this.infowindow.open(this.map, marker);
    },
    getListItem(index, place) {
      // 이 부분을 적절히 수정하세요.
      const itemEl = document.createElement("div");
      itemEl.className = "item";
      itemEl.innerHTML = '<span class="markerbg marker_' + (index + 1) + '"></span>' + place.place_name;
      return itemEl;
    },
    removeAllChildNodes(el) {
      while (el.hasChildNodes()) {
        el.removeChild(el.lastChild);
      }
    },
    displayPagination(pagination) {
      const paginationEl = document.getElementById("pagination");
      const fragment = document.createDocumentFragment();

      while (paginationEl.hasChildNodes()) {
        paginationEl.removeChild(paginationEl.lastChild);
      }

      for (let i = 1; i <= pagination.last; i++) {
        const el = document.createElement("a");
        el.href = "#";
        el.innerHTML = i;

        if (i === pagination.current) {
          el.className = "on";
        } else {
          el.addEventListener("click", () => {
            pagination.gotoPage(i);
          });
        }

        fragment.appendChild(el);
      }

      paginationEl.appendChild(fragment);
    },
  },
};
</script>

<style scoped>
#map {
  width: auto;
  height: 600px;
}

.button-group {
  margin: 10px 0px;
}

button {
  margin: 0 3px;
}
</style>
