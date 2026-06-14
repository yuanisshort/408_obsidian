<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
    <script src="./js/tailwind@3.4.1_typographytypography@0.5.10.js"></script>
    <link rel="icon" href="/favicon.ico">
    <title>从“零”开始，真正理解KMP算法next数组的求法</title>
    <link rel="stylesheet" href="./css/quill.snow.css?t=202208171505" />
    <link rel="stylesheet" href="./css/github.css" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
</head>

<body>
    <div class="post js_watermark quill-editor dark:!bg-[#20242A]">
        <h1 class="title title-mark dark:!text-slate-300">从“零”开始，真正理解KMP算法next数组的求法</h1>
        <div class="group-info">
            <a href="https://wx.zsxq.com/group/88885281525452">
                <span>来自：</span>
                <span class="group-name">计狗上岸</span>
            </a>
        </div>
        <div class="author-info">
            <div class="author">
                <img src="https://images.zsxq.com/Fqxpxhz6DdMltGxDkodBsOyAftte?e=2064038400&token=kIxbL07-8jAj8w1n4s9zv64FuZZNEATmlU_Vm6zD:680sbmpIU2keHlHHmA8uEAJHODk="  alt="用户头像" />
                <span class="nick-name">小布</span>
            </div>
            <span class="date" id="article-date">2023年10月07日 14:00</span>
        </div>
        <div class="ql-snow">
            <div class="content ql-editor"><h4>简介</h4><p>　　KMP 算法是 D.E.Knuth、J,H,Morris 和 V.R.Pratt 三位神人共同提出的，称之为 Knuth-Morria-Pratt 算法，简称 KMP 算法。该算法相对于 Brute-Force（暴力）算法有比较大的改进，主要是消除了主串指针的回溯，从而使算法效率有了某种程度的提高。</p><p><br></p><h4>提取加速匹配的信息</h4><p>　　上面说道 KMP 算法主要是通过消除主串指针的回溯来提高匹配的效率的，那么，它是则呢样来消除回溯的呢？就是因为它提取并运用了加速匹配的信息！</p><p>　　这种信息就是对于每模式串 t 的每个元素 t j，都存在一个实数 k ，使得模式串 t 开头的 k 个字符（t 0 t 1…t k-1）依次与 t j 前面的 k（t j-k t j-k+1…t j-1，这里第一个字符 t j-k 最多从 t 1 开始，所以 k &lt; j）个字符相同。如果这样的 k 有多个，则取最大的一个。模式串 t 中每个位置 j 的字符都有这种信息，采用 next 数组表示，即 next[ j ]=MAX{ k }。</p><p>　　</p><p>　　加速信息，即数组 next 的提取是整个 KMP 算法中最核心的部分，弄懂了 next 的求解方法，也就弄懂了 KMP 算法的十之七八了，但是不巧的是这部分代码恰恰是最不容易弄懂的……</p><p>　　</p><p>先上代码</p><p><br></p><div class="ql-code-block-container"><div class="ql-code-block"><span class="ql-token hljs-type">void</span> <span class="ql-token hljs-title">Getnext(int next[],String t)</span></div><div class="ql-code-block">{</div><div class="ql-code-block">   <span class="ql-token hljs-type">int</span> j=<span class="ql-token hljs-number">0</span>,k=<span class="ql-token hljs-number">-1</span>;</div><div class="ql-code-block">   next[<span class="ql-token hljs-number">0</span>]=<span class="ql-token hljs-number">-1</span>;</div><div class="ql-code-block">   <span class="ql-token hljs-keyword">while</span>(j&lt;t.length<span class="ql-token hljs-number">-1</span>)</div><div class="ql-code-block">   {</div><div class="ql-code-block">      <span class="ql-token hljs-keyword">if</span>(k == <span class="ql-token hljs-number">-1</span> || t[j] == t[k])</div><div class="ql-code-block">      {</div><div class="ql-code-block">         j++;k++;</div><div class="ql-code-block">         next[j] = k;</div><div class="ql-code-block">      }</div><div class="ql-code-block">      <span class="ql-token hljs-keyword">else</span> k = next[k];<span class="ql-token hljs-comment">//此语句是这段代码最反人类的地方，如果你一下子就能看懂，那么请允许我称呼你一声大神！</span></div><div class="ql-code-block">   }</div><div class="ql-code-block">}</div></div><p><br></p><p><br></p><p>ok，下面咱们分三种情况来讲 next 的求解过程</p><p><br></p><h4>特殊情况</h4><p>当 j 的值为 0 或 1 的时候，它们的 k 值都为 0，即 next[0] = 0、next[1] =0。但是为了后面 k 值计算的方便，我们将 next[0] 的值设置成 -1。</p><p><br></p><h4>当 t[j] == t[k] 的情况</h4><p>举个栗子</p><p><img src="https://article-images.zsxq.com/FqlBo78xiq4iOzzXdu9UulAi-zNl"></p><p>观察上图可知，当 t[j] == t[k] 时，必然有"t[0]…t[k-1]" == " t[j-k]…t[j-1]"，此时的 k 即是相同子串的长度。因为有"t[0]…t[k-1]" == " t[j-k]…t[j-1]"，且 t[j] == t[k]，则有"t[0]…t[k]" == " t[j-k]…t[j]"，这样也就得出了next[j+1]=k+1。</p><p><br></p><h4>当t[j] != t[k] 的情况</h4><p>关于这种情况，在代码中的描述就是“简单”的一句 k = next[k]；。我当时看了之后，感觉有点蒙，于是就去翻《数据结构教程》。但是这本书里，对于这行代码的解释只有三个字：k 回退…！于是我从“有点蒙”的状态升级到了“很蒙蔽”的状态，我心想，k 回退？我当然知道这是 k 退回，但是它为什么要会退到 next[k] 的位置？为什么不是回退到k-1？？？巴拉巴拉巴拉…此处省略一万字。</p><p><br></p><p>我绞尽脑汁，仍是不得其解。于是我就去问度娘…</p><p>在我看了众多博客之后，终于有了一种拨云见日的感觉，看下图</p><p><br></p><p><img src="https://article-images.zsxq.com/FsHhPiDqQvPkDGeHpARKziHSq9DO"></p><p><br></p><p>　　 由第2中情况可知，当 t[j] == t[k] 时，t[j+1] 的最大子串的长度为 k，即 next[j+1] = k+1。但是此时t[j] != t[k] 了，所以就有 next[j+1] &lt; k，那么求 next[j+1] 就等同于求 t[j] 往前小于 k 个的字符（包括t[j]，看上图蓝色框框）与 t[k] 前面的字符（绿色框框）的最长重合串，即 t[j-k+1] ~ t[j] 与 t[0] ~ t[k-1] 的最长重合串（这里所说“最长重合串”实不严谨，但你知道是符合 k 的子串就行…），那么就相当于求 next[k]（只不过 t[k] 变成了 t[j],但是 next[k] 的值与 t[k] 无关）!!!。所以才有了这句 k = next[k]，如果新的一轮循环（这时 k = next[k] ，j 不变）中 t[j] 依然不等于 t[k] ，则说明倒数第二大 t[0~next[k]-1] 也不行，那么 k 会继续被 next[k] 赋值（这就是所谓的 k 回退…），直到找到符合重合的子串或者 k == -1。</p><p><br></p><p>至此，算是把求解数组 next 的算法弄清楚了（其实是，终于把 k = next[k] 弄懂了…）</p><p><br></p><p>因为这个算法神奇难解之处就在k=next[k]这一处的理解上，网上解析的非常之多，有的就是例证，举例子按代码走流程，走出结果了，跟肉眼看的一致，就认为解释了为什么k=next[k]；很少有看到解释的非常清楚的。</p></div>
        </div>
        <div class="milkdown-preview"><h4>简介</h4><p>　　KMP 算法是 D.E.Knuth、J,H,Morris 和 V.R.Pratt 三位神人共同提出的，称之为 Knuth-Morria-Pratt 算法，简称 KMP 算法。该算法相对于 Brute-Force（暴力）算法有比较大的改进，主要是消除了主串指针的回溯，从而使算法效率有了某种程度的提高。</p><p><br></p><h4>提取加速匹配的信息</h4><p>　　上面说道 KMP 算法主要是通过消除主串指针的回溯来提高匹配的效率的，那么，它是则呢样来消除回溯的呢？就是因为它提取并运用了加速匹配的信息！</p><p>　　这种信息就是对于每模式串 t 的每个元素 t j，都存在一个实数 k ，使得模式串 t 开头的 k 个字符（t 0 t 1…t k-1）依次与 t j 前面的 k（t j-k t j-k+1…t j-1，这里第一个字符 t j-k 最多从 t 1 开始，所以 k &lt; j）个字符相同。如果这样的 k 有多个，则取最大的一个。模式串 t 中每个位置 j 的字符都有这种信息，采用 next 数组表示，即 next[ j ]=MAX{ k }。</p><p>　　</p><p>　　加速信息，即数组 next 的提取是整个 KMP 算法中最核心的部分，弄懂了 next 的求解方法，也就弄懂了 KMP 算法的十之七八了，但是不巧的是这部分代码恰恰是最不容易弄懂的……</p><p>　　</p><p>先上代码</p><p><br></p><div class="ql-code-block-container"><div class="ql-code-block"><span class="ql-token hljs-type">void</span> <span class="ql-token hljs-title">Getnext(int next[],String t)</span></div><div class="ql-code-block">{</div><div class="ql-code-block">   <span class="ql-token hljs-type">int</span> j=<span class="ql-token hljs-number">0</span>,k=<span class="ql-token hljs-number">-1</span>;</div><div class="ql-code-block">   next[<span class="ql-token hljs-number">0</span>]=<span class="ql-token hljs-number">-1</span>;</div><div class="ql-code-block">   <span class="ql-token hljs-keyword">while</span>(j&lt;t.length<span class="ql-token hljs-number">-1</span>)</div><div class="ql-code-block">   {</div><div class="ql-code-block">      <span class="ql-token hljs-keyword">if</span>(k == <span class="ql-token hljs-number">-1</span> || t[j] == t[k])</div><div class="ql-code-block">      {</div><div class="ql-code-block">         j++;k++;</div><div class="ql-code-block">         next[j] = k;</div><div class="ql-code-block">      }</div><div class="ql-code-block">      <span class="ql-token hljs-keyword">else</span> k = next[k];<span class="ql-token hljs-comment">//此语句是这段代码最反人类的地方，如果你一下子就能看懂，那么请允许我称呼你一声大神！</span></div><div class="ql-code-block">   }</div><div class="ql-code-block">}</div></div><p><br></p><p><br></p><p>ok，下面咱们分三种情况来讲 next 的求解过程</p><p><br></p><h4>特殊情况</h4><p>当 j 的值为 0 或 1 的时候，它们的 k 值都为 0，即 next[0] = 0、next[1] =0。但是为了后面 k 值计算的方便，我们将 next[0] 的值设置成 -1。</p><p><br></p><h4>当 t[j] == t[k] 的情况</h4><p>举个栗子</p><p><img src="https://article-images.zsxq.com/FqlBo78xiq4iOzzXdu9UulAi-zNl"></p><p>观察上图可知，当 t[j] == t[k] 时，必然有"t[0]…t[k-1]" == " t[j-k]…t[j-1]"，此时的 k 即是相同子串的长度。因为有"t[0]…t[k-1]" == " t[j-k]…t[j-1]"，且 t[j] == t[k]，则有"t[0]…t[k]" == " t[j-k]…t[j]"，这样也就得出了next[j+1]=k+1。</p><p><br></p><h4>当t[j] != t[k] 的情况</h4><p>关于这种情况，在代码中的描述就是“简单”的一句 k = next[k]；。我当时看了之后，感觉有点蒙，于是就去翻《数据结构教程》。但是这本书里，对于这行代码的解释只有三个字：k 回退…！于是我从“有点蒙”的状态升级到了“很蒙蔽”的状态，我心想，k 回退？我当然知道这是 k 退回，但是它为什么要会退到 next[k] 的位置？为什么不是回退到k-1？？？巴拉巴拉巴拉…此处省略一万字。</p><p><br></p><p>我绞尽脑汁，仍是不得其解。于是我就去问度娘…</p><p>在我看了众多博客之后，终于有了一种拨云见日的感觉，看下图</p><p><br></p><p><img src="https://article-images.zsxq.com/FsHhPiDqQvPkDGeHpARKziHSq9DO"></p><p><br></p><p>　　 由第2中情况可知，当 t[j] == t[k] 时，t[j+1] 的最大子串的长度为 k，即 next[j+1] = k+1。但是此时t[j] != t[k] 了，所以就有 next[j+1] &lt; k，那么求 next[j+1] 就等同于求 t[j] 往前小于 k 个的字符（包括t[j]，看上图蓝色框框）与 t[k] 前面的字符（绿色框框）的最长重合串，即 t[j-k+1] ~ t[j] 与 t[0] ~ t[k-1] 的最长重合串（这里所说“最长重合串”实不严谨，但你知道是符合 k 的子串就行…），那么就相当于求 next[k]（只不过 t[k] 变成了 t[j],但是 next[k] 的值与 t[k] 无关）!!!。所以才有了这句 k = next[k]，如果新的一轮循环（这时 k = next[k] ，j 不变）中 t[j] 依然不等于 t[k] ，则说明倒数第二大 t[0~next[k]-1] 也不行，那么 k 会继续被 next[k] 赋值（这就是所谓的 k 回退…），直到找到符合重合的子串或者 k == -1。</p><p><br></p><p>至此，算是把求解数组 next 的算法弄清楚了（其实是，终于把 k = next[k] 弄懂了…）</p><p><br></p><p>因为这个算法神奇难解之处就在k=next[k]这一处的理解上，网上解析的非常之多，有的就是例证，举例子按代码走流程，走出结果了，跟肉眼看的一致，就认为解释了为什么k=next[k]；很少有看到解释的非常清楚的。</p></div>
        <footer>
                <div class="horizon-line"></div>
                <img id="logo" src="/assets_dweb/logo@1x.png">
                <div class="text">知识星球</div>
                <div class="horizon-line"></div>
        </footer>
        <div class="qrcode-container">
            <img class="qrcode" id="qrcode">
            <div class="text-desc">扫码加入星球</div>
            <div class="text-desc">查看更多优质内容</div>
        </div>
        <div id="qrcode-url">https://wx.zsxq.com/mweb/views/joingroup/join_group.html?group_id=88885281525452</div>
        <input type="hidden" name="group_allow_copy" value="true" />
        <input type="hidden" name="group_enable_watermark" value="true" />
        <input type="hidden" name="member_id" value="812511188254442" />
        <input type="hidden" name="member_name" value="恍惚" />
        <input type="hidden" name="member_role" value="other" />
    </div>
    <div class="message-container-overlay">
    </div>
    <link rel="stylesheet" href="./css/styles.css" />
    <link rel="stylesheet" href="./css/article.css" />
    <script src="/js/jr-qrcode.js"></script>
    <script src="/js/content-protection.js"></script>
    <script src="/js/article_dweb.js"></script>
</body>
</html>
希望这篇文章可以帮助到大家。这也是我在学kmp时看过的一篇很详细的文章。<e type="web" href="https%3A%2F%2Fwww.acwing.com%2Ffile_system%2Ffile%2Fcontent%2Fwhole%2Findex%2Fcontent%2F6255932%2F" title="AcWing%20831.%20KMP%E5%AD%97%E7%AC%A6%E4%B8%B2%20%E2%80%94%E2%80%94%20%E6%B7%B1%E5%85%A5%E6%B5%85%E5%87%BA%20next%20%E6%95%B0%E7%BB%84%20-%20AcWing" />[强][强][强]