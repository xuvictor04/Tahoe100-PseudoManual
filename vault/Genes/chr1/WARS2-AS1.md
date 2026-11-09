---
symbol: "WARS2-AS1"
type: "gene"
col: 13793
ensembl_id: "ENSG00000231365"
name: "WARS2 antisense RNA 1"
location: "1p12"
module: 88
arm: "+"
pooled_cpm: 48.25
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 23
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# WARS2-AS1

*WARS2 antisense RNA 1* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +11.3, q 5e-27, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.408× (z -10.0, q 5e-21, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFX3-DT]] (+0.87, fdr 1e-05), [[ST7L]] (+0.85, fdr 7e-06), [[IQCH-AS1]] (+0.82, fdr 2e-05); moves opposite to [[HACE1]] (-0.75, fdr 1e-05), [[WASF3]] (-0.74, fdr 3e-05), [[SLC9A6]] (-0.74, fdr 1e-05).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PLEKHH2]] → it (grade B ⚠); 23 go from it, the strongest it → [[MBOAT2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13793.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +11.3 | 5e-27 | 38/45 (BT-474, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +11.2 | 2e-26 | 40/44 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +6.4 | 3e-08 | 36/44 (C32, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.9 | 7e-07 | 38/45 (J82, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +5.6 | 2e-06 | 32/44 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.51×** | +4.6 | 4e-04 | 31/45 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.007 | 26/45 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.008 | 23/44 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.041 | 22/45 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.056 | 19/45 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.056 | 22/44 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.065 | 23/45 (HT-29, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +3.1 | 0.081 | 21/45 (CHP-212, H4, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.086 | 19/45 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13793.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.408×** | -10.0 | 5e-21 | 39/45 (MIA PaCa-2, HCT15, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.484×** | -8.1 | 1e-13 | 40/45 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.518×** | -7.4 | 3e-11 | 32/45 (HCT15, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.525×** | -7.2 | 8e-11 | 40/45 (HCT15, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.561×** | -6.5 | 1e-08 | 36/45 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.378×** | -5.7 | 1e-06 | 34/46 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -4.2 | 0.002 | 26/45 (SW480, HCT15, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.492×** | -4.2 | 0.002 | 20/32 (HT-29, H4, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -3.9 | 0.007 | 23/44 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.521×** | -3.8 | 0.007 | 26/45 (HCT15, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.713×** | -3.8 | 0.008 | 23/45 (SK-MEL-2, SHP-77, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.664×** | -3.7 | 0.008 | 27/45 (SK-MEL-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -3.2 | 0.057 | 22/44 (HCT15, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -3.1 | 0.076 | 21/45 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.751×** | -3.1 | 0.076 | 19/44 (PANC-1, HepG2/C3A, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.826×** | -3.0 | 0.090 | 18/45 (HT-29, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 89.7 | 1 | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.189× (z -12.9) |
| [[SW480 (line)]] | alt | 75.1 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.290× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.324× (z -11.1) |
| [[PANC-1 (line)]] | alt | 30.3 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.238× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.327× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.395× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 56.8 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.7) | [[Belinostat (drug)]] 5 µM 0.306× (z -10.7) |
| [[LoVo (line)]] | wt | 63.0 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.339× (z -9.9) |
| [[C32 (line)]] | wt | 23.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +14.9) | — |
| [[KATO III (line)]] | alt | 67.4 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.368× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 69.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.172× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 112 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.5) | [[Ixazomib citrate (drug)]] 5 µM 0.288× (z -10.0) |
| [[H4 (line)]] | wt | 68.7 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.157× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 120 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +11.9) | [[Belinostat (drug)]] 5 µM 0.300× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +11.5) | — |
| [[J82 (line)]] | alt | 43.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +15.2) | — |
| [[Panc 03.27 (line)]] | alt | 36.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 34.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -9.4) |
| [[SNU-1 (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.248× (z -8.9) |
| [[A-427 (line)]] | wt | 25.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.329× (z -11.6) |
| [[BT-474 (line)]] | alt | 35.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.95× (z +16.9) | — |
| [[CFPAC-1 (line)]] | alt | 53.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 52.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0934× (z -10.6) |
| [[HOP62 (line)]] | alt | 32.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 42.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 50.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 56.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 35.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.334× (z -8.5) |
| [[SNU-423 (line)]] | alt | 47.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +11.5) | — |
| [[A-172 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.58 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFX3-DT]] | +0.87 | +0.87 / +0.52 | both halves | 1e-05 |  |
| [[ST7L]] | +0.85 | +0.87 / +0.58 | both halves | 7e-06 |  |
| [[IQCH-AS1]] | +0.82 | +0.83 / +0.47 | both halves | 2e-05 | same gene group |
| [[PPP3CB-AS1]] | +0.81 | +0.78 / +0.47 | both halves | 2e-05 | same gene group |
| [[PCNX4-DT]] | +0.80 | +0.80 / +0.40 | both halves | 4e-05 |  |
| [[ERCC6L2]] | +0.80 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.80 | +0.84 / +0.34 | both halves | 1e-04 | same gene group |
| [[INO80D]] | +0.80 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.79 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[RBM26-AS1]] | +0.78 | +0.79 / +0.38 | both halves | 6e-05 | same gene group |
| [[RAB30-DT]] | +0.78 | +0.81 / +0.52 | both halves | 1e-05 |  |
| [[MCPH1]] | +0.78 | +0.71 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | -0.75 | -0.74 / -0.50 | both halves | 1e-05 |  |
| [[WASF3]] | -0.74 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[SLC9A6]] | -0.74 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.72 | -0.74 / -0.44 | both halves | 3e-05 |  |
| [[MAST3]] | -0.72 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[POGLUT2]] | -0.72 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[IGSF8]] | -0.71 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[MYPOP]] | -0.71 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[YIF1B]] | -0.70 | -0.65 / -0.20 | both halves | 7e-04 |  |
| [[ANKRD27]] | -0.70 | -0.69 / -0.24 | both halves | 4e-04 |  |
| [[RIMS3]] | -0.69 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ARL6]] | -0.69 | -0.60 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHH2]] | B | PLEKHH2 activity raises WARS2-AS1's level | lines that do not express PLEKHH2 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without PLEKHH2 | 0.030 | ⚠ within organs, on part of the lines; also absent: PDLIM3, ENSG00000259363, AKT3 |
| [[LINC01505]] | B | LINC01505 activity raises WARS2-AS1's level | lines that do not express LINC01505 (5) vs lines expressing it (45) | 2.61× lower at baseline in the lines without LINC01505 | 0.040 | ⚠ within organs, on part of the lines; also absent: EID2, CENPP, ENSG00000223727; maybe low, not absent |
| [[PMFBP1]] | B | PMFBP1 activity raises WARS2-AS1's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without PMFBP1 | 0.045 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises WARS2-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without FSIP2-AS1 | 0.073 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[C19orf18]] | B | C19orf18 activity raises WARS2-AS1's level | lines that do not express C19orf18 (16) vs lines expressing it (34) | 1.16× lower at baseline in the lines without C19orf18 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, ZNF606, ZSCAN18 |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises WARS2-AS1's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without ITPR2-AS1 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MBOAT2]] | C | WARS2-AS1 activity lowers MBOAT2's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 4.58× higher at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[LRGUK]] | C | WARS2-AS1 activity raises LRGUK's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 3.49× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[NEK9]] | C | WARS2-AS1 activity raises NEK9's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[FAM234B]] | C | WARS2-AS1 activity raises FAM234B's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.48× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[SYNGR1]] | C | WARS2-AS1 activity raises SYNGR1's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[TTC27]] | C | WARS2-AS1 activity raises TTC27's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[THADA]] | C | WARS2-AS1 activity raises THADA's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[CARD8]] | C | WARS2-AS1 activity raises CARD8's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[ZBTB40]] | C | WARS2-AS1 activity raises ZBTB40's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.66× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[TRMT13]] | C | WARS2-AS1 activity raises TRMT13's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[TAF5L]] | C | WARS2-AS1 activity lowers TAF5L's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 1.43× higher at baseline in the lines without WARS2-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |
| [[EIF1B-AS1]] | C | WARS2-AS1 activity raises EIF1B-AS1's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.02× lower at baseline in the lines without WARS2-AS1 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.875). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (4.4, 8.7); signed map (18.3, -24.7). **Vector** length 132, 41.6% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.7 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +12.6 | +11.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.3 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +11.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.6 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.4 | -10.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.2 | -8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.0 | -3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.0 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.9 | -7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.3 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.2 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | WARS2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p12 — chr1:119,140,391-119,275,973 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40612](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40612) · Entrez [101929147](https://www.ncbi.nlm.nih.gov/gene/101929147) · Ensembl [ENSG00000231365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231365)

## Data

Gene col 13793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13793); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13793]; `tensor/DDL_lfc|DDL_z.npy` [13793]; `embed/gene_vectors.npy` [13793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13793 or target_col == 13793). Every well: [[WARS2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WARS2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
