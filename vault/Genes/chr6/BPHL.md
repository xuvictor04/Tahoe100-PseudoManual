---
symbol: "BPHL"
type: "gene"
col: 5995
ensembl_id: "ENSG00000137274"
name: "biphenyl hydrolase like"
location: "6p25.2"
module: 96
arm: "+"
pooled_cpm: 11.83
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# BPHL

*biphenyl hydrolase like* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.07× (z +9.5, q 9e-19, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.488× (z -9.4, q 2e-18, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UROS]] (+0.71, fdr 7e-06), [[ERMARD]] (+0.64, fdr 1e-05), [[LYRM9]] (+0.62, fdr 1e-05); moves opposite to [[RAB5IF]] (-0.52, fdr 3e-05), [[IL20RB]] (-0.51, fdr 2e-05), [[ISY1-RAB43]] (-0.51, fdr 5e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC113]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +9.5 | 9e-19 | 37/47 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +9.0 | 5e-17 | 41/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.51×** | +5.4 | 1e-05 | 22/47 (KATO III, A498, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.3 | 1e-05 | 23/45 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.0 | 8e-05 | 16/39 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +4.9 | 1e-04 | 15/47 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.5 | 7e-04 | 15/48 (C32, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +4.4 | 7e-04 | 15/47 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.25×** | +4.1 | 0.003 | 18/48 (HOP62, A498, …) | top dose only | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.1 | 0.003 | 10/22 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.006 | 16/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.31×** | +3.5 | 0.020 | 12/46 (A549, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.020 | 10/46 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.31×** | +3.5 | 0.022 | 13/46 (HT-29, A498, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.026 | 13/48 (SW1417, RKO, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.034 | 7/42 (SW480, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +3.3 | 0.034 | 4/48 (SW480, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.038 | 5/48 (SW480, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.069 | 11/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.093 | 4/47 (SNU-423, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5995.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.488×** | -9.4 | 2e-18 | 35/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -8.8 | 3e-16 | 34/46 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.517×** | -8.2 | 5e-14 | 29/46 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.555×** | -7.7 | 1e-12 | 31/47 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.583×** | -7.1 | 2e-10 | 30/47 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.623×** | -6.2 | 4e-08 | 27/47 (LOX-IMVI, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.629×** | -6.1 | 9e-08 | 30/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.640×** | -5.9 | 3e-07 | 26/47 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -4.6 | 3e-04 | 19/39 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.529×** | -4.4 | 7e-04 | 19/43 (RKO, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.537×** | -4.3 | 0.001 | 19/47 (LOX-IMVI, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.746×** | -3.9 | 0.005 | 16/48 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **0.788×** | -3.1 | 0.076 | 9/46 (hTERT-HPNE, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | 0.645× | -3.0 | 0.10 | 14/32 (C-33 A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -10.3) |
| [[SW480 (line)]] | alt | 10.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -9.9) |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0782× (z -12.4) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.165× (z -8.8) |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 2 | — | [[Vilanterol (drug)]] 0.5 µM 0.0906× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 9.73 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Hydroxyurea (drug)]] 0.05 µM 0.0441× (z -13.3) |
| [[C32 (line)]] | wt | 8.69 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.121× (z -8.6) |
| [[J82 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.205× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 9.22 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.142× (z -9.4) |
| [[SW48 (line)]] | wt | 13.1 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0858× (z -8.7) |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UROS]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[ERMARD]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[LYRM9]] | +0.62 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TMEM128]] | +0.58 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[TKFC]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[DHRS12]] | +0.57 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SPATA20]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SLC35A5]] | +0.56 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[RNF141]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[DMTF1]] | +0.54 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[HYI]] | +0.54 | +0.56 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5IF]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[IL20RB]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ISY1-RAB43]] | -0.51 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[SFXN5]] | -0.50 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[TVP23C-CDRT4]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[NUP88]] | -0.48 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[SMBD1P]] | -0.47 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[WNT2B]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[BIRC6]] | -0.47 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[LIN52]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ATP2A1]] | -0.47 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[LYG1]] | -0.46 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC113]] | C | CCDC113 activity raises BPHL's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without CCDC113 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-27.8, 22.0); signed map (16.5, -41.7). **Vector** length 57.6, 8.47% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +2.5 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.1 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -5.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -2.2 | +0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +3.4 |

## What is on record

|  |  |
|---|---|
| Name | biphenyl hydrolase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:3,118,374-3,153,578 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Bph-rp, VACVase; previously MCNAA |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WA6](https://www.uniprot.org/uniprotkb/Q86WA6) (Serine hydrolase BPHL):

> Specific alpha-amino acid ester serine hydrolase that prefers small, hydrophobic, and aromatic side chains and does not have a stringent requirement for the leaving group other than preferring a primary alcohol. Has homocysteine-thiolactonase activity (in vitro) and may play a significant role in the detoxification of homocysteine thiolactone in vivo. Catalyzes the hydrolytic activation of amino acid ester prodrugs of nucleoside analogs such as valacyclovir and valganciclovir, converting them …

**Summary**, from NCBI Gene [670](https://www.ncbi.nlm.nih.gov/gene/670):

> This gene encodes a member of the serine protease family of hydrolytic enzymes which contain a serine in their active site. The encoded protein may play a role in activation of the antiviral prodrug valacyclovir. Alternatively spliced transcript variants have been described.[provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:1094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1094) · Entrez [670](https://www.ncbi.nlm.nih.gov/gene/670) · UniProt [Q86WA6](https://www.uniprot.org/uniprotkb/Q86WA6) · Ensembl [ENSG00000137274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137274)

## Data

Gene col 5995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5995); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5995]; `tensor/DDL_lfc|DDL_z.npy` [5995]; `embed/gene_vectors.npy` [5995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5995 or target_col == 5995). Every well: [[BPHL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BPHL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
