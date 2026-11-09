---
symbol: "ARSB"
type: "gene"
col: 3443
ensembl_id: "ENSG00000113273"
name: "arylsulfatase B"
location: "5q14.1"
module: 124
arm: "+"
pooled_cpm: 12.34
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 8
n_dd_up_clean: 17
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# ARSB

*arylsulfatase B* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.11× (z +13.5, q 7e-39, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.470× (z -9.7, q 2e-19, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AVEN]] (+0.77, fdr 7e-06), [[CRPPA]] (+0.76, fdr 1e-05), [[ZNF124]] (+0.72, fdr 2e-05); moves opposite to [[HEATR5B]] (-0.69, fdr 3e-05), [[IFT172]] (-0.66, fdr 1e-05), [[TMEM256]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +13.5 | 7e-39 | 41/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.73×** | +12.8 | 4e-35 | 27/37 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +11.2 | 9e-27 | 15/20 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +10.0 | 2e-21 | 21/28 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +9.2 | 3e-18 | 36/48 (HOP62, A549, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +9.1 | 6e-18 | 28/45 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +7.7 | 1e-12 | 32/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +5.9 | 2e-07 | 23/47 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +5.7 | 6e-07 | 27/47 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.7 | 6e-07 | 23/47 (HEC-1-A, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +5.7 | 6e-07 | 22/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +5.4 | 3e-06 | 23/47 (C-33 A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.51×** | +5.0 | 2e-05 | 21/41 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 3e-04 | 18/47 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +3.9 | 0.003 | 13/47 (H4, HOP62, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.005 | 9/48 (A-172, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.008 | 15/46 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.011 | 13/47 (HS-578T, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.020 | 7/48 (SW480, SW 900, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.040 | 7/47 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.075 | 8/46 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.470×** | -9.7 | 2e-19 | 30/47 (HepG2/C3A, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.501×** | -8.9 | 2e-16 | 35/48 (HepG2/C3A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.538×** | -8.0 | 3e-13 | 33/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.727×** | -4.1 | 0.005 | 20/48 (AN3 CA, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.808×** | -3.9 | 0.011 | 16/48 (A-172, Hs 766T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.572×** | -3.8 | 0.016 | 15/48 (HepG2/C3A, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.757×** | -3.6 | 0.026 | 12/48 (A-172, SW 1088, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.775×** | -3.3 | 0.071 | 13/44 (BT-474, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | 0.785× | -3.1 | 0.11 | 8/48 (Hs 766T, H4, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.222× (z -10.1) |
| [[LoVo (line)]] | wt | 8.34 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.54× (z +10.4) ⚠ toxic; transcription drop | [[Simotinib (drug)]] 0.05 µM 0.180× (z -8.8) |
| [[RKO (line)]] | wt | 19.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -9.1) |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0490× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 4.33 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0600× (z -9.9) ⚠ cell-cycle shift, explains <1% of this change |
| [[HT-29 (line)]] | alt | 3.97 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0903× (z -8.6) |
| [[LS 180 (line)]] | wt | 4.44 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0799× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 9.35 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.08× (z +8.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 9.40 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 15.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -9.4) |
| [[A-172 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | +0.77 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CRPPA]] | +0.76 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ZNF124]] | +0.72 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[EPM2A]] | +0.72 | +0.64 / +0.39 | both halves | 5e-05 | pathway: Diseases of carbohydrate metabolism |
| [[TOR1A]] | +0.72 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A21]] | +0.67 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[PRDM5]] | +0.67 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[RCBTB2]] | +0.67 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[TMEM117]] | +0.67 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[ST7]] | +0.66 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[HCFC1]] | +0.66 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PBLD]] | +0.65 | +0.50 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR5B]] | -0.69 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[IFT172]] | -0.66 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TMEM256]] | -0.65 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[LCMT1]] | -0.64 | -0.57 / -0.32 | both halves | 1e-04 |  |
| [[AFMID]] | -0.64 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[KLHL26]] | -0.63 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[RAD17]] | -0.63 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[GPATCH11]] | -0.63 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[KBTBD3]] | -0.63 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[RRAS]] | -0.63 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.62 | -0.56 / -0.23 | both halves | 5e-04 |  |
| [[UBE2B]] | -0.62 | -0.56 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARSB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ARSB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CTSO]] | B | CTSO activity weakens ARSB's drug response | lines that do not express CTSO (8) vs lines expressing it (40) | the lines without CTSO respond 1.05× as strongly (z diff -0.15); strongest at Panobinostat 5 µM: 0.33x vs 0.57x (z diff -2.9) | 0.096 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT; target measured in part of the lines; both ways; artifact flags |
| [[SETD7]] | C | SETD7 activity lowers ARSB's level | lines that do not express SETD7 (3) vs lines expressing it (47) | 2.86× higher at baseline in the lines without SETD7 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| [[SETD7]] | C | SETD7 activity weakens ARSB's drug response | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7 respond 0.94× as strongly (z diff -0.27); strongest at Belinostat 5 µM: 0.16x vs 0.51x (z diff -5.0) | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.2, 8.7); signed map (23.4, -29.1). **Vector** length 98.4, 21.0% of its response variance represented; |z| ≥ 3 in 1,037 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +13.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +9.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +3.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.2 | -8.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -8.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.9 | -3.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.7 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.5 | -3.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | arylsulfatase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:78,777,209-78,986,087 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASB |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 15 pathways, smallest: The activation of arylsulfatases; Mucopolysaccharidoses; CS/DS degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P15848](https://www.uniprot.org/uniprotkb/P15848) (Arylsulfatase B):

> Removes sulfate groups from chondroitin-4-sulfate (C4S) and regulates its degradation. Involved in the regulation of cell adhesion, cell migration and invasion in colonic epithelium. In the central nervous system, is a regulator of neurite outgrowth and neuronal plasticity, acting through the control of sulfate glycosaminoglycans and neurocan levels (By similarity).

**Summary**, from NCBI Gene [411](https://www.ncbi.nlm.nih.gov/gene/411):

> Arylsulfatase B encoded by this gene belongs to the sulfatase family. The arylsulfatase B homodimer hydrolyzes sulfate groups of N-Acetyl-D-galactosamine, chondriotin sulfate, and dermatan sulfate. The protein is targeted to the lysozyme. Mucopolysaccharidosis type VI is an autosomal recessive lysosomal storage disorder resulting from a deficiency of arylsulfatase B. Two alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Dec …

**Accessions** — [HGNC:714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:714) · Entrez [411](https://www.ncbi.nlm.nih.gov/gene/411) · UniProt [P15848](https://www.uniprot.org/uniprotkb/P15848) · Ensembl [ENSG00000113273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113273)

## Data

Gene col 3443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3443); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3443]; `tensor/DDL_lfc|DDL_z.npy` [3443]; `embed/gene_vectors.npy` [3443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3443 or target_col == 3443). Every well: [[ARSB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARSB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
