/* global $, angular uploadcare */
angular.module('dragApp', [])
.controller('dragCtrl', function ($scope, $http) {
  $scope.drag = []
  $scope.freezer = []
  $scope.index = ''

  $scope.getData = function () {
    console.log('get ครั้งที่ 1')
    $http.get('/api').success(function (response) {
      $scope.drag = response
      // ////// LED Check //////
      $scope.CheckData = []
      for (var i = 0; i < $scope.drag.length; i++) {
        $scope.CheckData[i] = $scope.drag[i].endDate
        let now = new Date()
        let datePick = new Date($scope.CheckData[i])
        let SUMDATA = Math.ceil((datePick - now) / (1000 * 3600 * 24))
        if (SUMDATA <= 0) {
          console.log('เข้าในนี้ไหม 1')
          $scope.state = 1
        }else {
          $scope.stood = 1
        }
      }
      // ////// LED Check //////
    })
  }
  $scope.getData()
  $scope.positionDrag = function (index) {
    var css = $('#' + index).position()
    css.position = 'absolute'
    $scope.drag[index].css = css
    $http.put('/api/' + $scope.drag[index]['_id'], $scope.drag[index]).then(function (res) {
      console.log(res.data)
    })
  }

  $scope.init = function () {
    $scope.drag.forEach(function (item) {
      $('#' + item.ArrDrag).draggable()
      $('#' + item.ArrDrag).css(item.css)
    })
  }
  $scope.addDrag = function (day) {
    var ArrDrag = $scope.drag.length
    var endDate = new Date(+new Date() + (day * 24 * 60 * 60 * 1000))
    var dataForPush = {things: '', startDate: new Date(), endDate: endDate, days: day, ArrDrag: ArrDrag, css: {top: 200, left: 250, position: 'absolute'}}
    $http.post('/api', dataForPush).success(function (response) {
      $scope.drag.push(response)
    }).error(function (data, status, headers, config) {
      console.log('error')
    })
  }
  $scope.openDragCustom = function () {
    $('#openDragCustom').openModal()
  }
  $scope.addDragCustom = function (THING, DAY) {
    var ArrDrag = $scope.drag.length
    var now = new Date()
    var datePick = new Date(DAY)
    var SUM = Math.ceil((datePick - now) / (1000 * 3600 * 24))
    var endDate = new Date(+new Date() + (SUM * 24 * 60 * 60 * 1000))
    var dataCustomForPush = {things: THING, startDate: new Date(), endDate: endDate, days: SUM, ArrDrag: ArrDrag, css: {top: 200, left: 250, position: 'absolute'}}
    $http.post('/api', dataCustomForPush).success(function (response) {
      $scope.drag.push(response)
      $scope.THING = ''
      $scope.DAY = ''
    }).error(function (data, status, headers, config) {
      console.log('error')
    })
  }
  $scope.openDragUpdate = function (item, index) {
    $('#openDragUpdate').openModal()
    $scope.index = index
    $scope.updateThing = item.things
    $scope.updateDay = item.days
  }
  $scope.updateDrag = function (updateThing, updateDay) {
    if ($scope.drag[$scope.index].things === updateThing) {
      console.log('true')
    }if ($scope.drag[$scope.index].days === updateDay) {
      console.log('true')
    }if ($scope.drag[$scope.index].things !== updateThing) {
      $scope.drag[$scope.index].things = updateThing
    }if ($scope.drag[$scope.index].days !== updateDay) {
      var noww = new Date()
      var datePickk = new Date(updateDay)
      var SUMM = Math.ceil((datePickk - noww) / (1000 * 3600 * 24))
      $scope.drag[$scope.index].things = updateThing
      $scope.drag[$scope.index].days = SUMM
      $scope.drag[$scope.index].endDate = new Date(updateDay)
    }
    $http.put('/api/' + $scope.drag[$scope.index]['_id'], $scope.drag[$scope.index]).then(function (res) {
      console.log(res.data)
    })
  }
  $scope.deleteDrag = function (index) {
    $http.delete('/api/' + $scope.drag[$scope.index]['_id']).then(function (res) {
      $scope.drag.splice($scope.index, 1)
      console.log(res.data)
    })
  }
  $scope.countExpireDate = function (date) {
    var now = new Date()
    var datePick = new Date(date)
    var SUMDATA = Math.ceil((datePick - now) / (1000 * 3600 * 24))
    if (SUMDATA <= 0) {
      return (0)
    }else {
      return SUMDATA
    }
  }
  // ////////////////////////// FREEZER ////////////////////////////////////////
  $scope.url = ''
  var widget1 = uploadcare.Widget('[role=uploadcare-uploader][id=u1]')
  var widget2 = uploadcare.Widget('[role=uploadcare-uploader][id=u2]')
  widget1.onChange(function (file) {
    if (file) {
      console.log(file)
      file.done(function (fileInfo) {
        console.log(fileInfo.cdnUrl)
        $scope.url = fileInfo.cdnUrl
      }).fail(function (error, fileInfo) {
        console.log(error)
        console.log(fileInfo)
      })
    }
  })
  widget2.onChange(function (file) {
    if (file) {
      console.log(file)
      file.done(function (fileInfo) {
        console.log(fileInfo.cdnUrl)
        $scope.updateURL = fileInfo.cdnUrl
      }).fail(function (error, fileInfo) {
        console.log(error)
        console.log(fileInfo)
      })
    }
  })
  // ///////////////////////////////////////////////////////
  $scope.getDataFreezer = function () {
    console.log('getFreezer ครั้งที่ 1')
    $http.get('/freezer').success(function (response) {
      $scope.freezer = response
      // ////// LED Check //////
      $scope.CheckFreezer = []
      for (var i = 0; i < $scope.drag.length; i++) {
        $scope.CheckFreezer[i] = $scope.drag[i].endDate
        let now = new Date()
        let datePick = new Date($scope.CheckFreezer[i])
        let SUMDATA = Math.ceil((datePick - now) / (1000 * 3600 * 24))
        if (SUMDATA <= 0) {
          console.log('เข้าในนี้ไหม 2')
          $scope.state = 1
        }else {
          $scope.stood = 1
        }
      }
      // ////// LED Check //////
    })
  }
  $scope.getDataFreezer()
  $scope.openFreezer = function () {
    $('#openFreezer').openModal()
  }
  $scope.addDataFreezer = function (TFREEZER, DFREEZER) {
    var ArrDrag = $scope.freezer.length
    var now = new Date()
    var datePick = new Date(DFREEZER)
    var SUM = Math.ceil((datePick - now) / (1000 * 3600 * 24))
    var endDate = new Date(+new Date() + (SUM * 24 * 60 * 60 * 1000))
    var dataFreezerForPush = {things: TFREEZER, startDate: new Date(), endDate: endDate, days: SUM, ArrDrag: ArrDrag, Url: $scope.url}
    $http.post('/freezer', dataFreezerForPush).success(function (response) {
      $scope.freezer.push(response)
      $scope.TFREEZER = ''
      $scope.DFREEZER = ''
      $scope.url = ''
    }).error(function (data, status, headers, config) {
      console.log('error')
    })
  }
  $scope.openFreezerUpdate = function (id, index) {
    $('#openFreezerUpdate').openModal()
    $http.get('/freezer/' + id).then(function (response) {
      $scope.index = index
      $scope.updateTFREEZER = response.data.things
      $scope.updateDFREEZER = response.data.days
      $scope.updateURL = response.data.Url
    })
  }
  $scope.updateFreezer = function (updateDFREEZER) {
    $scope.freezer[$scope.index].things = $scope.updateTFREEZER
    if ($scope.freezer[$scope.index].days !== $scope.updateDFREEZER) {
      var now = new Date()
      var datePick = new Date(updateDFREEZER)
      var SUM = Math.ceil((datePick - now) / (1000 * 3600 * 24))
      $scope.freezer[$scope.index].days = SUM
      $scope.freezer[$scope.index].endDate = new Date(updateDFREEZER)
    }
    $scope.freezer[$scope.index].Url = $scope.updateURL
    $http.put('/freezer/' + $scope.freezer[$scope.index]['_id'], $scope.freezer[$scope.index]).then(function (res) {
      console.log(res.data)
      $scope.url = ''
    })
  }
  $scope.deleteFreezer = function (index) {
    $http.delete('/freezer/' + $scope.freezer[$scope.index]['_id']).then(function (res) {
      $scope.freezer.splice($scope.index, 1)
      console.log(res.data)
      // location.reload()
    })
  }
  $scope.countExpireFreezer = function (date) {
    var now = new Date()
    var datePick = new Date(date)
    var SUMFREEZER = Math.ceil((datePick - now) / (1000 * 3600 * 24))
    if (SUMFREEZER <= 0) {
      return (0)
    }else {
      return SUMFREEZER
    }
  }
  $scope.LEDAlert = function () {
    console.log($scope.state, $scope.stood, 'this')
    if ($scope.state === 1 && $scope.stood === 1) {
      $http.get('/ledAlertON').success(function (response) {
        console.log(response)
      })
    }else {
      $http.get('/ledAlertOFF').success(function (response) {
        console.log(response)
      })
    }
    // if ($scope.state === 0) {
    //   $http.get('/ledAlertOFF').success(function (response) {
    //     console.log(response)
    //   })
    // }if ($scope.state !== 0) {
    //   $http.get('/ledAlertON').success(function (response) {
    //     console.log(response)
    //   })
    // }
  }
  $scope.LEDAlert()
  $scope.order = [{item: 'Coke 220ml'}, {item: 'Milk 220ml'}, {item: 'Water 220ml'}]
  $scope.setupMail = function (M) {
    $http.post('/setupMail', M).success(function (response) {
      console.log(response)
    }).error(function (data, status, headers, config) {
      console.log('error')
    })
  }
  // FrontEnd Control RaspberryPi /////////////////////////////////////////////
  $scope.click = function () {
    console.log('Snapshot!')
    $http.get('/click').success(function (response) {
      $scope.data = response
      console.log(response)
      setTimeout(function () {
        window.location = 'index.html'
      }, 6000)
    }).error(function (data, status, headers, config) {
      console.log('error')
    })
  }

  // Flip FrontCamera/BackCamera /////////////////////
  $scope.flipStatus = false
  $scope.flip = function () {
    if ($scope.flipStatus === false) {
      $scope.flipStatus = true
      console.log($scope.flipStatus)
    } else {
      $scope.flipStatus = false
      console.log($scope.flipStatus)
    }
  }

  // Routing tabList tabFreezer tabTray ////////////
  $scope.tabList = true
  $scope.tabFreezer = false
  $scope.tabTray = false
  $scope.Tab = function (C) {
    if (C === 'L') {
      $scope.tabList = true
      $scope.tabFreezer = false
      $scope.tabTray = false
    }else if (C === 'F') {
      $scope.tabList = false
      $scope.tabFreezer = true
      $scope.tabTray = false
    }else if (C === 'D') {
      $scope.tabList = false
      $scope.tabFreezer = false
      $scope.tabTray = true
    }
  }
})
