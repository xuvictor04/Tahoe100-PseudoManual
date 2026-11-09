---
symbol: "DNAJC18"
type: "gene"
col: 9957
ensembl_id: "ENSG00000170464"
name: "DnaJ heat shock protein family (Hsp40) member C18"
location: "5q31.2"
module: 64
arm: "+"
pooled_cpm: 11.6
n_lines_expressing: 46
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# DNAJC18

*DnaJ heat shock protein family (Hsp40) member C18* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.28× (z +4.9, q 6e-04, up in 15 of 44 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.24× (z +4.2, q 0.007, up in 14 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.454× (z -10.9, q 8e-25, down in 36 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP37]] (+0.60, fdr 1e-05), [[ZSCAN26]] (+0.57, fdr 3e-05), [[PSMC1]] (+0.56, fdr 3e-05); moves opposite to [[FAM120A]] (-0.52, fdr 1e-05), [[CRNDE]] (-0.52, fdr 2e-05), [[DNAJC9]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 7 go from it, the strongest it → [[BTN2A2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.28×** | +4.9 | 6e-04 | 15/44 (A498, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.007 | 14/44 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.33×** | +3.9 | 0.014 | 14/43 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.014 | 9/43 (SW480, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +3.6 | 0.028 | 16/43 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.32×** | +3.6 | 0.028 | 13/43 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.061 | 5/39 (SHP-77, HS-578T, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -10.9 | 8e-25 | 36/44 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.493×** | -9.7 | 6e-20 | 31/43 (C32, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.501×** | -9.5 | 3e-19 | 30/40 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.503×** | -9.1 | 1e-17 | 29/42 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.506×** | -9.0 | 2e-17 | 28/39 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.662×** | -8.0 | 1e-13 | 26/43 (Hs 766T, C32, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -7.2 | 4e-11 | 28/43 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -6.9 | 4e-10 | 26/44 (LoVo, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.619×** | -6.6 | 3e-09 | 26/43 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.648×** | -6.0 | 1e-07 | 24/43 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.653×** | -5.9 | 2e-07 | 22/44 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.722×** | -4.5 | 4e-04 | 16/43 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.743×** | -4.1 | 0.002 | 14/44 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.572×** | -4.0 | 0.002 | 15/41 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.752×** | -3.8 | 0.006 | 18/44 (A-427, C32, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.799×** | -3.1 | 0.077 | 12/43 (HEC-1-A, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 82.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -13.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.9) |
| [[C32 (line)]] | wt | 11.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -12.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.141× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.158× (z -9.9) |
| [[A-427 (line)]] | wt | 17.7 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -13.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H23 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 8.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -8.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 6.28 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0851× (z -9.1) |
| [[COLO 205 (line)]] | alt | 5.51 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0628× (z -8.9) |
| [[HS-578T (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0419× (z -17.3) ⚠ toxic |
| [[LoVo (line)]] | wt | 9.05 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.222× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -12.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 5.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0901× (z -12.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP37]] | +0.60 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ZSCAN26]] | +0.57 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[PSMC1]] | +0.56 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[ZNF426]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[DCTN6]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PFDN4]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[KIF3B]] | +0.53 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[APBB1]] | +0.51 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[MARCHF7]] | +0.51 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SNRNP27]] | +0.51 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[ZNF222]] | +0.50 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[PSMD4]] | +0.50 | +0.54 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM120A]] | -0.52 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CRNDE]] | -0.52 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[DNAJC9]] | -0.50 | -0.29 / -0.62 | both halves | 2e-04 | same gene group |
| [[PTPN18]] | -0.48 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[TTC13]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[VRK1]] | -0.46 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[SETD3]] | -0.46 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[POC1A]] | -0.46 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[NSD2]] | -0.45 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[PIGX]] | -0.45 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[SFXN2]] | -0.45 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[NDC1]] | -0.45 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers DNAJC18's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTN2A2]] | C | DNAJC18 activity raises BTN2A2's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 3.61× lower at baseline in the lines without DNAJC18 | 0.001 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1; co-absent with the target |
| [[SLC36A4]] | C | DNAJC18 activity raises SLC36A4's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 3.73× lower at baseline in the lines without DNAJC18 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1; co-absent with the target |
| [[SMARCA1]] | C | DNAJC18 activity raises SMARCA1's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 8.37× lower at baseline in the lines without DNAJC18 | 0.024 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1 |
| [[DCTN6]] | C | DNAJC18 activity lowers DCTN6's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 1.71× higher at baseline in the lines without DNAJC18 | 0.034 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1 |
| [[HDX]] | C | DNAJC18 activity raises HDX's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 5.74× lower at baseline in the lines without DNAJC18 | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1 |
| [[ZNF155]] | C | DNAJC18 activity raises ZNF155's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 3.18× lower at baseline in the lines without DNAJC18 | 0.086 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1 |
| [[APBB1]] | C | DNAJC18 activity raises APBB1's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 3.05× lower at baseline in the lines without DNAJC18 | 0.091 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1 |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.556). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-32.6, 8.7); signed map (0.8, -25.1). **Vector** length 67.7, 11.3% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.9 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.2 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -1.5 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -9.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.5 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -1.8 | -9.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,408,588-139,444,491 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC29463 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H819](https://www.uniprot.org/uniprotkb/Q9H819) (DnaJ homolog subfamily C member 18):

> (Microbial infection) In case of infection by polyomavirus, involved in the virus endoplasmic reticulum membrane penetration and infection. Regulates the recruitment of DNAJB12:DNAJB14 into SV40-induced foci and all cooperate to guide SV40 across the endoplasmic reticulum membrane. The foci represent the site from which SV40 penetrates into the cytosol.

**Summary**, from NCBI Gene [202052](https://www.ncbi.nlm.nih.gov/gene/202052):

> Predicted to enable Hsp70 protein binding activity. Predicted to be involved in cellular response to misfolded protein and protein folding. Located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28429](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28429) · Entrez [202052](https://www.ncbi.nlm.nih.gov/gene/202052) · UniProt [Q9H819](https://www.uniprot.org/uniprotkb/Q9H819) · Ensembl [ENSG00000170464](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170464)

## Data

Gene col 9957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9957); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9957]; `tensor/DDL_lfc|DDL_z.npy` [9957]; `embed/gene_vectors.npy` [9957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9957 or target_col == 9957). Every well: [[DNAJC18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
