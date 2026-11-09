---
symbol: "SORBS1"
type: "gene"
col: 1751
ensembl_id: "ENSG00000095637"
name: "sorbin and SH3 domain containing 1"
location: "10q24.1"
module: 60
arm: "+"
pooled_cpm: 47.92
n_lines_expressing: 44
n_dd_up: 31
n_dd_down: 9
n_dd_up_clean: 28
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# SORBS1

*sorbin and SH3 domain containing 1* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 8.33× (z +40.3, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.440× (z -8.1, q 2e-13, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SESN3]] (+0.58, fdr 3e-05), [[PCSK5]] (+0.57, fdr 1e-05), [[ABHD3]] (+0.55, fdr 1e-05); moves opposite to [[FAM120C]] (-0.54, fdr 4e-05), [[NAF1]] (-0.49, fdr 3e-05), [[UTP15]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **8.33×** | +40.3 | 0e+00 | 41/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.52×** | +38.4 | 0e+00 | 41/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.30×** | +37.8 | 0e+00 | 40/41 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.85×** | +28.1 | 0e+00 | 33/41 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.23×** | +27.4 | 0e+00 | 40/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +27.4 | 0e+00 | 31/43 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.71×** | +26.8 | 0e+00 | 40/42 (HT-29, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.79×** | +25.3 | 0e+00 | 38/41 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.09×** | +20.3 | 0e+00 | 38/42 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.69×** | +18.8 | 0e+00 | 37/42 (A498, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.74×** | +15.5 | 0e+00 | 32/36 (A-427, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.23×** | +15.3 | 0e+00 | 36/41 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **3.07×** | +15.2 | 0e+00 | 37/43 (A498, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **4.07×** | +14.0 | 9e-43 | 38/43 (PANC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.89×** | +12.1 | 4e-32 | 34/41 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +12.0 | 1e-31 | 26/41 (A-172, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1751.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -8.1 | 2e-13 | 25/43 (COLO 205, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.711×** | -6.5 | 3e-08 | 24/38 (KATO III, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -6.4 | 3e-08 | 21/34 (KATO III, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.770×** | -5.0 | 1e-04 | 21/41 (SW 900, LS 180, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -4.6 | 5e-04 | 17/39 (COLO 205, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.806×** | -3.9 | 0.007 | 16/39 (COLO 205, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.799×** | -3.9 | 0.007 | 14/40 (RKO, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.815×** | -3.9 | 0.008 | 19/42 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.8 | 0.010 | 14/42 (SK-MEL-2, A-172, …) | rises with dose | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.706×** | -3.4 | 0.032 | 8/40 (A-427, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.844× | -3.2 | 0.070 | 9/40 (A-427, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.846× | -3.2 | 0.072 | 13/42 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.801× | -3.0 | 0.12 | 4/42 (PANC-1, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 47.3 | 18 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +21.0) | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 42.2 | 8 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 8.25× (z +20.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.279× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.282× (z -12.6) |
| [[A498 (line)]] | wt | 25.3 | 12 | 0 | [[Panobinostat (drug)]] 5 µM 14.6× (z +22.3) | — |
| [[HEC-1-A (line)]] | alt | 21.3 | 12 | 0 | [[Panobinostat (drug)]] 5 µM 10.3× (z +17.1) | — |
| [[HT-29 (line)]] | alt | 23.9 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +18.4) | — |
| [[LS 180 (line)]] | wt | 52.6 | 11 | 0 | [[Panobinostat (drug)]] 5 µM 7.24× (z +14.4) | — |
| [[A-172 (line)]] | wt | 23.0 | 10 | 0 | [[Panobinostat (drug)]] 5 µM 11.7× (z +15.3) | — |
| [[A549 (line)]] | wt | 16.9 | 10 | 0 | [[Panobinostat (drug)]] 5 µM 20.5× (z +17.4) | — |
| [[J82 (line)]] | alt | 14.5 | 10 | 0 | [[Panobinostat (drug)]] 5 µM 21.2× (z +18.2) | — |
| [[KATO III (line)]] | alt | 52.0 | 8 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.60× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.0863× (z -18.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 27.2 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.58× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 12.0 | 9 | 1 | [[Panobinostat (drug)]] 5 µM 18.6× (z +12.5) | [[Harringtonine (drug)]] 0.05 µM 0.0902× (z -9.6) |
| [[H4 (line)]] | wt | 20.2 | 7 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 18.4× (z +12.7) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.127× (z -9.0) |
| [[A-427 (line)]] | wt | 64.8 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.62× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -17.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 612 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -17.6) |
| [[NCI-H1573 (line)]] | alt | 16.5 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 15.2× (z +16.2) | — |
| [[SK-MEL-2 (line)]] | alt | 62.6 | 6 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 7.05× (z +15.6) | [[Harringtonine (drug)]] 0.5 µM 0.334× (z -8.8) ⚠ cell-cycle shift, explains ~3% of this change |
| [[SNU-423 (line)]] | alt | 17.1 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 22.9× (z +17.6) | — |
| [[LOX-IMVI (line)]] | wt | 18.9 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 15.1× (z +16.4) | — |
| [[SW 900 (line)]] | alt | 35.8 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.22× (z +13.6) | [[Sunitinib (drug)]] 5 µM 0.248× (z -8.5) ⚠ toxic |
| [[SW1417 (line)]] | alt | 172 | 6 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.14× (z +15.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.261× (z -12.5) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 39.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 27.9 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +17.4) | [[Dexamethasone (drug)]] 0.5 µM 0.211× (z -9.6) |
| [[HS-578T (line)]] | alt | 17.0 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 11.6× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 31.1 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 6.65× (z +15.1) | [[Digitoxin (drug)]] 5 µM 0.210× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 21.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 7.60× (z +13.8) | — |
| [[NCI-H2347 (line)]] | alt | 40.7 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.96× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 58.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.45× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 142 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +12.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.332× (z -11.0) ⚠ toxic |
| [[BT-474 (line)]] | alt | 16.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 14.0× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 40.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.84× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 214 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.37× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -9.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 22.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.54× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 15.8× (z +11.9) | — |
| [[C32 (line)]] | wt | 102 | 1 | 2 (2 ⚠) | [[Cobimetinib (drug)]] 0.5 µM 3.40× (z +9.6) | [[Harringtonine (drug)]] 0.5 µM 0.326× (z -8.9) ⚠ cell-cycle shift, explains ~3% of this change |
| [[SW48 (line)]] | wt | 34.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.28× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 45.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.80× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 30.5 | 0 | 1 | — | [[Belumosudil (drug)]] 0.05 µM 0.0455× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.73 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SESN3]] | +0.58 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[PCSK5]] | +0.57 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ABHD3]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CLU]] | +0.55 | +0.48 / +0.63 | both halves | 2e-05 | pathway: HALLMARK_MYOGENESIS |
| [[ABAT]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SH3KBP1]] | +0.54 | +0.33 / +0.51 | both halves | 1e-04 | same gene group |
| [[VASH2]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[STXBP5L]] | +0.52 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[HSPA1B]] | +0.51 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[NRIP3]] | +0.51 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[UBB]] | +0.51 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SAT1]] | +0.51 | +0.25 / +0.55 | both halves | 4e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM120C]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[NAF1]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[UTP15]] | -0.49 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[TXNRD3]] | -0.48 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[SCO1]] | -0.46 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[ZNF252P]] | -0.46 | -0.24 / -0.45 | both halves | 4e-04 |  |
| [[TMEM128]] | -0.46 | -0.21 / -0.50 | both halves | 7e-04 |  |
| [[LATS1]] | -0.46 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[ARMC8]] | -0.45 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[TEX22]] | -0.45 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[C1orf109]] | -0.45 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[MTPAP]] | -0.45 | -0.29 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SORBS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.469). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.0, 9.9); signed map (-11.4, 32.4). **Vector** length 105, 28.3% of its response variance represented; |z| ≥ 3 in 1,654 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.7 | +26.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.6 | +25.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.6 | +20.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.7 | +15.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.6 | +15.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +18.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +12.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +6.0 | +15.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +5.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -3.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.7 | -3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | sorbin and SH3 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:95,311,771-95,561,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12406, CAP, sh3p12, ponsin, KIAA1296; previously SH3D5 |
| Gene groups (HGNC) | SH3 domain containing |
| Hallmark sets | MYOGENESIS, ADIPOGENESIS |
| Reactome | 2 pathways, smallest: Smooth Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BX66](https://www.uniprot.org/uniprotkb/Q9BX66) (Sorbin and SH3 domain-containing protein 1):

> Plays a role in tyrosine phosphorylation of CBL by linking CBL to the insulin receptor. Required for insulin-stimulated glucose transport. Involved in formation of actin stress fibers and focal adhesions (By similarity).

**Summary**, from NCBI Gene [10580](https://www.ncbi.nlm.nih.gov/gene/10580):

> This gene encodes a CBL-associated protein which functions in the signaling and stimulation of insulin. Mutations in this gene may be associated with human disorders of insulin resistance. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:14565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14565) · Entrez [10580](https://www.ncbi.nlm.nih.gov/gene/10580) · UniProt [Q9BX66](https://www.uniprot.org/uniprotkb/Q9BX66) · Ensembl [ENSG00000095637](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095637)

## Data

Gene col 1751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1751); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1751]; `tensor/DDL_lfc|DDL_z.npy` [1751]; `embed/gene_vectors.npy` [1751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1751 or target_col == 1751). Every well: [[SORBS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SORBS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
