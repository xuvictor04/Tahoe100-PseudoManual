---
symbol: "GGNBP2"
type: "gene"
col: 15909
ensembl_id: "ENSG00000278311"
name: "gametogenetin binding protein 2"
location: "17q12"
module: 20
arm: "-"
pooled_cpm: 188.3
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# GGNBP2

*gametogenetin binding protein 2* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.69× (z +14.6, q 1e-45, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.00× (z +13.7, q 2e-40, up in 47 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 15 lines (HEC-1-A 3.24×, KATO III 3.02×, LoVo 2.86×, NCI-H460 2.33×, …); [[Homoharringtonine (drug)]] 5 µM in 12 lines (HEC-1-A 2.75×, A549 2.71×, LoVo 2.93×, KATO III 2.69×, …; ⚠ cell-cycle shift, explains ~39% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.681× (z -7.3, q 2e-10, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.787× (z -6.7, q 6e-09, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INAFM1]] (+0.75, fdr 7e-06), [[ZMYM5]] (+0.73, fdr 7e-06), [[CROCCP2-1]] (+0.70, fdr 7e-06); moves opposite to [[RPSA]] (-0.69, fdr 7e-06), [[VMA21]] (-0.66, fdr 7e-06), [[RPE]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15909.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 15 lines (HEC-1-A 3.24×, KATO III 3.02×, LoVo 2.86×, NCI-H460 2.33×, …); [[Homoharringtonine (drug)]] 5 µM in 12 lines (HEC-1-A 2.75×, A549 2.71×, LoVo 2.93×, KATO III 2.69×, …; ⚠ cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.69×** | +14.6 | 1e-45 | 45/48 (HEC-1-A, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +13.7 | 2e-40 | 47/48 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +7.9 | 6e-13 | 42/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.38×** | +6.4 | 2e-08 | 34/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +5.8 | 9e-07 | 32/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.35×** | +5.7 | 1e-06 | 31/48 (HEC-1-A, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +5.4 | 4e-06 | 31/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.28×** | +4.6 | 3e-04 | 30/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.20× | +3.3 | 0.057 | 20/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.0 | 0.15 | 21/48 (LS 180, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15909.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.681×** | -7.3 | 2e-10 | 30/44 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -6.7 | 6e-09 | 34/48 (A-172, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.715×** | -6.1 | 2e-07 | 27/45 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.831×** | -5.2 | 3e-05 | 25/48 (AsPC-1, COLO 205, …) | top dose only | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.773×** | -4.9 | 1e-04 | 32/48 (A549, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.785×** | -4.6 | 4e-04 | 27/47 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.813×** | -4.1 | 0.003 | 25/49 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.777×** | -3.8 | 0.010 | 28/49 (SNU-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.879× | -3.6 | 0.019 | 12/48 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.839× | -3.5 | 0.028 | 20/48 (AsPC-1, A498, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.844× | -3.1 | 0.097 | 18/48 (AsPC-1, A498, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15909. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 183 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -13.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 304 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +13.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -10.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 245 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +20.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.442× (z -11.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 139 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +20.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -10.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 249 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.546× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 169 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.45× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +8.6) | — |
| [[SW480 (line)]] | alt | 161 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 205 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +24.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.24× (z +19.9) | — |
| [[NCI-H1792 (line)]] | alt | 143 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +10.5) | — |
| [[RKO (line)]] | wt | 156 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +10.7) | — |
| [[A-427 (line)]] | wt | 192 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -15.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 203 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.657× (z -9.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[H4 (line)]] | wt | 159 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 227 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.09× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 218 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.567× (z -8.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 177 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.05× (z +9.3) | — |
| [[KATO III (line)]] | alt | 188 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +20.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.02× (z +15.9) | — |
| [[NCI-H2347 (line)]] | alt | 225 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.511× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[Panc 03.27 (line)]] | alt | 236 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +9.1) | — |
| [[PANC-1 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.1) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 218 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.98× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 238 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.5) ⚠ cell-cycle shift, explains ~39% of this change | [[Dinaciclib (drug)]] 5 µM 0.434× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 146 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +11.3) | — |
| [[A-172 (line)]] | wt | 217 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.645× (z -9.5) |
| [[AN3 CA (line)]] | alt | 150 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +8.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[C32 (line)]] | wt | 114 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.8) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[CFPAC-1 (line)]] | alt | 153 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.3) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HepG2_C3A (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +15.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HS-578T (line)]] | alt | 212 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +8.7) | — |
| [[J82 (line)]] | alt | 216 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +13.3) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 177 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 177 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -12.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 163 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0756× (z -9.9) |
| [[BT-474 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 141 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 188 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 198 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15909), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.73 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | +0.70 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ZFAND2B]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[FBXW5]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[PPIG]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 | STRING 423 |
| [[NKAP]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ARID4A]] | +0.67 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ING2]] | +0.67 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[SRSF11]] ⚠ | +0.67 | +0.69 / +0.57 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TERF2IP]] | +0.65 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[ATF4]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | -0.69 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[VMA21]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[RPE]] | -0.65 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[PSME3]] | -0.64 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.64 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[WDR77]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[CHID1]] | -0.62 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[PGAM1]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.62 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[APP]] | -0.62 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[EMC1]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.61 | -0.48 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.9, -29.6); signed map (-14.6, -0.5). **Vector** length 126, 43.1% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +8.2 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +13.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.0 | +5.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.0 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.6 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.6 | -6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -7.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.2 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.1 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | gametogenetin binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:36,544,912-36,589,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZFP403, LZK1, FLJ22561, FLJ21230, DIF-3, DIF3; previously ZNF403 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3C7](https://www.uniprot.org/uniprotkb/Q9H3C7) (Gametogenetin-binding protein 2):

> May be involved in spermatogenesis.

**Summary**, from NCBI Gene [79893](https://www.ncbi.nlm.nih.gov/gene/79893):

> Predicted to be involved in spermatogenesis. Predicted to act upstream of or within several processes, including labyrinthine layer blood vessel development; negative regulation of cell population proliferation; and negative regulation of peptidyl-tyrosine phosphorylation. Predicted to be located in cytoplasmic vesicle. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:19357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19357) · Entrez [79893](https://www.ncbi.nlm.nih.gov/gene/79893) · UniProt [Q9H3C7](https://www.uniprot.org/uniprotkb/Q9H3C7) · Ensembl [ENSG00000278311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278311)

## Data

Gene col 15909: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15909); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15909, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15909]; `tensor/DDL_lfc|DDL_z.npy` [15909]; `embed/gene_vectors.npy` [15909]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15909 or target_col == 15909). Every well: [[GGNBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGNBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
