---
symbol: "YPEL3"
type: "gene"
col: 1613
ensembl_id: "ENSG00000090238"
name: "yippee like 3"
location: "16p11.2"
module: 76
arm: "+"
pooled_cpm: 6.99
n_lines_expressing: 43
n_dd_up: 9
n_dd_down: 30
n_dd_up_clean: 7
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# YPEL3

*yippee like 3* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 2.91× (z +5.8, q 4e-06, up in 27 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.178× (z -14.2, q 6e-43, down in 39 of 40 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.221× (z -12.4, q 7e-33, down in 33 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGPEP1]] (+0.73, fdr 7e-06), [[CALCOCO1]] (+0.71, fdr 7e-06), [[CCNDBP1]] (+0.71, fdr 7e-06); moves opposite to [[PUS7L]] (-0.68, fdr 1e-05), [[UTP20]] (-0.63, fdr 1e-05), [[ABCE1]] (-0.62, fdr 7e-06).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BMF]] → it (grade C ⚠); 8 go from it, the strongest it → [[CTPS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.91×** | +5.8 | 4e-06 | 27/37 (HEC-1-A, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.1 | 1e-04 | 21/38 (SNU-423, KATO III, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.65×** | +4.2 | 0.006 | 18/39 (KATO III, HT-29, …) | top dose only |  |
| [[DTP3 (drug)]] 5 µM |  | **2.70×** | +4.1 | 0.006 | 14/35 (A498, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.11×** | +4.1 | 0.006 | 15/35 (LS 180, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.021 | 16/39 (A498, SW48, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.95×** | +3.6 | 0.022 | 13/38 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.5 | 0.034 | 11/32 (A-172, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.093 | 9/39 (J82, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.45× | +3.1 | 0.11 | 10/38 (KATO III, A-172, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.29× | +3.1 | 0.11 | 9/40 (Hs 766T, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1613.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.178×** | -14.2 | 6e-43 | 39/40 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.221×** | -12.4 | 7e-33 | 33/36 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.391×** | -10.9 | 2e-25 | 34/37 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.292×** | -9.7 | 3e-20 | 32/39 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.366×** | -8.2 | 2e-14 | 30/39 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.429×** | -7.0 | 3e-10 | 24/39 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.483×** | -6.0 | 2e-07 | 25/39 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.490×** | -5.8 | 3e-07 | 27/40 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.242×** | -5.8 | 6e-07 | 22/38 (NCI-H1792, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -5.6 | 2e-06 | 22/36 (MIA PaCa-2, SW 900, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.261×** | -5.4 | 3e-06 | 24/33 (A498, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.263×** | -5.4 | 3e-06 | 22/36 (AsPC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.376×** | -5.3 | 6e-06 | 24/40 (NCI-H1792, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.526×** | -5.3 | 6e-06 | 26/39 (SW480, AsPC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.308×** | -4.8 | 7e-05 | 22/35 (SW1417, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.311×** | -4.7 | 8e-05 | 22/35 (SW1417, KATO III, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 7 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0427× (z -16.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.111× (z -16.3) |
| [[HT-29 (line)]] | alt | 15.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0276× (z -17.7) |
| [[SW480 (line)]] | alt | 9.03 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -15.4) |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -12.1) |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0358× (z -15.2) |
| [[A498 (line)]] | wt | 8.15 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -10.0) |
| [[SW48 (line)]] | wt | 8.82 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0207× (z -10.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0961× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0730× (z -16.3) |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -8.9) |
| [[KATO III (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0784× (z -12.0) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 11.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0898× (z -11.4) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 9.64 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0918× (z -13.6) |
| [[SW 900 (line)]] | alt | 7.92 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0870× (z -12.8) |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -8.7) |
| [[A549 (line)]] | wt | 4.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0726× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -8.7) |
| [[Hs 766T (line)]] | wt | 6.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0968× (z -11.4) |
| [[HS-578T (line)]] | alt | 4.19 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0257× (z -12.2) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -8.6) |
| [[A-172 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.768 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGPEP1]] | +0.73 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[CALCOCO1]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 | STRING 406 |
| [[CCNDBP1]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[CBX7]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[HDAC5]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SYF2]] | +0.67 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[UBE2B]] | +0.67 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[GABARAPL2]] | +0.66 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[KLHL24]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS7L]] | -0.68 | -0.57 / -0.73 | both halves | 1e-05 |  |
| [[UTP20]] | -0.63 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.62 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[DARS2]] | -0.61 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.60 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[PSME3]] | -0.60 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[CCT7]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[CCT5]] | -0.60 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[PPIL1]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[RNASEH1]] | -0.59 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NUP188]] | -0.58 | -0.53 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMF]] | C | BMF activity raises YPEL3's level | lines that do not express BMF (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without BMF | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000285868; maybe low, not absent; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTPS1]] | B | YPEL3 activity lowers CTPS1's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 2.17× higher at baseline in the lines without YPEL3 | 0.019 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[EGFL8]] | B | YPEL3 activity lowers EGFL8's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.47× higher at baseline in the lines without YPEL3 | 0.068 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[TCP11L2]] | B | YPEL3 activity raises TCP11L2's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without YPEL3 | 0.084 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[UTP20]] | B | YPEL3 activity lowers UTP20's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.45× higher at baseline in the lines without YPEL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[GTF2H3]] | B | YPEL3 activity lowers GTF2H3's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.33× higher at baseline in the lines without YPEL3 | 0.090 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[CCT7]] | B | YPEL3 activity lowers CCT7's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.38× higher at baseline in the lines without YPEL3 | 0.092 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[PUS7L]] | B | YPEL3 activity lowers PUS7L's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.34× higher at baseline in the lines without YPEL3 | 0.094 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |
| [[ANAPC7]] | B | YPEL3 activity lowers ANAPC7's level | lines that do not express YPEL3 (7) vs lines expressing it (43) | 1.41× higher at baseline in the lines without YPEL3 | 0.095 | ⚠ within organs, on part of the lines; also absent: IKBKE, LTBR, RAB20 |

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.8, -46.7); signed map (-18.0, 9.7). **Vector** length 99.2, 26.0% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[GSK1059615 (drug)]] 0.5 µM |  | +3.3 | +5.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +3.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.0 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.1 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.1 | -14.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.2 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -8.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -5.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.0 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | yippee like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,092,314-30,096,915 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10500 |
| Gene groups (HGNC) | Yippee like family |
| Matched by | ensembl_id |

**Function**, from UniProt [P61236](https://www.uniprot.org/uniprotkb/P61236) (Protein yippee-like 3):

> Involved in proliferation and apoptosis in myeloid precursor cells.

**Summary**, from NCBI Gene [83719](https://www.ncbi.nlm.nih.gov/gene/83719):

> Predicted to enable metal ion binding activity. Involved in positive regulation of cellular senescence. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18327) · Entrez [83719](https://www.ncbi.nlm.nih.gov/gene/83719) · UniProt [P61236](https://www.uniprot.org/uniprotkb/P61236) · Ensembl [ENSG00000090238](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090238)

## Data

Gene col 1613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1613); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1613]; `tensor/DDL_lfc|DDL_z.npy` [1613]; `embed/gene_vectors.npy` [1613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1613 or target_col == 1613). Every well: [[YPEL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YPEL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
