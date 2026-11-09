---
symbol: "CHD4"
type: "gene"
col: 3249
ensembl_id: "ENSG00000111642"
name: "chromodomain helicase DNA binding protein 4"
location: "12p13.31"
module: 30
arm: "-"
pooled_cpm: 174.69
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# CHD4

*chromodomain helicase DNA binding protein 4* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.57× (z +33.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.820× (z -5.2, q 9e-05, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.453×); [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.308×; ⚠ toxic); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.457×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPA2B1]] (+0.69, fdr 7e-06), [[SKIL]] (+0.58, fdr 2e-05), [[NID1]] (+0.56, fdr 3e-05); moves opposite to [[LRIG2]] (-0.63, fdr 1e-05), [[LCMT1]] (-0.62, fdr 1e-05), [[CDADC1]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.57×** | +33.5 | 0e+00 | 46/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.27×** | +15.8 | 0e+00 | 44/48 (A498, NCI-H2347, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.04×** | +14.3 | 4e-44 | 45/49 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +14.2 | 2e-43 | 42/49 (NCI-H2030, A549, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +12.0 | 7e-31 | 37/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.82×** | +11.6 | 6e-29 | 43/44 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +10.3 | 7e-23 | 45/48 (C32, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.61×** | +8.8 | 1e-16 | 38/45 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.53×** | +8.6 | 6e-16 | 35/48 (AsPC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.40×** | +6.8 | 7e-10 | 32/48 (HOP62, AsPC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.30×** | +5.3 | 7e-06 | 35/48 (CFPAC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +5.2 | 8e-06 | 27/48 (A498, HS-578T, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.31×** | +5.2 | 8e-06 | 31/47 (LoVo, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.27×** | +4.9 | 5e-05 | 31/48 (NCI-H2347, RPMI-7951, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.26×** | +4.6 | 1e-04 | 26/48 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.3 | 6e-04 | 20/48 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 7e-04 | 26/48 (C32, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.006 | 15/48 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.027 | 18/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 1.13× | +3.1 | 0.039 | 5/48 (PANC-1, HCT15, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3249.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 0.453×); [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.308×; ⚠ toxic); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (COLO 205 0.457×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.820×** | -5.2 | 9e-05 | 31/48 (LoVo, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.852× | -4.2 | 0.009 | 18/48 (RPMI-7951, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.829×** | -3.6 | 0.052 | 22/47 (COLO 205, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.20 | 13/48 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.856× | -3.0 | 0.30 | 16/47 (NCI-H2030, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 159 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +33.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 175 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +21.8) | — |
| [[HOP62 (line)]] | alt | 162 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +32.5) | — |
| [[NCI-H460 (line)]] | wt | 102 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.7) | — |
| [[A498 (line)]] | wt | 155 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +39.7) | — |
| [[A549 (line)]] | wt | 97.7 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +22.8) | — |
| [[C32 (line)]] | wt | 149 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +23.7) | — |
| [[HS-578T (line)]] | alt | 132 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +26.4) | — |
| [[NCI-H1792 (line)]] | alt | 108 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +27.0) | — |
| [[NCI-H2347 (line)]] | alt | 208 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +36.5) | — |
| [[PANC-1 (line)]] | alt | 90.7 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +28.1) | — |
| [[SW 900 (line)]] | alt | 196 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +25.9) | — |
| [[Panc 03.27 (line)]] | alt | 222 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +33.4) | [[Lonafarnib (drug)]] 5 µM 0.308× (z -8.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 193 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +19.6) | — |
| [[SW480 (line)]] | alt | 350 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +16.9) | — |
| [[A-172 (line)]] | wt | 114 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 96.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +22.0) | — |
| [[CFPAC-1 (line)]] | alt | 99.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +25.4) | — |
| [[SNU-423 (line)]] | alt | 102 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +18.7) | — |
| [[SW48 (line)]] | wt | 252 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 140 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.0) | — |
| [[HepG2_C3A (line)]] | wt | 185 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +21.6) | — |
| [[hTERT-HPNE (line)]] | wt | 169 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.77× (z +27.0) | — |
| [[KATO III (line)]] | alt | 136 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +15.1) | — |
| [[NCI-H2030 (line)]] | alt | 176 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +30.5) | — |
| [[SW1417 (line)]] | alt | 239 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +30.2) | — |
| [[COLO 205 (line)]] | alt | 185 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.453× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 127 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.5) | — |
| [[Hs 766T (line)]] | wt | 92.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.8) | — |
| [[J82 (line)]] | alt | 167 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +21.8) | — |
| [[LOX-IMVI (line)]] | wt | 224 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +18.8) | — |
| [[LS 180 (line)]] | wt | 174 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.65× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 147 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +20.8) | — |
| [[NCI-H23 (line)]] | alt | 365 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +13.3) | — |
| [[SK-MEL-2 (line)]] | alt | 304 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +22.7) | — |
| [[A-427 (line)]] | wt | 276 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 219 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +23.7) | — |
| [[SNU-1 (line)]] | wt | 165 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +15.9) | — |
| [[SW 1271 (line)]] | alt | 166 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.64× (z +12.4) | — |
| [[H4 (line)]] | wt | 185 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.4) | — |
| [[HCT15 (line)]] | alt | 204 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.1) | — |
| [[RKO (line)]] | wt | 263 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SHP-77 (line)]] | alt | 176 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW 1088 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 219 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 188 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 246 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*30 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA2B1]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 | STRING 481 |
| [[SKIL]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[NID1]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[DLG2]] | +0.56 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[HNRNPU]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 | pathway: Adipogenesis; STRING 552 |
| [[ROCK2]] | +0.55 | +0.53 / +0.55 | both halves | 1e-05 | pathway: Potential therapeutics for SARS |
| [[CCDC144CP]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TRIP12]] | +0.54 | +0.50 / +0.41 | both halves | 4e-05 | STRING 529 |
| [[SMARCA1]] | +0.54 | +0.43 / +0.51 | both halves | 3e-05 | same gene group; STRING 756 |
| [[USP7]] | +0.54 | +0.45 / +0.48 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[HUWE1]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[PHF8]] | +0.53 | +0.56 / +0.41 | both halves | 4e-05 | same gene group; pathway: Chromatin modifying enzymes |

