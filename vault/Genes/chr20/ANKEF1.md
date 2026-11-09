---
symbol: "ANKEF1"
type: "gene"
col: 5349
ensembl_id: "ENSG00000132623"
name: "ankyrin repeat and EF-hand domain containing 1"
location: "20p12.2"
module: 16
arm: "+"
pooled_cpm: 5.68
n_lines_expressing: 44
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ANKEF1

*ankyrin repeat and EF-hand domain containing 1* — 20p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.61× (z +10.1, q 2e-21, up in 7 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.72× (z +8.5, q 7e-15, up in 23 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.357× (z -11.3, q 7e-27, down in 31 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT9]] (+0.64, fdr 7e-06), [[N6AMT1]] (+0.63, fdr 7e-06), [[TCTN1]] (+0.63, fdr 1e-05); moves opposite to [[TAF5]] (-0.63, fdr 1e-05), [[SRGAP2D]] (-0.62, fdr 1e-05), [[TPTEP2-CSNK1E]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ALOX12P2-1]] → it (grade B ⚠); 9 go from it, the strongest it → [[DLD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +10.1 | 2e-21 | 7/8 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.72×** | +8.5 | 7e-15 | 23/40 (SW480, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +6.2 | 1e-07 | 18/39 (NCI-H460, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.5 | 6e-06 | 8/26 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +5.4 | 6e-06 | 14/26 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +4.8 | 2e-04 | 5/16 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.40×** | +3.7 | 0.016 | 10/38 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.029 | 9/39 (LS 180, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.030 | 10/33 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Larotrectinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.074 | 4/41 (SHP-77, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.099 | 6/38 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.32× | +3.1 | 0.10 | 8/39 (COLO 205, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.357×** | -11.3 | 7e-27 | 31/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.373×** | -10.8 | 7e-25 | 25/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.408×** | -9.8 | 2e-20 | 28/40 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -8.4 | 9e-15 | 22/34 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.477×** | -8.1 | 5e-14 | 24/39 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.674×** | -4.3 | 0.001 | 11/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.724×** | -3.5 | 0.031 | 11/41 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -3.5 | 0.031 | 10/33 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.760× | -3.0 | 0.17 | 11/38 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.3 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -13.7) |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0927× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -10.2) |
| [[HT-29 (line)]] | alt | 6.24 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0342× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 4.32 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -10.1) |
| [[Hs 766T (line)]] | wt | 5.37 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0811× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 18.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -14.0) |
| [[LoVo (line)]] | wt | 8.44 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0597× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 4.12 | 0 | 1 | — | [[Rifaximin (drug)]] 0.05 µM 0.0853× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 5.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 5.43 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 5.73 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0654× (z -8.6) |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.835 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.770 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT9]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TCTN1]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[ZNF780A]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TRIM16]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[FECH]] | +0.61 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ZNF260]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GNGT1]] | +0.60 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[KCTD14]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[HSPA4L]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[DDX1]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TYW3]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5]] | -0.63 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[SRGAP2D]] | -0.62 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[MAP3K3]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NARF]] | -0.58 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[SRGAP2C]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[DDT]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[UBL5]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SMARCD2]] | -0.54 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[NFATC2IP]] | -0.53 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R14B]] | -0.53 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[NDUFA2]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALOX12P2-1]] | B | ALOX12P2-1 activity raises ANKEF1's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.65× lower at baseline in the lines without ALOX12P2-1 | 0.067 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[EFCAB7]] | C | EFCAB7's natural level strengthens ANKEF1's drug response | EFCAB7's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.09; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLD]] | B | ANKEF1 activity lowers DLD's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.45× higher at baseline in the lines without ANKEF1 | 0.016 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[LINC01128]] | B | ANKEF1 activity lowers LINC01128's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.54× higher at baseline in the lines without ANKEF1 | 0.027 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[FASTKD2]] | B | ANKEF1 activity lowers FASTKD2's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.31× higher at baseline in the lines without ANKEF1 | 0.034 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[GTF3C3]] | B | ANKEF1 activity lowers GTF3C3's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.36× higher at baseline in the lines without ANKEF1 | 0.063 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[GCOM1]] | B | ANKEF1 activity raises GCOM1's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without ANKEF1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[POLR2M]] | B | ANKEF1 activity raises POLR2M's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without ANKEF1 | 0.078 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| cells under [[TAK-733 (drug)]] 0.05 µM | B | ANKEF1 activity lowers the cells' numbers under TAK-733 0.05 µM (makes them more sensitive) | lines that do not express ANKEF1 (6) vs lines expressing it (42) | the lines without ANKEF1: 1.17× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| cells under [[Torkinib (drug)]] 5 µM | B | ANKEF1 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express ANKEF1 (6) vs lines expressing it (42) | the lines without ANKEF1: 0.89× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |
| [[KCTD14]] | B | ANKEF1 activity raises KCTD14's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without ANKEF1 | 0.098 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-22.9, 5.0); signed map (7.5, -33.0). **Vector** length 57.3, 8.96% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.8 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -8.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -11.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -0.9 | -1.5 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and EF-hand domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.2 — chr20:9,986,126-10,058,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21669, dJ839B4.6; previously ANKRD5 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; EF-hand domain containing |
| Matched by | ensembl_id |

UniProt [Q9NU02](https://www.uniprot.org/uniprotkb/Q9NU02) carries no function annotation.

**Summary**, from NCBI Gene [63926](https://www.ncbi.nlm.nih.gov/gene/63926):

> Predicted to enable calcium ion binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15803) · Entrez [63926](https://www.ncbi.nlm.nih.gov/gene/63926) · UniProt [Q9NU02](https://www.uniprot.org/uniprotkb/Q9NU02) · Ensembl [ENSG00000132623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132623)

## Data

Gene col 5349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5349); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5349]; `tensor/DDL_lfc|DDL_z.npy` [5349]; `embed/gene_vectors.npy` [5349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5349 or target_col == 5349). Every well: [[ANKEF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKEF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
