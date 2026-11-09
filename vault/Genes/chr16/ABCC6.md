---
symbol: "ABCC6"
type: "gene"
col: 1659
ensembl_id: "ENSG00000091262"
name: "ATP binding cassette subfamily C member 6"
location: "16p13.11"
module: 8
arm: "+"
pooled_cpm: 4.36
n_lines_expressing: 43
n_dd_up: 18
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ABCC6

*ATP binding cassette subfamily C member 6* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.69× (z +13.0, q 4e-36, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 1.47× (z +4.8, q 2e-04, up in 13 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.497× (z -7.3, q 2e-10, down in 17 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARSL]] (+0.68, fdr 7e-06), [[EPCAM-DT]] (+0.68, fdr 1e-05), [[A1CF]] (+0.63, fdr 1e-05); moves opposite to [[PHC2]] (-0.54, fdr 3e-05), [[PAQR5]] (-0.53, fdr 9e-05), [[CAPRIN2]] (-0.53, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[DCDC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.69×** | +13.0 | 4e-36 | 1/5 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +10.1 | 2e-21 | 7/15 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.40×** | +4.9 | 2e-04 | 16/37 (LoVo, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.9 | 2e-04 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 2e-04 | 13/34 (HepG2/C3A, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +4.7 | 2e-04 | 10/37 (HepG2/C3A, A498, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +4.7 | 2e-04 | 16/37 (AsPC-1, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.56×** | +4.6 | 3e-04 | 12/33 (HepG2/C3A, A498, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 6e-04 | 13/33 (SW480, AsPC-1, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.006 | 7/33 (HepG2/C3A, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.008 | 11/35 (HepG2/C3A, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.012 | 7/31 (HepG2/C3A, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.013 | 6/38 (HepG2/C3A, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.013 | 7/28 (HepG2/C3A, HEC-1-A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.41×** | +3.6 | 0.013 | 9/31 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.060 | 8/32 (HepG2/C3A, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.497×** | -7.3 | 2e-10 | 17/34 (RPMI-7951, A549, …) | all doses, flat | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.501×** | -7.2 | 2e-10 | 21/33 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.594×** | -5.4 | 1e-05 | 21/37 (A498, SW1417, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.602×** | -5.3 | 2e-05 | 21/39 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.674×** | -4.1 | 0.004 | 8/38 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.689×** | -3.9 | 0.010 | 12/32 (A498, HepG2/C3A, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.682×** | -3.8 | 0.010 | 2/36 (A498, NCI-H1792) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.708×** | -3.6 | 0.022 | 7/31 (A-172, PANC-1, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.715×** | -3.5 | 0.030 | 14/25 (NCI-H1792, J82, …) | all doses, flat | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.034 | 5/36 (SW1417, HOP62, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.719×** | -3.3 | 0.049 | 7/33 (RPMI-7951, A-427, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.732×** | -3.2 | 0.057 | 10/38 (NCI-H1573, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -3.1 | 0.091 | 11/38 (COLO 205, A498, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.746×** | -3.1 | 0.091 | 16/35 (A498, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 22.4 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -13.7) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 7.39 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0729× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 5.17 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0801× (z -8.8) |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.931 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARSL]] | +0.68 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[EPCAM-DT]] | +0.68 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[A1CF]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[HGD]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[HNF4G]] | +0.59 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[SLC44A3]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ACTR3C]] | +0.58 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[SEC16B]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[SULT1C2]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[POU5F1]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PREX2]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2]] | -0.54 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PAQR5]] | -0.53 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[CAPRIN2]] | -0.53 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SEPTIN10]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MFSD10]] | -0.52 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[S100A16]] | -0.52 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[SH3BGRL3]] | -0.51 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[CALM1]] | -0.49 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[BZW1]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZFYVE28]] | -0.48 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[RASA3]] | -0.48 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[ELOVL1]] | -0.48 | -0.47 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCDC2]] | B | DCDC2 activity raises ABCC6's level | lines that do not express DCDC2 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without DCDC2 | 0.011 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[SULT1C2]] | B | SULT1C2 activity raises ABCC6's level | lines that do not express SULT1C2 (30) vs lines expressing it (20) | 1.62× lower at baseline in the lines without SULT1C2 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC03040, EPS8L3, TMEM139 |
| [[EPCAM-DT]] | B | EPCAM-DT activity raises ABCC6's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.83× lower at baseline in the lines without EPCAM-DT | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[ACTR3C]] | B | ACTR3C activity raises ABCC6's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without ACTR3C | 0.022 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ABCC6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises ABCC6's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.74× lower at baseline in the lines without MTUS1-DT | 0.052 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[FRK]] | B | FRK activity raises ABCC6's level | lines that do not express FRK (22) vs lines expressing it (28) | 1.82× lower at baseline in the lines without FRK | 0.053 | ⚠ within organs, on part of the lines; also absent: GOLT1A, MYO5B, NCMAP |
| [[CP]] | B | CP activity raises ABCC6's level | lines that do not express CP (39) vs lines expressing it (11) | 1.84× lower at baseline in the lines without CP | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[PLCH1]] | B | PLCH1 activity raises ABCC6's level | lines that do not express PLCH1 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without PLCH1 | 0.082 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPR143]] | B | GPR143 activity raises ABCC6's level | lines that do not express GPR143 (19) vs lines expressing it (31) | 1.35× lower at baseline in the lines without GPR143 | 0.089 | ⚠ within organs, on part of the lines; also absent: SHROOM2, DCDC2, SCN5A; maybe low, not absent |
| [[HGD]] | B | HGD activity raises ABCC6's level | lines that do not express HGD (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without HGD | 0.089 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[LINC02904]] | B | LINC02904 activity raises ABCC6's level | lines that do not express LINC02904 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without LINC02904 | 0.092 | ⚠ within organs, on part of the lines; also absent: AQP3, B3GALNT1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.2, 51.2); signed map (56.9, -0.3). **Vector** length 54.0, 8.30% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.0 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.0 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +3.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.8 | -5.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | +0.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily C member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:16,149,565-16,223,522 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRP6, EST349056, MLP1, URG7; previously ARA, PXE |
| Gene groups (HGNC) | ATP binding cassette subfamily C |
| Reactome | 4 pathways, smallest: ABC transporter disorders; ABC-family protein mediated transport; Disorders of transmembrane transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [O95255](https://www.uniprot.org/uniprotkb/O95255) (ATP-binding cassette sub-family C member 6):

> [Isoform 1]: ATP-dependent transporter of the ATP-binding cassette (ABC) family that actively extrudes physiological compounds, and xenobiotics from cells. Mediates ATP-dependent transport of glutathione conjugates such as leukotriene-c4 (LTC4) and N-ethylmaleimide S-glutathione (NEM-GS) (in vitro), and an anionic cyclopentapeptide endothelin antagonist, BQ-123. May contribute to regulate the transport of organic compounds in testes across the blood-testis-barrier (Probable). Does not appear to …

**Summary**, from NCBI Gene [368](https://www.ncbi.nlm.nih.gov/gene/368):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). The encoded protein, a member of the MRP subfamily, is involved in multi-drug resistance. Mutations in this gene cause pseudoxanthoma elasticum. Alternatively spliced transcript variants that encode …

**Accessions** — [HGNC:57](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:57) · Entrez [368](https://www.ncbi.nlm.nih.gov/gene/368) · UniProt [O95255](https://www.uniprot.org/uniprotkb/O95255) · Ensembl [ENSG00000091262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091262)

## Data

Gene col 1659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1659); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1659]; `tensor/DDL_lfc|DDL_z.npy` [1659]; `embed/gene_vectors.npy` [1659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1659 or target_col == 1659). Every well: [[ABCC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
