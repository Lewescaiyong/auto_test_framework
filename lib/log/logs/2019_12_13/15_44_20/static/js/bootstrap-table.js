/**
 * bootstrap-table - An extended Bootstrap table with radio, checkbox, sort, pagination, and other added features. (supports twitter bootstrap v2 and v3).
 *
 * @version v1.13.5
 * @homepage https://bootstrap-table.com
 * @author wenzhixin <wenzhixin2010@gmail.com> (http://wenzhixin.net.cn/)
 * @license MIT
 */

(function (e, t) {
    if ('function' == typeof define && define.amd) define([], t); else if ('undefined' != typeof exports) t(); else {
        t(), e.bootstrapTable = {exports: {}}.exports
    }
})(this, function () {
    'use strict';

    function e(e, t) {
        if (!(e instanceof t)) throw new TypeError('Cannot call a class as a function')
    }

    function t(e) {
        if (Array.isArray(e)) {
            for (var t = 0, o = Array(e.length); t < e.length; t++) o[t] = e[t];
            return o
        }
        return Array.from(e)
    }

    var o = function () {
        function e(e, t) {
            for (var o, a = 0; a < t.length; a++) o = t[a], o.enumerable = o.enumerable || !1, o.configurable = !0, 'value' in o && (o.writable = !0), Object.defineProperty(e, o.key, o)
        }

        return function (t, o, i) {
            return o && e(t.prototype, o), i && e(t, i), t
        }
    }(), i = function () {
        function e(e, t) {
            var o = [], i = !0, a = !1, n = void 0;
            try {
                for (var s, l = e[Symbol.iterator](); !(i = (s = l.next()).done) && (o.push(s.value), !(t && o.length === t)); i = !0) ;
            } catch (e) {
                a = !0, n = e
            } finally {
                try {
                    !i && l['return'] && l['return']()
                } finally {
                    if (a) throw n
                }
            }
            return o
        }

        return function (t, o) {
            if (Array.isArray(t)) return t;
            if (Symbol.iterator in Object(t)) return e(t, o);
            throw new TypeError('Invalid attempt to destructure non-iterable instance')
        }
    }(), a = 'function' == typeof Symbol && 'symbol' == typeof Symbol.iterator ? function (e) {
        return typeof e
    } : function (e) {
        return e && 'function' == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? 'symbol' : typeof e
    };
    (function (n) {
        var s = 3;
        try {
            var g = n.fn.dropdown.Constructor.VERSION;
            g !== void 0 && (s = parseInt(g, 10))
        } catch (t) {
        }
        var l = {
            3: {
                iconsPrefix: 'glyphicon',
                icons: {
                    paginationSwitchDown: 'glyphicon-collapse-down icon-chevron-down',
                    paginationSwitchUp: 'glyphicon-collapse-up icon-chevron-up',
                    refresh: 'glyphicon-refresh icon-refresh',
                    toggleOff: 'glyphicon-list-alt icon-list-alt',
                    toggleOn: 'glyphicon-list-alt icon-list-alt',
                    columns: 'glyphicon-th icon-th',
                    detailOpen: 'glyphicon-plus icon-plus',
                    detailClose: 'glyphicon-minus icon-minus',
                    fullscreen: 'glyphicon-fullscreen'
                },
                classes: {buttons: 'default', pull: 'pull'},
                html: {
                    toobarDropdow: ['<ul class="dropdown-menu" role="menu">', '</ul>'],
                    toobarDropdowItem: '<li role="menuitem"><label>%s</label></li>',
                    pageDropdown: ['<ul class="dropdown-menu" role="menu">', '</ul>'],
                    pageDropdownItem: '<li role="menuitem" class="%s"><a href="#">%s</a></li>'
                }
            },
            4: {
                iconsPrefix: 'fa',
                icons: {
                    paginationSwitchDown: 'fa-caret-square-down',
                    paginationSwitchUp: 'fa-caret-square-up',
                    refresh: 'fa-sync',
                    toggleOff: 'fa-toggle-off',
                    toggleOn: 'fa-toggle-on',
                    columns: 'fa-th-list',
                    detailOpen: 'fa-plus',
                    detailClose: 'fa-minus',
                    fullscreen: 'fa-arrows-alt'
                },
                classes: {buttons: 'secondary', pull: 'float'},
                html: {
                    toobarDropdow: ['<div class="dropdown-menu dropdown-menu-right">', '</div>'],
                    toobarDropdowItem: '<label class="dropdown-item">%s</label>',
                    pageDropdown: ['<div class="dropdown-menu">', '</div>'],
                    pageDropdownItem: '<a class="dropdown-item %s" href="#">%s</a>'
                }
            }
        }[s], r = {
            bootstrapVersion: s, sprintf: function (e) {
                for (var t = arguments.length, o = Array(1 < t ? t - 1 : 0), a = 1; a < t; a++) o[a - 1] = arguments[a];
                var n = !0, s = 0, i = e.replace(/%s/g, function () {
                    var e = o[s++];
                    return 'undefined' == typeof e ? (n = !1, '') : e
                });
                return n ? i : ''
            }, getFieldTitle: function (e, t) {
                for (var o = e, i = Array.isArray(o), a = 0, _iterator = i ? o : o[Symbol.iterator](); ;) {
                    var n;
                    if (i) {
                        if (a >= o.length) break;
                        n = o[a++]
                    } else {
                        if (a = o.next(), a.done) break;
                        n = a.value
                    }
                    var s = n;
                    if (s.field === t) return s.title
                }
                return ''
            }, setFieldIndex: function (e) {
                for (var t = 0, o = [], a = e[0], n = Array.isArray(a), s = 0, _iterator2 = n ? a : a[Symbol.iterator](); ;) {
                    var l;
                    if (n) {
                        if (s >= a.length) break;
                        l = a[s++]
                    } else {
                        if (s = a.next(), s.done) break;
                        l = s.value
                    }
                    var d = l;
                    t += d.colspan || 1
                }
                for (var m = 0; m < e.length; m++) {
                    o[m] = [];
                    for (var i = 0; i < t; i++) o[m][i] = !1
                }
                for (var y = 0; y < e.length; y++) for (var p = e[y], c = Array.isArray(p), h = 0, _iterator3 = c ? p : p[Symbol.iterator](); ;) {
                    var g;
                    if (c) {
                        if (h >= p.length) break;
                        g = p[h++]
                    } else {
                        if (h = p.next(), h.done) break;
                        g = h.value
                    }
                    var u = g, r = u.rowspan || 1, f = u.colspan || 1, b = o[y].indexOf(!1);
                    1 === f && (u.fieldIndex = b, 'undefined' == typeof u.field && (u.field = b));
                    for (var w = 0; w < r; w++) o[y + w][b] = !0;
                    for (var k = 0; k < f; k++) o[y][b + k] = !0
                }
            }, getScrollBarWidth: function () {
                if (this.cachedWidth === void 0) {
                    var e = n('<div/>').addClass('fixed-table-scroll-inner'),
                        t = n('<div/>').addClass('fixed-table-scroll-outer');
                    t.append(e), n('body').append(t);
                    var o = e[0].offsetWidth;
                    t.css('overflow', 'scroll');
                    var i = e[0].offsetWidth;
                    o === i && (i = t[0].clientWidth), t.remove(), this.cachedWidth = o - i
                }
                return this.cachedWidth
            }, calculateObjectValue: function (e, o, i, n) {
                var s = o;
                if ('string' == typeof o) {
                    var h = o.split('.');
                    if (1 < h.length) {
                        s = window;
                        for (var l = h, r = Array.isArray(l), d = 0, _iterator4 = r ? l : l[Symbol.iterator](); ;) {
                            var p;
                            if (r) {
                                if (d >= l.length) break;
                                p = l[d++]
                            } else {
                                if (d = l.next(), d.done) break;
                                p = d.value
                            }
                            var c = p;
                            s = s[c]
                        }
                    } else s = window[o]
                }
                return null !== s && 'object' === ('undefined' == typeof s ? 'undefined' : a(s)) ? s : 'function' == typeof s ? s.apply(e, i || []) : !s && 'string' == typeof o && this.sprintf.apply(this, [o].concat(t(i))) ? this.sprintf.apply(this, [o].concat(t(i))) : n
            }, compareObjects: function (e, t, o) {
                var i = Object.keys(e), a = Object.keys(t);
                if (o && i.length !== a.length) return !1;
                for (var n = i, s = Array.isArray(n), l = 0, _iterator5 = s ? n : n[Symbol.iterator](); ;) {
                    var r;
                    if (s) {
                        if (l >= n.length) break;
                        r = n[l++]
                    } else {
                        if (l = n.next(), l.done) break;
                        r = l.value
                    }
                    var d = r;
                    if (-1 !== a.indexOf(d) && e[d] !== t[d]) return !1
                }
                return !0
            }, escapeHTML: function (e) {
                return 'string' == typeof e ? e.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#039;').replace(/`/g, '&#x60;') : e
            }, getRealDataAttr: function (e) {
                for (var t = function (e) {
                    return Object.keys(e).map(function (t) {
                        return [t, e[t]]
                    })
                }(e), o = Array.isArray(t), a = 0, _iterator6 = o ? t : t[Symbol.iterator](); ;) {
                    var n;
                    if (o) {
                        if (a >= t.length) break;
                        n = t[a++]
                    } else {
                        if (a = t.next(), a.done) break;
                        n = a.value
                    }
                    var s = n, l = i(s, 2), r = l[0], d = l[1], p = r.split(/(?=[A-Z])/).join('-').toLowerCase();
                    p !== r && (e[p] = d, delete e[r])
                }
                return e
            }, getItemField: function (e, t, o) {
                var i = e;
                if ('string' != typeof t || e.hasOwnProperty(t)) return o ? this.escapeHTML(e[t]) : e[t];
                for (var a = t.split('.'), n = a, s = Array.isArray(n), l = 0, _iterator7 = s ? n : n[Symbol.iterator](); ;) {
                    var r;
                    if (s) {
                        if (l >= n.length) break;
                        r = n[l++]
                    } else {
                        if (l = n.next(), l.done) break;
                        r = l.value
                    }
                    var d = r;
                    i = i && i[d]
                }
                return o ? this.escapeHTML(i) : i
            }, isIEBrowser: function () {
                return -1 !== navigator.userAgent.indexOf('MSIE ') || /Trident.*rv:11\./.test(navigator.userAgent)
            }, findIndex: function (e, t) {
                for (var o = e, i = Array.isArray(o), a = 0, _iterator8 = i ? o : o[Symbol.iterator](); ;) {
                    var n;
                    if (i) {
                        if (a >= o.length) break;
                        n = o[a++]
                    } else {
                        if (a = o.next(), a.done) break;
                        n = a.value
                    }
                    var s = n;
                    if (JSON.stringify(s) === JSON.stringify(t)) return e.indexOf(s)
                }
                return -1
            }
        }, d = {
            height: void 0,
            classes: 'table table-bordered table-hover',
            theadClasses: '',
            rowStyle: function () {
                return {}
            },
            rowAttributes: function () {
                return {}
            },
            undefinedText: '-',
            locale: void 0,
            sortable: !0,
            sortClass: void 0,
            silentSort: !0,
            sortName: void 0,
            sortOrder: 'asc',
            sortStable: !1,
            rememberOrder: !1,
            customSort: void 0,
            columns: [[]],
            data: [],
            url: void 0,
            method: 'get',
            cache: !0,
            contentType: 'application/json',
            dataType: 'json',
            ajax: void 0,
            ajaxOptions: {},
            queryParams: function (e) {
                return e
            },
            queryParamsType: 'limit',
            responseHandler: function (e) {
                return e
            },
            totalField: 'total',
            dataField: 'rows',
            pagination: !1,
            onlyInfoPagination: !1,
            paginationLoop: !0,
            sidePagination: 'client',
            totalRows: 0,
            pageNumber: 1,
            pageSize: 10,
            pageList: [10, 25, 50, 100],
            paginationHAlign: 'right',
            paginationVAlign: 'bottom',
            paginationDetailHAlign: 'left',
            paginationPreText: '&lsaquo;',
            paginationNextText: '&rsaquo;',
            paginationSuccessivelySize: 5,
            paginationPagesBySide: 1,
            paginationUseIntermediate: !1,
            search: !1,
            searchOnEnterKey: !1,
            strictSearch: !1,
            trimOnSearch: !0,
            searchAlign: 'right',
            searchTimeOut: 500,
            searchText: '',
            customSearch: void 0,
            showHeader: !0,
            showFooter: !1,
            footerStyle: function () {
                return {}
            },
            showColumns: !1,
            minimumCountColumns: 1,
            showPaginationSwitch: !1,
            showRefresh: !1,
            showToggle: !1,
            showFullscreen: !1,
            smartDisplay: !0,
            escape: !1,
            idField: void 0,
            uniqueId: void 0,
            cardView: !1,
            detailView: !1,
            detailFormatter: function () {
                return ''
            },
            detailFilter: function () {
                return !0
            },
            selectItemName: 'btSelectItem',
            clickToSelect: !1,
            ignoreClickToSelectOn: function (e) {
                var t = e.tagName;
                return -1 !== ['A', 'BUTTON'].indexOf(t)
            },
            singleSelect: !1,
            checkboxHeader: !0,
            maintainSelected: !1,
            toolbar: void 0,
            toolbarAlign: 'left',
            buttonsToolbar: void 0,
            buttonsAlign: 'right',
            buttonsClass: l.classes.buttons,
            icons: l.icons,
            iconSize: void 0,
            iconsPrefix: l.iconsPrefix,
            onAll: function () {
                return !1
            },
            onClickCell: function () {
                return !1
            },
            onDblClickCell: function () {
                return !1
            },
            onClickRow: function () {
                return !1
            },
            onDblClickRow: function () {
                return !1
            },
            onSort: function () {
                return !1
            },
            onCheck: function () {
                return !1
            },
            onUncheck: function () {
                return !1
            },
            onCheckAll: function () {
                return !1
            },
            onUncheckAll: function () {
                return !1
            },
            onCheckSome: function () {
                return !1
            },
            onUncheckSome: function () {
                return !1
            },
            onLoadSuccess: function () {
                return !1
            },
            onLoadError: function () {
                return !1
            },
            onColumnSwitch: function () {
                return !1
            },
            onPageChange: function () {
                return !1
            },
            onSearch: function () {
                return !1
            },
            onToggle: function () {
                return !1
            },
            onPreBody: function () {
                return !1
            },
            onPostBody: function () {
                return !1
            },
            onPostHeader: function () {
                return !1
            },
            onExpandRow: function () {
                return !1
            },
            onCollapseRow: function () {
                return !1
            },
            onRefreshOptions: function () {
                return !1
            },
            onRefresh: function () {
                return !1
            },
            onResetView: function () {
                return !1
            },
            onScrollBody: function () {
                return !1
            }
        }, p = {};
        p['en-US'] = p.en = {
            formatLoadingMessage: function () {
                return 'Loading, please wait...'
            }, formatRecordsPerPage: function (e) {
                return r.sprintf('%s rows per page', e)
            }, formatShowingRows: function (e, t, o) {
                return r.sprintf('Showing %s to %s of %s rows', e, t, o)
            }, formatDetailPagination: function (e) {
                return r.sprintf('Showing %s rows', e)
            }, formatSearch: function () {
                return 'Search'
            }, formatNoMatches: function () {
                return 'No matching records found'
            }, formatPaginationSwitch: function () {
                return 'Hide/Show pagination'
            }, formatRefresh: function () {
                return 'Refresh'
            }, formatToggle: function () {
                return 'Toggle'
            }, formatFullscreen: function () {
                return 'Fullscreen'
            }, formatColumns: function () {
                return 'Columns'
            }, formatAllRows: function () {
                return 'All'
            }
        }, n.extend(d, p['en-US']);
        var c = function () {
            function t(o, i) {
                e(this, t), this.options = i, this.$el = n(o), this.$el_ = this.$el.clone(), this.timeoutId_ = 0, this.timeoutFooter_ = 0, this.init()
            }

            return o(t, [{
                key: 'init', value: function () {
                    this.initLocale(), this.initContainer(), this.initTable(), this.initHeader(), this.initData(), this.initHiddenRows(), this.initFooter(), this.initToolbar(), this.initPagination(), this.initBody(), this.initSearchText(), this.initServer()
                }
            }, {
                key: 'initLocale', value: function () {
                    if (this.options.locale) {
                        var e = n.fn.bootstrapTable.locales, t = this.options.locale.split(/-|_/);
                        t[0] = t[0].toLowerCase(), t[1] && (t[1] = t[1].toUpperCase()), e[this.options.locale] ? n.extend(this.options, e[this.options.locale]) : e[t.join('-')] ? n.extend(this.options, e[t.join('-')]) : e[t[0]] && n.extend(this.options, e[t[0]])
                    }
                }
            }, {
                key: 'initContainer', value: function () {
                    var e = -1 === ['top', 'both'].indexOf(this.options.paginationVAlign) ? '' : '<div class="fixed-table-pagination clearfix"></div>',
                        t = -1 === ['bottom', 'both'].indexOf(this.options.paginationVAlign) ? '' : '<div class="fixed-table-pagination"></div>';
                    this.$container = n('\n        <div class="bootstrap-table">\n        <div class="fixed-table-toolbar"></div>\n        ' + e + '\n        <div class="fixed-table-container">\n        <div class="fixed-table-header"><table></table></div>\n        <div class="fixed-table-body">\n        <div class="fixed-table-loading">\n        ' + this.options.formatLoadingMessage() + '\n        </div>\n        </div>\n        <div class="fixed-table-footer"><table><thead><tr></tr></thead></table></div>\n        </div>\n        ' + t + '\n        </div>\n      '), this.$container.insertAfter(this.$el), this.$tableContainer = this.$container.find('.fixed-table-container'), this.$tableHeader = this.$container.find('.fixed-table-header'), this.$tableBody = this.$container.find('.fixed-table-body'), this.$tableLoading = this.$container.find('.fixed-table-loading'), this.$tableFooter = this.$container.find('.fixed-table-footer'), this.$toolbar = this.options.buttonsToolbar ? n('body').find(this.options.buttonsToolbar) : this.$container.find('.fixed-table-toolbar'), this.$pagination = this.$container.find('.fixed-table-pagination'), this.$tableBody.append(this.$el), this.$container.after('<div class="clearfix"></div>'), this.$el.addClass(this.options.classes), this.options.height && (this.$tableContainer.addClass('fixed-height'), this.options.showFooter && this.$tableContainer.addClass('has-footer'), -1 !== this.options.classes.split(' ').indexOf('table-bordered') && (this.$tableBody.append('<div class="fixed-table-border"></div>'), this.$tableBorder = this.$tableBody.find('.fixed-table-border'), this.$tableLoading.addClass('fixed-table-border')))
                }
            }, {
                key: 'initTable', value: function () {
                    var e = this, o = [], i = [];
                    if (this.$header = this.$el.find('>thead'), this.$header.length ? this.options.theadClasses && this.$header.addClass(this.options.theadClasses) : this.$header = n('<thead class="' + this.options.theadClasses + '"></thead>').appendTo(this.$el), this.$header.find('tr').each(function (e, t) {
                        var a = [];
                        n(t).find('th').each(function (e, t) {
                            'undefined' != typeof n(t).data('field') && n(t).data('field', '' + n(t).data('field')), a.push(n.extend({}, {
                                title: n(t).html(),
                                class: n(t).attr('class'),
                                titleTooltip: n(t).attr('title'),
                                rowspan: n(t).attr('rowspan') ? +n(t).attr('rowspan') : void 0,
                                colspan: n(t).attr('colspan') ? +n(t).attr('colspan') : void 0
                            }, n(t).data()))
                        }), o.push(a)
                    }), Array.isArray(this.options.columns[0]) || (this.options.columns = [this.options.columns]), this.options.columns = n.extend(!0, [], o, this.options.columns), this.columns = [], this.fieldsColumnsIndex = [], r.setFieldIndex(this.options.columns), this.options.columns.forEach(function (o, a) {
                        o.forEach(function (o, i) {
                            var s = n.extend({}, t.COLUMN_DEFAULTS, o);
                            'undefined' != typeof s.fieldIndex && (e.columns[s.fieldIndex] = s, e.fieldsColumnsIndex[s.field] = s.fieldIndex), e.options.columns[a][i] = s
                        })
                    }), !this.options.data.length) {
                        var a = [];
                        this.$el.find('>tbody>tr').each(function (t, o) {
                            var s = {};
                            s._id = n(o).attr('id'), s._class = n(o).attr('class'), s._data = r.getRealDataAttr(n(o).data()), n(o).find('>td').each(function (o, i) {
                                for (var l = +n(i).attr('colspan') || 1, d = +n(i).attr('rowspan') || 1, p = o; a[t] && a[t][p]; p++) ;
                                for (var h = p; h < p + l; h++) for (var g = t; g < t + d; g++) a[g] || (a[g] = []), a[g][h] = !0;
                                var c = e.columns[p].field;
                                s[c] = n(i).html().trim(), s['_' + c + '_id'] = n(i).attr('id'), s['_' + c + '_class'] = n(i).attr('class'), s['_' + c + '_rowspan'] = n(i).attr('rowspan'), s['_' + c + '_colspan'] = n(i).attr('colspan'), s['_' + c + '_title'] = n(i).attr('title'), s['_' + c + '_data'] = r.getRealDataAttr(n(i).data())
                            }), i.push(s)
                        }), this.options.data = i, i.length && (this.fromHtml = !0)
                    }
                }
            }, {
                key: 'initHeader', value: function () {
                    var t = this, e = {}, o = [];
                    this.header = {
                        fields: [],
                        styles: [],
                        classes: [],
                        formatters: [],
                        events: [],
                        sorters: [],
                        sortNames: [],
                        cellStyles: [],
                        searchables: []
                    }, this.options.columns.forEach(function (a, n) {
                        o.push('<tr>'), 0 === n && !t.options.cardView && t.options.detailView && o.push('<th class="detail" rowspan="' + t.options.columns.length + '">\n            <div class="fht-cell"></div>\n            </th>\n          '), a.forEach(function (i, a) {
                            var s = '', l = '', d = '', p = '', c = r.sprintf(' class="%s"', i['class']), h = 'px',
                                g = i.width;
                            if (void 0 === i.width || t.options.cardView || 'string' != typeof i.width || -1 === i.width.indexOf('%') || (h = '%'), i.width && 'string' == typeof i.width && (g = i.width.replace('%', '').replace('px', '')), l = r.sprintf('text-align: %s; ', i.halign ? i.halign : i.align), d = r.sprintf('text-align: %s; ', i.align), p = r.sprintf('vertical-align: %s; ', i.valign), p += r.sprintf('width: %s; ', (i.checkbox || i.radio) && !g ? i.showSelectTitle ? void 0 : '36px' : g ? g + h : void 0), 'undefined' != typeof i.fieldIndex) {
                                if (t.header.fields[i.fieldIndex] = i.field, t.header.styles[i.fieldIndex] = d + p, t.header.classes[i.fieldIndex] = c, t.header.formatters[i.fieldIndex] = i.formatter, t.header.events[i.fieldIndex] = i.events, t.header.sorters[i.fieldIndex] = i.sorter, t.header.sortNames[i.fieldIndex] = i.sortName, t.header.cellStyles[i.fieldIndex] = i.cellStyle, t.header.searchables[i.fieldIndex] = i.searchable, !i.visible) return;
                                if (t.options.cardView && !i.cardVisible) return;
                                e[i.field] = i
                            }
                            o.push('<th' + r.sprintf(' title="%s"', i.titleTooltip), i.checkbox || i.radio ? r.sprintf(' class="bs-checkbox %s"', i['class'] || '') : c, r.sprintf(' style="%s"', l + p), r.sprintf(' rowspan="%s"', i.rowspan), r.sprintf(' colspan="%s"', i.colspan), r.sprintf(' data-field="%s"', i.field), 0 === a && 0 < n ? ' data-not-first-th' : '', '>'), o.push(r.sprintf('<div class="th-inner %s">', t.options.sortable && i.sortable ? 'sortable both' : '')), s = t.options.escape ? r.escapeHTML(i.title) : i.title;
                            var u = s;
                            i.checkbox && (s = '', !t.options.singleSelect && t.options.checkboxHeader && (s = '<input name="btSelectAll" type="checkbox" />'), t.header.stateField = i.field), i.radio && (s = '', t.header.stateField = i.field, t.options.singleSelect = !0), !s && i.showSelectTitle && (s += u), o.push(s), o.push('</div>'), o.push('<div class="fht-cell"></div>'), o.push('</div>'), o.push('</th>')
                        }), o.push('</tr>')
                    }), this.$header.html(o.join('')), this.$header.find('th[data-field]').each(function (t, o) {
                        n(o).data(e[n(o).data('field')])
                    }), this.$container.off('click', '.th-inner').on('click', '.th-inner', function (o) {
                        var e = n(o.currentTarget);
                        return t.options.detailView && !e.parent().hasClass('bs-checkbox') && e.closest('.bootstrap-table')[0] !== t.$container[0] ? !1 : void(t.options.sortable && e.parent().data().sortable && t.onSort(o))
                    }), this.$header.children().children().off('keypress').on('keypress', function (o) {
                        if (t.options.sortable && n(o.currentTarget).data().sortable) {
                            var e = o.keyCode || o.which;
                            13 === e && t.onSort(o)
                        }
                    }), n(window).off('resize.bootstrap-table'), !this.options.showHeader || this.options.cardView ? (this.$header.hide(), this.$tableHeader.hide(), this.$tableLoading.css('top', 0)) : (this.$header.show(), this.$tableHeader.show(), this.$tableLoading.css('top', this.$header.outerHeight() + 1), this.getCaret(), n(window).on('resize.bootstrap-table', n.proxy(this.resetWidth, this))), this.$selectAll = this.$header.find('[name="btSelectAll"]'), this.$selectAll.off('click').on('click', function (e) {
                        var o = e.currentTarget, i = n(o).prop('checked');
                        t[i ? 'checkAll' : 'uncheckAll'](), t.updateSelected()
                    })
                }
            }, {
                key: 'initFooter', value: function () {
                    !this.options.showFooter || this.options.cardView ? this.$tableFooter.hide() : this.$tableFooter.show()
                }
            }, {
                key: 'initData', value: function (e, t) {
                    this.options.data = 'append' === t ? this.options.data.concat(e) : 'prepend' === t ? [].concat(e).concat(this.options.data) : e || this.options.data, this.data = this.options.data, 'server' === this.options.sidePagination || this.initSort()
                }
            }, {
                key: 'initSort', value: function () {
                    var e = this, t = this.options.sortName, o = 'desc' === this.options.sortOrder ? -1 : 1,
                        i = this.header.fields.indexOf(this.options.sortName), a = 0;
                    -1 !== i && (this.options.sortStable && this.data.forEach(function (e, t) {
                        e.hasOwnProperty('_position') || (e._position = t)
                    }), this.options.customSort ? r.calculateObjectValue(this.options, this.options.customSort, [this.options.sortName, this.options.sortOrder, this.data]) : this.data.sort(function (s, a) {
                        e.header.sortNames[i] && (t = e.header.sortNames[i]);
                        var l = r.getItemField(s, t, e.options.escape), d = r.getItemField(a, t, e.options.escape),
                            p = r.calculateObjectValue(e.header, e.header.sorters[i], [l, d, s, a]);
                        return void 0 === p ? ((void 0 === l || null === l) && (l = ''), (void 0 === d || null === d) && (d = ''), e.options.sortStable && l === d && (l = s._position, d = a._position), n.isNumeric(l) && n.isNumeric(d)) ? (l = parseFloat(l), d = parseFloat(d), l < d ? -1 * o : l > d ? o : 0) : l === d ? 0 : ('string' != typeof l && (l = l.toString()), -1 === l.localeCompare(d) ? -1 * o : o) : e.options.sortStable && 0 === p ? o * (s._position - a._position) : o * p
                    }), void 0 !== this.options.sortClass && (clearTimeout(a), a = setTimeout(function () {
                        e.$el.removeClass(e.options.sortClass);
                        var t = e.$header.find('[data-field="' + e.options.sortName + '"]').index();
                        e.$el.find('tr td:nth-child(' + (t + 1) + ')').addClass(e.options.sortClass)
                    }, 250)))
                }
            }, {
                key: 'onSort', value: function (e) {
                    var t = e.type, o = e.currentTarget, i = 'keypress' === t ? n(o) : n(o).parent(),
                        a = this.$header.find('th').eq(i.index());
                    return this.$header.add(this.$header_).find('span.order').remove(), this.options.sortName === i.data('field') ? this.options.sortOrder = 'asc' === this.options.sortOrder ? 'desc' : 'asc' : (this.options.sortName = i.data('field'), this.options.sortOrder = this.options.rememberOrder ? 'asc' === i.data('order') ? 'desc' : 'asc' : this.columns[this.fieldsColumnsIndex[i.data('field')]].order), this.trigger('sort', this.options.sortName, this.options.sortOrder), i.add(a).data('order', this.options.sortOrder), this.getCaret(), 'server' === this.options.sidePagination ? void this.initServer(this.options.silentSort) : void(this.initSort(), this.initBody())
                }
            }, {
                key: 'initToolbar', value: function () {
                    var e = this, t = [], o = 0, i = void 0, s = void 0, d = 0;
                    this.$toolbar.find('.bs-bars').children().length && n('body').append(n(this.options.toolbar)), this.$toolbar.html(''), ('string' == typeof this.options.toolbar || 'object' === a(this.options.toolbar)) && n(r.sprintf('<div class="bs-bars %s-%s"></div>', l.classes.pull, this.options.toolbarAlign)).appendTo(this.$toolbar).append(n(this.options.toolbar)), t = [r.sprintf('<div class="columns columns-%s btn-group %s-%s">', this.options.buttonsAlign, l.classes.pull, this.options.buttonsAlign)], 'string' == typeof this.options.icons && (this.options.icons = r.calculateObjectValue(null, this.options.icons)), this.options.showPaginationSwitch && t.push(r.sprintf('<button class="btn' + r.sprintf(' btn-%s', this.options.buttonsClass) + r.sprintf(' btn-%s', this.options.iconSize) + '" type="button" name="paginationSwitch" aria-label="pagination Switch" title="%s">', this.options.formatPaginationSwitch()), r.sprintf('<i class="%s %s"></i>', this.options.iconsPrefix, this.options.icons.paginationSwitchDown), '</button>'), this.options.showRefresh && t.push(r.sprintf('<button class="btn' + r.sprintf(' btn-%s', this.options.buttonsClass) + r.sprintf(' btn-%s', this.options.iconSize) + '" type="button" name="refresh" aria-label="refresh" title="%s">', this.options.formatRefresh()), r.sprintf('<i class="%s %s"></i>', this.options.iconsPrefix, this.options.icons.refresh), '</button>'), this.options.showToggle && t.push(r.sprintf('<button class="btn' + r.sprintf(' btn-%s', this.options.buttonsClass) + r.sprintf(' btn-%s', this.options.iconSize) + '" type="button" name="toggle" aria-label="toggle" title="%s">', this.options.formatToggle()), r.sprintf('<i class="%s %s"></i>', this.options.iconsPrefix, this.options.icons.toggleOff), '</button>'), this.options.showFullscreen && t.push(r.sprintf('<button class="btn' + r.sprintf(' btn-%s', this.options.buttonsClass) + r.sprintf(' btn-%s', this.options.iconSize) + '" type="button" name="fullscreen" aria-label="fullscreen" title="%s">', this.options.formatFullscreen()), r.sprintf('<i class="%s %s"></i>', this.options.iconsPrefix, this.options.icons.fullscreen), '</button>'), this.options.showColumns && (t.push(r.sprintf('<div class="keep-open btn-group" title="%s">', this.options.formatColumns()), '<button type="button" aria-label="columns" class="btn' + r.sprintf(' btn-%s', this.options.buttonsClass) + r.sprintf(' btn-%s', this.options.iconSize) + ' dropdown-toggle" data-toggle="dropdown">', r.sprintf('<i class="%s %s"></i>', this.options.iconsPrefix, this.options.icons.columns), ' <span class="caret"></span>', '</button>', l.html.toobarDropdow[0]), this.columns.forEach(function (o, a) {
                        if (!(o.radio || o.checkbox) && (!e.options.cardView || o.cardVisible)) {
                            var i = o.visible ? ' checked="checked"' : '';
                            o.switchable && (t.push(r.sprintf(l.html.toobarDropdowItem, r.sprintf('<input type="checkbox" data-field="%s" value="%s"%s> %s', o.field, a, i, o.title))), d++)
                        }
                    }), t.push(l.html.toobarDropdow[1], '</div>')), t.push('</div>'), (this.showToolbar || 2 < t.length) && this.$toolbar.append(t.join('')), this.options.showPaginationSwitch && this.$toolbar.find('button[name="paginationSwitch"]').off('click').on('click', n.proxy(this.togglePagination, this)), this.options.showFullscreen && this.$toolbar.find('button[name="fullscreen"]').off('click').on('click', n.proxy(this.toggleFullscreen, this)), this.options.showRefresh && this.$toolbar.find('button[name="refresh"]').off('click').on('click', n.proxy(this.refresh, this)), this.options.showToggle && this.$toolbar.find('button[name="toggle"]').off('click').on('click', function () {
                        e.toggleView()
                    }), this.options.showColumns && (i = this.$toolbar.find('.keep-open'), d <= this.options.minimumCountColumns && i.find('input').prop('disabled', !0), i.find('li').off('click').on('click', function (t) {
                        t.stopImmediatePropagation()
                    }), i.find('input').off('click').on('click', function (t) {
                        var o = t.currentTarget, i = n(o);
                        e.toggleColumn(i.val(), i.prop('checked'), !1), e.trigger('column-switch', i.data('field'), i.prop('checked'))
                    })), this.options.search && (t = [], t.push(r.sprintf('<div class="%s-%s search">', l.classes.pull, this.options.searchAlign), r.sprintf('<input class="form-control' + r.sprintf(' input-%s', this.options.iconSize) + '" type="text" placeholder="%s">', this.options.formatSearch()), '</div>'), this.$toolbar.append(t.join('')), s = this.$toolbar.find('.search input'), s.off('keyup drop blur').on('keyup drop blur', function (t) {
                        e.options.searchOnEnterKey && 13 !== t.keyCode || -1 !== [37, 38, 39, 40].indexOf(t.keyCode) || (clearTimeout(o), o = setTimeout(function () {
                            e.onSearch(t)
                        }, e.options.searchTimeOut))
                    }), r.isIEBrowser() && s.off('mouseup').on('mouseup', function (t) {
                        clearTimeout(o), o = setTimeout(function () {
                            e.onSearch(t)
                        }, e.options.searchTimeOut)
                    }))
                }
            }, {
                key: 'onSearch', value: function (e) {
                    var t = e.currentTarget, o = e.firedByInitSearchText, i = n.trim(n(t).val());
                    this.options.trimOnSearch && n(t).val() !== i && n(t).val(i), i === this.searchText || (this.searchText = i, this.options.searchText = i, !o && (this.options.pageNumber = 1), this.initSearch(), o ? 'client' === this.options.sidePagination && this.updatePagination() : this.updatePagination(), this.trigger('search', i))
                }
            }, {
                key: 'initSearch', value: function () {
                    var e = this;
                    if ('server' !== this.options.sidePagination) {
                        if (this.options.customSearch) return void(this.data = r.calculateObjectValue(this.options, this.options.customSearch, [this.options.data, this.searchText]));
                        var t = this.searchText && (this.options.escape ? r.escapeHTML(this.searchText) : this.searchText).toLowerCase(),
                            o = n.isEmptyObject(this.filterColumns) ? null : this.filterColumns;
                        this.data = o ? this.options.data.filter(function (e) {
                            for (var t in o) if (Array.isArray(o[t]) && -1 === o[t].indexOf(e[t]) || !Array.isArray(o[t]) && e[t] !== o[t]) return !1;
                            return !0
                        }) : this.options.data, this.data = t ? this.data.filter(function (o, a) {
                            for (var c = 0; c < e.header.fields.length; c++) if (e.header.searchables[c]) {
                                var i = n.isNumeric(e.header.fields[c]) ? parseInt(e.header.fields[c], 10) : e.header.fields[c],
                                    s = e.columns[e.fieldsColumnsIndex[i]], l = void 0;
                                if ('string' == typeof i) {
                                    l = o;
                                    for (var d = i.split('.'), p = 0; p < d.length; p++) null !== l[d[p]] && (l = l[d[p]])
                                } else l = o[i];
                                if (s && s.searchFormatter && (l = r.calculateObjectValue(s, e.header.formatters[c], [l, o, a], l)), 'string' == typeof l || 'number' == typeof l) if (e.options.strictSearch) {
                                    if (('' + l).toLowerCase() === t) return !0;
                                } else if (-1 !== ('' + l).toLowerCase().indexOf(t)) return !0
                            }
                            return !1
                        }) : this.data
                    }
                }
            }, {
                key: 'initPagination', value: function () {
                    var e = Math.round, t = this;
                    if (!this.options.pagination) return void this.$pagination.hide();
                    this.$pagination.show();
                    var o = [], a = !1, s = void 0, i = void 0, d = void 0, p = void 0, c = void 0, h = void 0,
                        g = void 0, u = this.getData(), f = this.options.pageList;
                    if ('server' !== this.options.sidePagination && (this.options.totalRows = u.length), this.totalPages = 0, this.options.totalRows) {
                        if (this.options.pageSize === this.options.formatAllRows()) this.options.pageSize = this.options.totalRows, a = !0; else if (this.options.pageSize === this.options.totalRows) {
                            var S = 'string' == typeof this.options.pageList ? this.options.pageList.replace('[', '').replace(']', '').replace(/ /g, '').toLowerCase().split(',') : this.options.pageList;
                            -1 !== S.indexOf(this.options.formatAllRows().toLowerCase()) && (a = !0)
                        }
                        this.totalPages = ~~((this.options.totalRows - 1) / this.options.pageSize) + 1, this.options.totalPages = this.totalPages
                    }
                    if (0 < this.totalPages && this.options.pageNumber > this.totalPages && (this.options.pageNumber = this.totalPages), this.pageFrom = (this.options.pageNumber - 1) * this.options.pageSize + 1, this.pageTo = this.options.pageNumber * this.options.pageSize, this.pageTo > this.options.totalRows && (this.pageTo = this.options.totalRows), o.push(r.sprintf('<div class="%s-%s pagination-detail">', l.classes.pull, this.options.paginationDetailHAlign), '<span class="pagination-info">', this.options.onlyInfoPagination ? this.options.formatDetailPagination(this.options.totalRows) : this.options.formatShowingRows(this.pageFrom, this.pageTo, this.options.totalRows), '</span>'), !this.options.onlyInfoPagination) {
                        o.push('<span class="page-list">');
                        var $ = [r.sprintf('<span class="btn-group %s">', 'top' === this.options.paginationVAlign || 'both' === this.options.paginationVAlign ? 'dropdown' : 'dropup'), '<button type="button" class="btn' + r.sprintf(' btn-%s', this.options.buttonsClass) + r.sprintf(' btn-%s', this.options.iconSize) + ' dropdown-toggle" data-toggle="dropdown">', '<span class="page-size">', a ? this.options.formatAllRows() : this.options.pageSize, '</span>', ' <span class="caret"></span>', '</button>', l.html.pageDropdown[0]];
                        if ('string' == typeof this.options.pageList) {
                            var P = this.options.pageList.replace('[', '').replace(']', '').replace(/ /g, '').split(',');
                            f = [];
                            for (var b = P, m = Array.isArray(b), y = 0, _iterator9 = m ? b : b[Symbol.iterator](); ;) {
                                var w;
                                if (m) {
                                    if (y >= b.length) break;
                                    w = b[y++]
                                } else {
                                    if (y = b.next(), y.done) break;
                                    w = y.value
                                }
                                var k = w;
                                f.push(k.toUpperCase() === this.options.formatAllRows().toUpperCase() || 'UNLIMITED' === k.toUpperCase() ? this.options.formatAllRows() : +k)
                            }
                        }
                        f.forEach(function (e, o) {
                            if (!t.options.smartDisplay || 0 === o || f[o - 1] < t.options.totalRows) {
                                var i;
                                i = a ? e === t.options.formatAllRows() ? 'active' : '' : e === t.options.pageSize ? 'active' : '', $.push(r.sprintf(l.html.pageDropdownItem, i, e))
                            }
                        }), $.push(l.html.pageDropdown[1] + '</span>'), o.push(this.options.formatRecordsPerPage($.join(''))), o.push('</span>'), o.push('</div>', r.sprintf('<div class="%s-%s pagination">', l.classes.pull, this.options.paginationHAlign), '<ul class="pagination' + r.sprintf(' pagination-%s', this.options.iconSize) + '">', r.sprintf('<li class="page-item page-pre"><a class="page-link" href="#">%s</a></li>', this.options.paginationPreText)), this.totalPages < this.options.paginationSuccessivelySize ? (i = 1, d = this.totalPages) : (i = this.options.pageNumber - this.options.paginationPagesBySide, d = i + 2 * this.options.paginationPagesBySide), this.options.pageNumber < this.options.paginationSuccessivelySize - 1 && (d = this.options.paginationSuccessivelySize), d > this.totalPages && (d = this.totalPages), this.options.paginationSuccessivelySize > this.totalPages - i && (i = i - (this.options.paginationSuccessivelySize - (this.totalPages - i)) + 1), 1 > i && (i = 1), d > this.totalPages && (d = this.totalPages);
                        var v = e(this.options.paginationPagesBySide / 2), x = function (e) {
                            var o = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : '';
                            return '\n          <li class="page-item' + o + (e === t.options.pageNumber ? ' active' : '') + '">\n            <a class="page-link" href="#">' + e + '</a>\n          </li>\n        '
                        };
                        if (1 < i) {
                            var C = this.options.paginationPagesBySide;
                            for (C >= i && (C = i - 1), s = 1; s <= C; s++) o.push(x(s));
                            i - 1 === C + 1 ? (s = i - 1, o.push(x(s))) : i - 1 > C && (i - 2 * this.options.paginationPagesBySide > this.options.paginationPagesBySide && this.options.paginationUseIntermediate ? (s = e((i - v) / 2 + v), o.push(x(s, ' page-intermediate'))) : o.push('\n                  <li class="page-item page-first-separator disabled">\n                    <a class="page-link" href="#">...</a>\n                  </li>'))
                        }
                        for (s = i; s <= d; s++) o.push(x(s));
                        if (this.totalPages > d) {
                            var T = this.totalPages - (this.options.paginationPagesBySide - 1);
                            for (d >= T && (T = d + 1), d + 1 === T - 1 ? (s = d + 1, o.push(x(s))) : T > d + 1 && (this.totalPages - d > 2 * this.options.paginationPagesBySide && this.options.paginationUseIntermediate ? (s = e((this.totalPages - v - d) / 2 + d), o.push(x(s, ' page-intermediate'))) : o.push('\n                  <li class="page-item page-last-separator disabled">\n                    <a class="page-link" href="#">...</a>\n                  </li>')), s = T; s <= this.totalPages; s++) o.push(x(s))
                        }
                        o.push('\n          <li class="page-item page-next">\n          <a class="page-link" href="#">' + this.options.paginationNextText + '</a>\n          </li>\n          </ul>\n          </div>\n        ')
                    }
                    this.$pagination.html(o.join('')), this.options.onlyInfoPagination || (p = this.$pagination.find('.page-list a'), c = this.$pagination.find('.page-pre'), h = this.$pagination.find('.page-next'), g = this.$pagination.find('.page-item').not('.page-next, .page-pre'), this.options.smartDisplay && (1 >= this.totalPages && this.$pagination.find('div.pagination').hide(), (2 > f.length || this.options.totalRows <= f[0]) && this.$pagination.find('span.page-list').hide(), this.$pagination[this.getData().length ? 'show' : 'hide']()), !this.options.paginationLoop && (1 === this.options.pageNumber && c.addClass('disabled'), this.options.pageNumber === this.totalPages && h.addClass('disabled')), a && (this.options.pageSize = this.options.formatAllRows()), p.off('click').on('click', n.proxy(this.onPageListChange, this)), c.off('click').on('click', n.proxy(this.onPagePre, this)), h.off('click').on('click', n.proxy(this.onPageNext, this)), g.off('click').on('click', n.proxy(this.onPageNumber, this)))
                }
            }, {
                key: 'updatePagination', value: function (e) {
                    e && n(e.currentTarget).hasClass('disabled') || (!this.options.maintainSelected && this.resetRows(), this.initPagination(), 'server' === this.options.sidePagination ? this.initServer() : this.initBody(), this.trigger('page-change', this.options.pageNumber, this.options.pageSize))
                }
            }, {
                key: 'onPageListChange', value: function (e) {
                    e.preventDefault();
                    var t = n(e.currentTarget);
                    return t.parent().addClass('active').siblings().removeClass('active'), this.options.pageSize = t.text().toUpperCase() === this.options.formatAllRows().toUpperCase() ? this.options.formatAllRows() : +t.text(), this.$toolbar.find('.page-size').text(this.options.pageSize), this.updatePagination(e), !1
                }
            }, {
                key: 'onPagePre', value: function (e) {
                    return e.preventDefault(), 0 == this.options.pageNumber - 1 ? this.options.pageNumber = this.options.totalPages : this.options.pageNumber--, this.updatePagination(e), !1
                }
            }, {
                key: 'onPageNext', value: function (e) {
                    return e.preventDefault(), this.options.pageNumber + 1 > this.options.totalPages ? this.options.pageNumber = 1 : this.options.pageNumber++, this.updatePagination(e), !1
                }
            }, {
                key: 'onPageNumber', value: function (e) {
                    if (e.preventDefault(), this.options.pageNumber !== +n(e.currentTarget).text()) return this.options.pageNumber = +n(e.currentTarget).text(), this.updatePagination(e), !1
                }
            }, {
                key: 'initRow', value: function (e, t) {
                    var o = this, a = [], s = {}, l = [], d = '', p = {}, c = [];
                    if (!(-1 < r.findIndex(this.hiddenRows, e))) {
                        if (s = r.calculateObjectValue(this.options, this.options.rowStyle, [e, t], s), s && s.css) for (var h = function (e) {
                            return Object.keys(e).map(function (t) {
                                return [t, e[t]]
                            })
                        }(s.css), g = Array.isArray(h), u = 0, _iterator10 = g ? h : h[Symbol.iterator](); ;) {
                            var f;
                            if (g) {
                                if (u >= h.length) break;
                                f = h[u++]
                            } else {
                                if (u = h.next(), u.done) break;
                                f = u.value
                            }
                            var b = f, m = i(b, 2), y = m[0], w = m[1];
                            l.push(y + ': ' + w)
                        }
                        if (p = r.calculateObjectValue(this.options, this.options.rowAttributes, [e, t], p), p) for (var x = function (e) {
                            return Object.keys(e).map(function (t) {
                                return [t, e[t]]
                            })
                        }(p), S = Array.isArray(x), $ = 0, _iterator11 = S ? x : x[Symbol.iterator](); ;) {
                            var P;
                            if (S) {
                                if ($ >= x.length) break;
                                P = x[$++]
                            } else {
                                if ($ = x.next(), $.done) break;
                                P = $.value
                            }
                            var C = P, T = i(C, 2), O = T[0], A = T[1];
                            c.push(O + '="' + r.escapeHTML(A) + '"')
                        }
                        if (e._data && !n.isEmptyObject(e._data)) for (var R = function (e) {
                            return Object.keys(e).map(function (t) {
                                return [t, e[t]]
                            })
                        }(e._data), I = Array.isArray(R), _ = 0, _iterator12 = I ? R : R[Symbol.iterator](); ;) {
                            var V;
                            if (I) {
                                if (_ >= R.length) break;
                                V = R[_++]
                            } else {
                                if (_ = R.next(), _.done) break;
                                V = _.value
                            }
                            var F = V, B = i(F, 2), N = B[0], k = B[1];
                            if ('index' === N) return;
                            d += ' data-' + N + '="' + k + '"'
                        }
                        return a.push('<tr', r.sprintf(' %s', c.length ? c.join(' ') : void 0), r.sprintf(' id="%s"', Array.isArray(e) ? void 0 : e._id), r.sprintf(' class="%s"', s.classes || (Array.isArray(e) ? void 0 : e._class)), ' data-index="' + t + '"', r.sprintf(' data-uniqueid="%s"', e[this.options.uniqueId]), r.sprintf('%s', d), '>'), this.options.cardView && a.push('<td colspan="' + this.header.fields.length + '"><div class="card-views">'), !this.options.cardView && this.options.detailView && (a.push('<td>'), r.calculateObjectValue(null, this.options.detailFilter, [t, e]) && a.push('\n            <a class="detail-icon" href="#">\n            <i class="' + this.options.iconsPrefix + ' ' + this.options.icons.detailOpen + '"></i>\n            </a>\n          '), a.push('</td>')), this.header.fields.forEach(function (d, p) {
                            var h = '', g = r.getItemField(e, d, o.options.escape), u = '', f = '', b = {}, m = '',
                                y = o.header.classes[p], w = '', k = '', v = '', x = '', S = '', $ = o.columns[p];
                            if ((!o.fromHtml || 'undefined' != typeof g || $.checkbox || $.radio) && $.visible && (!o.options.cardView || $.cardVisible)) {
                                if ($.escape && (g = r.escapeHTML(g)), l.concat([o.header.styles[p]]).length && (w = ' style="' + l.concat([o.header.styles[p]]).join('; ') + '"'), e['_' + d + '_id'] && (m = r.sprintf(' id="%s"', e['_' + d + '_id'])), e['_' + d + '_class'] && (y = r.sprintf(' class="%s"', e['_' + d + '_class'])), e['_' + d + '_rowspan'] && (v = r.sprintf(' rowspan="%s"', e['_' + d + '_rowspan'])), e['_' + d + '_colspan'] && (x = r.sprintf(' colspan="%s"', e['_' + d + '_colspan'])), e['_' + d + '_title'] && (S = r.sprintf(' title="%s"', e['_' + d + '_title'])), b = r.calculateObjectValue(o.header, o.header.cellStyles[p], [g, e, t, d], b), b.classes && (y = ' class="' + b.classes + '"'), b.css) {
                                    for (var P = [], C = function (e) {
                                        return Object.keys(e).map(function (t) {
                                            return [t, e[t]]
                                        })
                                    }(b.css), T = Array.isArray(C), O = 0, _iterator13 = T ? C : C[Symbol.iterator](); ;) {
                                        var A;
                                        if (T) {
                                            if (O >= C.length) break;
                                            A = C[O++]
                                        } else {
                                            if (O = C.next(), O.done) break;
                                            A = O.value
                                        }
                                        var R = A, I = i(R, 2), _ = I[0], V = I[1];
                                        P.push(_ + ': ' + V)
                                    }
                                    w = ' style="' + P.concat(o.header.styles[p]).join('; ') + '"'
                                }
                                if (u = r.calculateObjectValue($, o.header.formatters[p], [g, e, t, d], g), e['_' + d + '_data'] && !n.isEmptyObject(e['_' + d + '_data'])) for (var F = function (e) {
                                    return Object.keys(e).map(function (t) {
                                        return [t, e[t]]
                                    })
                                }(e['_' + d + '_data']), B = Array.isArray(F), N = 0, _iterator14 = B ? F : F[Symbol.iterator](); ;) {
                                    var j;
                                    if (B) {
                                        if (N >= F.length) break;
                                        j = F[N++]
                                    } else {
                                        if (N = F.next(), N.done) break;
                                        j = N.value
                                    }
                                    var H = j, L = i(H, 2), D = L[0], E = L[1];
                                    if ('index' === D) return;
                                    k += ' data-' + D + '="' + E + '"'
                                }
                                if ($.checkbox || $.radio) {
                                    f = $.checkbox ? 'checkbox' : f, f = $.radio ? 'radio' : f;
                                    var z = $['class'] || '', c = !0 === u || g || u && u.checked,
                                        U = !$.checkboxEnabled || u && u.disabled;
                                    h = [o.options.cardView ? '<div class="card-view ' + z + '">' : '<td class="bs-checkbox ' + z + '">', '<input\n              data-index="' + t + '"\n              name="' + o.options.selectItemName + '"\n              type="' + f + '"\n              ' + r.sprintf('value="%s"', e[o.options.idField]) + '\n              ' + r.sprintf('checked="%s"', c ? 'checked' : void 0) + '\n              ' + r.sprintf('disabled="%s"', U ? 'disabled' : void 0) + ' />', o.header.formatters[p] && 'string' == typeof u ? u : '', o.options.cardView ? '</div>' : '</td>'].join(''), e[o.header.stateField] = !0 === u || !!g || u && u.checked
                                } else if (u = 'undefined' == typeof u || null === u ? o.options.undefinedText : u, o.options.cardView) {
                                    var q = o.options.showHeader ? '<span class="title"' + s + '>' + r.getFieldTitle(o.columns, d) + '</span>' : '';
                                    h = '<div class="card-view">' + q + '<span class="value">' + u + '</span></div>', o.options.smartDisplay && '' === u && (h = '<div class="card-view"></div>')
                                } else h = '<td' + m + y + w + k + v + x + S + '>' + u + '</td>';
                                a.push(h)
                            }
                        }), this.options.cardView && a.push('</div></td>'), a.push('</tr>'), a.join('')
                    }
                }
            }, {
                key: 'initBody', value: function (e) {
                    var t = this, o = this.getData();
                    this.trigger('pre-body', o), this.$body = this.$el.find('>tbody'), this.$body.length || (this.$body = n('<tbody></tbody>').appendTo(this.$el)), this.options.pagination && 'server' !== this.options.sidePagination || (this.pageFrom = 1, this.pageTo = o.length);
                    for (var a = n(document.createDocumentFragment()), s = !1, l = this.pageFrom - 1; l < this.pageTo; l++) {
                        var d = o[l], p = this.initRow(d, l, o, a);
                        s = s || !!p, p && 'string' == typeof p && a.append(p)
                    }
                    s ? this.$body.html(a) : this.$body.html('<tr class="no-records-found">' + r.sprintf('<td colspan="%s">%s</td>', this.$header.find('th').length, this.options.formatNoMatches()) + '</tr>'), e || this.scrollTo(0), this.$body.find('> tr[data-index] > td').off('click dblclick').on('click dblclick', function (e) {
                        var o = e.currentTarget, i = e.type, a = e.target, s = n(o), l = s.parent(),
                            d = t.data[l.data('index')], p = s[0].cellIndex, c = t.getVisibleFields(),
                            h = c[t.options.detailView && !t.options.cardView ? p - 1 : p],
                            g = t.columns[t.fieldsColumnsIndex[h]], u = r.getItemField(d, h, t.options.escape);
                        if (!s.find('.detail-icon').length && (t.trigger('click' === i ? 'click-cell' : 'dbl-click-cell', h, u, d, s), t.trigger('click' === i ? 'click-row' : 'dbl-click-row', d, l, h), 'click' === i && t.options.clickToSelect && g.clickToSelect && !t.options.ignoreClickToSelectOn(a))) {
                            var f = l.find(r.sprintf('[name="%s"]', t.options.selectItemName));
                            f.length && f[0].click()
                        }
                    }), this.$body.find('> tr[data-index] > td > .detail-icon').off('click').on('click', function (i) {
                        i.preventDefault();
                        var e = n(i.currentTarget), a = e.parent().parent(), s = a.data('index'), l = o[s];
                        if (a.next().is('tr.detail-view')) e.find('i').attr('class', r.sprintf('%s %s', t.options.iconsPrefix, t.options.icons.detailOpen)), t.trigger('collapse-row', s, l, a.next()), a.next().remove(); else {
                            e.find('i').attr('class', r.sprintf('%s %s', t.options.iconsPrefix, t.options.icons.detailClose)), a.after(r.sprintf('<tr class="detail-view"><td colspan="%s"></td></tr>', a.find('td').length));
                            var d = a.next().find('td'),
                                p = r.calculateObjectValue(t.options, t.options.detailFormatter, [s, l, d], '');
                            1 === d.length && d.append(p), t.trigger('expand-row', s, l, d)
                        }
                        return t.resetView(), !1
                    }), this.$selectItem = this.$body.find(r.sprintf('[name="%s"]', this.options.selectItemName)), this.$selectItem.off('click').on('click', function (o) {
                        o.stopImmediatePropagation();
                        var e = n(o.currentTarget);
                        t.check_(e.prop('checked'), e.data('index'))
                    }), this.header.events.forEach(function (e, o) {
                        var a = e;
                        if (a) {
                            'string' == typeof a && (a = r.calculateObjectValue(null, a));
                            var s = t.header.fields[o], l = t.getVisibleFields().indexOf(s);
                            if (-1 !== l) {
                                t.options.detailView && !t.options.cardView && (l += 1);
                                for (var d = function () {
                                    if (c) {
                                        if (h >= p.length) return 'break';
                                        g = p[h++]
                                    } else {
                                        if (h = p.next(), h.done) return 'break';
                                        g = h.value
                                    }
                                    var e = g, o = i(e, 2), a = o[0], r = o[1];
                                    t.$body.find('>tr:not(.no-records-found)').each(function (e, o) {
                                        var i = n(o), d = i.find(t.options.cardView ? '.card-view' : 'td').eq(l),
                                            p = a.indexOf(' '), c = a.substring(0, p), h = a.substring(p + 1);
                                        d.find(h).off(c).on(c, function (o) {
                                            var e = i.data('index'), a = t.data[e], n = a[s];
                                            r.apply(t, [o, n, a, e])
                                        })
                                    })
                                }, p = function (e) {
                                    return Object.keys(e).map(function (t) {
                                        return [t, e[t]]
                                    })
                                }(a), c = Array.isArray(p), h = 0, _iterator15 = c ? p : p[Symbol.iterator](); ;) {
                                    var g, u = d();
                                    if ('break' === u) break
                                }
                            }
                        }
                    }), this.updateSelected(), this.resetView(), this.trigger('post-body', o)
                }
            }, {
                key: 'initServer', value: function (e, t, o) {
                    var i = this, a = {}, s = this.header.fields.indexOf(this.options.sortName), l = {
                        searchText: this.searchText,
                        sortName: this.options.sortName,
                        sortOrder: this.options.sortOrder
                    };
                    if ((this.header.sortNames[s] && (l.sortName = this.header.sortNames[s]), this.options.pagination && 'server' === this.options.sidePagination && (l.pageSize = this.options.pageSize === this.options.formatAllRows() ? this.options.totalRows : this.options.pageSize, l.pageNumber = this.options.pageNumber), o || this.options.url || this.options.ajax) && ('limit' === this.options.queryParamsType && (l = {
                        search: l.searchText,
                        sort: l.sortName,
                        order: l.sortOrder
                    }, this.options.pagination && 'server' === this.options.sidePagination && (l.offset = this.options.pageSize === this.options.formatAllRows() ? 0 : this.options.pageSize * (this.options.pageNumber - 1), l.limit = this.options.pageSize === this.options.formatAllRows() ? this.options.totalRows : this.options.pageSize, 0 === l.limit && delete l.limit)), n.isEmptyObject(this.filterColumnsPartial) || (l.filter = JSON.stringify(this.filterColumnsPartial, null)), a = r.calculateObjectValue(this.options, this.options.queryParams, [l], a), n.extend(a, t || {}), !1 !== a)) {
                        e || this.$tableLoading.show();
                        var d = n.extend({}, r.calculateObjectValue(null, this.options.ajaxOptions), {
                            type: this.options.method,
                            url: o || this.options.url,
                            data: 'application/json' === this.options.contentType && 'post' === this.options.method ? JSON.stringify(a) : a,
                            cache: this.options.cache,
                            contentType: this.options.contentType,
                            dataType: this.options.dataType,
                            success: function (t) {
                                var o = r.calculateObjectValue(i.options, i.options.responseHandler, [t], t);
                                i.load(o), i.trigger('load-success', o), e || i.$tableLoading.hide()
                            },
                            error: function (t) {
                                var o = [];
                                'server' === i.options.sidePagination && (o = {}, o[i.options.totalField] = 0, o[i.options.dataField] = []), i.load(o), i.trigger('load-error', t.status, t), e || i.$tableLoading.hide()
                            }
                        });
                        this.options.ajax ? r.calculateObjectValue(this, this.options.ajax, [d], null) : (this._xhr && 4 !== this._xhr.readyState && this._xhr.abort(), this._xhr = n.ajax(d))
                    }
                }
            }, {
                key: 'initSearchText', value: function () {
                    if (this.options.search && (this.searchText = '', '' !== this.options.searchText)) {
                        var e = this.$toolbar.find('.search input');
                        e.val(this.options.searchText), this.onSearch({currentTarget: e, firedByInitSearchText: !0})
                    }
                }
            }, {
                key: 'getCaret', value: function () {
                    var e = this;
                    this.$header.find('th').each(function (t, o) {
                        n(o).find('.sortable').removeClass('desc asc').addClass(n(o).data('field') === e.options.sortName ? e.options.sortOrder : 'both')
                    })
                }
            }, {
                key: 'updateSelected', value: function () {
                    var e = this.$selectItem.filter(':enabled').length && this.$selectItem.filter(':enabled').length === this.$selectItem.filter(':enabled').filter(':checked').length;
                    this.$selectAll.add(this.$selectAll_).prop('checked', e), this.$selectItem.each(function (e, t) {
                        n(t).closest('tr')[n(t).prop('checked') ? 'addClass' : 'removeClass']('selected')
                    })
                }
            }, {
                key: 'updateRows', value: function () {
                    var e = this;
                    this.$selectItem.each(function (t, o) {
                        e.data[n(o).data('index')][e.header.stateField] = n(o).prop('checked')
                    })
                }
            }, {
                key: 'resetRows', value: function () {
                    for (var e = this.data, t = Array.isArray(e), o = 0, _iterator16 = t ? e : e[Symbol.iterator](); ;) {
                        var i;
                        if (t) {
                            if (o >= e.length) break;
                            i = e[o++]
                        } else {
                            if (o = e.next(), o.done) break;
                            i = o.value
                        }
                        var a = i;
                        this.$selectAll.prop('checked', !1), this.$selectItem.prop('checked', !1), this.header.stateField && (a[this.header.stateField] = !1)
                    }
                    this.initHiddenRows()
                }
            }, {
                key: 'trigger', value: function (e) {
                    for (var o, i = e + '.bs.table', a = arguments.length, s = Array(1 < a ? a - 1 : 0), l = 1; l < a; l++) s[l - 1] = arguments[l];
                    (o = this.options)[t.EVENTS[i]].apply(o, s), this.$el.trigger(n.Event(i), s), this.options.onAll(i, s), this.$el.trigger(n.Event('all.bs.table'), [i, s])
                }
            }, {
                key: 'resetHeader', value: function () {
                    clearTimeout(this.timeoutId_), this.timeoutId_ = setTimeout(n.proxy(this.fitHeader, this), this.$el.is(':hidden') ? 100 : 0)
                }
            }, {
                key: 'fitHeader', value: function () {
                    var e = this;
                    if (this.$el.is(':hidden')) return void(this.timeoutId_ = setTimeout(n.proxy(this.fitHeader, this), 100));
                    var t = this.$tableBody.get(0),
                        o = t.scrollWidth > t.clientWidth && t.scrollHeight > t.clientHeight + this.$header.outerHeight() ? r.getScrollBarWidth() : 0;
                    this.$el.css('margin-top', -this.$header.outerHeight());
                    var i = n(':focus');
                    if (0 < i.length) {
                        var p = i.parents('th');
                        if (0 < p.length) {
                            var c = p.attr('data-field');
                            if (void 0 !== c) {
                                var h = this.$header.find('[data-field=\'' + c + '\']');
                                0 < h.length && h.find(':input').addClass('focus-temp')
                            }
                        }
                    }
                    this.$header_ = this.$header.clone(!0, !0), this.$selectAll_ = this.$header_.find('[name="btSelectAll"]'), this.$tableHeader.css('margin-right', o).find('table').css('width', this.$el.outerWidth()).html('').attr('class', this.$el.attr('class')).append(this.$header_);
                    var a = n('.focus-temp:visible:eq(0)');
                    0 < a.length && (a.focus(), this.$header.find('.focus-temp').removeClass('focus-temp')), this.$header.find('th[data-field]').each(function (t, o) {
                        e.$header_.find(r.sprintf('th[data-field="%s"]', n(o).data('field'))).data(n(o).data())
                    });
                    for (var s = this.getVisibleFields(), l = this.$header_.find('th'), d = this.$body.find('>tr:first-child:not(.no-records-found)'); d.length && d.find('>td[colspan]:not([colspan="1"])').length;) d = d.next();
                    d.find('> *').each(function (t, o) {
                        var i = n(o), a = t;
                        if (e.options.detailView && !e.options.cardView) {
                            if (0 === t) {
                                var d = l.filter('.detail'), p = d.width() - d.find('.fht-cell').width();
                                d.find('.fht-cell').width(i.innerWidth() - p)
                            }
                            a = t - 1
                        }
                        if (-1 !== a) {
                            var c = e.$header_.find(r.sprintf('th[data-field="%s"]', s[a]));
                            1 < c.length && (c = n(l[i[0].cellIndex]));
                            var h = c.width() - c.find('.fht-cell').width();
                            c.find('.fht-cell').width(i.innerWidth() - h)
                        }
                    }), this.horizontalScroll(), this.trigger('post-header')
                }
            }, {
                key: 'resetFooter', value: function () {
                    var e = this.getData(), t = [];
                    if (this.options.showFooter && !this.options.cardView) {
                        !this.options.cardView && this.options.detailView && t.push('<th class="detail"><div class="th-inner"></div><div class="fht-cell"></div></th>');
                        for (var o = this.columns, a = Array.isArray(o), n = 0, _iterator17 = a ? o : o[Symbol.iterator](); ;) {
                            var s;
                            if (a) {
                                if (n >= o.length) break;
                                s = o[n++]
                            } else {
                                if (n = o.next(), n.done) break;
                                s = n.value
                            }
                            var l = s, d = '', p = '', c = [], h = {}, g = r.sprintf(' class="%s"', l['class']);
                            if (l.visible) {
                                if (this.options.cardView && !l.cardVisible) return;
                                if (d = r.sprintf('text-align: %s; ', l.falign ? l.falign : l.align), p = r.sprintf('vertical-align: %s; ', l.valign), h = r.calculateObjectValue(null, this.options.footerStyle, [l]), h && h.css) for (var u = function (e) {
                                    return Object.keys(e).map(function (t) {
                                        return [t, e[t]]
                                    })
                                }(h.css), f = Array.isArray(u), b = 0, _iterator18 = f ? u : u[Symbol.iterator](); ;) {
                                    var m;
                                    if (f) {
                                        if (b >= u.length) break;
                                        m = u[b++]
                                    } else {
                                        if (b = u.next(), b.done) break;
                                        m = b.value
                                    }
                                    var y = m, w = i(y, 2), k = w[0], v = w[1];
                                    c.push(k + ': ' + v)
                                }
                                h && h.classes && (g = r.sprintf(' class="%s"', l['class'] ? [l['class'], h.classes].join(' ') : h.classes)), t.push('<th', g, r.sprintf(' style="%s"', d + p + c.concat().join('; ')), '>'), t.push('<div class="th-inner">'), t.push(r.calculateObjectValue(l, l.footerFormatter, [e], '')), t.push('</div>'), t.push('<div class="fht-cell"></div>'), t.push('</div>'), t.push('</th>')
                            }
                        }
                        this.$tableFooter.find('tr').html(t.join('')), this.$tableFooter.show(), this.fitFooter()
                    }
                }
            }, {
                key: 'fitFooter', value: function () {
                    var e = this;
                    if (this.$el.is(':hidden')) return void setTimeout(n.proxy(this.fitFooter, this), 100);
                    var t = this.$tableBody.get(0),
                        o = t.scrollWidth > t.clientWidth && t.scrollHeight > t.clientHeight + this.$header.outerHeight() ? r.getScrollBarWidth() : 0;
                    this.$tableFooter.css('margin-right', o).find('table').css('width', this.$el.outerWidth()).attr('class', this.$el.attr('class'));
                    for (var i = this.getVisibleFields(), a = this.$tableFooter.find('th'), s = this.$body.find('>tr:first-child:not(.no-records-found)'); s.length && s.find('>td[colspan]:not([colspan="1"])').length;) s = s.next();
                    s.find('> *').each(function (t, o) {
                        var i = n(o), s = t;
                        if (e.options.detailView && !e.options.cardView) {
                            if (0 === t) {
                                var l = a.filter('.detail'), r = l.width() - l.find('.fht-cell').width();
                                l.find('.fht-cell').width(i.innerWidth() - r)
                            }
                            s = t - 1
                        }
                        if (-1 !== s) {
                            var d = a.eq(t), p = d.width() - d.find('.fht-cell').width();
                            d.find('.fht-cell').width(i.innerWidth() - p)
                        }
                    }), this.horizontalScroll()
                }
            }, {
                key: 'horizontalScroll', value: function () {
                    var e = this;
                    this.trigger('scroll-body'), this.$tableBody.off('scroll').on('scroll', function (t) {
                        var o = t.currentTarget;
                        e.options.showHeader && e.options.height && e.$tableHeader.scrollLeft(n(o).scrollLeft()), e.options.showFooter && !e.options.cardView && e.$tableFooter.scrollLeft(n(o).scrollLeft())
                    })
                }
            }, {
                key: 'toggleColumn', value: function (e, t, o) {
                    if (-1 !== e && (this.columns[e].visible = t, this.initHeader(), this.initSearch(), this.initPagination(), this.initBody(), this.options.showColumns)) {
                        var i = this.$toolbar.find('.keep-open input').prop('disabled', !1);
                        o && i.filter(r.sprintf('[value="%s"]', e)).prop('checked', t), i.filter(':checked').length <= this.options.minimumCountColumns && i.filter(':checked').prop('disabled', !0)
                    }
                }
            }, {
                key: 'getVisibleFields', value: function () {
                    for (var e = [], t = this.header.fields, o = Array.isArray(t), i = 0, _iterator19 = o ? t : t[Symbol.iterator](); ;) {
                        var a;
                        if (o) {
                            if (i >= t.length) break;
                            a = t[i++]
                        } else {
                            if (i = t.next(), i.done) break;
                            a = i.value
                        }
                        var n = a, s = this.columns[this.fieldsColumnsIndex[n]];
                        s.visible && e.push(n)
                    }
                    return e
                }
            }, {
                key: 'resetView', value: function (e) {
                    var t = 0;
                    if (e && e.height && (this.options.height = e.height), this.$selectAll.prop('checked', 0 < this.$selectItem.length && this.$selectItem.length === this.$selectItem.filter(':checked').length), this.options.cardView) return this.$el.css('margin-top', '0'), this.$tableContainer.css('padding-bottom', '0'), void this.$tableFooter.hide();
                    if (this.options.showHeader && this.options.height ? (this.$tableHeader.show(), this.resetHeader(), t += this.$header.outerHeight()) : (this.$tableHeader.hide(), this.trigger('post-header')), this.options.showFooter && (this.resetFooter(), this.options.height && (t += this.$tableFooter.outerHeight())), this.options.height) {
                        var o = this.$toolbar.outerHeight(!0), i = this.$pagination.outerHeight(!0),
                            a = this.options.height - o - i, n = this.$tableBody.find('table').outerHeight(!0);
                        this.$tableContainer.css('height', a + 'px'), this.$tableBorder && this.$tableBorder.css('height', a - n - t - 1 + 'px')
                    }
                    this.getCaret(), this.$tableContainer.css('padding-bottom', t + 'px'), this.trigger('reset-view')
                }
            }, {
                key: 'getData', value: function (e) {
                    var t = this.options.data;
                    return (this.searchText || this.options.sortName || !n.isEmptyObject(this.filterColumns) || !n.isEmptyObject(this.filterColumnsPartial)) && (t = this.data), e ? t.slice(this.pageFrom - 1, this.pageTo) : t
                }
            }, {
                key: 'load', value: function (e) {
                    var t = !1, o = e;
                    this.options.pagination && 'server' === this.options.sidePagination && (this.options.totalRows = o[this.options.totalField]), t = o.fixedScroll, o = Array.isArray(o) ? o : o[this.options.dataField], this.initData(o), this.initSearch(), this.initPagination(), this.initBody(t)
                }
            }, {
                key: 'append', value: function (e) {
                    this.initData(e, 'append'), this.initSearch(), this.initPagination(), this.initSort(), this.initBody(!0)
                }
            }, {
                key: 'prepend', value: function (e) {
                    this.initData(e, 'prepend'), this.initSearch(), this.initPagination(), this.initSort(), this.initBody(!0)
                }
            }, {
                key: 'remove', value: function (e) {
                    var t = this.options.data.length, o = void 0, i = void 0;
                    if (e.hasOwnProperty('field') && e.hasOwnProperty('values')) {
                        for (o = t - 1; 0 <= o; o--) (i = this.options.data[o], !!i.hasOwnProperty(e.field)) && -1 !== e.values.indexOf(i[e.field]) && (this.options.data.splice(o, 1), 'server' === this.options.sidePagination && (this.options.totalRows -= 1));
                        t === this.options.data.length || (this.initSearch(), this.initPagination(), this.initSort(), this.initBody(!0))
                    }
                }
            }, {
                key: 'removeAll', value: function () {
                    0 < this.options.data.length && (this.options.data.splice(0, this.options.data.length), this.initSearch(), this.initPagination(), this.initBody(!0))
                }
            }, {
                key: 'getRowByUniqueId', value: function (e) {
                    var t = this.options.uniqueId, o = this.options.data.length, a = e, n = null, s = void 0,
                        i = void 0, l = void 0;
                    for (s = o - 1; 0 <= s; s--) {
                        if (i = this.options.data[s], i.hasOwnProperty(t)) l = i[t]; else if (i._data && i._data.hasOwnProperty(t)) l = i._data[t]; else continue;
                        if ('string' == typeof l ? a = a.toString() : 'number' == typeof l && (+l === l && 0 == l % 1 ? a = parseInt(a) : l === +l && 0 !== l && (a = parseFloat(a))), l === a) {
                            n = i;
                            break
                        }
                    }
                    return n
                }
            }, {
                key: 'removeByUniqueId', value: function (e) {
                    var t = this.options.data.length, o = this.getRowByUniqueId(e);
                    o && this.options.data.splice(this.options.data.indexOf(o), 1), t === this.options.data.length || (this.initSearch(), this.initPagination(), this.initBody(!0))
                }
            }, {
                key: 'updateByUniqueId', value: function (e) {
                    for (var t = Array.isArray(e) ? e : [e], o = t, i = Array.isArray(o), a = 0, _iterator20 = i ? o : o[Symbol.iterator](); ;) {
                        var s;
                        if (i) {
                            if (a >= o.length) break;
                            s = o[a++]
                        } else {
                            if (a = o.next(), a.done) break;
                            s = a.value
                        }
                        var l = s;
                        if (l.hasOwnProperty('id') && l.hasOwnProperty('row')) {
                            var r = this.options.data.indexOf(this.getRowByUniqueId(l.id));
                            -1 !== r && n.extend(this.options.data[r], l.row)
                        }
                    }
                    this.initSearch(), this.initPagination(), this.initSort(), this.initBody(!0)
                }
            }, {
                key: 'refreshColumnTitle', value: function (e) {
                    if (e.hasOwnProperty('field') && e.hasOwnProperty('title') && (this.columns[this.fieldsColumnsIndex[e.field]].title = this.options.escape ? r.escapeHTML(e.title) : e.title, this.columns[this.fieldsColumnsIndex[e.field]].visible)) {
                        var t = void 0 === this.options.height ? this.$header : this.$tableHeader;
                        t.find('th[data-field]').each(function (t, o) {
                            if (n(o).data('field') === e.field) return n(n(o).find('.th-inner')[0]).text(e.title), !1
                        })
                    }
                }
            }, {
                key: 'insertRow', value: function (e) {
                    e.hasOwnProperty('index') && e.hasOwnProperty('row') && (this.options.data.splice(e.index, 0, e.row), this.initSearch(), this.initPagination(), this.initSort(), this.initBody(!0))
                }
            }, {
                key: 'updateRow', value: function (e) {
                    for (var t = Array.isArray(e) ? e : [e], o = t, i = Array.isArray(o), a = 0, _iterator21 = i ? o : o[Symbol.iterator](); ;) {
                        var s;
                        if (i) {
                            if (a >= o.length) break;
                            s = o[a++]
                        } else {
                            if (a = o.next(), a.done) break;
                            s = a.value
                        }
                        var l = s;
                        l.hasOwnProperty('index') && l.hasOwnProperty('row') && n.extend(this.options.data[l.index], l.row)
                    }
                    this.initSearch(), this.initPagination(), this.initSort(), this.initBody(!0)
                }
            }, {
                key: 'initHiddenRows', value: function () {
                    this.hiddenRows = []
                }
            }, {
                key: 'showRow', value: function (e) {
                    this.toggleRow(e, !0)
                }
            }, {
                key: 'hideRow', value: function (e) {
                    this.toggleRow(e, !1)
                }
            }, {
                key: 'toggleRow', value: function (e, t) {
                    var o;
                    if (e.hasOwnProperty('index') ? o = this.getData()[e.index] : e.hasOwnProperty('uniqueId') && (o = this.getRowByUniqueId(e.uniqueId)), !!o) {
                        var i = r.findIndex(this.hiddenRows, o);
                        t || -1 !== i ? t && -1 < i && this.hiddenRows.splice(i, 1) : this.hiddenRows.push(o), this.initBody(!0)
                    }
                }
            }, {
                key: 'getHiddenRows', value: function (e) {
                    if (e) return this.initHiddenRows(), void this.initBody(!0);
                    for (var t = this.getData(), o = [], i = t, a = Array.isArray(i), n = 0, _iterator22 = a ? i : i[Symbol.iterator](); ;) {
                        var s;
                        if (a) {
                            if (n >= i.length) break;
                            s = i[n++]
                        } else {
                            if (n = i.next(), n.done) break;
                            s = n.value
                        }
                        var l = s;
                        -1 !== this.hiddenRows.indexOf(l) && o.push(l)
                    }
                    return this.hiddenRows = o, o
                }
            }, {
                key: 'mergeCells', value: function (e) {
                    var t = e.index, o = this.getVisibleFields().indexOf(e.field), a = e.rowspan || 1,
                        n = e.colspan || 1, s = void 0, i = void 0, l = this.$body.find('>tr');
                    this.options.detailView && !this.options.cardView && (o += 1);
                    var r = l.eq(t).find('>td').eq(o);
                    if (!(0 > t || 0 > o || t >= this.data.length)) {
                        for (s = t; s < t + a; s++) for (i = o; i < o + n; i++) l.eq(s).find('>td').eq(i).hide();
                        r.attr('rowspan', a).attr('colspan', n).show()
                    }
                }
            }, {
                key: 'updateCell', value: function (e) {
                    e.hasOwnProperty('index') && e.hasOwnProperty('field') && e.hasOwnProperty('value') && (this.data[e.index][e.field] = e.value, !1 === e.reinit || (this.initSort(), this.initBody(!0)))
                }
            }, {
                key: 'updateCellById', value: function (e) {
                    var t = this;
                    if (e.hasOwnProperty('id') && e.hasOwnProperty('field') && e.hasOwnProperty('value')) {
                        var o = Array.isArray(e) ? e : [e];
                        o.forEach(function (e) {
                            var o = e.id, i = e.field, a = e.value, n = t.options.data.indexOf(t.getRowByUniqueId(o));
                            -1 === n || (t.data[n][i] = a)
                        }), !1 === e.reinit || (this.initSort(), this.initBody(!0))
                    }
                }
            }, {
                key: 'getOptions', value: function () {
                    var e = n.extend({}, this.options);
                    return delete e.data, n.extend(!0, {}, e)
                }
            }, {
                key: 'getSelections', value: function () {
                    var e = this;
                    return this.options.data.filter(function (t) {
                        return !0 === t[e.header.stateField]
                    })
                }
            }, {
                key: 'getAllSelections', value: function () {
                    var e = this;
                    return this.options.data.filter(function (t) {
                        return t[e.header.stateField]
                    })
                }
            }, {
                key: 'checkAll', value: function () {
                    this.checkAll_(!0)
                }
            }, {
                key: 'uncheckAll', value: function () {
                    this.checkAll_(!1)
                }
            }, {
                key: 'checkInvert', value: function () {
                    var e = this.$selectItem.filter(':enabled'), t = e.filter(':checked');
                    e.each(function (e, t) {
                        n(t).prop('checked', !n(t).prop('checked'))
                    }), this.updateRows(), this.updateSelected(), this.trigger('uncheck-some', t), t = this.getSelections(), this.trigger('check-some', t)
                }
            }, {
                key: 'checkAll_', value: function (e) {
                    var t;
                    e || (t = this.getSelections()), this.$selectAll.add(this.$selectAll_).prop('checked', e), this.$selectItem.filter(':enabled').prop('checked', e), this.updateRows(), e && (t = this.getSelections()), this.trigger(e ? 'check-all' : 'uncheck-all', t)
                }
            }, {
                key: 'check', value: function (e) {
                    this.check_(!0, e)
                }
            }, {
                key: 'uncheck', value: function (e) {
                    this.check_(!1, e)
                }
            }, {
                key: 'check_', value: function (e, t) {
                    var o = this.$selectItem.filter('[data-index="' + t + '"]'), i = this.data[t];
                    if (o.is(':radio') || this.options.singleSelect) {
                        for (var a = this.options.data, n = Array.isArray(a), s = 0, _iterator23 = n ? a : a[Symbol.iterator](); ;) {
                            var l;
                            if (n) {
                                if (s >= a.length) break;
                                l = a[s++]
                            } else {
                                if (s = a.next(), s.done) break;
                                l = s.value
                            }
                            var d = l;
                            d[this.header.stateField] = !1
                        }
                        this.$selectItem.filter(':checked').not(o).prop('checked', !1)
                    }
                    i[this.header.stateField] = e, o.prop('checked', e), this.updateSelected(), this.trigger(e ? 'check' : 'uncheck', this.data[t], o)
                }
            }, {
                key: 'checkBy', value: function (e) {
                    this.checkBy_(!0, e)
                }
            }, {
                key: 'uncheckBy', value: function (e) {
                    this.checkBy_(!1, e)
                }
            }, {
                key: 'checkBy_', value: function (e, t) {
                    var o = this;
                    if (t.hasOwnProperty('field') && t.hasOwnProperty('values')) {
                        var a = [];
                        this.options.data.forEach(function (n, s) {
                            if (!n.hasOwnProperty(t.field)) return !1;
                            if (-1 !== t.values.indexOf(n[t.field])) {
                                var i = o.$selectItem.filter(':enabled').filter(r.sprintf('[data-index="%s"]', s)).prop('checked', e);
                                n[o.header.stateField] = e, a.push(n), o.trigger(e ? 'check' : 'uncheck', n, i)
                            }
                        }), this.updateSelected(), this.trigger(e ? 'check-some' : 'uncheck-some', a)
                    }
                }
            }, {
                key: 'destroy', value: function () {
                    this.$el.insertBefore(this.$container), n(this.options.toolbar).insertBefore(this.$el), this.$container.next().remove(), this.$container.remove(), this.$el.html(this.$el_.html()).css('margin-top', '0').attr('class', this.$el_.attr('class') || '')
                }
            }, {
                key: 'showLoading', value: function () {
                    this.$tableLoading.show()
                }
            }, {
                key: 'hideLoading', value: function () {
                    this.$tableLoading.hide()
                }
            }, {
                key: 'togglePagination', value: function () {
                    this.options.pagination = !this.options.pagination;
                    var e = this.$toolbar.find('button[name="paginationSwitch"] i');
                    this.options.pagination ? e.attr('class', this.options.iconsPrefix + ' ' + this.options.icons.paginationSwitchDown) : e.attr('class', this.options.iconsPrefix + ' ' + this.options.icons.paginationSwitchUp), this.updatePagination()
                }
            }, {
                key: 'toggleFullscreen', value: function () {
                    this.$el.closest('.bootstrap-table').toggleClass('fullscreen')
                }
            }, {
                key: 'refresh', value: function (e) {
                    e && e.url && (this.options.url = e.url), e && e.pageNumber && (this.options.pageNumber = e.pageNumber), e && e.pageSize && (this.options.pageSize = e.pageSize), this.initServer(e && e.silent, e && e.query, e && e.url), this.trigger('refresh', e)
                }
            }, {
                key: 'resetWidth', value: function () {
                    this.options.showHeader && this.options.height && this.fitHeader(), this.options.showFooter && !this.options.cardView && this.fitFooter()
                }
            }, {
                key: 'showColumn', value: function (e) {
                    this.toggleColumn(this.fieldsColumnsIndex[e], !0, !0)
                }
            }, {
                key: 'hideColumn', value: function (e) {
                    this.toggleColumn(this.fieldsColumnsIndex[e], !1, !0)
                }
            }, {
                key: 'getHiddenColumns', value: function () {
                    return this.columns.filter(function (e) {
                        var t = e.visible;
                        return !t
                    })
                }
            }, {
                key: 'getVisibleColumns', value: function () {
                    return this.columns.filter(function (e) {
                        var t = e.visible;
                        return t
                    })
                }
            }, {
                key: 'toggleAllColumns', value: function (e) {
                    for (var t = this.columns, o = Array.isArray(t), i = 0, _iterator24 = o ? t : t[Symbol.iterator](); ;) {
                        var a;
                        if (o) {
                            if (i >= t.length) break;
                            a = t[i++]
                        } else {
                            if (i = t.next(), i.done) break;
                            a = i.value
                        }
                        var n = a;
                        n.visible = e
                    }
                    if (this.initHeader(), this.initSearch(), this.initPagination(), this.initBody(), this.options.showColumns) {
                        var s = this.$toolbar.find('.keep-open input').prop('disabled', !1);
                        s.filter(':checked').length <= this.options.minimumCountColumns && s.filter(':checked').prop('disabled', !0)
                    }
                }
            }, {
                key: 'showAllColumns', value: function () {
                    this.toggleAllColumns(!0)
                }
            }, {
                key: 'hideAllColumns', value: function () {
                    this.toggleAllColumns(!1)
                }
            }, {
                key: 'filterBy', value: function (e) {
                    this.filterColumns = n.isEmptyObject(e) ? {} : e, this.options.pageNumber = 1, this.initSearch(), this.updatePagination()
                }
            }, {
                key: 'scrollTo', value: function (e) {
                    if ('undefined' == typeof e) return this.$tableBody.scrollTop();
                    var t = e;
                    'string' == typeof e && 'bottom' === e && (t = this.$tableBody[0].scrollHeight), this.$tableBody.scrollTop(t)
                }
            }, {
                key: 'getScrollPosition', value: function () {
                    return this.scrollTo()
                }
            }, {
                key: 'selectPage', value: function (e) {
                    0 < e && e <= this.options.totalPages && (this.options.pageNumber = e, this.updatePagination())
                }
            }, {
                key: 'prevPage', value: function () {
                    1 < this.options.pageNumber && (this.options.pageNumber--, this.updatePagination())
                }
            }, {
                key: 'nextPage', value: function () {
                    this.options.pageNumber < this.options.totalPages && (this.options.pageNumber++, this.updatePagination())
                }
            }, {
                key: 'toggleView', value: function () {
                    this.options.cardView = !this.options.cardView, this.initHeader();
                    var e = this.$toolbar.find('button[name="toggle"] i');
                    this.options.cardView ? (e.removeClass(this.options.icons.toggleOff), e.addClass(this.options.icons.toggleOn)) : (e.removeClass(this.options.icons.toggleOn), e.addClass(this.options.icons.toggleOff)), this.initBody(), this.trigger('toggle', this.options.cardView)
                }
            }, {
                key: 'refreshOptions', value: function (e) {
                    r.compareObjects(this.options, e, !0) || (this.options = n.extend(this.options, e), this.trigger('refresh-options', this.options), this.destroy(), this.init())
                }
            }, {
                key: 'resetSearch', value: function (e) {
                    var t = this.$toolbar.find('.search input');
                    t.val(e || ''), this.onSearch({currentTarget: t})
                }
            }, {
                key: 'expandRow_', value: function (e, t) {
                    var o = this.$body.find(r.sprintf('> tr[data-index="%s"]', t));
                    o.next().is('tr.detail-view') === !e && o.find('> td > .detail-icon').click()
                }
            }, {
                key: 'expandRow', value: function (e) {
                    this.expandRow_(!0, e)
                }
            }, {
                key: 'collapseRow', value: function (e) {
                    this.expandRow_(!1, e)
                }
            }, {
                key: 'expandAllRows', value: function (e) {
                    var t = this;
                    if (e) {
                        var o = this.$body.find(r.sprintf('> tr[data-index="%s"]', 0)), a = null, s = !1, l = -1;
                        if (o.next().is('tr.detail-view') ? !o.next().next().is('tr.detail-view') && (o.next().find('.detail-icon').click(), s = !0) : (o.find('> td > .detail-icon').click(), s = !0), s) try {
                            l = setInterval(function () {
                                a = t.$body.find('tr.detail-view').last().find('.detail-icon'), 0 < a.length ? a.click() : clearInterval(l)
                            }, 1)
                        } catch (e) {
                            clearInterval(l)
                        }
                    } else for (var d = this.$body.children(), p = 0; p < d.length; p++) this.expandRow_(!0, n(d[p]).data('index'))
                }
            }, {
                key: 'collapseAllRows', value: function (e) {
                    if (e) this.expandRow_(!1, 0); else for (var t = this.$body.children(), o = 0; o < t.length; o++) this.expandRow_(!1, n(t[o]).data('index'))
                }
            }, {
                key: 'updateFormatText', value: function (e, t) {
                    this.options[r.sprintf('format%s', e)] && ('string' == typeof t ? this.options[r.sprintf('format%s', e)] = function () {
                        return t
                    } : 'function' == typeof t && (this.options[r.sprintf('format%s', e)] = t)), this.initToolbar(), this.initPagination(), this.initBody()
                }
            }]), t
        }();
        c.DEFAULTS = d, c.LOCALES = p, c.COLUMN_DEFAULTS = {
            radio: !1,
            checkbox: !1,
            checkboxEnabled: !0,
            field: void 0,
            title: void 0,
            titleTooltip: void 0,
            class: void 0,
            align: void 0,
            halign: void 0,
            falign: void 0,
            valign: void 0,
            width: void 0,
            sortable: !1,
            order: 'asc',
            visible: !0,
            switchable: !0,
            clickToSelect: !0,
            formatter: void 0,
            footerFormatter: void 0,
            events: void 0,
            sorter: void 0,
            sortName: void 0,
            cellStyle: void 0,
            searchable: !0,
            searchFormatter: !0,
            cardVisible: !0,
            escape: !1,
            showSelectTitle: !1
        }, c.EVENTS = {
            "all.bs.table": 'onAll',
            "click-cell.bs.table": 'onClickCell',
            "dbl-click-cell.bs.table": 'onDblClickCell',
            "click-row.bs.table": 'onClickRow',
            "dbl-click-row.bs.table": 'onDblClickRow',
            "sort.bs.table": 'onSort',
            "check.bs.table": 'onCheck',
            "uncheck.bs.table": 'onUncheck',
            "check-all.bs.table": 'onCheckAll',
            "uncheck-all.bs.table": 'onUncheckAll',
            "check-some.bs.table": 'onCheckSome',
            "uncheck-some.bs.table": 'onUncheckSome',
            "load-success.bs.table": 'onLoadSuccess',
            "load-error.bs.table": 'onLoadError',
            "column-switch.bs.table": 'onColumnSwitch',
            "page-change.bs.table": 'onPageChange',
            "search.bs.table": 'onSearch',
            "toggle.bs.table": 'onToggle',
            "pre-body.bs.table": 'onPreBody',
            "post-body.bs.table": 'onPostBody',
            "post-header.bs.table": 'onPostHeader',
            "expand-row.bs.table": 'onExpandRow',
            "collapse-row.bs.table": 'onCollapseRow',
            "refresh-options.bs.table": 'onRefreshOptions',
            "reset-view.bs.table": 'onResetView',
            "refresh.bs.table": 'onRefresh',
            "scroll-body.bs.table": 'onScrollBody'
        };
        var h = ['getOptions', 'getSelections', 'getAllSelections', 'getData', 'load', 'append', 'prepend', 'remove', 'removeAll', 'insertRow', 'updateRow', 'updateCell', 'updateByUniqueId', 'removeByUniqueId', 'getRowByUniqueId', 'showRow', 'hideRow', 'getHiddenRows', 'mergeCells', 'refreshColumnTitle', 'checkAll', 'uncheckAll', 'checkInvert', 'check', 'uncheck', 'checkBy', 'uncheckBy', 'refresh', 'resetView', 'resetWidth', 'destroy', 'showLoading', 'hideLoading', 'showColumn', 'hideColumn', 'getHiddenColumns', 'getVisibleColumns', 'showAllColumns', 'hideAllColumns', 'filterBy', 'scrollTo', 'getScrollPosition', 'selectPage', 'prevPage', 'nextPage', 'togglePagination', 'toggleView', 'refreshOptions', 'resetSearch', 'expandRow', 'collapseRow', 'expandAllRows', 'collapseAllRows', 'updateFormatText', 'updateCellById'];
        n.BootstrapTable = c, n.fn.bootstrapTable = function (e) {
            for (var t = arguments.length, o = Array(1 < t ? t - 1 : 0), i = 1; i < t; i++) o[i - 1] = arguments[i];
            var s;
            return this.each(function (t, i) {
                var l = n(i).data('bootstrap.table'),
                    r = n.extend({}, c.DEFAULTS, n(i).data(), 'object' === ('undefined' == typeof e ? 'undefined' : a(e)) && e);
                if ('string' == typeof e) {
                    var d;
                    if (-1 === h.indexOf(e)) throw new Error('Unknown method: ' + e);
                    if (!l) return;
                    s = (d = l)[e].apply(d, o), 'destroy' === e && n(i).removeData('bootstrap.table')
                }
                l || n(i).data('bootstrap.table', l = new n.BootstrapTable(i, r))
            }), 'undefined' == typeof s ? this : s
        }, n.fn.bootstrapTable.Constructor = c, n.fn.bootstrapTable.defaults = c.DEFAULTS, n.fn.bootstrapTable.columnDefaults = c.COLUMN_DEFAULTS, n.fn.bootstrapTable.locales = c.LOCALES, n.fn.bootstrapTable.methods = h, n.fn.bootstrapTable.utils = r, n(function () {
            n('[data-toggle="table"]').bootstrapTable()
        })
    })(jQuery)
});