---
symbol: "ENTHD1"
type: "gene"
col: 10693
ensembl_id: "ENSG00000176177"
name: "ENTH domain containing 1"
location: "22q13.1"
module: 125
arm: "+"
pooled_cpm: 6.55
n_lines_expressing: 22
n_dd_up: 39
n_dd_down: 2
n_dd_up_clean: 29
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 14
direction_downstream: 18
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# ENTHD1

*ENTH domain containing 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.68× (z +15.6, q 0e+00, up in 17 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.867× (z -3.6, q 0.062, down in 7 of 19 measured lines) ⚠ position not correctable. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.702× (z -3.6, q 0.062, down in 8 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.253×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.0797×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLAMF7]] (+0.71, fdr 7e-06), [[LINC02154]] (+0.70, fdr 7e-06), [[ROR1-AS1]] (+0.69, fdr 7e-06).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[C12orf50]] → it (grade B ⚠); 18 go from it, the strongest it → [[NINJ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.68×** | +15.6 | 0e+00 | 17/17 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.10×** | +14.2 | 1e-43 | 6/17 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.91×** | +10.8 | 7e-25 | 16/18 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.67×** | +8.6 | 1e-15 | 2/7 (C32, A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +7.9 | 3e-13 | 8/16 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +7.3 | 3e-11 | 1/13 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.74×** | +6.9 | 4e-10 | 15/18 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.47×** | +6.4 | 9e-09 | 13/17 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +5.9 | 2e-07 | 1/7 (A-172) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +5.9 | 3e-07 | 13/17 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +5.8 | 3e-07 | 6/12 (A498, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.17×** | +5.5 | 1e-06 | 12/19 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.97×** | +4.8 | 6e-05 | 15/18 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.89×** | +4.5 | 2e-04 | 12/17 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +4.3 | 7e-04 | 5/15 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **2.21×** | +4.0 | 0.002 | 8/18 (SNU-423, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +4.0 | 0.002 | 3/18 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **2.05×** | +3.6 | 0.008 | 5/18 (SW 900, NCI-H1792, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.69×** | +3.5 | 0.011 | 5/18 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.58×** | +3.5 | 0.011 | 12/17 (SK-MEL-2, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.97×** | +3.4 | 0.014 | 4/18 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.95×** | +3.4 | 0.015 | 13/19 (SK-MEL-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10693.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.253×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.0797×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.867× | -3.6 | 0.062 | 7/19 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.702×** | -3.6 | 0.062 | 8/18 (SW 900, A-172, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.607×** | -3.6 | 0.062 | 9/17 (SW 900, hTERT-HPNE, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.627× | -3.4 | 0.11 | 10/17 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.733× | -3.2 | 0.17 | 4/19 (CFPAC-1, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +15.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0797× (z -9.2) |
| [[C32 (line)]] | wt | 58.7 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.00× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 205 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -10.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 2.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 3.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 6.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.8× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 1.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 1.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.4× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 7.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 5.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +10.0) | — |
| [[A-427 (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.934 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.972 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.952 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.955 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLAMF7]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[LINC02154]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ROR1-AS1]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[C12orf50]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[NAALADL2-AS2]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NDRG4]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[CRYM]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[DYRK3]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[CACNG2]] | +0.65 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[LINC01695]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[GPR158]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf50]] | B | C12orf50 activity raises ENTHD1's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 1.91× lower at baseline in the lines without C12orf50 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |
| [[CRYM]] | B | CRYM activity raises ENTHD1's level | lines that do not express CRYM (12) vs lines expressing it (38) | 2.03× lower at baseline in the lines without CRYM | 0.063 | ⚠ within organs, on part of the lines; also absent: GBP3, CD44, SERPINE2; maybe low, not absent |
| [[ANKRD30B]] | C | ANKRD30B activity raises ENTHD1's level | lines that do not express ANKRD30B (35) vs lines expressing it (15) | 3.62× lower at baseline in the lines without ANKRD30B | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMPH, GYPC, GDNF; co-absent with the target |
| [[LINC01828]] | C | LINC01828 activity raises ENTHD1's level | lines that do not express LINC01828 (17) vs lines expressing it (33) | 2.38× lower at baseline in the lines without LINC01828 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000253471, ENSG00000230647, ENSG00000253891; maybe low, not absent; co-absent with the target |
| [[PNLIPRP3]] | C | PNLIPRP3 activity raises ENTHD1's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.91× lower at baseline in the lines without PNLIPRP3 | 0.030 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A; co-absent with the target |
| [[LINC01320]] | C | LINC01320 activity raises ENTHD1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 3.57× lower at baseline in the lines without LINC01320 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168; co-absent with the target |
| [[SLAMF7]] | C | SLAMF7 activity raises ENTHD1's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.82× lower at baseline in the lines without SLAMF7 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17; co-absent with the target |
| [[LINC00520]] | C | LINC00520 activity raises ENTHD1's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without LINC00520 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930; co-absent with the target |
| [[LINC00504]] | C | LINC00504 activity raises ENTHD1's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 2.44× lower at baseline in the lines without LINC00504 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474; co-absent with the target |
| [[LINC00457]] | C | LINC00457 activity raises ENTHD1's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.95× lower at baseline in the lines without LINC00457 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent; co-absent with the target |
| [[ROR1-AS1]] | C | ROR1-AS1 activity raises ENTHD1's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.69× lower at baseline in the lines without ROR1-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; co-absent with the target |
| [[LINC00536]] | C | LINC00536 activity raises ENTHD1's level | lines that do not express LINC00536 (17) vs lines expressing it (33) | 2.25× lower at baseline in the lines without LINC00536 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, DOCK2, LDOC1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 9, C 9. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NINJ1]] | B | ENTHD1 activity raises NINJ1's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.36× lower at baseline in the lines without ENTHD1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[GLS2]] | B | ENTHD1 activity lowers GLS2's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.15× higher at baseline in the lines without ENTHD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[CRYM]] | B | ENTHD1 activity raises CRYM's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without ENTHD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[LINC01291]] | B | ENTHD1 activity raises LINC01291's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.08× lower at baseline in the lines without ENTHD1 | 0.020 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[WDFY1]] | B | ENTHD1 activity raises WDFY1's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without ENTHD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[C12orf50]] | B | ENTHD1 activity raises C12orf50's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 1.98× lower at baseline in the lines without ENTHD1 | 0.036 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[GSDME]] | B | ENTHD1 activity raises GSDME's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 3.77× lower at baseline in the lines without ENTHD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[RPLP0P2]] | B | ENTHD1 activity raises RPLP0P2's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without ENTHD1 | 0.046 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[DPYD-AS1]] | B | ENTHD1 activity raises DPYD-AS1's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 1.35× lower at baseline in the lines without ENTHD1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |
| [[ATP6V0D2]] | C | ENTHD1 activity raises ATP6V0D2's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 3.11× lower at baseline in the lines without ENTHD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600; co-absent with the target |
| [[RRAD]] | C | ENTHD1 activity raises RRAD's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without ENTHD1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600; co-absent with the target |
| [[LINC01828]] | C | ENTHD1 activity raises LINC01828's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 2.72× lower at baseline in the lines without ENTHD1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.0, 21.6); signed map (38.0, 22.2). **Vector** length 60.2, 19.3% of its response variance represented; |z| ≥ 3 in 485 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +8.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | ENTH domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,743,044-39,893,864 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25421 |
| Matched by | ensembl_id |

UniProt [Q8IYW4](https://www.uniprot.org/uniprotkb/Q8IYW4) carries no function annotation.

**Summary**, from NCBI Gene [150350](https://www.ncbi.nlm.nih.gov/gene/150350):

> Predicted to enable clathrin binding activity and phospholipid binding activity. Predicted to be involved in endocytosis. Predicted to be located in cytoplasm. Predicted to be part of clathrin vesicle coat. Predicted to be active in endosome and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26352) · Entrez [150350](https://www.ncbi.nlm.nih.gov/gene/150350) · UniProt [Q8IYW4](https://www.uniprot.org/uniprotkb/Q8IYW4) · Ensembl [ENSG00000176177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176177)

## Data

Gene col 10693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10693); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10693]; `tensor/DDL_lfc|DDL_z.npy` [10693]; `embed/gene_vectors.npy` [10693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10693 or target_col == 10693). Every well: [[ENTHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
