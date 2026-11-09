---
symbol: "TMEM170B"
type: "gene"
col: 12963
ensembl_id: "ENSG00000205269"
name: "transmembrane protein 170B"
location: "6p24.2"
module: 19
arm: "+"
pooled_cpm: 7.0
n_lines_expressing: 42
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# TMEM170B

*transmembrane protein 170B* — 6p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.67× (z +16.4, q 0e+00, up in 33 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.272× (z -13.8, q 1e-40, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASF3]] (+0.62, fdr 4e-05), [[EBF2]] (+0.61, fdr 1e-05), [[COL4A4]] (+0.60, fdr 3e-05); moves opposite to [[COMMD1]] (-0.62, fdr 1e-05), [[ATXN1L]] (-0.60, fdr 1e-04), [[EFCAB2]] (-0.58, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[UNC13A]] → it (grade B ⚠); 7 go from it, the strongest it → [[SSPOP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12963.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.67×** | +16.4 | 0e+00 | 33/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.84×** | +15.7 | 0e+00 | 36/38 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.86×** | +14.3 | 2e-44 | 31/38 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.86×** | +14.3 | 2e-44 | 34/38 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.30×** | +12.7 | 8e-35 | 36/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.16×** | +12.2 | 2e-32 | 30/34 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.54×** | +8.4 | 4e-15 | 31/35 (J82, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.19×** | +8.3 | 6e-15 | 28/34 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.52×** | +6.3 | 2e-08 | 16/37 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.006 | 9/39 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.007 | 5/37 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.007 | 8/39 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.6 | 0.015 | 2/6 (SNU-423, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.084 | 6/38 (NCI-H23, SW 900, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.085 | 5/32 (SHP-77, HT-29, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12963.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.272×** | -13.8 | 1e-40 | 32/40 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.350×** | -11.1 | 2e-26 | 27/32 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.433×** | -8.9 | 1e-16 | 27/37 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.468×** | -7.8 | 1e-12 | 22/37 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.496×** | -7.4 | 1e-11 | 26/36 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.523×** | -6.9 | 6e-10 | 23/36 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.532×** | -6.7 | 2e-09 | 20/38 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -5.7 | 7e-07 | 22/37 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.602×** | -5.4 | 5e-06 | 16/35 (SW1417, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.725×** | -4.8 | 8e-05 | 16/34 (NCI-H460, NCI-H23, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.635×** | -4.5 | 3e-04 | 15/35 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.656×** | -4.5 | 4e-04 | 8/39 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.684×** | -4.0 | 0.003 | 13/40 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.688×** | -4.0 | 0.003 | 14/32 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.517×** | -3.7 | 0.010 | 9/16 (A-427, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12963. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.3 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -17.5) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0752× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0600× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0629× (z -13.6) |
| [[PANC-1 (line)]] | alt | 2.68 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 7.00× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -10.7) ⚠ cell-cycle shift, explains ~67% of this change |
| [[J82 (line)]] | alt | 20.0 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.81× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.0694× (z -15.4) |
| [[LoVo (line)]] | wt | 7.84 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0655× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0646× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -11.2) |
| [[A-427 (line)]] | wt | 18.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0876× (z -15.2) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.254× (z -8.5) |
| [[SW480 (line)]] | alt | 5.32 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.25× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.134× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 7.11 | 0 | 1 | — | [[Cilostazol (drug)]] 0.05 µM 0.117× (z -8.5) |
| [[BT-474 (line)]] | alt | 5.19 | 0 | 1 | — | [[Osimertinib (mesylate) (drug)]] 5 µM 0.0595× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 9.06 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0446× (z -10.5) |
| [[HOP62 (line)]] | alt | 2.01 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 21.5× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 6.22 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0671× (z -10.9) |
| [[A-172 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.947 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.513 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12963), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | +0.62 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[EBF2]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[COL4A4]] | +0.60 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PRKAR2B]] | +0.60 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[GLRB]] | +0.59 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[MMP17]] | +0.59 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[UNC13A]] | +0.57 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[RIMKLA]] | +0.57 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[GDE1]] | +0.57 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[SNCA]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[RAB6B]] | +0.56 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[FHL1]] | +0.56 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD1]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ATXN1L]] | -0.60 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.58 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[SLC25A17]] | -0.56 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.55 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[LINC01004]] | -0.55 | -0.24 / -0.42 | both halves | 4e-04 |  |
| [[RCC1L]] | -0.54 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[SPART-AS1]] | -0.54 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[ANKRD17-DT]] | -0.54 | -0.27 / -0.31 | both halves | 3e-04 |  |
| [[DGLUCY]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[C1orf54]] | -0.53 | -0.24 / -0.45 | both halves | 5e-04 |  |
| [[ITPA]] | -0.52 | -0.23 / -0.48 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC13A]] | B | UNC13A activity raises TMEM170B's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 2.51× lower at baseline in the lines without UNC13A | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |
| [[CNKSR2]] | B | CNKSR2 activity raises TMEM170B's level | lines that do not express CNKSR2 (32) vs lines expressing it (18) | 2.45× lower at baseline in the lines without CNKSR2 | 0.052 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CDH10, CDH19; maybe low, not absent |
| [[SSPOP]] | B | SSPOP activity raises TMEM170B's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without SSPOP | 0.083 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[CBX2]] | B | CBX2 activity raises TMEM170B's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without CBX2 | 0.095 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSPOP]] | B | TMEM170B activity raises SSPOP's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without TMEM170B | 0.014 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[RNFT2]] | B | TMEM170B activity raises RNFT2's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 1.82× lower at baseline in the lines without TMEM170B | 0.066 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[TMOD2]] | B | TMEM170B activity raises TMOD2's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 2.38× lower at baseline in the lines without TMEM170B | 0.072 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[RNF182]] | B | TMEM170B activity raises RNF182's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 2.63× lower at baseline in the lines without TMEM170B | 0.079 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[PRKAR2B]] | B | TMEM170B activity raises PRKAR2B's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 3.22× lower at baseline in the lines without TMEM170B | 0.084 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[SFMBT2]] | B | TMEM170B activity raises SFMBT2's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 3.32× lower at baseline in the lines without TMEM170B | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[VPS13A]] | B | TMEM170B activity raises VPS13A's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without TMEM170B | 0.095 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.381). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.1, 39.7); signed map (40.0, 47.8). **Vector** length 75.1, 14.7% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +15.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +12.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +12.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +8.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.4 | +14.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.8 | +6.3 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.2 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.9 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -13.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 170B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p24.2 — chr6:11,537,749-11,583,524 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T4T1](https://www.uniprot.org/uniprotkb/Q5T4T1) (Transmembrane protein 170B):

> Negatively regulates the canonical Wnt signaling in breast cancer cells. Exerts an inhibitory effect on breast cancer growth by inhibiting CTNNB1 stabilization and nucleus translocation, which reduces the activity of Wnt targets.

**Summary**, from NCBI Gene [100113407](https://www.ncbi.nlm.nih.gov/gene/100113407):

> Involved in negative regulation of canonical Wnt signaling pathway. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:34244](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34244) · Entrez [100113407](https://www.ncbi.nlm.nih.gov/gene/100113407) · UniProt [Q5T4T1](https://www.uniprot.org/uniprotkb/Q5T4T1) · Ensembl [ENSG00000205269](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205269)

## Data

Gene col 12963: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12963); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12963, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12963]; `tensor/DDL_lfc|DDL_z.npy` [12963]; `embed/gene_vectors.npy` [12963]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12963 or target_col == 12963). Every well: [[TMEM170B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM170B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
