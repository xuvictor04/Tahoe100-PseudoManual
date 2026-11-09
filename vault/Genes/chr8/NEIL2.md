---
symbol: "NEIL2"
type: "gene"
col: 7800
ensembl_id: "ENSG00000154328"
name: "nei like DNA glycosylase 2"
location: "8p23.1"
module: 36
arm: "+"
pooled_cpm: 8.62
n_lines_expressing: 47
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# NEIL2

*nei like DNA glycosylase 2* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.04× (z +9.3, q 1e-17, up in 11 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.96× (z +9.1, q 2e-17, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.354× (z -19.9, q 0e+00, down in 37 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACC1]] (+0.79, fdr 7e-06), [[GARNL3]] (+0.71, fdr 7e-06), [[TMEM161A]] (+0.71, fdr 7e-06); moves opposite to [[CGGBP1]] (-0.63, fdr 1e-05), [[BAZ2B]] (-0.61, fdr 1e-04), [[RC3H2]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[WRN]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +9.3 | 1e-17 | 11/13 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +9.1 | 2e-17 | 31/44 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.5 | 5e-15 | 18/32 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +7.7 | 1e-12 | 27/44 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +6.3 | 3e-08 | 23/44 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +5.6 | 2e-06 | 17/44 (NCI-H2347, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.3 | 1e-05 | 14/35 (A-427, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +5.1 | 2e-05 | 16/44 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.9 | 6e-05 | 12/44 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.3 | 9e-04 | 14/43 (A498, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.010 | 16/45 (A498, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.4 | 0.037 | 3/29 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +3.3 | 0.037 | 0/23 | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.041 | 14/44 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.049 | 3/41 (NCI-H460, LOX-IMVI, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.74×** | +3.1 | 0.064 | 3/40 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.067 | 9/43 (A549, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.354×** | -19.9 | 0e+00 | 37/42 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.536×** | -8.5 | 6e-15 | 28/44 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.543×** | -8.3 | 2e-14 | 26/43 (HCT15, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.525×** | -7.9 | 3e-13 | 26/40 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.591×** | -7.1 | 1e-10 | 25/44 (KATO III, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.601×** | -6.9 | 4e-10 | 27/44 (BT-474, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.635×** | -5.9 | 2e-07 | 17/43 (SNU-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.383×** | -5.4 | 4e-06 | 21/45 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.756×** | -3.8 | 0.009 | 12/44 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.552×** | -3.4 | 0.041 | 6/41 (LOX-IMVI, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.767×** | -3.3 | 0.053 | 2/45 (NCI-H23, SW480) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 6.99 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -20.0) |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -11.4) |
| [[A498 (line)]] | wt | 8.68 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.4) |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.124× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 9.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.0) |
| [[HOP62 (line)]] | alt | 6.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -9.5) |
| [[Hs 766T (line)]] | wt | 7.56 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0921× (z -8.8) |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.4) |
| [[J82 (line)]] | alt | 6.48 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.9) |
| [[LoVo (line)]] | wt | 7.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 5.82 | 0 | 1 | — | [[MK-8353 (drug)]] 0.05 µM 0.0428× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 9.33 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 14.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -8.5) |
| [[RKO (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -11.2) ⚠ cell-cycle shift, explains ~82% of this change |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.3) |
| [[SNU-423 (line)]] | alt | 5.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -10.1) |
| [[SW48 (line)]] | wt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.0) |
| [[SW480 (line)]] | alt | 7.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -11.5) |
| [[A-172 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | +0.79 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[GARNL3]] | +0.71 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.71 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ST6GALNAC4]] | +0.69 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CHCHD6]] | +0.69 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[ANKS6]] | +0.69 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[DFFA]] | +0.69 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[WASF3]] | +0.68 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[ST6GALNAC6]] | +0.68 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[TRABD]] | +0.67 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.67 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.66 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.63 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.61 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[RC3H2]] | -0.60 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[NDUFS1]] | -0.59 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TIA1]] | -0.59 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[TAPBPL]] | -0.59 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[PKN2-AS1]] | -0.58 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[NUCKS1]] | -0.58 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[THAP9]] | -0.58 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[NDUFA6-DT]] | -0.58 | -0.57 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[TMEM202-AS1]] | -0.58 | -0.53 / -0.22 | both halves | 6e-04 |  |
| [[EP300]] | -0.57 | -0.42 / -0.41 | both halves | 4e-05 | STRING 442 |
| [[TAPBP]] | -0.57 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WRN]] | C | NEIL2 activity raises WRN's level | lines that do not express NEIL2 (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without NEIL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[GTF2E2]] | C | NEIL2 activity raises GTF2E2's level | lines that do not express NEIL2 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without NEIL2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.6, -39.4); signed map (-10.5, -55.2). **Vector** length 64.8, 11.4% of its response variance represented; |z| ≥ 3 in 703 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.1 | +4.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -19.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -7.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.2 | -0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | nei like DNA glycosylase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:11,769,639-11,787,345 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NEH2, FLJ31644, MGC2832, MGC4505 |
| Gene groups (HGNC) | DNA glycosylases; DNA-(apurinic or apyrimidinic site) lyases |
| Reactome | 8 pathways, smallest: APEX1-Independent Resolution of AP Sites via the Single Nucleotide Replacement Pathway; Cleavage of the damaged pyrimidine; Depyrimidination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969S2](https://www.uniprot.org/uniprotkb/Q969S2) (Endonuclease 8-like 2):

> Involved in base excision repair of DNA damaged by oxidation or by mutagenic agents. Has DNA glycosylase activity towards 5-hydroxyuracil and other oxidized derivatives of cytosine with a preference for mismatched double-stranded DNA (DNA bubbles). Has low or no DNA glycosylase activity towards thymine glycol, 2-hydroxyadenine, hypoxanthine and 8-oxoguanine. Has AP (apurinic/apyrimidinic) lyase activity and introduces nicks in the DNA strand. Cleaves the DNA backbone by beta-delta elimination …

**Summary**, from NCBI Gene [252969](https://www.ncbi.nlm.nih.gov/gene/252969):

> This gene encodes a member of the Fpg/Nei family of DNA glycosylases. These glycosylases initiate the first step in base excision repair by cleaving oxidatively damaged bases and introducing a DNA strand break via their abasic site lyase activity. This enzyme is primarily associated with DNA repair during transcription and acts prefentially on cytosine-derived lesions, particularly 5-hydroxyuracil and 5-hydroxycytosine. It contains an N-terminal catalytic domain, a hinge region, and a …

**Accessions** — [HGNC:18956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18956) · Entrez [252969](https://www.ncbi.nlm.nih.gov/gene/252969) · UniProt [Q969S2](https://www.uniprot.org/uniprotkb/Q969S2) · Ensembl [ENSG00000154328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154328)

## Data

Gene col 7800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7800); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7800]; `tensor/DDL_lfc|DDL_z.npy` [7800]; `embed/gene_vectors.npy` [7800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7800 or target_col == 7800). Every well: [[NEIL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEIL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
