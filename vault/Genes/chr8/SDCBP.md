---
symbol: "SDCBP"
type: "gene"
col: 6039
ensembl_id: "ENSG00000137575"
name: "syndecan binding protein"
location: "8q12.1"
module: 36
arm: "-"
pooled_cpm: 153.15
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SDCBP

*syndecan binding protein* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.14× (z +29.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.788× (z -4.3, q 0.009, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C21orf91]] (+0.58, fdr 1e-05), [[LSMEM1]] (+0.57, fdr 1e-05), [[TEX14]] (+0.57, fdr 1e-05); moves opposite to [[TIMM23B]] (-0.67, fdr 7e-06), [[EMC8]] (-0.65, fdr 1e-05), [[NDUFS6]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.14×** | +29.4 | 0e+00 | 47/48 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.26×** | +14.3 | 6e-44 | 45/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.05×** | +13.1 | 7e-37 | 41/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +10.1 | 1e-21 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +8.1 | 7e-14 | 35/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +7.0 | 3e-10 | 34/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.9 | 6e-10 | 30/49 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 7e-09 | 38/48 (NCI-H460, SW 900, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +6.0 | 1e-07 | 33/49 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.8 | 3e-07 | 29/48 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +5.8 | 4e-07 | 31/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.7 | 7e-07 | 34/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.5 | 2e-06 | 34/48 (NCI-H460, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +5.1 | 1e-05 | 29/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +5.0 | 2e-05 | 29/48 (C32, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +5.0 | 2e-05 | 27/49 (Hs 766T, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.788×** | -4.3 | 0.009 | 25/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.803×** | -4.0 | 0.019 | 26/48 (AN3 CA, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.823×** | -3.6 | 0.072 | 23/48 (SW 1088, A498, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.880× | -3.3 | 0.14 | 11/48 (SNU-1, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -3.0 | 0.28 | 23/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 124 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +27.0) | — |
| [[PANC-1 (line)]] | alt | 84.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +27.6) | — |
| [[C32 (line)]] | wt | 216 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +24.5) | — |
| [[A-172 (line)]] | wt | 138 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +27.0) | — |
| [[A498 (line)]] | wt | 400 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +30.7) | — |
| [[HS-578T (line)]] | alt | 186 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +30.6) | — |
| [[LOX-IMVI (line)]] | wt | 130 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +21.1) | — |
| [[NCI-H1792 (line)]] | alt | 151 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +27.2) | — |
| [[NCI-H2030 (line)]] | alt | 157 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +18.0) | — |
| [[SW 900 (line)]] | alt | 218 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +20.1) | — |
| [[A549 (line)]] | wt | 176 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +24.9) | — |
| [[hTERT-HPNE (line)]] | wt | 175 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.67× (z +27.8) | — |
| [[LoVo (line)]] | wt | 138 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +25.7) | — |
| [[SNU-1 (line)]] | wt | 136 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 190 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +33.1) | — |
| [[HEC-1-A (line)]] | alt | 103 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 167 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +26.9) | — |
| [[Hs 766T (line)]] | wt | 283 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +19.1) | — |
| [[J82 (line)]] | alt | 206 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +27.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 101 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +19.8) | — |
| [[NCI-H2347 (line)]] | alt | 187 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +16.8) | — |
| [[RPMI-7951 (line)]] | alt | 188 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +23.5) | — |
| [[SK-MEL-2 (line)]] | alt | 126 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +28.2) | — |
| [[AsPC-1 (line)]] | alt | 251 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +18.3) | — |
| [[BT-474 (line)]] | alt | 145 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.1) | — |
| [[COLO 205 (line)]] | alt | 164 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +12.8) | — |
| [[H4 (line)]] | wt | 127 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +16.1) | — |
| [[HT-29 (line)]] | alt | 236 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -8.9) |
| [[KATO III (line)]] | alt | 119 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 87.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 163 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +23.7) | — |
| [[RKO (line)]] | wt | 196 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 268 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +23.1) | — |
| [[SW48 (line)]] | wt | 79.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.7) | — |
| [[A-427 (line)]] | wt | 74.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | — |
| [[HCT15 (line)]] | alt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 62.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.6) | — |
| [[NCI-H23 (line)]] | alt | 70.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.9) | — |
| [[SW 1088 (line)]] | alt | 143 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 82.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.2) | — |
| [[SW480 (line)]] | alt | 74.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +15.8) | — |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C21orf91]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LSMEM1]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TEX14]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[HLA-E]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ATF3]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[LINC00910]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[RNF103-CHMP3]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[MKLN1-AS]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[HCP5]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[TENT5C]] | +0.55 | +0.62 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[ABCA10]] | +0.54 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[MED29]] | +0.54 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*69 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B]] | -0.67 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[EMC8]] | -0.65 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[NDUFS6]] | -0.65 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[NUP93]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[HIRA]] | -0.62 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[GTF3C2]] | -0.61 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[PPIH]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[DGCR8]] | -0.61 | -0.62 / -0.55 | both halves | 1e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[PCGF6]] | -0.61 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[PELP1]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | -0.60 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[XPO4]] | -0.60 | -0.66 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **-** arm (projection on the module's main direction -0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-10.9, -17.8); signed map (5.5, 16.9). **Vector** length 118, 40.8% of its response variance represented; |z| ≥ 3 in 1,222 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.4 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +6.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.9 | +5.8 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +6.0 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.8 | +1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.8 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.3 | +5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | +5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.1 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | syndecan binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:58,552,924-58,582,859 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SYCL, MDA-9, SDCBP1 |
| Gene groups (HGNC) | PDZ domain containing |
| Hallmark sets | DNA_REPAIR, HEME_METABOLISM |
| Reactome | 12 pathways, smallest: Neurofascin interactions; Ephrin signaling; RIPK1-mediated regulated necrosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O00560](https://www.uniprot.org/uniprotkb/O00560) (Syntenin-1):

> Multifunctional adapter protein involved in diverse array of functions including trafficking of transmembrane proteins, neuro and immunomodulation, exosome biogenesis, and tumorigenesis. Positively regulates TGFB1-mediated SMAD2/3 activation and TGFB1-induced epithelial-to-mesenchymal transition (EMT) and cell migration in various cell types. May increase TGFB1 signaling by enhancing cell-surface expression of TGFR1 by preventing the interaction between TGFR1 and CAV1 and subsequent …

**Summary**, from NCBI Gene [6386](https://www.ncbi.nlm.nih.gov/gene/6386):

> The protein encoded by this gene was initially identified as a molecule linking syndecan-mediated signaling to the cytoskeleton. The syntenin protein contains tandemly repeated PDZ domains that bind the cytoplasmic, C-terminal domains of a variety of transmembrane proteins. This protein may also affect cytoskeletal-membrane organization, cell adhesion, protein trafficking, and the activation of transcription factors. The protein is primarily localized to membrane-associated adherens junctions …

**Accessions** — [HGNC:10662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10662) · Entrez [6386](https://www.ncbi.nlm.nih.gov/gene/6386) · UniProt [O00560](https://www.uniprot.org/uniprotkb/O00560) · Ensembl [ENSG00000137575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137575)

## Data

Gene col 6039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6039); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6039]; `tensor/DDL_lfc|DDL_z.npy` [6039]; `embed/gene_vectors.npy` [6039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6039 or target_col == 6039). Every well: [[SDCBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDCBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
