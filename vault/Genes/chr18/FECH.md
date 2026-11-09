---
symbol: "FECH"
type: "gene"
col: 843
ensembl_id: "ENSG00000066926"
name: "ferrochelatase"
location: "18q21.31"
module: 25
arm: "+"
pooled_cpm: 11.41
n_lines_expressing: 49
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# FECH

*ferrochelatase* — 18q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.33× (z +16.8, q 0e+00, up in 17 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.62× (z +7.0, q 4e-10, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.658× (z -6.1, q 5e-07, down in 25 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.666× (z -6.0, q 7e-07, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN1]] (+0.75, fdr 1e-05), [[RAD23B]] (+0.71, fdr 1e-04), [[EWSR1]] (+0.70, fdr 7e-06); moves opposite to [[DDT]] (-0.59, fdr 1e-05), [[UBL5]] (-0.58, fdr 1e-05), [[NDUFA2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MYO1E]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.33×** | +16.8 | 0e+00 | 17/18 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.79×** | +14.9 | 0e+00 | 32/38 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +11.7 | 4e-29 | 22/27 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +7.0 | 4e-10 | 26/46 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +6.7 | 2e-09 | 21/46 (HEC-1-A, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +6.5 | 7e-09 | 21/47 (CFPAC-1, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +6.4 | 1e-08 | 24/47 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.7 | 6e-07 | 5/47 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +5.7 | 6e-07 | 21/46 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +5.7 | 9e-07 | 22/46 (LoVo, BT-474, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +5.5 | 2e-06 | 22/47 (LS 180, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 2e-06 | 23/46 (HOP62, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 1e-05 | 22/46 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +4.8 | 7e-05 | 17/45 (LoVo, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.40×** | +4.7 | 9e-05 | 18/40 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +4.3 | 5e-04 | 12/46 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 11/47 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.006 | 11/46 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.045 | 5/46 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.045 | 7/46 (BT-474, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -6.1 | 5e-07 | 25/44 (SHP-77, SNU-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -6.0 | 7e-07 | 24/46 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -5.2 | 2e-05 | 20/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.700×** | -5.2 | 2e-05 | 17/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PF-06260933 (drug)]] 5 µM |  | 0.669× | -3.1 | 0.23 | 9/45 (KATO III, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.01 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.21× (z +10.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 2 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.0487× (z -10.6) |
| [[J82 (line)]] | alt | 14.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.96× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 23.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 12.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.9) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -10.1) |
| [[A549 (line)]] | wt | 11.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.34× (z +10.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 6.26 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0633× (z -11.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 7.10 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.26× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.21× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 8.29 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.8× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0470× (z -15.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0651× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN1]] | +0.75 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.71 | +0.35 / +0.69 | both halves | 1e-04 |  |
| [[EWSR1]] | +0.70 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[NUDT9]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[DLD]] | +0.69 | +0.65 / +0.76 | both halves | 7e-06 | pathway: Mitochondrial protein degradation |
| [[PFKM]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[MRPL9]] | +0.67 | +0.72 / +0.45 | both halves | 3e-05 |  |
| [[PSMD11]] | +0.67 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[GPN1]] | +0.66 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[NCKAP1]] | +0.66 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[GSR]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDT]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[UBL5]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[NDUFA2]] | -0.56 | -0.43 / -0.48 | both halves | 3e-05 | pathway: Mitochondrial protein degradation |
| [[NUDT22]] | -0.56 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[TRPT1]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ELL]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TMSB10]] | -0.56 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[HIC2]] | -0.56 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.55 | -0.52 / -0.46 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[INAFM1]] | -0.55 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[RABGEF1]] | -0.55 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[ATP5MK]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R13L]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO1E]] | B | MYO1E activity lowers FECH's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 2.10× higher at baseline in the lines without MYO1E | 0.040 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[CFL2]] | C | CFL2 activity raises FECH's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.09× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |
| [[PLS3]] | C | PLS3 activity lowers FECH's level | lines that do not express PLS3 (4) vs lines expressing it (46) | 2.02× higher at baseline in the lines without PLS3 | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.4, -15.8); signed map (-16.0, -41.9). **Vector** length 74.7, 12.8% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +11.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.9 | +2.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -5.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.2 | +2.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.0 | -1.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ferrochelatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.31 — chr18:57,544,377-57,586,732 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 3 pathways, smallest: Heme biosynthesis; Metabolism of porphyrins; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P22830](https://www.uniprot.org/uniprotkb/P22830) (Ferrochelatase, mitochondrial):

> Catalyzes the ferrous insertion into protoporphyrin IX and participates in the terminal step in the heme biosynthetic pathway.

**Summary**, from NCBI Gene [2235](https://www.ncbi.nlm.nih.gov/gene/2235):

> The protein encoded by this gene is localized to the mitochondrion, where it catalyzes the insertion of the ferrous form of iron into protoporphyrin IX in the heme synthesis pathway. Mutations in this gene are associated with erythropoietic protoporphyria. Two transcript variants encoding different isoforms have been found for this gene. A pseudogene of this gene is found on chromosome 3.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:3647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3647) · Entrez [2235](https://www.ncbi.nlm.nih.gov/gene/2235) · UniProt [P22830](https://www.uniprot.org/uniprotkb/P22830) · Ensembl [ENSG00000066926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066926)

## Data

Gene col 843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 843); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 843]; `tensor/DDL_lfc|DDL_z.npy` [843]; `embed/gene_vectors.npy` [843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 843 or target_col == 843). Every well: [[FECH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FECH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
