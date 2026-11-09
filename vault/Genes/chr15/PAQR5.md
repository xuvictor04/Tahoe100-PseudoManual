---
symbol: "PAQR5"
type: "gene"
col: 6076
ensembl_id: "ENSG00000137819"
name: "progestin and adipoQ receptor family member 5"
location: "15q23"
module: 136
arm: "+"
pooled_cpm: 32.73
n_lines_expressing: 39
n_dd_up: 12
n_dd_down: 34
n_dd_up_clean: 11
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# PAQR5

*progestin and adipoQ receptor family member 5* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.68× (z +12.2, q 3e-31, up in 23 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.383× (z -22.3, q 0e+00, down in 33 of 36 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLNB]] (+0.72, fdr 7e-06), [[ZFYVE28]] (+0.72, fdr 1e-05), [[CSNK1E]] (+0.68, fdr 1e-05); moves opposite to [[AHI1-DT]] (-0.61, fdr 2e-04), [[TAPBPL]] (-0.61, fdr 3e-05), [[DECR1]] (-0.57, fdr 1e-04).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CCDC68]] → it (grade B ⚠); 4 go from it, the strongest it → [[MFSD10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +12.2 | 3e-31 | 23/37 (SW480, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +10.3 | 1e-22 | 25/37 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +10.1 | 6e-22 | 22/37 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +9.2 | 4e-18 | 26/37 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +8.5 | 3e-15 | 21/37 (SW480, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +7.8 | 5e-13 | 21/37 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +6.2 | 6e-08 | 17/36 (HCT15, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +4.5 | 5e-04 | 10/37 (NCI-H460, SW480, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.016 | 12/37 (NCI-H460, SW48, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.021 | 5/37 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.040 | 7/37 (SW 1271, HS-578T, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.065 | 12/37 (SW48, HOP62, …) | two highest doses | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.089 | 7/37 (SW48, NCI-H460, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.094 | 2/37 (LS 180, HT-29) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 6 with an alert ⚠; shown: the 15 strongest. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.383×** | -22.3 | 0e+00 | 33/36 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.289×** | -19.6 | 0e+00 | 31/36 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.508×** | -11.1 | 1e-26 | 24/36 (NCI-H2030, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -8.9 | 8e-17 | 23/37 (HT-29, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.574×** | -8.8 | 2e-16 | 26/37 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.682×** | -7.7 | 1e-12 | 23/37 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -7.4 | 1e-11 | 25/37 (C-33 A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.631×** | -7.1 | 7e-11 | 22/37 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.671×** | -6.5 | 4e-09 | 22/37 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.393×** | -6.4 | 9e-09 | 20/38 (LoVo, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.665×** | -6.3 | 1e-08 | 23/37 (AsPC-1, A549, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.729×** | -6.3 | 2e-08 | 23/37 (AsPC-1, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.717×** | -6.1 | 4e-08 | 21/37 (AsPC-1, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.767×** | -6.0 | 6e-08 | 19/37 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.693×** | -6.0 | 6e-08 | 18/37 (AsPC-1, RKO, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 49.8 | 0 | 14 | — | [[Binimetinib (drug)]] 0.5 µM 0.196× (z -15.6) |
| [[A549 (line)]] | wt | 232 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -23.6) |
| [[MIA PaCa-2 (line)]] | alt | 22.5 | 0 | 11 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0719× (z -16.3) |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0549× (z -36.2) |
| [[CFPAC-1 (line)]] | alt | 67.0 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -15.9) |
| [[SW480 (line)]] | alt | 12.4 | 7 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.95× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 34.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -27.5) |
| [[SW48 (line)]] | wt | 85.6 | 2 (1 ⚠) | 4 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.27× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -22.7) |
| [[HCT15 (line)]] | alt | 94.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -19.4) |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0458× (z -15.2) |
| [[HT-29 (line)]] | alt | 132 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0817× (z -23.2) |
| [[LoVo (line)]] | wt | 36.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.4) |
| [[LS 180 (line)]] | wt | 23.0 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 49.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.8) |
| [[A-172 (line)]] | wt | 16.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.0) |
| [[A-427 (line)]] | wt | 17.5 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0512× (z -18.8) |
| [[HEC-1-A (line)]] | alt | 91.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -14.9) |
| [[HS-578T (line)]] | alt | 18.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0631× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0615× (z -14.4) |
| [[CHP-212 (line)]] | wt | 66.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -10.8) |
| [[HOP62 (line)]] | alt | 34.7 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.623× (z -12.2) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.350× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -14.0) |
| [[RKO (line)]] | wt | 13.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.156× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 23.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.6) |
| [[SW 1271 (line)]] | alt | 76.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -10.4) |
| [[COLO 205 (line)]] | alt | 8.81 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 5 µM 0.0415× (z -10.2) |
| [[H4 (line)]] | wt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 8.70 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0870× (z -8.8) |
| [[A498 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.81 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB]] | +0.72 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[ZFYVE28]] | +0.72 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[CSNK1E]] | +0.68 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[S100A16]] | +0.68 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[ARHGEF4]] | +0.68 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[PPP2R2C]] | +0.67 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PLEKHG5]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.64 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[FMNL2]] | +0.63 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[TOR4A]] | +0.63 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.63 | +0.66 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHI1-DT]] | -0.61 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[TAPBPL]] | -0.61 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[DECR1]] | -0.57 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[MTUS1-DT]] | -0.57 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[GTF2IRD2]] | -0.57 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[ARMCX4]] | -0.57 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[RAF1]] | -0.55 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[RNF146]] | -0.55 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[RC3H2]] | -0.55 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[GTF2IRD2B]] | -0.55 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[KANSL1L]] | -0.55 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[SCAMP1-AS1]] | -0.55 | -0.50 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC68]] | B | CCDC68 activity raises PAQR5's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without CCDC68 | 0.012 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[CALB2]] | B | CALB2 activity raises PAQR5's level | lines that do not express CALB2 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without CALB2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CSF2, LINC02577, AADACP1 |
| [[SLCO4A1]] | B | SLCO4A1 activity raises PAQR5's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 2.93× lower at baseline in the lines without SLCO4A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[S100A16]] | B | S100A16 activity raises PAQR5's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.67× lower at baseline in the lines without S100A16 | 0.043 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[ITPR3]] | B | ITPR3 activity raises PAQR5's level | lines that do not express ITPR3 (6) vs lines expressing it (44) | 2.08× lower at baseline in the lines without ITPR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAT1, LRRC8E, HTATIP2; its own permutation p |
| [[THSD4]] | B | THSD4 activity raises PAQR5's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 2.16× lower at baseline in the lines without THSD4 | 0.089 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1 |
| [[NIBAN2]] | B | NIBAN2 activity raises PAQR5's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 2.67× lower at baseline in the lines without NIBAN2 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[BOK]] | B | BOK activity raises PAQR5's level | lines that do not express BOK (5) vs lines expressing it (45) | 3.42× lower at baseline in the lines without BOK | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC35F2, PLEC, IL4R |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFSD10]] | B | PAQR5 activity raises MFSD10's level | lines that do not express PAQR5 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without PAQR5 | 0.029 | ⚠ within organs, on part of the lines; also absent: ADORA2B |
| [[PLAUR]] | B | PAQR5 activity raises PLAUR's level | lines that do not express PAQR5 (11) vs lines expressing it (39) | 2.90× lower at baseline in the lines without PAQR5 | 0.033 | ⚠ within organs, on part of the lines; also absent: ADORA2B |
| [[SPTLC2]] | B | PAQR5 activity raises SPTLC2's level | lines that do not express PAQR5 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without PAQR5 | 0.035 | ⚠ within organs, on part of the lines; also absent: ADORA2B |
| [[CCDC68]] | B | PAQR5 activity raises CCDC68's level | lines that do not express PAQR5 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without PAQR5 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADORA2B |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.9, 2.5); signed map (0.3, 49.6). **Vector** length 124, 33.8% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +12.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.4 | +9.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.8 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +1.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.7 | -7.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.5 | -7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -22.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.3 | -6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.2 | -4.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -5.1 | -6.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | progestin and adipoQ receptor family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:69,298,912-69,407,780 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20190, MPRG |
| Gene groups (HGNC) | Progestin and adipoQ receptor family; PAQR family membrane progesterone receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXK6](https://www.uniprot.org/uniprotkb/Q9NXK6) (Membrane progestin receptor gamma):

> Plasma membrane progesterone (P4) receptor coupled to G proteins. Seems to act through a G(i) mediated pathway. May be involved in oocyte maturation.

**Summary**, from NCBI Gene [54852](https://www.ncbi.nlm.nih.gov/gene/54852):

> Predicted to enable signaling receptor activity. Predicted to be involved in oogenesis. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29645) · Entrez [54852](https://www.ncbi.nlm.nih.gov/gene/54852) · UniProt [Q9NXK6](https://www.uniprot.org/uniprotkb/Q9NXK6) · Ensembl [ENSG00000137819](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137819)

## Data

Gene col 6076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6076); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6076]; `tensor/DDL_lfc|DDL_z.npy` [6076]; `embed/gene_vectors.npy` [6076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6076 or target_col == 6076). Every well: [[PAQR5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAQR5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
