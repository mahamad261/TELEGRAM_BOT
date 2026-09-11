<?php

error_reporting(0);
ini_set('display_errors', '0');
ini_set('log_errors', '1');
set_time_limit(0);
date_default_timezone_set('Asia/Tehran');

/* =========================================================
   تنظیمات اولیه
   ========================================================= */

define('MAIN_BOT_TOKEN', '8613140319:AAHg1DkMljOBQQapOM9e0Ajd8qNbgwNa8eQ');
define('OWNER_ID', 8276393129); // آیدی عددی مالک اصلی

define('BASE_DIR', __DIR__ . '/');
define('DATA_DIR', BASE_DIR . 'data/');
define('BOTS_DIR', BASE_DIR . 'bots/');
define('TEMP_DIR', BASE_DIR . 'temp/');
define('LOGS_DIR', BASE_DIR . 'logs/');

define('SETTINGS_FILE', DATA_DIR . 'settings.json');
define('ADMINS_FILE', DATA_DIR . 'admins.json');
define('USERS_FILE', DATA_DIR . 'users.json');
define('BOTS_FILE', DATA_DIR . 'bots.json');
define('PAYMENTS_FILE', DATA_DIR . 'payments.json');
define('PAYMENT_METHODS_FILE', DATA_DIR . 'payment_methods.json');
define('TICKETS_FILE', DATA_DIR . 'tickets.json');
define('BROADCASTS_FILE', DATA_DIR . 'broadcasts.json');
define('TRANSACTIONS_FILE', DATA_DIR . 'transactions.json');

foreach ([DATA_DIR, BOTS_DIR, TEMP_DIR, LOGS_DIR] as $dir) {
    if (!is_dir($dir)) {
        mkdir($dir, 0755, true);
    }
}

/* =========================================================
   دیتای پیش‌فرض
   ========================================================= */

function defaultSettings()
{
    return [
        'service_name' => 'ربات‌ساز حرفه‌ای',
        'currency' => 'تومان',
        'maintenance' => false,
        'bot_price' => 80000,
        'free_bots' => 1,
        'default_bot_limit' => 999999,
        'max_file_mb' => 10,
        'support_id' => OWNER_ID,
        'strict_security' => true,
        'force_join' => [
            'enabled' => false,
            'channels' => []
        ],
        'buttons' => [
            'run_bot' => '🚀 ران کردن ربات',
            'account' => '👤 حساب کاربری',
            'balance' => '💰 افزایش موجودی',
            'guide' => '📚 راهنمای بات',
            'ticket' => '🎫 تیکت پشتیبانی',
            'admin' => '👑 مدیریت ویژه',
            'back' => '🔙 بازگشت',
            'my_bots' => '🤖 ربات‌های من',
            'my_tickets' => '🎫 تیکت‌های من'
        ],
        'admin_buttons' => [
            'users' => '👥 مدیریت کاربران',
            'bots' => '🤖 مدیریت ربات‌ها',
            'finance' => '💰 مدیریت مالی',
            'payment_methods' => '💳 روش‌های پرداخت',
            'plans' => '📦 تنظیم پلن‌ها و قیمت‌ها',
            'guide' => '📚 تنظیم راهنمای بات',
            'tickets' => '🎫 مدیریت تیکت‌ها',
            'broadcast' => '📢 ارسال و فوروارد همگانی',
            'force_join' => '🔐 عضویت اجباری',
            'customize' => '🎨 شخصی‌سازی متن‌ها و دکمه‌ها',
            'stats' => '📊 آمار کلی',
            'settings' => '⚙️ تنظیمات ربات',
            'admins' => '🔐 مدیریت ادمین‌ها',
            'back' => '🔙 بازگشت'
        ],
        'texts' => [
            'start' => "🤖 <b>{service_name}</b>\n\nسلام {name} عزیز 🌹\nبه پنل حرفه‌ای ساخت و مدیریت ربات خوش آمدید.\n\nاز دکمه‌های پایین استفاده کنید.",
            'no_access' => '⛔ شما دسترسی لازم برای این بخش را ندارید.',
            'blocked' => '🚫 حساب شما توسط مدیریت مسدود شده است.',
            'maintenance' => "🛠 ربات در حال بروزرسانی است.\nلطفاً کمی بعد دوباره تلاش کنید.",
            'guide' => "📚 <b>راهنمای استفاده از ربات</b>\n\n1️⃣ روی دکمه ران کردن ربات بزنید.\n2️⃣ فایل PHP یا ZIP ربات خود را ارسال کنید.\n3️⃣ سیستم توکن را بررسی می‌کند.\n4️⃣ وبهوک به‌صورت خودکار فعال می‌شود.\n\nدر صورت نیاز از بخش تیکت پشتیبانی پیام بدهید.",
            'force_join' => "🔐 <b>عضویت اجباری</b>\n\nبرای استفاده از ربات ابتدا در کانال‌ها یا گروه‌های زیر عضو شوید، سپس روی دکمه بررسی عضویت بزنید.",
            'join_ok' => '✅ عضویت شما تایید شد. اکنون می‌توانید از ربات استفاده کنید.',
            'join_bad' => '❌ هنوز عضو همه کانال‌ها یا گروه‌های اجباری نشده‌اید.',
            'run_intro' => "🚀 <b>ران کردن ربات</b>\n\n💰 قیمت ران کردن هر ربات: <b>{price}</b>\n🎁 سهمیه رایگان شما: <b>{free_total}</b> عدد\n✅ استفاده‌شده رایگان: <b>{free_used}</b> عدد\n🤖 تعداد ربات‌های شما: <b>{bot_count}</b> عدد\n💳 موجودی فعلی: <b>{balance}</b>\n\n📤 فایل PHP یا ZIP ربات را ارسال کنید.",
            'not_enough_balance' => "❌ موجودی شما کافی نیست.\n\n💳 موجودی فعلی: <b>{balance}</b>\n💰 مبلغ مورد نیاز: <b>{price}</b>\n\nبرای ادامه، ابتدا موجودی را افزایش دهید.",
            'upload_processing' => '⏳ در حال دریافت و بررسی فایل...',
            'upload_success' => "✅ <b>ربات با موفقیت ساخته شد!</b>\n\n🤖 ربات: @{username}\n📛 نام: {name}\n🆔 آیدی: <code>{bot_id}</code>\n🌐 Webhook: ✅ فعال\n📁 فایل اصلی: <code>{main_file}</code>\n🔗 لینک وبهوک:\n<code>{webhook_url}</code>\n\n🚀 ربات آماده استفاده است.",
            'account' => "👤 <b>حساب کاربری شما</b>\n\n━━━━━━━━━━━━━━\n\n🆔 آیدی عددی:\n<code>{id}</code>\n\n👤 نام:\n<b>{name}</b>\n\n🔗 یوزرنیم:\n{username}\n\n📅 تاریخ عضویت:\n{joined_at}\n\n🕒 آخرین فعالیت:\n{last_seen}\n\n💰 موجودی کیف پول:\n<b>{balance}</b>\n\n📊 مجموع پرداخت تایید شده:\n<b>{total_paid}</b>\n\n🤖 تعداد ربات‌های ساخته‌شده:\n<b>{bot_count}</b> عدد\n\n🎁 سهمیه رایگان کل:\n<b>{free_total}</b> عدد\n\n✅ ربات رایگان استفاده‌شده:\n<b>{free_used}</b> عدد\n\n💎 وضعیت حساب:\n<b>{vip}</b>\n\n📦 سقف مجاز ربات:\n<b>{bot_limit}</b> عدد\n\n🚫 وضعیت مسدودی:\n<b>{blocked}</b>\n\n🎫 تیکت‌های باز:\n<b>{open_tickets}</b> عدد\n\n━━━━━━━━━━━━━━\n\nاز دکمه‌های زیر برای مدیریت حساب استفاده کنید.",
            'balance' => "💰 <b>افزایش موجودی</b>\n\n━━━━━━━━━━━━━━\n\n💳 موجودی فعلی شما:\n<b>{balance}</b>\n\nبرای افزایش موجودی، یکی از روش‌های پرداخت زیر را انتخاب کنید.",
            'ticket_intro' => "🎫 <b>تیکت پشتیبانی</b>\n\nاز این بخش می‌توانید با پشتیبانی ارتباط بگیرید.\nموضوع درخواست را انتخاب کنید یا تیکت‌های قبلی را مشاهده کنید.",
            'ticket_created' => "✅ تیکت شما با موفقیت ثبت شد.\n\n🆔 شماره تیکت: <code>{ticket_id}</code>\n📌 وضعیت: باز\n\nپشتیبانی به‌زودی پاسخ شما را بررسی می‌کند."
        ]
    ];
}

function defaultPaymentMethods()
{
    return [
        'card_default' => [
            'id' => 'card_default',
            'name' => '💳 کارت به کارت',
            'details' => "💳 شماره کارت:\n<code>6037-0000-0000-0000</code>\n\n👤 به نام:\nنام صاحب کارت\n\nبعد از پرداخت، رسید را ارسال کنید.",
            'active' => true,
            'created_at' => now()
        ]
    ];
}

/* =========================================================
   ابزارهای عمومی دیتابیس و متن
   ========================================================= */

function now()
{
    return date('Y-m-d H:i:s');
}

function h($text)
{
    return htmlspecialchars((string)$text, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}

function startsWith($text, $prefix)
{
    return substr((string)$text, 0, strlen($prefix)) === $prefix;
}

function newId($prefix)
{
    return $prefix . '_' . date('ymdHis') . '_' . substr(str_shuffle('abcdefghijklmnopqrstuvwxyz0123456789'), 0, 6);
}

function jsonRead($file, $default = [])
{
    if (!file_exists($file)) {
        return $default;
    }

    $raw = file_get_contents($file);
    $data = json_decode($raw, true);

    return is_array($data) ? $data : $default;
}

function jsonWrite($file, $data)
{
    file_put_contents($file, json_encode($data, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE), LOCK_EX);
}

function settings()
{
    $default = defaultSettings();
    $current = jsonRead(SETTINGS_FILE, []);
    return array_replace_recursive($default, $current);
}

function saveSettings($settings)
{
    jsonWrite(SETTINGS_FILE, $settings);
}

function admins()
{
    $data = jsonRead(ADMINS_FILE, []);
    if (empty($data)) {
        $data = [
            (string)OWNER_ID => [
                'id' => OWNER_ID,
                'role' => 'owner',
                'created_at' => now()
            ]
        ];
        jsonWrite(ADMINS_FILE, $data);
    }
    return $data;
}

function saveAdmins($data)
{
    jsonWrite(ADMINS_FILE, $data);
}

function users()
{
    return jsonRead(USERS_FILE, []);
}

function saveUsers($data)
{
    jsonWrite(USERS_FILE, $data);
}

function bots()
{
    return jsonRead(BOTS_FILE, []);
}

function saveBots($data)
{
    jsonWrite(BOTS_FILE, $data);
}

function payments()
{
    return jsonRead(PAYMENTS_FILE, []);
}

function savePayments($data)
{
    jsonWrite(PAYMENTS_FILE, $data);
}

function paymentMethods()
{
    $data = jsonRead(PAYMENT_METHODS_FILE, []);
    if (empty($data)) {
        $data = defaultPaymentMethods();
        jsonWrite(PAYMENT_METHODS_FILE, $data);
    }
    return $data;
}

function savePaymentMethods($data)
{
    jsonWrite(PAYMENT_METHODS_FILE, $data);
}

function tickets()
{
    return jsonRead(TICKETS_FILE, []);
}

function saveTickets($data)
{
    jsonWrite(TICKETS_FILE, $data);
}

function broadcasts()
{
    return jsonRead(BROADCASTS_FILE, []);
}

function saveBroadcasts($data)
{
    jsonWrite(BROADCASTS_FILE, $data);
}

function transactions()
{
    return jsonRead(TRANSACTIONS_FILE, []);
}

function saveTransactions($data)
{
    jsonWrite(TRANSACTIONS_FILE, $data);
}

function initStorage()
{
    if (!file_exists(SETTINGS_FILE)) {
        saveSettings(defaultSettings());
    }
    if (!file_exists(ADMINS_FILE)) {
        saveAdmins([
            (string)OWNER_ID => [
                'id' => OWNER_ID,
                'role' => 'owner',
                'created_at' => now()
            ]
        ]);
    }
    foreach ([USERS_FILE, BOTS_FILE, PAYMENTS_FILE, TICKETS_FILE, BROADCASTS_FILE, TRANSACTIONS_FILE] as $file) {
        if (!file_exists($file)) {
            jsonWrite($file, []);
        }
    }
    if (!file_exists(PAYMENT_METHODS_FILE)) {
        savePaymentMethods(defaultPaymentMethods());
    }
}

initStorage();

function normalizeDigits($text)
{
    $fa = ['۰','۱','۲','۳','۴','۵','۶','۷','۸','۹'];
    $ar = ['٠','١','٢','٣','٤','٥','٦','٧','٨','٩'];
    $en = ['0','1','2','3','4','5','6','7','8','9'];
    return str_replace($ar, $en, str_replace($fa, $en, (string)$text));
}

function toInt($text)
{
    $text = normalizeDigits($text);
    $text = preg_replace('/[^0-9\-]/', '', $text);
    return (int)$text;
}

function money($amount)
{
    $s = settings();
    return number_format((int)$amount) . ' ' . $s['currency'];
}

function formatBytes($bytes)
{
    $units = ['B', 'KB', 'MB', 'GB'];
    $i = 0;
    while ($bytes >= 1024 && $i < count($units) - 1) {
        $bytes /= 1024;
        $i++;
    }
    return round($bytes, 2) . ' ' . $units[$i];
}

function shortText($text, $length = 20)
{
    $text = strip_tags((string)$text);
    if (function_exists('mb_substr')) {
        return mb_substr($text, 0, $length, 'UTF-8');
    }
    return substr($text, 0, $length);
}

function tpl($text, $vars = [])
{
    $vars['service_name'] = $vars['service_name'] ?? settings()['service_name'];
    foreach ($vars as $key => $value) {
        $text = str_replace('{' . $key . '}', (string)$value, $text);
    }
    return $text;
}

/* =========================================================
   تلگرام API
   ========================================================= */

function tgApi($token, $method, $data = [])
{
    $url = "https://api.telegram.org/bot{$token}/{$method}";

    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => $url,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $data,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_SSL_VERIFYPEER => false,
        CURLOPT_CONNECTTIMEOUT => 15,
        CURLOPT_TIMEOUT => 60
    ]);

    $result = curl_exec($ch);
    curl_close($ch);

    $json = json_decode($result, true);
    return is_array($json) ? $json : ['ok' => false, 'description' => 'Invalid Telegram response'];
}

function bot($method, $data = [])
{
    return tgApi(MAIN_BOT_TOKEN, $method, $data);
}

function sendMessage($chatId, $text, $keyboard = null, $parseMode = 'HTML')
{
    $data = [
        'chat_id' => $chatId,
        'text' => $text,
        'disable_web_page_preview' => true
    ];
    if ($parseMode) {
        $data['parse_mode'] = $parseMode;
    }
    if ($keyboard) {
        $data['reply_markup'] = json_encode($keyboard, JSON_UNESCAPED_UNICODE);
    }
    return bot('sendMessage', $data);
}

function editMessage($chatId, $messageId, $text, $keyboard = null, $parseMode = 'HTML')
{
    $data = [
        'chat_id' => $chatId,
        'message_id' => $messageId,
        'text' => $text,
        'disable_web_page_preview' => true
    ];
    if ($parseMode) {
        $data['parse_mode'] = $parseMode;
    }
    if ($keyboard) {
        $data['reply_markup'] = json_encode($keyboard, JSON_UNESCAPED_UNICODE);
    }
    return bot('editMessageText', $data);
}

function answerCallback($callbackId, $text = '', $alert = false)
{
    return bot('answerCallbackQuery', [
        'callback_query_id' => $callbackId,
        'text' => $text,
        'show_alert' => $alert
    ]);
}

function copyMsg($toChat, $fromChat, $messageId)
{
    return bot('copyMessage', [
        'chat_id' => $toChat,
        'from_chat_id' => $fromChat,
        'message_id' => $messageId
    ]);
}

