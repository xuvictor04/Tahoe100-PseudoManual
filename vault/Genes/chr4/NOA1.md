---
symbol: "NOA1"
type: "gene"
col: 1393
ensembl_id: "ENSG00000084092"
name: "nitric oxide associated 1"
location: "4q12"
module: 24
arm: "+"
pooled_cpm: 18.33
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NOA1

*nitric oxide associated 1* — 4q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.82× (z +17.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.703× (z -5.8, q 3e-06, down in 18 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.713× (z -5.7, q 3e-06, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (CFPAC-1 0.111×, MIA PaCa-2 0.175×, SHP-77 0.267×, KATO III 0.255×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1573 0.102×, NCI-H23 0.208×, LoVo 0.339×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.276×, A-172 0.182×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.134×); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (NCI-H661 0.0578×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HOP62 0.265×).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYG1]] (+0.67, fdr 1e-05), [[NOB1]] (+0.66, fdr 7e-06), [[TOMM70]] (+0.62, fdr 1e-05); moves opposite to [[ARGLU1]] (-0.57, fdr 1e-04), [[SDCBP2-AS1]] (-0.56, fdr 0.001, ⚠ one half only (not replicated)), [[RYR2]] (-0.55, fdr 0.001, ⚠ not reproduced), [[PSMD6-AS1]] (-0.55, fdr 4e-04), [[SRSF5]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.82×** | +17.5 | 0e+00 | 47/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.69×** | +16.7 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.66×** | +16.5 | 0e+00 | 46/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +10.2 | 3e-22 | 37/46 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +8.3 | 1e-14 | 40/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.6 | 2e-06 | 24/48 (SHP-77, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.2 | 1e-05 | 18/40 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.9 | 6e-05 | 21/44 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +4.7 | 2e-04 | 17/47 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.6 | 2e-04 | 16/47 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +4.5 | 3e-04 | 14/48 (NCI-H1792, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 3e-04 | 17/47 (A498, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +4.4 | 5e-04 | 18/48 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.30×** | +4.3 | 7e-04 | 16/45 (LS 180, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.005 | 10/47 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.011 | 9/47 (HEC-1-A, SW480, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.049 | 7/44 (A498, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.059 | 4/46 (NCI-H2347, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1393.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (CFPAC-1 0.111×, MIA PaCa-2 0.175×, SHP-77 0.267×, KATO III 0.255×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H1573 0.102×, NCI-H23 0.208×, LoVo 0.339×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.276×, A-172 0.182×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (SNU-1 0.134×); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (NCI-H661 0.0578×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (HOP62 0.265×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -5.8 | 3e-06 | 18/32 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.713×** | -5.7 | 3e-06 | 22/46 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -5.6 | 3e-06 | 26/48 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.749×** | -4.9 | 1e-04 | 22/46 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.785×** | -4.1 | 0.005 | 22/42 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | 0.697× | -3.2 | 0.13 | 14/46 (HT-29, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.831× | -3.1 | 0.13 | 19/47 (SNU-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (drug)]] 5 µM |  | 0.828× | -3.1 | 0.14 | 13/46 (HOP62, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 11.7 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.95× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.265× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.95× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 31.6 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -10.6) |
| [[SW480 (line)]] | alt | 23.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.63× (z +10.2) | — |
| [[A498 (line)]] | wt | 15.7 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.94× (z +8.9) | — |
| [[A-172 (line)]] | wt | 8.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -9.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 14.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.125× (z -8.8) |
| [[HT-29 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.102× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 15.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.01× (z +9.7) | — |
| [[NCI-H661 (line)]] | alt | 36.9 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0578× (z -9.6) |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 17.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +8.5) | — |
| [[A-427 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 11 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYG1]] | +0.67 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NOB1]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 | STRING 533 |
| [[TOMM70]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.62 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[MRPL10]] | +0.61 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[MRPS2]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 | STRING 905 |
| [[MRPS34]] | +0.59 | +0.34 / +0.51 | both halves | 1e-04 | STRING 961 |
| [[MRPL43]] | +0.59 | +0.48 / +0.50 | both halves | 2e-05 | STRING 524 |
| [[RMND1]] | +0.58 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[PHAF1]] | +0.58 | +0.25 / +0.50 | both halves | 4e-04 |  |
| [[MRPS26]] | +0.58 | +0.41 / +0.54 | both halves | 4e-05 | STRING 895 |
| [[BAG4]] | +0.57 | +0.40 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARGLU1]] | -0.57 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[SDCBP2-AS1]] | -0.56 | -0.17 / -0.55 | ⚠ one half (not replicated) | 0.001 |  |
| [[RYR2]] | -0.55 | -0.16 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[PSMD6-AS1]] | -0.55 | -0.24 / -0.42 | both halves | 4e-04 |  |
| [[SRSF5]] | -0.54 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[CROCC]] | -0.54 | -0.02 / -0.50 | ⚠ not reproduced | 0.007 |  |
| [[PPP1R3F]] | -0.53 | -0.31 / -0.26 | both halves | 4e-04 |  |
| [[CSTF3]] | -0.53 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[SRSF1]] | -0.53 | -0.19 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[CYB5D2]] | -0.53 | -0.13 / -0.37 | ⚠ not reproduced | 0.002 |  |
| [[PLA2G4C]] | -0.52 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[SPTY2D1OS]] | -0.51 | -0.24 / -0.21 | both halves | 7e-04 |  |
| [[MMRN2]] | -0.51 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[DCAF8]] | -0.51 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[ARRDC3-AS1]] | -0.51 | -0.20 / -0.33 | both halves | 7e-04 |  |
| [[ENSA]] | -0.50 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[AGER]] | -0.50 | -0.41 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.347). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-45.9, -7.9); signed map (-16.6, -24.3). **Vector** length 81.3, 15.8% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.3 | +16.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +17.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +16.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.3 | +4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +4.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.8 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | nitric oxide associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q12 — chr4:56,963,350-56,977,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3232, hAtNOS1, hNOA1, MTG3; previously C4orf14 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NC60](https://www.uniprot.org/uniprotkb/Q8NC60) (Nitric oxide-associated protein 1):

> Involved in regulation of mitochondrial protein translation and respiration. Plays a role in mitochondria-mediated cell death. May act as a scaffolding protein or stabilizer of respiratory chain supercomplexes. Binds GTP.

**Summary**, from NCBI Gene [84273](https://www.ncbi.nlm.nih.gov/gene/84273):

> The protein encoded by this gene is a nuclear-encoded GTPase that functions in the mitochondrion. Upon translation, this protein is imported into the nucleus and then into the nucleolus before being exported to the mitochondrion. The encoded protein is required for oxygen-dependent regulation of mitochondrial respiratory complexes and for mitochondrial protein synthesis. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:28473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28473) · Entrez [84273](https://www.ncbi.nlm.nih.gov/gene/84273) · UniProt [Q8NC60](https://www.uniprot.org/uniprotkb/Q8NC60) · Ensembl [ENSG00000084092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084092)

## Data

Gene col 1393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1393); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1393]; `tensor/DDL_lfc|DDL_z.npy` [1393]; `embed/gene_vectors.npy` [1393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1393 or target_col == 1393). Every well: [[NOA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
