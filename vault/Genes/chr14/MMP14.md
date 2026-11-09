---
symbol: "MMP14"
type: "gene"
col: 8055
ensembl_id: "ENSG00000157227"
name: "matrix metallopeptidase 14"
location: "14q11.2"
module: 13
arm: "+"
pooled_cpm: 69.16
n_lines_expressing: 31
n_dd_up: 6
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 23
direction_downstream: 17
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MMP14

*matrix metallopeptidase 14* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.31× (z +11.7, q 1e-28, up in 25 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.49× (z +4.0, q 0.008, up in 15 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 4.08×, LOX-IMVI 3.06×, A-172 2.31×, SW1417 3.32×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 3.74×, LOX-IMVI 3.64×, NCI-H2030 2.47×, COLO 205 4.91×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 9.50×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.174× (z -34.3, q 0e+00, down in 29 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMA4]] (+0.65, fdr 7e-06), [[SCUBE3]] (+0.61, fdr 1e-05), [[COL6A1]] (+0.60, fdr 1e-05); moves opposite to [[TIGD2]] (-0.48, fdr 3e-05), [[BABAM2]] (-0.46, fdr 3e-05), [[TRIM16]] (-0.46, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[MMP1]] → it (grade B ⚠); 17 go from it, the strongest it → [[RAC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8055.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (SNU-423 4.08×, LOX-IMVI 3.06×, A-172 2.31×, SW1417 3.32×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 3.74×, LOX-IMVI 3.64×, NCI-H2030 2.47×, COLO 205 4.91×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 5 µM in 1 line (NCI-H596 9.50×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +11.7 | 1e-28 | 25/28 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +10.5 | 2e-23 | 21/24 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +6.9 | 7e-10 | 18/24 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +6.1 | 2e-07 | 19/28 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.49×** | +4.0 | 0.008 | 15/28 (A498, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.015 | 15/28 (C32, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.38× | +3.2 | 0.10 | 11/29 (LS 180, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | 1.25× | +3.1 | 0.13 | 15/29 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 1 with an alert ⚠; shown: the 15 strongest. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.174×** | -34.3 | 0e+00 | 29/29 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.195×** | -22.7 | 0e+00 | 29/29 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.190×** | -22.1 | 0e+00 | 29/29 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.359×** | -14.2 | 2e-43 | 28/29 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.373×** | -13.7 | 2e-40 | 29/29 (C32, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.375×** | -13.6 | 6e-40 | 28/29 (C32, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.454×** | -10.9 | 8e-26 | 27/29 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.466×** | -10.6 | 3e-24 | 27/29 (H4, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.369×** | -7.2 | 3e-11 | 26/30 (C32, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.609×** | -6.6 | 3e-09 | 22/30 (NCI-H2030, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.633×** | -6.3 | 1e-08 | 23/29 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.680×** | -5.3 | 5e-06 | 21/29 (SK-MEL-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -5.3 | 6e-06 | 22/29 (C32, NCI-H2347, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.709×** | -4.7 | 9e-05 | 15/29 (C32, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.713×** | -4.7 | 1e-04 | 19/28 (CFPAC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 316 | 0 | 16 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0807× (z -37.7) |
| [[HOP62 (line)]] | alt | 216 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0140× (z -47.0) |
| [[SK-MEL-2 (line)]] | alt | 148 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -23.4) |
| [[NCI-H2347 (line)]] | alt | 100 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.0464× (z -44.1) |
| [[H4 (line)]] | wt | 142 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.0819× (z -28.1) |
| [[hTERT-HPNE (line)]] | wt | 297 | 0 | 9 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0241× (z -32.6) |
| [[LOX-IMVI (line)]] | wt | 68.6 | 2 (2 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0732× (z -30.9) |
| [[A498 (line)]] | wt | 140 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -20.5) |
| [[Hs 766T (line)]] | wt | 181 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0643× (z -30.2) |
| [[HS-578T (line)]] | alt | 97.7 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -26.1) |
| [[CFPAC-1 (line)]] | alt | 219 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0426× (z -42.5) |
| [[COLO 205 (line)]] | alt | 30.1 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -19.4) |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -25.2) |
| [[NCI-H2030 (line)]] | alt | 96.4 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0568× (z -44.8) |
| [[SW 900 (line)]] | alt | 74.2 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0659× (z -26.5) |
| [[A-172 (line)]] | wt | 105 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -35.7) |
| [[AsPC-1 (line)]] | alt | 33.0 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -19.9) |
| [[Panc 03.27 (line)]] | alt | 62.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -27.7) |
| [[J82 (line)]] | alt | 35.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0734× (z -27.4) |
| [[KATO III (line)]] | alt | 22.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.9) |
| [[RKO (line)]] | wt | 19.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -13.2) |
| [[SNU-423 (line)]] | alt | 83.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0743× (z -32.1) |
| [[SW 1088 (line)]] | alt | 206 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0715× (z -15.8) |
| [[SW1417 (line)]] | alt | 27.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -13.6) |
| [[LS 180 (line)]] | wt | 18.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 461 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -27.8) |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -8.8) |
| [[NCI-H596 (line)]] | alt | 61.3 | 1 | 0 | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 9.50× (z +9.8) | — |
| [[A-427 (line)]] | wt | 4.99 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.48 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.74 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.64 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.18 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.28 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMA4]] | +0.65 | +0.68 / +0.61 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[SCUBE3]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 | pathway: Degradation of the extracellular matrix |
| [[COL6A1]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 | pathway: Collagen degradation |
| [[ITGA11]] | +0.59 | +0.58 / +0.60 | both halves | 8e-06 | pathway: Extracellular matrix organization |
| [[PCDHGC3]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[COL6A2]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 425 |
| [[NAV1]] | +0.57 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SPOCD1]] | +0.57 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[ZCCHC24]] | +0.56 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[AEBP1]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MXRA7]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[FBLN7]] | +0.53 | +0.48 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIGD2]] | -0.48 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[BABAM2]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TRIM16]] | -0.46 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[MT1M]] | -0.45 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[YDJC]] | -0.45 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[RDH14]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[TNFAIP6]] | -0.44 | -0.44 / -0.45 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[TRIM16L-1]] | -0.44 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[CAVIN2]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MT1E]] | -0.44 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[JADE1]] | -0.44 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[MTFP1]] | -0.43 | -0.32 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 9, C 14. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP1]] | B | MMP1 activity raises MMP14's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without MMP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[AEBP1]] | B | AEBP1 activity raises MMP14's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 4.27× lower at baseline in the lines without AEBP1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[MT1M]] | B | MT1M activity raises MMP14's level | lines that do not express MT1M (29) vs lines expressing it (21) | 2.07× lower at baseline in the lines without MT1M | 0.061 | ⚠ within organs, on part of the lines; also absent: IRAK3, MIR155HG, G0S2 |
| [[LAMA4]] | B | LAMA4 activity raises MMP14's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 5.03× lower at baseline in the lines without LAMA4 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC |
| [[ITGA3]] | B | ITGA3 activity raises MMP14's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 4.56× lower at baseline in the lines without ITGA3 | 0.071 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[TMEM158]] | B | TMEM158 activity raises MMP14's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 4.20× lower at baseline in the lines without TMEM158 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[COL6A1]] | B | COL6A1 activity raises MMP14's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 4.01× lower at baseline in the lines without COL6A1 | 0.082 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN |
| [[ADAM19]] | B | ADAM19 activity raises MMP14's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 4.26× lower at baseline in the lines without ADAM19 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[COL7A1]] | B | COL7A1 activity raises MMP14's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.94× lower at baseline in the lines without COL7A1 | 0.097 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[TNFAIP6]] | C | TNFAIP6 activity raises MMP14's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 6.45× lower at baseline in the lines without TNFAIP6 | 0.005 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[ITGB3]] | C | ITGB3 activity raises MMP14's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 4.46× lower at baseline in the lines without ITGB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises MMP14's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.23× lower at baseline in the lines without COL5A1 | 0.014 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 10, C 7. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAC2]] | B | MMP14 activity raises RAC2's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 4.84× lower at baseline in the lines without MMP14 | 0.001 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[STING1]] | B | MMP14 activity raises STING1's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 2.85× lower at baseline in the lines without MMP14 | 0.013 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[ADAM19]] | B | MMP14 activity raises ADAM19's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 4.11× lower at baseline in the lines without MMP14 | 0.016 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[PDLIM7]] | B | MMP14 activity raises PDLIM7's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without MMP14 | 0.022 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[EFR3B]] | B | MMP14 activity lowers EFR3B's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 1.80× higher at baseline in the lines without MMP14 | 0.052 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[FXYD5]] | B | MMP14 activity raises FXYD5's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without MMP14 | 0.064 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[ECE1]] | B | MMP14 activity raises ECE1's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without MMP14 | 0.090 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[ITGA3]] | B | MMP14 activity raises ITGA3's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without MMP14 | 0.093 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| cells under [[Riluzole hydrochloride (drug)]] 5 µM | B | MMP14 activity raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | lines that do not express MMP14 (19) vs lines expressing it (29) | the lines without MMP14: 0.92× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[RDH14]] | B | MMP14 activity lowers RDH14's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 1.21× higher at baseline in the lines without MMP14 | 0.096 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |
| [[ITGB3]] | C | MMP14 activity raises ITGB3's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 4.10× lower at baseline in the lines without MMP14 | 0.017 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A; co-absent with the target |
| [[SPOCD1]] | C | MMP14 activity raises SPOCD1's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 3.99× lower at baseline in the lines without MMP14 | 0.030 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (55.0, 17.9); signed map (23.3, 44.7). **Vector** length 102, 29.7% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | -2.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.2 | +0.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -10.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.7 | -22.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -4.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.8 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -22.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.3 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,836,560-22,849,041 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MT1-MMP |
| Gene groups (HGNC) | M10 matrix metallopeptidases; Elastases |
| Hallmark sets | COAGULATION, INFLAMMATORY_RESPONSE, UV_RESPONSE_UP, COMPLEMENT, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 11 pathways, smallest: TGFBR3 PTM regulation; Activation of Matrix Metalloproteinases; Signaling by TGFBR3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P50281](https://www.uniprot.org/uniprotkb/P50281) (Matrix metalloproteinase-14):

> Endopeptidase that degrades various components of the extracellular matrix such as collagen. Essential for pericellular collagenolysis and modeling of skeletal and extraskeletal connective tissues during development (By similarity). Activates progelatinase A/MMP2, thereby acting as a positive regulator of cell growth and migration. Involved in the formation of the fibrovascular tissues in association with pro-MMP2. May be involved in actin cytoskeleton reorganization by cleaving PTK7. Acts as a …

**Summary**, from NCBI Gene [4323](https://www.ncbi.nlm.nih.gov/gene/4323):

> Proteins of the matrix metalloproteinase (MMP) family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. Most MMP's are secreted as inactive proproteins which are activated when cleaved by extracellular proteinases. However, the protein encoded by this gene is a member of the membrane-type MMP (MT-MMP) subfamily; each member …

**Accessions** — [HGNC:7160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7160) · Entrez [4323](https://www.ncbi.nlm.nih.gov/gene/4323) · UniProt [P50281](https://www.uniprot.org/uniprotkb/P50281) · Ensembl [ENSG00000157227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157227)

## Data

Gene col 8055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8055); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8055]; `tensor/DDL_lfc|DDL_z.npy` [8055]; `embed/gene_vectors.npy` [8055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8055 or target_col == 8055). Every well: [[MMP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