function forwardMsg($toChat, $fromChat, $messageId)
{
    return bot('forwardMessage', [
        'chat_id' => $toChat,
        'from_chat_id' => $fromChat,
        'message_id' => $messageId
    ]);
}

function sendDoc($chatId, $path, $caption = '')
{
    if (!file_exists($path)) {
        return ['ok' => false, 'description' => 'File not found'];
    }
    return bot('sendDocument', [
        'chat_id' => $chatId,
        'document' => new CURLFile($path),
        'caption' => $caption,
        'parse_mode' => 'HTML'
    ]);
}

function getBaseUrl()
{
    $https = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') ||
        (!empty($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https') ||
        (!empty($_SERVER['SERVER_PORT']) && $_SERVER['SERVER_PORT'] == 443);

    $protocol = $https ? 'https://' : 'http://';
    $host = $_SERVER['HTTP_HOST'] ?? 'localhost';
    $path = rtrim(dirname($_SERVER['SCRIPT_NAME']), '/\\');

    return $protocol . $host . ($path ? $path . '/' : '/');
}

function downloadTelegramFile($fileId)
{
    $info = bot('getFile', ['file_id' => $fileId]);
    if (!$info || empty($info['ok'])) {
        return false;
    }

    $filePath = $info['result']['file_path'];
    $url = 'https://api.telegram.org/file/bot' . MAIN_BOT_TOKEN . '/' . $filePath;

    $ch = curl_init();
    curl_setopt_array($ch, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_SSL_VERIFYPEER => false,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_CONNECTTIMEOUT => 20,
        CURLOPT_TIMEOUT => 120
    ]);
    $content = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($code !== 200 || $content === false) {
        return false;
    }
    return $content;
}

/* =========================================================
   کاربران، ادمین‌ها، وضعیت‌ها
   ========================================================= */

function isAdmin($id)
{
    if ((int)$id === (int)OWNER_ID) {
        return true;
    }
    $admins = admins();
    return isset($admins[(string)$id]);
}

function addAdminUser($id)
{
    $admins = admins();
    $id = (int)$id;
    if (!isset($admins[(string)$id])) {
        $admins[(string)$id] = [
            'id' => $id,
            'role' => 'admin',
            'created_at' => now()
        ];
        saveAdmins($admins);
        return true;
    }
    return false;
}

function removeAdminUser($id)
{
    $id = (int)$id;
    if ($id === (int)OWNER_ID) {
        return false;
    }
    $admins = admins();
    if (isset($admins[(string)$id])) {
        unset($admins[(string)$id]);
        saveAdmins($admins);
        return true;
    }
    return false;
}

function userDefault($id, $from = [])
{
    $s = settings();
    return [
        'id' => (int)$id,
        'first_name' => $from['first_name'] ?? '',
        'last_name' => $from['last_name'] ?? '',
        'username' => $from['username'] ?? '',
        'joined_at' => now(),
        'last_seen' => now(),
        'balance' => 0,
        'total_paid' => 0,
        'free_used' => 0,
        'bot_limit' => $s['default_bot_limit'],
        'is_vip' => false,
        'blocked' => false,
        'blocked_by_bot' => false,
        'state' => null,
        'state_data' => [],
        'notes' => ''
    ];
}

function registerUser($from)
{
    $id = (int)($from['id'] ?? 0);
    if (!$id) {
        return null;
    }

    $users = users();
    if (!isset($users[(string)$id])) {
        $users[(string)$id] = userDefault($id, $from);
    }

    $users[(string)$id]['first_name'] = $from['first_name'] ?? $users[(string)$id]['first_name'];
    $users[(string)$id]['last_name'] = $from['last_name'] ?? $users[(string)$id]['last_name'];
    $users[(string)$id]['username'] = $from['username'] ?? $users[(string)$id]['username'];
    $users[(string)$id]['last_seen'] = now();

    saveUsers($users);
    return $users[(string)$id];
}

function getUser($id)
{
    $users = users();
    if (!isset($users[(string)$id])) {
        $users[(string)$id] = userDefault($id);
        saveUsers($users);
    }
    return $users[(string)$id];
}

function updateUser($id, $patch)
{
    $users = users();
    if (!isset($users[(string)$id])) {
        $users[(string)$id] = userDefault($id);
    }
    foreach ($patch as $key => $value) {
        $users[(string)$id][$key] = $value;
    }
    saveUsers($users);
    return $users[(string)$id];
}

function setState($userId, $state, $data = [])
{
    updateUser($userId, [
        'state' => $state,
        'state_data' => $data
    ]);
}

function clearState($userId)
{
    updateUser($userId, [
        'state' => null,
        'state_data' => []
    ]);
}

function addTransaction($userId, $type, $amount, $description, $meta = [])
{
    $tx = transactions();
    $id = newId('tx');
    $tx[$id] = [
        'id' => $id,
        'user_id' => (int)$userId,
        'type' => $type,
        'amount' => (int)$amount,
        'description' => $description,
        'meta' => $meta,
        'created_at' => now()
    ];
    saveTransactions($tx);
    return $id;
}

function changeBalance($userId, $amount, $description, $type = 'manual', $meta = [])
{
    $u = getUser($userId);
    $newBalance = max(0, (int)$u['balance'] + (int)$amount);
    updateUser($userId, ['balance' => $newBalance]);
    addTransaction($userId, $type, $amount, $description, $meta);
    return $newBalance;
}

function fullName($u)
{
    $name = trim(($u['first_name'] ?? '') . ' ' . ($u['last_name'] ?? ''));
    return $name ?: 'بدون نام';
}

/* =========================================================
   کیبوردها
   ========================================================= */

function userKeyboard($userId = null)
{
    $b = settings()['buttons'];
    $rows = [
        [['text' => $b['run_bot']]],
        [['text' => $b['account']], ['text' => $b['balance']]],
        [['text' => $b['guide']], ['text' => $b['ticket']]]
    ];
    if ($userId && isAdmin($userId)) {
        $rows[] = [['text' => $b['admin']]];
    }
    return ['keyboard' => $rows, 'resize_keyboard' => true];
}

function adminKeyboard()
{
    $a = settings()['admin_buttons'];
    return [
        'keyboard' => [
            [['text' => $a['users']], ['text' => $a['bots']]],
            [['text' => $a['finance']], ['text' => $a['payment_methods']]],
            [['text' => $a['plans']], ['text' => $a['guide']]],
            [['text' => $a['tickets']], ['text' => $a['broadcast']]],
            [['text' => $a['force_join']], ['text' => $a['customize']]],
            [['text' => $a['stats']], ['text' => $a['settings']]],
            [['text' => $a['admins']], ['text' => $a['back']]]
        ],
        'resize_keyboard' => true
    ];
}

function inlineBack($callback = 'main_back')
{
    return ['inline_keyboard' => [[['text' => '🔙 بازگشت', 'callback_data' => $callback]]]];
}

/* =========================================================
   عضویت اجباری
   ========================================================= */

function forceChannels()
{
    return settings()['force_join']['channels'] ?? [];
}

function checkForceJoin($userId)
{
    if (isAdmin($userId)) {
        return true;
    }

    $s = settings();
    if (empty($s['force_join']['enabled'])) {
        return true;
    }

    $channels = $s['force_join']['channels'] ?? [];
    foreach ($channels as $channel) {
        if (empty($channel['active'])) {
            continue;
        }

        $chatId = $channel['chat_id'];
        $res = bot('getChatMember', [
            'chat_id' => $chatId,
            'user_id' => $userId
        ]);

        if (!$res || empty($res['ok'])) {
            return false;
        }

        $status = $res['result']['status'] ?? 'left';
        if (in_array($status, ['left', 'kicked'], true)) {
            return false;
        }
    }

    return true;
}

function sendForceJoin($chatId)
{
    $s = settings();
    $rows = [];
    foreach ($s['force_join']['channels'] ?? [] as $channel) {
        if (empty($channel['active'])) {
            continue;
        }
        $title = $channel['title'] ?: 'عضویت';
        $link = $channel['link'] ?: 'https://t.me/' . ltrim((string)$channel['username'], '@');
        if ($link) {
            $rows[] = [[
                'text' => '📢 ' . $title,
                'url' => $link
            ]];
        }
    }
    $rows[] = [[
        'text' => '✅ بررسی عضویت',
        'callback_data' => 'force_check'
    ]];

    sendMessage($chatId, $s['texts']['force_join'], ['inline_keyboard' => $rows]);
}

/* =========================================================
   فایل، زیپ، وبهوک، ربات‌های ساخته‌شده
   ========================================================= */

function deleteDirectory($dir)
{
    if (!is_dir($dir)) {
        return;
    }
    foreach (array_diff(scandir($dir), ['.', '..']) as $file) {
        $path = $dir . '/' . $file;
        if (is_dir($path)) {
            deleteDirectory($path);
        } else {
            @unlink($path);
        }
    }
    @rmdir($dir);
}

function safeRelativePath($path)
{
    $path = str_replace('\\', '/', $path);
    $path = ltrim($path, '/');
    if ($path === '' || strpos($path, '..') !== false || strpos($path, ':') !== false || startsWith($path, '.')) {
        return false;
    }
    $parts = explode('/', $path);
    foreach ($parts as $p) {
        if ($p === '' || $p === '.' || $p === '..' || startsWith($p, '.')) {
            return false;
        }
    }
    return $path;
}

function sourceSecurityProblems($content)
{
    $s = settings();
    if (empty($s['strict_security'])) {
        return [];
    }

    $patterns = [
        '/\beval\s*\(/i' => 'eval()',
        '/\bassert\s*\(/i' => 'assert()',
        '/\bshell_exec\s*\(/i' => 'shell_exec()',
        '/\bexec\s*\(/i' => 'exec()',
        '/\bsystem\s*\(/i' => 'system()',
        '/\bpassthru\s*\(/i' => 'passthru()',
        '/\bproc_open\s*\(/i' => 'proc_open()',
        '/\bpopen\s*\(/i' => 'popen()',
        '/\bpcntl_exec\s*\(/i' => 'pcntl_exec()',
        '/\bbase64_decode\s*\(/i' => 'base64_decode()',
        '/\bgzinflate\s*\(/i' => 'gzinflate()',
        '/\bstr_rot13\s*\(/i' => 'str_rot13()',
        '/\bchmod\s*\(/i' => 'chmod()',
        '/\bchown\s*\(/i' => 'chown()',
        '/\bsymlink\s*\(/i' => 'symlink()',
        '/\bmove_uploaded_file\s*\(/i' => 'move_uploaded_file()'
    ];

    $bad = [];
    foreach ($patterns as $regex => $name) {
        if (preg_match($regex, $content)) {
            $bad[] = $name;
        }
    }
    return array_unique($bad);
}

function extractBotTokenFromText($content)
{
    $patterns = [
        '/define\s*\(\s*[\'\"]TOKEN[\'\"]\s*,\s*[\'\"]([^\'\"]+)[\'\"]\s*\)/i',
        '/define\s*\(\s*[\'\"]BOT_TOKEN[\'\"]\s*,\s*[\'\"]([^\'\"]+)[\'\"]\s*\)/i',
        '/const\s+TOKEN\s*=\s*[\'\"]([^\'\"]+)[\'\"]/i',
        '/\$token\s*=\s*[\'\"]([^\'\"]+)[\'\"]/i',
        '/\$botToken\s*=\s*[\'\"]([^\'\"]+)[\'\"]/i',
        '/\$API_KEY\s*=\s*[\'\"]([^\'\"]+)[\'\"]/i',
        '/([0-9]{8,15}:[A-Za-z0-9_\-]{30,100})/'
    ];

    foreach ($patterns as $pattern) {
        if (preg_match($pattern, $content, $m)) {
            return trim($m[1]);
        }
    }
    return false;
}

function scanZipForTokenAndProblems($zipPath, &$problems = [])
{
    if (!class_exists('ZipArchive')) {
        $problems[] = 'ZipArchive روی هاست فعال نیست';
        return false;
    }

    $zip = new ZipArchive();
    if ($zip->open($zipPath) !== true) {
        $problems[] = 'فایل ZIP باز نشد';
        return false;
    }

    $token = false;
    $phpFound = false;

    for ($i = 0; $i < $zip->numFiles; $i++) {
        $name = $zip->getNameIndex($i);
        $rel = safeRelativePath($name);
        if (!$rel || substr($rel, -1) === '/') {
            continue;
        }
        if (strtolower(pathinfo($rel, PATHINFO_EXTENSION)) !== 'php') {
            continue;
        }

        $phpFound = true;
        $content = $zip->getFromIndex($i);
        if ($content === false) {
            continue;
        }

        $bad = sourceSecurityProblems($content);
        if ($bad) {
            $problems[] = 'فایل ' . $rel . ' شامل موارد غیرمجاز است: ' . implode(', ', $bad);
        }

        if (!$token) {
            $token = extractBotTokenFromText($content);
        }
    }

    $zip->close();

    if (!$phpFound) {
        $problems[] = 'هیچ فایل PHP داخل ZIP پیدا نشد';
    }

    return $token;
}

function extractZipSafely($zipPath, $targetDir, &$mainFile = null, &$problems = [])
{
    $allowedExt = ['php', 'json', 'txt', 'html', 'htm', 'css', 'js', 'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp3', 'ogg', 'wav', 'pdf'];
    $zip = new ZipArchive();
    if ($zip->open($zipPath) !== true) {
        $problems[] = 'فایل ZIP باز نشد';
        return false;
    }

    $phpFiles = [];
    if (!is_dir($targetDir)) {
        mkdir($targetDir, 0755, true);
    }

    for ($i = 0; $i < $zip->numFiles; $i++) {
        $name = $zip->getNameIndex($i);
        $rel = safeRelativePath($name);
        if (!$rel || substr($rel, -1) === '/') {
            continue;
        }

        $ext = strtolower(pathinfo($rel, PATHINFO_EXTENSION));
        if (!in_array($ext, $allowedExt, true)) {
            continue;
        }

        $content = $zip->getFromIndex($i);
        if ($content === false) {
            continue;
        }

        if ($ext === 'php') {
            $bad = sourceSecurityProblems($content);
            if ($bad) {
                $problems[] = 'فایل ' . $rel . ' شامل موارد غیرمجاز است: ' . implode(', ', $bad);
                continue;
            }
            $phpFiles[] = $rel;
        }

        $dest = $targetDir . $rel;
        $dir = dirname($dest);
        if (!is_dir($dir)) {
            mkdir($dir, 0755, true);
        }
        file_put_contents($dest, $content);
    }

    $zip->close();

    if (!$phpFiles) {
        $problems[] = 'هیچ فایل PHP قابل استفاده‌ای استخراج نشد';
        return false;
    }

    $preferred = ['index.php', 'bot.php', 'main.php', 'webhook.php'];
    foreach ($preferred as $p) {
        foreach ($phpFiles as $f) {
            if (strtolower(basename($f)) === $p) {
                $mainFile = $f;
                return true;
            }
        }
    }

    $mainFile = $phpFiles[0];
    return true;
}

function botRecordByToken($token)
{
    foreach (bots() as $id => $bot) {
        if (($bot['token'] ?? '') === $token) {
            return $bot;
        }
    }
    return false;
}

function ownedBotCount($userId)
{
    $count = 0;
    foreach (bots() as $bot) {
        if ((int)($bot['owner_id'] ?? 0) === (int)$userId) {
            $count++;
        }
    }
    return $count;
}

function makeBotHash($token, $userId)
{
    return 'b_' . substr(sha1($token . '|' . $userId . '|' . microtime(true)), 0, 18);
}

function setBotWebhook($token, $url)
{
    return tgApi($token, 'setWebhook', [
        'url' => $url,
        'drop_pending_updates' => true
    ]);
}

function deleteBotWebhook($token)
{
    return tgApi($token, 'deleteWebhook', [
        'drop_pending_updates' => false
    ]);
}

function saveBotRecord($id, $data)
{
    $bots = bots();
    $bots[$id] = $data;
    saveBots($bots);
}

function deleteBotCompletely($id)
{
    $bots = bots();
    if (!isset($bots[$id])) {
        return false;
    }
    $bot = $bots[$id];
    deleteBotWebhook($bot['token']);
    $folder = BOTS_DIR . ($bot['folder'] ?? '');
    if (is_dir($folder)) {
        deleteDirectory($folder);
    }
    unset($bots[$id]);
    saveBots($bots);
    return true;
}

function setBotStatus($id, $active)
{
    $bots = bots();
    if (!isset($bots[$id])) {
        return false;
    }
    $bot = $bots[$id];
    if ($active) {
        $res = setBotWebhook($bot['token'], $bot['webhook_url']);
        if (!$res || empty($res['ok'])) {
            return false;
        }
        $bots[$id]['status'] = 'active';
        $bots[$id]['updated_at'] = now();
    } else {
        deleteBotWebhook($bot['token']);
        $bots[$id]['status'] = 'inactive';
        $bots[$id]['updated_at'] = now();
    }
    saveBots($bots);
    return true;
}

function createZipFromFolder($folder, $zipPath)
{
    if (!class_exists('ZipArchive') || !is_dir($folder)) {
        return false;
    }
    $zip = new ZipArchive();
    if ($zip->open($zipPath, ZipArchive::CREATE | ZipArchive::OVERWRITE) !== true) {
        return false;
    }
    $folder = rtrim($folder, '/') . '/';
    $it = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($folder, FilesystemIterator::SKIP_DOTS));
    foreach ($it as $file) {
        if ($file->isFile()) {
            $real = $file->getRealPath();
            $rel = substr($real, strlen(realpath($folder)) + 1);
            $zip->addFile($real, $rel);
        }
    }
    $zip->close();
    return true;
}

