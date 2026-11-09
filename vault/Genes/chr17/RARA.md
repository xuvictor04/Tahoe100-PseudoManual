---
symbol: "RARA"
type: "gene"
col: 5241
ensembl_id: "ENSG00000131759"
name: "retinoic acid receptor alpha"
location: "17q21.2"
module: 206
arm: "+"
pooled_cpm: 33.75
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# RARA

*retinoic acid receptor alpha* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.17× (z +18.6, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.619× (z -5.9, q 2e-06, down in 22 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 0.706× (z -4.3, q 0.003, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDGFB]] (+0.62, fdr 7e-06), [[MIDEAS]] (+0.60, fdr 1e-05), [[ING1]] (+0.59, fdr 1e-05); moves opposite to [[UBE2K]] (-0.57, fdr 1e-05), [[PDS5A]] (-0.56, fdr 2e-05), [[NUTM2A-AS1]] (-0.54, fdr 1e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ICAM1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NRP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.17×** | +18.6 | 0e+00 | 43/47 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.77×** | +8.5 | 7e-15 | 38/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +6.8 | 2e-09 | 31/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +6.7 | 2e-09 | 30/48 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.2 | 8e-08 | 30/47 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +5.9 | 3e-07 | 27/45 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.57×** | +5.5 | 4e-06 | 31/48 (KATO III, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.52×** | +5.1 | 2e-05 | 27/48 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +4.8 | 1e-04 | 26/45 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.44×** | +4.4 | 6e-04 | 24/48 (LOX-IMVI, PANC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.35×** | +3.6 | 0.014 | 23/48 (KATO III, SW1417, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5241.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -5.9 | 2e-06 | 22/41 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -4.8 | 5e-04 | 5/48 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.695×** | -4.3 | 0.003 | 20/32 (CHP-212, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.706×** | -4.3 | 0.003 | 21/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -4.1 | 0.005 | 24/48 (HOP62, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -4.1 | 0.005 | 23/48 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.709×** | -4.0 | 0.005 | 22/47 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.751×** | -3.5 | 0.031 | 22/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.581×** | -3.5 | 0.031 | 18/46 (LS 180, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.760×** | -3.4 | 0.041 | 22/48 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.761×** | -3.4 | 0.041 | 16/48 (C32, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 23.0 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -12.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 163 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0523× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -8.6) |
| [[HOP62 (line)]] | alt | 73.9 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.254× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 44.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -12.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 35.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 87.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 96.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 13.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +16.1) | — |
| [[PANC-1 (line)]] | alt | 41.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 37.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.0748× (z -15.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 43.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +13.7) | — |
| [[A498 (line)]] | wt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.9) | — |
| [[A549 (line)]] | wt | 47.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +9.4) | — |
| [[H4 (line)]] | wt | 42.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0858× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -11.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -9.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +11.1) | — |
| [[J82 (line)]] | alt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +13.6) | — |
| [[LoVo (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 19.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +9.7) | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0812× (z -8.8) |
| [[A-427 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDGFB]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MIDEAS]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[ING1]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[PFKFB4]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[NFKBIE]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[NR1D1]] | +0.58 | +0.67 / +0.55 | both halves | 1e-05 | pathway: Nuclear Receptor transcription pathway |
| [[N4BP3]] | +0.56 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[VASN]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[LRP1]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[FSCN1]] | +0.54 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[KDM5B]] | +0.54 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.54 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2K]] | -0.57 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PDS5A]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[NUTM2A-AS1]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[NCBP3]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[CLASP2]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SFMBT1]] | -0.51 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[LARP4]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CDC42BPA]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZFYVE9]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 | pathway: Signaling by TGFB family members |
| [[KLHL2]] | -0.50 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[IPP]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[HERC2]] | -0.49 | -0.56 / -0.59 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ICAM1]] | B | ICAM1 activity raises RARA's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without ICAM1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[SPNS2]] | B | SPNS2 activity raises RARA's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 1.14× lower at baseline in the lines without SPNS2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[IGFBP3]] | B | IGFBP3 activity raises RARA's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.92× lower at baseline in the lines without IGFBP3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[PDGFB]] | B | PDGFB activity raises RARA's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.68× lower at baseline in the lines without PDGFB | 0.069 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[CFAP45]] | B | CFAP45 activity raises RARA's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without CFAP45 | 0.088 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises RARA's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RAB3A]] | C | RAB3A's natural level weakens RARA's drug response | RAB3A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.02; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP2]] | B | RARA, [[RARB]], [[RARG]] activity raises NRP2's level | compounds that target RARA, RARB, RARG: 2 of 2 raise it (Retinoic acid, Tazarotene) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.2, -5.8); signed map (-4.5, 15.3). **Vector** length 105, 26.4% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +18.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | +8.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.7 | +0.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -7.5 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | -7.3 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.4 | -4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.8 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.1 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | retinoic acid receptor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,309,180-40,357,643 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAR, NR1B1, RARalpha, RAR-alpha |
| Gene groups (HGNC) | Retinoic acid receptors |
| Hallmark sets | APOPTOSIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 12 pathways, smallest: TGFBR3 expression; SUMOylation of intracellular receptors; Signaling by Retinoic Acid |
| Matched by | ensembl_id |

**Function**, from UniProt [P10276](https://www.uniprot.org/uniprotkb/P10276) (Retinoic acid receptor alpha):

> Receptor for retinoic acid. Retinoic acid receptors bind as heterodimers to their target response elements in response to their ligands, all-trans or 9-cis retinoic acid, and regulate gene expression in various biological processes. The RXR/RAR heterodimers bind to the retinoic acid response elements (RARE) composed of tandem 5'-AGGTCA-3' sites known as DR1-DR5. In the absence of ligand, the RXR-RAR heterodimers associate with a multiprotein complex containing transcription corepressors that …

**Summary**, from NCBI Gene [5914](https://www.ncbi.nlm.nih.gov/gene/5914):

> This gene represents a nuclear retinoic acid receptor. The encoded protein, retinoic acid receptor alpha, regulates transcription in a ligand-dependent manner. This gene has been implicated in regulation of development, differentiation, apoptosis, granulopoeisis, and transcription of clock genes. Translocations between this locus and several other loci have been associated with acute promyelocytic leukemia. Alternatively spliced transcript variants have been found for this locus.[provided by …

**Accessions** — [HGNC:9864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9864) · Entrez [5914](https://www.ncbi.nlm.nih.gov/gene/5914) · UniProt [P10276](https://www.uniprot.org/uniprotkb/P10276) · Ensembl [ENSG00000131759](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131759)

## Data

Gene col 5241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5241); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5241]; `tensor/DDL_lfc|DDL_z.npy` [5241]; `embed/gene_vectors.npy` [5241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5241 or target_col == 5241). Every well: [[RARA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RARA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
