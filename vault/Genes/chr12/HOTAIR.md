---
symbol: "HOTAIR"
type: "gene"
col: 13662
ensembl_id: "ENSG00000228630"
name: "HOX transcript antisense RNA"
location: "12q13.13"
module: 46
arm: "+"
pooled_cpm: 2.81
n_lines_expressing: 23
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# HOTAIR

*HOX transcript antisense RNA* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.04× (z +15.0, q 0e+00, up in 11 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.452× (z -6.1, q 8e-07, down in 12 of 17 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB7]] (+0.74, fdr 1e-05), [[GAS2]] (+0.71, fdr 2e-05), [[HOXB8]] (+0.69, fdr 1e-05); moves opposite to [[EHD4]] (-0.59, fdr 1e-04), [[LRRFIP1]] (-0.58, fdr 6e-05), [[FLNB]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[HOXC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13662.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.04×** | +15.0 | 0e+00 | 11/14 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.37×** | +10.3 | 1e-22 | 1/6 (SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.89×** | +10.3 | 1e-22 | 4/7 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.82×** | +9.8 | 2e-20 | 3/4 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +7.7 | 2e-12 | 6/10 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.03×** | +7.6 | 4e-12 | 11/18 (A-172, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.0 | 2e-07 | 4/20 (A-172, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.94×** | +5.0 | 3e-05 | 2/8 (KATO III, HT-29) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +5.0 | 4e-05 | 9/13 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.86×** | +4.7 | 2e-04 | 7/18 (KATO III, PANC-1, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.29×** | +4.5 | 4e-04 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.5 | 4e-04 | 4/9 (NCI-H23, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.1 | 0.002 | 3/11 (LS 180, A-172, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.01×** | +3.8 | 0.006 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.017 | 6/15 (KATO III, PANC-1, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +3.3 | 0.036 | 3/11 (LS 180, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.57×** | +3.2 | 0.044 | 1/12 (A-172) | inconsistent across doses | low cells (technical?) |
| [[Neratinib (drug)]] 0.05 µM |  | **1.50×** | +3.1 | 0.067 | 3/15 (NCI-H1573, HT-29, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.070 | 5/18 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.47×** | +2.9 | 0.098 | 0/11 | inconsistent across doses | low cells (technical?) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.46×** | +2.9 | 0.098 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.51×** | +2.9 | 0.098 | 2/10 (Hs 766T, HT-29) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13662.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.452×** | -6.1 | 8e-07 | 12/17 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.471×** | -5.7 | 3e-06 | 13/18 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -4.0 | 0.008 | 12/18 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.590×** | -4.0 | 0.008 | 8/12 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -3.9 | 0.011 | 11/18 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -3.7 | 0.018 | 7/15 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.627×** | -3.6 | 0.026 | 2/19 (BT-474, SW480) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.628×** | -3.6 | 0.026 | 9/19 (PANC-1, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.632×** | -3.5 | 0.028 | 8/19 (SW480, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13662. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.4 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.0815× (z -15.3) |
| [[SW480 (line)]] | alt | 7.25 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0738× (z -14.8) |
| [[KATO III (line)]] | alt | 18.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0590× (z -15.4) |
| [[LS 180 (line)]] | wt | 2.94 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0326× (z -10.3) |
| [[A-172 (line)]] | wt | 8.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 8.52 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0863× (z -8.6) |
| [[A-427 (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.798 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.292 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13662), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB7]] | +0.74 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[GAS2]] | +0.71 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[HOXB8]] | +0.69 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZNF362]] | +0.67 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[NEIL1]] | +0.66 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[C14orf93]] | +0.66 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[C11orf52]] | +0.66 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[HNF1A]] | +0.64 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[SPINT1-AS1]] | +0.64 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[C10orf95-AS1]] | +0.64 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[STEAP2-AS1]] | +0.63 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[CHDH]] | +0.63 | +0.66 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.59 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[LRRFIP1]] | -0.58 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[FLNB]] | -0.56 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[AP1M1]] | -0.56 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[CLTCL1]] | -0.55 | -0.31 / -0.28 | both halves | 3e-04 |  |
| [[PSD3]] | -0.55 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[DGKD]] | -0.53 | -0.38 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HOTAIR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NSUN7]] | B | NSUN7 activity raises HOTAIR's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without NSUN7 | 0.060 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HOTAIR's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC4]] | B | HOTAIR activity raises HOXC4's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without HOTAIR | 0.011 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |
| [[PLXNB3-AS1]] | B | HOTAIR activity raises PLXNB3-AS1's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without HOTAIR | 0.020 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |
| [[HOXC6]] | B | HOTAIR activity raises HOXC6's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 2.34× lower at baseline in the lines without HOTAIR | 0.025 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |
| [[MRPS30-DT]] | B | HOTAIR activity raises MRPS30-DT's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without HOTAIR | 0.069 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |
| [[HOXC4]] | B | HOTAIR activity strengthens HOXC4's drug response | lines that do not express HOTAIR (18) vs lines expressing it (19) | the lines without HOTAIR respond 0.67× as strongly (z diff +1.05); strongest at Homoharringtonine 0.5 µM: 0.46x vs 0.23x (z diff +2.8) | 0.075 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P; target measured in part of the lines; artifact flags |
| [[AP1M1]] | B | HOTAIR activity lowers AP1M1's level | lines that do not express HOTAIR (27) vs lines expressing it (23) | 1.31× higher at baseline in the lines without HOTAIR | 0.082 | ⚠ within organs, on part of the lines; also absent: CES1, DOK5, ANKRD20A9P |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.5, 27.9); signed map (36.9, -17.1). **Vector** length 39.7, 8.82% of its response variance represented; |z| ≥ 3 in 464 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +15.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +9.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.8 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.3 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -3.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | HOX transcript antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q13.13 — chr12:53,962,308-53,974,956 (-) |
| Ensembl biotype | lncRNA |
| Also known as | HOXC-AS4, HOXC11-AS1, NCRNA00072 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100124700](https://www.ncbi.nlm.nih.gov/gene/100124700):

> This gene is located within the Homeobox C (HOXC) gene cluster on chromosome 12 and is co-expressed with the HOXC genes. It functions through an RNA product, which binds lysine specific demethylase 1 (LSD1) and Polycomb repressive complex 2 (PRC2), and serves as a scaffold to assemble these regulators at the HOXD gene cluster, thereby promoting epigenetic repression of HOXD. This gene is highly expressed in multiple tumors. Alternatively spliced transcript variants have been identified. …

**Accessions** — [HGNC:33510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33510) · Entrez [100124700](https://www.ncbi.nlm.nih.gov/gene/100124700) · Ensembl [ENSG00000228630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228630)

## Data

Gene col 13662: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13662); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13662, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13662]; `tensor/DDL_lfc|DDL_z.npy` [13662]; `embed/gene_vectors.npy` [13662]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13662 or target_col == 13662). Every well: [[HOTAIR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOTAIR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