/* =========================================================
   صفحات کاربر
   ========================================================= */

function showStart($chatId, $user)
{
    $s = settings();
    $text = tpl($s['texts']['start'], [
        'name' => h(fullName($user))
    ]);
    sendMessage($chatId, $text, userKeyboard($user['id']));
}

function showRunBot($chatId, $userId)
{
    $s = settings();
    $u = getUser($userId);
    $botCount = ownedBotCount($userId);

    if ($botCount >= (int)$u['bot_limit']) {
        sendMessage($chatId, "⛔ سقف مجاز ساخت ربات برای حساب شما تکمیل شده است.\n\n📦 سقف شما: <b>{$u['bot_limit']}</b> عدد\n🤖 تعداد فعلی: <b>{$botCount}</b> عدد");
        return;
    }

    $canFree = (int)$u['free_used'] < (int)$s['free_bots'];
    $canPaid = (int)$u['balance'] >= (int)$s['bot_price'];

    if (!$canFree && !$canPaid) {
        sendMessage($chatId, tpl($s['texts']['not_enough_balance'], [
            'balance' => money($u['balance']),
            'price' => money($s['bot_price'])
        ]), [
            'inline_keyboard' => [
                [['text' => '💰 افزایش موجودی', 'callback_data' => 'user_balance']]
            ]
        ]);
        return;
    }

    setState($userId, 'wait_bot_file', []);
    sendMessage($chatId, tpl($s['texts']['run_intro'], [
        'price' => money($s['bot_price']),
        'free_total' => $s['free_bots'],
        'free_used' => $u['free_used'],
        'bot_count' => $botCount,
        'balance' => money($u['balance'])
    ]));
}

function showAccount($chatId, $userId)
{
    $s = settings();
    $u = getUser($userId);
    $openTickets = 0;
    foreach (tickets() as $ticket) {
        if ((int)$ticket['user_id'] === (int)$userId && $ticket['status'] === 'open') {
            $openTickets++;
        }
    }

    $text = tpl($s['texts']['account'], [
        'id' => $u['id'],
        'name' => h(fullName($u)),
        'username' => $u['username'] ? '@' . h($u['username']) : 'ندارد',
        'joined_at' => h($u['joined_at']),
        'last_seen' => h($u['last_seen']),
        'balance' => money($u['balance']),
        'total_paid' => money($u['total_paid']),
        'bot_count' => ownedBotCount($userId),
        'free_total' => $s['free_bots'],
        'free_used' => $u['free_used'],
        'vip' => !empty($u['is_vip']) ? 'کاربر ویژه 💎' : 'کاربر عادی 👤',
        'bot_limit' => $u['bot_limit'],
        'blocked' => !empty($u['blocked']) ? 'مسدود 🚫' : 'فعال 🟢',
        'open_tickets' => $openTickets
    ]);

    $b = $s['buttons'];
    sendMessage($chatId, $text, [
        'inline_keyboard' => [
            [['text' => $b['balance'], 'callback_data' => 'user_balance']],
            [['text' => $b['my_bots'], 'callback_data' => 'user_my_bots'], ['text' => $b['my_tickets'], 'callback_data' => 'ticket_list']],
            [['text' => $b['back'], 'callback_data' => 'main_back']]
        ]
    ]);
}

function showBalance($chatId, $userId)
{
    $s = settings();
    $u = getUser($userId);
    $methods = paymentMethods();
    $rows = [];
    foreach ($methods as $id => $m) {
        if (!empty($m['active'])) {
            $rows[] = [[
                'text' => $m['name'],
                'callback_data' => 'pay_method_' . $id
            ]];
        }
    }
    $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'main_back']];

    sendMessage($chatId, tpl($s['texts']['balance'], [
        'balance' => money($u['balance'])
    ]), ['inline_keyboard' => $rows]);
}

function showGuide($chatId)
{
    $s = settings();
    sendMessage($chatId, $s['texts']['guide'], inlineBack('main_back'));
}

function showUserBots($chatId, $userId)
{
    $rows = [];
    $text = "🤖 <b>ربات‌های من</b>\n\n";
    $i = 1;
    foreach (bots() as $id => $bot) {
        if ((int)$bot['owner_id'] !== (int)$userId) {
            continue;
        }
        $status = $bot['status'] === 'active' ? 'فعال ✅' : 'غیرفعال ⛔';
        $text .= $i . ". @" . h($bot['username']) . "\n";
        $text .= "   📛 " . h($bot['name']) . "\n";
        $text .= "   📌 {$status}\n";
        $text .= "   📅 " . h($bot['created_at']) . "\n\n";
        $rows[] = [[
            'text' => '🔎 @' . $bot['username'],
            'callback_data' => 'user_bot_view_' . $id
        ]];
        $i++;
    }
    if ($i === 1) {
        $text .= "📭 هنوز رباتی نساخته‌اید.";
    }
    $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'main_back']];
    sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
}

/* =========================================================
   پردازش آپلود و ران کردن ربات
   ========================================================= */

function handleBotUpload($chatId, $userId, $msg)
{
    if (empty($msg['document'])) {
        sendMessage($chatId, "❌ لطفاً فایل PHP یا ZIP ارسال کنید.");
        return;
    }

    $s = settings();
    $u = getUser($userId);
    $doc = $msg['document'];
    $fileName = $doc['file_name'] ?? 'file';
    $fileSize = $doc['file_size'] ?? 0;
    $ext = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
    $maxBytes = (int)$s['max_file_mb'] * 1024 * 1024;

    if ($fileSize > $maxBytes) {
        sendMessage($chatId, "❌ حجم فایل بیشتر از حد مجاز است.\n\n📦 حد مجاز: <b>" . formatBytes($maxBytes) . "</b>");
        return;
    }

    if (!in_array($ext, ['php', 'zip'], true)) {
        sendMessage($chatId, "❌ فقط فایل‌های PHP و ZIP مجاز هستند.");
        return;
    }

    $botCount = ownedBotCount($userId);
    if ($botCount >= (int)$u['bot_limit']) {
        sendMessage($chatId, "⛔ سقف مجاز ساخت ربات برای حساب شما تکمیل شده است.");
        clearState($userId);
        return;
    }

    $canFree = (int)$u['free_used'] < (int)$s['free_bots'];
    $canPaid = (int)$u['balance'] >= (int)$s['bot_price'];
    if (!$canFree && !$canPaid) {
        sendMessage($chatId, tpl($s['texts']['not_enough_balance'], [
            'balance' => money($u['balance']),
            'price' => money($s['bot_price'])
        ]));
        clearState($userId);
        return;
    }

    sendMessage($chatId, $s['texts']['upload_processing']);

    $content = downloadTelegramFile($doc['file_id']);
    if ($content === false) {
        sendMessage($chatId, "❌ خطا در دانلود فایل از تلگرام.");
        return;
    }

    $token = false;
    $problems = [];
    $tempZip = null;
    $singlePhpContent = null;
    $sourceType = $ext;

    if ($ext === 'php') {
        $singlePhpContent = $content;
        $bad = sourceSecurityProblems($singlePhpContent);
        if ($bad) {
            sendMessage($chatId, "❌ فایل شامل کدهای غیرمجاز است:\n<code>" . h(implode(', ', $bad)) . "</code>");
            return;
        }
        $token = extractBotTokenFromText($singlePhpContent);
    } else {
        $tempZip = TEMP_DIR . newId('upload') . '.zip';
        file_put_contents($tempZip, $content);
        $token = scanZipForTokenAndProblems($tempZip, $problems);
        if ($problems) {
            @unlink($tempZip);
            sendMessage($chatId, "❌ مشکل در فایل ZIP:\n\n<code>" . h(implode("\n", $problems)) . "</code>");
            return;
        }
    }

    if (!$token) {
        if ($tempZip) @unlink($tempZip);
        sendMessage($chatId, "❌ توکن ربات داخل فایل پیدا نشد.\n\nفرمت‌های قابل قبول:\n<code>define('TOKEN', '123:ABC');</code>\n<code>\$token = '123:ABC';</code>");
        return;
    }

    if ($token === MAIN_BOT_TOKEN) {
        if ($tempZip) @unlink($tempZip);
        sendMessage($chatId, "❌ توکن فایل نباید توکن ربات اصلی باشد.");
        return;
    }

    if (botRecordByToken($token)) {
        if ($tempZip) @unlink($tempZip);
        sendMessage($chatId, "⚠️ این ربات قبلاً در سیستم ثبت شده است.");
        return;
    }

    sendMessage($chatId, "🔍 در حال بررسی توکن ربات...");
    $info = tgApi($token, 'getMe');
    if (!$info || empty($info['ok'])) {
        if ($tempZip) @unlink($tempZip);
        sendMessage($chatId, "❌ توکن داخل فایل نامعتبر است.");
        return;
    }

    $botId = makeBotHash($token, $userId);
    $folderName = $botId;
    $folder = BOTS_DIR . $folderName . '/';
    $mainFile = 'index.php';

    if (!is_dir($folder)) {
        mkdir($folder, 0755, true);
    }

    if ($ext === 'php') {
        file_put_contents($folder . 'index.php', $singlePhpContent);
    } else {
        $extractProblems = [];
        $ok = extractZipSafely($tempZip, $folder, $mainFile, $extractProblems);
        @unlink($tempZip);
        if (!$ok || $extractProblems) {
            deleteDirectory($folder);
            sendMessage($chatId, "❌ خطا در استخراج ZIP:\n<code>" . h(implode("\n", $extractProblems)) . "</code>");
            return;
        }
    }

    $webhookUrl = getBaseUrl() . 'bots/' . rawurlencode($folderName) . '/' . str_replace('%2F', '/', rawurlencode($mainFile));

    sendMessage($chatId, "⚙️ در حال تنظیم Webhook...");
    $webhook = setBotWebhook($token, $webhookUrl);
    if (!$webhook || empty($webhook['ok'])) {
        deleteDirectory($folder);
        $desc = $webhook['description'] ?? 'خطای نامشخص';
        sendMessage($chatId, "❌ وبهوک تنظیم نشد.\n\nخطا:\n<code>" . h($desc) . "</code>\n\nنکته: هاست باید SSL معتبر داشته باشد و مسیر فایل از بیرون باز شود.");
        return;
    }

    $chargeType = 'free';
    if ($canFree) {
        updateUser($userId, ['free_used' => (int)$u['free_used'] + 1]);
    } else {
        changeBalance($userId, -1 * (int)$s['bot_price'], 'کسر بابت ران کردن ربات @' . ($info['result']['username'] ?? ''), 'run_bot', [
            'bot_id' => $botId
        ]);
        $chargeType = 'paid';
    }

    $record = [
        'id' => $botId,
        'owner_id' => (int)$userId,
        'token' => $token,
        'telegram_bot_id' => $info['result']['id'] ?? '',
        'username' => $info['result']['username'] ?? '',
        'name' => $info['result']['first_name'] ?? '',
        'folder' => $folderName,
        'main_file' => $mainFile,
        'source_type' => $sourceType,
        'webhook_url' => $webhookUrl,
        'status' => 'active',
        'charge_type' => $chargeType,
        'price' => $chargeType === 'paid' ? (int)$s['bot_price'] : 0,
        'created_at' => now(),
        'updated_at' => now()
    ];
    saveBotRecord($botId, $record);
    clearState($userId);

    $text = tpl($s['texts']['upload_success'], [
        'username' => h($record['username']),
        'name' => h($record['name']),
        'bot_id' => h($record['telegram_bot_id']),
        'main_file' => h($record['main_file']),
        'webhook_url' => h($record['webhook_url'])
    ]);

    sendMessage($chatId, $text, [
        'inline_keyboard' => [
            [['text' => '🚀 رفتن به ربات', 'url' => 'https://t.me/' . $record['username']]],
            [['text' => '📥 دانلود فایل', 'callback_data' => 'user_bot_download_' . $botId]],
            [['text' => '🗑️ حذف ربات', 'callback_data' => 'user_bot_delete_' . $botId]]
        ]
    ]);
}

/* =========================================================
   پرداخت و افزایش موجودی
   ========================================================= */

function createPaymentRequest($userId, $methodId, $amount, $msg)
{
    $payments = payments();
    $id = newId('pay');
    $payments[$id] = [
        'id' => $id,
        'user_id' => (int)$userId,
        'method_id' => $methodId,
        'amount' => (int)$amount,
        'status' => 'pending',
        'receipt_chat_id' => $msg['chat']['id'],
        'receipt_message_id' => $msg['message_id'],
        'created_at' => now(),
        'updated_at' => now(),
        'admin_id' => null,
        'admin_note' => ''
    ];
    savePayments($payments);
    return $id;
}

function notifyAdminsPayment($paymentId)
{
    $payments = payments();
    if (!isset($payments[$paymentId])) {
        return;
    }
    $p = $payments[$paymentId];
    $u = getUser($p['user_id']);
    $methods = paymentMethods();
    $methodName = $methods[$p['method_id']]['name'] ?? 'نامشخص';

    $text = "💳 <b>درخواست افزایش موجودی</b>\n\n";
    $text .= "🆔 شماره: <code>{$paymentId}</code>\n";
    $text .= "👤 کاربر: " . h(fullName($u)) . "\n";
    $text .= "🔗 یوزرنیم: " . ($u['username'] ? '@' . h($u['username']) : 'ندارد') . "\n";
    $text .= "🆔 آیدی: <code>{$u['id']}</code>\n";
    $text .= "💰 مبلغ: <b>" . money($p['amount']) . "</b>\n";
    $text .= "💳 روش: " . h($methodName) . "\n";
    $text .= "📅 تاریخ: " . h($p['created_at']) . "\n\n";
    $text .= "رسید کاربر در پیام بعدی کپی می‌شود.";

    $kb = [
        'inline_keyboard' => [
            [
                ['text' => '✅ تایید', 'callback_data' => 'pay_approve_' . $paymentId],
                ['text' => '❌ رد', 'callback_data' => 'pay_reject_' . $paymentId]
            ]
        ]
    ];

    foreach (admins() as $admin) {
        $aid = $admin['id'];
        sendMessage($aid, $text, $kb);
        copyMsg($aid, $p['receipt_chat_id'], $p['receipt_message_id']);
    }
}

