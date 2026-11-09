---
symbol: "NUDT5"
type: "gene"
col: 9149
ensembl_id: "ENSG00000165609"
name: "nudix hydrolase 5"
location: "10p14"
module: 4
arm: "+"
pooled_cpm: 25.07
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NUDT5

*nudix hydrolase 5* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +19.0, q 0e+00, up in 41 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.69× (z +9.2, q 3e-18, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.803× (z -5.4, q 4e-05, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MACROH2A1]] (+0.72, fdr 7e-06), [[TMEM33]] (+0.68, fdr 7e-06), [[PSMD1]] (+0.66, fdr 7e-06); moves opposite to [[SAT2]] (-0.67, fdr 7e-06), [[AAMDC]] (-0.59, fdr 2e-05), [[JUND]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9149.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.98×** | +19.0 | 0e+00 | 41/43 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.06×** | +18.7 | 0e+00 | 34/35 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.36×** | +13.8 | 3e-41 | 32/40 (A549, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.80×** | +10.3 | 1e-22 | 41/47 (AsPC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.77×** | +9.9 | 4e-21 | 39/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.78×** | +9.6 | 6e-20 | 36/45 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.48×** | +9.6 | 6e-20 | 35/47 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.71×** | +9.4 | 5e-19 | 37/48 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +9.2 | 3e-18 | 36/47 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.63×** | +8.5 | 8e-16 | 36/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +8.5 | 1e-15 | 34/47 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.3 | 1e-11 | 32/48 (SW480, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.46×** | +6.3 | 1e-08 | 25/48 (SW480, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.45×** | +6.2 | 2e-08 | 30/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +5.9 | 1e-07 | 23/47 (COLO 205, HT-29, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.24×** | +3.5 | 0.012 | 11/47 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.015 | 15/47 (NCI-H1573, LOX-IMVI, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.017 | 11/45 (KATO III, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.020 | 7/48 (NCI-H1792, SW 1088, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.030 | 9/48 (NCI-H1792, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.2 | 0.031 | 13/48 (LOX-IMVI, RKO, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.13× | +3.1 | 0.038 | 8/48 (A-172, SW1417, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.052 | 5/44 (J82, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.17× | +2.8 | 0.096 | 7/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.36×** | +2.8 | 0.097 | 2/48 (NCI-H23, SHP-77) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.803×** | -5.4 | 4e-05 | 23/47 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.639×** | -4.1 | 0.007 | 16/47 (A-172, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.848× | -4.1 | 0.007 | 12/48 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.792×** | -4.1 | 0.007 | 17/48 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.795×** | -3.8 | 0.014 | 15/47 (NCI-H2030, HT-29, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.663×** | -3.7 | 0.017 | 9/48 (A498, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.829×** | -3.3 | 0.090 | 9/48 (LS 180, H4, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.831×** | -3.2 | 0.090 | 14/47 (HEC-1-A, SNU-423, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.65 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 22.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[HOP62 (line)]] | alt | 15.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.09× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 33.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 27.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 30.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[Hs 766T (line)]] | wt | 19.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.79× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 33.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LoVo (line)]] | wt | 29.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.84× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LOX-IMVI (line)]] | wt | 24.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.99× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LS 180 (line)]] | wt | 27.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.90× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SNU-423 (line)]] | alt | 14.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.26× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0669× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0702× (z -10.9) |
| [[KATO III (line)]] | alt | 22.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2030 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H23 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.395× (z -9.4) |
| [[SHP-77 (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -8.5) |
| [[A-427 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROH2A1]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[TMX3]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[NUP155]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CDC123]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 | STRING 769; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[GOT2]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[XRCC5]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[RPE]] | +0.62 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CHID1]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[UGGT1]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[BANF1]] | +0.59 | +0.51 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | -0.67 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.59 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[JUND]] | -0.59 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[RSRP1]] | -0.58 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CNNM4]] | -0.57 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[WIPF2]] | -0.57 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[EIF1]] | -0.57 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[NEU1]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[KMT2E]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[DCXR]] | -0.56 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[SNHG7]] | -0.56 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SIRT2]] | -0.55 | -0.60 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NUDT5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.5, -33.2); signed map (-13.6, -45.6). **Vector** length 67.9, 13.2% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.8 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +7.3 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.6 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | -2.2 | +3.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | +0.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | -0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -4.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -1.4 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:12,165,330-12,195,891 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hYSAH1, YSA1H |
| Gene groups (HGNC) | Nudix hydrolase family |
| Reactome | 4 pathways, smallest: Phosphate bond hydrolysis by NUDT proteins; Purine catabolism; Nucleotide catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKK9](https://www.uniprot.org/uniprotkb/Q9UKK9) (ADP-sugar pyrophosphatase):

> Enzyme that can either act as an ADP-sugar pyrophosphatase in absence of diphosphate or catalyze the synthesis of ATP in presence of diphosphate. In absence of diphosphate, hydrolyzes with similar activities various modified nucleoside diphosphates such as ADP-ribose, ADP-mannose, ADP-glucose, 8-oxo-GDP and 8-oxo-dGDP. Can also hydrolyze other nucleotide sugars with low activity. In presence of diphosphate, mediates the synthesis of ATP in the nucleus by catalyzing the conversion of ADP-ribose …

**Summary**, from NCBI Gene [11164](https://www.ncbi.nlm.nih.gov/gene/11164):

> This gene belongs to the Nudix (nucleoside diphosphate linked moiety X) hydrolase superfamily. The encoded enzyme catalyzes the hydrolysis of modified nucleoside diphosphates, including ADP-ribose (ADPR) and 8-oxoGua-containing 8-oxo-dADP and 8-oxo-dGDP. Protein-bound ADP ribose can be hazardous to the cell because it can modify some amino acid residues, resulting in the inhibition of ATP-activated potassium channels. 8-oxoGua is an oxidized form of guanine that can potentially alter genetic …

**Accessions** — [HGNC:8052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8052) · Entrez [11164](https://www.ncbi.nlm.nih.gov/gene/11164) · UniProt [Q9UKK9](https://www.uniprot.org/uniprotkb/Q9UKK9) · Ensembl [ENSG00000165609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165609)

## Data

Gene col 9149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9149); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9149]; `tensor/DDL_lfc|DDL_z.npy` [9149]; `embed/gene_vectors.npy` [9149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9149 or target_col == 9149). Every well: [[NUDT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
