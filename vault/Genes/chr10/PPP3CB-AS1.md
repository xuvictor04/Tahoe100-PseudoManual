---
symbol: "PPP3CB-AS1"
type: "gene"
col: 13304
ensembl_id: "ENSG00000221817"
name: "PPP3CB antisense RNA 1"
location: "10q22.2"
module: 10
arm: "+"
pooled_cpm: 7.32
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PPP3CB-AS1

*PPP3CB antisense RNA 1* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.30× (z +8.2, q 2e-13, up in 10 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.68× (z +5.3, q 2e-05, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.266× (z -13.5, q 7e-39, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB30-DT]] (+0.82, fdr 8e-06), [[ZCWPW1]] (+0.82, fdr 7e-06), [[GABPB2]] (+0.82, fdr 7e-06); moves opposite to [[HACE1]] (-0.75, fdr 1e-05), [[MAST3]] (-0.72, fdr 3e-05), [[L2HGDH]] (-0.72, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSORS1C1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +8.2 | 2e-13 | 10/12 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.0 | 4e-13 | 20/31 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +5.8 | 1e-06 | 9/22 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.68×** | +5.3 | 2e-05 | 29/46 (SW480, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.2 | 2e-05 | 22/40 (BT-474, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.6 | 5e-04 | 10/47 (SW480, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.4 | 0.001 | 19/40 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.13 | 11/39 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.38× | +3.0 | 0.16 | 3/45 (A549, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.266×** | -13.5 | 7e-39 | 35/46 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.288×** | -12.7 | 2e-34 | 40/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.324×** | -11.5 | 3e-28 | 38/45 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.461×** | -7.9 | 5e-13 | 30/40 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.473×** | -7.6 | 3e-12 | 28/47 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.448×** | -7.5 | 6e-12 | 32/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.547×** | -6.1 | 6e-08 | 25/44 (RKO, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.328×** | -5.9 | 2e-07 | 23/40 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -5.1 | 3e-05 | 24/46 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.611×** | -5.0 | 3e-05 | 22/42 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.394×** | -5.0 | 4e-05 | 25/44 (KATO III, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.650×** | -4.4 | 6e-04 | 21/45 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -4.2 | 0.001 | 13/43 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.687×** | -3.7 | 0.010 | 18/36 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -3.7 | 0.010 | 15/44 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Silodosin (drug)]] 5 µM |  | **0.691×** | -3.6 | 0.011 | 12/42 (BT-474, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -3.4 | 0.027 | 17/42 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.539×** | -3.3 | 0.031 | 11/36 (SW480, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.724×** | -3.3 | 0.031 | 8/43 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.732×** | -3.2 | 0.044 | 5/47 (NCI-H1573, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 16.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0505× (z -17.7) |
| [[PANC-1 (line)]] | alt | 8.64 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.206× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 7.51 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.117× (z -8.7) |
| [[SW480 (line)]] | alt | 10.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 5.25 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0799× (z -10.3) |
| [[A-427 (line)]] | wt | 5.48 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0568× (z -10.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[BT-474 (line)]] | alt | 4.98 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0628× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 7.76 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.149× (z -8.6) |
| [[COLO 205 (line)]] | alt | 9.17 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0929× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -9.1) |
| [[HOP62 (line)]] | alt | 8.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 5.53 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LoVo (line)]] | wt | 9.45 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 6.88 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 8.16 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0635× (z -9.2) |
| [[A-172 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB30-DT]] | +0.82 | +0.80 / +0.58 | both halves | 8e-06 |  |
| [[ZCWPW1]] | +0.82 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[GABPB2]] | +0.82 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[PBLD]] | +0.81 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.81 | +0.80 / +0.37 | both halves | 8e-05 | same gene group |
| [[WARS2-AS1]] | +0.81 | +0.78 / +0.47 | both halves | 2e-05 | same gene group |
| [[KRCC1]] | +0.81 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[ERMAP]] | +0.80 | +0.82 / +0.47 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | +0.80 | +0.81 / +0.36 | both halves | 1e-04 |  |
| [[ATE1OSP]] | +0.80 | +0.79 / +0.47 | both halves | 2e-05 |  |
| [[RFX3-DT]] | +0.79 | +0.78 / +0.34 | both halves | 1e-04 |  |
| [[FKRP]] | +0.79 | +0.79 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACE1]] | -0.75 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[MAST3]] | -0.72 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[L2HGDH]] | -0.72 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.71 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[ARRB2]] | -0.71 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD27]] | -0.71 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[SH3PXD2B]] | -0.70 | -0.64 / -0.38 | both halves | 7e-05 |  |
| [[YIF1B]] | -0.70 | -0.61 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[ARL6]] | -0.70 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.69 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ATRN]] | -0.69 | -0.60 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSORS1C1]] | B | PSORS1C1 activity raises PPP3CB-AS1's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.32× lower at baseline in the lines without PSORS1C1 | 0.074 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[CDON]] | C | CDON activity raises PPP3CB-AS1's level | lines that do not express CDON (3) vs lines expressing it (47) | 1.12× lower at baseline in the lines without CDON | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | PPP3CB-AS1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | PPP3CB-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.500 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.0, 13.4); signed map (25.9, -10.0). **Vector** length 81.7, 15.8% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.1 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +0.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.6 | -13.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.2 | -7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -11.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.7 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | -12.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | PPP3CB antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q22.2 — chr10:73,495,525-73,520,070 (+) |
| Ensembl biotype | lncRNA |
| Also known as | USP54-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50750) · Entrez [101929145](https://www.ncbi.nlm.nih.gov/gene/101929145) · Ensembl [ENSG00000221817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221817)

## Data

Gene col 13304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13304); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13304]; `tensor/DDL_lfc|DDL_z.npy` [13304]; `embed/gene_vectors.npy` [13304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13304 or target_col == 13304). Every well: [[PPP3CB-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP3CB-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
