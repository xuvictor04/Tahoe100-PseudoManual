---
symbol: "MED10"
type: "gene"
col: 5445
ensembl_id: "ENSG00000133398"
name: "mediator complex subunit 10"
location: "5p15.31"
module: 24
arm: "+"
pooled_cpm: 50.59
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MED10

*mediator complex subunit 10* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.74× (z +6.3, q 2e-07, up in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.60× (z +5.3, q 3e-05, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.621× (z -5.4, q 4e-05, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.736× (z -3.5, q 0.059, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.0820×, NCI-H2030 0.0948×, Panc 03.27 0.121×, AsPC-1 0.268×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.465×, SNU-423 0.443×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.471×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.124×); [[Furosemide (drug)]] 0.05 µM in 1 line (NCI-H661 0.0831×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMLG]] (+0.76, fdr 7e-06), [[SNHG7]] (+0.75, fdr 1e-05), [[ADPRM]] (+0.73, fdr 1e-05); moves opposite to [[SEPTIN11]] (-0.66, fdr 1e-05), [[NUP188]] (-0.65, fdr 1e-05), [[HNRNPL]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ADGRG6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +6.3 | 2e-07 | 42/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +5.3 | 3e-05 | 36/48 (A-427, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +4.6 | 7e-04 | 31/47 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +4.6 | 7e-04 | 32/48 (HT-29, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.1 | 0.004 | 29/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.004 | 32/49 (HT-29, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.004 | 29/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.007 | 29/48 (KATO III, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.6 | 0.017 | 29/47 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.017 | 26/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.2 | 0.064 | 23/45 (HepG2/C3A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.092 | 18/49 (KATO III, LS 180, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.11 | 22/48 (A498, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5445.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H460 0.0820×, NCI-H2030 0.0948×, Panc 03.27 0.121×, AsPC-1 0.268×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SHP-77 0.465×, SNU-423 0.443×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.471×; ⚠ cell-cycle shift, explains ~0% of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.124×); [[Furosemide (drug)]] 0.05 µM in 1 line (NCI-H661 0.0831×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.621×** | -5.4 | 4e-05 | 33/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.779×** | -4.0 | 0.017 | 25/48 (SHP-77, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.708×** | -3.9 | 0.017 | 27/48 (AsPC-1, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.712×** | -3.8 | 0.017 | 26/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.736×** | -3.5 | 0.059 | 28/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.747×** | -3.3 | 0.093 | 25/48 (LS 180, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 57.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.55× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 43.8 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.53× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[CHP-212 (line)]] | wt | 46.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.124× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0948× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H460 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0820× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 1 | — | [[Furosemide (drug)]] 0.05 µM 0.0831× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[RPMI-7951 (line)]] | alt | 60.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[SHP-77 (line)]] | alt | 95.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -10.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 93.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 75.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMLG]] | +0.76 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.75 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[ADPRM]] | +0.73 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | +0.71 | +0.49 / +0.70 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | +0.69 | +0.49 / +0.72 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC127]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[NSUN5P2-1]] ⚠ | +0.68 | +0.38 / +0.64 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CIAO2B]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[SCNM1]] | +0.67 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[SIRT6]] | +0.67 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PCGF1]] ⚠ | +0.67 | +0.52 / +0.68 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | +0.66 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[ZRSR2]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.66 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[NDUFB4]] | +0.66 | +0.46 / +0.72 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN11]] | -0.66 | -0.53 / -0.74 | both halves | 1e-05 |  |
| [[NUP188]] | -0.65 | -0.51 / -0.73 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.65 | -0.62 / -0.70 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.65 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[POGLUT3]] | -0.63 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[WDR1]] | -0.62 | -0.46 / -0.64 | both halves | 3e-05 |  |
| [[LMNB2]] | -0.62 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[GNG12]] | -0.61 | -0.38 / -0.63 | both halves | 6e-05 |  |
| [[CAPRIN1]] | -0.61 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[PSME3]] | -0.61 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[HNRNPUL1]] | -0.61 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[FOXM1]] | -0.61 | -0.54 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG6]] | B | ADGRG6 activity lowers MED10's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.46× higher at baseline in the lines without ADGRG6 | 0.011 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[THBS1]] | B | THBS1 activity raises MED10's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without THBS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[HDAC6]] | B | HDAC6 activity raises MED10's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.5, -13.8); signed map (-15.8, -3.1). **Vector** length 93.6, 27.8% of its response variance represented; |z| ≥ 3 in 683 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +4.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | -3.5 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -1.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.31 — chr5:6,371,874-6,378,571 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRG20, L6, MGC5309, NUT2 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTT4](https://www.uniprot.org/uniprotkb/Q9BTT4) (Mediator of RNA polymerase II transcription subunit 10):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [84246](https://www.ncbi.nlm.nih.gov/gene/84246):

> MED10 is a component of the Mediator complex, which is a coactivator for DNA-binding factors that activate transcription via RNA polymerase II (Sato et al., 2003 [PubMed 12584197]).[supplied by OMIM, Oct 2008]

**Accessions** — [HGNC:28760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28760) · Entrez [84246](https://www.ncbi.nlm.nih.gov/gene/84246) · UniProt [Q9BTT4](https://www.uniprot.org/uniprotkb/Q9BTT4) · Ensembl [ENSG00000133398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133398)

## Data

Gene col 5445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5445); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5445]; `tensor/DDL_lfc|DDL_z.npy` [5445]; `embed/gene_vectors.npy` [5445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5445 or target_col == 5445). Every well: [[MED10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
