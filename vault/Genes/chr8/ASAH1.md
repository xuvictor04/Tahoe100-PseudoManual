---
symbol: "ASAH1"
type: "gene"
col: 2494
ensembl_id: "ENSG00000104763"
name: "N-acylsphingosine amidohydrolase 1"
location: "8p22"
module: 45
arm: "+"
pooled_cpm: 36.01
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# ASAH1

*N-acylsphingosine amidohydrolase 1* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.46× (z +12.0, q 2e-30, up in 31 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.02× (z +9.7, q 5e-20, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.466× (z -10.5, q 3e-23, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERP29]] (+0.72, fdr 7e-06), [[GM2A]] (+0.72, fdr 7e-06), [[DNASE2]] (+0.69, fdr 7e-06); moves opposite to [[NEPRO-AS1]] (-0.65, fdr 1e-05), [[NSRP1]] (-0.62, fdr 2e-05), [[SSUH2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MSLN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +12.0 | 2e-30 | 31/37 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +11.9 | 5e-30 | 38/42 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +9.7 | 5e-20 | 39/46 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +8.7 | 4e-16 | 38/46 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +8.0 | 1e-13 | 29/39 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.7 | 1e-12 | 34/46 (CFPAC-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.69×** | +7.2 | 4e-11 | 33/46 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +6.0 | 2e-07 | 34/46 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +5.8 | 3e-07 | 27/46 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.8 | 4e-07 | 32/46 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +5.2 | 8e-06 | 28/46 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.47×** | +5.2 | 1e-05 | 24/47 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 3e-04 | 28/44 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.5 | 3e-04 | 23/46 (A498, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.36×** | +4.1 | 0.002 | 23/44 (J82, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.013 | 17/46 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.013 | 17/46 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.013 | 21/45 (SNU-423, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.024 | 14/46 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.024 | 10/46 (HOP62, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.058 | 21/46 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.466×** | -10.5 | 3e-23 | 38/45 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.631×** | -9.0 | 6e-17 | 37/45 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.544×** | -8.1 | 1e-13 | 34/46 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.580×** | -7.5 | 8e-12 | 36/46 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.674×** | -5.4 | 6e-06 | 25/46 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.744×** | -3.8 | 0.015 | 22/44 (C32, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.793× | -3.2 | 0.11 | 18/46 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.790× | -3.1 | 0.12 | 17/45 (SK-MEL-2, SNU-423, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.0 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 72.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.63× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 3.18× (z +11.9) | — |
| [[A498 (line)]] | wt | 12.5 | 3 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 3.57× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 25.2 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.4) |
| [[HS-578T (line)]] | alt | 46.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 16.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.25× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 131 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.274× (z -13.5) |
| [[COLO 205 (line)]] | alt | 55.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.20× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 13.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +9.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 38.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 67.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 33.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 49.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.264× (z -9.8) |
| [[HCT15 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 94.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.30× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 51.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.2) |
| [[LoVo (line)]] | wt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.9) |
| [[PANC-1 (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +8.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 37.7 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.49× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 55.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.7) |
| [[SNU-423 (line)]] | alt | 46.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -9.6) |
| [[SW480 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.74 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERP29]] | +0.72 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[GM2A]] | +0.72 | +0.63 / +0.70 | both halves | 7e-06 | pathway: Glycosphingolipid catabolism; STRING 505 |
| [[DNASE2]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CTSD]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 | STRING 576 |
| [[C20orf96]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[LAPTM4A]] | +0.67 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[GLB1]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 | pathway: Glycosphingolipid catabolism; STRING 771 |
| [[PEBP1]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PECR]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[SUMF2]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 | pathway: Glycosphingolipid catabolism |
| [[FAM210B]] | +0.63 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SCPEP1]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEPRO-AS1]] | -0.65 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.62 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[SSUH2]] | -0.60 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[ZNF347]] | -0.60 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[MIS12]] | -0.60 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.59 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[RPL7L1]] | -0.59 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[UTP3]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SETX]] | -0.57 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[ZNF562]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSLN]] | B | MSLN activity raises ASAH1's level | lines that do not express MSLN (33) vs lines expressing it (17) | 1.50× lower at baseline in the lines without MSLN | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-18.0, -19.0); signed map (-50.9, -8.7). **Vector** length 102, 27.7% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +3.6 | +3.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.5 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Afatinib (drug)]] 5 µM |  | +3.0 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.3 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.5 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.4 | -5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | N-acylsphingosine amidohydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:18,055,992-18,084,998 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AC, PHP32, FLJ21558, ACDase; previously ASAH |
| Reactome | 9 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13510](https://www.uniprot.org/uniprotkb/Q13510) (Acid ceramidase):

> Lysosomal ceramidase that hydrolyzes sphingolipid ceramides into sphingosine and free fatty acids at acidic pH. Ceramides, sphingosine, and its phosphorylated form sphingosine-1-phosphate are bioactive lipids that mediate cellular signaling pathways regulating several biological processes including cell proliferation, apoptosis and differentiation. Has a higher catalytic efficiency towards C12-ceramides versus other ceramides. Also catalyzes the reverse reaction allowing the synthesis of …

**Summary**, from NCBI Gene [427](https://www.ncbi.nlm.nih.gov/gene/427):

> This gene encodes a member of the acid ceramidase family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed. Processing of this preproprotein generates alpha and beta subunits that heterodimerize to form the mature lysosomal enzyme, which catalyzes the degradation of ceramide into sphingosine and free fatty acid. This enzyme is overexpressed in multiple human cancers and may play a role in …

**Accessions** — [HGNC:735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:735) · Entrez [427](https://www.ncbi.nlm.nih.gov/gene/427) · UniProt [Q13510](https://www.uniprot.org/uniprotkb/Q13510) · Ensembl [ENSG00000104763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104763)

## Data

Gene col 2494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2494); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2494]; `tensor/DDL_lfc|DDL_z.npy` [2494]; `embed/gene_vectors.npy` [2494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2494 or target_col == 2494). Every well: [[ASAH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASAH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
