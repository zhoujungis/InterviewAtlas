# 美图 · 算法/AI

> 共 **23** 条 ｜ [返回总目录](../../README.md)

---

## 美图多模态算法面经（二编）

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-09-14 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/2ceab76f02034ccfb530ee55be35a089)

🎓学历背景：28届双非本
👨‍💻意向职位：多模态算法
📍求职类型：日常实习
🔑问题：
1、自我介绍
2、实习拷打（b站视频生成业务）
3、视频局部重新生成流程
4、反问：业务、每周实习时间、学校放实习吗

无八股无手撕，无深度学习内容

9.14一面，等后续
9.18告知横向，前面有一个高优先级

---

## 妙鸭相机爆款增长叙事已经彻底终结：第一代 C 端 AIGC 产品为什么留不住用户？

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-06-30 ｜ [原文链接](https://www.nowcoder.com/discuss/901572070314688512)

写在前面

 

 
 【WeThinkIn出品】栏目专注于分享Rocky的认知思考与经验感悟，范围涵盖但不限于AI行业。

 
 
 干货AIGC、AI Agent、LLM算法工程师/开发工程师面试面经秘籍分享（持续更新）： WeThinkIn/AIGC-Interview-Book 欢迎大家Star～

 

 大家好，我是Rocky。

 妙鸭相机又一次被推回了 AI 圈的视野。

 这一次，不是因为它又生成了什么惊艳写真，而是因为一组关于“团队解散”“最低程度运营”的截图开始流传。截图里提到，虎鲸文娱旗下妙鸭相机团队疑似已于 2025 年 9 月底解散，产品不再进行升级和运营推广，只保留最低程度运营；最初带队的产品负责人张月光，也早已离开原项目，转向新的 AI 创业。

 

 这件事真正值得讨论的，并不是“一个 App 是不是还活着”，而是第一代 C 端 AIGC 爆款为什么没能把热度变成长期产品。

 把它理解为爆款增长叙事终结、团队创业状态结束、产品不再拥有清晰第二曲线，那么妙鸭相机实际上的产品生命周期已经进入尾声。

 Rocky认为，妙鸭相机不是简单“做不下去了”，而是第一代 C 端 AIGC 爆款完成了它的历史任务，却没能长成一个能跨周期延续的产品。 

 它不是因为 AI 不够强而走到尾声，而是因为 AI 变强太快；不是因为完全没有用户，而是因为用户没有足够强的理由回来；不是因为没有商业化，而是因为商业化结构太薄，薄到只能支撑一次性尝鲜。

 在本文中，Rocky将深入浅出本质讲解分析，妙鸭相机为什么能在 2023 年迅速爆红，为什么又会在热度过去之后迅速失速，以及这件事对 C 端 AIGC工具和 AI 产业意味着什么。

 一、妙鸭的高光：9.9 元买一次“AI 照相馆革命”

 从现在回头看，妙鸭相机在 2023 年 7 月的爆红不是偶然。

 妙鸭相机于 2023 年 6 月 30 日开始邀请制内测，7 月 17 日正式上线；用户上传 20 张以上包含人脸的照片，支付 9.9 元，选择模板和造型后，就能生成自己的“数字分身”和写真作品。在当年 8 月的多家媒体采访报道中也提到，妙鸭来自阿里大文娱内部项目，由张月光带队，早期以小程序形态存在，内测主要从同事和身边朋友开始。

 这个产品踩中了 2023 年中国 C 端 AIGC 的三个情绪点。

 第一，用户第一次感到“AI 不是只能写段文字、画张图，而是真的能生产一个和自己有关的消费品”。AI 写真不是抽象能力展示，而是可晒朋友圈、可做头像、可被亲友评价的社交货币。

 第二，9.9 元的定价击穿了线下写真价格锚点。它不需要真的替代海马体或天真蓝，只要让用户觉得“花一杯奶茶钱试试也不亏”，裂变就能启动。

 第三，AIGC图像创作技术在那个时间点刚好从研究论文、极客工具和AI行业探索破圈，进入普通人的消费界面。Stable Diffusion 已经把文生图带到大众视野，LoRA、ControlNet、Adapter等可控生成技术让“给模型看几张自己的照片，它就能在新场景里画出自己的写真”变得可理解，LoRA 又让个性化微调的成本和门槛明显下降。 妙鸭不是这些技术的发明者，但它把复杂技术包装成了一个极其简单的消费动作：上传照片，付款，等待出片 。

 这就是妙鸭的历史意义。它让很多中国用户第一次意识到，AIGC 不只是内容平台的新滤镜，而可能是一个新的内容工厂。

 问题在于，这类产品的价值曲线天然是陡峰低谷，爆红越快，衰减也越快。 

 二、它不是不够 AI，而是太像一个 AI 魔术

 Rocky认为，妙鸭的核心体验可以概括为八个字：个体保持，模板生成。 

 用户提供多张自拍，系统学习这个人的面部特征，再把这个“人”放进不同风格的写真模板中。技术上，它接近基于少量参考图像的主体驱动生成和个性化扩散模型能力。DreamBooth 论文提出的方向，正是让模型通过少量主体图片，在新场景、新姿态、新光照中生成保持主体特征的图像；IP-Adapter 则代表了另一类更轻量的图像提示控制路线；LoRA 作为低秩适配方法，也成为后来图像模型个性化和风格化微调的重要工具之一。

 这些技术在 2023 年足够惊艳，但它们的缺陷也非常明显：一旦底层模型、控制工具和开源工作流快速成熟，应用层的单点能力就会迅速商品化，剩下的只会是更难复制的工作流、分发和信任。

 Rocky认为这就是妙鸭增长叙事松动的第一层原因：技术震撼没有沉淀成技术壁垒。 

 一个 AI 应用真正的护城河，通常不在“我能不能生成这张图”，而在更靠后的地方：我是否拥有足够高频的用户入口，是否拥有独特数据，是否沉淀用户资产，是否嵌入不可替代的工作流，是否能持续供应审美，是否有渠道和品牌信任。

 妙鸭的答案并不理想。

 它有生成能力，但没有形成足够强的后续工作流。用户做完一套写真后，并不会自然每天打开它。它有数字分身，但这个分身没有成为用户长期身份资产。它有模板供给，但模板很容易被竞品、开源工作流和平台型影像工具复制。它有社交传播，但没有自己的强关系链，传播发生在微信和朋友圈，用户心智却不一定留在妙鸭。

 所以妙鸭最尴尬的地方在于：它越像魔术，用户越容易在看完第一场后离开。魔术的价值在“第一次不敢相信”，产品的价值却在“第十次仍然需要”。 

 三、C 端 AI 写真的商业悖论：传播很高频，需求很低频

 妙鸭早期最有争议、也最有前瞻性的选择，是上线第一天就收费。

 据证券时报报道，张月光当时解释过商业化前置的逻辑： AIGC 改变的是生产方式，AI 像工厂，如果第一天收不到用户钱，后面也很难收到 。 Rocky认为这个判断在大方向上并不幼稚 。AI 应用的确很难完全照搬移动互联网“先免费圈用户、再靠广告或增值服务变现”的路径，因为每一次生成都对应算力、模型、审核和客服成本。

 但妙鸭的困境也恰恰在这里：它证明了用户愿意为第一次惊艳付费，却没有证明用户愿意为长期使用持续付费。 

 AI 写真天然高传播、低频次。它适合刷屏，适合炫耀，适合“你也来试试”，但它不天然适合复购。一个用户可能愿意花 9.9 元看看 AI 眼中的自己，甚至愿意再买几套风格模板；但当头像、朋友圈九宫格和社交新鲜感都被满足后，下一次强需求什么时候到来？

 **这里有一个看似反常、实际很核心的矛盾：**AI 写真越便宜，越不像“人生纪念”；越像本人，越引发隐私焦虑；越不像本人，越失去产品价值；越模板化，越容易规模化；越规模化，越容易审美疲劳。

 妙鸭其实同时面对三类成本，而这三类成本都不是一次性发生的：

 
 生成成本 ：算力、推理、模板和内容审核。

 留存成本 ：用户做完一次以后，为什么还回来。

 信任成本 ：用户愿不愿意把人脸照片继续交给你。

 
 供给侧也没有想象中轻。妙鸭爆红时，有媒体曾报道过用户等待时间过长、算力扩容、成本可控但盈亏状态未披露等问题。AI 生成不是传统互联网里复制一份内容的边际成本，它至少包含推理成本、个性化训练或适配成本、素材与模板成本、内容安全成本，以及用户不满意时的客服和退款压力。

 2023 年，妙鸭 iOS 端曾登上应用榜高位，但 8 月中旬后排名下滑，截至 11 月 13 日，其 iOS“社交”榜单排名降至 64 位。这个数据来自第三方榜单，不能当作官方经营数据， 但它揭示了一个朴素事实：爆款传播曲线和长期留存曲线是两回事 。

 朋友圈刷屏解决的是“知道你这个产品”，不是“需要你这个产品”。C 端 AI 应用最难的不是让用户来一次，而是让用户持续回来。

 

 四、真正让增长叙事松动的，是定位摇摆

 妙鸭并不是没有意识到“尝鲜式产品”的风险。

 在 2023 年 8 月的一个媒体采访中，张月光提到，妙鸭希望成为“基于 AI 的摄影摄像美学平台”，并强调并非要替代海马体、天真蓝等，而是希望与摄影摄像行业共生，甚至计划推出面向 B 端的工作站，邀请设计师参与模板设计内测。

 这个方向逻辑并不差。问题是，它同时指向了三个完全不同的产品物种：

 面向 C 端，它像一个 AI 写真玩具，核心是低价、惊艳、分享。

 面向 B 端，它需要像生产力工具，核心是稳定、可控、可批量交付、能融入摄影机构和设计师流程。

 面向社交和时尚，它又想变成一个“变美社区”，核心是内容供给、关系链、达人生态和日常使用频次。

 这三个方向都能讲故事，但很难由同一个小团队同时打穿 。更现实地说，三条线任何一条只要没做成稳定用户/客户留存，另外两条就只能不断补洞，而补洞本身并不能生成新的护城河。

 Rocky认为，定位摇摆不是“想做的太多”，而是“没有一个场景真正完成从试用到持续用户留存的闭环”。 

 App Store 的版本历史很有意思。2025 年以后，妙鸭的更新记录里出现了视频写真、AI 美颜、传图面板、色彩测试、灵感社区、好运日推、数字分身免费版和专业版等功能。2026 年 1 月的版本说明甚至把产品描述推向“AI 时尚社交新阵地”，强调色彩测试、穿搭方案、灵感社区和视觉焕新。

 这说明妙鸭不是没有迭代。相反，它在努力寻找第二曲线。

 但这也说明，原来的“AI 写真”已经不够了。产品不得不从写真生成扩展到美颜、社区、穿搭、运势、视频和会员。这些功能未必错，却暴露了一个更深的问题： 妙鸭再也没有找到一个比“第一次生成写真”更强的核心场景 。

 AI 产品最怕的不是功能少，而是主场景松松的 。一旦主场景松了，迭代就容易变成外延堆叠：今天加社区，明天加测试，后天加会员，最后用户反而更难说清它到底是什么。

 妙鸭不是没有升级，而是没有把升级变成新的必需品。

 五、组织问题：大厂内部创业项目的天然尴尬

 妙鸭的故事还有一个重要背景：它不是纯独立创业公司，而是阿里大文娱内部孵化出的项目。

 大厂内部创业的优点很明显：能拿到品牌背书、技术支持、算力资源、合规能力和组织协同。妙鸭爆红初期，算力扩容和数据安全回应背后，阿里大文娱体系的支持显然是重要资源。

 但大厂内部创业也有天然尴尬。爆红之后，一个项目需要快速完成独立产品、增长、运营、商业化、内容供给、合规治理和品牌公关的全链条建设。它既要像创业公司一样快，又要像大厂项目一样稳；既要承担公众关注，又要服从组织优先级；既要自我证明，又很难完全掌握资源调度。

 2023 年 11 月，有多家媒体报道称，妙鸭相关人士确认产品负责人张月光离职，同时回应“项目本身照常”。

 这不是说张月光离职直接导致妙鸭进入尾声。一个成熟产品不应该把命运完全绑定在单个产品经理身上。

 但对一个刚刚爆红、还没有完成产品定义和商业闭环的内部创业项目来说，核心产品叙事的原始推手离开，必然会增加组织惯性。尤其是当产品从“爆款”进入“苦活”阶段，后面要做的不是开发布会，而是修留存、降成本、扩模板、做复购、扛合规、找第二曲线。 这些事都不性感，却决定产品能不能活 。

 Rocky认为，很多 AI 应用不是突然停止的。它们往往是先失去叙事，再失去资源，最后只剩最低程度的系统维护。 

 六、为什么美图能活得更稳：AI 影像不是不能商业化，是一次性写真太薄

 妙鸭增长叙事终结，不等于 AI 影像赛道不行。恰恰相反，AI 影像仍然是最容易被普通用户理解、最容易产生付费冲动的 AI 场景之一。

 关键差别在于：你卖的是一次性惊喜，还是长期工作流？

 美图是一个很好的对照组。根据美图公司 2026 年 3 月发布的 2025 年度业绩，2025 年美图持续经营业务收入 38.6 亿元，经调整归母净利润 9.65 亿元；影像与设计产品收入 29.5 亿元，占总收入 76.6%；截至 2025 年底，全球付费订阅用户数达到 1691 万。

 这组数据说明两件事，或者更准确地说，说明了两种完全不同的产品命运。

 
 
 
 维度 
 妙鸭相机 
 美图 
 
 
 
 
 核心价值 
 单次 AI 写真、数字分身 
 影像编辑、设计、视频、订阅 
 
 
 使用频次 
 低频尝鲜 
 中高频工作流 
 
 
 付费逻辑 
 一次性门票 
 持续订阅与增值 
 
 
 护城河 
 爆款传播和模板创意 
 用户入口、编辑习惯、产品矩阵 
 
 
 为什么能活 
 解决一次新鲜感 
 嵌入长期视觉工作流 
 
 
 
 第一，AI 影像不是没有商业化 。用户愿意为变美、修图、视频、设计、电商素材和生产力场景付费。

 第二，能持续商业化的不是“生成一张好看的人脸写真”，而是“用户能够持续根据需要处理图像、视频和视觉内容” 。美图有长期用户、有编辑习惯、有订阅体系、有全球化产品矩阵，也有电商设计、口播视频、线下门店等生产力场景。AI 对它来说不是单点魔术，而是嵌进高频入口和付费体系的能力升级。

 2026 年发布的全球消费级生成式 AI 应用榜单也提到，AI-first 与传统软件的边界正在变模糊。CapCut、Canva、Notion、Picsart、Grammarly 等传统或平台型产品，都在把生成式 AI 变成核心体验的一部分。 换句话说，未来的赢家未必是最早喊出“AI 原生”的应用，而可能是那些已经掌握用户入口、工作流和付费关系的产品 。

 这对妙鸭尤其残酷。

 妙鸭代表的是第一代 C 端 AIGC 爆款：一个清晰、惊艳、可分享的 AI 单点能力。美图、Canva、CapCut 代表的是另一条路：把 AI 变成成熟产品体系里的生产力部件。前者像烟花，后者像电力。

 烟花很亮，但电力才会进入日常生活。

 

 七、妙鸭给 C 端 AI 创业者的 5 个提醒

 Rocky认为，妙鸭相机的爆款增长叙事终结，不是一个产品被简单否定，而是 2023 年那批“AI 套壳爆款”的成人礼。 

 它提醒所有 C 端 AI 创业者，今天做 AI 应用，不能只问“这个能力够不够惊艳”，还要问五个更硬的问题。

 第一，用户为什么持续长期回来？

 Rocky认为，如果答案只是“因为生成效果好”，那就很危险 。生成效果会被基础大模型持续抬高，今天惊艳，明天就是标配。产品必须有复用场景、资产沉淀或工作流依赖。

 第二，用户为什么付第二次钱？

 一次性付费可以验证新鲜感，复购和订阅才能验证价值。AI 应用要么解决高频问题，要么解决高价值问题，最怕的是低频又低价值，只能靠热点续命。

 第三，通用大模型的迭代优化为什么不能顺手吃掉你？

 当多模态大模型、图像编辑大模型和手机系统级 AI 越来越强，单点生成能力会越来越难独立存在。应用层必须拥有场景、数据、分发、品牌或行业流程，否则迟早被基础设施吞掉。

 第四，组织是否愿意陪你过冷启动后的苦日子？

 AI 爆款最容易获得掌声，也最容易在掌声之后暴露真实问题：成本、留存、客服、审核、合规、供给、迭代节奏。产品真正难的部分往往发生在热搜之后，而不是热搜当天。

 妙鸭相机不是一个笑话。相反，它是中国 C 端 AIGC 早期最值得复盘的样本之一。它找到了足够好的破圈场景，也证明了普通用户愿意为 AI 生成内容付费；它失败的地方不在“没有价值”，而在“价值没有长成习惯”。

 所以讨论妙鸭相机真正要说的，不是某个 App 消失了，而是一个阶段结束了。

 Rocky认为，那个阶段里，AI 应用只要把一个能力包装得足够新奇，就能刷屏、融资、拿到用户和媒体关注。下一个阶段里，AI 应用必须证明自己不只是会表演魔法，而是能进入用户生活和产业流程。 

 妙鸭相机不是输在 AI 不够强，而是卡在 AI 变强太快。当魔法变成基础设施，卖魔法表演的人必须变成真正的服务商。

 如果把这件事放到更长周期看，Rocky的判断是： 工具红利会退潮，认知红利会抬头。 谁能把单点能力做成工作流，谁就更容易穿过一轮又一轮大模型换代。

 更具体一点说，妙鸭的价值不在于它曾经火过，而在于它把一件事讲得很清楚： AIGC 中场之后，单点工具会被更强的基础大模型吸收，能留下来的只有工作流、分发渠道和用户信任。 

 所以，妙鸭相机的真正意义不在于它是不是一个被否定的案例，而在于它把行业分水岭提前摆在了桌面上： 能被复制的功能会被复制，能沉淀下来的习惯、分发和信任才会最终留下。 

 给不同人群的思考和经验

 
 对产品经理 ：不要把“能出图”当成“有产品价值”，真正要设计的是复购、留存和资产沉淀。

 对创业者 ：不要只盯着第一次传播，要尽早想清楚第二次、第三次为什么还会发生。

 对投资人 ：凡是靠单次惊艳起家的 AI 应用，都要优先问它的留存、单位经济模型和合规成本，而不是只看前期热度。

 对研发工人 ：技术能力会被平台和基础大模型吸收，最后留下来的，是对场景和业务的深度理解。

 
 妙鸭相机已经不再是那个值得每天追热点的产品，但它仍然是理解 C 端 AIGC 早期为什么会热、后来为什么会冷的一把很好的尺子。

---

## 美图北斗大模型算法岗面经

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-05-24 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/97060296dbfb4957908062b4bd898aba)

1️⃣一面
1. 介绍第一篇论文，reward model怎么设计。
2. 过程监督的信号具体是怎么设计的。过程监督的信号还能应用在哪些地方。
3. 如何保证强化学习的训练效率（平衡效率和稳定），grpo训练过程中出现了全0或者全1怎么解决。
4. 混合推理是怎么做的（OpenAI GPT-5），大模型在增强推理的时候如何保证通用数据不遗忘。
5. 现在大模型还有那些能力值得增强。
6. 介绍第二篇论文
7. 介绍第一段实习，介绍落地的场景。
8. 写题，非hot100的模拟
 
2️⃣二面
1. 介绍第二段实习，中间会打断提问，问看过qwen2.5‑vl的报告了吗，问具体业务细节，强化学习数据集的构建方法，问部门几个人
2. 介绍第一段实习，主包这一段实习是基座的，问了很多部门的情况，包括后训练、预训练、数据生成等等
3. 介绍第一篇论文，介绍背景和方法
4. 面试官感觉很真诚，共享屏幕介绍他们组的业务
 
3️⃣三面
1. 问是保研的吗，论文是研究生阶段发的吗，大四在干什么，研究生的毕业论文写好了吗，两篇论文是一个领域的吗
2. 介绍第一篇论文，中途打断，说不了解你们这个领域，针对强化学习的底层设计，怎么去设计的，强化学习能解决什么问题，强化学习每一轮用的数据是多少，模型用的多大的，用小模型做强化学习效果会好吗，实验室里有多少张卡，训练的时候都用了几张。
3. 研究生阶段在做科研时遇到了什么困难，花费时间最长的是哪个阶段，研究生有什么成功的经验，有没有失败的经历，发现某条技术路线不行。
4. 你认为未来会有什么新技术，还会有强化学习这种路线吗，agent调用工具时工具需要很多参数，幻觉现象很严重，未来可能会有什么解决方案
 
4️⃣四面
1. 共享屏幕介绍论文，面试官听不懂，打开word讲述，问论文的创新点，输入输出是什么。
2. 介绍第二篇论文。你的方法有泛化性吗，可以泛化到垂直领域吗
3. 介绍第一段实习，问有什么经验，有哪些失败的尝试
4. 介绍第二段实习，觉得我的介绍太平铺直叙了，说可以后面做个PPT

📳对于想求职算法岗的同学，如果想参加高质量项目辅导，提升面试能力，欢迎后台联系。

---

## 美图 AIGC算法实习一面分享

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-04-11 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/e9c3a25c100e402a91f34376b351c629)

发一下问题给大家参考，攒攒人品！有面试过同岗的朋友欢迎评论区交流
实习+项目拷打
1. 解决过拟合的方法有哪些
2. 你知道哪些归一化方法
3. 介绍一下自注意力的计算方法
4. 介绍一下LoRA的原理
5. 介绍一下ControlNet的原理

---

## 【无论文无实习面实习】美图（不是美团）cv算法一面

来源：牛客网 ｜ 类型：面经 ｜ 发布：2026-01-29 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/e7089725feef4e1793878f041beb515c)

45min
拷打项目
你的项目实现原理，你提到的多智能体写作项目的多模态是什么架构
你对图像质量的效果如何量化，为什么这么量化
我们这边业务方向偏艺术图像生成 扩散模型你了解多少，原理是什么样，尝试过打mask后生成和语义分割+CNN哪个效果更好么？ 为什么？
你觉得自己项目中哪个方面最值得一提？

做题，面试官人很好，先问你刷题咋样，我说不太行，给了道重排链表（刚好这几天在着重看链表，但其实还是没撕完，就把思路讲了下然后能写多少写多少，十分钟 对不起面试官）
反问：
要去做什么？在开发一个艺术类图像生成，感觉要朝着nano banana那种方面努力？
我的面试缺点及努力方向？ 如果要做生成，而非图像质量调优，应当对最近新技术有更深入了解和实践。

总结：面试官人真的真的很好，面试还是在牛客上面的233 我之前总是感觉准备不充分就去面试是不是不太尊重人家，但现在就把面试当来聊天 认识不同企业不同方向的陌生大佬然后聊聊技术 当然复盘和自我改进还是要做的

---

## 美图AIGC效果设计面经

来源：牛客网 ｜ 类型：面经 ｜ 发布：2025-10-20 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/7c5b07df23ac47b5887587208fdbcdf5)

讲述一次你在美术绘画中克服困难完成满意作品的经历和收获。
如何利用扎实美术功底为AIGC效果设计提供更优质的视觉基础?
当面对多种画风融合需求时，你会怎样进行插画风格的创新与融合?
说说你使用AI工具进行设计创作时，遇到过哪些挑战及解决办法?
在精通的设计软件中，如何运用其功能提升AIGC效果设计效率?
假如项目时间紧迫，具有强烈执行力的你会如何安排工作流程?
怎样在团队合作中发挥积极主动精神，促进AIGC项目顺利推进?
谈谈你对通过数据观察分析总结来优化设计方案的县体思路。
本科艺术类专业学习中，哪些课程对AIGC效果设计实践帮助最大?
如何看待海外效果项目经验在美图公司AIGC业务发展中的作用?
若有海外留学背景，讲讲在国外学习对设计审美和理念的提升。
负责AIGC效果落地，怎样建立有效的质量反馈机制以保障效果?
产出视觉创意制定规范时，怎样确保规范能在不同项目中有效执行?
参与全球化项目创意策划，如何与不同文化背景团队成员高效沟通?
分享一个你运用想象力将普通创意转化为精彩设计的实际案例。
扎实美术功底在应对AIGC快速变化的设计需求时有哪些优势?
当项目要求紧跟潮流画风时，你怎样快速学习并应用新风格
谈谈你对利用AI工具拓展AIGC效果设计创意边界的看法和实践

---

## 美图公司AIGC效果设计面经

来源：牛客网 ｜ 类型：面经 ｜ 发布：2025-10-12 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/86dce6e6c8724c6ea7c717861d5a659d)

1. 请先做个简单的自我介绍？重点介绍一下自己在美术绘画及相关领域的经历
2. 你最近5年的职业规划是什么，能否详细谈谈未来在AIGC效果设计方面的规划？
3. 你应聘这个岗位的优势是什么？劣势是什么？请各列举三点并详细说明
4. 为什么选择应聘我们美图公司的AIGC效果设计实习生岗位？说说你的想法
5. 能不能谈谈对我们美图公司产品以及AIGC所在行业的了解程度？
6. 你期望的薪酬是多少，对于实习生薪酬标准你有怎样的预期和考虑？
7. 大学期间最喜欢哪一门专业课程？为什么喜欢这一门对AIGC效果设计有帮助的课程？
8. 用三个词，总结一下这几年自己大学的经历，并且阐述为何选这三个词
9. 大学期间都参加过哪些社团或者学生组织?可否详细谈谈在其中的收获与体会？
10. 平时有什么兴趣爱好？有什么特长吗？这些对AIGC效果设计工作会有怎样助力？
11. 若负责AIGC相关效果落地，面对质量把控难题你会采取什么具体措施？
12. 在产出视觉创意时，怎样确保制定的相关项目设计规范符合公司要求？
13. 参与全球化项目创意脑暴及策划，如何精准抓取当地用户图像素材使用趋势？
14. 谈谈你对扎实美术绘画功底在AIGC效果设计工作中重要性的理解。
15. 举例说明你如何凭借丰富想象力在美术创作中展现独特风格。
16. 当项目要求不同插画风格时，你会怎样快速确定并实现相应风格绘制？

---

## 美图AIGC算法面试-社招

来源：牛客网 ｜ 类型：面经 ｜ 发布：2024-08-17 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/72164bc673a5418481cacd332307bfca)

你们美图算法面试一面结束多久能收到反馈的结果已。
已经等待了一个星期，是不是已经凉凉了 #算法# #AIGC# #美图算法# #美图面经# #社招#

---

## 美图 AIGC视觉算法 一面 30分钟

来源：牛客网 ｜ 类型：面经 ｜ 发布：2024-05-21 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/db7befcb438b4a93818c4121945be2e9)

5.6面的，是面试体验最差的一次，面试官的面相不是很好，而且我每次说完或者说不会都得等面试官10s说出他的下一个问题。。。 
介绍Controlnet ？它是怎么引导的
介绍DDPM？他预测的是什么？为什么可以直接预测噪声？讲一下那个公式
重参化知道吗
GAN和扩散模型区别？为什么扩散模型效果好
文本控制是怎么嵌入的？
注意力机制公式为什么除以根号d?如果不除会变成什么？
介绍VAE
VAE和AE的区别？
介绍LoRA
DDIM和DDPM区别
位置编码了解过吗？绝对的加在什么地方，qkv映射前还是映射后
旋转位置编码了解过吗？
无算法题，差不多30分钟结束
 #面经# #计算机视觉岗# #算法# #实习# #我的实习求职记录#

---

## 秋招总结