function approvePayment($paymentId, $adminId)
{
    $payments = payments();
    if (!isset($payments[$paymentId])) {
        return [false, 'درخواست پیدا نشد'];
    }
    if ($payments[$paymentId]['status'] !== 'pending') {
        return [false, 'این درخواست قبلاً بررسی شده است'];
    }

    $p = $payments[$paymentId];
    $u = getUser($p['user_id']);
    updateUser($p['user_id'], [
        'balance' => (int)$u['balance'] + (int)$p['amount'],
        'total_paid' => (int)$u['total_paid'] + (int)$p['amount']
    ]);
    addTransaction($p['user_id'], 'payment_approved', $p['amount'], 'تایید شارژ کیف پول', ['payment_id' => $paymentId]);

    $payments[$paymentId]['status'] = 'approved';
    $payments[$paymentId]['updated_at'] = now();
    $payments[$paymentId]['admin_id'] = (int)$adminId;
    savePayments($payments);

    sendMessage($p['user_id'], "✅ پرداخت شما تایید شد.\n\n💰 مبلغ: <b>" . money($p['amount']) . "</b>\n💳 موجودی جدید: <b>" . money(getUser($p['user_id'])['balance']) . "</b>");
    return [true, 'پرداخت تایید شد'];
}

function rejectPayment($paymentId, $adminId)
{
    $payments = payments();
    if (!isset($payments[$paymentId])) {
        return [false, 'درخواست پیدا نشد'];
    }
    if ($payments[$paymentId]['status'] !== 'pending') {
        return [false, 'این درخواست قبلاً بررسی شده است'];
    }
    $payments[$paymentId]['status'] = 'rejected';
    $payments[$paymentId]['updated_at'] = now();
    $payments[$paymentId]['admin_id'] = (int)$adminId;
    savePayments($payments);

    sendMessage($payments[$paymentId]['user_id'], "❌ پرداخت شما توسط مدیریت رد شد.\n\n🆔 شماره درخواست: <code>{$paymentId}</code>");
    return [true, 'پرداخت رد شد'];
}

/* =========================================================
   تیکت‌ها
   ========================================================= */

function showTicketMenu($chatId)
{
    $s = settings();
    sendMessage($chatId, $s['texts']['ticket_intro'], [
        'inline_keyboard' => [
            [['text' => '➕ ایجاد تیکت جدید', 'callback_data' => 'ticket_new']],
            [['text' => '📂 تیکت‌های من', 'callback_data' => 'ticket_list']],
            [['text' => '🔙 بازگشت', 'callback_data' => 'main_back']]
        ]
    ]);
}

function createTicket($userId, $subject, $msg)
{
    $tickets = tickets();
    $id = newId('t');
    $text = $msg['text'] ?? ($msg['caption'] ?? 'پیام غیرمتنی');
    $tickets[$id] = [
        'id' => $id,
        'user_id' => (int)$userId,
        'subject' => $subject,
        'status' => 'open',
        'messages' => [[
            'from' => 'user',
            'user_id' => (int)$userId,
            'text' => $text,
            'chat_id' => $msg['chat']['id'],
            'message_id' => $msg['message_id'],
            'created_at' => now()
        ]],
        'created_at' => now(),
        'updated_at' => now()
    ];
    saveTickets($tickets);
    return $id;
}

function notifyAdminsTicket($ticketId)
{
    $tickets = tickets();
    if (!isset($tickets[$ticketId])) {
        return;
    }
    $t = $tickets[$ticketId];
    $u = getUser($t['user_id']);
    $last = end($t['messages']);

    $text = "🎫 <b>تیکت جدید / پیام جدید</b>\n\n";
    $text .= "🆔 تیکت: <code>{$ticketId}</code>\n";
    $text .= "👤 کاربر: " . h(fullName($u)) . "\n";
    $text .= "🔗 یوزرنیم: " . ($u['username'] ? '@' . h($u['username']) : 'ندارد') . "\n";
    $text .= "🆔 آیدی: <code>{$u['id']}</code>\n";
    $text .= "📌 موضوع: " . h($t['subject']) . "\n";
    $text .= "📅 تاریخ: " . h($t['updated_at']) . "\n\n";
    $text .= "📝 پیام:\n" . h($last['text']);

    $kb = [
        'inline_keyboard' => [
            [['text' => '👁 مشاهده تیکت', 'callback_data' => 'admin_ticket_view_' . $ticketId]],
            [['text' => '✍️ پاسخ', 'callback_data' => 'admin_ticket_reply_' . $ticketId], ['text' => '🔒 بستن', 'callback_data' => 'admin_ticket_close_' . $ticketId]]
        ]
    ];

    foreach (admins() as $admin) {
        sendMessage($admin['id'], $text, $kb);
        if (!empty($last['chat_id']) && !empty($last['message_id'])) {
            copyMsg($admin['id'], $last['chat_id'], $last['message_id']);
        }
    }
}

function showTicketList($chatId, $userId)
{
    $rows = [];
    $text = "📂 <b>تیکت‌های شما</b>\n\n";
    $i = 1;
    foreach (tickets() as $id => $t) {
        if ((int)$t['user_id'] !== (int)$userId) {
            continue;
        }
        $status = $t['status'] === 'open' ? 'باز 🟢' : 'بسته 🔒';
        $text .= "{$i}. <code>{$id}</code> | " . h($t['subject']) . " | {$status}\n";
        $rows[] = [[
            'text' => "🎫 {$id}",
            'callback_data' => 'ticket_view_' . $id
        ]];
        $i++;
    }
    if ($i === 1) {
        $text .= "📭 تیکتی وجود ندارد.";
    }
    $rows[] = [['text' => '➕ تیکت جدید', 'callback_data' => 'ticket_new']];
    $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'main_back']];
    sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
}

function ticketSummaryText($ticketId, $adminView = false)
{
    $tickets = tickets();
    if (!isset($tickets[$ticketId])) {
        return '❌ تیکت پیدا نشد.';
    }
    $t = $tickets[$ticketId];
    $u = getUser($t['user_id']);
    $status = $t['status'] === 'open' ? 'باز 🟢' : 'بسته 🔒';
    $text = "🎫 <b>تیکت {$ticketId}</b>\n\n";
    if ($adminView) {
        $text .= "👤 کاربر: " . h(fullName($u)) . "\n";
        $text .= "🆔 آیدی: <code>{$u['id']}</code>\n";
        $text .= "🔗 یوزرنیم: " . ($u['username'] ? '@' . h($u['username']) : 'ندارد') . "\n";
    }
    $text .= "📌 موضوع: " . h($t['subject']) . "\n";
    $text .= "📍 وضعیت: {$status}\n";
    $text .= "📅 ایجاد: " . h($t['created_at']) . "\n";
    $text .= "🕒 بروزرسانی: " . h($t['updated_at']) . "\n\n";
    $text .= "━━━━━━━━━━━━━━\n";

    $messages = array_slice($t['messages'], -8);
    foreach ($messages as $m) {
        $who = $m['from'] === 'admin' ? '👑 پشتیبانی' : '👤 کاربر';
        $text .= "{$who} | " . h($m['created_at']) . "\n";
        $text .= h($m['text']) . "\n\n";
    }
    return $text;
}

function appendTicketMessage($ticketId, $from, $userId, $msg)
{
    $tickets = tickets();
    if (!isset($tickets[$ticketId])) {
        return false;
    }
    if ($tickets[$ticketId]['status'] !== 'open') {
        return false;
    }
    $text = $msg['text'] ?? ($msg['caption'] ?? 'پیام غیرمتنی');
    $tickets[$ticketId]['messages'][] = [
        'from' => $from,
        'user_id' => (int)$userId,
        'text' => $text,
        'chat_id' => $msg['chat']['id'],
        'message_id' => $msg['message_id'],
        'created_at' => now()
    ];
    $tickets[$ticketId]['updated_at'] = now();
    saveTickets($tickets);
    return true;
}

/* =========================================================
   پنل مدیریت: نمایش‌ها
   ========================================================= */

function showAdminPanel($chatId)
{
    $text = "👑 <b>مدیریت ویژه</b>\n\n";
    $text .= "به پنل مدیریت کامل خوش آمدید.\n";
    $text .= "از دکمه‌های پایین بخش مورد نظر را انتخاب کنید.";
    sendMessage($chatId, $text, adminKeyboard());
}

function showStats($chatId)
{
    $users = users();
    $bots = bots();
    $payments = payments();
    $tickets = tickets();

    $vip = $blocked = 0;
    foreach ($users as $u) {
        if (!empty($u['is_vip'])) $vip++;
        if (!empty($u['blocked'])) $blocked++;
    }

    $activeBots = $inactiveBots = 0;
    foreach ($bots as $b) {
        if (($b['status'] ?? '') === 'active') $activeBots++;
        else $inactiveBots++;
    }

    $pendingPay = $income = 0;
    foreach ($payments as $p) {
        if ($p['status'] === 'pending') $pendingPay++;
        if ($p['status'] === 'approved') $income += (int)$p['amount'];
    }

    $openTickets = 0;
    foreach ($tickets as $t) {
        if ($t['status'] === 'open') $openTickets++;
    }

    $text = "📊 <b>آمار کلی ربات</b>\n\n";
    $text .= "👥 کل کاربران: <b>" . count($users) . "</b>\n";
    $text .= "💎 کاربران ویژه: <b>{$vip}</b>\n";
    $text .= "🚫 کاربران مسدود: <b>{$blocked}</b>\n\n";
    $text .= "🤖 کل ربات‌ها: <b>" . count($bots) . "</b>\n";
    $text .= "✅ ربات‌های فعال: <b>{$activeBots}</b>\n";
    $text .= "⛔ ربات‌های غیرفعال: <b>{$inactiveBots}</b>\n\n";
    $text .= "💰 درآمد تایید شده: <b>" . money($income) . "</b>\n";
    $text .= "📥 شارژهای در انتظار: <b>{$pendingPay}</b>\n";
    $text .= "🎫 تیکت‌های باز: <b>{$openTickets}</b>\n\n";
    $text .= "🕒 آخرین بروزرسانی: " . now();

    sendMessage($chatId, $text, inlineBack('admin_back'));
}

function showAdminUsersMenu($chatId)
{
    sendMessage($chatId, "👥 <b>مدیریت کاربران</b>\n\nآیدی عددی کاربر را ارسال کنید یا از گزینه‌های زیر استفاده کنید.", [
        'inline_keyboard' => [
            [['text' => '🔍 جستجوی کاربر با آیدی', 'callback_data' => 'admin_user_search']],
            [['text' => '📋 لیست ۲۰ کاربر اخیر', 'callback_data' => 'admin_user_recent']],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']]
        ]
    ]);
}

function adminUserProfileText($userId)
{
    $u = getUser($userId);
    $text = "👤 <b>پروفایل کاربر</b>\n\n";
    $text .= "🆔 آیدی: <code>{$u['id']}</code>\n";
    $text .= "👤 نام: " . h(fullName($u)) . "\n";
    $text .= "🔗 یوزرنیم: " . ($u['username'] ? '@' . h($u['username']) : 'ندارد') . "\n";
    $text .= "💰 موجودی: <b>" . money($u['balance']) . "</b>\n";
    $text .= "📊 مجموع پرداختی: <b>" . money($u['total_paid']) . "</b>\n";
    $text .= "🤖 تعداد ربات‌ها: <b>" . ownedBotCount($userId) . "</b>\n";
    $text .= "🎁 رایگان استفاده‌شده: <b>{$u['free_used']}</b>\n";
    $text .= "📦 سقف ربات: <b>{$u['bot_limit']}</b>\n";
    $text .= "💎 ویژه: " . (!empty($u['is_vip']) ? 'بله ✅' : 'خیر ❌') . "\n";
    $text .= "🚫 مسدود: " . (!empty($u['blocked']) ? 'بله 🚫' : 'خیر ✅') . "\n";
    $text .= "📅 عضویت: " . h($u['joined_at']) . "\n";
    $text .= "🕒 آخرین فعالیت: " . h($u['last_seen']) . "\n";
    return $text;
}

function showAdminUserProfile($chatId, $userId)
{
    $u = getUser($userId);
    $kb = [
        'inline_keyboard' => [
            [['text' => '➕ افزایش موجودی', 'callback_data' => 'admin_user_addbal_' . $userId], ['text' => '➖ کاهش موجودی', 'callback_data' => 'admin_user_subbal_' . $userId]],
            [['text' => !empty($u['blocked']) ? '✅ آزاد کردن' : '🚫 مسدود کردن', 'callback_data' => 'admin_user_toggleblock_' . $userId]],
            [['text' => !empty($u['is_vip']) ? '❌ حذف ویژه' : '💎 ویژه کردن', 'callback_data' => 'admin_user_togglevip_' . $userId]],
            [['text' => '📦 تنظیم سقف ربات', 'callback_data' => 'admin_user_setlimit_' . $userId]],
            [['text' => '🤖 ربات‌های کاربر', 'callback_data' => 'admin_user_bots_' . $userId], ['text' => '🎫 تیکت‌های کاربر', 'callback_data' => 'admin_user_tickets_' . $userId]],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_users_menu']]
        ]
    ];
    sendMessage($chatId, adminUserProfileText($userId), $kb);
}

function showAdminBotsMenu($chatId)
{
    $all = bots();
    $rows = [];
    $text = "🤖 <b>مدیریت ربات‌ها</b>\n\n";
    $text .= "تعداد کل: <b>" . count($all) . "</b>\n\n";
    $i = 1;
    foreach (array_reverse($all, true) as $id => $bot) {
        if ($i > 20) break;
        $status = $bot['status'] === 'active' ? '✅' : '⛔';
        $rows[] = [[
            'text' => $status . ' @' . ($bot['username'] ?: $id),
            'callback_data' => 'admin_bot_view_' . $id
        ]];
        $i++;
    }
    if (!$rows) {
        $text .= "📭 هنوز رباتی ثبت نشده است.";
    }
    $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']];
    sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
}

function showAdminBotView($chatId, $botId)
{
    $all = bots();
    if (!isset($all[$botId])) {
        sendMessage($chatId, '❌ ربات پیدا نشد.');
        return;
    }
    $b = $all[$botId];
    $u = getUser($b['owner_id']);
    $status = $b['status'] === 'active' ? 'فعال ✅' : 'غیرفعال ⛔';
    $text = "🤖 <b>اطلاعات ربات</b>\n\n";
    $text .= "🆔 شناسه سیستم: <code>{$botId}</code>\n";
    $text .= "🤖 یوزرنیم: @" . h($b['username']) . "\n";
    $text .= "📛 نام: " . h($b['name']) . "\n";
    $text .= "📌 وضعیت: {$status}\n";
    $text .= "👤 صاحب: " . h(fullName($u)) . "\n";
    $text .= "🆔 آیدی صاحب: <code>{$u['id']}</code>\n";
    $text .= "📁 فایل اصلی: <code>" . h($b['main_file']) . "</code>\n";
    $text .= "🌐 وبهوک:\n<code>" . h($b['webhook_url']) . "</code>\n";
    $text .= "💰 نوع ساخت: " . ($b['charge_type'] === 'free' ? 'رایگان 🎁' : 'پرداختی 💰') . "\n";
    $text .= "📅 ساخت: " . h($b['created_at']) . "\n";

    $kb = [
        'inline_keyboard' => [
            [['text' => '🔄 تنظیم مجدد Webhook', 'callback_data' => 'admin_bot_rehook_' . $botId]],
            [['text' => $b['status'] === 'active' ? '⛔ غیرفعال کردن' : '✅ فعال کردن', 'callback_data' => 'admin_bot_toggle_' . $botId]],
            [['text' => '📥 دانلود فایل', 'callback_data' => 'admin_bot_download_' . $botId]],
            [['text' => '👤 مشاهده صاحب', 'callback_data' => 'admin_user_view_' . $u['id']]],
            [['text' => '🗑 حذف کامل', 'callback_data' => 'admin_bot_delete_' . $botId]],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_bots_menu']]
        ]
    ];
    sendMessage($chatId, $text, $kb);
}

function showFinanceMenu($chatId)
{
    sendMessage($chatId, "💰 <b>مدیریت مالی</b>\n\nبخش مورد نظر را انتخاب کنید.", [
        'inline_keyboard' => [
            [['text' => '📥 درخواست‌های شارژ', 'callback_data' => 'finance_pending']],
            [['text' => '📜 تاریخچه تراکنش‌ها', 'callback_data' => 'finance_transactions']],
            [['text' => '💵 مجموع درآمد', 'callback_data' => 'finance_income']],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']]
        ]
    ]);
}

