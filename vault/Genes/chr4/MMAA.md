---
symbol: "MMAA"
type: "gene"
col: 7539
ensembl_id: "ENSG00000151611"
name: "metabolism of cobalamin associated A"
location: "4q31.21"
module: 7
arm: "+"
pooled_cpm: 6.18
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MMAA

*metabolism of cobalamin associated A* — 4q31.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +11.2, q 3e-26, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.553× (z -8.3, q 4e-14, down in 21 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM: 0.707× (z -4.9, q 1e-04, down in 15 of 43 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTPBP10]] (+0.56, fdr 3e-05), [[INTS12]] (+0.52, fdr 7e-05), [[SMAD1]] (+0.48, fdr 7e-05, ⚠ same locus), [[C18orf25]] (+0.48, fdr 2e-04); moves opposite to [[ATP1B3]] (-0.52, fdr 5e-05), [[C8orf88]] (-0.49, fdr 7e-05), [[OSBPL8]] (-0.48, fdr 9e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[KDF1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7539.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.2 | 3e-26 | 24/40 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.75×** | +7.5 | 3e-11 | 23/41 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.007 | 6/44 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.27× | +3.3 | 0.11 | 8/47 (AsPC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.24 | 3/45 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.50× | +3.0 | 0.24 | 5/38 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7539.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.553×** | -8.3 | 4e-14 | 21/39 (LS 180, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.558×** | -8.2 | 6e-14 | 25/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.685×** | -5.3 | 2e-05 | 17/44 (HepG2/C3A, SW 900, …) | all doses, stronger at high dose |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM |  | **0.707×** | -4.9 | 1e-04 | 15/43 (SK-MEL-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.703×** | -4.8 | 2e-04 | 17/30 (LoVo, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.720×** | -4.6 | 3e-04 | 17/28 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.736×** | -4.3 | 0.001 | 16/44 (SHP-77, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.767×** | -3.6 | 0.024 | 13/44 (LOX-IMVI, A498, …) | top dose only | composition shift |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.781×** | -3.5 | 0.032 | 6/42 (SHP-77, HCT15, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.798×** | -3.2 | 0.084 | 10/43 (A549, NCI-H2030, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.793×** | -3.1 | 0.084 | 12/36 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7539. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0654× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 3.85 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 9.28 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0908× (z -8.9) |
| [[HOP62 (line)]] | alt | 2.82 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0957× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 4.64 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0707× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[KATO III (line)]] | alt | 8.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 6.50 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.07 | 0 | 1 | — | [[Busulfan (drug)]] 0.5 µM 0.0782× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 7.44 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0868× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 5.97 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[A-172 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7539), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTPBP10]] | +0.56 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[INTS12]] | +0.52 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[SMAD1]] | +0.48 | +0.51 / +0.37 | both halves | 7e-05 | ⚠ same locus (39.9 kb, same strand: neighbours can correlate without regulation) |
| [[C18orf25]] | +0.48 | +0.55 / +0.29 | both halves | 2e-04 |  |
| [[SPATA2]] | +0.48 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[TMEM9B]] | +0.48 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[FASTKD3]] | +0.48 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[CNOT11]] | +0.48 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[GCC1]] | +0.47 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[ZNF777]] | +0.47 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[ZNF7]] | +0.46 | +0.52 / +0.32 | both halves | 2e-04 |  |
| [[TFIP11]] | +0.46 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[DET1]] | +0.46 | +0.54 / +0.26 | both halves | 4e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP1B3]] | -0.52 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[C8orf88]] | -0.49 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[OSBPL8]] | -0.48 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[CCDC88A]] | -0.45 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[ODF2L]] | -0.43 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[TGFB1]] | -0.40 | -0.50 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[LIMS1]] | -0.40 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[STARD9]] | -0.40 | -0.38 / -0.29 | both halves | 3e-04 |  |
| [[ERC1]] | -0.39 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[CDK14]] | -0.38 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[CSPP1]] | -0.38 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[SPATS2]] | -0.38 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ANKRD36]] | -0.38 | -0.43 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KDF1]] | B | KDF1 activity raises MMAA's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.53× lower at baseline in the lines without KDF1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[STARD9]] | B | STARD9 activity lowers MMAA's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.81× higher at baseline in the lines without STARD9 | 0.003 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[INAVA]] | B | INAVA activity raises MMAA's level | lines that do not express INAVA (29) vs lines expressing it (21) | 1.53× lower at baseline in the lines without INAVA | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[HNF4G]] | B | HNF4G activity raises MMAA's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without HNF4G | 0.034 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[CCDC88A]] | B | CCDC88A activity lowers MMAA's level | lines that do not express CCDC88A (8) vs lines expressing it (42) | 1.60× higher at baseline in the lines without CCDC88A | 0.037 | ⚠ within organs, on part of the lines; also absent: LIX1L, HEG1, CHROMR |
| [[PDZK1IP1]] | B | PDZK1IP1 activity raises MMAA's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 1.42× lower at baseline in the lines without PDZK1IP1 | 0.068 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8 |
| [[HSH2D]] | B | HSH2D activity raises MMAA's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.36× lower at baseline in the lines without HSH2D | 0.086 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.348). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.6, 5.6); signed map (-8.4, -24.7). **Vector** length 54.8, 6.94% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +2.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -2.7 | -8.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | -2.5 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | -2.5 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.4 | -8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.3 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | metabolism of cobalamin associated A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.21 — chr4:145,599,042-145,660,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | cblA |
| Reactome | 11 pathways, smallest: Propionyl-CoA catabolism; Cobalamin (Cbl) metabolism; Defects in cobalamin (B12) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVH4](https://www.uniprot.org/uniprotkb/Q8IVH4) (Methylmalonic aciduria type A protein, mitochondrial):

> GTPase, binds and hydrolyzes GTP. Involved in intracellular vitamin B12 metabolism, mediates the transport of cobalamin (Cbl) into mitochondria for the final steps of adenosylcobalamin (AdoCbl) synthesis. Functions as a G protein chaperone that assists AdoCbl cofactor delivery from MMAB to the methylmalonyl-CoA mutase (MMUT). Plays a dual role as both a protectase and a reactivase for MMUT. Protects MMUT from progressive inactivation by oxidation by decreasing the rate of the formation of the …

**Summary**, from NCBI Gene [166785](https://www.ncbi.nlm.nih.gov/gene/166785):

> The protein encoded by this gene is involved in the translocation of cobalamin into the mitochondrion, where it is used in the final steps of adenosylcobalamin synthesis. Adenosylcobalamin is a coenzyme required for the activity of methylmalonyl-CoA mutase. Defects in this gene are a cause of methylmalonic aciduria. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18871](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18871) · Entrez [166785](https://www.ncbi.nlm.nih.gov/gene/166785) · UniProt [Q8IVH4](https://www.uniprot.org/uniprotkb/Q8IVH4) · Ensembl [ENSG00000151611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151611)

## Data

Gene col 7539: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7539); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7539, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7539]; `tensor/DDL_lfc|DDL_z.npy` [7539]; `embed/gene_vectors.npy` [7539]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7539 or target_col == 7539). Every well: [[MMAA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMAA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