来源：牛客网 ｜ 类型：面经 ｜ 发布：2023-11-30 ｜ [原文链接](https://www.nowcoder.com/discuss/559559713378099200)

背景：双非本211硕 

 编程语言 c++ cuda python

 方向是 AI工程开发 算子开发 模型训练推理优化 AI编译器 深度学习框架开发 

 目标行业 互联网 半导体

 

 oc 

 深势科技 高性能计算

 浙江大华 算法移植

 集创北方（集郎）AI编译器

 星临科技 大模型训练推理优化

 唯品会 大模型训练推理优化

 元象唯思 大模型训练推理优化

 soul 大模型训练推理优化

 华为 AI工程师 2012中软 

 小米 AI编译器 

 美图秀秀 高性能计算 

 大疆车载 机器学习算法工程师 

 科大讯飞 算法工程师 AI框架方向 

 
 

 

 总结 

 一. 算法加速的工作相对来说不会像纯算法岗那么注重学历论文，本人无论文无专利 。薪酬对齐算法岗，注重相关领域的经验和基础知识

 二.半导体公司给予面试机会比较少，主要是AI开发， AI编译器相关岗位。今年是互联网回暖，但是半导体比起去年缩招了。今年是大模型元年，相关的岗位开的比较多，但是hc数量依然很少。

 三.算法加速倾向于开发方向，对于c++和cuda基础比较重视，适合有深度学习背景的同学

---

## 美图秀秀（北京）

来源：牛客网 ｜ 类型：面经 ｜ 发布：2023-08-21 ｜ [原文链接](https://www.nowcoder.com/feed/main/detail/9c7462bf0f344069b8f4ea6fce440d01)

计算机视觉：
一面40min:项目+手写自注意力+快排
二面30min:项目+八股+排序数组的两数之和
HR面8min
问题都很简单，HR口头offer

---

## CV算法工程师求职复盘

来源：牛客网 ｜ 类型：面经 ｜ 发布：2021-10-26 ｜ [原文链接](https://www.nowcoder.com/discuss/353158816990699520)

总览 

 本人秋招于8月21日开始投递，于10月22日尘埃落定，经历了整整两个月的时间，虽然拿到的offer不及大佬们，但是水平如此，也无太多遗憾。下面总结一下自己的秋招历程，也是写给自己的。祝愿仍在求职的同行者们都能拿到满意的offer，共勉。 

 基本情况：985本硕，研究方向为目标检测，项目经历两个，无论文无实习，offer四个[大厂只有小米一个，一个中厂以及其他行业的CV岗]。 

 面试是不断完善自己的过程 

 每一次面试后都应当及时复盘并查漏补缺。在我的另一篇帖子中，记录了一些面试知识点，这些知识点考察了不只一次，而我在求职前期对于不会的问题并没有做到下一次我一定能回答完美的程度，在遇到同一道题多次回答不出之后才意识到这点。 Coding很重要。回顾自己的面试流程，Coding不出来的无一例外全部挂掉。第一次面试时只刷了四五十道题，面试官出的题目是K反转链表，代码想半天还有错误。后续不断改进，对于CodeTop前100题代码能够做到全部背下来的程度（虽然也很菜）。但是如果是面试官自己出题没见过的就还是很难做出来，忍痛被挂掉。 保持良好的心态。虽然在这个过程中也会因0offer焦虑，也会因面试的完美发挥而得意。但是我相信自己最终是一定会拿到一个offer的，相信努力的准备笔试面试一定会有回馈的，所以自己也都沉浸在学习里，努力多背一个知识点，多刷一道题。 面试大类 

 

 对于很多公司（APP）来说，算法落地是首要目的。所以考察的知识点会涉及轻量化模型和模型压缩，还会考察你是否有模型部署的经验，c++代码能力等。[美图，小米，Soul] 一些公司直接接触图像端，会考察图像处理的知识。[一些公司的OCR部门，医疗行业] 一些面试官对你的论文项目进行深入探讨以及交流相关论文。[大厂面试官] 面试官大类 

 

 既是面试，也是交流。这类面试官对于你不会的问题会引导你回答、教给你答案，让你在面试后获益匪浅，很喜欢这类面试官。[基本上大厂面试官都如此] 纯为面试，单纯出题。这些面试官说出一个题目让你回答，对你的回答不做回应，你不会也不会有回应，毫无面试体验。 遗憾 

 

 最遗憾的面试应该就是百度了，一面过了但是因为时间冲突没有参与当天后续面试，结果再去联系已经泡池子了。 

 Note：百度是连环面，面试的同学应当把握好时间。 

 
 

 祝愿仍在路上的各位都能有满意的offer！！！

---

## 厦门美图之家科技有限公司2022届校园招聘

来源：牛客网 ｜ 类型：面经 ｜ 发布：2021-10-24 ｜ [原文链接](https://www.nowcoder.com/discuss/353158802189000704)

公司招聘动态、名企内推、笔面试题库及面经攻略

 
 请认准2021名企校招日程汇总： https://www.nowcoder.com/school/schedule 

 
 

 
 
 青春当燃，美“途”不凡
 

 
 美图2022届秋季校园招聘正式启动
 

 
 招聘对象：
 

 
 2022届毕业生

毕业时间（国内/海外）：（2021年11月—2022年10月）
 

 
 招聘岗位：
 

 
 技术研发类：iOS研发工程师、Android研发工程师、C++研发工程师、PHP研发工程师、测试工程师
 

 
 AI、数据类：计算机视觉工程师、算法工程师、大数据开发工程师、数据分析师
 

 
 设计类：效果设计师、素材设计师、视频特效设计师、3D效果设计师
 

 
 产品运营类：产品专员、运营专员
 

 
 工作地点：
 

 
 北京、厦门、深圳
 

 
 校招流程安排：
 

 
 在线网申 在线笔试 面试 offer发放
 

 
 9月1日开始 部分岗位需要 9月15日开始 面试通过后
 

 
 
 

 
 投递方式：
 

 
 方式一：网申地址：Meitu.hotjob.cn
 

 
 方式二：关注 “美图公司招聘” 微信公众号，点击“校园招聘”投递简历，了解美图公司更多详情
 

 
 
 

 
 
 

 
 关于美图：
 

 
 美图公司成立于2008年10月，是一家以“美”为内核、以人工智能为驱动的科技公司，通过影像产品和颜值管理服务帮助用户全方位变美，通过SaaS服务助力美丽产业数字化升级。2016年12月15日，美图公司在香港联合交易所（“联交所”）主板挂牌上市，股票代码1357。
 

 
 用户规模：
 

 
 月活近3亿 用户突破23.4亿 图片保存量60亿/月
 

 
 技术实力：
 

 
 ² 算法领先——在影像处理领域，美图的机器学习、计算机视觉、AI、AR等算法研究与产品应用能力始终保持行业领导地位；
 

 
 ² 核心技术——覆盖人脸识别、人脸检测、人体技术、图像识别、图像处理、图像生成、音视频技术等多个方面；
 

 
 ² 数据智能——行业领先的基于NLP和CV算法的内容理解、用户画像、推荐算法、搜索、push、反作弊、数据分析等大数据和智能计算能力；
 

 
 ² 注册专利——影像技术、计算机视觉领域注册超过451项专利，且专利数量仍在逐年提升；国际冠军——连年斩获计算机视觉领域多项国际顶级赛事及会议冠军，包括CVPR-NTIRE 2019图像增强赛道冠军，IC-CV-DeepFashion2 2019服饰关键点估计任务冠军，EC-CV-PIRM 2018图像增强技术比赛冠军，MICCAI-ISIC 2018皮肤癌病灶分割任务冠军等

---

## 内推--美图秀秀--数据挖掘工程师（北京）

来源：牛客网 ｜ 类型：面经 ｜ 发布：2021-06-01 ｜ [原文链接](https://www.nowcoder.com/discuss/353157984517824512)

内推~~ 简历直达面试官 

 
 

 美图秀秀是一款广受欢迎的图片处理软件，全球累计超过10亿用户，月活超过1.2亿，在摄影图像类应用中长期保持领先优势，目前美图秀秀已从单一的图片处理工具转型成为让用户变美为核心的社区平台。 

 
 

 美图秀秀--数据挖掘工程师（北京） 
 

 岗位职责： 

 1. 针对具体业务需求场景，分析和研究数据，挖掘用户分类、用户生命周期、用户流失、用户价值、用户行为预测、用户兴趣、人群包挖掘等。 
 
 任职要求： 

 1. 有2年以上工作经验。 

 2. 熟练掌握数据挖掘、机器学习的基础理论和方法； 

 3. 了解Hive/Hadoop/MapReduce/Spark等常用大数据处理工具优先； 

 4. 熟练掌握至少一种编程语言:Java/Scala/Python，熟悉Linux系统及常用Shell命令； 

 5. 有互联网公司有大规模用户画像实践经验,参与过用户画像建模； 

 6. 有良好的数据直觉，善于协调数据信息资源 
 

 
 

 工作地点：北京市海淀区-五道口-优盛大厦B座7层 

 
 

 简历可投递邮箱：hml2@meitu.com

---

## 秋招回忆录

来源：牛客网 ｜ 类型：面经 ｜ 发布：2020-12-30 ｜ [原文链接](https://www.nowcoder.com/discuss/353157452441001984)

秋招回忆录-在自我否定中摸索

 我的秋招终于在12月中旬结束了 

 其实很早就想写点东西记录一下今年的春招+秋招的经历，由于各种问题，现在才开始写。

 个人情况的介绍
双211的硕士（在人均大厂offer，人均985的渣硕中，我觉得我还真配不上称渣硕），非科班，不是工科，本硕都是数学。主要投算法岗位（也想投开发，但是我真的没学过）。方向小众，有两篇JCR A区的文章（两篇IF加起来超过10），拿到了国奖，有两段实习，都是做的算法预演工作，一个很小的公司，一个中厂。 直接给结论：投算法大厂全跪，基本都是做完笔试直接没消息，即使全A编程题。小公司更是看学历招人，面试体验极差。

 所以这是一个算法劝退贴，特别是像我这种学历不行，课题组就老师自己单打独斗的情况下，要想拿到大厂的offer，做开发的难度要比算法小 结合个人今年的经历，给后来者（特别是迷茫的同学）一点借鉴的经验。

 春招实习

 由于疫情的原因，今年上半年1，2月在家特别放松，啥都不考虑。3，4月忙着把论文做完。期间4月份的时候，我本科的同学有询问我是否投了暑期实习，我那时还不太想投，主要是前段时间一直忙论文，leetcode啥的都没刷过（对于很多理科同学，基本很少去刷题），胆怯心理就一直拖着没投实习。每天刷刷题。到了5月份，来牛客投实习，发现大公司基本都不找暑期实习，特别是让之前的同门师姐内推华为的实习，直接hr劝退，心态直接爆炸，连着一周多的时间每天晚上睡不着。感觉自己能力也不差，也有两篇A区的，不应该这样呀。在牛客上看了很多3个月转后端的帖子，决定转后端开发（也考虑过测试，侧开之类的），狂学了一周的JAVA，每天8点起床看书，2点多才睡觉，还要在父母面前表现出自己不担心工作，免得他们担心。在这一周中，我意外接到了两个面试， OPPO研究院和美图 。OPPP面试就是讲自己做的东西，美图更多的考察算法实现能力。OPPO的实习offer异常的顺利拿到。但是由于前面找实习的碰壁，考虑要不要去实习，而且我也开始学后端了。纠结再三，还是又转回了算法，在算法中，我有文章可以跟面试官聊聊，在后端中，我从没做过后端开发，没有项目，不知道能和面试官啥。

 给明年秋招的小伙伴的建议：过年后大公司春招实习马上就开始了，自己一定要赶早，hc本来就很有限，投的越晚越困难，投到前面了，即便过不了也能骂醒自己，积攒经验。

 实习中

 其实实习本没啥好说的，好好实习，努力工作，争取转正呗。但是在努力工作的同时，一定要知道自己实习的组到底有没有hc给实习生转正。也要自己判断。不要孤注一掷，或者过于乐观。不管实习期间工作再忙，也要每天都刷leetcode（像我这种编程基础跟科班完全比不了的，至少把 剑指 刷一下，以及LeetCode的 hot100 的题目）。

 此外实习期间一般在6,7,8这3个月，同时这个时间段也是大厂的提前批集中的时间段。我自己犯的错误是：觉得实习期间就认真实习，做好实习的题目，不想去投其他的公司，不想三心两用。导致错过了提前批这个很好的锻炼的机会。

 给明年秋招的小伙伴的建议: 实习期间，一定要关注好是否转正这个信息，及时止损，此外一定要投递提前批，哪怕和实习工作冲突了。

 秋招（正戏）

 9月份回学校，开始秋招。海投了很多公司，一部分都给了笔试，其中也有不少连笔试机会都没给，不管是大公司还是小公司。 这时候深深的感觉到算法岗对于出身的看重 。只有几个公司给了面试机会，除了个小公司都拿到offer了。面经如下，其实算法岗，特别是我这种就看论文，写论文了，其实没啥特别好问的，一般都是讲自己的论文。

 华为（最想去）已拿offer 面试时间：9.12

 华为面试有点拖沓，体验一般
一面：由于华为那边出了故障，导致我和面试官不在一个zoom中，耽误了点时间，因此面试官为了节约时间，没有复盘笔试（一般要复盘的，所以大家记得面试前复习好）。面试官直接让共享自己的论文，对着论文讲，讲idea，讲实习。最后就是手撕代码，自己思路对了，有个书写小错误，（我都能写出来的，题目很简单，后面的同学多刷leetcode就没事）

 二面：上来直接手撕代码，问了问时间复杂度。然后共享论文开始讲。后面问了问成绩，有没有比赛啥的，由于我自己一直都是单打独斗，参加过一次CCF大赛，成绩很差，就没在参加过比赛，做论文去了。 建议：想投算法，还是要做做比赛，kaggle，天池，有条件可以搞搞顶会的比赛 

 三面：就是最玄学的主管面，本来会问问项目啥的，但是由于我在友商实习，主管说因为存在竞争，他就不问了。聊天，问的问题无外乎：家里的情况，意向地，职业规划。遇到问题的处理方式，这块大家尽可能真诚回答的同时，表现出自己的思考能力和自己的能力。一个事情有很多解决方式，尽可能表现出自己的独立思考的同时也不闭门造车。

 对华为的吐槽： 真的能拖，池子真深，等了整3个月。

 浙江大华 已拿offer 大华都是电话面，会有短信通知，1-2天内有电话面试。但是时间不确定就有点难受。一面时在做广联达笔试，直接打过来电话要面试，直接放弃笔试。整体效率很高。

 一面：一个声音很好听的小姐姐，面试体验很好，一直有引导，包括最后跟我聊了聊算法从业人员这两年的现状。好感度max。面试同样是先讲自己的论文和实习。然后由于我是数学的，面试官问了几个知识点，希望我在数学推导方面来解答。大概记得问了SVD分解，交叉熵，sotfmax。一开始答得不是很好，还是给我过了。

 二面：在外面的时候，直接一个电话面试，唉！赶紧找了个星巴克，常规的讲论文和实习。一些深度学习的知识点。过拟合啥的。

 三面：就是HR面，基本就是问问意向，家庭情况，情感情况，期望薪资（多看看os，免得少了再想调薪很困难）

 面试评价： 有效率

 中兴
本来中兴的笔试安排在华为面试那天，我就鸽了。后续突然问我想不想面试一下，就面了面，面试内容，同样论文+实习开始讲，成绩，获奖啥的。面完没多久主管打电话来聊，由于要转方向到NLP或者语音识别，考虑了几天还是跟主管拒了，给的价在中兴给的中算高的（没报蓝剑，跟大佬没法比）

 广发研发中心（佛山）

 面试时间比较短，1面技术面+线下宣讲会的总经理面试。技术面也还是讲论文和实习，面试官没问啥问题，就问了有啥offer。线下跟总经理聊，聊得挺好，人家主动加了我个微信，但是后续我没交体检，放弃了。还是不太想太早去银行。

 美菜网
无意中投的，1个技术面，跟之前面试完全不同，从408开始问，对于我这种非科班的选手，真的煎熬，虽然自学过408的课程，但是一直没被问过，所以也没再看看，答得很不好，面试官态度很好。我自己觉得凉透了，但是11月多突然有hr打电话问我三方情况，因为已经签了其他的，所以就拒了

 58同城（一面通过，时间冲突调了一下二面时间，结果之后再无消息）
一面通过没消息是真的骚，说好了第二天面试，等邮件就好，然后就没有然后，关键官网显示一面通过。
一面：论文+实习，实习做的人脸，因此多聊了聊这块的问题，然后就是根据自己的简历提到的技能点提问，例如框架的问题，机器学习的问题，linux的常规操作

 玄武科技（体验差到再也不想投小公司）
面试体验真的是，在腾讯会议等了快两个小时。面试官进来直接说不用介绍了，节约时间，我问你答（心中万千曹尼玛）。随便问了问论文的问题，然后说我们不做这块内容，我追问他们做什么，说是做检测，分类（现在的人脸的算法不就是基于分类嘛）。恶心到了，面试5分钟结束。

 还有就是中国移动研究院要求现场面试，拒绝了，人寿研发中心面试等了2个多小时还排不到，不面了。

 后秋招（心态起伏）

 整个秋招就面试了这几家，其他的要么笔试过后没消息，要么就是简历直接挂。深深的体会到算法岗对于学历，学校要求真的苛刻。相比开发，其实也没性价比，尤其是12月初的时候，在看os，脉脉。牛客时，心态一度爆炸。对于名校，大牛的组，论文，项目都是充足的，对于下面的学生算法这条路真的难走（对于想去大厂的同学）。这两年多的研究生生活，不敢说很勤奋，至少没有过假期，元旦，周末都不敢想。一直看论文，做实验。像数学这类理科，基本也就没有项目，主要还是做理论。如果这些时间花在后端上，觉得自己应该也能试试大厂的面试，不像现在连面试机会都没有。但是这也这是假设。自己大学成绩一般，从毕设开始做图像到现在，还是想做图像，可能做后端自己并没有太多兴趣，而且要和正科班的同学竞争，我也不会有啥优势。

 华为是我一直想去的，我一直觉得图像的落地一定是在嵌入式，我自己从没学过嵌入式，所以想去华为来做图像算法。此外二线城市中，华为算是薪资给的很可观的，后期还是想着逃离北上广，回到压力相对小的城市，像杭州，武汉，定居结婚生活。人总是很贪心，没拿到大厂offer时，想着大厂offer，拿到大厂offer，又想着sp offer。调整了一周的心态，开始生活进入正轨，学点自己想学的知识，看看检测的工程代码，看看推荐的算法。在最后的半年的时间，主要为了开阔视野，开阔知识面。

 总结

 写了很多废话，不知道到以后的同学有没有帮助。这是个劝退贴，当然，我的秋招也有今年情况特殊的原因，也曾考虑过不行读博去，但是还是想工作。

 写给想做算法去大厂的同学

 出身好，能力强，那努力准备，大厂offer收割机 出身一般，又想去大厂，问问自己是否真的想做算法，不然及时转后端，可能是去大厂好的选择 真的想做算法的同学，借用我在B站UP“稚晖君”的主页看到的一句话“十年饮冰，难凉热血”，加油，一直充能，厚积而薄发。 一点题外话

 写完这些，重新读了一遍内容，回顾了今年的经历的事，觉得自己挺对得起自己的id，性格像个鸵鸟，不管是学习工作上，还是情感生活上。就谈过一次恋爱，还被无缘故的分手，从此感情上变得渴望但自卑。希望有经验的同学，能给点建议，咋和女孩聊天之类的。之前在牛客上许愿过华为的offer，第二天就接到了意向电话。希望牛客再给带来点好运，祝我找个女朋友。（是不是有点贪心了，哈哈哈）

---

## 2020届秋招面经分类汇总（分类：各个岗位（技术&非技术））

来源：牛客网 ｜ 类型：面经 ｜ 发布：2019-08-27 ｜ [原文链接](https://www.nowcoder.com/discuss/353155299374735360)

2020届秋招面经分类汇总（分类标准：各个岗位（技术&非技术））

 个人整理的2019&2020的秋招汇总，按技术和非技术分类，可以直接用ctrl+f直接搜索跳转。祝各位师弟师妹秋招顺利，加油！！！

 插一条内推信息 ：三七互娱2020届校招（含内推码） 

 技术：java、C++、python、IOS、Go、安卓、测试&测开、大数据、安全、运维、前端、游戏研发、算法、机器学习、架构、全栈、嵌入式、数据分析、数据挖掘、

 非技术：产品、管理、管培生、设计、游戏策划、游戏运营、营销

 技术

 JAVA

 【Java】华为 成渝IT软件开发java方向： https://www.nowcoder.com/discuss/99229 
【java】小红书凉经，很详细，攒人品： https://www.nowcoder.com/discuss/116085 
【Java】2018年9月28日顺丰java远程一面： https://www.nowcoder.com/discuss/120367 
【java】顺丰面经： https://www.nowcoder.com/discuss/113396 
【java】顺丰提前批java开发视频面 一面 https://www.nowcoder.com/discuss/88758 
【java】顺丰科技一面面经(内推-Java开发岗) https://www.nowcoder.com/discuss/88782 
【java】顺丰Java一面面经 https://www.nowcoder.com/discuss/88786 
【java】顺丰科技一面面经（说好的问的少呢。。。） https://www.nowcoder.com/discuss/88851 
【java】顺丰内推面Java研发 https://www.nowcoder.com/discuss/88909 
【java】顺丰科技Java技术面面经 https://www.nowcoder.com/discuss/90043 
【Java】顺丰java一面面经 https://www.nowcoder.com/discuss/90726 
【java】顺丰科技面经(HR面) https://www.nowcoder.com/discuss/90564 
【java】58到家 面经 一面挂： https://www.nowcoder.com/discuss/116113 
【Java】【蚂蚁金服】一面挂经，大数据开发java岗 https://www.nowcoder.com/discuss/94574 
【java开发】蚂蚁金服面经 https://www.nowcoder.com/discuss/88079 
【java开发】 蚂蚁三面面经，java开发岗 https://www.nowcoder.com/discuss/92118 
【java】cvte一面： https://www.nowcoder.com/discuss/114028 
【java】cvte 7.26一面面经(电话面) https://www.nowcoder.com/discuss/88476 
【java工程师】cvte面经 挂在hr https://www.nowcoder.com/discuss/91277 
【java后台】CVTE Java后台电话一面 https://www.nowcoder.com/discuss/89961 
【java】CVTE Java后台开发一面二面,攒人品和运气! https://www.nowcoder.com/discuss/92317 
【java】美团点评西安站凉面筋： https://www.nowcoder.com/discuss/113872 
【java】美团 西安9.20求个offer： https://www.nowcoder.com/discuss/117440 
【java】美团点评西安站凉面筋： https://www.nowcoder.com/discuss/113872 
【java】美团 西安9.20求个offer： https://www.nowcoder.com/discuss/117440 
【java】美团123面+hr面： https://www.nowcoder.com/discuss/111179 
【java】美团一面： https://www.nowcoder.com/discuss/110274 
【java】美团3面面经： https://www.nowcoder.com/discuss/109567 
【java】发个周一深圳美团电话面经： https://www.nowcoder.com/discuss/109255 
【java】美团 后台Java研发 三面： https://www.nowcoder.com/discuss/108805 
【java】美团java后台 哈尔滨现场面试面经： https://www.nowcoder.com/discuss/108195 
【Java】热腾腾的腾讯java后台一面面经 https://www.nowcoder.com/discuss/90649 
【java】腾讯java web开发 一面 https://www.nowcoder.com/discuss/90542 
【java】腾讯java web开发 二面 https://www.nowcoder.com/discuss/93465 
【java】 腾讯IEG运营开发2面java方向 https://www.nowcoder.com/discuss/92180 
【java】南京小米二面 全程58分钟： https://www.nowcoder.com/discuss/126502 
【Java】小米秋招软件开发(java方向)面经： https://www.nowcoder.com/discuss/125991 
【java】记一次小米一面面经。 https://www.nowcoder.com/discuss/91449 
【java】中兴技术面被怼面经： https://www.nowcoder.com/discuss/113126 
【java】中兴一面凉经，热乎的： https://www.nowcoder.com/discuss/109192 
【java】vivo一面凉经： https://www.nowcoder.com/discuss/112192 
【java】 【Vivo二面】新鲜出炉的面经～(Java开发) https://www.nowcoder.com/discuss/90739‘ 
【java】vivo面经 https://www.nowcoder.com/discuss/92381 
【java】科大讯飞java二面面经： https://www.nowcoder.com/discuss/110025 
【java】科大讯飞二面面经： https://www.nowcoder.com/discuss/109544 
【java】海康威视，面试： https://www.nowcoder.com/discuss/113293 
【java】海康专业面+综合面（南京面的）： https://www.nowcoder.com/discuss/111923 
【java】海康威视Java面经 （西安站）： https://www.nowcoder.com/discuss/111444 
【Java】网易考拉java凉面面经 https://www.nowcoder.com/discuss/97738 
【Java】网易考拉java三面面经（好多忘了） https://www.nowcoder.com/discuss/97479 
【java】网易Java面经： https://www.nowcoder.com/discuss/111888 
【java】网易刚出炉面经 （秋招批次）： https://www.nowcoder.com/discuss/111005 
【Java】网易java开发面经： https://www.nowcoder.com/discuss/99217 
【Java】java网易考拉面经： https://www.nowcoder.com/discuss/98113 
【Java】网易考拉java凉面面经： https://www.nowcoder.com/discuss/97738 
【java】从零基础到拿到网易Java实习offer，我做对了哪些事： https://www.nowcoder.com/discuss/141176 
【java】运满满面试(9.15)： https://www.nowcoder.com/discuss/110425 
【java】星环科技(JAVA后端)二面凉经： https://www.nowcoder.com/discuss/117530 
【Java】商汤java实习生一面： https://www.nowcoder.com/discuss/142821 
【java】头条2018.9.22一面与二面与三面凉经： https://www.nowcoder.com/discuss/115824 
【java】头条三面透心凉： https://www.nowcoder.com/discuss/109937 
【java】头条java后台一面凉经： https://www.nowcoder.com/discuss/142537 
【java】头条好人卡get，一面面经： https://www.nowcoder.com/discuss/142201 
【java】平安银行java后台面经： https://www.nowcoder.com/discuss/115587 
【java】依图一面面经（感觉凉）： https://www.nowcoder.com/discuss/109523 
【java】欢聚时代yy现场java一面热经： https://www.nowcoder.com/discuss/114114 
【java】欢聚时代yy现场java二面凉经： https://www.nowcoder.com/discuss/114672 
【java】重庆360企业安全凉经： https://www.nowcoder.com/discuss/114170 
【java】360公司服务器端软件开发面经： https://www.nowcoder.com/discuss/108604 
【Java】远景能源java现场面面经： https://www.nowcoder.com/discuss/100630 
【Java】远景能源java电面面经 https://www.nowcoder.com/discuss/97406 
【java】好未来面经： https://www.nowcoder.com/discuss/110782 
【java】好未来一面凉经： https://www.nowcoder.com/discuss/110440 
【java】珍爱网java现场一面： https://www.nowcoder.com/discuss/110223 
【java】快手二三面+ hr面： https://www.nowcoder.com/discuss/108707 
【Java】猫眼java岗面经： https://www.nowcoder.com/discuss/100366 
【Java】猫眼java开发一面面经： https://www.nowcoder.com/discuss/99821 
【java】热乎乎的猫眼面经： https://www.nowcoder.com/discuss/106579 
【java】用友凉面_面经： https://www.nowcoder.com/discuss/110232 
【java】贝壳JAVA三面面经： https://www.nowcoder.com/discuss/110486 
【Java】贝壳北京现场面java（等结果）： https://www.nowcoder.com/discuss/99174 
【java】贝壳面试体验真心好： https://www.nowcoder.com/discuss/114037 
【java】蘑菇街玄学一面，凉凉……： https://www.nowcoder.com/discuss/107037 
【java】蘑菇街JAVA后台一面： https://www.nowcoder.com/discuss/106633 
【java】keep面经： https://www.nowcoder.com/discuss/113559 
【java】keep面经，动手能力太差啊啊啊啊： https://www.nowcoder.com/discuss/111050 
【java】keep面经，积累人品。： https://www.nowcoder.com/discuss/110915 
【java】回馈牛客，keep面经： https://www.nowcoder.com/discuss/109972 
【java】途牛微信视频面试一面： https://www.nowcoder.com/discuss/106598 
【Java】宜信大数据中心java研发岗面经： https://www.nowcoder.com/discuss/105875 
【java】宜信java面经： https://www.nowcoder.com/discuss/111611 
【java】阴差阳错的虎牙面试： https://www.nowcoder.com/discuss/105838 
【java】爱奇艺java实习生一面： https://www.nowcoder.com/discuss/141277 
【java】爱奇艺java后端一面、二面面经： https://www.nowcoder.com/discuss/142301 
【java】喜马拉雅 西安9.18： https://www.nowcoder.com/discuss/117406 
【java】9月18日武汉去哪儿面经： https://www.nowcoder.com/discuss/113038 
【java】9月18日武汉去哪儿面经： https://www.nowcoder.com/discuss/113038 
【java】迅雷面经： https://www.nowcoder.com/discuss/117002 
【java】迅雷一面面筋： https://www.nowcoder.com/discuss/116185 
【java】居然之家设计一面二面： https://www.nowcoder.com/discuss/116750 
【java】完美世界4面面经（已拿口头offer）： https://www.nowcoder.com/discuss/116547 
【Java】新浪java后台开发工程师一面面经： https://www.nowcoder.com/discuss/119507 
【Java】途家java开发岗凉经： https://www.nowcoder.com/discuss/123403 
【java】中信信用卡面经。感觉过了，等消息。： https://www.nowcoder.com/discuss/143463 
【java】面经继续写 高思集团java后台一面二面面经： https://www.nowcoder.com/discuss/142889 
【java】高思教育视频面： https://www.nowcoder.com/discuss/142727 
【Java】java后端-软通/华微/华为-一面~口头offer： https://www.nowcoder.com/discuss/130954 
【Java】皮一下，java开发菜鸡结束秋招： https://www.nowcoder.com/discuss/129499 
【java】阿里，京东，好未来，水滴面经（含实习）： https://www.nowcoder.com/discuss/113993 
【java】我的秋招之路 ： https://www.nowcoder.com/discuss/117423 
【java】顺丰科技、去哪儿网面经： https://www.nowcoder.com/discuss/113837 
【java】纪念日男票拿offer了(秀波男票，并回馈一波牛友攒人品)： https://www.nowcoder.com/discuss/115517 
【java】一家外包的面经，顺便求助。： https://www.nowcoder.com/discuss/115332 
【java】回馈一波，凉经……大家想看可以参考一下： https://www.nowcoder.com/discuss/114783 
【java】春招到秋招27面面筋总结 ： https://www.nowcoder.com/discuss/113997 
【java】海康和37现场凉面面经： https://www.nowcoder.com/discuss/113543 
【java】秋招几家公司的面经： https://www.nowcoder.com/discuss/112142 
【java】百度，阿里，腾讯，网易面经 ： https://www.nowcoder.com/discuss/108927 
【java】【Java后台开发面经】阿里|网易|头条|腾讯|华为 ： https://www.nowcoder.com/discuss/108655 
【java】完美世界，中兴，新大陆支付面经： https://www.nowcoder.com/discuss/108748 
【java】【回馈】超详细，助你秋招逆袭！： https://www.nowcoder.com/discuss/111311 
【java】贝壳一面凉经+keep三面： https://www.nowcoder.com/discuss/108192 
【java】听说发面经可以拿offer： https://www.nowcoder.com/discuss/110259 
【java】从春招到秋招，经验总结（收获AT）： https://www.nowcoder.com/discuss/106396 
【java】阿里美团京东面经： https://www.nowcoder.com/discuss/106805 
【java】我的秋招经验分享（已拿百度，阿里，网易，头条，华为）： https://www.nowcoder.com/discuss/106619 
【java】非科班渣硕JAVA面经（京东华为小米海康去哪百度美团阿里等）： https://www.nowcoder.com/discuss/138000 
【java】秋招总结，看了这么多相亲贴，是时候来股清流了： https://www.nowcoder.com/discuss/137695 
【java】发一波笔经面经，鼓励自己(大家)坚持走下去： https://www.nowcoder.com/discuss/137613 
【java】非科班秋招面试总结： https://www.nowcoder.com/discuss/143224 
【java】双非的秋招，感谢牛客： https://www.nowcoder.com/discuss/142181 
【java】自己及同学的一些面经整理： https://www.nowcoder.com/discuss/141703 
【java后台开发】跨专业转CS拿下百度java后台开发的干货分享（6000字）： https://www.nowcoder.com/discuss/141507 
【Java】java复***纲（精华版）： https://www.nowcoder.com/discuss/120267 
【Java】回馈牛客！各大公司java面试整理对应问题博客整理！： https://www.nowcoder.com/discuss/120239 
【java】说说两个月的秋招之路和经常碰到的面试题，顺便offer求建议： https://www.nowcoder.com/discuss/117077 
【Java】java并发 面经： https://www.nowcoder.com/discuss/97942 

 【java】招银网络科技java面经： https://www.nowcoder.com/discuss/139236 
【Java】招银网络java软开面经： https://www.nowcoder.com/discuss/128821 
【Java】招银网络java面经： https://www.nowcoder.com/discuss/120970 
【java】凉经-招银科技： https://www.nowcoder.com/discuss/113040 
【java】招银网络面试： https://www.nowcoder.com/discuss/110687 
【java】招银网络后台开发电话面经： https://www.nowcoder.com/discuss/108588 
【java】4399一面技术面+HR面凉经： https://www.nowcoder.com/discuss/111487 
【java】斗鱼面经： https://www.nowcoder.com/discuss/111472 
【java】百词斩一面9.17： https://www.nowcoder.com/discuss/111305 
【java】有赞面经（详细）： https://www.nowcoder.com/discuss/141451 
【java】百度三面。。。。： https://www.nowcoder.com/discuss/113406 
【java】百度Java开发一面面经： https://www.nowcoder.com/discuss/111454 
【java】百度一面面经： https://www.nowcoder.com/discuss/111099 
【java】百度java一面面经： https://www.nowcoder.com/discuss/109127 
【java】百度DuerOS部门面经，凉凉 https://www.nowcoder.com/discuss/89094 
【java】三七互娱补招技术二面： https://www.nowcoder.com/discuss/137849 
【java】三七互娱一面面经，通过，明天二面不知是HR面还是二轮技术面： https://www.nowcoder.com/discuss/137549 
【java服务端】三七互娱秋招提前批java服务端 https://www.nowcoder.com/discuss/85510 
【java】京东三面面经： https://www.nowcoder.com/discuss/113076 
【java】京东面经： https://www.nowcoder.com/discuss/111943 
【java】京东9月16日北京JAVA研发工程师一面： https://www.nowcoder.com/discuss/110887 
【java】jd一面： https://www.nowcoder.com/discuss/108837 
【java】 京东提前批面试 https://www.nowcoder.com/discuss/91413 
【java】谈谈我那的京东面试，伤心 https://www.nowcoder.com/discuss/9673 
【Java】java京东一面，凉凉 https://www.nowcoder.com/discuss/92447 
【java】阿里一面感受【补面经】： https://www.nowcoder.com/discuss/113050 
【java】百度一二三面面经，结果未知还在等待，过程中的收获很大 https://www.nowcoder.com/discuss/230947 
【java】百度提前批一面挂 https://www.nowcoder.com/discuss/230794 
【java】滴滴一面记录 https://www.nowcoder.com/discuss/230873 
【java】阿里三面，交叉面已过 https://www.nowcoder.com/discuss/230960 
【java】阿里云内推一面挂 https://www.nowcoder.com/discuss/230568 
【java】阿里二面 java https://www.nowcoder.com/discuss/232058 
【java】京东 Java 后台三面凉经 https://www.nowcoder.com/discuss/231496 
【java】美团Java后台开发一面面经 https://www.nowcoder.com/discuss/231011 
【java】美团后台（java）一面面经 （凉凉） https://www.nowcoder.com/discuss/231578 
【java】美团系统开发一面 https://www.nowcoder.com/discuss/231509 
【java】腾讯一面 后端 https://www.nowcoder.com/discuss/232902 
【java】网易现场三面凉经出炉 https://www.nowcoder.com/discuss/230963 
【java】网易云音乐二面 https://www.nowcoder.com/discuss/230750 
【java】网易云音乐，技术二面，懵了。 https://www.nowcoder.com/discuss/230674 
【java】网易有道云二面凉经 https://www.nowcoder.com/discuss/231614 
【java】小米有品商城现场面经分享 https://www.nowcoder.com/discuss/230897 
【java】携程后台开发两面 https://www.nowcoder.com/discuss/230923 
【java】依图科技一面 https://www.nowcoder.com/discuss/230489 
【java】有赞面经（一面）---凉经 https://www.nowcoder.com/discuss/232894 
【java】有赞一、二面面经 https://www.nowcoder.com/discuss/232534 
【java】猿辅导提前批一面JAVA凉经 https://www.nowcoder.com/discuss/232243 
【java】远景科技一面面经 https://www.nowcoder.com/discuss/231312 
【java】【java】一面面经 https://www.nowcoder.com/discuss/229830 
【java】蘑菇街后台电话一面凉经 https://www.nowcoder.com/discuss/229613 
【java】拼多多服务端开发 https://www.nowcoder.com/discuss/229699 
【java】拼多多服务器开发二面，求求保佑过吧 https://www.nowcoder.com/discuss/229548 
【java】腾讯PCG后台开发一面面经 https://www.nowcoder.com/discuss/229726 
【java】网易-杭研-Java开发-二面 https://www.nowcoder.com/discuss/229621 
【java】网易二（凉）面一份(Java) https://www.nowcoder.com/discuss/229555 
【java】网易严选提前批二面JAVA凉经 https://www.nowcoder.com/discuss/229419 
【java】用友一面经 https://www.nowcoder.com/discuss/229530 
【java】远景8月20日视频一面 面经 https://www.nowcoder.com/discuss/230175 
【java】百度Java电面一面 https://www.nowcoder.com/discuss/228751 
【java】百度智能云计算两面面经，攒个人品 https://www.nowcoder.com/discuss/228397 
【java】阿里java一面面经 https://www.nowcoder.com/discuss/229394 
【java】格力一面 https://www.nowcoder.com/discuss/229239 
【java】美团一面凉面（第一次面试） https://www.nowcoder.com/discuss/229348 
【java】美团面经 https://www.nowcoder.com/discuss/229237 
【java】美团点评 电话面试 面经 Java https://www.nowcoder.com/discuss/229162 
【java】蘑菇街一面，攒一波人品 https://www.nowcoder.com/discuss/228646 
【java】8.21浦发面经 https://www.nowcoder.com/discuss/229355 
【java】网易二面凉经 https://www.nowcoder.com/discuss/229249 
【java】刚收到猿辅导的电话，特意发个面经吧 https://www.nowcoder.com/discuss/229412 
【java】0817贝壳一面——Java参考 https://www.nowcoder.com/discuss/228066 
【java】贝壳找房二面挂经 https://www.nowcoder.com/discuss/227957 
【java】热乎乎的阿里一面凉经 https://www.nowcoder.com/discuss/228041 
【java】华为8.20北京 java 面经 https://www.nowcoder.com/discuss/228181 
【java】雷火 游戏测试 面经 https://www.nowcoder.com/discuss/228137 
【java】美团一面 https://www.nowcoder.com/discuss/228190 
【java】美团点评一面面经(后台开发) https://www.nowcoder.com/discuss/227925 
【java】来了来了他来了.....表哥至强面筋... https://www.nowcoder.com/discuss/227733 
【java】刚下高铁后赶场的美团一面面经（Java后台开发） https://www.nowcoder.com/discuss/227624 
【java】蘑菇街后台一面面经 https://www.nowcoder.com/discuss/227668 
【java】蘑菇街后台一面面经 https://www.nowcoder.com/discuss/227357 
【java】浦发银行面经 https://www.nowcoder.com/discuss/228232 
【java】腾讯一面凉经 https://www.nowcoder.com/discuss/227403 
【java】新鲜出炉的网易Java开发二面面经，面完后面试官对我笑嘻嘻 https://www.nowcoder.com/discuss/228179 
【java】网易严选Java后端 二面：40分钟，问的有点懵 https://www.nowcoder.com/discuss/227512 
【java】猿辅导服务端二面，继续攒人品 https://www.nowcoder.com/discuss/227697 
【java】【java】百度+字节+滴滴+虾皮 https://www.nowcoder.com/discuss/227754 
【java】网易有道的二面凉经 https://www.nowcoder.com/discuss/227162 
【java】网易有道一面凉经-JAVA https://www.nowcoder.com/discuss/226860 
【java】字节后台三面面经 https://www.nowcoder.com/discuss/226817 
【java】迟到的作业帮面经(口头offer) https://www.nowcoder.com/discuss/226978 
【java】网易考拉一面凉经 https://www.nowcoder.com/discuss/225337 
【java】猿辅导二面，面试官劝退，所有努力白费 https://www.nowcoder.com/discuss/225924 
【java】猿辅导三面（凉透） https://www.nowcoder.com/discuss/225847 
【java】远景电话面 https://www.nowcoder.com/discuss/225677 
【java】云从面试 java开发方向 两轮技术面+1轮HR面 https://www.nowcoder.com/discuss/225574 
【java】2020字节跳动春招客户端开发岗面经 https://www.nowcoder.com/discuss/225697 
【java】头条一面记录 https://www.nowcoder.com/discuss/226623 
【java】菜鸡面经（百度 & 作业帮 & 华为） https://www.nowcoder.com/discuss/225270 
【java】shopee一面面筋 https://www.nowcoder.com/discuss/225743 
【java】Shopee一面面经 https://www.nowcoder.com/discuss/225558 
【java】2020拼多多学霸批客户端开发岗面经 https://www.nowcoder.com/discuss/225694 
【java】浦发面经 https://www.nowcoder.com/discuss/225949 
【java】上海浦发提前批面结束了emmm吐槽一下 https://www.nowcoder.com/discuss/226645 
【java】顺丰sp专场面经 java https://www.nowcoder.com/discuss/225403 
【java】腾讯二面 43分钟 https://www.nowcoder.com/discuss/225485 
【java】腾讯客户端一面面经 https://www.nowcoder.com/discuss/225437 
【java】腾讯一面凉经 https://www.nowcoder.com/discuss/225392 
【java】字节二面凉 https://www.nowcoder.com/discuss/226654 
【java】字节跳动后端三轮面经 https://www.nowcoder.com/discuss/226626 
【java】thoughtworks 加试问的全是技术问题 https://www.nowcoder.com/discuss/224261 
【java】百度java研发 一面 凉经 https://www.nowcoder.com/discuss/224340 
【java】滴滴小桔车服杭州实习面经 https://www.nowcoder.com/discuss/224787 
【java】东方财富一面、hr面经 https://www.nowcoder.com/discuss/224209 
【java】人生第一面：阿里巴巴电话面40min https://www.nowcoder.com/discuss/224894 
【java】阿里业务平台校招二面 https://www.nowcoder.com/discuss/224783 
【java】阿里巴巴Java一面 https://www.nowcoder.com/discuss/224321 
【java】阿里一二面、远景一面，秋招Java开发面经 https://www.nowcoder.com/discuss/224390 
【java】华为优招面经 https://www.nowcoder.com/discuss/224934 
【java】美团8.15一面下午四点到四点四十二 https://www.nowcoder.com/discuss/224752 
【java】蘑菇街后台一面凉经 https://www.nowcoder.com/discuss/224577 
【java】蘑菇街一面凉经 https://www.nowcoder.com/discuss/224532 
【java】秋招的开始：宁波银行IT科技部 https://www.nowcoder.com/discuss/224916 
【java】拼多多服务端一二面 https://www.nowcoder.com/discuss/224651 
【java】趋势科技一面妥妥的凉面已发感谢信 https://www.nowcoder.com/discuss/224758 
【java】人人三面面经（提前批） https://www.nowcoder.com/discuss/224128 
【java】顺丰科技SP专场3面-java https://www.nowcoder.com/discuss/224296 
【java】java日常实习一、二面面经，滴滴AI Lab https://www.nowcoder.com/discuss/224774 
【java】网易杭研所一面 Java https://www.nowcoder.com/discuss/224513 
【java】网易严选提前批一面JAVA凉经 https://www.nowcoder.com/discuss/224464 
【java】网易云音乐一面面经 https://www.nowcoder.com/discuss/224412 
【java】网易有道二面凉经 https://www.nowcoder.com/discuss/224402 
【java】网易云音乐 一面凉经 57min https://www.nowcoder.com/discuss/224372 
【java】网易杭研一面 8.15 上午 凉凉 https://www.nowcoder.com/discuss/224345 
【java】网易严选提前批JAVA一面凉经 https://www.nowcoder.com/discuss/224341 
【java】估计凉了，面经拿去 https://www.nowcoder.com/discuss/224328 
【java】网易考拉一面不知道凉没凉面筋 https://www.nowcoder.com/discuss/224258 
【java】网易云音乐一面凉 https://www.nowcoder.com/discuss/224185 
【java】远景后台一面，30min https://www.nowcoder.com/discuss/224523 
【java】远景智能java一面 https://www.nowcoder.com/discuss/224469 
【java】ihandy后台开发（云平台）一面面经 https://www.nowcoder.com/discuss/223972 
【java】滴滴出行实习面经 https://www.nowcoder.com/discuss/223406 
【java】东方财富网一面面经-java方向 https://www.nowcoder.com/discuss/223994 
【java】阿里一面凉经 https://www.nowcoder.com/discuss/224078 
【java】阿里被捞一面（忘记是啥部门了） https://www.nowcoder.com/discuss/223915 
【java】阿里一面面经-淘宝事业群-智能制造事业部 https://www.nowcoder.com/discuss/223865 
【java】阿里一面面经 https://www.nowcoder.com/discuss/223721 
【java】阿里飞猪电话一面 https://www.nowcoder.com/discuss/223599 
【java】【java】蚂蚁金服-java-社招 https://www.nowcoder.com/discuss/223700 
【java】新鲜的美团后端一面凉经 https://www.nowcoder.com/discuss/224111 
【java】蘑菇街后端一面，咸鱼渴望翻身 https://www.nowcoder.com/discuss/223428 
【java】宁波银行提前批技术面经 https://www.nowcoder.com/discuss/224068 
【java】人人三面面经（提前批） https://www.nowcoder.com/discuss/224128 
【java】腾讯运营开发技术三面面经 被血虐 https://www.nowcoder.com/discuss/224096 
【java】网易杭研 一面 https://www.nowcoder.com/discuss/224116 
【java】网易Java后台一面，凉凉 https://www.nowcoder.com/discuss/223590 
【java】远景Java电话一面 https://www.nowcoder.com/discuss/223816 
【java】远景科技一面--1.5小时，全程底层原理与实现 https://www.nowcoder.com/discuss/223795 
【java】百度java一面二面面经 https://www.nowcoder.com/discuss/222642 
【java】【java】大搜车-java-社招 https://www.nowcoder.com/discuss/222777 
【java】阿里电话面试经验： https://www.nowcoder.com/discuss/223144 
【java】阿里面经 https://www.nowcoder.com/discuss/222739 
【java】阿里Java一面二面面经 https://www.nowcoder.com/discuss/222684 
【java】虎牙直播-后台开发一面 https://www.nowcoder.com/discuss/222589 
【java】蘑菇街后端一面凉经 https://www.nowcoder.com/discuss/223105 
【java】顺丰凉面 https://www.nowcoder.com/discuss/222637 
【java】腾讯后台开发，一面凉经，滚去学习 https://www.nowcoder.com/discuss/222766 
【java】严选Java一面凉经 https://www.nowcoder.com/discuss/223146 
【java】网易一面面经 https://www.nowcoder.com/discuss/223101 
【java】网易严选Java提前批一面攒人品 https://www.nowcoder.com/discuss/222742 
【java】网易杭研java一面 https://www.nowcoder.com/discuss/222665 
【java】网易互联网一面凉经 https://www.nowcoder.com/discuss/222631 
【java】中兴软开电话面一面 https://www.nowcoder.com/discuss/222833 
【java】【java】百词斩 - java - 社招 https://www.nowcoder.com/discuss/221920 
【java】美团系统开发工程师面试问题 https://www.nowcoder.com/discuss/221864 
【java】平安壹钱包面经 https://www.nowcoder.com/discuss/221975 
【java】趋势科技一面 https://www.nowcoder.com/discuss/221922 
【java】顺丰java sp专场一面面经 https://www.nowcoder.com/discuss/221954 
【java】顺丰Java二面 https://www.nowcoder.com/discuss/221951 
【java】腾讯一面凉经 https://www.nowcoder.com/discuss/222035 
【java】头条二面面经（攒人品别给挂啊） https://www.nowcoder.com/discuss/221898 
【java】滴滴牛客SP专场后台开发一二三面面经，等通知 https://www.nowcoder.com/discuss/221383 
【java】阿里二面凉经 https://www.nowcoder.com/discuss/221416 
【java】面经 | 成功收割阿里offer干货分享 https://www.nowcoder.com/discuss/221297 
【java】猿辅导Java视频一面 https://www.nowcoder.com/discuss/221214 
【java】【java】招银网络科技JAVA https://www.nowcoder.com/discuss/221130 
【java】迟了几天的字节跳动面经 https://www.nowcoder.com/discuss/221324 
【java】滴滴提前批Java一二面面经 https://www.nowcoder.com/discuss/219909 
【java】阿里java服务端简历面 https://www.nowcoder.com/discuss/219742 
【java】阿里巴巴搜索推荐事业部面经及实习经历 https://www.nowcoder.com/discuss/219729 
【java】阿里盒马，一面+一面补面 (二面凉透) https://www.nowcoder.com/discuss/219661 
【java】阿里四面面经 https://www.nowcoder.com/discuss/219509 
【java】阿里优酷Java后台电面 https://www.nowcoder.com/discuss/219368 
【java】阿里优酷一面凉经 https://www.nowcoder.com/discuss/219339 
【java】虎牙 后台开发 一面 https://www.nowcoder.com/discuss/219544 
【java】美团后端 现场面 一面挂 https://www.nowcoder.com/discuss/220033 
【java】PDD远程Java一面面经，积德积德 https://www.nowcoder.com/discuss/219666 
【java】拼多多服务端二面凉经 https://www.nowcoder.com/discuss/219486 
【java】拼多多学霸批服务端研发工程师面经 https://www.nowcoder.com/discuss/219391 
【java】顺丰第二轮技术面 https://www.nowcoder.com/discuss/221090 
【java】腾讯后台一面面经 https://www.nowcoder.com/discuss/219646 
【java】腾讯后台开发一面面经 https://www.nowcoder.com/discuss/219573 
【java】腾讯一面(java开发) https://www.nowcoder.com/discuss/220349 
【java】雷火云平台开发提前批一二三面面经 https://www.nowcoder.com/discuss/219918 
【java】猿辅导服务端提前批面试 https://www.nowcoder.com/discuss/220601 
【java】猿辅导服务端一面大概是凉经 https://www.nowcoder.com/discuss/220594 
【java】猿辅导服务器后端 https://www.nowcoder.com/discuss/220585 
【java】2019.08.10 猿辅导服务端开发提前批 在线一面 https://www.nowcoder.com/discuss/220542 
【java】猿辅导一面面经(视频面试) https://www.nowcoder.com/discuss/220454 
【java】猿辅导服务端一面凉经 https://www.nowcoder.com/discuss/221099 
【java】阿里巴巴淘宝新制造java后台开发岗一面凉经： https://www.nowcoder.com/discuss/112007 
【java】阿里云Java研发三面技术+HR面： https://www.nowcoder.com/discuss/108343 
【Java】 阿里菜鸟内推/java/一面（电话） https://www.nowcoder.com/discuss/96453 
【java】阿里秋招内推1.2.3面面经（Java后台） https://www.nowcoder.com/discuss/87473 
【java】阿里7.24号java开发一面 电话面 https://www.nowcoder.com/discuss/88759 
【java】阿里菜鸟Java简历评估面 https://www.nowcoder.com/discuss/91149 
【JAVA】阿里电面---java开发 https://www.nowcoder.com/discuss/91051 
【java】阿里菜鸟一面经验 https://www.nowcoder.com/discuss/89975 
【java】阿里钉钉凉面 https://www.nowcoder.com/discuss/89956 
【Java】阿里技术开发（java）一面面经 https://www.nowcoder.com/discuss/89653 
【Java】 阿里巴巴java 1+2+3+hr面 https://www.nowcoder.com/discuss/94656 
【Java】腾讯java web开发 三面 https://www.nowcoder.com/discuss/97440 
【java】阿里巴巴java开发北美on campus面经（10.27）： https://www.nowcoder.com/discuss/137599 
【java】苏宁面试Java岗（西安站）： https://www.nowcoder.com/discuss/112064 
【java】苏宁南京9.05现场面： https://www.nowcoder.com/discuss/109213 

 C++

 【C++】百度三面： https://www.nowcoder.com/discuss/114792 
【C++】百度C++面试 一/二面 面经： https://www.nowcoder.com/discuss/113601 
【C++】百度一面二面经历（体验极差）： https://www.nowcoder.com/discuss/112003 
【C++】百度一面凉面面经： https://www.nowcoder.com/discuss/111058 
【C++】百度一面： https://www.nowcoder.com/discuss/109958 
【C++】来自小白的百度一面面经： https://www.nowcoder.com/discuss/109318 
【C++】秋招第一次面试->百度（c++后台岗位） https://www.nowcoder.com/discuss/90069 
【C++】提前批面经C/C++后台开发岗位(持续更新) https://www.nowcoder.com/discuss/94734 
【C++】 百度 提前批C++一面 二面 三面（GG） https://www.nowcoder.com/discuss/96139 
【C++】大佬们新鲜出炉的度秘面经，了解一下 ~ https://www.nowcoder.com/discuss/96056 
【C++】京东二面凉面筋： https://www.nowcoder.com/discuss/112228 
【C++】 京东提前批C++面试 https://www.nowcoder.com/discuss/91590 
【C++】有幸被菜鸟开奖，结束秋招，回馈牛油： https://www.nowcoder.com/discuss/110317 
【C++】阿里、C++三面技术面+ hr面面筋 ： https://www.nowcoder.com/discuss/100946 
【C/C++】阿里-面经-研发工程师（C/C++）： https://www.nowcoder.com/discuss/101607 
【Java】阿里国际事务部挂经，Java岗 https://www.C++nowcoder.com/discuss/96464 
【后端c++】DJI+阿里巴巴ICBU一面面经（后端C++） https://www.nowcoder.com/discuss/87621 
【C++】阿里-面经-研发工程师（C/C++）： https://www.nowcoder.com/discuss/101607 
【c++】阿里一面面经C++，攒个人品 https://www.nowcoder.com/discuss/88501 
【c++】新鲜热乎的百度一面面筋(C++)，攒人品 https://www.nowcoder.com/discuss/88852 
【C++】阿里飞猪一面凉经 https://www.nowcoder.com/discuss/94080 
【C++后台开发】 阿里巴巴新零售 一面凉凉（C++后台开发） https://www.nowcoder.com/discuss/90335 
【C++】华为凉经： https://www.nowcoder.com/discuss/121852 
【C++】华为优招-长沙-一二面面经（感觉用处不大） https://www.nowcoder.com/discuss/96528 
【C++】 华为优招面经8.20 https://www.nowcoder.com/discuss/96410 
【c++开发】蚂蚁金服中间件一面和二面面筋（C++开发） https://www.nowcoder.com/discuss/87810 
【C++】 秋招提前批面试记录小结 https://www.nowcoder.com/discuss/97474 
【C++】CVTE武汉面经： https://www.nowcoder.com/discuss/113462 
【C++】CVTE一面二面+HR面 https://www.nowcoder.com/discuss/89764 
【C++】CVTE提前批c++开发一面 https://www.nowcoder.com/discuss/89534 
【C++】CVTE的电话两面面经 https://www.nowcoder.com/discuss/91635 
【C++】美团二面凉经： https://www.nowcoder.com/discuss/108186 
【C++】腾讯面经(一面，二面，hr面）： https://www.nowcoder.com/discuss/118386 
【C++开发】腾讯面筋 https://www.nowcoder.com/discuss/89707 
【C++】腾讯内推面试 https://www.nowcoder.com/discuss/93770 
【C++】 腾讯IEG凉经 https://www.nowcoder.com/discuss/96731 
【C++】一脸懵逼的腾讯面试 https://www.nowcoder.com/discuss/96355 
【C++】腾讯云补录一面面经： https://www.nowcoder.com/discuss/140442 
【C++】小米云存储面经： https://www.nowcoder.com/discuss/111718 
【C++】小米面经： https://www.nowcoder.com/discuss/108813 
【C++】中兴武汉面经一面： https://www.nowcoder.com/discuss/112960 
【C++】vivo开发( c++)一面面经： https://www.nowcoder.com/discuss/118539 
【C++】8.10 vivo C++软件开发工程师一面面经 https://www.nowcoder.com/discuss/93137 
【C++】金山WPS C++岗一面： https://www.nowcoder.com/discuss/118302 
【C++】金山WPS，C++，二面面筋 https://www.nowcoder.com/discuss/95219 
【C++】金山C++研发工程师 一面 https://www.nowcoder.com/discuss/96606 
【C++】金山 凉经 https://www.nowcoder.com/discuss/96286 
【C++】wps一面面经 https://www.nowcoder.com/discuss/97704 
【C++】金山wps一面 https://www.nowcoder.com/discuss/97425 
【C++】金山WPS，C++研发工程师，一面 https://www.nowcoder.com/discuss/92322 
【Java】银联应用开发面经（我是Java，他们也有C++） 西安站 https://www.nowcoder.com/discuss/93155 
【C++】8月底的拼多多学霸批面经： https://www.nowcoder.com/discuss/112238 
【C++】拼多多面经： https://www.nowcoder.com/discuss/109638 
【C++】迈瑞面经--C++工程师 https://www.nowcoder.com/discuss/90442 
【C++】中国电信it研发中心面筋： https://www.nowcoder.com/discuss/114075 
【C++】今日海康面试体验： https://www.nowcoder.com/discuss/112148 
【C++】海康威视面经： https://www.nowcoder.com/discuss/111844 
【C++】滴滴面经～回忆版： https://www.nowcoder.com/discuss/136818 
【C++】网易雷火平台开发工程师一面： https://www.nowcoder.com/discuss/120667 
【C++】网易互娱面经： https://www.nowcoder.com/discuss/114820 
【C++】网易雷火一面（估计已经凉了）： https://www.nowcoder.com/discuss/113819 
【C++】网易互娱-我为自己耽误了面试官的时间而愧疚： https://www.nowcoder.com/discuss/113550 
【C++】很难受的网易互娱研发面经 https://www.nowcoder.com/discuss/96710 
【C++】网易初游研面经 https://www.nowcoder.com/discuss/96793 
【C++】网易互娱游戏研发面经（两面）： https://www.nowcoder.com/discuss/111976 
【C++】网易互娱校招面经： https://www.nowcoder.com/discuss/111018 
【C++】网易互娱1面 （）经【括号里的字不确定于是先空着】： https://www.nowcoder.com/discuss/106443 
【C++】字节跳动后端一面被一个巨水的面试官给毙了： https://www.nowcoder.com/discuss/128236 
【C++】今日头条三面面经： https://www.nowcoder.com/discuss/109167 
【C++】头条1 2 3面经： https://www.nowcoder.com/discuss/99287 
【C++】今日头条三面面经： https://www.nowcoder.com/discuss/102612 
【C++】 头条三面（攒一波人品） https://www.nowcoder.com/discuss/93423 
【C++】今日头条c++后台开发 一二面，二面gg https://www.nowcoder.com/discuss/95939 
【C++】平安科技一面又懵逼凉经： https://www.nowcoder.com/discuss/113464 
【C++】2019校招盛大游戏cocos凉经： https://www.nowcoder.com/discuss/109360 
【C++】趋势windows platform developer： https://www.nowcoder.com/discuss/111933 
【后台C++】360后台C++ 2面凉： https://www.nowcoder.com/discuss/103844 
【C++】360面筋！！： https://www.nowcoder.com/discuss/98392 
【C++】360面经： https://www.nowcoder.com/discuss/97830 
【C++】360一面二面，估计凉 https://www.nowcoder.com/discuss/96670 
【C++】刚刚出炉的360一面二面挂经 https://www.nowcoder.com/discuss/96310 
【C++】360一面凉经C++ https://www.nowcoder.com/discuss/97182 
【C++】360面经 https://www.nowcoder.com/discuss/97830 
【C++】360面经 https://www.nowcoder.com/discuss/97741 
【C++】360奇葩挂经 https://www.nowcoder.com/discuss/98188 
【C++】贡献一波知乎面经。。： https://www.nowcoder.com/discuss/120463 
【C++】快手提前批面经： https://www.nowcoder.com/discuss/112954 
【C++】美图C++研发工程师（算法落地）面经 ： https://www.nowcoder.com/discuss/103212 
【C++研发岗】贝壳三面面经。： https://www.nowcoder.com/discuss/102429 
【C++】米哈游引擎渲染挂面： https://www.nowcoder.com/discuss/120197 
【C++】微软面经： https://www.nowcoder.com/discuss/136414 
【C++】研发工程师面经（C++）： https://www.nowcoder.com/discuss/126102 
【C++】秋招结束，春招再战！（附面经）： https://www.nowcoder.com/discuss/125248 
【C++】offer选择，随便附上秋招面筋头条百度贝壳电信IT研发华为： https://www.nowcoder.com/discuss/123320 
【C++】某菜鸡的头条+百度菜鸡实习面试记录： https://www.nowcoder.com/discuss/118629 
【C++】秋招的面经：百度+中兴+链家+烽火： https://www.nowcoder.com/discuss/123214 
【C++】写个秋招总结C++开发岗： https://www.nowcoder.com/discuss/124174 
【C++】秋招结束，整理一下。内含面筋 ： https://www.nowcoder.com/discuss/124030 
【C++】一个失败者的秋招面经： https://www.nowcoder.com/discuss/123798 
【C++】2018年秋招游戏公司面经+面试准备心得： https://www.nowcoder.com/discuss/123714 
【C++】结束秋招，总结自己的秋招之旅，回馈牛客（面经大礼包）： https://www.nowcoder.com/discuss/123111 
【C++】弱鸡的游戏秋招之路： https://www.nowcoder.com/discuss/123043 
【C++】2018面经总结： https://www.nowcoder.com/discuss/122973 
【C++】终于轮到我了——来自非科班渣硕的秋招之路： https://www.nowcoder.com/discuss/122105 
【C++】非科班985水硕秋招经历： https://www.nowcoder.com/discuss/122056 
【C++】总结一下到目前为止的秋招，发C++面经攒人品： https://www.nowcoder.com/discuss/121780 
【C++】秋招结束，回馈牛友 （建议和面经）： https://www.nowcoder.com/discuss/121478 
【C++】和女朋友都已完成秋招，发出面经回馈牛客： https://www.nowcoder.com/discuss/120275 
【C++】总结一个菜鸡的秋招之路，望博牛油们一乐： https://www.nowcoder.com/discuss/120185 
【C++】C++开发渣硕妹纸BAT春招秋招面经： https://www.nowcoder.com/discuss/117644 
【C++】不一样的面经（攒人品）： https://www.nowcoder.com/discuss/116175 
【C++】回馈牛客，渣本的秋招总结（BAT）： https://www.nowcoder.com/discuss/114087 
【C++】腾讯、网易互娱面经： https://www.nowcoder.com/discuss/111543 
【C++后台研发工程师】C++后台研发工程师2018年BAT华为网易等面经总结： https://www.nowcoder.com/discuss/103939 

 【c++】网易互娱一面凉经 https://www.nowcoder.com/discuss/230669 
【c++】网易互娱 一面凉经 https://www.nowcoder.com/discuss/230611 
【c++】网易互娱研发一面面经 https://www.nowcoder.com/discuss/232268 
【c++】新鲜出炉的猿辅导服务端面经 https://www.nowcoder.com/discuss/232256 
【c++】猿辅导一面凉经 https://www.nowcoder.com/discuss/231456 
【c++】最近的面试经历，分享一下, 一些个人的愚见 https://www.nowcoder.com/discuss/230121 
【c++】旷视科技软件开发一面面经 https://www.nowcoder.com/discuss/230271 
【c++】美团视频一面面经（系统开发） https://www.nowcoder.com/discuss/229521 
【c++】蘑菇街 视觉算法一面（估计凉凉） https://www.nowcoder.com/discuss/230188 
【c++】拼多多学霸批二面凉经 https://www.nowcoder.com/discuss/229459 
【c++】腾讯游戏秋招客户端面经(电面) https://www.nowcoder.com/discuss/229924 
【c++】网易互娱初级游戏研发一面 https://www.nowcoder.com/discuss/230192 
【c++】猿辅导北京开奖发波面经 https://www.nowcoder.com/discuss/229534 
【c++】百度一面面经 https://www.nowcoder.com/discuss/228872 
【c++】美团点评后台一面、二面不知道凉没凉经 https://www.nowcoder.com/discuss/228812 
【c++】深信服一面C++ https://www.nowcoder.com/discuss/229218 
【c++】我真的太难了..深信服一面凉面 https://www.nowcoder.com/discuss/228876 
【c++】网易雷火客户端三面(视频)凉经 https://www.nowcoder.com/discuss/228899 
【c++】雷火14号约的杭州面，有事去不了改成了今天的视频面试(服务器 https://www.nowcoder.com/discuss/228804 
【c++】百度一面凉经（C/C++后台开发 秋招第一次面试） https://www.nowcoder.com/discuss/227345 
【c++】大疆PC软件开发工程师初面凉经攒人品 https://www.nowcoder.com/discuss/227915 
【c++】阿里面试一面（凉经） https://www.nowcoder.com/discuss/227719 
【c++】发一波C++面经攒人品，希望8月能收获offer https://www.nowcoder.com/discuss/228118 
【c++】柠檬微趣c++面经 https://www.nowcoder.com/discuss/227461 
【c++】拼多多C++过的多吗 https://www.nowcoder.com/discuss/227280 
【c++】浦发银行凉经(20号上午) https://www.nowcoder.com/discuss/228163 
【c++】深信服面试软开二面 https://www.nowcoder.com/discuss/227772 
【c++】深信服电话一面凉经 https://www.nowcoder.com/discuss/227715 
【c++】为什么我的深信服三面不是HR啊 https://www.nowcoder.com/discuss/227359 
【c++】云从cv面经 https://www.nowcoder.com/discuss/228121 
【c++】字节跳动面经（含一二三面） https://www.nowcoder.com/discuss/227808 
【c++】字节后端三面 凉凉夜色为我思念成河～ https://www.nowcoder.com/discuss/227726 
【c++】贝壳C++后台凉经 https://www.nowcoder.com/discuss/227106 
【c++】华为优招录用排序中？ https://www.nowcoder.com/discuss/227151 
【c++】网易，杭研，C++二面 https://www.nowcoder.com/discuss/227100 
【c++】字节跳动三面凉 https://www.nowcoder.com/discuss/226803 
【c++】贝壳找房凉经 https://www.nowcoder.com/discuss/226651 
【c++】第四范式尬凉经 https://www.nowcoder.com/discuss/226108 
【c++】英语流利说面试后台开发一面 https://www.nowcoder.com/discuss/226176 
【c++】拼多多PDD服务端开发二面 https://www.nowcoder.com/discuss/225813 
【c++】深信服 一面 可能是凉经 https://www.nowcoder.com/discuss/225929 
【c++】深信服C++凉筋 https://www.nowcoder.com/discuss/226196 
【c++】深信服电话面试一面二面(菜鸡没有三面) https://www.nowcoder.com/discuss/226107 
【c++】深信服优招研发C++一面凉经 https://www.nowcoder.com/discuss/226026 
【c++】腾讯后台开发一面 https://www.nowcoder.com/discuss/225810 
【c++】腾讯武汉研发中心现场面(c++后台） https://www.nowcoder.com/discuss/226133 
【c++】腾讯3面面经 offer审核当中 https://www.nowcoder.com/discuss/226116 
【c++】【c++】 https://www.nowcoder.com/discuss/226390 
【c++】猿辅导凉经 https://www.nowcoder.com/discuss/226387 
【c++】猿辅导二面面经 https://www.nowcoder.com/discuss/226114 
【c++】猿辅导二面面经 https://www.nowcoder.com/discuss/226040 
【c++】字节跳动一面凉经 https://www.nowcoder.com/discuss/226609 
【c++】字节跳动一面凉经 https://www.nowcoder.com/discuss/226600 
【c++】Shopee后台开发面经 https://www.nowcoder.com/discuss/224176 
【c++】补一下百度C++研发的面经 https://www.nowcoder.com/discuss/224364 
【c++】虎牙秋招提前批c++后台开发面经（一面） https://www.nowcoder.com/discuss/224563 
【c++】宁波银行一面面经，系统开发(宁波) https://www.nowcoder.com/discuss/224273 
【c++】拼多多学霸批服务端研发C++一面面经 https://www.nowcoder.com/discuss/224420 
【c++】腾讯一面 https://www.nowcoder.com/discuss/224546 
【c++】新鲜出炉的雷火两面凉经 https://www.nowcoder.com/discuss/224155 
【c++】2019.08.15 云从科技 远程二面 https://www.nowcoder.com/discuss/224236 
【c++】腾讯一面，55分钟 https://www.nowcoder.com/discuss/223656 
【c++】thoughtworks终面面经，软开(西安) https://www.nowcoder.com/discuss/223009 
【c++】雷火服务端研发两面凉经 https://www.nowcoder.com/discuss/222569 
【c++】拼多多学霸批服务端开发一面凉经 https://www.nowcoder.com/discuss/222776 
【c++】趋势科技西安大唐西市酒店一二面 https://www.nowcoder.com/discuss/222664 
【c++】趋势科技一面凉经0/1 https://www.nowcoder.com/discuss/222520 
【c++】腾讯后端开发一面 https://www.nowcoder.com/discuss/222679 
【c++】网易C++研发工程师一面凉经 https://www.nowcoder.com/discuss/223154 
【c++】可爱的网易有道c++一面凉经 https://www.nowcoder.com/discuss/222617 
【c++】网易互联网，杭研C++，一面 https://www.nowcoder.com/discuss/222457 
【c++】大华一面 https://www.nowcoder.com/discuss/221874 
【c++】腾讯一面 0.9 凉面经 https://www.nowcoder.com/discuss/221875 
【c++】第一次这么快就结束了。。。 https://www.nowcoder.com/discuss/220058 
【c++】thoughtworks凉经，C++(成都) https://www.nowcoder.com/discuss/220821 
【c++】B站游戏C++客户端一面 https://www.nowcoder.com/discuss/219392 
【c++】百度基础架构部一面面经 https://www.nowcoder.com/discuss/219562 
【c++】百度二面凉经 https://www.nowcoder.com/discuss/219469 
【c++】百度面经 https://www.nowcoder.com/discuss/219432 
【c++】多益后台开发笔经 https://www.nowcoder.com/discuss/220093 
【c++】阿里云一面凉经 https://www.nowcoder.com/discuss/219748 
【c++】为阿里云刷kpi了+凉经 https://www.nowcoder.com/discuss/219519 
【c++】【c++】【c++】 https://www.nowcoder.com/discuss/220297 
【c++】转正答辩终于过了，附转正面经和陌陌三面面经 https://www.nowcoder.com/discuss/219361 
【c++】武汉拼多多服务端研发方向面经 https://www.nowcoder.com/discuss/220808 
【c++】腾讯 旷世 面经 https://www.nowcoder.com/discuss/219281 
【c++】网易雷火C++游戏服务器端一二面 https://www.nowcoder.com/discuss/220214 
【c++】雷火游戏研发日常实习二面面经 https://www.nowcoder.com/discuss/220575 
【c++】猿辅导服务器开发一面凉经-面试要稳住心态啊 https://www.nowcoder.com/discuss/219782 
【c++】猿辅导一面凉经（服务器开发C++） https://www.nowcoder.com/discuss/220747 
【c++】猿辅导服务器开发一面面经 https://www.nowcoder.com/discuss/220317 
【c++】补：2019.08.02 云从科技远程面试 https://www.nowcoder.com/discuss/220892 
【c++】武汉中兴提前批面试--软开 https://www.nowcoder.com/discuss/219480 
【c++】拿到offer了，来牛客还愿 https://www.nowcoder.com/discuss/219789 
【c++】字节跳动 四面经+祈福 https://www.nowcoder.com/discuss/219231 
【c++】远景C/C++一面 https://www.nowcoder.com/discuss/221115 
【c++】百度系统部OC，附面经（云计算、数据中心网络、RDMA相关） https://www.nowcoder.com/discuss/218705 
【c++】腾讯移动端开发一面，面后转岗测开，面经 https://www.nowcoder.com/discuss/218804 
【C++】美团，快手面经~： https://www.nowcoder.com/discuss/101667 
【C++】贝壳现场面（C++）+京东技术管培生专业面： https://www.nowcoder.com/discuss/99274 
【C++/后端】2019秋招C++/后端 今日头条等公司面经 ： https://www.nowcoder.com/discuss/137145 
【C++】2018年秋招面试经验总结 ： https://www.nowcoder.com/discuss/140814 
【C++】秋招总结-奋斗没有结束，这只是一个开始： https://www.nowcoder.com/discuss/138258 
【C++】前来还愿啦，一波面经给需要的人： https://www.nowcoder.com/discuss/137775 
【C++】全凉经： https://www.nowcoder.com/discuss/142903 
【C++】一个非科班普通211硕士如何拿到腾讯、百度等offer： https://www.nowcoder.com/discuss/142151 
【C++】致下一级毕业生：如何将自身强化到斩获国内大厂Offer的水平： https://www.nowcoder.com/discuss/141516 
【C++】非计算机专业苦逼的秋招路： https://www.nowcoder.com/discuss/128187 
【C++】秋招结束，总结一下，说下个人经验： https://www.nowcoder.com/discuss/127797 
【C++】秋招over，回馈牛客网的帮助 ： https://www.nowcoder.com/discuss/122760 
【C++】秋招总结与技巧，回馈与感谢： https://www.nowcoder.com/discuss/122640 
【C++】(C++向)从零开始，游戏程序员学习之路(还愿贴)： https://www.nowcoder.com/discuss/121834 
【C++】2018年9月秋招个人总结 ： https://www.nowcoder.com/discuss/121665 

 python

 【Python】字节跳动python后端一，二轮，三轮online： https://www.nowcoder.com/discuss/139734 
【Python】360 python后端 内推面试 https://www.nowcoder.com/discuss/97250 

 【Python】寒武纪 框架开发一面 https://www.nowcoder.com/discuss/212817 
【Python】头条一面 后台研发 https://www.nowcoder.com/discuss/206371 

 【Python】python后台开发面经 https://www.nowcoder.com/discuss/201324 
【Python】奇安信今日面试记录-python服务器方向 https://www.nowcoder.com/discuss/184587 
【Python】360 企业安全 服务端 Python 面经 https://www.nowcoder.com/discuss/184136 
【Python】360服务端开发-python https://www.nowcoder.com/discuss/183942 
【Python】【Python】多家大厂春招实习经历汇总，我的春招回忆流水账+面经 https://www.nowcoder.com/discuss/176162 
【Python】春招实习上岸，分享面筋回报社区 https://www.nowcoder.com/discuss/172824 

 IOS

 【IOS】今日头条面试秀出新智商： https://www.nowcoder.com/discuss/128211 
【IOS】头条IOS三面，有点小神奇： https://www.nowcoder.com/discuss/128110 
【IOS】2019秋招面经大汇总 ： https://www.nowcoder.com/discuss/122402 

 Go

 【go】盛趣游戏-服务器Go语言-一面凉经 https://www.nowcoder.com/discuss/229495 
【go】商汤面经 https://www.nowcoder.com/discuss/210652 

 安卓

 【安卓&Android】2019 腾讯 Android 面经(凉) https://www.nowcoder.com/discuss/231130 
【安卓&Android】字节，蘑菇街Android面经，求好运 https://www.nowcoder.com/discuss/233119 
【安卓&Android】安卓方向秋招面经记录 https://www.nowcoder.com/discuss/229649 
【安卓&Android】阿里 Android一面 https://www.nowcoder.com/discuss/227437 
【安卓&Android】ihandy汉迪移动客户端android方向面经 https://www.nowcoder.com/discuss/225671 
【安卓&Android】猿辅导客户端Android方向面经凉经 https://www.nowcoder.com/discuss/225670 
【安卓&Android】虎牙客户端android方向一面凉经 https://www.nowcoder.com/discuss/224300 
【安卓&Android】腾讯安卓开发面经 https://www.nowcoder.com/discuss/224576 
【安卓&Android】网易有道Android一面广州批 https://www.nowcoder.com/discuss/224335 
【安卓&Android】字节跳动、oppo安卓开发面筋 https://www.nowcoder.com/discuss/223431 
【安卓&Android】腾讯音乐事业群 Android 移动客户端一二面凉经 https://www.nowcoder.com/discuss/222198 
【安卓&Android】网易杭研院面试 https://www.nowcoder.com/discuss/222165 
【安卓&Android】oppo提前批安卓开发面筋 https://www.nowcoder.com/discuss/214265 
【安卓&Android】oppo提前批安卓开发面筋 https://www.nowcoder.com/discuss/212518 
【安卓&Android】回馈牛客！【安卓&Android】ios移动端已拿意向书 https://www.nowcoder.com/discuss/212124 
【安卓&Android】OPPO提前批 安卓开发岗hr面凉凉 https://www.nowcoder.com/discuss/207439 
【安卓&Android】字节跳动效率工程提前批Android实习面经 https://www.nowcoder.com/discuss/208452 
【安卓&Android】字节跳动Android一面凉经。。 https://www.nowcoder.com/discuss/205830 
【安卓&Android】补发：字节跳动安卓开发实习三轮面经 https://www.nowcoder.com/discuss/203703 
【安卓&Android】字节跳动，Android开发提前批，新鲜面经 https://www.nowcoder.com/discuss/204840 
【安卓&Android】头条提前批安卓岗面经 https://www.nowcoder.com/discuss/204672 

 测试&测开

 【测试&测开】深信服测试面经--武汉地区（没见到HR,应该是凉了）： https://www.nowcoder.com/discuss/117567 
【测试&测开】深信服-测试面经： https://www.nowcoder.com/discuss/117337 

 【测试&测开】招银测开面经： https://www.nowcoder.com/discuss/130888 
【测试&测开】招银网络科技烫手面经： https://www.nowcoder.com/discuss/120264 
【测试&测开】【测试&测开】： https://www.nowcoder.com/discuss/137970 
【测试&测开】发一波百度测开面经，攒一波人品吧 ： https://www.nowcoder.com/discuss/128249 
【测试&测开】百度提前批测开面经： https://www.nowcoder.com/discuss/125206 
【测试&测开】百度测开一面-深圳： https://www.nowcoder.com/discuss/114202 
【测试&测开】百度测开面经（二面凉凉）： https://www.nowcoder.com/discuss/111815 
【测试&测开】百度测开面筋(更新一下二面)： https://www.nowcoder.com/discuss/110218 
【测试&测开】百度测开面经： https://www.nowcoder.com/discuss/109630 
【测试&测开】阿里测开面经 ： https://www.nowcoder.com/discuss/111661 
【测试&测开】阿里测开岗（有且只有一面） https://www.nowcoder.com/discuss/96264 
【测试&测开】阿里测开一面面经 https://www.nowcoder.com/discuss/97445 
【测试&测开】美团测开面经： https://www.nowcoder.com/discuss/117556 
【测试&测开】美团测开四面面筋： https://www.nowcoder.com/discuss/114631 
【测试&测开】刚出炉的美团Java面经： https://www.nowcoder.com/discuss/103038【测试&测开】美团测开面经：https://www.nowcoder.com/discuss/117556 
【测试&测开】美团测开四面面筋： https://www.nowcoder.com/discuss/114631 
【测试&测开】小米测开一二面面经： https://www.nowcoder.com/discuss/130468 
【测试&测开】10月15小米新鲜测开面经 一面凉： https://www.nowcoder.com/discuss/128944 
【测试&测开】中国电信IT研发中心 测开两面面筋： https://www.nowcoder.com/discuss/109998 
【测试&测开】实习-滴滴测开 一二面： https://www.nowcoder.com/discuss/141367 
【测试&测开】网易有道测开一面凉经（北京）： https://www.nowcoder.com/discuss/125264 
【测试&测开】网易测开面经攒人品，等的快秃头了！更新：不秃头了，开奖了： https://www.nowcoder.com/discuss/121300 
【测试&测开】网易测开攒人品： https://www.nowcoder.com/discuss/120569 
【测试&测开】网易互娱测开面经： https://www.nowcoder.com/discuss/114659 
【测试&测开】网易互娱测开一面凉面 https://www.nowcoder.com/discuss/93995 
【测试&测开】网易互娱测开一面，凉凉 https://www.nowcoder.com/discuss/93941 
【测试&测开】网易互娱测开一面凉经 https://www.nowcoder.com/discuss/92672 
【测试&测开】>网易互娱 测开三面 https://www.nowcoder.com/discuss/97251 
【测试&测开】网易传媒（北京）面经～： https://www.nowcoder.com/discuss/103944 
【测试&测开】今天头条分享一波凉凉的测开面经： https://www.nowcoder.com/discuss/119297 
【测试&测开】实习-抖音测开 三面凉： https://www.nowcoder.com/discuss/141370 
【测试&测开】头条测开： https://www.nowcoder.com/discuss/139339 
【测试&测开】头条实习测开岗三面面筋： https://www.nowcoder.com/discuss/143387 
【测试&测开】依图科技测开面经 https://www.nowcoder.com/discuss/96323 
【测试&测开】360北京现场面试测开一面挂面经 https://www.nowcoder.com/discuss/97707 
【测试&测开】搜狗测开一面面经(顺便求二面面经)： https://www.nowcoder.com/discuss/122513 
【测试&测开】贝壳测开面经： https://www.nowcoder.com/discuss/109032 
【测试&测开】去哪儿网测开面经： https://www.nowcoder.com/discuss/113387 
【测试&测开】去哪儿网测开面经： https://www.nowcoder.com/discuss/113387 
【测试&测开】融360测开面经： https://www.nowcoder.com/discuss/136552 
【测试&测开】总结一下自己的面试经验，主要是测开： https://www.nowcoder.com/discuss/126407 
【测试&测开】秋招面经分享（测开和开发都有）： https://www.nowcoder.com/discuss/119016 
【测试&测开】英特尔，京东，百度，阿里面经： https://www.nowcoder.com/discuss/112175 
【测试&测开】秋招到现在的面经（测开，c++）： https://www.nowcoder.com/discuss/109051 
【测试&测开】测开秋招求职面经： https://www.nowcoder.com/discuss/138408 
【测试&测开】兜兜转转还是要去北京了，附上测开面经~： https://www.nowcoder.com/discuss/135632 
【测试&测开】深信服一面+二面+HR面（软件测试）： https://www.nowcoder.com/discuss/119990 
【测试&测开】深信服测试面经--武汉地区（没见到HR,应该是凉了）： https://www.nowcoder.com/discuss/117567 
【测试&测开】深信服-测试面经： https://www.nowcoder.com/discuss/117337 
【测试&测开】百度测试开发工程师二面凉经： https://www.nowcoder.com/discuss/126171 
【测试&测开】百度测试开发面经： https://www.nowcoder.com/discuss/113802 
【测试&测开】百度测试开发一面（凉凉）： https://www.nowcoder.com/discuss/110721 
【测试&测开】百度开发测试岗送人头一面凉经： https://www.nowcoder.com/discuss/109505 
【测试&测开】京东测试开发二面： https://www.nowcoder.com/discuss/118249 
【测试&测开】京东测试开发一面： https://www.nowcoder.com/discuss/117320 
【测试&测开】京东测试开发一面 https://www.nowcoder.com/discuss/92253 
【测试&测开】京东提前批测试开发面试 https://www.nowcoder.com/discuss/92806 
【测试&测开】大疆一面：测试岗 https://www.nowcoder.com/discuss/89085 
【测试&测开】大疆测试岗：二面 https://www.nowcoder.com/discuss/90667 
【测试&测开】美的测试工程师一面： https://www.nowcoder.com/discuss/110554 
【测试&测开】腾讯阿里3+1面经，岗位测试开发： https://www.nowcoder.com/discuss/101602 
【测试&测开】阿里一二面面经，测开岗 https://www.nowcoder.com/discuss/87692 
【测试&测开】秋招第一战：测试开发工程师阿里一面 https://www.nowcoder.com/discuss/88060 
【测试&测开】阿里测开凉经 https://www.nowcoder.com/discuss/90707 
【测试&测开】顺丰测试岗提前批一面 https://www.nowcoder.com/discuss/90692 
【测试&测开】阿里测试开发5面面经 攒人品 https://www.nowcoder.com/discuss/91278 
【测试&测开】阿里测试二面凉凉面经 https://www.nowcoder.com/discuss/89691 
【测试&测开】华为测试岗的面经分享： https://www.nowcoder.com/discuss/113432 
【测试&测开】秋招第一场面试华为测试南研所 https://www.nowcoder.com/discuss/96279 
【测试&测开】顺丰测试岗面经： https://www.nowcoder.com/discuss/118823 
【测试&测开】顺丰科技测试开发HR面 https://www.nowcoder.com/discuss/90946 
【测试&测开】顺丰测试岗提前批一面 https://www.nowcoder.com/discuss/90660 
【测试&测开】顺丰科技测试岗提前批面攒人品 https://www.nowcoder.com/discuss/93682 
【测试&测开】顺丰提前批测试一面技术二面HR https://www.nowcoder.com/discuss/90386 
【测试&测开】华为优招测试面经 https://www.nowcoder.com/discuss/94741 
【测试&测开】9.14 CVTE测试开发凉面T^T： https://www.nowcoder.com/discuss/111580 
【测试&测开】美团-测试开发-一面经验： https://www.nowcoder.com/discuss/101142 
【测试&测开】2018.8.29美团点评测试开发面经（坐标上海）： https://www.nowcoder.com/discuss/100650 
【测试&测开】腾讯一面面经系统测试岗： https://www.nowcoder.com/discuss/97858 
【测试&测开】腾讯一面面经系统测试岗 https://www.nowcoder.com/discuss/97858 
【测试&测开】腾讯阿里3+1面经，岗位测试开发： https://www.nowcoder.com/discuss/101602 
【测试&测开】思特沃克测试面经： https://www.nowcoder.com/discuss/113807 
【测试&测开】vivo。26号测试工程师面试： https://www.nowcoder.com/discuss/118721 
【测试&测开】vivo软件测试岗面经，努力过，等结果，攒人品： https://www.nowcoder.com/discuss/113598 
【测试&测开】金山-软件测试工程师-一面 https://www.nowcoder.com/discuss/96750 
【测试&测开】vipkid测试开发面经(吐槽)： https://www.nowcoder.com/discuss/128791 
【测试&测开】网易游戏测试开发面经： https://www.nowcoder.com/discuss/121343 
【测试&测开】网易测试面经： https://www.nowcoder.com/discuss/113795 
【测试&测开】网易互娱游戏测试面经求offer！ https://www.nowcoder.com/discuss/98123 
【测试&测开】网易互娱游戏测试工程师一二三面 https://www.nowcoder.com/discuss/98045 
【测试&测开】网易游戏，测试开发面经 https://www.nowcoder.com/discuss/93917 
【测试&测开】网易游戏测试开发一面面筋 https://www.nowcoder.com/discuss/93639 
【测试&测开】网易游戏测试面试分享 https://www.nowcoder.com/discuss/94213 
【测试&测开】网易游戏测试开发二面凉经 https://www.nowcoder.com/discuss/96401 
【测试&测开】网易互娱测试开发工程师二面 https://www.nowcoder.com/discuss/96333 
【测试&测开】网易游戏测试二面凉凉帖 https://www.nowcoder.com/discuss/97392 
【测试&测开】网易互娱测试岗，一面，面凉的经 https://www.nowcoder.com/discuss/94008 
【测试&测开】透心凉的网易面筋测试： https://www.nowcoder.com/discuss/111908 
【测试&测开】广州网易有道Java开发工程师一二三面面经：【测试&测开】网易考拉 测试 三面面筋： https://www.nowcoder.com/discuss/100178 
【测试&测开】网易游戏测试工程师面经： https://www.nowcoder.com/discuss/100644 
【测试&测开】网易互娱游戏测试三轮面经： https://www.nowcoder.com/discuss/102147 
【测试&测开】网易游戏互娱游戏测试面经： https://www.nowcoder.com/discuss/100836 
【测试&测开】网易互娱游戏测试面经求offer！： https://www.nowcoder.com/discuss/98123 
【测试&测开】网易互娱游戏测试工程师一二三面： https://www.nowcoder.com/discuss/98045 
【测试&测开】网易游戏测试开发三轮面经（10.26面完）： https://www.nowcoder.com/discuss/137600 
【测试&测开】商汤科技，测试岗二面凉： https://www.nowcoder.com/discuss/116028 
【测试&测开】今日头条测试开发岗面经（一二面，GG）： https://www.nowcoder.com/discuss/139374 
【测试&测开】今日头条/字节跳动补招测试开发凉径： https://www.nowcoder.com/discuss/143070 
【测试&测开】字节跳动/今日头条 测试开发三面： https://www.nowcoder.com/discuss/142739 
【测试&测开】依图测试开发岗面经： https://www.nowcoder.com/discuss/122754 
【测试&测开】360测开一面凉经： https://www.nowcoder.com/discuss/104008 
【测试&测开】360测试岗位面筋： https://www.nowcoder.com/discuss/103913 
【测试&测开】360视频面试 测试开发 一面凉凉 https://www.nowcoder.com/discuss/97203 
【测试&测开】360很失败的面经 https://www.nowcoder.com/discuss/97157 
【测试&测开】搜狗测试开发岗凉面经： https://www.nowcoder.com/discuss/110809 
【测试&测开】知乎测试开发面经～～： https://www.nowcoder.com/discuss/102047 
【测试&测开】快手秋招面经,测试工程师： https://www.nowcoder.com/discuss/101945 
【测试&测开】快手秋招面经,测试工程师： https://www.nowcoder.com/discuss/101945 
【测试&测开】猫眼测试开发一面凉经(内推)： https://www.nowcoder.com/discuss/111702 
【测试&测开】猫眼电话复面面经【测试&测开】： https://www.nowcoder.com/discuss/115486 
【测试&测开】贝壳+测试开发面经： https://www.nowcoder.com/discuss/108573 
【测试&测开】贝壳测试开发面经： https://www.nowcoder.com/discuss/113805 
【测试&测开】贝壳找房测开面筋： https://www.nowcoder.com/discuss/113364 
【测试&测开】去哪儿网测试开发一面面经： https://www.nowcoder.com/discuss/126848 
【测试&测开】恒生电子群面奇葩经历： https://www.nowcoder.com/discuss/122576 
【测试&测开】创梦天地测试工程师一面面经： https://www.nowcoder.com/discuss/136917 
【测试&测开】回馈牛友，发一波测开/测试面经啦： https://www.nowcoder.com/discuss/130841 
【测试&测开】测试/测开面经： https://www.nowcoder.com/discuss/124011 
【测试&测开】结束秋招，回馈牛客，测试开发岗面经： https://www.nowcoder.com/discuss/123153 
【测试&测开】真菜-不是假的菜-废话很多-测试-求职惨路（内附学习资料）： https://www.nowcoder.com/discuss/122667 
【测试&测开】腾讯阿里3+1面经，岗位测试开发： https://www.nowcoder.com/discuss/101602 
【测试&测开】菜鸡的测试/测开秋招面经： https://www.nowcoder.com/discuss/138294 

 【测试&测开】百度测开二面凉经~我止步到这里啦，希望各位小伙伴顺利 https://www.nowcoder.com/discuss/231982 
【测试&测开】深信服- 一面/二面 测开面经 https://www.nowcoder.com/discuss/231613 
【测试&测开】腾讯测开一面面经 https://www.nowcoder.com/discuss/231007 
【测试&测开】大疆测试一面 https://www.nowcoder.com/discuss/231945 
【测试&测开】深信服测试面试经 https://www.nowcoder.com/discuss/233027 
【测试&测开】百度一面面经：测试开发 https://www.nowcoder.com/discuss/230313 
【测试&测开】美团测开二面面经 https://www.nowcoder.com/discuss/229675 
【测试&测开】哔哩哔哩测试一面凉经～我太难了 （后面想起啥我继续补充） https://www.nowcoder.com/discuss/229593 
【测试&测开】盛大测试一面面经 https://www.nowcoder.com/discuss/230170 
【测试&测开】网易雷火秋招 游戏测试 凉经 https://www.nowcoder.com/discuss/229828 
【测试&测开】大疆测开一面 https://www.nowcoder.com/discuss/228911 
【测试&测开】美团测开一面面经 https://www.nowcoder.com/discuss/229149 
【测试&测开】美团测开一面面经 https://www.nowcoder.com/discuss/228661 
【测试&测开】美团测开一面面经 https://www.nowcoder.com/discuss/228653 
【测试&测开】美团测开夺命三连面面经，希望能有好结果 https://www.nowcoder.com/discuss/228648 
【测试&测开】远景电话一面 https://www.nowcoder.com/discuss/228739 
【测试&测开】美团-测试开发-一面面经（电话面试） https://www.nowcoder.com/discuss/228015 
【测试&测开】美团 测试开发一面 https://www.nowcoder.com/discuss/227892 
【测试&测开】美团 测开 https://www.nowcoder.com/discuss/227680 
【测试&测开】网易雷火 游戏测开凉经 https://www.nowcoder.com/discuss/227723 
【测试&测开】橙汁的面试经验分享（百度，诺瓦，平安壹钱包） https://www.nowcoder.com/discuss/228018 
【测试&测开】分享一个新鲜的中兴网安面经，攒人品攒人品 https://www.nowcoder.com/discuss/227635 
【测试&测开】贝壳测开一面凉经 https://www.nowcoder.com/discuss/226915 
【测试&测开】美团点评一面记录 https://www.nowcoder.com/discuss/227110 
【测试&测开】字节跳动一二面凉经 https://www.nowcoder.com/discuss/226825 
【测试&测开】深信服测开电话一面，33min https://www.nowcoder.com/discuss/225828 
【测试&测开】迷迷糊糊的深信服测开一面 https://www.nowcoder.com/discuss/225906 
【测试&测开】深信服长研所测开一面凉经 https://www.nowcoder.com/discuss/226104 
【测试&测开】深信服测开二面凉经 https://www.nowcoder.com/discuss/226045 
【测试&测开】网易互娱测开一面凉经 https://www.nowcoder.com/discuss/224896 
【测试&测开】网易测开一面凉经 https://www.nowcoder.com/discuss/224664 
【测试&测开】网易 测试开发凉面经 2019-8-15 https://www.nowcoder.com/discuss/224291 
【测试&测开】大华二面面经 https://www.nowcoder.com/discuss/224450 
【测试&测开】腾讯系统测试一面 https://www.nowcoder.com/discuss/224440 
【测试&测开】面经趋势科技（开发测试）——一面已跪 https://www.nowcoder.com/discuss/223616 
【测试&测开】哔哩哔哩测试一面 https://www.nowcoder.com/discuss/223567 
【测试&测开】百度测开二面凉经 https://www.nowcoder.com/discuss/223155 
【测试&测开】百度测开一面凉经 https://www.nowcoder.com/discuss/222543 
【测试&测开】顺丰科技一面面经，测开（北京） https://www.nowcoder.com/discuss/223022 
【测试&测开】趋势科技一二面凉经 https://www.nowcoder.com/discuss/222590 
【测试&测开】8.13号顺丰提前批测试一面面经（不知道是不是凉经） https://www.nowcoder.com/discuss/222653 
【测试&测开】腾讯系统测试一面凉经 https://www.nowcoder.com/discuss/222568 
【测试&测开】腾讯测开岗一面 https://www.nowcoder.com/discuss/222049 
【测试&测开】百度测开二面 https://www.nowcoder.com/discuss/219422 
【测试&测开】百度测开三面面试 https://www.nowcoder.com/discuss/220063 
【测试&测开】新鲜热乎的阿里测开一面面经 https://www.nowcoder.com/discuss/220006 
【测试&测开】腾讯测试开发一面 https://www.nowcoder.com/discuss/220399 
【测试&测开】远景测试开发一面，二面 https://www.nowcoder.com/discuss/220067 
【测试&测开】阿里测试工程师二面 https://www.nowcoder.com/discuss/219239 
【测试&测开】百度测开三面面经 https://www.nowcoder.com/discuss/218920 
【测试&测开】百度某部门面试凉经 https://www.nowcoder.com/discuss/218834 
【测试&测开】阿里一面开发测试岗凉经 https://www.nowcoder.com/discuss/218085 
【测试&测开】百度测试一面面经 https://www.nowcoder.com/discuss/217950 
【测试&测开】阿里CBU部门 测试开发面经 https://www.nowcoder.com/discuss/217348 
【测试&测开】百度测开一二面面经 https://www.nowcoder.com/discuss/216513 
【测试&测开】百度测开一二面面经 https://www.nowcoder.com/discuss/216513 
【测试&测开】shopee 测试面经（估计凉凉。。。） https://www.nowcoder.com/discuss/215731 
【测试&测开】shopee测试一面面经 https://www.nowcoder.com/discuss/215613 
【测试&测开】阿里一面，电话面，测开岗 https://www.nowcoder.com/discuss/215382 
【测试&测开】测开面经 头条 阿里 百度 作业帮 https://www.nowcoder.com/discuss/214829 
【测试&测开】测开面经 https://www.nowcoder.com/discuss/214526 
【测试&测开】阿里巴巴新零售技术事业群-数字政务中台事业部测试开发一面凉经 https://www.nowcoder.com/discuss/213258 
【测试&测开】【测试&测开】头条提前批测开面经 https://www.nowcoder.com/discuss/213349 
【测试&测开】2019.07字节跳动 测试开发技术面 https://www.nowcoder.com/discuss/213808 
【测试&测开】作业帮提前批测试开发全流程详细面经 https://www.nowcoder.com/discuss/212867 
【测试&测开】作业帮测开一面凉经 https://www.nowcoder.com/discuss/212805 
【测试&测开】【测试&测开】 https://www.nowcoder.com/discuss/212086 
【测试&测开】作业帮测开面经 https://www.nowcoder.com/discuss/211391 
【测试&测开】百度测开 一面 https://www.nowcoder.com/discuss/210606 
【测试&测开】字节提前批测试开发三面 https://www.nowcoder.com/discuss/210319 
【测试&测开】作业帮提前批测开一面二面hr面经 https://www.nowcoder.com/discuss/210324 
【测试&测开】oppo测开面经 https://www.nowcoder.com/discuss/207905 
【测试&测开】腾讯测开一面凉经 https://www.nowcoder.com/discuss/208851 
【测试&测开】腾讯测开一面凉经 https://www.nowcoder.com/discuss/208851 
【测试&测开】字节跳动提前批测开劝退一面面经 https://www.nowcoder.com/discuss/207520 
【测试&测开】抖音火山测开凉经 https://www.nowcoder.com/discuss/208097 
【测试&测开】回馈一下牛客网（字节跳动测试开发一二面凉经） https://www.nowcoder.com/discuss/209199 
【测试&测开】回馈一下牛客网（字节跳动测试开发一二面凉经） https://www.nowcoder.com/discuss/209199 
【测试&测开】作业帮提前批测开面试 https://www.nowcoder.com/discuss/208151 
【测试&测开】作业帮提前批测开面经 https://www.nowcoder.com/discuss/206572 
【测试&测开】字节跳动凉经（一、二、三+boss(hr)面） https://www.nowcoder.com/discuss/205655 
【测试&测开】百度移动生态质量部测开123面试经验 https://www.nowcoder.com/discuss/203227 
【测试&测开】2019字节跳动秋招提前批测试开发岗一面 https://www.nowcoder.com/discuss/203384 
【测试&测开】面经：字节跳动测试开发提前批面经 https://www.nowcoder.com/discuss/203453 
【测试&测开】字节跳动 游戏测开一二三面面经 https://www.nowcoder.com/discuss/204117 
【测试&测开】字节跳动游戏测试开发二面凉经 https://www.nowcoder.com/discuss/204107 
【测试&测开】字节跳动游戏提前批-杭州-测开三面 https://www.nowcoder.com/discuss/204318 
【测试&测开】字节跳动 测试开发提前批一二面 https://www.nowcoder.com/discuss/205153 
【测试&测开】字节跳动测试提前批一面 https://www.nowcoder.com/discuss/203485 
【测试&测开】字节跳动 测试一面凉经 https://www.nowcoder.com/discuss/205286 
【测试&测开】头条测试工程师一面 https://www.nowcoder.com/discuss/205092 

 大数据

 【大数据】上海浦发面经(秋招面经持续更新，攒人品) https://www.nowcoder.com/discuss/90871 
【大数据】浦发银行大数据创新岗上海打卡 https://www.nowcoder.com/discuss/91675 
【大数据】浦发银行总行（上海）大数据岗8月6号面经 https://www.nowcoder.com/discuss/91911 
【大数据】深信服提前批面经（大数据平台研发岗） https://www.nowcoder.com/discuss/86060 
【大数据】感谢牛客网！发一波面经！阿里、网易游戏、京东等offer。： https://www.nowcoder.com/discuss/101712 
【大数据】华为大数据面经： https://www.nowcoder.com/discuss/120732 
【大数据】顺丰科技面经-大数据研发： https://www.nowcoder.com/discuss/120499 
【大数据】顺丰科技一面面经（内推--大数据挖掘与分析岗） https://www.nowcoder.com/discuss/88818 
【大数据】 【大数据】信息科技岗(大数据创新岗)8.6日上海总行面经 https://www.nowcoder.com/discuss/91147 
【大数据】上海浦发面经(秋招面经持续更新，攒人品) https://www.nowcoder.com/discuss/90871 
【大数据】浦发银行大数据创新岗上海打卡 https://www.nowcoder.com/discuss/91675 
【大数据】浦发银行总行（上海）大数据岗8月6号面经 https://www.nowcoder.com/discuss/91911 
【大数据】菜鸟的面试：科大讯飞和作业帮 https://www.nowcoder.com/discuss/90245 
【大数据】海康威视-大数据岗-一面面经总结18年8月8日 https://www.nowcoder.com/discuss/92149 
【大数据】网易大数据面经--有点凉： https://www.nowcoder.com/discuss/118336 
【大数据】网易大数据面经： https://www.nowcoder.com/discuss/103119 
【大数据】网易杭研所(大数据、云计算)Java研发面经 https://www.nowcoder.com/discuss/97078 
【大数据】感谢牛客网！发一波面经！阿里、网易游戏、京东等offer。： https://www.nowcoder.com/discuss/101712 
【大数据】网易大数据面经： https://www.nowcoder.com/discuss/103119 
【大数据】网易杭研大数据玄面分享： https://www.nowcoder.com/discuss/100227 
【大数据】网易云音乐大数据：一点引导都没有的二面面试官： https://www.nowcoder.com/discuss/99553 
【大数据】网易（北京）-大数据开发工程师二面面经： https://www.nowcoder.com/discuss/99861 
【大数据】头条一面面经： https://www.nowcoder.com/discuss/127831 
【大数据】360企业安全大数据开发面经： https://www.nowcoder.com/discuss/111970 
【大数据】第四范式大数据开发： https://www.nowcoder.com/discuss/110224 
【大数据】
【大数据】说好的面经来啦！！ 数据挖掘/大数据开发： https://www.nowcoder.com/discuss/127104 
【大数据】十余家公司大数据开发面经： https://www.nowcoder.com/discuss/109518 
【大数据】美团、网易、贝壳、华为、小米、携程、快手大数据开发面经： https://www.nowcoder.com/discuss/106368 
【大数据】新鲜出炉的浦发大数据岗面筋： https://www.nowcoder.com/discuss/140690 
【大数据】分享一个大数据的面经： https://www.nowcoder.com/discuss/142963 
【大数据】大数据开发（研发）面经： https://www.nowcoder.com/discuss/120918 
【大数据】大数据面经好少啊，我来写点： https://www.nowcoder.com/discuss/119208 

 【大数据】贝壳找房 北京现场面 大数据开发 三面面经 https://www.nowcoder.com/discuss/233224 
【大数据】浙江大华提前批大数据研发3面面经 https://www.nowcoder.com/discuss/232010 
【大数据】有赞 现场 四面（加面技术面） 大数据面经 https://www.nowcoder.com/discuss/232897 
【大数据】网易大数据开发二面 https://www.nowcoder.com/discuss/229184 
【大数据】柠檬微趣 一面凉经 岗位大数据开发工程师 https://www.nowcoder.com/discuss/226875 
【大数据】8月17 17:00 浙江大华 大数据一面凉经 28分钟 https://www.nowcoder.com/discuss/226297 
【大数据】【大数据】凉面之“没有最菜只有更菜”-大数据工程师 https://www.nowcoder.com/discuss/226018 
【大数据】流利说大数据一面凉经 https://www.nowcoder.com/discuss/225837 
【大数据】字节跳动大数据一面凉经 https://www.nowcoder.com/discuss/226685 
【大数据】字节跳动大数据工程师二面凉经 https://www.nowcoder.com/discuss/226652 
【大数据】腾讯云一面面经，非典型，已过 https://www.nowcoder.com/discuss/226202 
【大数据】网易严选大数据开发凉经 https://www.nowcoder.com/discuss/225340 
【大数据】蘑菇街大数据开发一面 https://www.nowcoder.com/discuss/224311 
【大数据】网易严选大数据岗位内推一面面经 https://www.nowcoder.com/discuss/224968 
【大数据】大数据海康面经 https://www.nowcoder.com/discuss/224086 
【大数据】【大数据】顺丰提前批 大数据挖掘与分析 一面 https://www.nowcoder.com/discuss/223163 
【大数据】顺丰科技视频面-大数据开发 https://www.nowcoder.com/discuss/221382 
【大数据】顺丰科技 大数据分析与挖掘一面凉经 https://www.nowcoder.com/discuss/218228 
【大数据】顺丰科技 大数据挖掘与分析工程师 一面面经 https://www.nowcoder.com/discuss/217930 
【大数据】头条提前批三轮面试终于结束了 https://www.nowcoder.com/discuss/212794 
【大数据】阿里大数据平台一面面经 https://www.nowcoder.com/discuss/210776 
【大数据】字节跳动（提前批）二面凉经 https://www.nowcoder.com/discuss/210332 
【大数据】字节跳动大数据岗 https://www.nowcoder.com/discuss/204836 
【大数据】字节跳动提前批 大数据面经 = = https://www.nowcoder.com/discuss/204677 

 安全

 【安全】企业安全意向offer，安全岗终于开张了： https://www.nowcoder.com/discuss/118730 
【安全】秋招季面试经验分享——360企业安全： https://www.nowcoder.com/discuss/121260 
【安全】喜提360企业安全offer一枚（附面经--运维开发）： https://www.nowcoder.com/discuss/115982 
【安全】360企业安全一面二面凉面经： https://www.nowcoder.com/discuss/115414 
【安全】360企业安全武汉现场一面凉经： https://www.nowcoder.com/discuss/115218 
【安全】360企业安全后端开发二面： https://www.nowcoder.com/discuss/114717 
【安全】重庆360企业安全凉经： https://www.nowcoder.com/discuss/114170 
【安全】360企业安全服务器端开发面经： https://www.nowcoder.com/discuss/113579 
【安全】360意向offer，面经感恩牛客： https://www.nowcoder.com/discuss/113400 
【安全】360企业安全大数据开发面经： https://www.nowcoder.com/discuss/111970 
【安全】360面经 个人安全-服务端开发(C++)： https://www.nowcoder.com/discuss/111818 
【安全】深信服一面，c++研发（网络安全方向） https://www.nowcoder.com/discuss/87521 
【安全】vivo武汉 安全工程师： https://www.nowcoder.com/discuss/113212 
【安全】【安全】内容安全中心-内容监控专员面试 https://www.nowcoder.com/discuss/95974 
【安全】企业安全意向offer，安全岗终于开张了： https://www.nowcoder.com/discuss/118730 
【安全】秋招季面试经验分享——360企业安全： https://www.nowcoder.com/discuss/121260 
【安全】360企业安全一面二面凉面经： https://www.nowcoder.com/discuss/115414 
【安全】360企业安全武汉现场一面凉经： https://www.nowcoder.com/discuss/115218 
【安全】360企业安全后端开发二面： https://www.nowcoder.com/discuss/114717 
【安全】360企业安全服务器端开发面经： https://www.nowcoder.com/discuss/113579 
【安全】本渣来总结下安全岗的面试经历，等一个好运： https://www.nowcoder.com/discuss/111857 
【安全】安全岗菜鸡的坎坷秋招路（面经+笔试题分享）： https://www.nowcoder.com/discuss/139226 
【安全】网易、360企业安全、有赞和远景能源(Android)面经： https://www.nowcoder.com/discuss/136714 
【安全】2019/8 阿里安全秋招（ing） https://www.nowcoder.com/discuss/228754 
【安全】腾讯一、二面凉面面经-安全研究（二进制） https://www.nowcoder.com/discuss/228493 
【安全】oppo安全工程师两面,等hr https://www.nowcoder.com/discuss/205533 

 运维

 【运维】我的秋招面经——问题篇： https://www.nowcoder.com/discuss/125144 
【运维】攒波人品，希望国庆后能够开奖： https://www.nowcoder.com/discuss/123466 
【运维】今天有点邪乎，51加面，小米还加面： https://www.nowcoder.com/discuss/125903 
【运维】两天五场面试。。发波面经攒人品（运维开发）： https://www.nowcoder.com/discuss/119106 

 【运维】一名普通学生的2018秋招经历： https://www.nowcoder.com/discuss/144556 
【运维】塞翁失马，焉知非福： https://www.nowcoder.com/discuss/143996 
【运维】51信用卡面经，求好运： https://www.nowcoder.com/discuss/124783 
【运维】喜提360企业安全offer一枚（附面经--运维开发）： https://www.nowcoder.com/discuss/115982 
【运维】百度凉凉，但还是分享一波面经： https://www.nowcoder.com/discuss/119010 
【运维】美团点评运维面试题： https://www.nowcoder.com/discuss/117425 
【运维】美团点评运维面试题： https://www.nowcoder.com/discuss/117425 
【运维】小米面试，感谢牛客网的大家分享，还在等结果： https://www.nowcoder.com/discuss/115683 
【运维】断断续续的1小时小米一面： https://www.nowcoder.com/discuss/103057 
【运维】技术小白到vivo offer之路： https://www.nowcoder.com/discuss/97566 
【运维】vivo运维一面+HR面 https://www.nowcoder.com/discuss/94264 
【运维】感谢网易捞我出来，太激动了： https://www.nowcoder.com/discuss/125186 
【运维】喜提360企业安全offer一枚（附面经--运维开发）： https://www.nowcoder.com/discuss/115982 
【运维】虎牙OS系统运维一面+二面+HR面： https://www.nowcoder.com/discuss/113967 
【运维】51信用卡面经，求好运： https://www.nowcoder.com/discuss/124783 
【运维】我的秋招面经——问题篇： https://www.nowcoder.com/discuss/125144 
【运维】攒波人品，希望国庆后能够开奖： https://www.nowcoder.com/discuss/123466 
【运维】今天有点邪乎，51加面，小米还加面： https://www.nowcoder.com/discuss/125903 
【运维】两天五场面试。。发波面经攒人品（运维开发）： https://www.nowcoder.com/discuss/119106 
【运维】凉经反馈希望不再凉凉： https://www.nowcoder.com/discuss/112144 
【运维】秋招总结（运维）： https://www.nowcoder.com/discuss/142474 

 【运维】美团提前批 运维最新面经8月22日 https://www.nowcoder.com/discuss/231023 
【运维】小米 运维开发新鲜面筋 https://www.nowcoder.com/discuss/231289 
【运维】攒人品啦~热乎的网易面经 https://www.nowcoder.com/discuss/227418 
【运维】一般般可爱的浦发面筋 https://www.nowcoder.com/discuss/226201 

 前端

 【前端】阿里前端2面面经 [已回绝] 写个面经攒攒人品 https://www.nowcoder.com/discuss/95295 
【前端】阿里前端内推一面-电话面试，在线编程 https://www.nowcoder.com/discuss/95215 
【前端】 阿里前端一面凉经 https://www.nowcoder.com/discuss/92808 
【前端】 阿里前端一面面经 https://www.nowcoder.com/discuss/93672 
【前端】阿里二面凉透经 https://www.nowcoder.com/discuss/94724 
【前端】阿里前端面经 https://www.nowcoder.com/discuss/96781 

 【前端】【前端】一面顺利通过 https://www.nowcoder.com/discuss/90535 
【前端】【前端】一次凉凉的二面 https://www.nowcoder.com/discuss/92033 
【前端】 有赞前端一面 https://www.nowcoder.com/discuss/93642 
【前端】有赞前端js面经一面 https://www.nowcoder.com/discuss/93681 

 【前端】绿盟科技实习面经： https://www.nowcoder.com/discuss/113284 
【前端】百信银行校园招聘： https://www.nowcoder.com/discuss/112972 
【前端】2018.9.29招银网络电话面： https://www.nowcoder.com/discuss/121326 
【前端】招银网络科技面经： https://www.nowcoder.com/discuss/121287 
【前端】【前端】一面顺利通过 https://www.nowcoder.com/discuss/90535 
【前端】【前端】一次凉凉的二面 https://www.nowcoder.com/discuss/92033 
【前端】有赞前端一面 https://www.nowcoder.com/discuss/93642 
【前端】有赞前端js面经一面 https://www.nowcoder.com/discuss/93681 
【前端】多益前端一面 https://www.nowcoder.com/discuss/96296 
【前端】百度秋招一面面经，武汉区： https://www.nowcoder.com/discuss/111446 
【前端】百度智能云前端面经 https://www.nowcoder.com/discuss/91112 
【前端】百度前端面经 https://www.nowcoder.com/discuss/97957 
【前端】百度fex面经： https://www.nowcoder.com/discuss/103817 
【前端】百度前端面经： https://www.nowcoder.com/discuss/97957 
【前端】码一篇京东历程： https://www.nowcoder.com/discuss/122088 
【前端】京东广州场前端初试、复试面经： https://www.nowcoder.com/discuss/120128 
【前端】京东前端面试恕我难以洞察您老人家的心： https://www.nowcoder.com/discuss/112872 
【前端】京东前端一面还不知道结果： https://www.nowcoder.com/discuss/111883 
【前端】京东北京前端1面： https://www.nowcoder.com/discuss/110831 
【前端】京东前端一面面筋，已过，18号二面。： https://www.nowcoder.com/discuss/110828 
【前端】认真写下阿里的面筋，祝福大家收到满意的offer（前端向）： https://www.nowcoder.com/discuss/102509 
【前端】阿里前端2面面经[已回绝]写个面经攒攒人品 https://www.nowcoder.com/discuss/95295 
【前端】阿里前端内推一面-电话面试，在线编程 https://www.nowcoder.com/discuss/95215 
【前端】阿里前端一面凉经 https://www.nowcoder.com/discuss/92808 
【前端】阿里前端一面面经 https://www.nowcoder.com/discuss/93672 
【前端】阿里二面凉透经 https://www.nowcoder.com/discuss/94724 
【前端】阿里前端面经 https://www.nowcoder.com/discuss/96781 
【前端】阿里天猫前端一面 https://www.nowcoder.com/discuss/90347 
【前端】阿里菜鸟前端一面 https://www.nowcoder.com/discuss/92272 
【前端】时隔26天后的阿里菜鸟二面 https://www.nowcoder.com/discuss/94106 
【前端】发下阿里三面凉经 https://www.nowcoder.com/discuss/94400 
【前端】前端阿里二面（彻底凉凉血泪教训无参考价值） https://www.nowcoder.com/discuss/97247 
【前端】阿里天猫前端js面经一面 https://www.nowcoder.com/discuss/93504 
【前端】曾很喜欢华为现在不知道说什么： https://www.nowcoder.com/discuss/114010 
【前端】顺丰前端面试： https://www.nowcoder.com/discuss/112130 
【前端】顺丰前端一面凉凉攒人品 https://www.nowcoder.com/discuss/90509 
【前端】顺丰前端视频一面 https://www.nowcoder.com/discuss/90447 
【前端】阿里蚂蚁金服前端一面 https://www.nowcoder.com/discuss/90133 
【前端】阿里一面 https://www.nowcoder.com/discuss/93483 
【前端】阿里前端体验技术部二面 https://www.nowcoder.com/discuss/96496 
【前端】9-14广州CVTE现场前端一面（已凉）： https://www.nowcoder.com/discuss/111510 
【前端】CVTE前端一面 https://www.nowcoder.com/discuss/88493 
【前端】CVTE前端电话一面 https://www.nowcoder.com/discuss/88561 
【前端】CVTE前端开发一面面经 https://www.nowcoder.com/discuss/88607 
【前端】CVTE前端一面面经 https://www.nowcoder.com/discuss/88621 
【前端】cvte前端一面 https://www.nowcoder.com/discuss/88627 
【前端】CVTE前端一面面经 https://www.nowcoder.com/discuss/88897 
【前端】CVTE一面+二面 https://www.nowcoder.com/discuss/90334 
【前端】CVTE HR面 https://www.nowcoder.com/discuss/92649 
【前端】CVTE终面 https://www.nowcoder.com/discuss/93549 
【前端】成都美团前端面试： https://www.nowcoder.com/discuss/118580 
【前端】西安美团前端一面： https://www.nowcoder.com/discuss/112861 
【前端】美团点评前端面经（二三面+hr面）： https://www.nowcoder.com/discuss/103755 
【前端】西安美团前端一面： https://www.nowcoder.com/discuss/112861 
【前端】美团一面： https://www.nowcoder.com/discuss/101449 
【前端】美团前端一、二面面经： https://www.nowcoder.com/discuss/99954 
【前端】美团前端二面： https://www.nowcoder.com/discuss/99736 
【前端】美团前端一面： https://www.nowcoder.com/discuss/99519 
【前端】美团前端一面凉面： https://www.nowcoder.com/discuss/99289 
【前端】美团前端面经： https://www.nowcoder.com/discuss/97562 
【前端】美团前端一面 https://www.nowcoder.com/discuss/97847 
【前端】美团前端面经 https://www.nowcoder.com/discuss/97562 
【前端】美团一面： https://www.nowcoder.com/discuss/101449 
【前端】美团前端意向书get奉上面经： https://www.nowcoder.com/discuss/106576 
【前端】腾讯前端提前批两面+正式批三面（持续更新中）： https://www.nowcoder.com/discuss/120047 
【前端】成都腾讯一面： https://www.nowcoder.com/discuss/120035 
【前端】腾讯凉面： https://www.nowcoder.com/discuss/118723 
【前端】腾讯云前端一面凉经： https://www.nowcoder.com/discuss/101093 
【前端】腾讯前端一面凉经： https://www.nowcoder.com/discuss/98475 
【前端】记十分坎坷的腾讯深圳前端面试经历 https://www.nowcoder.com/discuss/96602 
【前端】昨天投今天面，令人窒息的腾讯前端一面(二面待更新) https://www.nowcoder.com/discuss/88698 
【前端】腾讯MIG前端一面 https://www.nowcoder.com/discuss/96724 
【前端】腾讯前端一面凉经 https://www.nowcoder.com/discuss/91201 
【前端】腾讯前端一面 https://www.nowcoder.com/discuss/90243 
【前端】腾讯wxg前端一面面经 https://www.nowcoder.com/discuss/92679 
【前端】腾讯前端一面（好凉好冷） https://www.nowcoder.com/discuss/93079 
【前端】小米前端视频一面： https://www.nowcoder.com/discuss/109130 
【前端】小米前端电话一面： https://www.nowcoder.com/discuss/108736 
【前端】小米一面面筋： https://www.nowcoder.com/discuss/108694 
【前端】thoughtworks前端技术面+ hr面 https://www.nowcoder.com/discuss/90531 
【前端】金山WPS前端凉面筋 https://www.nowcoder.com/discuss/97137 
【前端】拼多多前端二面： https://www.nowcoder.com/discuss/98470 
【前端】拼多多2019提前批web前端研发岗笔试 https://www.nowcoder.com/discuss/90910 
【前端】拼多多Web前端面经——一面+二面（等结果中 ）： https://www.nowcoder.com/discuss/143035 
【前端】菜是原罪，可是今天真的是被气到了： https://www.nowcoder.com/discuss/115265 
【前端】9.14科大讯飞前端工程师岗位面经： https://www.nowcoder.com/discuss/109356 
【前端】网易前端二面： https://www.nowcoder.com/discuss/103229 
【前端】网易考拉前端开奖啦 分享一波面筋： https://www.nowcoder.com/discuss/102838 
【前端】记网易杭研（教育文漫）前端面试 https://www.nowcoder.com/discuss/96587 
【前端】网易前端面经 https://www.nowcoder.com/discuss/97233 
【前端】网易前端校招一面凉经 https://www.nowcoder.com/discuss/97212 
【前端】广州网易邮件事业部前端一面二面凉面（面经） https://www.nowcoder.com/discuss/97459 
【前端】网易前端一面挂经 https://www.nowcoder.com/discuss/97442 
【前端】网易前端二面： https://www.nowcoder.com/discuss/103229 
【前端】网易考拉前端开奖啦 分享一波面筋： https://www.nowcoder.com/discuss/102838 
【前端】网易有道前端凉经好冷： https://www.nowcoder.com/discuss/100555 
【前端】网易考拉前端面经： https://www.nowcoder.com/discuss/99069 
【前端】前端视频三面+详解： https://www.nowcoder.com/discuss/128106 
【前端】头条凉经： https://www.nowcoder.com/discuss/119796 
【前端】字节跳动笔试面经： https://www.nowcoder.com/discuss/109068 
【前端】头条一面凉经 https://www.nowcoder.com/discuss/92523 
【前端】头条前端面经： https://www.nowcoder.com/discuss/141443 
【前端】猿辅导前端一面： https://www.nowcoder.com/discuss/97744 
【前端】猿辅导前端面筋 https://www.nowcoder.com/discuss/93354 
【前端】猿辅导前端一面 https://www.nowcoder.com/discuss/97744 
【前端】【前端】一面 https://www.nowcoder.com/discuss/95983 
【前端】老虎证券前端： https://www.nowcoder.com/discuss/113599 
【前端】【前端】等二面通知： https://www.nowcoder.com/discuss/99625 
【前端】老虎证券前端一面： https://www.nowcoder.com/discuss/99056 
【前端】携程前端一面面筋 https://www.nowcoder.com/discuss/97545 
【前端】远景能源一面： https://www.nowcoder.com/discuss/101479 
【前端】搜狗校招专场三面： https://www.nowcoder.com/discuss/114070 
【前端】知乎提前批前端面经： https://www.nowcoder.com/discuss/103707 
【前端】快手前端视频一、二面： https://www.nowcoder.com/discuss/101914 
【前端】【前端】口头offer： https://www.nowcoder.com/discuss/99160 
【前端】快手前端视频一、二面： https://www.nowcoder.com/discuss/101914 
【前端】猫眼前端面试，一面～三面，不知道，能通过不： https://www.nowcoder.com/discuss/101321 
【前端】猫眼前端面筋…回馈牛客攒点人品…怕是凉了： https://www.nowcoder.com/discuss/106647 
【前端】猫眼前端北京备胎面： https://www.nowcoder.com/discuss/139117 
【前端】用友前端一面： https://www.nowcoder.com/discuss/108776 
【前端】贝壳开到奖了，发一波面筋吧： https://www.nowcoder.com/discuss/122044 
【前端】贝壳前端一面二面hr面凉面筋： https://www.nowcoder.com/discuss/99003 
【前端】很幸运，结束秋招。面筋奉上。： https://www.nowcoder.com/discuss/106577 
【前端】纷享销客前端一二面： https://www.nowcoder.com/discuss/103876 
【前端】追一科技前端凉经： https://www.nowcoder.com/discuss/102875 
【前端】富途前端线下面试： https://www.nowcoder.com/discuss/110345 
【前端】虎牙前端一面： https://www.nowcoder.com/discuss/110250 
【前端】虎牙前端一面： https://www.nowcoder.com/discuss/110250 
【前端】shopee技术终面+HR面： https://www.nowcoder.com/discuss/125422 
【前端】shopee二面： https://www.nowcoder.com/discuss/119657 
【前端】码一篇千千音乐面经： https://www.nowcoder.com/discuss/126732 
【前端】涂鸦智能电话面试,前端岗： https://www.nowcoder.com/discuss/143275 
【前端】分享一波前端面筋，共勉，加油吧： https://www.nowcoder.com/discuss/128497 
【前端】前端面经：途牛，米哈游： https://www.nowcoder.com/discuss/127436 
【前端】从0offer到一天谈完薪资，几乎结束秋招，前端面经回馈牛客： https://www.nowcoder.com/discuss/127134 
【前端】前端秋招面经汇总： https://www.nowcoder.com/discuss/126617 
【前端】秋招结束，9 offer，面经分享一波，加油骚年们！： https://www.nowcoder.com/discuss/125303 
【前端】硕渣百度阿里腾讯美团京东爱奇艺58面经 已签华为： https://www.nowcoder.com/discuss/122178 
【前端】百度阿里网易大疆等大小厂前端校招面筋： https://www.nowcoder.com/discuss/123161 
【前端】2019校招前端面试总结： https://www.nowcoder.com/discuss/125842 
【前端】前端不完全面经： https://www.nowcoder.com/discuss/122366 
【前端】码一篇知乎面经： https://www.nowcoder.com/discuss/122076 
【前端】码一篇知乎面经： https://www.nowcoder.com/discuss/122076 
【前端】一波前端面经，回馈牛客 ： https://www.nowcoder.com/discuss/119115 
【前端】几个公司的前端面经： https://www.nowcoder.com/discuss/117653 
【前端】腾讯+网易前端面经： https://www.nowcoder.com/discuss/117490 
【前端】链家&贝壳找房凉经： https://www.nowcoder.com/discuss/114795 
【前端】吉比特&雷霆游戏凉经： https://www.nowcoder.com/discuss/114837 
【前端】不带劲的前端烤面筋： https://www.nowcoder.com/discuss/114699 
【前端】分享下暑期实习到现在的秋招经历，顺便求offer比较，谢谢 ： https://www.nowcoder.com/discuss/112117 
【前端】腾讯，百度，京东，美团，VIVO，VIPKID面经和一些感想： https://www.nowcoder.com/discuss/109055 
【前端】快手/头条/BIGO前端面经： https://www.nowcoder.com/discuss/111688 
【前端】百度&多益一面： https://www.nowcoder.com/discuss/110475 
【前端】9月第一天 总结了一下八月份的提前批面试： https://www.nowcoder.com/discuss/101938 
【前端】前端校招提前批，8月收尾： https://www.nowcoder.com/discuss/100430 
【前端】大厂面试经验小汇总（2018秋招）： https://www.nowcoder.com/discuss/100224 
【前端】拿到了几个自己比较满意的offer，特来牛客还愿。： https://www.nowcoder.com/discuss/98417 
【前端】（打怪升级中）炮灰的前端面经（美团、网易有道、小米）： https://www.nowcoder.com/discuss/137094 
【前端】秋招结束，感恩牛客： https://www.nowcoder.com/discuss/140716 
【前端】秋招面经合集—前端大作战！： https://www.nowcoder.com/discuss/142989 
【前端】麻烦给前端菜鸡一条活路[狗头]： https://www.nowcoder.com/discuss/142305 
【前端】秋招总结，来自山区的双非本科少年（超长待机！）： https://www.nowcoder.com/discuss/141877 
【前端】前端渣本的打怪历程： https://www.nowcoder.com/discuss/122813 
【前端】一篇还算正规的前端面经： https://www.nowcoder.com/discuss/122092 
【前端】从春招到秋招的个人经历，前端岗： https://www.nowcoder.com/discuss/122960 
【前端】前端基础面试题总结： https://www.nowcoder.com/discuss/136331 

 【前端】贝壳前端一二面面经 https://www.nowcoder.com/discuss/232762 
【前端】东方财富前端提前批一面 https://www.nowcoder.com/discuss/231021 
【前端】美团一面分享 https://www.nowcoder.com/discuss/232355 
【前端】美团点评前端烤面筋汇总 https://www.nowcoder.com/discuss/232237 
【前端】美团前端三面，凉经 https://www.nowcoder.com/discuss/231627 
【前端】拼多多前端提前批二面凉凉 https://www.nowcoder.com/discuss/231017 
【前端】拼多多 前端 一面面经 https://www.nowcoder.com/discuss/230495 
【前端】猿辅导前端一面面经 https://www.nowcoder.com/discuss/231819 
【前端】网易有道 前端 面经 一面 二面 https://www.nowcoder.com/discuss/230621 
【前端】前端：网易云音乐面经 https://www.nowcoder.com/discuss/233112 
【前端】小米内推前端1-3面面经 https://www.nowcoder.com/discuss/231034 
【前端】杭州有赞前端面试 https://www.nowcoder.com/discuss/232732 
【前端】美团前端凉凉 https://www.nowcoder.com/discuss/230293 
【前端】美团LBS部门前端二面凉经～ https://www.nowcoder.com/discuss/230242 
【前端】腾讯前端一面凉经 https://www.nowcoder.com/discuss/229709 
【前端】美团前端电话面试新鲜出炉 https://www.nowcoder.com/discuss/229360 
【前端】美团一二面前端面筋 https://www.nowcoder.com/discuss/229285 
【前端】前端二面 https://www.nowcoder.com/discuss/228651 
【前端】pdd前端一面凉经 https://www.nowcoder.com/discuss/229361 
【前端】远景前端一面 https://www.nowcoder.com/discuss/228783 
【前端】云从前端二面 https://www.nowcoder.com/discuss/229308 
【前端】珠海格力一面 前端 https://www.nowcoder.com/discuss/227954 
【前端】美团前端一面面经 https://www.nowcoder.com/discuss/227523 
【前端】前端：拿到快手意向书了，分享一波腾讯的面经 https://www.nowcoder.com/discuss/228100 
【前端】8.19腾讯前端一面 https://www.nowcoder.com/discuss/227812 
【前端】网易云音乐前端一面凉经 https://www.nowcoder.com/discuss/227686 
【前端】网易杭研一面二面凉经 https://www.nowcoder.com/discuss/227398 
【前端】首次面试字节跳动两面凉经，菜鸟一个，勿喷。 https://www.nowcoder.com/discuss/227853 
【前端】蘑菇街前端一面凉经 https://www.nowcoder.com/discuss/227777 
【前端】深信服前端电话二面(同时也求个offer) https://www.nowcoder.com/discuss/227734 
【前端】Bilibili 前端面经 https://www.nowcoder.com/discuss/226790 
【前端】贝壳 前端 提前批 一面挂 https://www.nowcoder.com/discuss/226911 
【前端】贝壳前端面经 https://www.nowcoder.com/discuss/226844 
【前端】拼多多一面 https://www.nowcoder.com/discuss/226855 
【前端】字节跳动两次凉经 https://www.nowcoder.com/discuss/226994 
【前端】字节跳动前端一面凉经 https://www.nowcoder.com/discuss/226798 
【前端】哔哩哔哩 前端 https://www.nowcoder.com/discuss/225896 
【前端】【前端】前端二面，坐等感谢信 https://www.nowcoder.com/discuss/226520 
【前端】欢聚时代面经（前端） https://www.nowcoder.com/discuss/225885 
【前端】美团点评-校招-前端一面 https://www.nowcoder.com/discuss/225368 
【前端】深信服一面过经 https://www.nowcoder.com/discuss/225869 
【前端】深信服 一面面经. https://www.nowcoder.com/discuss/225843 
【前端】吐槽一下腾讯的二面面试官，含面经 https://www.nowcoder.com/discuss/225909 
【前端】前端菜鸡的网易远程一面 https://www.nowcoder.com/discuss/225640 
【前端】网易一面面经 https://www.nowcoder.com/discuss/225364 
【前端】远景智能前端一面 https://www.nowcoder.com/discuss/226590 
【前端】字节前端一面凉经 https://www.nowcoder.com/discuss/226691 
【前端】新鲜出炉的百度前端凉经 https://www.nowcoder.com/discuss/224549 
【前端】美团点评 前端 一面面经 https://www.nowcoder.com/discuss/224950 
【前端】美团前端面筋 https://www.nowcoder.com/discuss/224861 
【前端】【前端】前端一面，大家秋招加油 https://www.nowcoder.com/discuss/224560 
【前端】网易云音乐前端一面凉经 https://www.nowcoder.com/discuss/224355 
【前端】阿里一面，已通过 https://www.nowcoder.com/discuss/223810 
【前端】2019校照 前端岗位（面经攒人品） https://www.nowcoder.com/discuss/223737 
【前端】美团一面 https://www.nowcoder.com/discuss/224050 
【前端】作业帮前端提前批一面 https://www.nowcoder.com/discuss/223692 
【前端】哔哩哔哩 前端一面 https://www.nowcoder.com/discuss/222509 
【前端】蘑菇街前端一面 https://www.nowcoder.com/discuss/222656 
【前端】搜狗面试（口头offer） https://www.nowcoder.com/discuss/222764 
【前端】前端腾讯一面(电话面试) https://www.nowcoder.com/discuss/222755 
【前端】东方财富前端面经 https://www.nowcoder.com/discuss/221792 
【前端】【前端】前端一面 https://www.nowcoder.com/discuss/221901 
【前端】阿里一面、美团一面 https://www.nowcoder.com/discuss/222013 
【前端】蘑菇街一面 https://www.nowcoder.com/discuss/221992 
【前端】网易前端内推一面凉经 https://www.nowcoder.com/discuss/221804 
【前端】作业帮，一波三折的一面,前端 https://www.nowcoder.com/discuss/222147 
【前端】百度前端二面凉经，我太难了 https://www.nowcoder.com/discuss/220899 
【前端】【前端】前端一面，大家秋招加油 https://www.nowcoder.com/discuss/219279 
【前端】武汉拼多多前端提前批一二面加hr面面经，凉凉 https://www.nowcoder.com/discuss/220490 
【前端】字节提前批+猿辅导一面 前端 面经 https://www.nowcoder.com/discuss/220884 
【前端】作业帮前端提前批面经 https://www.nowcoder.com/discuss/219441 
【前端】拼多多2019提前批前端一面面经 https://www.nowcoder.com/discuss/218895 
【前端】百度前端三面面经，求过！！刷人品 https://www.nowcoder.com/discuss/218405 
【前端】阿里钉钉前端开发一面凉经 https://www.nowcoder.com/discuss/218244 
【前端】实习中的阿里飞猪前端一面面经 https://www.nowcoder.com/discuss/218131 
【前端】拼多多前端提前批一面(电话远程笔试)被榨干了真的一滴都没有了 https://www.nowcoder.com/discuss/218488 
【前端】拼多多 前端 一面 2020提前批 https://www.nowcoder.com/discuss/218153 
【前端】阿里飞猪一面面经，（感觉要凉） https://www.nowcoder.com/discuss/217439 
【前端】依图前端面经 https://www.nowcoder.com/discuss/217773 
【前端】云从 提前批 前端一面 https://www.nowcoder.com/discuss/216966 
【前端】云从前端一面 https://www.nowcoder.com/discuss/216625 
【前端】阿里前端一面凉经 https://www.nowcoder.com/discuss/216281 
【前端】【前端】秋招面经 https://www.nowcoder.com/discuss/216244 
【前端】拼多多前端提前批一面面经秋招首战 https://www.nowcoder.com/discuss/215245 
【前端】2018届前端校招面经：百度、网易、搜狗与阿里 https://www.nowcoder.com/discuss/214323 
【前端】【前端】前端一面面经 https://www.nowcoder.com/discuss/214722 
【前端】【前端】毕业一年的阿里学长秋招经验分享 https://www.nowcoder.com/discuss/214273 
【前端】【前端】前端一面面经 https://www.nowcoder.com/discuss/214004 
【前端】寒冬中1年经验的社招前端面经 https://www.nowcoder.com/discuss/214799 
【前端】小米南京面 https://www.nowcoder.com/discuss/213879 
【前端】依图前端一面 https://www.nowcoder.com/discuss/214623 
【前端】百度某部门电话一面 https://www.nowcoder.com/discuss/213240 
【前端】百度三面和小米一面 https://www.nowcoder.com/discuss/213460 
【前端】小米南京面 https://www.nowcoder.com/discuss/213879 
【前端】字节跳动前端面经, 已拿意向书 https://www.nowcoder.com/discuss/213424 
【前端】字节跳动 深圳抖音 提前批前端 三面+HR面 已拿意向书 https://www.nowcoder.com/discuss/213863 
【前端】头条猿辅导瓜子老虎证券等前端面经 https://www.nowcoder.com/discuss/213693 
【前端】顺丰SP前端面经 https://www.nowcoder.com/discuss/212898 
【前端】顺丰科技 SP 前端 https://www.nowcoder.com/discuss/212847 
【前端】顺丰sp前端一面面经 https://www.nowcoder.com/discuss/212718 
【前端】字节跳动 提前批 凉经 https://www.nowcoder.com/discuss/212855 
【前端】记录一下自己的春招之路 https://www.nowcoder.com/discuss/212456 
【前端】抖音前端凉经 https://www.nowcoder.com/discuss/212448 
【前端】阿里淘宝FED前端 3面offer https://www.nowcoder.com/discuss/211609 
【前端】第一次在这里写面经，记一次水滴互助的面经吧 https://www.nowcoder.com/discuss/211911 
【前端】【前端】前端二面凉经 https://www.nowcoder.com/discuss/211772 
【前端】作业帮一面 https://www.nowcoder.com/discuss/211561 
【前端】多益前端提前批一面 https://www.nowcoder.com/discuss/211275 
【前端】【前端】前端一面 https://www.nowcoder.com/discuss/210806 
【前端】字节跳动提前批前端，已拿意向书~ https://www.nowcoder.com/discuss/210817 
【前端】作业帮前端凉面 https://www.nowcoder.com/discuss/211055 
【前端】面试体验：Facebook 篇 https://www.nowcoder.com/discuss/209681 
【前端】百度提前批前端面筋 https://www.nowcoder.com/discuss/210314 
【前端】百度云智能前端一面 https://www.nowcoder.com/discuss/210105 
【前端】【前端】 前端面经 https://www.nowcoder.com/discuss/210168 
【前端】寒武纪前端一面面经 https://www.nowcoder.com/discuss/209664 
【前端】字节跳动提前批前端一面凉经 https://www.nowcoder.com/discuss/210083 
【前端】oppo 提前批 前端 一面 https://www.nowcoder.com/discuss/206840 
【前端】oppo提前批 前端面经 https://www.nowcoder.com/discuss/207419 
【前端】百度前端秋招提前批一面面经 https://www.nowcoder.com/discuss/208841 
【前端】寒武纪一面面经 https://www.nowcoder.com/discuss/207803 
【前端】网易 前端 实习生 面经 一面 https://www.nowcoder.com/discuss/207836 
【前端】网易 前端 实习生 面经 三面 https://www.nowcoder.com/discuss/208783 
【前端】新浪微博前端面试 https://www.nowcoder.com/discuss/207879 
【前端】云智联前端（H5）实习面经 https://www.nowcoder.com/discuss/209398 
【前端】字节跳动 互娱 前端一面凉经 https://www.nowcoder.com/discuss/207553 
【前端】字节跳动ToB业务前端提前批一面凉面 https://www.nowcoder.com/discuss/207409 
【前端】字节跳动提前批前端三面面经 https://www.nowcoder.com/discuss/208384 
【前端】字节跳动提前批前端3面+HR面 面经 https://www.nowcoder.com/discuss/208931 
【前端】字节前端一面凉经 https://www.nowcoder.com/discuss/206457 
【前端】OPPO前端一面面经 https://www.nowcoder.com/discuss/205434 
【前端】字节跳动游戏平台 前端三面凉经 https://www.nowcoder.com/discuss/205511 
【前端】字节跳动提前批前端岗一面面经 https://www.nowcoder.com/discuss/205969 
【前端】字节跳动提前批前端岗一面面经 https://www.nowcoder.com/discuss/205969 
【前端】多益网络 前端面经 一面 https://www.nowcoder.com/discuss/204706 
【前端】壹钱包前端面试 https://www.nowcoder.com/discuss/203712 
【前端】字节跳动to B提前批前端一面（攒个人品） https://www.nowcoder.com/discuss/203874 
【前端】记一次字节跳动前端面试，四轮技术面通过，已拿offer https://www.nowcoder.com/discuss/204314 
【前端】字节跳动一面总结（前端技术岗） https://www.nowcoder.com/discuss/204829 

 游戏研发

 作者：菠萝哒
链接： https://www.nowcoder.com/discuss/90907 
来源：牛客网

 【游戏研发】[面经]网易互娱游戏研发工程师 https://www.nowcoder.com/discuss/97703 
【游戏研发】网易互娱初级游戏研发面经 https://www.nowcoder.com/discuss/97563 
【游戏研发】网易游戏研发工程师一面（8.23） https://www.nowcoder.com/discuss/97866 
【游戏研发】网易互娱(初级游戏研发) https://www.nowcoder.com/discuss/95256 
【游戏研发】网易游戏研发一面（电话）凉凉面经 https://www.nowcoder.com/discuss/94681 
【游戏研发】网易游戏研发1面 https://www.nowcoder.com/discuss/98181 
【游戏研发】网易互娱 初级游戏研发面筋 https://www.nowcoder.com/discuss/97989 
【游戏研发】网易游戏 互娱 游戏研发 一面挂经 回忆版： https://www.nowcoder.com/discuss/101395 

 算法

 【算法】蘑菇街 视觉算法一面（估计凉凉） https://www.nowcoder.com/discuss/230188 
【算法】招银信用卡中心AI面试： https://www.nowcoder.com/discuss/120676 
【算法】百度AIG一、二面面筋： https://www.nowcoder.com/discuss/98541 
【算法】美团2019校招AI算法提前批面经（已拿两部门offer） https://www.nowcoder.com/discuss/88679 
【算法】网易雷火AI游戏产品策划 面经： https://www.nowcoder.com/discuss/124169 
【算法】网易游戏AI研究员面经 https://www.nowcoder.com/discuss/98305 
【算法】网易互娱一二三面（AI工程师）： https://www.nowcoder.com/discuss/112298 
【算法】【算法】雷火&盘古&伏羲AI游戏研究员笔试题型面经分享： https://www.nowcoder.com/discuss/110706 
【算法】网易游戏AI研究员面经： https://www.nowcoder.com/discuss/98305 
【算法】平安人寿AI研发团队算法面经 https://www.nowcoder.com/discuss/92701 
【算法】热乎乎的招银成都面经： https://www.nowcoder.com/discuss/118423 
【算法】顺丰提前批人工智能岗技术面面经【算法】 https://www.nowcoder.com/discuss/92370 
【算法】vivo人工智能语音算法工程师面经： https://www.nowcoder.com/discuss/115049 
【算法】【算法】一面(技术面)面经 https://www.nowcoder.com/discuss/92260 
【算法】【算法】二面HR面面经 https://www.nowcoder.com/discuss/95197 
【算法】中国银联面试经历分享 https://www.nowcoder.com/discuss/91333 
【算法】银联武汉人工智能开发刚面完，热乎着 https://www.nowcoder.com/discuss/91879 
【算法】广州网易游戏-人工智能岗 https://www.nowcoder.com/discuss/97818 
【算法】网易互娱人工智能研究工程师一面 https://www.nowcoder.com/discuss/97689 
【算法】记一次难忘的面试，网易伏羲人工智能研究员5面面经 https://www.nowcoder.com/discuss/97427 
【算法】网易互娱人工智能研究工程师一面： https://www.nowcoder.com/discuss/97689 

 【算法】深信服机器学习算法工程师一面面经 https://www.nowcoder.com/discuss/87545 
【算法】百度-机器学习（已offer-手百推荐feed流）： https://www.nowcoder.com/discuss/121233 
【算法】百度算法岗（机器学习）酱油o.o： https://www.nowcoder.com/discuss/111758 
【算法】秋招面试--百度机器学习面经--更新至二面： https://www.nowcoder.com/discuss/111385 
【算法】秋招面试--百度机器学习一面： https://www.nowcoder.com/discuss/109158 
【算法】华为算法工程师（机器学习）面经：： https://www.nowcoder.com/discuss/121790 
【算法】华为-海外提前批-1技术，2综合，3boss-机器学习算法： https://www.nowcoder.com/discuss/95240 
【算法】华为-海外留学生提前比-机器学习算法 https://www.nowcoder.com/discuss/95240 
【算法】顺丰科技内推提前批人工智能与机器学习HR面，凉凉面经 https://www.nowcoder.com/discuss/88906 
【算法】顺丰科技机器学习 https://www.nowcoder.com/discuss/89042 
【算法】顺丰机器学习与人工智能工程师面经 https://www.nowcoder.com/discuss/91192 
【算法】[阿里蚂蚁]IOT实验室-机器学习算法-一面面经 https://www.nowcoder.com/discuss/92851 
【算法】阿里蚂蚁金服-机器学习算法-二面 https://www.nowcoder.com/discuss/93959 
【算法】阿里蚂蚁-机器学习算法工程师-三面 https://www.nowcoder.com/discuss/95225 
【算法】美团点评机器学习算法工程师面筋： https://www.nowcoder.com/discuss/111220 
【算法】实习面试--腾讯机器学习面经： https://www.nowcoder.com/discuss/111388 
【算法】小米机器学习算法工程师面经： https://www.nowcoder.com/discuss/128590 
【算法】vivo机器学习面经： https://www.nowcoder.com/discuss/113367 
【算法】vivo机器学习算法工程师视频一面面经 https://www.nowcoder.com/discuss/93329 
【算法】秋招第一次走完全程，vivo机器学习面经 https://www.nowcoder.com/discuss/93521 
【算法】菜鸟的面试：科大讯飞和作业帮 https://www.nowcoder.com/discuss/90245 
【算法】网易互娱面经数据挖掘/机器学习算法（10.9更新二面）： https://www.nowcoder.com/discuss/121338 
【算法】网易云音乐机器学习面经： https://www.nowcoder.com/discuss/99349 
【算法】360手机卫士-机器学习算法研发工程师 面经 https://www.nowcoder.com/discuss/97260 
【算法】虹软机器学习算法工程师初面面经【算法】 https://www.nowcoder.com/discuss/97154 
【算法】快手【算法】记录 ： https://www.nowcoder.com/discuss/102265 
【算法】快手机器学习算法工程师凉面（经）： https://www.nowcoder.com/discuss/101927 
【算法】快手【算法】记录 ： https://www.nowcoder.com/discuss/102265 
【算法】快手机器学习算法工程师凉面（经）： https://www.nowcoder.com/discuss/101927 
【算法】贝壳机器学习算法面经： https://www.nowcoder.com/discuss/124931 
【算法】【算法】贝壳找房三轮现场面（机器学习/数据挖掘岗）8.26： https://www.nowcoder.com/discuss/99190 
【算法】贝壳-机器学习面经： https://www.nowcoder.com/discuss/99153 
【算法】【算法】个人多厂面经分享： https://www.nowcoder.com/discuss/126457 
【算法】2018年机器学习岗面试干货(京东／华为／美图／招银)： https://www.nowcoder.com/discuss/108820 
【算法】2018春招秋招算法机器学习岗面经（阿里、腾讯、美团、携程）： https://www.nowcoder.com/discuss/106725 
【算法】机器学习/数据挖掘岗2019秋招总结： https://www.nowcoder.com/discuss/138721 
【算法】机器学习相关面经总结，可自查： https://www.nowcoder.com/discuss/102895 

 【算法】透心凉的百度-计算机视觉-一面面经 https://www.nowcoder.com/discuss/90591 
【算法】OPPO2019提前批计算机视觉算法开发工程师凉经： https://www.nowcoder.com/discuss/138577 
【算法】计算机视觉算法岗面经：两万字啊你确定不看看： https://www.nowcoder.com/discuss/128148 

 【算法】【算法】三面+【算法】二面 算法面经 https://www.nowcoder.com/discuss/231327 
【算法】华为面经 粤港澳地区优招 https://www.nowcoder.com/discuss/232187 
【算法】【算法】-希望能有二面 https://www.nowcoder.com/discuss/232192 
【算法】有赞算法面经 https://www.nowcoder.com/discuss/232844 
【算法】字节跳动，蘑菇街凉面 https://www.nowcoder.com/discuss/233198 
【算法】算法工程师面经+少量后端内容 2019年8月 BAT面经都有 https://www.nowcoder.com/discuss/231656 
【算法】2020地平线提前批算法面经（凉经） https://www.nowcoder.com/discuss/230211 
【算法】旷视2020校招-提前批-算法面经 https://www.nowcoder.com/discuss/229537 
【算法】猿辅导 计算机视觉算法岗一面面经（发面精，攒人品） https://www.nowcoder.com/discuss/229500 
【算法】作业帮NLP面试+腾讯NLP面试 https://www.nowcoder.com/discuss/230234 
【算法】百度搜索岗视频内容搜索算法一面二面面试记录 https://www.nowcoder.com/discuss/228452 
【算法】贝壳 算法凉经 https://www.nowcoder.com/discuss/228774 
【算法】阿里 机器学习算法岗 一面 https://www.nowcoder.com/discuss/228866 
【算法】欢聚时代二面整体GG，但貌似还有第三面 https://www.nowcoder.com/discuss/228449 
【算法】20届秋招美团算法凉经 https://www.nowcoder.com/discuss/228890 
【算法】星环科技NLP电话面试 https://www.nowcoder.com/discuss/228772 
【算法】2020提前批云从面经 https://www.nowcoder.com/discuss/229326 
【算法】计算机视觉面经之云从科技(offer) https://www.nowcoder.com/discuss/229031 
【算法】计算机视觉面经之tplink(offer) https://www.nowcoder.com/discuss/229028 
【算法】追一科技一二面凉凉经 算法 对抗样本 https://www.nowcoder.com/discuss/228765 
【算法】字节跳动-ailab-视觉算法面经 https://www.nowcoder.com/discuss/229358 
【算法】百度 深度学习平台部 凉经 https://www.nowcoder.com/discuss/227906 
【算法】美团机器学习一面面经 https://www.nowcoder.com/discuss/228061 
【算法】浦发面经-上海 https://www.nowcoder.com/discuss/227818 
【算法】【算法】商汤科技 - CV研究员 https://www.nowcoder.com/discuss/227554 
【算法】深信服一面面经 https://www.nowcoder.com/discuss/228067 
【算法】腾讯后台一面面(liang)经 https://www.nowcoder.com/discuss/227601 
【算法】网易云音乐面经？？？ https://www.nowcoder.com/discuss/227605 
【算法】网易游戏互娱，人工智能岗(Cv方向)一面面经 https://www.nowcoder.com/discuss/227344 
【算法】云从上海计算机视觉面经 https://www.nowcoder.com/discuss/228102 
【算法】云从科技-计算机视觉算法工程师-面经 https://www.nowcoder.com/discuss/227716 
【算法】追一科技 知识图谱算法岗 凉经 https://www.nowcoder.com/discuss/227904 
【算法】追一 NLP凉经 https://www.nowcoder.com/discuss/227752 
【算法】字节跳动算法岗一二面面经 https://www.nowcoder.com/discuss/227743 
【算法】作业帮NLP面经 https://www.nowcoder.com/discuss/227552 
【算法】地平线面经 https://www.nowcoder.com/discuss/226965 
【算法】拼多多 2020.08.17 算法岗面经 https://www.nowcoder.com/discuss/226906 
【算法】字节跳动算法工程师岗一二三面经 https://www.nowcoder.com/discuss/226960 
【算法】百度提前批机器学习算法二面面经 https://www.nowcoder.com/discuss/226065 
【算法】秋招上岸，回馈牛友一波面经 https://www.nowcoder.com/discuss/226526 
【算法】阿里一面 https://www.nowcoder.com/discuss/225972 
【算法】8月17 20:30 海康威视 算法一面凉经 34分钟 https://www.nowcoder.com/discuss/226298 
【算法】虎牙多媒体算法视频一面 https://www.nowcoder.com/discuss/225339 
【算法】拼多多图像算法凉经 https://www.nowcoder.com/discuss/225968 
【算法】2020深信服提前批面经（凉经） https://www.nowcoder.com/discuss/226440 
【算法】网易云机器学习一面36min https://www.nowcoder.com/discuss/225454 
【算法】依图科技-算法-计算机视觉【算法】 https://www.nowcoder.com/discuss/225571 
【算法】阿里优酷机器学习岗位一面面经，虽然希望不要凉，但是估计已凉 https://www.nowcoder.com/discuss/225737 
【算法】猿辅导二面面经 https://www.nowcoder.com/discuss/225338 
【算法】字节跳动算法二面凉经 https://www.nowcoder.com/discuss/226706 
【算法】字节二面凉经 https://www.nowcoder.com/discuss/226657 
【算法】字节跳动面试一面凉凉 https://www.nowcoder.com/discuss/226622 
【算法】字节跳动算法岗一面凉经 https://www.nowcoder.com/discuss/226619 
【算法】2020作业帮提前批面经（凉经） https://www.nowcoder.com/discuss/226439 
【算法】浙江大华凉凉凉面经，我不配学算法 https://www.nowcoder.com/discuss/224604 
【算法】华为，愉快的面经 https://www.nowcoder.com/discuss/224977 
【算法】PDD图像算法一面凉经 https://www.nowcoder.com/discuss/224360 
【算法】依图科技SP专场算法岗面经 https://www.nowcoder.com/discuss/224757 
【算法】阿里云机器学习岗一面面经 https://www.nowcoder.com/discuss/223799 
【算法】蘑菇街算法一面 https://www.nowcoder.com/discuss/222765 
【算法】拼多多一面 https://www.nowcoder.com/discuss/222772 
【算法】腾讯 一面 面经 https://www.nowcoder.com/discuss/222541 
【算法】依图 算法 二面凉经 https://www.nowcoder.com/discuss/222710 
【算法】猿辅导算法一面面经 https://www.nowcoder.com/discuss/222638 
【算法】【算法】京东零售 - 搜索与推荐平台部 - 算法岗 https://www.nowcoder.com/discuss/221822 
【算法】旷视提前批（算法研究员，3轮技面+HR面+终面） https://www.nowcoder.com/discuss/222073 
【算法】美团机器学习视频面试一面面经(提前批) https://www.nowcoder.com/discuss/222018 
【算法】阿里大文娱算法一面凉经 https://www.nowcoder.com/discuss/221185 
【算法】猿辅导算法岗一面凉经 https://www.nowcoder.com/discuss/221479 
【算法】shopee 一二面经 https://www.nowcoder.com/discuss/220443 
【算法】滴滴出行 提前批SP专场 算法工程师 三面面经 https://www.nowcoder.com/discuss/220938 
【算法】格力人工智能岗位提前批电话面试 https://www.nowcoder.com/discuss/219493 
【算法】京东 提前批 推荐与搜索平台 算法三面 面经 https://www.nowcoder.com/discuss/219957 
【算法】科大讯飞AI研究院内推一面凉经 https://www.nowcoder.com/discuss/219638 
【算法】旷视面经 https://www.nowcoder.com/discuss/221103 
【算法】旷视slam岗秋招面经 https://www.nowcoder.com/discuss/219601 
【算法】旷视提前批算法面经（3技术面+1交叉技术面+hr面+终面） https://www.nowcoder.com/discuss/220004 
【算法】拼多多算法一面面经 https://www.nowcoder.com/discuss/220011 
【算法】拼多多 提前批算法岗 南京现场面三轮面经！！！ https://www.nowcoder.com/discuss/220591 
【算法】拼多多学霸批 算法工程师面经 https://www.nowcoder.com/discuss/220587 
【算法】武汉拼多多算法工程师面经 https://www.nowcoder.com/discuss/220959 
【算法】拼多多武汉现场面经 https://www.nowcoder.com/discuss/220921 
【算法】腾讯一面来了。 https://www.nowcoder.com/discuss/220529 
【算法】【算法】深度学习算法工程师-秋招首面-过 https://www.nowcoder.com/discuss/221035 
【算法】头条提前批算法面经（2技术面+1leader面） https://www.nowcoder.com/discuss/220966 
【算法】百度推荐技术平台一面凉经 https://www.nowcoder.com/discuss/218722 
【算法】图森未来感知组计算机视觉算法面经 https://www.nowcoder.com/discuss/218937 
【算法】【算法】视觉算法二面和CTO面 https://www.nowcoder.com/discuss/218919 
【算法】头条南京后端上岸 https://www.nowcoder.com/discuss/218650 
【算法】顺丰 机器学习一面 https://www.nowcoder.com/discuss/218219 
【算法】【算法】成功面筋 https://www.nowcoder.com/discuss/218590 
【算法】作业帮 视觉算法工程师 面经 https://www.nowcoder.com/discuss/218362 
【算法】作业帮 机器学习算法面经 https://www.nowcoder.com/discuss/218216 
【算法】扔出面经求offer https://www.nowcoder.com/discuss/217402 
【算法】百度提前批NLP算法三面面经 https://www.nowcoder.com/discuss/217396 
【算法】欢聚时代-视频编解码算法工程师（一面） https://www.nowcoder.com/discuss/217204 
【算法】快手2020届提前批面经--推荐算法工程师 https://www.nowcoder.com/discuss/217487 
【算法】诺瓦软件开发SP专场凉经 https://www.nowcoder.com/discuss/217753 
【算法】拼多多学霸批NLP面经 https://www.nowcoder.com/discuss/217515 
【算法】追一科技机器学习算法工程师面经 https://www.nowcoder.com/discuss/217585 
【算法】收到头条意向书，分享一点面经 https://www.nowcoder.com/discuss/217326 
【算法】阿里 达摩院 cv 算法 面经 https://www.nowcoder.com/discuss/216797 
【算法】拼多多提前批算法工程师面经 https://www.nowcoder.com/discuss/216469 
【算法】字节跳动ailab面经 https://www.nowcoder.com/discuss/216993 
【算法】字节跳动 算法 已拿意向书 https://www.nowcoder.com/discuss/216672 
【算法】20校招AI算法岗（目前阿里+百度+京东offer）持续更新 https://www.nowcoder.com/discuss/216117 
【算法】寒武纪深度学习三面面经 https://www.nowcoder.com/discuss/216007 
【算法】欢聚时代机器学习算法工程师一面 https://www.nowcoder.com/discuss/215792 
【算法】京东广告部 一面面经 https://www.nowcoder.com/discuss/215667 
【算法】拼多多提前批算法工程师面经 https://www.nowcoder.com/discuss/216469 
【算法】[面经] 依图-旷视cv算法面经 https://www.nowcoder.com/discuss/215800 
【算法】阿里优酷算法工程师电话一面面经 https://www.nowcoder.com/discuss/215907 
【算法】云从机器学习面经 https://www.nowcoder.com/discuss/215651 
【算法】字节跳动算法岗提前批面经 https://www.nowcoder.com/discuss/215883 
【算法】字节跳动提前批ailab面经 https://www.nowcoder.com/discuss/215858 
【算法】作业帮CV一面 https://www.nowcoder.com/discuss/215679 
【算法】作业帮一面凉经 https://www.nowcoder.com/discuss/216131 
【算法】作业帮nlp面经 https://www.nowcoder.com/discuss/215140 
【算法】快手提前批 商业化部门三面 机器学习算法 广告算法 面经 https://www.nowcoder.com/discuss/213940 
【算法】腾讯CDG社交广告一面头条Data四面 面经 https://www.nowcoder.com/discuss/213960 
【算法】作业帮一面 https://www.nowcoder.com/discuss/214657 
【算法】北京智云视图算法工程师面试经历 https://www.nowcoder.com/discuss/213750 
【算法】顺丰科技视觉算法岗面经 https://www.nowcoder.com/discuss/213290 
【算法】顺丰视频面经——视觉算法 https://www.nowcoder.com/discuss/213283 
【算法】顺丰 运筹优化算法工程师 一面经 https://www.nowcoder.com/discuss/213263 
【算法】顺丰科技人工智能机器学习算法视频面经 https://www.nowcoder.com/discuss/213259 
【算法】顺丰科技人工智能机器学习算法视频面经 https://www.nowcoder.com/discuss/213820 
【算法】AI&机器学习突击面试【算法】 https://www.nowcoder.com/discuss/213816 
【算法】头条算法提前批三面面经 https://www.nowcoder.com/discuss/213671 
【算法】字节跳动AI lab 三面记录 https://www.nowcoder.com/discuss/213726 
【算法】百度 推荐技术平台 算法 凉经 https://www.nowcoder.com/discuss/212861 
【算法】字节跳动，二面问题 https://www.nowcoder.com/discuss/212922 
【算法】字节跳动，提前批一面问题 https://www.nowcoder.com/discuss/212913 
【算法】巨人网络-算法岗-一面 https://www.nowcoder.com/discuss/212554 
【算法】还愿，收到字节跳动提前批算法岗offer了~ https://www.nowcoder.com/discuss/212439 
【算法】回馈牛客，字节算法三面许愿求offer https://www.nowcoder.com/discuss/211763 
【算法】深夜-作业帮NLP凉面 https://www.nowcoder.com/discuss/211426 
【算法】作业帮_北京_算法岗_sp https://www.nowcoder.com/discuss/212220 
【算法】百度凤巢广告算法提前批三面面经 https://www.nowcoder.com/discuss/211954 
【算法】图森_北京_感知算法研究员_技术面 https://www.nowcoder.com/discuss/211262 
【算法】中兴_南京_计算机视觉算法_技术面 https://www.nowcoder.com/discuss/211261 
【算法】追一科技_深圳_视觉算法工程师面经 https://www.nowcoder.com/discuss/211258 
【算法】深圳抖音图像图形算法三面面经(已获意向书) https://www.nowcoder.com/discuss/211382 
【算法】字节AiLab CV 面经，感觉凉透了 https://www.nowcoder.com/discuss/211352 
【算法】字节跳动 AILab 二面记录 https://www.nowcoder.com/discuss/211174 
【算法】作业帮 机器学习算法 面经 https://www.nowcoder.com/discuss/211326 
【算法】乐鑫通信算法一面hr面面经 https://www.nowcoder.com/discuss/210961 
【算法】字节跳动提前批后端，刚拿意向书，分享一下面经 https://www.nowcoder.com/discuss/210872 
【算法】字节跳动计算机视觉算法面经 https://www.nowcoder.com/discuss/210829 
【算法】百度提前批算法岗四小时面试记录 https://www.nowcoder.com/discuss/210313 
【算法】百度nlp一面 https://www.nowcoder.com/discuss/210299 
【算法】阿里文娱提前批 视觉算法岗 https://www.nowcoder.com/discuss/209671 
【算法】【算法】计算机视觉一面面经 https://www.nowcoder.com/discuss/210056 
【算法】0723快手 Openday社区科学部 算法工程师面经 https://www.nowcoder.com/discuss/210333 
【算法】旷视算法研究员一面凉经 https://www.nowcoder.com/discuss/210569 
【算法】商汤20校招CV算法研究员面经【算法】 https://www.nowcoder.com/discuss/209857 
【算法】依图一面 https://www.nowcoder.com/discuss/210550 
【算法】【算法】视觉算法一面凉经 https://www.nowcoder.com/discuss/210063 
【算法】[字节跳动/头条] 算法提前批三轮面经，前来回馈广大牛油们~ https://www.nowcoder.com/discuss/210036 
【算法】字节跳动2020届提前批 AI Lab cv 三面视频面 https://www.nowcoder.com/discuss/210508 
【算法】OPPO西安 机器学习凉凉经 https://www.nowcoder.com/discuss/206792 
【算法】Dell EMC数据保护部门实习生面试 https://www.nowcoder.com/discuss/207579 
【算法】多益面试（人工智能） https://www.nowcoder.com/discuss/208550 
【算法】多益算法奇经 https://www.nowcoder.com/discuss/209251 
【算法】阿里大文娱 机器学习面经 https://www.nowcoder.com/discuss/209171 
【算法】阿里一面 https://www.nowcoder.com/discuss/209000 
【算法】阿里算法面经 https://www.nowcoder.com/discuss/209306 
【算法】2-图森未来@Beijing(7276845) 凉经-攒人品 https://www.nowcoder.com/discuss/208586 
【算法】字节跳动 图像图像一面面经 https://www.nowcoder.com/discuss/207221 
【算法】字节跳动算法岗三面面经 https://www.nowcoder.com/discuss/207105 
【算法】字节跳动提前批算法工程师面经 https://www.nowcoder.com/discuss/207092 
【算法】OPPO视频面（NLP算法），凉经 https://www.nowcoder.com/discuss/206740 
【算法】头条抖音互娱-图形图像一二三面 https://www.nowcoder.com/discuss/207369 
【算法】字节跳动头条研发算法一面 https://www.nowcoder.com/discuss/207317 
【算法】算法岗提前批凉经【算法】 https://www.nowcoder.com/discuss/207287 
【算法】字节跳动一面凉经！ https://www.nowcoder.com/discuss/207749 
【算法】头条 机器学习算法一面 https://www.nowcoder.com/discuss/207712 
【算法】头条AILab一面面经 https://www.nowcoder.com/discuss/208289 
【算法】头条后台二面面经 https://www.nowcoder.com/discuss/208881 
【算法】字节跳动算法工程师面经+个人疑问 https://www.nowcoder.com/discuss/209478 
【算法】作业帮一面，二面。估计二面已凉 https://www.nowcoder.com/discuss/208777 
【算法】两次作业帮凉经 https://www.nowcoder.com/discuss/208481 
【算法】作业帮nlp面经 https://www.nowcoder.com/discuss/208986 
【算法】京东提前批算法工程师电面面经 https://www.nowcoder.com/discuss/206186 
【算法】字节跳动 AILab提前批算法工程师面经(已收到offer) https://www.nowcoder.com/discuss/206226 
【算法】字节跳动CV算法一面凉经 https://www.nowcoder.com/discuss/206593 
【算法】今日头条 多媒体开发(视频架构)面经 https://www.nowcoder.com/discuss/206578 
【算法】oppo提前批 机器学习 一面凉经 https://www.nowcoder.com/discuss/205699 
【算法】oppo提前批机器学习岗面经 https://www.nowcoder.com/discuss/205955 
【算法】成都oppo机器学习算法工程师面经 https://www.nowcoder.com/discuss/205841 
【算法】OPPO 视觉算法一二三面 https://www.nowcoder.com/discuss/205472 
【算法】OPPO--提前批--机器学习--面经 https://www.nowcoder.com/discuss/205467 
【算法】多益网络-人工智能岗面试 https://www.nowcoder.com/discuss/205848 
【算法】【算法】趁热分享 https://www.nowcoder.com/discuss/205964 
【算法】头条图形图像一面面筋 https://www.nowcoder.com/discuss/205864 
【算法】字节跳动ai lab cv算法面经（我来反馈攒人品了） https://www.nowcoder.com/discuss/205843 
【算法】字节跳动 Data 算法工程师 广告/AML 提前批3面面经 https://www.nowcoder.com/discuss/205736 
【算法】菜鸡总结暑期实习求职经历（附部分面经 https://www.nowcoder.com/discuss/205718 
【算法】说说自己的字节跳动EE部门一面凉经，以及面试官给我的三连击！ https://www.nowcoder.com/discuss/206106 
【算法】腾讯光子技术中心 日常实习CV方向面筋 https://www.nowcoder.com/discuss/206089 
【算法】头条算法最新凉经 https://www.nowcoder.com/discuss/206065 
【算法】【算法】趁热分享 https://www.nowcoder.com/discuss/205964 
【算法】oppo提前批机器学习岗面经 https://www.nowcoder.com/discuss/205955 
【算法】2020届视觉算法菜鸡的秋招求职之路(面经，持续更新) https://www.nowcoder.com/discuss/205231 
【算法】2019.7.5百度生态搜索质量部 提前批 面试题回忆 https://www.nowcoder.com/discuss/203473 
【算法】百度搜索部提前批一面 https://www.nowcoder.com/discuss/204597 
【算法】多益网络面经 https://www.nowcoder.com/discuss/204628 
【算法】多益面经（人工智能） https://www.nowcoder.com/discuss/205251 
【算法】多益网络，2019年人工智能与大数据研发岗位面试 https://www.nowcoder.com/discuss/204993 
【算法】阿里NLP面经 https://www.nowcoder.com/discuss/205021 
【算法】已拿提前批offer 映客笔经加面经 https://www.nowcoder.com/discuss/204240 
【算法】中兴通讯2020届校园招聘提前批面经（算法工程师） https://www.nowcoder.com/discuss/203584 
【算法】记一次十分惨烈的头条一面 https://www.nowcoder.com/discuss/203454 
【算法】头条机器学习算法岗面试记录 https://www.nowcoder.com/discuss/205260 

 机器学习

 【机器学习】阿里机器学习一面面经 https://www.nowcoder.com/discuss/226711 
【机器学习】美团机器学习一面面经 https://www.nowcoder.com/discuss/228061 
【机器学习】百度提前批机器学习算法二面面经 https://www.nowcoder.com/discuss/226065 
【机器学习】云从机器学习面经 https://www.nowcoder.com/discuss/215651 
【机器学习】欢聚时代机器学习算法工程师一面 https://www.nowcoder.com/discuss/215792 

 【机器学习】追一科技机器学习算法工程师面经 https://www.nowcoder.com/discuss/217585 
【机器学习】网易云机器学习一面36min https://www.nowcoder.com/discuss/225454 
【机器学习】阿里优酷机器学习岗位一面面经，虽然希望不要凉，但是估计已凉
【机器学习】阿里云机器学习岗一面面经 https://www.nowcoder.com/discuss/223799 
【机器学习】美团机器学习视频面试一面面经(提前批) https://www.nowcoder.com/discuss/222018 
【机器学习】顺丰 机器学习一面 https://www.nowcoder.com/discuss/218219 
【机器学习】作业帮 机器学习算法面经 https://www.nowcoder.com/discuss/218216 
【机器学习】快手提前批 商业化部门三面 机器学习算法 广告算法 面经 https://www.nowcoder.com/discuss/213940 

 【机器学习】顺丰科技人工智能机器学习算法视频面经 https://www.nowcoder.com/discuss/213259 
【机器学习】顺丰科技人工智能机器学习算法视频面经 https://www.nowcoder.com/discuss/213820 
【机器学习】AI&机器学习突击面试【机器学习】 https://www.nowcoder.com/discuss/213816 
【机器学习】作业帮 机器学习算法 面经 https://www.nowcoder.com/discuss/211326 

 【机器学习】OPPO西安 机器学习凉凉经 https://www.nowcoder.com/discuss/206792 
【机器学习】头条 机器学习算法一面 https://www.nowcoder.com/discuss/207712 
【机器学习】顺丰科技内推提前批人工智能与机器学习HR面，凉凉面经 https://www.nowcoder.com/discuss/88906 
【机器学习】顺丰科技机器学习 https://www.nowcoder.com/discuss/89042 
【机器学习】顺丰 机器学习与人工智能工程师 面经 https://www.nowcoder.com/discuss/91192 
【机器学习】oppo提前批 机器学习 一面凉经 https://www.nowcoder.com/discuss/205699 
【机器学习】oppo提前批机器学习岗面经 https://www.nowcoder.com/discuss/205955 
【机器学习】成都oppo机器学习算法工程师面经 https://www.nowcoder.com/discuss/205841 
【机器学习】OPPO 视觉算法一二三面 https://www.nowcoder.com/discuss/205472 
【机器学习】OPPO--提前批--机器学习--面经 https://www.nowcoder.com/discuss/205467 
【机器学习】深信服机器学习算法工程师一面面经 https://www.nowcoder.com/discuss/87545 
【机器学习】百度-机器学习（已offer-手百推荐feed流）： https://www.nowcoder.com/discuss/121233 
【机器学习】百度算法岗（机器学习）酱油o.o： https://www.nowcoder.com/discuss/111758 
【机器学习】秋招面试--百度机器学习面经--更新至二面： https://www.nowcoder.com/discuss/111385 
【机器学习】秋招面试--百度机器学习一面： https://www.nowcoder.com/discuss/109158 
【机器学习】华为算法工程师（机器学习）面经：： https://www.nowcoder.com/discuss/121790 
【机器学习】华为-海外提前批-1技术，2综合，3boss-机器学习算法： https://www.nowcoder.com/discuss/95240 
【机器学习】华为-海外留学生提前比-机器学习算法 https://www.nowcoder.com/discuss/95240 
【机器学习】顺丰科技内推提前批人工智能与机器学习HR面，凉凉面经 https://www.nowcoder.com/discuss/88906 
【机器学习】顺丰科技机器学习 https://www.nowcoder.com/discuss/89042 
【机器学习】顺丰机器学习与人工智能工程师面经 https://www.nowcoder.com/discuss/91192 
【机器学习】[阿里蚂蚁]IOT实验室-机器学习算法-一面面经 https://www.nowcoder.com/discuss/92851 
【机器学习】阿里蚂蚁金服-机器学习算法-二面 https://www.nowcoder.com/discuss/93959 
【机器学习】阿里蚂蚁-机器学习算法工程师-三面 https://www.nowcoder.com/discuss/95225 
【机器学习】美团点评机器学习算法工程师面筋： https://www.nowcoder.com/discuss/111220 
【机器学习】实习面试--腾讯机器学习面经： https://www.nowcoder.com/discuss/111388 
【机器学习】小米机器学习算法工程师面经： https://www.nowcoder.com/discuss/128590 
【机器学习】vivo机器学习面经： https://www.nowcoder.com/discuss/113367 
【机器学习】vivo机器学习算法工程师视频一面面经 https://www.nowcoder.com/discuss/93329 
【机器学习】秋招第一次走完全程，vivo机器学习面经 https://www.nowcoder.com/discuss/93521 
【机器学习】菜鸟的面试：科大讯飞和作业帮 https://www.nowcoder.com/discuss/90245 
【机器学习】网易互娱面经数据挖掘/机器学习算法（10.9更新二面）： https://www.nowcoder.com/discuss/121338 
【机器学习】网易云音乐机器学习面经： https://www.nowcoder.com/discuss/99349 
【机器学习】360手机卫士-机器学习算法研发工程师 面经 https://www.nowcoder.com/discuss/97260 
【机器学习】虹软机器学习算法工程师初面面经【机器学习】 https://www.nowcoder.com/discuss/97154 
【机器学习】快手【机器学习】记录： https://www.nowcoder.com/discuss/102265 
【机器学习】快手机器学习算法工程师凉面（经）： https://www.nowcoder.com/discuss/101927 
【机器学习】快手【机器学习】记录： https://www.nowcoder.com/discuss/102265 
【机器学习】快手机器学习算法工程师凉面（经）： https://www.nowcoder.com/discuss/101927 
【机器学习】贝壳机器学习算法面经： https://www.nowcoder.com/discuss/124931 
【机器学习】【机器学习】贝壳找房三轮现场面（机器学习/数据挖掘岗）8.26： https://www.nowcoder.com/discuss/99190 
【机器学习】贝壳-机器学习面经： https://www.nowcoder.com/discuss/99153 
【机器学习】个人多厂面经分享： https://www.nowcoder.com/discuss/126457 
【机器学习】2018年机器学习岗面试干货(京东／华为／美图／招银)： https://www.nowcoder.com/discuss/108820 
【机器学习】2018春招秋招算法机器学习岗面经（阿里、腾讯、美团、携程）： https://www.nowcoder.com/discuss/106725 
【机器学习】机器学习/数据挖掘岗2019秋招总结： https://www.nowcoder.com/discuss/138721 
【机器学习】机器学习相关面经总结，可自查： https://www.nowcoder.com/discuss/102895 

 架构

 【架构】阿里云高可用架构 C++岗一面 https://www.nowcoder.com/discuss/212938 
【架构】字节跳动提前批后端开发（视频架构）一二三面 https://www.nowcoder.com/discuss/209548 

 【架构】字节跳动系统架构组实习生一二面凉经 https://www.nowcoder.com/discuss/203548 
【架构】字节提前批后端开发-视频架构方向面经 https://www.nowcoder.com/discuss/207891 
【架构】字节跳动-视频架构-后端开发（视频一面） https://www.nowcoder.com/discuss/208773 

 【架构】百度 度秘事业部 架构一面 https://www.nowcoder.com/discuss/228747 
【架构】阿里高可用架构一面面经 https://www.nowcoder.com/discuss/208150 
【架构】百度推荐架构部 秋招提前批 3面面经 https://www.nowcoder.com/discuss/209462 
【架构】亚马逊AWS解决方案架构师实习生三面（终面）面经 https://www.nowcoder.com/discuss/204431 
【架构】香侬科技基础架构实习生面经 https://www.nowcoder.com/discuss/204991 
【架构】顺丰科技基础架构部秋招一面面经 https://www.nowcoder.com/discuss/88146 
【架构】2019网易雷火虚拟世界架构师面经，杭州： https://www.nowcoder.com/discuss/126845 
【架构】顺丰科技基础架构部秋招一面面经 https://www.nowcoder.com/discuss/88146 

 嵌入式

 【嵌入式】网易有道 嵌入式面经 https://www.nowcoder.com/discuss/225345 
【嵌入式】云从嵌入式一面 https://www.nowcoder.com/discuss/225895 
【嵌入式】云从嵌入式一面 https://www.nowcoder.com/discuss/217311 
【嵌入式】阿里-自动化嵌入式-一面已挂 https://www.nowcoder.com/discuss/92892 
【嵌入式】CVTE嵌入式凉面经： https://www.nowcoder.com/discuss/109591 
【嵌入式】CVTE嵌入式一面面经 https://www.nowcoder.com/discuss/90250 
【嵌入式】回馈牛客网，CVTE秋招嵌入式面经： https://www.nowcoder.com/discuss/139261 
【嵌入式】阿里-自动化嵌入式-一面已挂 https://www.nowcoder.com/discuss/92892 
【嵌入式】CVTE嵌入式凉面经： https://www.nowcoder.com/discuss/109591 

 【嵌入式】CVTE嵌入式一面面经 https://www.nowcoder.com/discuss/90250 
【嵌入式】回馈牛客网，CVTE秋招嵌入式面经： https://www.nowcoder.com/discuss/139261 

 数据分析

 【数据分析】顺丰科技 大数据分析与挖掘一面凉经 https://www.nowcoder.com/discuss/218228 
【数据分析】京东数据分析二面： https://www.nowcoder.com/discuss/120618 
【数据分析】58数据分析面经，0offer攒人品！！！！： https://www.nowcoder.com/discuss/121791 
【数据分析】终于收到意向书，回报大家一份拼多多数据分析师的面经： https://www.nowcoder.com/discuss/121091 

 【数据分析】网易数据分析面经： https://www.nowcoder.com/discuss/121329 
【数据分析】网易考拉数据分析面经： https://www.nowcoder.com/discuss/119724 
【数据分析】网易数据分析+算法面经： https://www.nowcoder.com/discuss/118891 
【数据分析】网易互联网邮件事业部数据分析面经： https://www.nowcoder.com/discuss/114797 
【数据分析】网易考拉数据分析三面面筋： https://www.nowcoder.com/discuss/98892 
【数据分析】迟到的头条数据分析凉面： https://www.nowcoder.com/discuss/99812 
【数据分析】神策-数据分析&WPS-产品-一面凉经&网易游戏-项目管理： https://www.nowcoder.com/discuss/123125 
【数据分析】微众（数挖）+京东+拼多多数据分析面经： https://www.nowcoder.com/discuss/122060 
【数据分析】2019数据分析求职经验贴【数据分析】： https://www.nowcoder.com/discuss/123711 
【数据分析】数据分析秋招总结：虽然offer少，但是有我就很开心了： https://www.nowcoder.com/discuss/122992 

 【数据分析】头条数据分析一面凉经： https://www.nowcoder.com/discuss/110037 
【数据分析】8.26头条/字节跳动数据分析面试面经： https://www.nowcoder.com/discuss/105828 
【数据分析】头条/字节跳动数据分析岗面经~： https://www.nowcoder.com/discuss/144255 
【数据分析】今日头条数据分析面经： https://www.nowcoder.com/discuss/144841 
【数据分析】宇宙条数据分析实习面经： https://www.nowcoder.com/discuss/143595 
【数据分析】今日头条/字节跳动 数据分析岗情况： https://www.nowcoder.com/discuss/128911 

 【数据分析】银联面经： https://www.nowcoder.com/discuss/102382 
【数据分析】西安 中国银联数据分析岗2019内推面试 https://www.nowcoder.com/discuss/92555 

 【数据分析】10.8杭州vivo数据分析经理面经： https://www.nowcoder.com/discuss/124269 
【数据分析】10.8vivo数据分析经理面经： https://www.nowcoder.com/discuss/124157 
【数据分析】【数据分析】VIVO面经 互联网数据分析经理： https://www.nowcoder.com/discuss/111542 

 【数据分析】京东数据分析二面： https://www.nowcoder.com/discuss/120618 
【数据分析】58数据分析面经，0offer攒人品！！！！： https://www.nowcoder.com/discuss/121791 
【数据分析】10.8杭州vivo数据分析经理面经： https://www.nowcoder.com/discuss/124269 
【数据分析】10.8vivo数据分析经理面经： https://www.nowcoder.com/discuss/124157 
【数据分析】【数据分析】VIVO面经 互联网数据分析经理： https://www.nowcoder.com/discuss/111542 
【数据分析】银联面经： https://www.nowcoder.com/discuss/102382 
【数据分析】西安中国银联数据分析岗2019内推面试 https://www.nowcoder.com/discuss/92555 
【数据分析】终于收到意向书，回报大家一份拼多多数据分析师的面经： https://www.nowcoder.com/discuss/121091 
【数据分析】网易数据分析面经： https://www.nowcoder.com/discuss/121329 
【数据分析】网易考拉数据分析面经： https://www.nowcoder.com/discuss/119724 
【数据分析】网易数据分析+算法面经： https://www.nowcoder.com/discuss/118891 
【数据分析】网易互联网邮件事业部数据分析面经： https://www.nowcoder.com/discuss/114797 
【数据分析】网易考拉数据分析三面面筋： https://www.nowcoder.com/discuss/98892 
【数据分析】今日头条/字节跳动 数据分析岗情况： https://www.nowcoder.com/discuss/128911 
【数据分析】头条数据分析一面凉经： https://www.nowcoder.com/discuss/110037 
【数据分析】8.26头条/字节跳动数据分析面试面经： https://www.nowcoder.com/discuss/105828 
【数据分析】迟到的头条数据分析凉面： https://www.nowcoder.com/discuss/99812 
【数据分析】欢聚YY，数据分析一面凉筋： https://www.nowcoder.com/discuss/119838 
【数据分析】珍爱网数据分析一面面经： https://www.nowcoder.com/discuss/99606 
【数据分析】【数据分析】网易、拼多多、58、vivo笔经面经 ： https://www.nowcoder.com/discuss/128127 
【数据分析】神策-数据分析&WPS-产品-一面凉经&网易游戏-项目管理： https://www.nowcoder.com/discuss/123125 
【数据分析】微众（数挖）+京东+拼多多数据分析面经： https://www.nowcoder.com/discuss/122060 
【数据分析】2019数据分析求职经验贴【数据分析】： https://www.nowcoder.com/discuss/123711 
【数据分析】数据分析秋招总结：虽然offer少，但是有我就很开心了： https://www.nowcoder.com/discuss/122992 
【数据分析】实名感谢杨超越小姐姐哈哈哈 ： https://www.nowcoder.com/discuss/113279 
【数据分析】秋招面试总结（数据分析岗）： https://www.nowcoder.com/discuss/101014 
【数据分析】人力数据分析岗一面二面三面hr面分享： https://www.nowcoder.com/discuss/142169 
【数据分析】你是数据分析吗？我也是！不过我们可能不是同一岗。。。： https://www.nowcoder.com/discuss/127928 

 【数据分析】字节跳动 数据分析 一面 https://www.nowcoder.com/discuss/230722 
【数据分析】拼多多数据分析师一二面面经，交流 https://www.nowcoder.com/discuss/228882 
【数据分析】拼多多：一二面 https://www.nowcoder.com/discuss/228722 
【数据分析】拼多多学霸批数据分析面经 https://www.nowcoder.com/discuss/226925 
【数据分析】阿里一面总结 https://www.nowcoder.com/discuss/226834 
【数据分析】拼多多数据分析 817北京现场面 面经分享 https://www.nowcoder.com/discuss/226713 
【数据分析】网易考拉数据分析一面面经 https://www.nowcoder.com/discuss/225388 
【数据分析】网易考拉数据分析一面面经 https://www.nowcoder.com/discuss/225348 
【数据分析】猿辅导数据分析一面凉经（我太难了） https://www.nowcoder.com/discuss/226712 
【数据分析】滴滴出行数据分析面经 https://www.nowcoder.com/discuss/224138 
【数据分析】顺丰科技大数据分析与挖掘 https://www.nowcoder.com/discuss/224765 
【数据分析】拼多多数据分析师一面面经 https://www.nowcoder.com/discuss/223794 
【数据分析】拼多多学霸批数据分析师一面凉经 https://www.nowcoder.com/discuss/223753 
【数据分析】拼多多数据分析远程一面 https://www.nowcoder.com/discuss/223641 
【数据分析】近期面经（数据分析&挖掘方向） https://www.nowcoder.com/discuss/222592 
【数据分析】拼多多 数据分析 远程二面 https://www.nowcoder.com/discuss/223196 
【数据分析】拼多多数分远程一面 https://www.nowcoder.com/discuss/222962 
【数据分析】凉透了的拼多多数据分析二面（牛客再见，回家种田） https://www.nowcoder.com/discuss/222900 
【数据分析】拼多多数分二面 https://www.nowcoder.com/discuss/222557 
【数据分析】8.11拼多多数据分析现场面 https://www.nowcoder.com/discuss/221285 
【数据分析】拼多多 数据分析提前批一面 https://www.nowcoder.com/discuss/219629 
【数据分析】拼多多 数据分析 远程一面 https://www.nowcoder.com/discuss/219555 
【数据分析】拼多多数分远程一面 https://www.nowcoder.com/discuss/219494 
【数据分析】拼多多数据分析一面凉经 https://www.nowcoder.com/discuss/219359 
【数据分析】拼多多数分一面远程 https://www.nowcoder.com/discuss/218750 
【数据分析】字节跳动数据分析一面凉经... https://www.nowcoder.com/discuss/219080 
【数据分析】字节跳动秋招 数据分析 一面 https://www.nowcoder.com/discuss/219004 
【数据分析】阿里巴巴 数据分析 简历评估面 面经 https://www.nowcoder.com/discuss/215854 
【数据分析】拼多多学霸批数据分析笔经 https://www.nowcoder.com/discuss/212449 
【数据分析】字节跳动数分凉面 https://www.nowcoder.com/discuss/212382 
【数据分析】字节跳动 数据分析 产品方向 日常实习 面经 https://www.nowcoder.com/discuss/207493 
【数据分析】头条一面二面Data后端（一首凉凉送给自己） https://www.nowcoder.com/discuss/205742 
【数据分析】我的面试经历-数据分析实习生 https://www.nowcoder.com/discuss/204273 

 数据挖掘

 【数据挖掘】顺丰科技数据挖掘岗20分钟第一面 https://www.nowcoder.com/discuss/214042 

 【数据挖掘】网易互娱面经数据挖掘/机器学习算法（10.9更新二面）： https://www.nowcoder.com/discuss/121338 
【数据挖掘】贝壳找房三轮现场面（机器学习/数据挖掘岗）8.26： https://www.nowcoder.com/discuss/99190 

 【数据挖掘】机器学习/数据挖掘岗2019秋招总结： https://www.nowcoder.com/discuss/138721 
【数据挖掘】京东数据挖掘岗一面 https://www.nowcoder.com/discuss/87973 
【数据挖掘】CVTE研究院数据挖掘岗三轮面经： https://www.nowcoder.com/discuss/91678 
【数据挖掘】顺丰科技一面面经（内推--大数据挖掘与分析岗） https://www.nowcoder.com/discuss/88818 
【数据挖掘】说好的面经来啦！！ 数据挖掘/大数据开发： https://www.nowcoder.com/discuss/127104 
【数据挖掘】 京东数据挖掘岗一面 https://www.nowcoder.com/discuss/87973 
【数据挖掘】 顺丰科技一面面经（内推--大数据挖掘与分析岗） https://www.nowcoder.com/discuss/88818 
【数据挖掘】顺丰数据挖掘工程师提前批一面面经 https://www.nowcoder.com/discuss/88755 
【数据挖掘】顺丰hr面 https://www.nowcoder.com/discuss/90500 
【数据挖掘】CVTE研究院数据挖掘岗三轮面经： https://www.nowcoder.com/discuss/91678 
【数据挖掘】网易数据挖掘工程师　面经： https://www.nowcoder.com/discuss/125565 
【数据挖掘】网易互娱面经数据挖掘/机器学习算法（10.9更新二面）： https://www.nowcoder.com/discuss/121338 
【数据挖掘】回馈牛客，头条日常实习-数据挖掘offer（附一年面经）： https://www.nowcoder.com/discuss/142996 
【数据挖掘】 珍爱网数据挖掘一面面经 https://www.nowcoder.com/discuss/98294 

 非技术

 产品

 【产品】ihandy产品sp专场一面凉经 https://www.nowcoder.com/discuss/231571 
【产品】#贝壳提前批#产品凉经，，我好恨呐 https://www.nowcoder.com/discuss/232911 
【产品】美团助理产品经理岗一面+二面面经～～～ https://www.nowcoder.com/discuss/230551 
【产品】顺丰科技产品经理一二三面面经合集 https://www.nowcoder.com/discuss/231216 
【产品】字节跳动商业产品运营经理三面面经 https://www.nowcoder.com/discuss/232127 
【产品】20届秋招|斗鱼直播|0820产品经理岗笔试复盘 https://www.nowcoder.com/discuss/230034 
【产品】【产品】AI策略产品经理 https://www.nowcoder.com/discuss/229391 
【产品】字节跳动b端产品经理面经 https://www.nowcoder.com/discuss/228910 
【产品】贝壳找房产品面经（三面） https://www.nowcoder.com/discuss/226822 
【产品】字节跳动产品运营面经（已完成一二三面 许愿意向书） https://www.nowcoder.com/discuss/226872 
【产品】贝壳产品一面面（凉）经 https://www.nowcoder.com/discuss/226034 
【产品】阿里饿了么本地生活-电话初面-交流分享 https://www.nowcoder.com/discuss/226320 
【产品】流利说产品一面 https://www.nowcoder.com/discuss/226146 
【产品】【产品】深信服一面（凉～） https://www.nowcoder.com/discuss/226210 
【产品】顺丰SP产品三面 https://www.nowcoder.com/discuss/225882 
【产品】19.8.17，搜狐产品面试 https://www.nowcoder.com/discuss/226661 
【产品】Shopee产品(新加坡base)一面面经 https://www.nowcoder.com/discuss/224361 
【产品】秋招产品面经 https://www.nowcoder.com/discuss/224811 
【产品】流利说产品电面一面面经 https://www.nowcoder.com/discuss/224409 
【产品】美团上海POI数据中心产品一面，电话面 https://www.nowcoder.com/discuss/224365 
【产品】深信服（售前产品经理）一面挂凉经 https://www.nowcoder.com/discuss/223649 
【产品】顺丰sp产品二面总结 https://www.nowcoder.com/discuss/221428 
【产品】阿里用户型产品经理暑期实习-八面面经 https://www.nowcoder.com/discuss/220767 
【产品】面完了小鹏汽车产品，简单整理下 https://www.nowcoder.com/discuss/218811 
【产品】顺丰sp产品一面总结 https://www.nowcoder.com/discuss/217934 
【产品】bigo 产品实习面经 https://www.nowcoder.com/discuss/211421 
【产品】华为产品行销校招面经（2019.1） https://www.nowcoder.com/discuss/211428 
【产品】2020届京东管培生产品方向群面复盘 https://www.nowcoder.com/discuss/212154 
【产品】0704映客直播秋招提前批产品岗笔试复盘 https://www.nowcoder.com/discuss/210691 
【产品】新浪微博产品实习生面试复盘（一面加二面，已拿到offer） https://www.nowcoder.com/discuss/208735 
【产品】多益网络校招（互联网产品策划助理） https://www.nowcoder.com/discuss/205750 
【产品】锐捷售前产品经理一面面经： https://www.nowcoder.com/discuss/112199 
【产品】多益网络一面面经： https://www.nowcoder.com/discuss/108614 
【产品】多益网络一面-互联网产品研发工程师： https://www.nowcoder.com/discuss/108556 
【产品】多益网络产品策划助理面经，攒人品： https://www.nowcoder.com/discuss/97933 
【产品】发个面经攒人品-多益互联网开发工程师： https://www.nowcoder.com/discuss/97742 
【产品】多益网络 提前批视频面 https://www.nowcoder.com/discuss/85304 
【产品】多益网络提前批产品策划面经 https://www.nowcoder.com/discuss/85248 
【产品】多益网络秋招提前批互联网产品助理岗二面主管面面经 https://www.nowcoder.com/discuss/85125 
【产品】多益网络2019提前批面经：产品岗 https://www.nowcoder.com/discuss/88379 
【产品】多益网络 产品策划 专业面面经 https://www.nowcoder.com/discuss/96151 
【产品】多益网络面经 https://www.nowcoder.com/discuss/96643 
【产品】多益网络产品岗一面面经 https://www.nowcoder.com/discuss/96490 
【产品】多益 产品策划助理 二面 https://www.nowcoder.com/discuss/96764 
【产品】多益-互联网产品研发工程师（凉经） https://www.nowcoder.com/discuss/97158 
【产品】 多益产品二面+360一面 https://www.nowcoder.com/discuss/97743 
【产品】多益网络产品策划助理面经，攒人品 https://www.nowcoder.com/discuss/97933 
【产品】百度产品经理武汉群面： https://www.nowcoder.com/discuss/109289 
【产品】京东面试流程分享： https://www.nowcoder.com/discuss/123636 
【产品】京东产品凉面经历-一面二面： https://www.nowcoder.com/discuss/121532 
【产品】京东上海产品运营面经： https://www.nowcoder.com/discuss/117582 

 【产品】京东管培生（产品方向）群面简要复盘： https://www.nowcoder.com/discuss/102193 
【产品】 京东提前批-软件产品经理凉面 https://www.nowcoder.com/discuss/87564 
【产品】京东 软件产品经理 一二面 https://www.nowcoder.com/discuss/91179 
【产品】 2018年8月1日阿里平台型产品经理电话面试 https://www.nowcoder.com/discuss/89666 
【产品】阿里二面产品经理－最悲催、悲惨、悲痛的体验 https://www.nowcoder.com/discuss/89728 
【产品】苏宁产品一面面经和百度群面（群面已过更新面经）： https://www.nowcoder.com/discuss/109200 
【产品】秋招小白的顺丰一二面回味儿~（面经） https://www.nowcoder.com/discuss/90536 
【产品】美团点评 产品运营（上海）面经（群面+单面2轮+hr电话面）： https://www.nowcoder.com/discuss/100569 
【产品】新鲜出炉的美团一面和二面（二面估计已经凉了）： https://www.nowcoder.com/discuss/101561 
【产品】新鲜出炉的美团一面和二面（二面估计已经凉了）： https://www.nowcoder.com/discuss/101561 
【产品】美团点评 互联网产品经理 一面： https://www.nowcoder.com/discuss/108586 
【产品】腾讯云产品面经分享： https://www.nowcoder.com/discuss/144718 
【产品】19秋招-腾讯-云计算产品经理-复盘&总结（初试挂）： https://www.nowcoder.com/discuss/123260 
【产品】腾讯产品培训生（补招）面试经历简要复盘（群面、初面） ： https://www.nowcoder.com/discuss/102249 
【产品】【产品】我是如何通过2019腾讯产品培训生面试的： https://www.nowcoder.com/discuss/102064 
【产品】 腾讯 产品策划 一面 https://www.nowcoder.com/discuss/91604 
【产品】腾讯产品面经（群面一面二面hr面） https://www.nowcoder.com/discuss/93768 
【产品】腾讯产品培训生（补招）面试经历简要复盘（群面、初面） ： https://www.nowcoder.com/discuss/102249 
【产品】【产品】我是如何通过2019腾讯产品培训生面试的： https://www.nowcoder.com/discuss/102064 
【产品】小米产品一面凉经： https://www.nowcoder.com/discuss/126176 

 【产品】秋招珠海金山WPS产品设计师一面面经 https://www.nowcoder.com/discuss/90241 

 【产品】字节跳动补录用户产品经理一面（很快就通知挂了自己真菜）： https://www.nowcoder.com/discuss/143647 
【产品】字节跳动用户产品经理补录面试复盘： https://www.nowcoder.com/discuss/145150 
【产品】头条用户产品面经以及求offer！： https://www.nowcoder.com/discuss/126267 
【产品】9.15 字节跳动凉面筋复盘： https://www.nowcoder.com/discuss/116205 
【产品】【产品】商业产品三面面经，周二加面定等级： https://www.nowcoder.com/discuss/110214 
【产品】头条商业产品经理面试回顾： https://www.nowcoder.com/discuss/110534 
【产品】今日头条/字节跳动 商业产品经理 三面 凉面筋： https://www.nowcoder.com/discuss/101081 
【产品】新鲜出炉的凉面～#策略产品： https://www.nowcoder.com/discuss/98972 
【产品】贝壳9.8产品三面面经： https://www.nowcoder.com/discuss/110293 
【产品】贝壳的产品岗面经： https://www.nowcoder.com/discuss/99820 

 管理

 【管理】字节跳动游戏品牌管理面经分享 https://www.nowcoder.com/discuss/210907 
【管理】游戏品牌管理 1/2/3/Hr面凉经 https://www.nowcoder.com/discuss/206466 
【管理】神策-数据分析&WPS-产品-一面凉经&网易游戏-项目管理： https://www.nowcoder.com/discuss/123125 
【管理】大疆研发管理工程师一面两次面试记录（不知道结果2333）
 https://www.nowcoder.com/discuss/89762 
【管理】顺丰科技，非技术流程管理岗一面面经，攒RP ~ https://www.nowcoder.com/discuss/90067 
【管理】 网易游戏项目管理工程师――内推一二电话面试 https://www.nowcoder.com/discuss/93417 
【管理】 网易游戏 项目管理工程师 一面面经 https://www.nowcoder.com/discuss/97162 
【管理】网易互娱项目管理（产品）内推一面 https://www.nowcoder.com/discuss/93783 
【管理】 网易游戏项目管理一面 面经 （攒人品贴） https://www.nowcoder.com/discuss/97824 
【管理】网易互娱 项目管理工程师 一面 https://www.nowcoder.com/discuss/98182 
【管理】热腾腾网易游戏项目管理二三面经： https://www.nowcoder.com/discuss/111564 
【管理】网易互娱 项目管理工程师 一面： https://www.nowcoder.com/discuss/98182 
【管理】网易游戏项目管理一面 面经 （攒人品贴）： https://www.nowcoder.com/discuss/97824 
【管理】神策-数据分析&WPS-产品-一面凉经&网易游戏-项目管理： https://www.nowcoder.com/discuss/123125 
格力智能项目管理面经： https://www.nowcoder.com/discuss/114600 

 管培生

 【管培生】2020届 京东管培生 第一批 技术方向 北京场 https://www.nowcoder.com/discuss/213235 
【管培生】京东管培面试之路详细分享，秋招攒人品。 https://www.nowcoder.com/discuss/213233 
【管培生】2020届京东管培生产品方向群面复盘 https://www.nowcoder.com/discuss/212154 
【管培生】贝壳现场面（C++）+京东技术管培生专业面： https://www.nowcoder.com/discuss/99274 
【管培生】Pdd产品管培生凉经，希望各位大佬给我一些建议。： https://www.nowcoder.com/discuss/121277 
【管培生】依图科技-项目管培生： https://www.nowcoder.com/discuss/107041 
【管培生】贝壳现场面（C++）+京东技术管培生专业面： https://www.nowcoder.com/discuss/99274 

 设计

 【设计】阿里云体验设计5轮面经 许愿offer https://www.nowcoder.com/discuss/224789 
【设计】 热乎乎的浦发总行8月6日面筋！ https://www.nowcoder.com/discuss/91095 

 【设计】秋招珠海金山WPS产品设计师一面面经 https://www.nowcoder.com/discuss/90241 
【设计】发个面经攒人品，网易互娱广州电面+现场面（游戏设计师）： https://www.nowcoder.com/discuss/122143 
【设计】网易游戏测试开发面经： https://www.nowcoder.com/discuss/121343 
【设计】网易互娱面经数据挖掘/机器学习算法（10.9更新二面）： https://www.nowcoder.com/discuss/121338 
【设计】网易数据分析面经： https://www.nowcoder.com/discuss/121329 
【设计】网易测开面经攒人品，等的快秃头了！更新：不秃头了，开奖了： https://www.nowcoder.com/discuss/121300 
【设计】网易互娱广州-游戏设计师一面凉经 https://www.nowcoder.com/discuss/92216 
【设计】拒绝了网易华为有赞，我去做了一名高中老师： https://www.nowcoder.com/discuss/142599 

 游戏策划

 【游戏策划】游戏品牌管理 1/2/3/Hr面凉经 https://www.nowcoder.com/discuss/206466 
【游戏策划】字节跳动游戏策划面经 https://www.nowcoder.com/discuss/205817 
【游戏策划】字节跳动游戏策划一面面经 https://www.nowcoder.com/discuss/203613 
【游戏策划】写面经攒人品，字节跳动游戏策划base 上海 https://www.nowcoder.com/discuss/203837 
【游戏策划】提前批 游戏策划 面经 https://www.nowcoder.com/discuss/204079 
【游戏策划】字节跳动游戏策划一面面经 https://www.nowcoder.com/discuss/203950 
【游戏策划】游戏策划 数值+系统+战斗方向 三面 面经 https://www.nowcoder.com/discuss/204180 
【游戏策划】字节跳动游戏策划三面面经 https://www.nowcoder.com/discuss/204302 
【游戏策划】（也写个面经攒攒人品）字节跳动北京游策电面三连 https://www.nowcoder.com/discuss/204216 
【游戏策划】多益游戏策划一面，攒人品贴 https://www.nowcoder.com/discuss/93851 
【游戏策划】多益网络-游戏策划-面经 https://www.nowcoder.com/discuss/94281 
【游戏策划】菜鸡佛系秋招总结： https://www.nowcoder.com/discuss/126981 

 运营&游戏运营

 【运营&游戏运营】【运营&游戏运营】运营开发岗 https://www.nowcoder.com/discuss/227795 
【运营&游戏运营】腾讯春招-运营岗二面凉经 https://www.nowcoder.com/discuss/226940 
【运营&游戏运营】【运营&游戏运营】运营岗面经+20届内推 https://www.nowcoder.com/discuss/211612 
【运营&游戏运营】字节跳动游戏提前批游戏运营管理面经（3面+HR） https://www.nowcoder.com/discuss/210136 
【运营&游戏运营】腾讯提前批游戏运营面经之二： https://www.nowcoder.com/discuss/111886 
【运营&游戏运营】bilibili游戏运营二面结束： https://www.nowcoder.com/discuss/109346 
【运营&游戏运营】京东上海产品运营面经： https://www.nowcoder.com/discuss/117582 
【运营&游戏运营】2019阿里菜鸟运营岗-内推3面已获意向书： https://www.nowcoder.com/discuss/105992 
【运营&游戏运营】美团点评 产品运营（上海）面经（群面+单面2轮+hr电话面）： https://www.nowcoder.com/discuss/100569 
【运营&游戏运营】美团算法工程师-凉面面经： https://www.nowcoder.com/discuss/100531 
【运营&游戏运营】美团前端一、二面面经： https://www.nowcoder.com/discuss/99954 
【运营&游戏运营】美团前端二面： https://www.nowcoder.com/discuss/99736 
【运营&游戏运营】美团前端一面： https://www.nowcoder.com/discuss/99519 
【运营&游戏运营】美团前端一面 凉面： https://www.nowcoder.com/discuss/99289 
【运营&游戏运营】新鲜出炉的美团一面和二面（二面估计已经凉了）： https://www.nowcoder.com/discuss/101561 
【运营&游戏运营】新鲜出炉的美团一面和二面（二面估计已经凉了）： https://www.nowcoder.com/discuss/101561 
【运营&游戏运营】网易广州秋招电商运营一面到三面： https://www.nowcoder.com/discuss/126013 
【运营&游戏运营】9.15 字节跳动凉面筋复盘： https://www.nowcoder.com/discuss/116205 
【运营&游戏运营】【运营&游戏运营】直播运营岗电面： https://www.nowcoder.com/discuss/109627 
【运营&游戏运营】bigo产品运营面经，3轮专业面＋hr面，攒人品。： https://www.nowcoder.com/discuss/122417 
【运营&游戏运营】途游产品运营一面....要凉的节奏....： https://www.nowcoder.com/discuss/144485 
【运营&游戏运营】字节跳动商业产品运营经理三面面经 https://www.nowcoder.com/discuss/232127 
【运营&游戏运营】字节跳动产品运营面经（已完成一二三面 许愿意向书） https://www.nowcoder.com/discuss/226872 

 营销

 【营销】京东专业面视频面试营销岗面经 https://www.nowcoder.com/discuss/215411 
【营销】远景能源 技术营销岗 四轮面经： https://www.nowcoder.com/discuss/115808 
【营销】汉中国银联市场营销岗群面+非技术面 https://www.nowcoder.com/discuss/94659

---

## 美图C++研发工程师（算法落地）面经~

来源：牛客网 ｜ 类型：面经 ｜ 发布：2018-09-04 ｜ [原文链接](https://www.nowcoder.com/discuss/353154510568759296)

直接进入主题吧。

 
 1.自我介绍，自己觉得最好的项目

 
 2.说一下Tensorflow.

 
 3,Tensorflow中的池化层有哪些（除了最大和平均）

 
 4.Tensorflow数据流图的优点是什么？

 
 5.BN的过程

 
 然后就是c++的基础

 
 6.纯虚函数的定义

 
 7.c和c++的结构体有什么区别

 
 8. C++ vector 的resize和reverve的区别 

 
 9.c++函数的拷贝 

 
 10.你是哪里的？ 

 
 11.职业规划，具体技术方面的。 

 
 12.你有什么想问的。 

 
 15分钟。。。。就给挂了，回去补c++基础。

---

## 北京美图MTLab怎么样？

来源：牛客网 ｜ 类型：面经 ｜ 发布：2018-05-11 ｜ [原文链接](https://www.nowcoder.com/discuss/353154372727152640)

本人计算机视觉渣硕一枚，之前投递了大量简历，笔试被刷了一波，面试被刷了一波，深感cv界不好混
 

 
 美图的实习笔试做了，然后就没消息了；然后自己又在水木社区找了美图的招聘信息，又投了一遍；今天下午面试了，然后面试官说只有一面，聊的方向他们实验室也在做
 一面（27分钟）：自我介绍，质量评价怎么做的，高通和低通滤波，opencv&PIL，BN作用，1*1卷积作用，防止过拟合的方法，python：迭代器，通道转换；C++: 指针和引用区别，const作用 
 

 
 晚上直接hr就发offer了，聊了入职时间问题
 

 
 其实自己主要是以一种学习的心态，也没有当算转正在北京呆，毕竟以后秋招才重要
 

 
 自己在等的offer：百度cv的度秘，感觉这部门太玄学了，过程很复杂，自己都不知道招不招cv的人了，那干嘛把我简历捞到他们部门去；还有快手cv算法,说的这周给信息，也没消息
 

 
 有大佬了解MTLab的吗？我想先接了offer,毕竟美图里面做图像有很多应用场景，自己想先去学东西，好好准备秋招
 

 
 大家给给建议啊！！！！

---

## 求美图厦门算法实习岗的视频面面经

来源：牛客网 ｜ 类型：面经 ｜ 发布：2018-05-04 ｜ [原文链接](https://www.nowcoder.com/discuss/353154363860393984)

求问各位大佬，有人视频面面过美图厦门算法实习岗吗？求面经，手撕代码吗？

---

## 面经- -

来源：牛客网 ｜ 类型：面经 ｜ 发布：2017-10-02 ｜ [原文链接](https://www.nowcoder.com/discuss/353154192204308480)

看到各位说牛客上面经越来越少了我决定把我这个菜鸡的面经也算回馈牛客。 

 
 

 先介绍下我自己，末流211（学校rank100左右那种），ACM铜牌（其实是抱大腿混的），没有项目经历（其实有一个但是是跟深度学习有关的我一个小小的本科生投C++写上也没多大用），实习经历有两个，一个是在科大讯飞，做了一个半月辞职来了北京现在实习的公司，Terark，现在实习这家公司我还是很推荐的，在这里我学到了很多，而且这家公司虽然是创业公司但是我觉得很有前景，从跟boss的接触来看这家公司以后应该会走很远。 

 秋招的投了batjn和很多大厂- -最后收到京东offer- -结束秋招- - 

 
 

 咸鱼我的面试经历秋招其实不算多，只有美图（一面G），京东（offer），吉比特（一面G），华为（没去面试） 

 笔试全ac但是没有面试的也不少- -大概还是简历搓了些- -以及bat的笔试因为都在实习工作时间内所以都翘了.... 

 
 

 美图一面面经： 

 介绍下你的项目（- -没写过项目啊- -） 
 

 两个计算机组成原理题（机组我挂了题目说得啥我也不记得了大概就因为开场两个问题导致心态问题导致整场崩盘...） 

 mysql的事务等级有哪些，分别有什么作用 

 ACID是什么
 

 数据库索引的匹配原则 

 介绍下B树（B树B+树） 

 B树效率 

 为什么要使用B树 

 如何在C语言中使用C++的头文件 

 给出一个结构体中的一个成员的地址如何找到结构体的地址 

 TCP四次挥手的过程，TIME WAIT的作用 

 进程的优先级是如何确定的 

 Linux的进程优先级应该怎么看 

 进程的内存地址是如何安排的 

 死锁是怎么产生的 

 select/epoll的区别 

 智能指针有哪些有什么作用有什么区别 

 dynamic_cast的作用 

 内存隔断（- -当时完全没听过） 

 fork出来的子进程和父进程是否会有共享内存空间 

 进程通信有哪些方式 

 ping的过程 

 给出一个数组，找出和为给定数的所有组合 

 梯度下降算法是怎么回事，梯度下降算***有什么问题 

 
 

 - -美图挂的原因主要是基础确实不牢上面文的问题好多都是一知半解一半能答一半不能答- -或者说了一半没说到面试官的点子上去。 

 以及那天早上面试...我有种没睡醒的感觉- - 

 
 

 京东一面： 

 你实习所做的项目中有什么对你来说是最困难的 

 看你实习做的跟rocksdb相关，简单介绍下rocksdb 

 介绍下LSM tree 

 介绍下B tree 

 看你简历上有写机器学习，你简单介绍下你会的机器学习算法 

 多进程与多线程的区别。 

 数据库索引为什么要用B树 

 数据结构设计题（面试官的标解是哈希+链表（不止一个next的那种），我给的解法是跳表，面试完发现跳表貌似有问题...面试的时候面试官没说这个错了- -）具体问题忘了- - 

 平时喜欢看开源项目吗（不喜欢看别人代码- -现在想想能过一面我也是幸运啊....） 

 
 

 京东二面： 

 你实习的公司是做什么的，介绍下主要产品 

 有女朋友吗- - 

 （主要闲聊我也不太记得闲聊啥了） 

 
 

 京东hr面： 

 你愿意在北京工作吗，父母也支持吗 

 你以后想从事什么方面的工作 

 你在学校里是怎么学习的 

 （6分40秒解决战斗感觉hr超强的...) 

 
 

 - - 

 感觉京东过了的原因...可能真的是运气好吧.... 

 
 

 吉比特一面： 

 数学成绩- -（不咋地） 

 给了上次笔试的一道题目问为什么这么写- -有没有别的思路 

 TCP拥塞控制 

 如果客户端这里的网络出现拥堵，如何知道还能不能继续发包- -（这个题目我没听太明白当时） 

 给了个数学题让写一下- -大概是那种思维题然后没写出来- - 

 
 

 吉比特没过的原因感觉一个是对游戏编程没接触过- -一个是网络方面的知识没了解太深- -一个是思维太过僵化- - 

 另外就是hc真少.... 

 
 

 - - 

 秋招结束，我也有一些感触- - 

 首先就是面试的时候要自信，无论你觉得这场是必挂的还是必过的就是要自信，（京东一面可能就是表现的太自信了很多问题面试官没发现- -美图一面可能就是表现的太不自信了很多亮点也被掩盖住了- -） 

 其次就是要有足够的知识来做储备。我今年找工作的历程时春招全挂- -当时觉得acm出身学过一些机器学习应该可以去搞一搞算法然后就全挂了- -到了6月底我才明确自己以后想写C++的想法，C++ Primer这本书我没看完- -UNIX网络编程也没看- -TCP/IP也是凑合看的- -STL源码看了一部分- -多线程看了会视频教学面试那会基本忘完了- -所以我今年的结果- -真的是运气- -如果不想凭运气进一家公司- -一定要有足够的知识储备- -而这些来自平时写代码遇到的各种各样的坑 

 最后就是- -平时多积点人品吧- -运气也是很重要的- - 

 
 

 今年秋招的面试经历感受就是上面这样，希望各位dalao不要虐我- -也希望能给后来者一些帮助吧- -

---

## 面了四家公司的计算机视觉岗，发个面试官的评价

来源：牛客网 ｜ 类型：面经 ｜ 发布：2017-09-12 ｜ [原文链接](https://www.nowcoder.com/discuss/353154116358709248)

本人是做医学图像的，研究生期间数学建模、比赛都获得了TOP3的名次，医学图像顶一作会发了4篇，投了4家互联网公司，以下是面试官（技术面）对我个人的评价

 
 CVTE：嗯，项目经验比较多，也发了顶会挺好的，结果：技术面过了

 
 美图：不错，自然图像医学图像方向都是通的，结果：OFFER到手

 
 腾讯：项目经验挺多的，也刷了比赛，挺好，什么时候来实习 结果：OFFER差不多到手

 
 阿里：你为什么投我们方向？你知道我们是做自然图像的吗？ 结果：一面挂

---

## 美图内推面试过去一周了还没消息，是挂了吗？

来源：牛客网 ｜ 类型：面经 ｜ 发布：2017-09-11 ｜ [原文链接](https://www.nowcoder.com/discuss/353154113422696448)

上周三面了美图内推的机器学习计算机视觉岗，当时感觉还不错，说是顺利的话三天内给二面通知，可到现在快一周了还没消息，不知道是不是挂了，心塞。

---

## 有面美图计算机视觉的吗😊，求面经。

来源：牛客网 ｜ 类型：面经 ｜ 发布：2017-09-03 ｜ [原文链接](https://www.nowcoder.com/discuss/353154095747899392)

各位大佬有面美图的没？计算机视觉，求面经求交流呀。

---
