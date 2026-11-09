---
symbol: "ASS1"
type: "gene"
col: 5102
ensembl_id: "ENSG00000130707"
name: "argininosuccinate synthase 1"
location: "9q34.11"
module: 8
arm: "+"
pooled_cpm: 32.34
n_lines_expressing: 36
n_dd_up: 6
n_dd_down: 48
n_dd_up_clean: 5
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 28
direction_downstream: 1
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ASS1

*argininosuccinate synthase 1* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.29× (z +3.9, q 0.027, up in 13 of 34 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.30× (z +3.9, q 0.027, up in 16 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (18 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.478× (z -10.9, q 8e-25, down in 22 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC44A4]] (+0.64, fdr 7e-06), [[TJP3]] (+0.62, fdr 1e-05), [[SLC50A1]] (+0.60, fdr 1e-05); moves opposite to [[SLC35B4]] (-0.58, fdr 1e-05), [[MSANTD2]] (-0.48, fdr 4e-05), [[TADA2A]] (-0.47, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[SLC44A4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[TMPRSS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5102.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +3.9 | 0.027 | 13/34 (LS 180, PANC-1, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.027 | 16/34 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.034 | 11/34 (CFPAC-1, LS 180, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.034 | 13/34 (LS 180, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.052 | 12/34 (CFPAC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.052 | 11/34 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.091 | 7/34 (KATO III, J82, …) | two highest doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.23× | +3.0 | 0.17 | 10/34 (CFPAC-1, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5102.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.478×** | -10.9 | 8e-25 | 22/33 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.494×** | -10.8 | 9e-25 | 28/33 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.501×** | -10.6 | 6e-24 | 24/31 (Panc 03.27, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -9.7 | 4e-20 | 21/32 (HT-29, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.534×** | -9.6 | 9e-20 | 26/34 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.543×** | -9.3 | 9e-19 | 25/34 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.536×** | -9.2 | 3e-18 | 24/32 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.568×** | -8.7 | 3e-16 | 23/34 (LoVo, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.572×** | -8.5 | 8e-16 | 25/34 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.576×** | -8.4 | 2e-15 | 25/34 (COLO 205, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.587×** | -8.2 | 2e-14 | 21/34 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.688×** | -7.8 | 2e-13 | 23/34 (NCI-H1792, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -7.4 | 6e-12 | 21/34 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -7.0 | 1e-10 | 21/35 (Panc 03.27, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.648×** | -6.6 | 1e-09 | 21/34 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.676×** | -5.9 | 1e-07 | 21/34 (LoVo, A549, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -5.7 | 3e-07 | 16/34 (COLO 205, Panc 03.27, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -5.6 | 6e-07 | 22/34 (HT-29, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **0.498×** | -5.6 | 6e-07 | 20/33 (LoVo, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -4.8 | 5e-05 | 15/34 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.571×** | -4.5 | 2e-04 | 18/33 (A549, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.666×** | -4.4 | 2e-04 | 15/34 (Panc 03.27, A549, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5102. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 157 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -16.3) |
| [[HT-29 (line)]] | alt | 58.0 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -16.6) |
| [[RKO (line)]] | wt | 24.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -15.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -12.6) |
| [[A549 (line)]] | wt | 35.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.4) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.275× (z -9.4) |
| [[COLO 205 (line)]] | alt | 120 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.239× (z -9.9) |
| [[KATO III (line)]] | alt | 85.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 19.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.125× (z -12.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -10.9) |
| [[SW480 (line)]] | alt | 42.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -10.1) |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -10.1) |
| [[J82 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.316× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.182× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~52% of this change |
| [[NCI-H2347 (line)]] | alt | 45.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.331× (z -9.8) |
| [[SW1417 (line)]] | alt | 50.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -13.7) |
| [[A-172 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 89.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.09 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5102), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC44A4]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TJP3]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[SLC50A1]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[MUC4]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[FOXO4]] | +0.59 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[KCNQ1]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ELF3]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TC2N]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ALOX5]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MUC16]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[MUC3A]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 | pathway: Diseases of metabolism |
| [[PLEKHG6]] | +0.56 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35B4]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[MSANTD2]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TADA2A]] | -0.47 | -0.47 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 27, C 1. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A4]] | B | SLC44A4 activity raises ASS1's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 4.52× lower at baseline in the lines without SLC44A4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[ALOX5]] | B | ALOX5 activity raises ASS1's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.30× lower at baseline in the lines without ALOX5 | 0.007 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[ABO]] | B | ABO activity raises ASS1's level | lines that do not express ABO (32) vs lines expressing it (18) | 5.14× lower at baseline in the lines without ABO | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[TMC5]] | B | TMC5 activity raises ASS1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 3.67× lower at baseline in the lines without TMC5 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ASS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[RNF39]] | B | RNF39 activity raises ASS1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.77× lower at baseline in the lines without RNF39 | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[TMPRSS3]] | B | TMPRSS3 activity raises ASS1's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.91× lower at baseline in the lines without TMPRSS3 | 0.020 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[CYP4F12]] | B | CYP4F12 activity raises ASS1's level | lines that do not express CYP4F12 (32) vs lines expressing it (18) | 2.69× lower at baseline in the lines without CYP4F12 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD3, CDH17, MUC13 |
| [[SIDT1]] | B | SIDT1 activity raises ASS1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.63× lower at baseline in the lines without SIDT1 | 0.028 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[PIP5K1B]] | B | PIP5K1B activity raises ASS1's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 3.13× lower at baseline in the lines without PIP5K1B | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[ELF3]] | B | ELF3 activity raises ASS1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.36× lower at baseline in the lines without ELF3 | 0.033 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[CLIC5]] | B | CLIC5 activity raises ASS1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 4.15× lower at baseline in the lines without CLIC5 | 0.033 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS3]] | B | ASS1 activity raises TMPRSS3's level | lines that do not express ASS1 (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without ASS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: GPRC5C, VAMP8, GALNT6 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, 55.9); signed map (54.9, -1.5). **Vector** length 97.6, 26.5% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.5 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.1 | -6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +1.9 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.3 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -10.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -8.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | argininosuccinate synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:130,444,961-130,501,274 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CTLN1; previously ASS |
| Gene groups (HGNC) | Ligases |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 4 pathways, smallest: Diseases of the urea cycle; Urea cycle; Diseases of metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P00966](https://www.uniprot.org/uniprotkb/P00966) (Argininosuccinate synthase):

> One of the enzymes of the urea cycle, the metabolic pathway transforming neurotoxic amonia produced by protein catabolism into inocuous urea in the liver of ureotelic animals. Catalyzes the formation of arginosuccinate from aspartate, citrulline and ATP and together with ASL it is responsible for the biosynthesis of arginine in most body tissues.

**Summary**, from NCBI Gene [445](https://www.ncbi.nlm.nih.gov/gene/445):

> The protein encoded by this gene catalyzes the penultimate step of the arginine biosynthetic pathway. There are approximately 10 to 14 copies of this gene including the pseudogenes scattered across the human genome, among which the one located on chromosome 9 appears to be the only functional gene for argininosuccinate synthetase. Mutations in the chromosome 9 copy of this gene cause citrullinemia. Two transcript variants encoding the same protein have been found for this gene. [provided by …

**Accessions** — [HGNC:758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:758) · Entrez [445](https://www.ncbi.nlm.nih.gov/gene/445) · UniProt [P00966](https://www.uniprot.org/uniprotkb/P00966) · Ensembl [ENSG00000130707](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130707)

## Data

Gene col 5102: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5102); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5102, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5102]; `tensor/DDL_lfc|DDL_z.npy` [5102]; `embed/gene_vectors.npy` [5102]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5102 or target_col == 5102). Every well: [[ASS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
