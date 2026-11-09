---
symbol: "CCDC136"
type: "gene"
col: 4901
ensembl_id: "ENSG00000128596"
name: "coiled-coil domain containing 136"
location: "7q32.1"
module: 102
arm: "+"
pooled_cpm: 10.11
n_lines_expressing: 40
n_dd_up: 23
n_dd_down: 12
n_dd_up_clean: 16
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 3
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# CCDC136

*coiled-coil domain containing 136* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.74× (z +10.4, q 1e-22, up in 28 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.485× (z -9.6, q 3e-19, down in 29 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.516× (z -8.8, q 4e-16, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCN8A]] (+0.58, fdr 2e-05), [[FAM171B]] (+0.56, fdr 1e-05), [[LRRN2]] (+0.54, fdr 2e-05); moves opposite to [[TCTN3]] (-0.53, fdr 4e-05), [[NDUFV1]] (-0.49, fdr 3e-05), [[GALK2]] (-0.47, fdr 3e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[APBB1]] → it (grade B ⚠); 3 go from it, the strongest it → [[APBB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +10.4 | 1e-22 | 28/38 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +7.9 | 6e-13 | 21/36 (HOP62, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.7 | 2e-12 | 18/38 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +7.4 | 2e-11 | 23/36 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +7.0 | 2e-10 | 18/37 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +6.4 | 2e-08 | 21/37 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +5.8 | 4e-07 | 17/37 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.52×** | +5.1 | 2e-05 | 13/37 (SW480, LoVo, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.43×** | +4.6 | 3e-04 | 14/31 (HOP62, LoVo, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.38×** | +4.3 | 9e-04 | 15/36 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +4.0 | 0.003 | 11/37 (J82, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.004 | 10/36 (SK-MEL-2, LoVo, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.004 | 7/36 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.004 | 10/37 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.004 | 9/37 (HOP62, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.009 | 6/37 (LoVo, C32, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.020 | 6/38 (HOP62, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.034 | 9/35 (RKO, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4901.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.485×** | -9.6 | 3e-19 | 29/35 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.516×** | -8.8 | 4e-16 | 21/37 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.594×** | -6.9 | 8e-10 | 21/36 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.586×** | -6.8 | 1e-09 | 16/32 (LoVo, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.396×** | -6.5 | 1e-08 | 18/37 (SK-MEL-2, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.406×** | -6.3 | 3e-08 | 17/34 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -6.0 | 2e-07 | 16/37 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.739×** | -4.0 | 0.004 | 13/38 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM |  | **0.822×** | -3.7 | 0.013 | 5/38 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.013 | 12/34 (AN3 CA, HCT15, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | **0.755×** | -3.5 | 0.028 | 11/35 (HOP62, H4, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.611×** | -3.4 | 0.028 | 10/35 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 23.5 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -13.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -11.2) |
| [[A-427 (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -8.5) |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0828× (z -9.6) |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 3.63 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.05 µM 0.0459× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 66.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCN8A]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[FAM171B]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[LRRN2]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[WIPF3]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[GLIPR2]] | +0.54 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ZNF483]] | +0.53 | +0.39 / +0.66 | both halves | 6e-05 |  |
| [[FAM184A]] | +0.53 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[HAGLR]] | +0.53 | +0.28 / +0.60 | both halves | 3e-04 |  |
| [[RHBDL3]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SYNM]] | +0.52 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PAK1]] | +0.52 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[MARK1]] | +0.52 | +0.40 / +0.59 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCTN3]] | -0.53 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[NDUFV1]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[GALK2]] | -0.47 | -0.29 / -0.39 | both halves | 3e-04 |  |
| [[DZANK1]] | -0.45 | -0.14 / -0.41 | ⚠ not reproduced | 0.002 |  |
| [[CA5B]] | -0.45 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[FUCA1]] | -0.45 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ALDH6A1]] | -0.44 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[RSPRY1]] | -0.44 | -0.25 / -0.52 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APBB1]] | B | APBB1 activity raises CCDC136's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without APBB1 | 0.035 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[MSI1]] | B | MSI1 activity strengthens CCDC136's drug response | lines that do not express MSI1 (19) vs lines expressing it (19) | the lines without MSI1 respond 0.84× as strongly (z diff +0.68); strongest at Ouabain (Octahydrate) 0.5 µM: 0.71x vs 0.40x (z diff +2.8) | 0.040 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; target measured in part of the lines; artifact flags |
| [[EBF4]] | B | EBF4 activity raises CCDC136's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.40× lower at baseline in the lines without EBF4 | 0.040 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[RHBDL3]] | B | RHBDL3 activity raises CCDC136's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 3.05× lower at baseline in the lines without RHBDL3 | 0.047 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[SYNM]] | B | SYNM activity raises CCDC136's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without SYNM | 0.052 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[SPEG]] | C | SPEG activity raises CCDC136's level | lines that do not express SPEG (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without SPEG | 0.055 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APBB1]] | B | CCDC136 activity raises APBB1's level | lines that do not express CCDC136 (10) vs lines expressing it (40) | 2.93× lower at baseline in the lines without CCDC136 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, RECK, ENSG00000267405; maybe low, not absent |
| [[SCD5]] | B | CCDC136 activity raises SCD5's level | lines that do not express CCDC136 (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without CCDC136 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, RECK, ENSG00000267405; maybe low, not absent |
| cells under [[Daptomycin (drug)]] 5 µM | B | CCDC136 activity lowers the cells' numbers under Daptomycin 5 µM (makes them more sensitive) | lines that do not express CCDC136 (10) vs lines expressing it (38) | the lines without CCDC136: 1.20× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, RECK, ENSG00000267405; maybe low, not absent; cell counts less trustworthy |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (5.2, 35.3); signed map (29.5, 25.1). **Vector** length 62.2, 10.6% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.7 | -4.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 136 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,790,757-128,822,132 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1793, NAG6, DKFZP434G156 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JN2](https://www.uniprot.org/uniprotkb/Q96JN2) (Coiled-coil domain-containing protein 136):

> May play a role in acrosome formation in spermatogenesis and in fertilization.

**Summary**, from NCBI Gene [64753](https://www.ncbi.nlm.nih.gov/gene/64753):

> Predicted to be involved in acrosome assembly and single fertilization. Predicted to be located in cytoplasmic vesicle. Predicted to be active in acrosomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:22225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22225) · Entrez [64753](https://www.ncbi.nlm.nih.gov/gene/64753) · UniProt [Q96JN2](https://www.uniprot.org/uniprotkb/Q96JN2) · Ensembl [ENSG00000128596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128596)

## Data

Gene col 4901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4901); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4901]; `tensor/DDL_lfc|DDL_z.npy` [4901]; `embed/gene_vectors.npy` [4901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4901 or target_col == 4901). Every well: [[CCDC136 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC136.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
