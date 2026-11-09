---
symbol: "ALG10B"
type: "gene"
col: 10619
ensembl_id: "ENSG00000175548"
name: "ALG10 alpha-1,2-glucosyltransferase B"
location: "12q12"
module: 25
arm: "+"
pooled_cpm: 6.83
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ALG10B

*ALG10 alpha-1,2-glucosyltransferase B* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.91× (z +11.8, q 2e-29, up in 11 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM: 1.45× (z +4.3, q 0.002, up in 6 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.441× (z -9.4, q 2e-18, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG10]] (+0.89, fdr 7e-06), [[PNPO]] (+0.70, fdr 7e-06), [[HDHD2]] (+0.70, fdr 1e-05); moves opposite to [[RPL18]] (-0.65, fdr 2e-05, ⚠ RPL18 in the vector space only through flagged drug-doses), [[RPL36AL]] (-0.65, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[RABAC1]] (-0.62, fdr 1e-05), [[RPL36]] (-0.62, fdr 3e-05), [[HIC2]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CEP41]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +11.8 | 2e-29 | 11/12 (A498, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +10.6 | 7e-24 | 15/20 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.71×** | +8.7 | 5e-16 | 26/46 (A549, SW480, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +8.4 | 9e-15 | 17/27 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +4.3 | 0.002 | 6/45 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.011 | 12/46 (NCI-H460, A-427, …) | rises with dose | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.052 | 5/46 (NCI-H1573, J82, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 1.34× | +3.1 | 0.15 | 4/45 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.33× | +3.0 | 0.17 | 6/36 (SW480, SNU-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.441×** | -9.4 | 2e-18 | 31/45 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.487×** | -8.3 | 4e-14 | 24/39 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.522×** | -7.5 | 1e-11 | 23/45 (J82, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.524×** | -7.4 | 1e-11 | 26/44 (A-427, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.539×** | -6.7 | 2e-09 | 22/41 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.598×** | -5.9 | 3e-07 | 21/44 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -5.7 | 8e-07 | 22/45 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.442×** | -4.9 | 6e-05 | 14/45 (Panc 03.27, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.688×** | -4.3 | 0.001 | 10/45 (C-33 A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.689×** | -4.3 | 0.001 | 15/45 (C-33 A, SW480, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.609×** | -3.9 | 0.005 | 13/45 (C32, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.529×** | -3.8 | 0.006 | 16/40 (NCI-H460, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.731×** | -3.6 | 0.013 | 9/45 (SW480, RKO, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.551×** | -3.6 | 0.013 | 10/23 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -3.3 | 0.035 | 15/40 (Hs 766T, NCI-H23, …) | top dose only | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 5.19 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0873× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 9.60 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0762× (z -8.5) |
| [[C-33 A (line)]] | alt | 9.70 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.0749× (z -9.1) |
| [[J82 (line)]] | alt | 6.61 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0834× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 7.31 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0770× (z -9.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.694 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG10]] | +0.89 | +0.79 / +0.89 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 903 |
| [[PNPO]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[HDHD2]] | +0.70 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[GMFB]] | +0.70 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.70 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[GUF1]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MBTPS2]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[DR1]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SRP9]] | +0.68 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[ZBED8]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ERLIN2]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL18]] ⚠ | -0.65 | -0.48 / -0.64 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.65 | -0.53 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RABAC1]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RPL36]] | -0.62 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[HIC2]] | -0.62 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[COX6B1]] | -0.61 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[RAB40C]] | -0.60 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ZBTB7A]] | -0.60 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[RPS19]] | -0.60 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[RPS29]] | -0.60 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[INAFM1]] | -0.60 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[SLC37A3]] | -0.60 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CSNK1G2]] | -0.59 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[RPS27]] | -0.59 | -0.44 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEP41]] | C | CEP41 activity raises ALG10B's level | lines that do not express CEP41 (4) vs lines expressing it (46) | 2.26× lower at baseline in the lines without CEP41 | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRIQ3, LINC02175, WDR35; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.1, -18.2); signed map (-16.4, -39.2). **Vector** length 65.9, 10.3% of its response variance represented; |z| ≥ 3 in 975 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.2 | +2.8 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.2 | +1.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.9 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ALG10 alpha-1,2-glucosyltransferase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:38,316,762-38,329,721 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KCR1 |
| Gene groups (HGNC) | Alpha-1,2-glucosyltransferases |
| Reactome | 2 pathways, smallest: Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein; Asparagine N-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5I7T1](https://www.uniprot.org/uniprotkb/Q5I7T1) (Dol-P-Glc:Glc(2)Man(9)GlcNAc(2)-PP-Dol alpha-1,2-glucosyltransferase B):

> Dol-P-Glc:Glc(2)Man(9)GlcNAc(2)-PP-Dol alpha-1,2-glucosyltransferase that operates in the biosynthetic pathway of dolichol-linked oligosaccharides, the glycan precursors employed in protein asparagine (N)-glycosylation. The assembly of dolichol-linked oligosaccharides begins on the cytosolic side of the endoplasmic reticulum membrane and finishes in its lumen. The sequential addition of sugars to dolichol pyrophosphate produces dolichol-linked oligosaccharides containing fourteen sugars, …

**Summary**, from NCBI Gene [144245](https://www.ncbi.nlm.nih.gov/gene/144245):

> Enables dolichyl pyrophosphate Glc2Man9GlcNAc2 alpha-1,2-glucosyltransferase activity. Involved in dolichol-linked oligosaccharide biosynthetic process. Located in plasma membrane. Is active in endoplasmic reticulum membrane. Implicated in long QT syndrome 2. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31088) · Entrez [144245](https://www.ncbi.nlm.nih.gov/gene/144245) · UniProt [Q5I7T1](https://www.uniprot.org/uniprotkb/Q5I7T1) · Ensembl [ENSG00000175548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175548)

## Data

Gene col 10619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10619); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10619]; `tensor/DDL_lfc|DDL_z.npy` [10619]; `embed/gene_vectors.npy` [10619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10619 or target_col == 10619). Every well: [[ALG10B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALG10B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