## Genes that move opposite

*70 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIG2]] | -0.63 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[LCMT1]] | -0.62 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[CDADC1]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ZNF333]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[HEATR6]] | -0.60 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[CCZ1B]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[GTF2H2B]] | -0.59 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[HEATR5B]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[SLC15A4]] | -0.57 | -0.64 / -0.40 | both halves | 4e-05 |  |
| [[MMS19]] | -0.57 | -0.67 / -0.39 | both halves | 5e-05 |  |
| [[PSMF1]] | -0.57 | -0.62 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **-** arm (projection on the module's main direction -0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-2.2, -12.4); signed map (14.1, -10.2). **Vector** length 111, 37.0% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +33.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +10.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.1 | +15.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +14.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | +3.1 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +0.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.0 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,570,082-6,614,524 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Mi-2b, Mi2-BETA |
| Gene groups (HGNC) | PHD finger proteins; SNF2 related family; NuRD complex subunits; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: ChAHP complex assembly; Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14839](https://www.uniprot.org/uniprotkb/Q14839) (ATP-dependent chromatin remodeler CHD4):

> ATP-dependent chromatin-remodeling factor that binds and distorts nucleosomal DNA. Acts as a component of the histone deacetylase NuRD complex which participates in the remodeling of chromatin. Localizes to acetylated damaged chromatin in a ZMYND8-dependent manner, to promote transcriptional repression and double-strand break repair by homologous recombination. Involved in neurogenesis (By similarity).

**Summary**, from NCBI Gene [1108](https://www.ncbi.nlm.nih.gov/gene/1108):

> The product of this gene belongs to the SNF2/RAD54 helicase family. It represents the main component of the nucleosome remodeling and deacetylase complex and plays an important role in epigenetic transcriptional repression. Patients with dermatomyositis develop antibodies against this protein. Somatic mutations in this gene are associated with serous endometrial tumors. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:1919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1919) · Entrez [1108](https://www.ncbi.nlm.nih.gov/gene/1108) · UniProt [Q14839](https://www.uniprot.org/uniprotkb/Q14839) · Ensembl [ENSG00000111642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111642)

## Data

Gene col 3249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3249); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3249]; `tensor/DDL_lfc|DDL_z.npy` [3249]; `embed/gene_vectors.npy` [3249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3249 or target_col == 3249). Every well: [[CHD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