function showPendingPayments($chatId)
{
    $rows = [];
    $text = "📥 <b>درخواست‌های شارژ در انتظار</b>\n\n";
    $i = 1;
    foreach (array_reverse(payments(), true) as $id => $p) {
        if ($p['status'] !== 'pending') continue;
        $u = getUser($p['user_id']);
        $text .= "{$i}. <code>{$id}</code> | " . h(fullName($u)) . " | " . money($p['amount']) . "\n";
        $rows[] = [[
            'text' => '💳 ' . money($p['amount']) . ' | ' . ($u['username'] ? '@' . $u['username'] : $u['id']),
            'callback_data' => 'pay_view_' . $id
        ]];
        $i++;
        if ($i > 20) break;
    }
    if ($i === 1) {
        $text .= "📭 درخواست در انتظاری وجود ندارد.";
    }
    $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'finance_menu']];
    sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
}

function showPaymentView($chatId, $paymentId)
{
    $pays = payments();
    if (!isset($pays[$paymentId])) {
        sendMessage($chatId, '❌ درخواست پیدا نشد.');
        return;
    }
    $p = $pays[$paymentId];
    $u = getUser($p['user_id']);
    $methods = paymentMethods();
    $methodName = $methods[$p['method_id']]['name'] ?? 'نامشخص';
    $text = "💳 <b>جزئیات درخواست شارژ</b>\n\n";
    $text .= "🆔 شماره: <code>{$paymentId}</code>\n";
    $text .= "👤 کاربر: " . h(fullName($u)) . "\n";
    $text .= "🆔 آیدی: <code>{$u['id']}</code>\n";
    $text .= "💰 مبلغ: <b>" . money($p['amount']) . "</b>\n";
    $text .= "💳 روش: " . h($methodName) . "\n";
    $text .= "📌 وضعیت: " . h($p['status']) . "\n";
    $text .= "📅 تاریخ: " . h($p['created_at']) . "\n";
    $kb = [
        'inline_keyboard' => [
            [['text' => '✅ تایید', 'callback_data' => 'pay_approve_' . $paymentId], ['text' => '❌ رد', 'callback_data' => 'pay_reject_' . $paymentId]],
            [['text' => '🧾 ارسال رسید', 'callback_data' => 'pay_receipt_' . $paymentId]],
            [['text' => '🔙 بازگشت', 'callback_data' => 'finance_pending']]
        ]
    ];
    sendMessage($chatId, $text, $kb);
}

function showPaymentMethodsAdmin($chatId)
{
    $methods = paymentMethods();
    $text = "💳 <b>روش‌های پرداخت</b>\n\n";
    $rows = [];
    foreach ($methods as $id => $m) {
        $status = !empty($m['active']) ? '✅' : '⛔';
        $text .= "{$status} " . h($m['name']) . "\n";
        $rows[] = [[
            'text' => $status . ' ' . $m['name'],
            'callback_data' => 'pm_view_' . $id
        ]];
    }
    $rows[] = [['text' => '➕ افزودن روش پرداخت', 'callback_data' => 'pm_add']];
    $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']];
    sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
}

function showPaymentMethodView($chatId, $id)
{
    $methods = paymentMethods();
    if (!isset($methods[$id])) {
        sendMessage($chatId, '❌ روش پرداخت پیدا نشد.');
        return;
    }
    $m = $methods[$id];
    $text = "💳 <b>روش پرداخت</b>\n\n";
    $text .= "🆔 شناسه: <code>{$id}</code>\n";
    $text .= "📛 نام: " . h($m['name']) . "\n";
    $text .= "📌 وضعیت: " . (!empty($m['active']) ? 'فعال ✅' : 'غیرفعال ⛔') . "\n\n";
    $text .= "📝 توضیحات:\n" . ($m['details'] ?? '');
    sendMessage($chatId, $text, [
        'inline_keyboard' => [
            [['text' => '✏️ ویرایش نام', 'callback_data' => 'pm_edit_name_' . $id], ['text' => '📝 ویرایش توضیحات', 'callback_data' => 'pm_edit_details_' . $id]],
            [['text' => !empty($m['active']) ? '⛔ غیرفعال کردن' : '✅ فعال کردن', 'callback_data' => 'pm_toggle_' . $id]],
            [['text' => '🗑 حذف', 'callback_data' => 'pm_delete_' . $id]],
            [['text' => '🔙 بازگشت', 'callback_data' => 'payment_methods_menu']]
        ]
    ]);
}

function showPlansMenu($chatId)
{
    $s = settings();
    $text = "📦 <b>تنظیم پلن‌ها و قیمت‌ها</b>\n\n";
    $text .= "💰 قیمت ران کردن هر ربات: <b>" . money($s['bot_price']) . "</b>\n";
    $text .= "🎁 تعداد ربات رایگان: <b>{$s['free_bots']}</b>\n";
    $text .= "📦 سقف پیش‌فرض ربات کاربر: <b>{$s['default_bot_limit']}</b>\n";
    $text .= "📁 حداکثر حجم فایل: <b>{$s['max_file_mb']} MB</b>\n";
    $text .= "🛡 بررسی امنیتی سورس: " . (!empty($s['strict_security']) ? 'روشن ✅' : 'خاموش ⛔') . "\n";
    sendMessage($chatId, $text, [
        'inline_keyboard' => [
            [['text' => '💰 تغییر قیمت ران', 'callback_data' => 'set_bot_price']],
            [['text' => '🎁 تغییر سهمیه رایگان', 'callback_data' => 'set_free_bots']],
            [['text' => '📦 تغییر سقف پیش‌فرض', 'callback_data' => 'set_default_limit']],
            [['text' => '📁 تغییر حداکثر حجم فایل', 'callback_data' => 'set_max_file']],
            [['text' => !empty($s['strict_security']) ? '⛔ خاموش کردن بررسی امنیتی' : '✅ روشن کردن بررسی امنیتی', 'callback_data' => 'toggle_strict_security']],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']]
        ]
    ]);
}

function showForceJoinAdmin($chatId)
{
    $s = settings();
    $enabled = !empty($s['force_join']['enabled']);
    $text = "🔐 <b>عضویت اجباری</b>\n\n";
    $text .= "📌 وضعیت: " . ($enabled ? 'روشن ✅' : 'خاموش ⛔') . "\n";
    $text .= "📢 تعداد کانال/گروه: <b>" . count($s['force_join']['channels']) . "</b>\n\n";
    foreach ($s['force_join']['channels'] as $id => $ch) {
        $text .= (!empty($ch['active']) ? '✅' : '⛔') . ' ' . h($ch['title']) . " | <code>" . h($ch['chat_id']) . "</code>\n";
    }

    sendMessage($chatId, $text, [
        'inline_keyboard' => [
            [['text' => $enabled ? '⛔ خاموش کردن' : '✅ روشن کردن', 'callback_data' => 'fj_toggle']],
            [['text' => '➕ افزودن کانال / گروه', 'callback_data' => 'fj_add']],
            [['text' => '📋 لیست و مدیریت', 'callback_data' => 'fj_list']],
            [['text' => '👁 تست عضویت اجباری', 'callback_data' => 'fj_test']],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']]
        ]
    ]);
}

function showForceJoinList($chatId)
{
    $channels = settings()['force_join']['channels'] ?? [];
    $rows = [];
    $text = "📋 <b>لیست عضویت اجباری</b>\n\n";
    foreach ($channels as $id => $ch) {
        $status = !empty($ch['active']) ? '✅' : '⛔';
        $text .= "{$status} " . h($ch['title']) . " | <code>" . h($ch['chat_id']) . "</code>\n";
        $rows[] = [[
            'text' => $status . ' ' . $ch['title'],
            'callback_data' => 'fj_view_' . $id
        ]];
    }
    if (!$channels) {
        $text .= "📭 موردی ثبت نشده است.";
    }
    $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'force_join_menu']];
    sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
}

function showCustomizeMenu($chatId)
{
    sendMessage($chatId, "🎨 <b>شخصی‌سازی متن‌ها و دکمه‌ها</b>\n\nهر متن، عنوان، اسم دکمه و پیام را از اینجا تغییر دهید.", [
        'inline_keyboard' => [
            [['text' => '🔘 دکمه‌های منوی کاربر', 'callback_data' => 'cust_buttons_user']],
            [['text' => '👑 دکمه‌های پنل مدیریت', 'callback_data' => 'cust_buttons_admin']],
            [['text' => '📝 متن‌های اصلی ربات', 'callback_data' => 'cust_texts']],
            [['text' => '🔄 بازگردانی پیش‌فرض', 'callback_data' => 'cust_reset_confirm']],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']]
        ]
    ]);
}

function showCustomizeList($chatId, $type)
{
    $s = settings();
    if ($type === 'user') {
        $items = $s['buttons'];
        $prefix = 'cust_edit_user_';
        $title = '🔘 دکمه‌های منوی کاربر';
    } elseif ($type === 'admin') {
        $items = $s['admin_buttons'];
        $prefix = 'cust_edit_admin_';
        $title = '👑 دکمه‌های پنل مدیریت';
    } else {
        $items = $s['texts'];
        $prefix = 'cust_edit_text_';
        $title = '📝 متن‌های اصلی ربات';
    }

    $rows = [];
    $text = "{$title}\n\nموردی که می‌خواهید ویرایش شود را انتخاب کنید.";
    foreach ($items as $key => $value) {
        $label = $key . ' | ' . shortText($value, 20);
        $rows[] = [[
            'text' => $label,
            'callback_data' => $prefix . $key
        ]];
    }
    $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'customize_menu']];
    sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
}

function showSettingsMenu($chatId)
{
    $s = settings();
    $text = "⚙️ <b>تنظیمات ربات</b>\n\n";
    $text .= "📛 نام سرویس: <b>" . h($s['service_name']) . "</b>\n";
    $text .= "🛠 حالت تعمیر: " . (!empty($s['maintenance']) ? 'روشن ✅' : 'خاموش ⛔') . "\n";
    $text .= "📞 آیدی پشتیبانی: <code>{$s['support_id']}</code>\n";
    sendMessage($chatId, $text, [
        'inline_keyboard' => [
            [['text' => '📛 تغییر نام سرویس', 'callback_data' => 'set_service_name']],
            [['text' => !empty($s['maintenance']) ? '⛔ خاموش کردن تعمیر' : '✅ روشن کردن تعمیر', 'callback_data' => 'toggle_maintenance']],
            [['text' => '📞 تغییر آیدی پشتیبانی', 'callback_data' => 'set_support_id']],
            [['text' => '🧹 پاکسازی فایل‌های موقت', 'callback_data' => 'clean_temp']],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']]
        ]
    ]);
}

function showAdminsMenu($chatId)
{
    $text = "🔐 <b>مدیریت ادمین‌ها</b>\n\n";
    foreach (admins() as $admin) {
        $role = $admin['role'] ?? 'admin';
        $text .= "🆔 <code>{$admin['id']}</code> | {$role}\n";
    }
    sendMessage($chatId, $text, [
        'inline_keyboard' => [
            [['text' => '➕ افزودن ادمین', 'callback_data' => 'admin_add_admin']],
            [['text' => '➖ حذف ادمین', 'callback_data' => 'admin_remove_admin']],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']]
        ]
    ]);
}

function showBroadcastMenu($chatId)
{
    sendMessage($chatId, "📢 <b>ارسال و فوروارد همگانی</b>\n\nنوع عملیات را انتخاب کنید.", [
        'inline_keyboard' => [
            [['text' => '📨 ارسال همگانی', 'callback_data' => 'bc_mode_copy']],
            [['text' => '↪️ فوروارد همگانی', 'callback_data' => 'bc_mode_forward']],
            [['text' => '📊 وضعیت ارسال‌ها', 'callback_data' => 'bc_status']],
            [['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']]
        ]
    ]);
}

function createBroadcastDraft($adminId, $mode, $fromChat, $messageId)
{
    $all = broadcasts();
    $id = newId('bc');
    $all[$id] = [
        'id' => $id,
        'admin_id' => (int)$adminId,
        'mode' => $mode,
        'from_chat_id' => $fromChat,
        'message_id' => $messageId,
        'target' => 'all',
        'status' => 'draft',
        'total' => 0,
        'success' => 0,
        'failed' => 0,
        'created_at' => now(),
        'started_at' => null,
        'finished_at' => null
    ];
    saveBroadcasts($all);
    return $id;
}

function usersForBroadcast($target)
{
    $result = [];
    foreach (users() as $id => $u) {
        if (!empty($u['blocked_by_bot'])) {
            continue;
        }
        if ($target === 'vip' && empty($u['is_vip'])) continue;
        if ($target === 'normal' && !empty($u['is_vip'])) continue;
        if ($target === 'nonblocked' && !empty($u['blocked'])) continue;
        $result[] = (int)$u['id'];
    }
    return $result;
}

function runBroadcast($broadcastId, $adminChatId)
{
    $all = broadcasts();
    if (!isset($all[$broadcastId])) {
        sendMessage($adminChatId, '❌ ارسال پیدا نشد.');
        return;
    }
    $bc = $all[$broadcastId];
    $targets = usersForBroadcast($bc['target']);
    $total = count($targets);

    $all[$broadcastId]['status'] = 'running';
    $all[$broadcastId]['total'] = $total;
    $all[$broadcastId]['started_at'] = now();
    saveBroadcasts($all);

    sendMessage($adminChatId, "📢 عملیات ارسال شروع شد.\n\n👥 تعداد مخاطب: <b>{$total}</b>\n⚡ حالت: " . ($bc['mode'] === 'forward' ? 'فوروارد' : 'ارسال کپی'));

    $success = 0;
    $failed = 0;
    foreach ($targets as $uid) {
        if ($bc['mode'] === 'forward') {
            $res = forwardMsg($uid, $bc['from_chat_id'], $bc['message_id']);
        } else {
            $res = copyMsg($uid, $bc['from_chat_id'], $bc['message_id']);
        }
        if ($res && !empty($res['ok'])) {
            $success++;
        } else {
            $failed++;
            $desc = strtolower($res['description'] ?? '');
            if (strpos($desc, 'blocked') !== false || strpos($desc, 'forbidden') !== false) {
                updateUser($uid, ['blocked_by_bot' => true]);
            }
        }
        usleep(35000);
    }

    $all = broadcasts();
    $all[$broadcastId]['status'] = 'finished';
    $all[$broadcastId]['success'] = $success;
    $all[$broadcastId]['failed'] = $failed;
    $all[$broadcastId]['finished_at'] = now();
    saveBroadcasts($all);

    sendMessage($adminChatId, "✅ عملیات ارسال تمام شد.\n\n👥 کل کاربران: <b>{$total}</b>\n✅ موفق: <b>{$success}</b>\n❌ ناموفق: <b>{$failed}</b>");
}

/* =========================================================
   هندل وضعیت پیام‌ها
   ========================================================= */

