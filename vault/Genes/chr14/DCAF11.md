---
symbol: "DCAF11"
type: "gene"
col: 2038
ensembl_id: "ENSG00000100897"
name: "DDB1 and CUL4 associated factor 11"
location: "14q12"
module: 76
arm: "+"
pooled_cpm: 27.04
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# DCAF11

*DDB1 and CUL4 associated factor 11* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +10.3, q 3e-22, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.631× (z -8.2, q 1e-13, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH6A1]] (+0.73, fdr 7e-06), [[CBFA2T2]] (+0.64, fdr 9e-06), [[TSEN34]] (+0.62, fdr 2e-05); moves opposite to [[ZNF239]] (-0.62, fdr 1e-05), [[GPATCH4]] (-0.60, fdr 1e-05), [[C12orf29]] (-0.60, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PRKG2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +10.3 | 3e-22 | 34/47 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +9.0 | 8e-17 | 32/48 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +8.0 | 2e-13 | 33/48 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +6.3 | 4e-08 | 27/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.9 | 4e-07 | 17/35 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.38×** | +5.7 | 1e-06 | 24/48 (NCI-H460, SNU-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.37×** | +5.5 | 3e-06 | 24/44 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.30×** | +4.7 | 2e-04 | 21/47 (NCI-H460, SNU-1, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.28×** | +4.3 | 0.001 | 14/44 (HS-578T, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.006 | 19/47 (HEC-1-A, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.008 | 10/45 (NCI-H460, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.23×** | +3.5 | 0.024 | 16/48 (Panc 03.27, HEC-1-A, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.046 | 12/45 (H4, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.22×** | +3.2 | 0.047 | 14/39 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.071 | 7/48 (NCI-H2347, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.075 | 7/48 (BT-474, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2038.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.631×** | -8.2 | 1e-13 | 34/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.635×** | -8.1 | 2e-13 | 35/47 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -7.9 | 4e-13 | 28/47 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.749×** | -7.1 | 1e-10 | 29/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.689×** | -6.6 | 4e-09 | 28/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.708×** | -6.1 | 8e-08 | 25/47 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.703×** | -6.0 | 1e-07 | 25/47 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.738×** | -5.1 | 2e-05 | 23/47 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.755×** | -5.0 | 4e-05 | 22/48 (A-427, NCI-H1573, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -4.9 | 4e-05 | 24/47 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.765×** | -4.5 | 3e-04 | 23/48 (AN3 CA, NCI-H2030, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.673×** | -3.5 | 0.023 | 14/46 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 0.834× | -3.1 | 0.080 | 14/47 (NCI-H2030, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.6 | 7 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.82× (z +17.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HEC-1-A (line)]] | alt | 25.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +11.3) | — |
| [[NCI-H2347 (line)]] | alt | 57.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -11.3) |
| [[HT-29 (line)]] | alt | 35.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -11.8) |
| [[PANC-1 (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -12.5) |
| [[SNU-1 (line)]] | wt | 25.2 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.63× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 28.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 38.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 44.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.167× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 26.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.324× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.161× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.72× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.469× (z -8.5) ⚠ cell-cycle shift, explains ~96% of this change |
| [[Panc 03.27 (line)]] | alt | 45.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +8.5) | — |
| [[A-172 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH6A1]] | +0.73 | +0.65 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[CBFA2T2]] | +0.64 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[TSEN34]] | +0.62 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[CNNM2]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ATF6B]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[HDAC6]] | +0.61 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[NARF]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[KMT5C]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[DNM2]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ZNHIT1]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PBXIP1]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PLAG1]] | +0.60 | +0.59 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF239]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.60 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[C12orf29]] | -0.60 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[ZNF195]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CCT5]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[PPIL1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[MAK16]] | -0.57 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | -0.57 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[CCT7]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[SLC35B4]] | -0.56 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[POGK]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PSMC5]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 | pathway: Neddylation |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKG2-AS1]] | B | PRKG2-AS1 activity strengthens DCAF11's drug response | lines that do not express PRKG2-AS1 (23) vs lines expressing it (25) | the lines without PRKG2-AS1 respond 0.57× as strongly (z diff +1.48); rises at some drug-doses, falls at others (67% from rises): Homoharringtonine 0.5 µM: 0.71x vs 0.52x (z diff +2.8); Panobinostat 0.5 µM: 1.41x vs 1.76x (z diff +2.2); Panobinostat 5 µM: 1.38x vs 1.70x (z diff +2.1) | 0.012 | ⚠ within organs, on part of the lines; also absent: CBLC, B3GNT3, ESRP2; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[PCOLCE2]] | B | PCOLCE2 activity lowers DCAF11's level | lines that do not express PCOLCE2 (16) vs lines expressing it (34) | 1.44× higher at baseline in the lines without PCOLCE2 | 0.063 | ⚠ within organs, on part of the lines; also absent: WDR17, NRG1, TSHZ3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.9, -19.2); signed map (-20.5, 7.1). **Vector** length 99.6, 22.6% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +4.9 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +10.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.3 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.2 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +9.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.7 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +3.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.7 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,114,195-24,125,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRO2389, GL014; previously WDR23 |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEB1](https://www.uniprot.org/uniprotkb/Q8TEB1) (DDB1- and CUL4-associated factor 11):

> May function as a substrate receptor for CUL4-DDB1 E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [80344](https://www.ncbi.nlm.nih.gov/gene/80344):

> This gene encodes a WD repeat-containing protein that interacts with the COP9 signalosome, a macromolecular complex that interacts with cullin-RING E3 ligases and regulates their activity by hydrolyzing cullin-Nedd8 conjugates. Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:20258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20258) · Entrez [80344](https://www.ncbi.nlm.nih.gov/gene/80344) · UniProt [Q8TEB1](https://www.uniprot.org/uniprotkb/Q8TEB1) · Ensembl [ENSG00000100897](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100897)

## Data

Gene col 2038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2038); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2038]; `tensor/DDL_lfc|DDL_z.npy` [2038]; `embed/gene_vectors.npy` [2038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2038 or target_col == 2038). Every well: [[DCAF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
