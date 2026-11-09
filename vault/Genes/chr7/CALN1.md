---
symbol: "CALN1"
type: "gene"
col: 11377
ensembl_id: "ENSG00000183166"
name: "calneuron 1"
location: "7q11.22"
module: 191
arm: "+"
pooled_cpm: 12.99
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 12
n_dd_up_clean: 21
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/191"]
generated_by: "tahoemap"
---

# CALN1

*calneuron 1* — 7q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 12.1× (z +42.8, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.485× (z -12.4, q 2e-32, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00624]] (+0.73, fdr 1e-05), [[GNG7]] (+0.69, fdr 7e-06), [[COL26A1]] (+0.60, fdr 7e-06); moves opposite to [[TOR3A]] (-0.58, fdr 4e-05), [[DBR1]] (-0.56, fdr 7e-04, ⚠ one half only (not replicated)), [[PCNA]] (-0.51, fdr 3e-04), [[PANK1]] (-0.51, fdr 2e-04).
> It is in [[Module 191]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00595]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **12.1×** | +42.8 | 0e+00 | 47/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.90×** | +35.5 | 0e+00 | 47/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.47×** | +32.1 | 0e+00 | 47/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.52×** | +30.6 | 0e+00 | 33/45 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.77×** | +22.8 | 0e+00 | 42/47 (SW480, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +18.0 | 0e+00 | 14/19 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +17.7 | 0e+00 | 40/48 (SW480, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.40×** | +15.0 | 0e+00 | 39/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +14.9 | 0e+00 | 31/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +14.8 | 0e+00 | 27/37 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +13.2 | 4e-38 | 30/46 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +12.1 | 3e-32 | 27/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.09×** | +10.2 | 1e-22 | 31/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +8.5 | 5e-16 | 17/31 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.61×** | +8.2 | 6e-15 | 23/47 (RKO, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +7.3 | 1e-11 | 23/46 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.98×** | +6.1 | 2e-08 | 13/44 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 1e-07 | 14/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.485×** | -12.4 | 2e-32 | 31/47 (C32, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.545×** | -10.0 | 4e-21 | 25/42 (NCI-H23, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.879× | -7.4 | 2e-11 | 16/48 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.716×** | -5.7 | 2e-06 | 17/47 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -4.6 | 4e-04 | 18/45 (LoVo, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.773×** | -4.2 | 0.002 | 7/47 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -4.0 | 0.004 | 6/47 (COLO 205, LoVo, …) | top dose only | plate-row cell shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.779×** | -3.9 | 0.005 | 16/44 (hTERT-HPNE, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.794×** | -3.9 | 0.005 | 17/47 (C32, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | 0.851× | -3.9 | 0.006 | 7/48 (HOP62, LoVo, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.853× | -3.8 | 0.007 | 11/48 (CHP-212, C-33 A, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.803×** | -3.5 | 0.019 | 13/47 (C32, AN3 CA, …) | inconsistent across doses |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.025 | 6/48 (SW 1088, PANC-1, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.040 | 5/47 (NCI-H661, AN3 CA, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.832×** | -3.1 | 0.068 | 10/46 (NCI-H1792, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 366 | 6 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 34.8× (z +29.3) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -15.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 14.3 | 8 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +20.1) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.264× (z -8.6) |
| [[SW480 (line)]] | alt | 14.5 | 8 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 109× (z +33.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.244× (z -9.7) ⚠ toxic |
| [[C32 (line)]] | wt | 26.5 | 2 | 6 (5 ⚠) | [[Auranofin (drug)]] 5 µM 17.4× (z +15.8) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.102× (z -12.6) |
| [[LoVo (line)]] | wt | 21.7 | 5 (1 ⚠) | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.5× (z +18.7) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.278× (z -9.8) |
| [[A549 (line)]] | wt | 6.88 | 6 | 1 | [[Panobinostat (drug)]] 5 µM 108× (z +18.4) | [[Monocrotaline (drug)]] 0.05 µM 0.0859× (z -8.9) |
| [[KATO III (line)]] | alt | 12.9 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 25.1× (z +16.0) | — |
| [[NCI-H460 (line)]] | wt | 4.12 | 7 | 0 | [[Auranofin (drug)]] 5 µM 21.0× (z +14.2) | — |
| [[PANC-1 (line)]] | alt | 6.68 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.22× (z +18.8) | — |
| [[A-172 (line)]] | wt | 4.11 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 31.5× (z +12.0) | [[Vortioxetine (drug)]] 5 µM 0.0807× (z -8.7) ⚠ toxic |
| [[A498 (line)]] | wt | 8.16 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 41.4× (z +21.4) | — |
| [[HS-578T (line)]] | alt | 12.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 37.1× (z +17.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 17.2× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 22.0 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 74.3× (z +17.8) | — |
| [[SW1417 (line)]] | alt | 12.7 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 71.3× (z +19.6) | — |
| [[SW48 (line)]] | wt | 27.3 | 2 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 25.6× (z +14.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0718× (z -11.6) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.140× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 7.66 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 13.8× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -9.8) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 5.97 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.06× (z +13.4) | — |
| [[HT-29 (line)]] | alt | 6.93 | 3 | 0 | [[Auranofin (drug)]] 5 µM 42.0× (z +16.3) | — |
| [[LS 180 (line)]] | wt | 11.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.04× (z +11.2) | — |
| [[A-427 (line)]] | wt | 6.71 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.80× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 10.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.0× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 4.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 9.66 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 19.1× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 7.18 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.08× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0630× (z -13.9) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 3.37 | 2 | 0 | [[Auranofin (drug)]] 5 µM 22.6× (z +12.7) | — |
| [[RKO (line)]] | wt | 13.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 10.9× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 11.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.42× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 4.75 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 3.58 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.4× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 6.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 18.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.28× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 4.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 4.45 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 15.6× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 5.30 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.8× (z +9.6) | — |
| [[SNU-1 (line)]] | wt | 15.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.99× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 6.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00624]] | +0.73 | +0.55 / +0.77 | both halves | 1e-05 | **novel candidate** |
| [[GNG7]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[COL26A1]] | +0.60 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[HULC]] | +0.59 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.56 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[CCDC144NL-1]] | +0.56 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[LINC00243]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[LINC02885]] | +0.55 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[SYN3]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[KCNAB1]] | +0.53 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[DNAH3]] | +0.53 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.53 | +0.39 / +0.65 | both halves | 5e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR3A]] | -0.58 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[DBR1]] | -0.56 | -0.20 / -0.58 | ⚠ one half (not replicated) | 7e-04 |  |
| [[PCNA]] | -0.51 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[PANK1]] | -0.51 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[MCM9]] | -0.48 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[ASH2L]] | -0.48 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[ZDHHC5]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[LIN9]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[MFSD14A]] | -0.45 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[CASP8AP2]] | -0.45 | -0.16 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[ZNF142]] | -0.44 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[ANKFY1]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[MFSD5]] | -0.44 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[WBP11]] | -0.43 | -0.22 / -0.43 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00595]] | B | LINC00595 activity raises CALN1's level | lines that do not express LINC00595 (9) vs lines expressing it (41) | 1.70× lower at baseline in the lines without LINC00595 | 0.065 | ⚠ within organs, on part of the lines; also absent: SUSD4, EBF4, SLC17A7; maybe low, not absent |
| [[PRKN]] | B | PRKN activity raises CALN1's level | lines that do not express PRKN (8) vs lines expressing it (42) | 2.10× lower at baseline in the lines without PRKN | 0.067 | ⚠ within organs, on part of the lines; also absent: GREB1, SLC17A7, ITGA10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 191]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.7, 34.3); signed map (26.7, 17.0). **Vector** length 73.3, 13.8% of its response variance represented; |z| ≥ 3 in 1,307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +22.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +14.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +30.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +17.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +18.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.4 | -12.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -3.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.7 | -4.0 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | calneuron 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.22 — chr7:71,779,491-72,447,151 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CABP8 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXU9](https://www.uniprot.org/uniprotkb/Q9BXU9) (Calcium-binding protein 8):

> Negatively regulates Golgi-to-plasma membrane trafficking by interacting with PI4KB and inhibiting its activity. May play a role in the physiology of neurons and is potentially important in memory and learning.

**Summary**, from NCBI Gene [83698](https://www.ncbi.nlm.nih.gov/gene/83698):

> This gene encodes a protein with high similarity to the calcium-binding proteins of the calmodulin family. The encoded protein contains two EF-hand domains and potential calcium-binding sites. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13248) · Entrez [83698](https://www.ncbi.nlm.nih.gov/gene/83698) · UniProt [Q9BXU9](https://www.uniprot.org/uniprotkb/Q9BXU9) · Ensembl [ENSG00000183166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183166)

## Data

Gene col 11377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11377); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11377]; `tensor/DDL_lfc|DDL_z.npy` [11377]; `embed/gene_vectors.npy` [11377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11377 or target_col == 11377). Every well: [[CALN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CALN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