function handleStateMessage($chatId, $userId, $msg)
{
    $u = getUser($userId);
    $state = $u['state'] ?? null;
    $data = $u['state_data'] ?? [];
    $text = trim($msg['text'] ?? '');

    if (!$state) {
        return false;
    }

    if ($text === '/cancel') {
        clearState($userId);
        sendMessage($chatId, '✅ عملیات لغو شد.', userKeyboard($userId));
        return true;
    }

    switch ($state) {
        case 'wait_bot_file':
            handleBotUpload($chatId, $userId, $msg);
            return true;

        case 'wait_payment_amount':
            $amount = toInt($text);
            if ($amount < 1000) {
                sendMessage($chatId, '❌ مبلغ معتبر وارد کنید. مثال: <code>100000</code>');
                return true;
            }
            $methodId = $data['method_id'] ?? '';
            $methods = paymentMethods();
            if (!isset($methods[$methodId])) {
                clearState($userId);
                sendMessage($chatId, '❌ روش پرداخت پیدا نشد.');
                return true;
            }
            setState($userId, 'wait_payment_receipt', ['method_id' => $methodId, 'amount' => $amount]);
            sendMessage($chatId, "💳 <b>اطلاعات پرداخت</b>\n\n💰 مبلغ انتخابی: <b>" . money($amount) . "</b>\n\n" . $methods[$methodId]['details'] . "\n\n🧾 بعد از پرداخت، رسید را همینجا ارسال کنید.");
            return true;

        case 'wait_payment_receipt':
            $methodId = $data['method_id'] ?? '';
            $amount = (int)($data['amount'] ?? 0);
            if (!$methodId || !$amount) {
                clearState($userId);
                sendMessage($chatId, '❌ اطلاعات پرداخت ناقص بود. دوباره تلاش کنید.');
                return true;
            }
            $paymentId = createPaymentRequest($userId, $methodId, $amount, $msg);
            clearState($userId);
            sendMessage($chatId, "✅ رسید شما ثبت شد.\n\n🆔 شماره درخواست: <code>{$paymentId}</code>\n💰 مبلغ: <b>" . money($amount) . "</b>\n\nبعد از بررسی مدیریت، موجودی شما افزایش داده می‌شود.", userKeyboard($userId));
            notifyAdminsPayment($paymentId);
            return true;

        case 'wait_ticket_message':
            $subject = $data['subject'] ?? 'سایر موارد';
            $ticketId = createTicket($userId, $subject, $msg);
            clearState($userId);
            sendMessage($chatId, tpl(settings()['texts']['ticket_created'], ['ticket_id' => $ticketId]), userKeyboard($userId));
            notifyAdminsTicket($ticketId);
            return true;

        case 'wait_ticket_reply':
            $ticketId = $data['ticket_id'] ?? '';
            if (!appendTicketMessage($ticketId, 'user', $userId, $msg)) {
                clearState($userId);
                sendMessage($chatId, '❌ امکان پاسخ به این تیکت وجود ندارد.');
                return true;
            }
            clearState($userId);
            sendMessage($chatId, "✅ پاسخ شما ثبت شد.\n\n🆔 تیکت: <code>{$ticketId}</code>", userKeyboard($userId));
            notifyAdminsTicket($ticketId);
            return true;

        case 'admin_wait_ticket_reply':
            if (!isAdmin($userId)) return false;
            $ticketId = $data['ticket_id'] ?? '';
            if (!appendTicketMessage($ticketId, 'admin', $userId, $msg)) {
                clearState($userId);
                sendMessage($chatId, '❌ امکان پاسخ به این تیکت وجود ندارد.');
                return true;
            }
            $tickets = tickets();
            clearState($userId);
            sendMessage($chatId, "✅ پاسخ پشتیبانی ثبت شد.", adminKeyboard());
            if (isset($tickets[$ticketId])) {
                sendMessage($tickets[$ticketId]['user_id'], "🎫 <b>پاسخ جدید پشتیبانی</b>\n\n🆔 تیکت: <code>{$ticketId}</code>\n\n" . h($msg['text'] ?? ($msg['caption'] ?? 'پیام غیرمتنی')), [
                    'inline_keyboard' => [[['text' => '👁 مشاهده تیکت', 'callback_data' => 'ticket_view_' . $ticketId]]]
                ]);
                if (empty($msg['text']) && empty($msg['caption'])) {
                    copyMsg($tickets[$ticketId]['user_id'], $msg['chat']['id'], $msg['message_id']);
                }
            }
            return true;

        case 'admin_user_search':
            if (!isAdmin($userId)) return false;
            $target = toInt($text);
            if (!$target) {
                sendMessage($chatId, '❌ آیدی عددی معتبر ارسال کنید.');
                return true;
            }
            clearState($userId);
            showAdminUserProfile($chatId, $target);
            return true;

        case 'admin_user_add_balance':
            if (!isAdmin($userId)) return false;
            $target = $data['user_id'] ?? 0;
            $amount = toInt($text);
            if ($amount <= 0) {
                sendMessage($chatId, '❌ مبلغ معتبر وارد کنید.');
                return true;
            }
            changeBalance($target, $amount, 'افزایش دستی توسط مدیریت', 'admin_add_balance', ['admin_id' => $userId]);
            clearState($userId);
            sendMessage($chatId, '✅ موجودی کاربر افزایش یافت.');
            showAdminUserProfile($chatId, $target);
            return true;

        case 'admin_user_sub_balance':
            if (!isAdmin($userId)) return false;
            $target = $data['user_id'] ?? 0;
            $amount = toInt($text);
            if ($amount <= 0) {
                sendMessage($chatId, '❌ مبلغ معتبر وارد کنید.');
                return true;
            }
            changeBalance($target, -1 * $amount, 'کاهش دستی توسط مدیریت', 'admin_sub_balance', ['admin_id' => $userId]);
            clearState($userId);
            sendMessage($chatId, '✅ موجودی کاربر کاهش یافت.');
            showAdminUserProfile($chatId, $target);
            return true;

        case 'admin_user_set_limit':
            if (!isAdmin($userId)) return false;
            $target = $data['user_id'] ?? 0;
            $limit = toInt($text);
            if ($limit < 0) {
                sendMessage($chatId, '❌ عدد معتبر وارد کنید.');
                return true;
            }
            updateUser($target, ['bot_limit' => $limit]);
            clearState($userId);
            sendMessage($chatId, '✅ سقف ربات کاربر تغییر کرد.');
            showAdminUserProfile($chatId, $target);
            return true;

        case 'pm_add_name':
            if (!isAdmin($userId)) return false;
            if ($text === '') {
                sendMessage($chatId, '❌ نام روش پرداخت را ارسال کنید.');
                return true;
            }
            setState($userId, 'pm_add_details', ['name' => $text]);
            sendMessage($chatId, "📝 توضیحات کامل روش پرداخت را ارسال کنید.\nمثلاً شماره کارت، نام صاحب حساب، لینک یا آدرس ولت.");
            return true;

        case 'pm_add_details':
            if (!isAdmin($userId)) return false;
            $methods = paymentMethods();
            $id = newId('pm');
            $methods[$id] = [
                'id' => $id,
                'name' => $data['name'],
                'details' => $msg['text'] ?? ($msg['caption'] ?? ''),
                'active' => true,
                'created_at' => now()
            ];
            savePaymentMethods($methods);
            clearState($userId);
            sendMessage($chatId, '✅ روش پرداخت اضافه شد.');
            showPaymentMethodsAdmin($chatId);
            return true;

        case 'pm_edit_name':
            if (!isAdmin($userId)) return false;
            $methods = paymentMethods();
            $id = $data['id'];
            if (isset($methods[$id])) {
                $methods[$id]['name'] = $text;
                savePaymentMethods($methods);
            }
            clearState($userId);
            showPaymentMethodView($chatId, $id);
            return true;

        case 'pm_edit_details':
            if (!isAdmin($userId)) return false;
            $methods = paymentMethods();
            $id = $data['id'];
            if (isset($methods[$id])) {
                $methods[$id]['details'] = $msg['text'] ?? ($msg['caption'] ?? '');
                savePaymentMethods($methods);
            }
            clearState($userId);
            showPaymentMethodView($chatId, $id);
            return true;

        case 'set_number_setting':
            if (!isAdmin($userId)) return false;
            $key = $data['key'] ?? '';
            $val = toInt($text);
            if ($val < 0) {
                sendMessage($chatId, '❌ عدد معتبر وارد کنید.');
                return true;
            }
            $s = settings();
            $s[$key] = $val;
            saveSettings($s);
            clearState($userId);
            sendMessage($chatId, '✅ تنظیمات ذخیره شد.');
            showPlansMenu($chatId);
            return true;

        case 'set_text_setting':
            if (!isAdmin($userId)) return false;
            $key = $data['key'] ?? '';
            $s = settings();
            $s[$key] = $msg['text'] ?? ($msg['caption'] ?? '');
            saveSettings($s);
            clearState($userId);
            sendMessage($chatId, '✅ تنظیمات ذخیره شد.');
            showSettingsMenu($chatId);
            return true;

        case 'set_support_id':
            if (!isAdmin($userId)) return false;
            $sid = toInt($text);
            if (!$sid) {
                sendMessage($chatId, '❌ آیدی عددی معتبر ارسال کنید.');
                return true;
            }
            $s = settings();
            $s['support_id'] = $sid;
            saveSettings($s);
            clearState($userId);
            showSettingsMenu($chatId);
            return true;

        case 'fj_wait_chat':
            if (!isAdmin($userId)) return false;
            $chatIdentifier = trim($text);
            if (preg_match('/t\.me\/([A-Za-z0-9_]+)/i', $chatIdentifier, $m)) {
                $chatIdentifier = '@' . $m[1];
            }
            $res = bot('getChat', ['chat_id' => $chatIdentifier]);
            if (!$res || empty($res['ok'])) {
                sendMessage($chatId, "❌ کانال/گروه پیدا نشد.\n\nنکته: ربات باید عضو یا ادمین آن کانال/گروه باشد.");
                return true;
            }
            $chat = $res['result'];
            $link = '';
            if (!empty($chat['username'])) {
                $link = 'https://t.me/' . $chat['username'];
            } elseif (!empty($chat['invite_link'])) {
                $link = $chat['invite_link'];
            }
            $chData = [
                'id' => newId('fj'),
                'chat_id' => $chat['id'],
                'title' => $chat['title'] ?? ($chat['first_name'] ?? 'بدون عنوان'),
                'username' => $chat['username'] ?? '',
                'type' => $chat['type'] ?? '',
                'link' => $link,
                'active' => true,
                'created_at' => now()
            ];
            if (!$link) {
                setState($userId, 'fj_wait_link', ['channel' => $chData]);
                sendMessage($chatId, "🔗 این کانال/گروه لینک عمومی ندارد.\nلطفاً لینک دعوت را ارسال کنید.");
                return true;
            }
            $s = settings();
            $s['force_join']['channels'][$chData['id']] = $chData;
            saveSettings($s);
            clearState($userId);
            sendMessage($chatId, "✅ کانال/گروه اضافه شد.\n\n📌 نام: " . h($chData['title']) . "\n🆔 شناسه: <code>" . h($chData['chat_id']) . "</code>\n🔗 لینک: " . h($chData['link']));
            showForceJoinAdmin($chatId);
            return true;

        case 'fj_wait_link':
            if (!isAdmin($userId)) return false;
            $link = trim($text);
            if (!filter_var($link, FILTER_VALIDATE_URL)) {
                sendMessage($chatId, '❌ لینک معتبر ارسال کنید.');
                return true;
            }
            $chData = $data['channel'];
            $chData['link'] = $link;
            $s = settings();
            $s['force_join']['channels'][$chData['id']] = $chData;
            saveSettings($s);
            clearState($userId);
            sendMessage($chatId, '✅ کانال/گروه اضافه شد.');
            showForceJoinAdmin($chatId);
            return true;

        case 'customize_wait_value':
            if (!isAdmin($userId)) return false;
            $type = $data['type'];
            $key = $data['key'];
            $val = $msg['text'] ?? ($msg['caption'] ?? '');
            $s = settings();
            if ($type === 'user') {
                $s['buttons'][$key] = $val;
            } elseif ($type === 'admin') {
                $s['admin_buttons'][$key] = $val;
            } else {
                $s['texts'][$key] = $val;
            }
            saveSettings($s);
            clearState($userId);
            sendMessage($chatId, '✅ متن با موفقیت تغییر کرد.');
            showCustomizeMenu($chatId);
            return true;

        case 'guide_edit':
            if (!isAdmin($userId)) return false;
            $s = settings();
            $s['texts']['guide'] = $msg['text'] ?? ($msg['caption'] ?? '');
            saveSettings($s);
            clearState($userId);
            sendMessage($chatId, '✅ متن راهنما ذخیره شد.');
            showGuide($chatId);
            return true;

        case 'admin_add_admin_wait':
            if ((int)$userId !== (int)OWNER_ID) {
                clearState($userId);
                sendMessage($chatId, '⛔ فقط مالک اصلی می‌تواند ادمین اضافه کند.');
                return true;
            }
            $aid = toInt($text);
            if (!$aid) {
                sendMessage($chatId, '❌ آیدی عددی معتبر ارسال کنید.');
                return true;
            }
            addAdminUser($aid);
            clearState($userId);
            sendMessage($chatId, '✅ ادمین اضافه شد.');
            showAdminsMenu($chatId);
            return true;

        case 'admin_remove_admin_wait':
            if ((int)$userId !== (int)OWNER_ID) {
                clearState($userId);
                sendMessage($chatId, '⛔ فقط مالک اصلی می‌تواند ادمین حذف کند.');
                return true;
            }
            $aid = toInt($text);
            if (removeAdminUser($aid)) {
                sendMessage($chatId, '✅ ادمین حذف شد.');
            } else {
                sendMessage($chatId, '❌ ادمین حذف نشد.');
            }
            clearState($userId);
            showAdminsMenu($chatId);
            return true;

        case 'bc_wait_message':
            if (!isAdmin($userId)) return false;
            $mode = $data['mode'] ?? 'copy';
            $bcId = createBroadcastDraft($userId, $mode, $chatId, $msg['message_id']);
            clearState($userId);
            sendMessage($chatId, "📢 پیام دریافت شد.\n\nحالا جامعه هدف را انتخاب کنید:", [
                'inline_keyboard' => [
                    [['text' => '👥 همه کاربران', 'callback_data' => 'bc_target_' . $bcId . '_all']],
                    [['text' => '💎 کاربران ویژه', 'callback_data' => 'bc_target_' . $bcId . '_vip']],
                    [['text' => '👤 کاربران عادی', 'callback_data' => 'bc_target_' . $bcId . '_normal']],
                    [['text' => '🚫 کاربران غیرمسدود', 'callback_data' => 'bc_target_' . $bcId . '_nonblocked']],
                    [['text' => '❌ لغو', 'callback_data' => 'bc_cancel_' . $bcId]]
                ]
            ]);
            return true;
    }

    return false;
}

/* =========================================================
   پردازش Callback
   ========================================================= */

