---
symbol: "PSD4"
type: "gene"
col: 4636
ensembl_id: "ENSG00000125637"
name: "pleckstrin and Sec7 domain containing 4"
location: "2q14.1"
module: 31
arm: "+"
pooled_cpm: 12.86
n_lines_expressing: 42
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 32
direction_downstream: 4
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PSD4

*pleckstrin and Sec7 domain containing 4* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.57× (z +6.2, q 3e-07, up in 8 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.35× (z +4.2, q 0.008, up in 13 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.317× (z -23.3, q 0e+00, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM83H]] (+0.60, fdr 1e-05), [[IQANK1]] (+0.59, fdr 1e-05), [[TMEM184A]] (+0.57, fdr 5e-05); moves opposite to [[UFSP2]] (-0.51, fdr 3e-05), [[GPC6]] (-0.48, fdr 8e-05), [[IFT122]] (-0.47, fdr 5e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[UCA1]] → it (grade B ⚠); 4 go from it, the strongest it → [[ZNF710]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.2 | 3e-07 | 8/20 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.008 | 13/39 (NCI-H1573, HCT15, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.020 | 5/36 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.30×** | +3.6 | 0.038 | 14/39 (SW48, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.063 | 13/39 (NCI-H460, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.098 | 5/39 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | 1.51× | +3.1 | 0.16 | 6/33 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.317×** | -23.3 | 0e+00 | 34/37 (A-172, COLO 205, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.295×** | -17.5 | 0e+00 | 33/39 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.310×** | -16.8 | 0e+00 | 34/39 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.322×** | -16.2 | 0e+00 | 34/39 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.379×** | -13.9 | 8e-42 | 33/39 (LoVo, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.365×** | -13.9 | 8e-42 | 33/38 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.516×** | -9.5 | 3e-19 | 24/37 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.543×** | -8.7 | 2e-16 | 24/39 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.573×** | -8.0 | 1e-13 | 24/38 (BT-474, COLO 205, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -7.4 | 1e-11 | 21/38 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.621×** | -6.8 | 5e-10 | 25/39 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.415×** | -6.6 | 2e-09 | 23/39 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.632×** | -6.6 | 2e-09 | 22/39 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.671×** | -5.5 | 2e-06 | 22/34 (PANC-1, RKO, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.495×** | -5.3 | 6e-06 | 18/38 (A-172, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.705×** | -4.7 | 8e-05 | 18/39 (Hs 766T, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -4.4 | 3e-04 | 15/39 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.577×** | -4.1 | 0.001 | 12/40 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.769×** | -3.8 | 0.005 | 15/39 (A-427, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.6 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0345× (z -27.3) |
| [[SW480 (line)]] | alt | 37.7 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -13.4) |
| [[LoVo (line)]] | wt | 14.9 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -14.8) |
| [[LS 180 (line)]] | wt | 23.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -16.2) |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0178× (z -25.5) |
| [[BT-474 (line)]] | alt | 34.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -18.2) |
| [[COLO 205 (line)]] | alt | 53.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -22.7) |
| [[KATO III (line)]] | alt | 23.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.5) |
| [[HT-29 (line)]] | alt | 23.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0561× (z -21.7) |
| [[AsPC-1 (line)]] | alt | 26.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -14.8) |
| [[RKO (line)]] | wt | 12.7 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0768× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.140× (z -8.5) |
| [[A-427 (line)]] | wt | 10.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.115× (z -10.6) |
| [[HOP62 (line)]] | alt | 7.65 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 7.22 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0653× (z -15.7) |
| [[NCI-H2030 (line)]] | alt | 3.98 | 0 | 2 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0674× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -10.4) |
| [[PANC-1 (line)]] | alt | 3.41 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0422× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.146× (z -11.1) |
| [[SW48 (line)]] | wt | 17.3 | 0 | 2 | — | [[Bicalutamide (drug)]] 0.5 µM 0.0584× (z -11.5) |
| [[A549 (line)]] | wt | 7.00 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0851× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 8.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 6.77 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -9.5) |
| [[SW 900 (line)]] | alt | 9.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -12.6) |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.6) |
| [[A498 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM83H]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[IQANK1]] | +0.59 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[TMEM184A]] | +0.57 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[ACSL5]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[MST1R]] | +0.55 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[IL1RN]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 | ⚠ same locus (23.3 kb, same strand: neighbours can correlate without regulation) |
| [[PAX8-AS1]] | +0.54 | +0.45 / +0.55 | both halves | 3e-05 | ⚠ same locus (2.0 kb, same strand: neighbours can correlate without regulation) |
| [[TMEM30B]] | +0.54 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[SLC25A25-AS1]] | +0.54 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[ZBTB7C]] | +0.53 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[SLC16A5]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[CAPN8]] | +0.53 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[DMTN]] | +0.52 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[TMC6]] | +0.52 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFSP2]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[GPC6]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[IFT122]] | -0.47 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[WDR54]] | -0.47 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[ZNF652]] | -0.46 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[LIX1L]] | -0.46 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[KANTR]] | -0.45 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[ST8SIA4]] | -0.45 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[MFF]] | -0.44 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[RARB]] | -0.44 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[PXK]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[NKTR]] | -0.44 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 30, C 2. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UCA1]] | B | UCA1 activity raises PSD4's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without UCA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ |
| [[B3GNT3]] | B | B3GNT3 activity raises PSD4's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without B3GNT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[LAD1]] | B | LAD1 activity raises PSD4's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 3.27× lower at baseline in the lines without LAD1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[TNNT2]] | B | TNNT2 activity raises PSD4's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 3.16× lower at baseline in the lines without TNNT2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[C6orf132]] | B | C6orf132 activity raises PSD4's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 3.12× lower at baseline in the lines without C6orf132 | 0.008 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[C1orf116]] | B | C1orf116 activity raises PSD4's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 3.19× lower at baseline in the lines without C1orf116 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[DMKN]] | B | DMKN activity raises PSD4's level | lines that do not express DMKN (24) vs lines expressing it (26) | 2.28× lower at baseline in the lines without DMKN | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[SLC16A5]] | B | SLC16A5 activity raises PSD4's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 2.72× lower at baseline in the lines without SLC16A5 | 0.017 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[EVPL]] | B | EVPL activity raises PSD4's level | lines that do not express EVPL (16) vs lines expressing it (34) | 2.71× lower at baseline in the lines without EVPL | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: PTK6, MYO5C, SFN |
| [[SLC22A3]] | B | SLC22A3 activity raises PSD4's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without SLC22A3 | 0.026 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA |
| [[ESRP2]] | B | ESRP2 activity raises PSD4's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 3.08× lower at baseline in the lines without ESRP2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[ALS2CL]] | B | ALS2CL activity raises PSD4's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.69× lower at baseline in the lines without ALS2CL | 0.032 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF710]] | B | PSD4 activity raises ZNF710's level | lines that do not express PSD4 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without PSD4 | 0.064 | ⚠ within organs, on part of the lines; also absent: TBILA, SH2D4A, GPR39 |
| [[FSCN2]] | B | PSD4 activity raises FSCN2's level | lines that do not express PSD4 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without PSD4 | 0.073 | ⚠ within organs, on part of the lines; also absent: TBILA, SH2D4A, GPR39 |
| cells under [[Arbutin (drug)]] 5 µM | B | PSD4 activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express PSD4 (8) vs lines expressing it (40) | the lines without PSD4: 0.75× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TBILA, SH2D4A, GPR39 |
| [[PKP3]] | C | PSD4 activity raises PKP3's level | lines that do not express PSD4 (8) vs lines expressing it (42) | 4.14× lower at baseline in the lines without PSD4 | 0.091 | ⚠ within organs, on part of the lines; also absent: TBILA, SH2D4A, GPR39; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.4, 53.6); signed map (58.4, 10.1). **Vector** length 69.6, 13.2% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +0.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +3.5 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.4 | -13.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.3 | -13.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.1 | -1.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin and Sec7 domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:113,157,325-113,209,396 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIC, EFA6B |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Pleckstrin and Sec7 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDX1](https://www.uniprot.org/uniprotkb/Q8NDX1) (PH and SEC7 domain-containing protein 4):

> Guanine nucleotide exchange factor for ARF6 and ARL14/ARF7. Through ARL14 activation, controls the movement of MHC class II-containing vesicles along the actin cytoskeleton in dendritic cells. Involved in membrane recycling. Interacts with several phosphatidylinositol phosphate species, including phosphatidylinositol 3,4-bisphosphate, phosphatidylinositol 3,5-bisphosphate and phosphatidylinositol 4,5-bisphosphate.

**Summary**, from NCBI Gene [23550](https://www.ncbi.nlm.nih.gov/gene/23550):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in vesicle-mediated transport. Located in ruffle membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19096) · Entrez [23550](https://www.ncbi.nlm.nih.gov/gene/23550) · UniProt [Q8NDX1](https://www.uniprot.org/uniprotkb/Q8NDX1) · Ensembl [ENSG00000125637](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125637)

## Data

Gene col 4636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4636); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4636]; `tensor/DDL_lfc|DDL_z.npy` [4636]; `embed/gene_vectors.npy` [4636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4636 or target_col == 4636). Every well: [[PSD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
