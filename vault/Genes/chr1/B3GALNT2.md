---
symbol: "B3GALNT2"
type: "gene"
col: 8593
ensembl_id: "ENSG00000162885"
name: "beta-1,3-N-acetylgalactosaminyltransferase 2"
location: "1q42.3"
module: 52
arm: "-"
pooled_cpm: 67.45
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 1
n_dd_up_clean: 31
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# B3GALNT2

*beta-1,3-N-acetylgalactosaminyltransferase 2* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.68× (z +52.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 0.784× (z -5.2, q 9e-05, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.177×, Hs 766T 0.219×, AN3 CA 0.254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.135×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DGKE]] (+0.58, fdr 1e-05), [[ME2]] (+0.56, fdr 1e-05), [[SAP30L-AS1]] (+0.55, fdr 2e-04); moves opposite to [[DIABLO]] (-0.58, fdr 6e-05), [[PRPF3]] (-0.55, fdr 2e-04), [[SMIM8]] (-0.54, fdr 3e-04).
> It sits in the **-** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MFAP3L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.68×** | +52.7 | 0e+00 | 46/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +27.3 | 0e+00 | 48/49 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.14×** | +24.6 | 0e+00 | 45/48 (SHP-77, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.11×** | +24.3 | 0e+00 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.86×** | +22.5 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.60×** | +20.5 | 0e+00 | 44/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.65×** | +20.1 | 0e+00 | 43/48 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.45×** | +19.2 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.32×** | +18.0 | 0e+00 | 47/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.22×** | +17.1 | 0e+00 | 47/48 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +16.6 | 0e+00 | 44/47 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.15×** | +16.4 | 0e+00 | 46/48 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +15.0 | 0e+00 | 44/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.83×** | +12.9 | 2e-36 | 47/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.5 | 4e-29 | 40/50 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +10.9 | 3e-26 | 39/47 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +9.5 | 9e-20 | 35/48 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +9.3 | 7e-19 | 36/48 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +8.9 | 1e-17 | 40/47 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8593.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SK-MEL-2 0.177×, Hs 766T 0.219×, AN3 CA 0.254×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.135×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **0.784×** | -5.2 | 9e-05 | 24/48 (A549, LS 180, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 5 µM |  | 0.895× | -3.4 | 0.16 | 10/48 (hTERT-HPNE, A498, …) | top dose only |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.898× | -3.3 | 0.16 | 4/49 (C-33 A, HOP62, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.864× | -3.2 | 0.16 | 9/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.865× | -3.2 | 0.16 | 10/48 (Panc 03.27, HEC-1-A, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.865× | -3.1 | 0.16 | 10/48 (SK-MEL-2, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 117 | 21 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 70.6× (z +41.1) | — |
| [[SW480 (line)]] | alt | 97.8 | 18 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +54.0) | — |
| [[HOP62 (line)]] | alt | 33.9 | 14 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +20.2) | — |
| [[LS 180 (line)]] | wt | 96.7 | 13 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +39.2) | — |
| [[LoVo (line)]] | wt | 64.2 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +26.4) | — |
| [[LOX-IMVI (line)]] | wt | 58.0 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +33.3) | — |
| [[A498 (line)]] | wt | 66.1 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +41.2) | — |
| [[H4 (line)]] | wt | 53.2 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +27.4) | — |
| [[HEC-1-A (line)]] | alt | 52.2 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +24.0) | — |
| [[A-172 (line)]] | wt | 53.9 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +26.9) | — |
| [[CFPAC-1 (line)]] | alt | 36.9 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +21.9) | — |
| [[COLO 205 (line)]] | alt | 29.9 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 47.0× (z +31.6) | — |
| [[NCI-H1573 (line)]] | alt | 45.8 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +34.6) | — |
| [[SW 900 (line)]] | alt | 90.2 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +33.8) | — |
| [[BT-474 (line)]] | alt | 66.6 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.3) | — |
| [[SW1417 (line)]] | alt | 118 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +48.6) | — |
| [[AsPC-1 (line)]] | alt | 75.9 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +28.3) | — |
| [[C32 (line)]] | wt | 49.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +35.6) | — |
| [[Hs 766T (line)]] | wt | 61.9 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +26.0) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[NCI-H2347 (line)]] | alt | 71.2 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +25.1) | — |
| [[SNU-423 (line)]] | alt | 46.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +16.0) | — |
| [[PANC-1 (line)]] | alt | 83.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +31.4) | — |
| [[SW48 (line)]] | wt | 95.3 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +23.5) | — |
| [[A-427 (line)]] | wt | 55.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +21.9) | — |
| [[HT-29 (line)]] | alt | 54.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +18.8) | — |
| [[SK-MEL-2 (line)]] | alt | 60.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[J82 (line)]] | alt | 45.1 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +26.9) | — |
| [[Panc 03.27 (line)]] | alt | 58.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +32.0) | — |
| [[RKO (line)]] | wt | 72.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 37.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +25.4) | — |
| [[A549 (line)]] | wt | 66.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +31.7) | — |
| [[HCT15 (line)]] | alt | 59.5 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.01× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.4) | — |
| [[KATO III (line)]] | alt | 32.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +23.4) | — |
| [[NCI-H1792 (line)]] | alt | 53.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +18.9) | — |
| [[NCI-H23 (line)]] | alt | 48.0 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.32× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 103 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[HepG2_C3A (line)]] | wt | 44.8 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.09× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 137 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +19.0) | — |
| [[C-33 A (line)]] | alt | 109 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.13× (z +14.8) | — |
| [[HS-578T (line)]] | alt | 31.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +16.3) | — |
| [[hTERT-HPNE (line)]] | wt | 36.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 43.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +32.7) | — |
| [[SNU-1 (line)]] | wt | 92.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.8) | — |
| [[CHP-212 (line)]] | wt | 94.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.94× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 74.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.9× (z +24.2) | — |
| [[NCI-H2122 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKE]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ME2]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | +0.55 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[MEMO1]] | +0.54 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[DUSP22]] | +0.52 | +0.38 / +0.37 | both halves | 9e-05 |  |
| [[ANKRD10]] | +0.51 | +0.51 / +0.32 | both halves | 2e-04 |  |
| [[GLRX3]] | +0.51 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[KTN1-AS1]] | +0.50 | +0.52 / +0.30 | both halves | 2e-04 |  |
| [[PPP2R2D]] | +0.50 | +0.32 / +0.37 | both halves | 2e-04 |  |
| [[SEL1L3]] | +0.49 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[UBE2Q2]] | +0.49 | +0.26 / +0.34 | both halves | 4e-04 |  |
| [[GARS1-DT]] | +0.48 | +0.35 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIABLO]] | -0.58 | -0.68 / -0.39 | both halves | 6e-05 |  |
| [[PRPF3]] | -0.55 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[SMIM8]] | -0.54 | -0.45 / -0.26 | both halves | 3e-04 |  |
| [[PRPF6]] | -0.53 | -0.53 / -0.29 | both halves | 3e-04 |  |
| [[RNF40]] | -0.53 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[ZNF136]] | -0.52 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ZNF350]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[SDE2]] | -0.50 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[ZNF414]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[ARFIP1]] | -0.50 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[ZNF548]] | -0.50 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[SRP68]] | -0.49 | -0.51 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFAP3L]] | B | MFAP3L activity raises B3GALNT2's level | lines that do not express MFAP3L (9) vs lines expressing it (41) | 1.47× lower at baseline in the lines without MFAP3L | 0.033 | ⚠ within organs, on part of the lines; also absent: CRACD, FILIP1, TSPAN33; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers B3GALNT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCTD15]] | B | KCTD15 activity raises B3GALNT2's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without KCTD15 | 0.075 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.230). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-34.9, -5.7); signed map (9.1, -2.4). **Vector** length 65.4, 16.7% of its response variance represented; |z| ≥ 3 in 1,638 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +24.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +16.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.9 | +15.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +7.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.3 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.2 | +12.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.2 | +16.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -5.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -0.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,3-N-acetylgalactosaminyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:235,447,190-235,504,452 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39558 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 3 pathways, smallest: DAG1 core M3 glycosylations; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCR0](https://www.uniprot.org/uniprotkb/Q8NCR0) (UDP-GalNAc:beta-1,3-N-acetylgalactosaminyltransferase 2):

> Beta-1,3-N-acetylgalactosaminyltransferase that synthesizes a unique carbohydrate structure, GalNAc-beta-1-3GlcNAc, on N- and O-glycans. Has no galactose nor galactosaminyl transferase activity toward any acceptor substrate. Involved in alpha-dystroglycan (DAG1) glycosylation: acts coordinately with GTDC2/POMGnT2 to synthesize a GalNAc-beta3-GlcNAc-beta-terminus at the 4-position of protein O-mannose in the biosynthesis of the phosphorylated O-mannosyl trisaccharide …

**Summary**, from NCBI Gene [148789](https://www.ncbi.nlm.nih.gov/gene/148789):

> This gene encodes a member of the glycosyltransferase 31 family. The encoded protein synthesizes GalNAc:beta-1,3GlcNAc, a novel carbohydrate structure, on N- and O-glycans. Alternatively spliced transcript variants that encode different isoforms have been described. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:28596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28596) · Entrez [148789](https://www.ncbi.nlm.nih.gov/gene/148789) · UniProt [Q8NCR0](https://www.uniprot.org/uniprotkb/Q8NCR0) · Ensembl [ENSG00000162885](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162885)

## Data

Gene col 8593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8593); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8593]; `tensor/DDL_lfc|DDL_z.npy` [8593]; `embed/gene_vectors.npy` [8593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8593 or target_col == 8593). Every well: [[B3GALNT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GALNT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