function handleCallback($cb)
{
    $callbackId = $cb['id'];
    $chatId = $cb['message']['chat']['id'];
    $messageId = $cb['message']['message_id'];
    $userId = $cb['from']['id'];
    $data = $cb['data'];

    registerUser($cb['from']);

    if ($data === 'force_check') {
        if (checkForceJoin($userId)) {
            answerCallback($callbackId, settings()['texts']['join_ok'], false);
            showStart($chatId, getUser($userId));
        } else {
            answerCallback($callbackId, settings()['texts']['join_bad'], true);
        }
        return;
    }

    if (!checkForceJoin($userId)) {
        answerCallback($callbackId, 'ابتدا عضویت را کامل کنید.', true);
        sendForceJoin($chatId);
        return;
    }

    if ($data === 'main_back') {
        answerCallback($callbackId);
        clearState($userId);
        showStart($chatId, getUser($userId));
        return;
    }

    if ($data === 'user_balance') {
        answerCallback($callbackId);
        showBalance($chatId, $userId);
        return;
    }

    if ($data === 'user_my_bots') {
        answerCallback($callbackId);
        showUserBots($chatId, $userId);
        return;
    }

    if (startsWith($data, 'pay_method_')) {
        answerCallback($callbackId);
        $methodId = substr($data, strlen('pay_method_'));
        $methods = paymentMethods();
        if (!isset($methods[$methodId]) || empty($methods[$methodId]['active'])) {
            sendMessage($chatId, '❌ این روش پرداخت فعال نیست.');
            return;
        }
        setState($userId, 'wait_payment_amount', ['method_id' => $methodId]);
        sendMessage($chatId, "💰 لطفاً مبلغ افزایش موجودی را ارسال کنید.\n\nمثال: <code>100000</code>\n\nبرای لغو: /cancel");
        return;
    }

    if ($data === 'ticket_new') {
        answerCallback($callbackId);
        sendMessage($chatId, "🎫 <b>ایجاد تیکت جدید</b>\n\nموضوع تیکت را انتخاب کنید:", [
            'inline_keyboard' => [
                [['text' => '💰 مشکل پرداخت', 'callback_data' => 'ticket_subject_مشکل پرداخت']],
                [['text' => '🤖 مشکل ران کردن ربات', 'callback_data' => 'ticket_subject_مشکل ران کردن ربات']],
                [['text' => '📁 مشکل آپلود فایل', 'callback_data' => 'ticket_subject_مشکل آپلود فایل']],
                [['text' => '👤 مشکل حساب کاربری', 'callback_data' => 'ticket_subject_مشکل حساب کاربری']],
                [['text' => '❓ سایر موارد', 'callback_data' => 'ticket_subject_سایر موارد']],
                [['text' => '🔙 بازگشت', 'callback_data' => 'main_back']]
            ]
        ]);
        return;
    }

    if (startsWith($data, 'ticket_subject_')) {
        answerCallback($callbackId);
        $subject = substr($data, strlen('ticket_subject_'));
        setState($userId, 'wait_ticket_message', ['subject' => $subject]);
        sendMessage($chatId, "✍️ لطفاً پیام تیکت خود را ارسال کنید.\n\nمی‌توانید متن، عکس یا فایل ارسال کنید.\nبرای لغو: /cancel");
        return;
    }

    if ($data === 'ticket_list') {
        answerCallback($callbackId);
        showTicketList($chatId, $userId);
        return;
    }

    if (startsWith($data, 'ticket_view_')) {
        answerCallback($callbackId);
        $ticketId = substr($data, strlen('ticket_view_'));
        $tickets = tickets();
        if (!isset($tickets[$ticketId]) || (int)$tickets[$ticketId]['user_id'] !== (int)$userId) {
            sendMessage($chatId, '❌ تیکت پیدا نشد.');
            return;
        }
        $rows = [];
        if ($tickets[$ticketId]['status'] === 'open') {
            $rows[] = [['text' => '✍️ پاسخ به تیکت', 'callback_data' => 'ticket_reply_' . $ticketId], ['text' => '🔒 بستن تیکت', 'callback_data' => 'ticket_close_' . $ticketId]];
        }
        $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'ticket_list']];
        sendMessage($chatId, ticketSummaryText($ticketId), ['inline_keyboard' => $rows]);
        return;
    }

    if (startsWith($data, 'ticket_reply_')) {
        answerCallback($callbackId);
        $ticketId = substr($data, strlen('ticket_reply_'));
        setState($userId, 'wait_ticket_reply', ['ticket_id' => $ticketId]);
        sendMessage($chatId, "✍️ پاسخ خود را ارسال کنید.\nبرای لغو: /cancel");
        return;
    }

    if (startsWith($data, 'ticket_close_')) {
        answerCallback($callbackId);
        $ticketId = substr($data, strlen('ticket_close_'));
        $tickets = tickets();
        if (isset($tickets[$ticketId]) && (int)$tickets[$ticketId]['user_id'] === (int)$userId) {
            $tickets[$ticketId]['status'] = 'closed';
            $tickets[$ticketId]['updated_at'] = now();
            saveTickets($tickets);
            sendMessage($chatId, '✅ تیکت بسته شد.');
        }
        return;
    }

    if (startsWith($data, 'user_bot_view_')) {
        answerCallback($callbackId);
        $botId = substr($data, strlen('user_bot_view_'));
        $all = bots();
        if (!isset($all[$botId]) || (int)$all[$botId]['owner_id'] !== (int)$userId) {
            sendMessage($chatId, '❌ ربات پیدا نشد.');
            return;
        }
        $b = $all[$botId];
        $status = $b['status'] === 'active' ? 'فعال ✅' : 'غیرفعال ⛔';
        $text = "🤖 <b>ربات من</b>\n\n";
        $text .= "🤖 @" . h($b['username']) . "\n";
        $text .= "📛 " . h($b['name']) . "\n";
        $text .= "📌 وضعیت: {$status}\n";
        $text .= "📁 فایل: <code>" . h($b['main_file']) . "</code>\n";
        $text .= "📅 ساخت: " . h($b['created_at']) . "\n";
        sendMessage($chatId, $text, [
            'inline_keyboard' => [
                [['text' => '🚀 رفتن به ربات', 'url' => 'https://t.me/' . $b['username']]],
                [['text' => '📥 دانلود فایل', 'callback_data' => 'user_bot_download_' . $botId]],
                [['text' => '🗑 حذف ربات', 'callback_data' => 'user_bot_delete_' . $botId]],
                [['text' => '🔙 بازگشت', 'callback_data' => 'user_my_bots']]
            ]
        ]);
        return;
    }

    if (startsWith($data, 'user_bot_download_')) {
        answerCallback($callbackId, 'در حال آماده‌سازی فایل...');
        $botId = substr($data, strlen('user_bot_download_'));
        $all = bots();
        if (!isset($all[$botId]) || (int)$all[$botId]['owner_id'] !== (int)$userId) {
            answerCallback($callbackId, '❌ دسترسی ندارید', true);
            return;
        }
        sendBotPackage($chatId, $botId);
        return;
    }

    if (startsWith($data, 'user_bot_delete_')) {
        answerCallback($callbackId);
        $botId = substr($data, strlen('user_bot_delete_'));
        $all = bots();
        if (!isset($all[$botId]) || (int)$all[$botId]['owner_id'] !== (int)$userId) {
            sendMessage($chatId, '❌ ربات پیدا نشد.');
            return;
        }
        deleteBotCompletely($botId);
        sendMessage($chatId, '✅ ربات شما حذف شد.');
        return;
    }

    if (!isAdmin($userId)) {
        answerCallback($callbackId, '⛔ دسترسی ندارید', true);
        return;
    }

    handleAdminCallback($callbackId, $chatId, $messageId, $userId, $data);
}

function sendBotPackage($chatId, $botId)
{
    $all = bots();
    if (!isset($all[$botId])) {
        sendMessage($chatId, '❌ ربات پیدا نشد.');
        return;
    }
    $b = $all[$botId];
    $folder = BOTS_DIR . $b['folder'] . '/';
    if (!is_dir($folder)) {
        sendMessage($chatId, '❌ فایل ربات روی سرور وجود ندارد.');
        return;
    }
    if (class_exists('ZipArchive')) {
        $zipPath = TEMP_DIR . $botId . '_' . time() . '.zip';
        if (createZipFromFolder($folder, $zipPath)) {
            sendDoc($chatId, $zipPath, '📥 فایل ربات @' . ($b['username'] ?? ''));
            @unlink($zipPath);
            return;
        }
    }
    $main = $folder . $b['main_file'];
    sendDoc($chatId, $main, '📥 فایل ربات @' . ($b['username'] ?? ''));
}

