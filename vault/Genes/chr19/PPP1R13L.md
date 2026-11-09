---
symbol: "PPP1R13L"
type: "gene"
col: 2514
ensembl_id: "ENSG00000104881"
name: "protein phosphatase 1 regulatory subunit 13 like"
location: "19q13.32"
module: 25
arm: "-"
pooled_cpm: 68.46
n_lines_expressing: 45
n_dd_up: 4
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PPP1R13L

*protein phosphatase 1 regulatory subunit 13 like* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.21× (z +5.2, q 1e-04, up in 16 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.498× (z -13.3, q 9e-38, down in 39 of 43 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.646× (z -11.8, q 1e-29, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELL]] (+0.66, fdr 7e-06), [[RGP1]] (+0.62, fdr 1e-05), [[TRIOBP]] (+0.61, fdr 7e-06); moves opposite to [[PDCL3]] (-0.61, fdr 2e-05), [[SMG7]] (-0.59, fdr 1e-05), [[DTWD2]] (-0.59, fdr 7e-06).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ALS2CL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +5.2 | 1e-04 | 16/44 (A-172, HS-578T, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.017 | 21/43 (SW1417, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +3.9 | 0.020 | 16/43 (A-172, SW 900, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.033 | 20/42 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.498×** | -13.3 | 9e-38 | 39/43 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.646×** | -11.8 | 1e-29 | 32/43 (SNU-423, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.544×** | -11.6 | 6e-29 | 39/43 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.591×** | -9.6 | 7e-20 | 25/36 (LS 180, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.580×** | -9.6 | 8e-20 | 27/36 (SK-MEL-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -9.3 | 1e-18 | 31/41 (HOP62, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.622×** | -9.1 | 1e-17 | 35/43 (HOP62, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.652×** | -8.2 | 2e-14 | 27/41 (A-172, NCI-H23, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -7.7 | 1e-12 | 24/42 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.719×** | -6.3 | 2e-08 | 25/43 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.716×** | -6.0 | 8e-08 | 29/43 (HOP62, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -6.0 | 1e-07 | 24/43 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.731×** | -5.7 | 4e-07 | 23/41 (J82, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.742×** | -5.7 | 5e-07 | 25/43 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.744×** | -5.6 | 6e-07 | 27/43 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.762×** | -5.2 | 7e-06 | 25/42 (J82, NCI-H1792, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.839× | -4.7 | 7e-05 | 19/43 (HOP62, J82, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.775×** | -4.7 | 9e-05 | 20/43 (SHP-77, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.785×** | -4.6 | 1e-04 | 20/42 (A-427, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.631×** | -4.6 | 1e-04 | 17/44 (Panc 03.27, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.799×** | -4.3 | 4e-04 | 21/43 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.809×** | -4.0 | 0.001 | 22/43 (HepG2/C3A, AsPC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.688×** | -3.7 | 0.004 | 20/44 (RPMI-7951, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.721×** | -3.3 | 0.021 | 15/42 (SNU-423, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 268 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.288× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 226 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -16.0) |
| [[J82 (line)]] | alt | 92.9 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.426× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 63.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.505× (z -9.0) |
| [[A-172 (line)]] | wt | 55.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 68.1 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.504× (z -10.2) |
| [[HS-578T (line)]] | alt | 94.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 51.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 69.0 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.435× (z -11.7) |
| [[A-427 (line)]] | wt | 49.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0861× (z -22.5) |
| [[HCT15 (line)]] | alt | 153 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 69.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.519× (z -8.8) |
| [[HT-29 (line)]] | alt | 91.4 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Selinexor (drug)]] 5 µM 0.532× (z -10.5) |
| [[SW480 (line)]] | alt | 69.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 59.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.205× (z -11.7) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 26.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.84× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 64.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 45.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.27× (z +11.2) | — |
| [[C32 (line)]] | wt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.05× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 79.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[LS 180 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0708× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 84.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.427× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A498 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELL]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[RGP1]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[TRIOBP]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TPT1-AS1]] | +0.60 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CATSPERG]] | +0.60 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[ADGRL1-AS1]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.57 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MAPK8IP3]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ARHGAP45]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[POLR2J4]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[RABGEF1]] | +0.55 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCL3]] | -0.61 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SMG7]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[DTWD2]] | -0.59 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[MRPL19]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[PYURF]] | -0.55 | -0.62 / -0.46 | both halves | 2e-05 |  |
| [[RAD23B]] | -0.55 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[TSPAN6]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[FECH]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[DLD]] | -0.55 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[TRUB1]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[DHX9]] | -0.54 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[PAIP1]] | -0.54 | -0.56 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALS2CL]] | B | ALS2CL activity raises PPP1R13L's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.62× lower at baseline in the lines without ALS2CL | 0.003 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[UNC13D]] | B | UNC13D activity raises PPP1R13L's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 1.56× lower at baseline in the lines without UNC13D | 0.092 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.1, -16.4); signed map (-0.5, 29.1). **Vector** length 108, 29.3% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | -1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +3.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.0 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.6 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.5 | -11.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.7 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -9.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.2 | -4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 13 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,379,638-45,406,349 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAI, IASPP |
| Gene groups (HGNC) | Ankyrin repeat domain containing; SH3 domain containing |
| Reactome | 3 pathways, smallest: Regulation of TP53 Activity through Association with Co-factors; Regulation of TP53 Activity; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUF5](https://www.uniprot.org/uniprotkb/Q8WUF5) (RelA-associated inhibitor):

> Regulator that plays a central role in regulation of apoptosis and transcription via its interaction with NF-kappa-B and p53/TP53 proteins. Blocks transcription of HIV-1 virus by inhibiting the action of both NF-kappa-B and SP1. Also inhibits p53/TP53 function, possibly by preventing the association between p53/TP53 and ASPP1 or ASPP2, and therefore suppressing the subsequent activation of apoptosis. Is involved in NF-kappa-B dependent negative regulation of inflammatory response.

**Summary**, from NCBI Gene [10848](https://www.ncbi.nlm.nih.gov/gene/10848):

> IASPP is one of the most evolutionarily conserved inhibitors of p53 (TP53; MIM 191170), whereas ASPP1 (MIM 606455) and ASPP2 (MIM 602143) are activators of p53.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18838) · Entrez [10848](https://www.ncbi.nlm.nih.gov/gene/10848) · UniProt [Q8WUF5](https://www.uniprot.org/uniprotkb/Q8WUF5) · Ensembl [ENSG00000104881](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104881)

## Data

Gene col 2514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2514); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2514]; `tensor/DDL_lfc|DDL_z.npy` [2514]; `embed/gene_vectors.npy` [2514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2514 or target_col == 2514). Every well: [[PPP1R13L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R13L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