function handleAdminCallback($callbackId, $chatId, $messageId, $userId, $data)
{
    answerCallback($callbackId);

    if ($data === 'admin_back') {
        clearState($userId);
        showAdminPanel($chatId);
        return;
    }

    if ($data === 'admin_users_menu') { showAdminUsersMenu($chatId); return; }
    if ($data === 'admin_bots_menu') { showAdminBotsMenu($chatId); return; }
    if ($data === 'finance_menu') { showFinanceMenu($chatId); return; }
    if ($data === 'payment_methods_menu') { showPaymentMethodsAdmin($chatId); return; }
    if ($data === 'force_join_menu') { showForceJoinAdmin($chatId); return; }
    if ($data === 'customize_menu') { showCustomizeMenu($chatId); return; }

    if ($data === 'admin_user_search') {
        setState($userId, 'admin_user_search');
        sendMessage($chatId, '🔍 آیدی عددی کاربر را ارسال کنید.');
        return;
    }

    if ($data === 'admin_user_recent') {
        $rows = [];
        $all = array_reverse(users(), true);
        $text = "📋 <b>۲۰ کاربر اخیر</b>\n\n";
        $i = 1;
        foreach ($all as $id => $u) {
            if ($i > 20) break;
            $text .= "{$i}. " . h(fullName($u)) . " | <code>{$id}</code>\n";
            $rows[] = [[
                'text' => ($u['username'] ? '@' . $u['username'] : $id),
                'callback_data' => 'admin_user_view_' . $id
            ]];
            $i++;
        }
        $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'admin_users_menu']];
        sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
        return;
    }

    if (startsWith($data, 'admin_user_view_')) {
        showAdminUserProfile($chatId, substr($data, strlen('admin_user_view_')));
        return;
    }

    if (startsWith($data, 'admin_user_addbal_')) {
        $target = substr($data, strlen('admin_user_addbal_'));
        setState($userId, 'admin_user_add_balance', ['user_id' => $target]);
        sendMessage($chatId, '➕ مبلغ افزایش موجودی را ارسال کنید.');
        return;
    }

    if (startsWith($data, 'admin_user_subbal_')) {
        $target = substr($data, strlen('admin_user_subbal_'));
        setState($userId, 'admin_user_sub_balance', ['user_id' => $target]);
        sendMessage($chatId, '➖ مبلغ کاهش موجودی را ارسال کنید.');
        return;
    }

    if (startsWith($data, 'admin_user_toggleblock_')) {
        $target = substr($data, strlen('admin_user_toggleblock_'));
        $u = getUser($target);
        updateUser($target, ['blocked' => empty($u['blocked'])]);
        showAdminUserProfile($chatId, $target);
        return;
    }

    if (startsWith($data, 'admin_user_togglevip_')) {
        $target = substr($data, strlen('admin_user_togglevip_'));
        $u = getUser($target);
        updateUser($target, ['is_vip' => empty($u['is_vip'])]);
        showAdminUserProfile($chatId, $target);
        return;
    }

    if (startsWith($data, 'admin_user_setlimit_')) {
        $target = substr($data, strlen('admin_user_setlimit_'));
        setState($userId, 'admin_user_set_limit', ['user_id' => $target]);
        sendMessage($chatId, '📦 سقف جدید تعداد ربات کاربر را ارسال کنید.');
        return;
    }

    if (startsWith($data, 'admin_user_bots_')) {
        $target = substr($data, strlen('admin_user_bots_'));
        $rows = [];
        $text = "🤖 <b>ربات‌های کاربر</b>\n\n";
        foreach (bots() as $id => $b) {
            if ((int)$b['owner_id'] === (int)$target) {
                $text .= '@' . h($b['username']) . " | " . h($b['status']) . "\n";
                $rows[] = [['text' => '@' . $b['username'], 'callback_data' => 'admin_bot_view_' . $id]];
            }
        }
        if (!$rows) $text .= '📭 رباتی ندارد.';
        $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'admin_user_view_' . $target]];
        sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
        return;
    }

    if (startsWith($data, 'admin_user_tickets_')) {
        $target = substr($data, strlen('admin_user_tickets_'));
        $rows = [];
        $text = "🎫 <b>تیکت‌های کاربر</b>\n\n";
        foreach (tickets() as $id => $t) {
            if ((int)$t['user_id'] === (int)$target) {
                $text .= "<code>{$id}</code> | " . h($t['subject']) . " | " . h($t['status']) . "\n";
                $rows[] = [['text' => $id, 'callback_data' => 'admin_ticket_view_' . $id]];
            }
        }
        if (!$rows) $text .= '📭 تیکتی ندارد.';
        $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'admin_user_view_' . $target]];
        sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
        return;
    }

    if (startsWith($data, 'admin_bot_view_')) { showAdminBotView($chatId, substr($data, strlen('admin_bot_view_'))); return; }

    if (startsWith($data, 'admin_bot_toggle_')) {
        $botId = substr($data, strlen('admin_bot_toggle_'));
        $all = bots();
        if (isset($all[$botId])) {
            $active = $all[$botId]['status'] !== 'active';
            if (setBotStatus($botId, $active)) sendMessage($chatId, '✅ وضعیت ربات تغییر کرد.');
            else sendMessage($chatId, '❌ خطا در تغییر وضعیت ربات.');
        }
        showAdminBotView($chatId, $botId);
        return;
    }

    if (startsWith($data, 'admin_bot_rehook_')) {
        $botId = substr($data, strlen('admin_bot_rehook_'));
        $all = bots();
        if (isset($all[$botId])) {
            $res = setBotWebhook($all[$botId]['token'], $all[$botId]['webhook_url']);
            sendMessage($chatId, !empty($res['ok']) ? '✅ وبهوک دوباره تنظیم شد.' : '❌ خطا: ' . h($res['description'] ?? 'نامشخص'));
        }
        return;
    }

    if (startsWith($data, 'admin_bot_download_')) {
        sendBotPackage($chatId, substr($data, strlen('admin_bot_download_')));
        return;
    }

    if (startsWith($data, 'admin_bot_delete_')) {
        $botId = substr($data, strlen('admin_bot_delete_'));
        deleteBotCompletely($botId);
        sendMessage($chatId, '✅ ربات کامل حذف شد.');
        showAdminBotsMenu($chatId);
        return;
    }

    if ($data === 'finance_pending') { showPendingPayments($chatId); return; }
    if (startsWith($data, 'pay_view_')) { showPaymentView($chatId, substr($data, strlen('pay_view_'))); return; }

    if (startsWith($data, 'pay_approve_')) {
        $paymentId = substr($data, strlen('pay_approve_'));
        [$ok, $msg] = approvePayment($paymentId, $userId);
        sendMessage($chatId, ($ok ? '✅ ' : '❌ ') . h($msg));
        return;
    }

    if (startsWith($data, 'pay_reject_')) {
        $paymentId = substr($data, strlen('pay_reject_'));
        [$ok, $msg] = rejectPayment($paymentId, $userId);
        sendMessage($chatId, ($ok ? '✅ ' : '❌ ') . h($msg));
        return;
    }

    if (startsWith($data, 'pay_receipt_')) {
        $paymentId = substr($data, strlen('pay_receipt_'));
        $pays = payments();
        if (isset($pays[$paymentId])) {
            copyMsg($chatId, $pays[$paymentId]['receipt_chat_id'], $pays[$paymentId]['receipt_message_id']);
        }
        return;
    }

    if ($data === 'finance_transactions') {
        $text = "📜 <b>آخرین تراکنش‌ها</b>\n\n";
        $i = 1;
        foreach (array_reverse(transactions(), true) as $tx) {
            if ($i > 20) break;
            $text .= "{$i}. <code>{$tx['user_id']}</code> | " . h($tx['type']) . " | " . money($tx['amount']) . "\n";
            $text .= "   " . h($tx['created_at']) . "\n";
            $i++;
        }
        sendMessage($chatId, $text, inlineBack('finance_menu'));
        return;
    }

    if ($data === 'finance_income') {
        $income = 0;
        foreach (payments() as $p) if ($p['status'] === 'approved') $income += (int)$p['amount'];
        sendMessage($chatId, "💵 <b>مجموع درآمد تایید شده:</b>\n\n" . money($income), inlineBack('finance_menu'));
        return;
    }

    if ($data === 'pm_add') {
        setState($userId, 'pm_add_name');
        sendMessage($chatId, '📛 نام روش پرداخت را ارسال کنید.');
        return;
    }
    if (startsWith($data, 'pm_view_')) { showPaymentMethodView($chatId, substr($data, strlen('pm_view_'))); return; }
    if (startsWith($data, 'pm_edit_name_')) {
        $id = substr($data, strlen('pm_edit_name_'));
        setState($userId, 'pm_edit_name', ['id' => $id]);
        sendMessage($chatId, '✏️ نام جدید روش پرداخت را ارسال کنید.');
        return;
    }
    if (startsWith($data, 'pm_edit_details_')) {
        $id = substr($data, strlen('pm_edit_details_'));
        setState($userId, 'pm_edit_details', ['id' => $id]);
        sendMessage($chatId, '📝 توضیحات جدید روش پرداخت را ارسال کنید.');
        return;
    }
    if (startsWith($data, 'pm_toggle_')) {
        $id = substr($data, strlen('pm_toggle_'));
        $m = paymentMethods();
        if (isset($m[$id])) {
            $m[$id]['active'] = empty($m[$id]['active']);
            savePaymentMethods($m);
        }
        showPaymentMethodView($chatId, $id);
        return;
    }
    if (startsWith($data, 'pm_delete_')) {
        $id = substr($data, strlen('pm_delete_'));
        $m = paymentMethods();
        unset($m[$id]);
        savePaymentMethods($m);
        showPaymentMethodsAdmin($chatId);
        return;
    }

    if ($data === 'set_bot_price') { setState($userId, 'set_number_setting', ['key' => 'bot_price']); sendMessage($chatId, '💰 قیمت جدید ران کردن ربات را ارسال کنید.'); return; }
    if ($data === 'set_free_bots') { setState($userId, 'set_number_setting', ['key' => 'free_bots']); sendMessage($chatId, '🎁 تعداد ربات رایگان را ارسال کنید.'); return; }
    if ($data === 'set_default_limit') { setState($userId, 'set_number_setting', ['key' => 'default_bot_limit']); sendMessage($chatId, '📦 سقف پیش‌فرض ربات کاربر را ارسال کنید.'); return; }
    if ($data === 'set_max_file') { setState($userId, 'set_number_setting', ['key' => 'max_file_mb']); sendMessage($chatId, '📁 حداکثر حجم فایل بر حسب MB را ارسال کنید.'); return; }
    if ($data === 'toggle_strict_security') {
        $s = settings();
        $s['strict_security'] = empty($s['strict_security']);
        saveSettings($s);
        showPlansMenu($chatId);
        return;
    }

    if ($data === 'fj_toggle') {
        $s = settings();
        $s['force_join']['enabled'] = empty($s['force_join']['enabled']);
        saveSettings($s);
        showForceJoinAdmin($chatId);
        return;
    }
    if ($data === 'fj_add') {
        setState($userId, 'fj_wait_chat');
        sendMessage($chatId, "➕ آیدی کانال/گروه را ارسال کنید.\n\nمثال:\n<code>@channel</code>\nیا\n<code>-100123456789</code>\n\nنکته: ربات باید داخل کانال/گروه عضو یا ادمین باشد.");
        return;
    }
    if ($data === 'fj_list') { showForceJoinList($chatId); return; }
    if ($data === 'fj_test') { sendForceJoin($chatId); return; }
    if (startsWith($data, 'fj_view_')) {
        $id = substr($data, strlen('fj_view_'));
        $s = settings();
        if (!isset($s['force_join']['channels'][$id])) { sendMessage($chatId, '❌ پیدا نشد.'); return; }
        $ch = $s['force_join']['channels'][$id];
        $text = "🔐 <b>عضویت اجباری</b>\n\n";
        $text .= "📌 نام: " . h($ch['title']) . "\n";
        $text .= "🆔 شناسه: <code>" . h($ch['chat_id']) . "</code>\n";
        $text .= "🔗 لینک: " . h($ch['link']) . "\n";
        $text .= "📍 نوع: " . h($ch['type']) . "\n";
        $text .= "وضعیت: " . (!empty($ch['active']) ? 'فعال ✅' : 'غیرفعال ⛔');
        sendMessage($chatId, $text, [
            'inline_keyboard' => [
                [['text' => !empty($ch['active']) ? '⛔ غیرفعال' : '✅ فعال', 'callback_data' => 'fj_toggle_ch_' . $id]],
                [['text' => '🗑 حذف', 'callback_data' => 'fj_delete_' . $id]],
                [['text' => '🔙 بازگشت', 'callback_data' => 'fj_list']]
            ]
        ]);
        return;
    }
    if (startsWith($data, 'fj_toggle_ch_')) {
        $id = substr($data, strlen('fj_toggle_ch_'));
        $s = settings();
        if (isset($s['force_join']['channels'][$id])) {
            $s['force_join']['channels'][$id]['active'] = empty($s['force_join']['channels'][$id]['active']);
            saveSettings($s);
        }
        showForceJoinList($chatId);
        return;
    }
    if (startsWith($data, 'fj_delete_')) {
        $id = substr($data, strlen('fj_delete_'));
        $s = settings();
        unset($s['force_join']['channels'][$id]);
        saveSettings($s);
        showForceJoinList($chatId);
        return;
    }

    if ($data === 'cust_buttons_user') { showCustomizeList($chatId, 'user'); return; }
    if ($data === 'cust_buttons_admin') { showCustomizeList($chatId, 'admin'); return; }
    if ($data === 'cust_texts') { showCustomizeList($chatId, 'text'); return; }
    if (startsWith($data, 'cust_edit_user_')) {
        $key = substr($data, strlen('cust_edit_user_'));
        setState($userId, 'customize_wait_value', ['type' => 'user', 'key' => $key]);
        sendMessage($chatId, "✏️ متن جدید دکمه <code>{$key}</code> را ارسال کنید.");
        return;
    }
    if (startsWith($data, 'cust_edit_admin_')) {
        $key = substr($data, strlen('cust_edit_admin_'));
        setState($userId, 'customize_wait_value', ['type' => 'admin', 'key' => $key]);
        sendMessage($chatId, "✏️ متن جدید دکمه <code>{$key}</code> را ارسال کنید.");
        return;
    }
    if (startsWith($data, 'cust_edit_text_')) {
        $key = substr($data, strlen('cust_edit_text_'));
        setState($userId, 'customize_wait_value', ['type' => 'text', 'key' => $key]);
        sendMessage($chatId, "📝 متن جدید پیام <code>{$key}</code> را ارسال کنید.\nمی‌توانید از HTML استفاده کنید.");
        return;
    }
    if ($data === 'cust_reset_confirm') {
        sendMessage($chatId, '⚠️ مطمئن هستید همه متن‌ها و دکمه‌ها پیش‌فرض شود؟', [
            'inline_keyboard' => [
                [['text' => '✅ بله، بازگردانی کن', 'callback_data' => 'cust_reset_do']],
                [['text' => '❌ لغو', 'callback_data' => 'customize_menu']]
            ]
        ]);
        return;
    }
    if ($data === 'cust_reset_do') {
        saveSettings(defaultSettings());
        sendMessage($chatId, '✅ تنظیمات پیش‌فرض شد.');
        showCustomizeMenu($chatId);
        return;
    }

    if ($data === 'set_service_name') { setState($userId, 'set_text_setting', ['key' => 'service_name']); sendMessage($chatId, '📛 نام جدید سرویس را ارسال کنید.'); return; }
    if ($data === 'toggle_maintenance') {
        $s = settings();
        $s['maintenance'] = empty($s['maintenance']);
        saveSettings($s);
        showSettingsMenu($chatId);
        return;
    }
    if ($data === 'set_support_id') { setState($userId, 'set_support_id'); sendMessage($chatId, '📞 آیدی عددی پشتیبانی را ارسال کنید.'); return; }
    if ($data === 'clean_temp') {
        deleteDirectory(TEMP_DIR);
        mkdir(TEMP_DIR, 0755, true);
        sendMessage($chatId, '✅ فایل‌های موقت پاکسازی شدند.');
        return;
    }

    if ($data === 'admin_add_admin') {
        setState($userId, 'admin_add_admin_wait');
        sendMessage($chatId, '➕ آیدی عددی ادمین جدید را ارسال کنید.');
        return;
    }
    if ($data === 'admin_remove_admin') {
        setState($userId, 'admin_remove_admin_wait');
        sendMessage($chatId, '➖ آیدی عددی ادمینی که باید حذف شود را ارسال کنید.');
        return;
    }

    if ($data === 'bc_mode_copy') {
        setState($userId, 'bc_wait_message', ['mode' => 'copy']);
        sendMessage($chatId, "📨 پیام مورد نظر برای ارسال همگانی را ارسال کنید.\n\nبعد از ارسال، از شما تایید گرفته می‌شود.");
        return;
    }
    if ($data === 'bc_mode_forward') {
        setState($userId, 'bc_wait_message', ['mode' => 'forward']);
        sendMessage($chatId, "↪️ پیام مورد نظر برای فوروارد همگانی را ارسال کنید.\n\nبعد از ارسال، از شما تایید گرفته می‌شود.");
        return;
    }
    if ($data === 'bc_status') {
        $text = "📊 <b>وضعیت آخرین ارسال‌ها</b>\n\n";
        $i = 1;
        foreach (array_reverse(broadcasts(), true) as $bc) {
            if ($i > 10) break;
            $text .= "{$i}. <code>{$bc['id']}</code> | " . h($bc['status']) . " | 👥 {$bc['total']} | ✅ {$bc['success']} | ❌ {$bc['failed']}\n";
            $i++;
        }
        sendMessage($chatId, $text, inlineBack('admin_back'));
        return;
    }
    if (startsWith($data, 'bc_target_')) {
        $tmp = substr($data, strlen('bc_target_'));
        $pos = strrpos($tmp, '_');
        $bcId = substr($tmp, 0, $pos);
        $target = substr($tmp, $pos + 1);
        $all = broadcasts();
        if (isset($all[$bcId])) {
            $all[$bcId]['target'] = $target;
            saveBroadcasts($all);
            $count = count(usersForBroadcast($target));
            sendMessage($chatId, "✅ جامعه هدف انتخاب شد.\n\n👥 تعداد مخاطب: <b>{$count}</b>\n\nارسال شروع شود؟", [
                'inline_keyboard' => [
                    [['text' => '✅ شروع ارسال', 'callback_data' => 'bc_start_' . $bcId]],
                    [['text' => '❌ لغو', 'callback_data' => 'bc_cancel_' . $bcId]]
                ]
            ]);
        }
        return;
    }
    if (startsWith($data, 'bc_start_')) {
        $bcId = substr($data, strlen('bc_start_'));
        runBroadcast($bcId, $chatId);
        return;
    }
    if (startsWith($data, 'bc_cancel_')) {
        $bcId = substr($data, strlen('bc_cancel_'));
        $all = broadcasts();
        if (isset($all[$bcId])) {
            $all[$bcId]['status'] = 'cancelled';
            saveBroadcasts($all);
        }
        sendMessage($chatId, '❌ ارسال لغو شد.');
        return;
    }

    if (startsWith($data, 'admin_ticket_view_')) {
        $ticketId = substr($data, strlen('admin_ticket_view_'));
        $tickets = tickets();
        if (!isset($tickets[$ticketId])) { sendMessage($chatId, '❌ تیکت پیدا نشد.'); return; }
        $rows = [];
        if ($tickets[$ticketId]['status'] === 'open') {
            $rows[] = [['text' => '✍️ پاسخ', 'callback_data' => 'admin_ticket_reply_' . $ticketId], ['text' => '🔒 بستن', 'callback_data' => 'admin_ticket_close_' . $ticketId]];
        }
        $rows[] = [['text' => '🗑 حذف', 'callback_data' => 'admin_ticket_delete_' . $ticketId]];
        $rows[] = [['text' => '🔙 بازگشت', 'callback_data' => 'admin_tickets_open']];
        sendMessage($chatId, ticketSummaryText($ticketId, true), ['inline_keyboard' => $rows]);
        return;
    }
    if (startsWith($data, 'admin_ticket_reply_')) {
        $ticketId = substr($data, strlen('admin_ticket_reply_'));
        setState($userId, 'admin_wait_ticket_reply', ['ticket_id' => $ticketId]);
        sendMessage($chatId, "✍️ پاسخ خود را برای تیکت <code>{$ticketId}</code> ارسال کنید.");
        return;
    }
    if (startsWith($data, 'admin_ticket_close_')) {
        $ticketId = substr($data, strlen('admin_ticket_close_'));
        $tickets = tickets();
        if (isset($tickets[$ticketId])) {
            $tickets[$ticketId]['status'] = 'closed';
            $tickets[$ticketId]['updated_at'] = now();
            saveTickets($tickets);
            sendMessage($tickets[$ticketId]['user_id'], "🔒 تیکت شما بسته شد.\n\n🆔 <code>{$ticketId}</code>");
        }
        sendMessage($chatId, '✅ تیکت بسته شد.');
        return;
    }
    if (startsWith($data, 'admin_ticket_delete_')) {
        $ticketId = substr($data, strlen('admin_ticket_delete_'));
        $tickets = tickets();
        unset($tickets[$ticketId]);
        saveTickets($tickets);
        sendMessage($chatId, '🗑 تیکت حذف شد.');
        return;
    }
    if ($data === 'admin_tickets_open') { showAdminTickets($chatId, 'open'); return; }

    sendMessage($chatId, '❔ دستور ناشناخته بود.');
}

function showAdminTickets($chatId, $status = 'open')
{
    $rows = [];
    $text = "🎫 <b>مدیریت تیکت‌ها</b>\n\n";
    $i = 1;
    foreach (array_reverse(tickets(), true) as $id => $t) {
        if ($status !== 'all' && $t['status'] !== $status) continue;
        $u = getUser($t['user_id']);
        $text .= "{$i}. <code>{$id}</code> | " . h($t['subject']) . " | " . h(fullName($u)) . " | " . h($t['status']) . "\n";
        $rows[] = [['text' => '🎫 ' . $id, 'callback_data' => 'admin_ticket_view_' . $id]];
        $i++;
        if ($i > 20) break;
    }
    if ($i === 1) $text .= '📭 تیکتی وجود ندارد.';
    $rows[] = [['text' => '📂 باز', 'callback_data' => 'admin_tickets_open'], ['text' => '🔙 بازگشت', 'callback_data' => 'admin_back']];
    sendMessage($chatId, $text, ['inline_keyboard' => $rows]);
}

/* =========================================================
   ورودی اصلی
   ========================================================= */

$update = json_decode(file_get_contents('php://input'), true);
if (!$update) {
    echo 'OK';
    exit;
}

if (isset($update['callback_query'])) {
    handleCallback($update['callback_query']);
    exit;
}

if (!isset($update['message'])) {
    echo 'OK';
    exit;
}

$msg = $update['message'];
$chatId = $msg['chat']['id'];
$from = $msg['from'] ?? [];
$userId = $from['id'] ?? 0;
$text = trim($msg['text'] ?? '');

$user = registerUser($from);
$s = settings();
$b = $s['buttons'];
$a = $s['admin_buttons'];

if (!$userId) {
    exit;
}

if (!empty(getUser($userId)['blocked']) && !isAdmin($userId)) {
    sendMessage($chatId, $s['texts']['blocked']);
    exit;
}

if (!empty($s['maintenance']) && !isAdmin($userId)) {
    sendMessage($chatId, $s['texts']['maintenance']);
    exit;
}

if ($text === '/start') {
    clearState($userId);
    if (!checkForceJoin($userId)) {
        sendForceJoin($chatId);
        exit;
    }
    showStart($chatId, getUser($userId));
    exit;
}

if (!checkForceJoin($userId)) {
    sendForceJoin($chatId);
    exit;
}

if (handleStateMessage($chatId, $userId, $msg)) {
    exit;
}

if ($text === '/admin' || $text === $b['admin']) {
    if (!isAdmin($userId)) {
        sendMessage($chatId, $s['texts']['no_access']);
        exit;
    }
    clearState($userId);
    showAdminPanel($chatId);
    exit;
}

if ($text === $b['run_bot']) {
    showRunBot($chatId, $userId);
    exit;
}

if ($text === $b['account']) {
    showAccount($chatId, $userId);
    exit;
}

if ($text === $b['balance']) {
    showBalance($chatId, $userId);
    exit;
}

if ($text === $b['guide']) {
    showGuide($chatId);
    exit;
}

if ($text === $b['ticket']) {
    showTicketMenu($chatId);
    exit;
}

if (isAdmin($userId)) {
    if ($text === $a['users']) { showAdminUsersMenu($chatId); exit; }
    if ($text === $a['bots']) { showAdminBotsMenu($chatId); exit; }
    if ($text === $a['finance']) { showFinanceMenu($chatId); exit; }
    if ($text === $a['payment_methods']) { showPaymentMethodsAdmin($chatId); exit; }
    if ($text === $a['plans']) { showPlansMenu($chatId); exit; }
    if ($text === $a['guide']) { setState($userId, 'guide_edit'); sendMessage($chatId, "📚 متن جدید راهنمای بات را ارسال کنید.\n\nمتن فعلی:\n\n" . $s['texts']['guide']); exit; }
    if ($text === $a['tickets']) { showAdminTickets($chatId, 'open'); exit; }
    if ($text === $a['broadcast']) { showBroadcastMenu($chatId); exit; }
    if ($text === $a['force_join']) { showForceJoinAdmin($chatId); exit; }
    if ($text === $a['customize']) { showCustomizeMenu($chatId); exit; }
    if ($text === $a['stats']) { showStats($chatId); exit; }
    if ($text === $a['settings']) { showSettingsMenu($chatId); exit; }
    if ($text === $a['admins']) { showAdminsMenu($chatId); exit; }
    if ($text === $a['back']) { showStart($chatId, getUser($userId)); exit; }
}

sendMessage($chatId, "❔ دستور نامعتبر است.\nاز دکمه‌های پایین استفاده کنید.", userKeyboard($userId));

?>
