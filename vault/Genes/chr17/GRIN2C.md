---
symbol: "GRIN2C"
type: "gene"
col: 8433
ensembl_id: "ENSG00000161509"
name: "glutamate ionotropic receptor NMDA type subunit 2C"
location: "17q25.1"
module: 62
arm: "+"
pooled_cpm: 4.29
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 10
direction_downstream: 18
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# GRIN2C

*glutamate ionotropic receptor NMDA type subunit 2C* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.93× (z +18.1, q 0e+00, up in 23 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.581× (z -4.4, q 0.006, down in 13 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDXR]] (+0.84, fdr 7e-06, ⚠ same locus), [[PINCR]] (+0.79, fdr 7e-06), [[PTCHD4]] (+0.75, fdr 7e-06), [[ZMAT3]] (+0.74, fdr 7e-06).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 18 go from it, the strongest it → [[PPM1D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.93×** | +18.1 | 0e+00 | 23/25 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.33×** | +9.3 | 4e-18 | 19/25 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.85×** | +8.4 | 7e-15 | 16/32 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +7.7 | 2e-12 | 0/4 | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +7.6 | 3e-12 | 10/25 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +7.0 | 2e-10 | 1/8 (MIA PaCa-2) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +6.9 | 3e-10 | 19/27 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.2 | 5e-08 | 13/32 (A498, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.98×** | +5.5 | 3e-06 | 15/31 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.98×** | +5.3 | 7e-06 | 10/15 (NCI-H460, A498, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.93×** | +4.9 | 6e-05 | 12/20 (A498, A-427, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.53×** | +4.8 | 7e-05 | 12/31 (LOX-IMVI, SNU-1, …) | rises with dose | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.75×** | +4.5 | 3e-04 | 18/32 (A498, A549, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +4.5 | 3e-04 | 2/18 (H4, LOX-IMVI) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.67×** | +4.1 | 0.002 | 14/29 (A549, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | **1.61×** | +3.8 | 0.005 | 11/30 (SNU-1, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.037 | 8/23 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vandetanib (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.063 | 2/28 (KATO III, NCI-H2347) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.581×** | -4.4 | 0.006 | 13/29 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.603×** | -4.1 | 0.012 | 16/29 (A498, H4, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.612×** | -4.0 | 0.013 | 10/30 (NCI-H460, A-427, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.621×** | -3.9 | 0.016 | 10/30 (SNU-1, SW48, …) | two highest doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.631×** | -3.7 | 0.022 | 16/21 (A-427, A549, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.639×** | -3.6 | 0.027 | 11/31 (A-172, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.664×** | -3.3 | 0.064 | 14/32 (A-427, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -3.3 | 0.064 | 7/32 (LS 180, hTERT-HPNE, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.680× | -3.1 | 0.10 | 7/32 (SW1417, NCI-H460, …) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 5 µM |  | 0.684× | -3.1 | 0.10 | 6/32 (C-33 A, A498, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.05 µM |  | 0.684× | -3.1 | 0.10 | 10/29 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.767× | -3.1 | 0.11 | 6/31 (COLO 205, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.76 per unit of S-phase module lfc, -0.85 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 29.9 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0449× (z -15.9) |
| [[A498 (line)]] | wt | 10.2 | 3 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.05× (z +11.1) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0953× (z -8.9) |
| [[H4 (line)]] | wt | 27.8 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0514× (z -11.1) |
| [[LoVo (line)]] | wt | 8.75 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.15× (z +12.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0776× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 9.45 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.44× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0824× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.77× (z +8.9) | — |
| [[A549 (line)]] | wt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 3.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +10.5) | — |
| [[SW48 (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.26× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.872 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.883 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDXR]] | +0.84 | +0.74 / +0.86 | both halves | 7e-06 | ⚠ same locus (1.0 kb, same strand: neighbours can correlate without regulation) |
| [[PINCR]] | +0.79 | +0.60 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[PTCHD4]] | +0.75 | +0.60 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ZMAT3]] | +0.74 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ACTA2]] | +0.73 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[EDA2R]] | +0.73 | +0.54 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[SPATA18]] | +0.71 | +0.51 / +0.76 | both halves | 1e-05 |  |
| [[PURPL]] | +0.69 | +0.56 / +0.74 | both halves | 1e-05 | **novel candidate** |
| [[INKA2]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[MDM2]] | +0.68 | +0.55 / +0.64 | both halves | 1e-05 | pathway: Neuronal System |
| [[RRM2B]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[BAX]] | +0.68 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[DDB2]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 2, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens GRIN2C's drug response | recorded loss-of-function mutation of TP53 in 16 lines vs 16 not recorded | the TP53-altered lines respond 0.69× as strongly (z diff +0.92); strongest at Idarubicin (hydrochloride) 5 µM: 3.41x vs 8.20x (z diff +4.3) | 0.018 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); both ways; artifact flags |
| [[TP53]] | A | TP53 activity raises GRIN2C's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 3.32× lower at baseline in the TP53-altered lines | 0.048 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[PINCR]] | B | PINCR activity raises GRIN2C's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.50× lower at baseline in the lines without PINCR | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[TOP2A]] | B | TOP2A activity lowers GRIN2C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EDA2R]] | B | EDA2R activity raises GRIN2C's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without EDA2R | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[ADGRA2]] | B | ADGRA2 activity raises GRIN2C's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 1.92× lower at baseline in the lines without ADGRA2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |
| [[PINCR]] | B | PINCR activity strengthens GRIN2C's drug response | lines that do not express PINCR (14) vs lines expressing it (18) | the lines without PINCR respond 0.67× as strongly (z diff +0.90); strongest at Idarubicin (hydrochloride) 5 µM: 3.03x vs 8.38x (z diff +4.1) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises GRIN2C's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.30× lower at baseline in the lines without PTCHD4 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[FDXR]] | C | FDXR activity raises GRIN2C's level | lines that do not express FDXR (8) vs lines expressing it (42) | 2.67× lower at baseline in the lines without FDXR | 0.094 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent; co-absent with the target |
| [[CYFIP2]] | C | CYFIP2 activity raises GRIN2C's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.29× lower at baseline in the lines without CYFIP2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 16, C 2. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPM1D]] | B | GRIN2C activity raises PPM1D's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.75× lower at baseline in the lines without GRIN2C | 0.005 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[ZMAT3]] | B | GRIN2C activity raises ZMAT3's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 2.72× lower at baseline in the lines without GRIN2C | 0.010 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[BAX]] | B | GRIN2C activity raises BAX's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.63× lower at baseline in the lines without GRIN2C | 0.011 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[DDX3Y]] | B | GRIN2C activity raises DDX3Y's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 3.31× lower at baseline in the lines without GRIN2C | 0.027 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[DDB2]] | B | GRIN2C activity raises DDB2's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without GRIN2C | 0.034 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[EDA2R]] | B | GRIN2C activity raises EDA2R's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 2.56× lower at baseline in the lines without GRIN2C | 0.036 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[PTCHD4]] | B | GRIN2C activity raises PTCHD4's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 4.04× lower at baseline in the lines without GRIN2C | 0.039 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[ZNF423]] | B | GRIN2C activity raises ZNF423's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without GRIN2C | 0.053 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[DOCK8]] | B | GRIN2C activity raises DOCK8's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.92× lower at baseline in the lines without GRIN2C | 0.053 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[ACER2]] | B | GRIN2C activity raises ACER2's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without GRIN2C | 0.058 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[PINCR]] | B | GRIN2C activity raises PINCR's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 2.28× lower at baseline in the lines without GRIN2C | 0.067 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[TIGAR]] | B | GRIN2C activity raises TIGAR's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without GRIN2C | 0.067 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.856). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.9, 36.7); signed map (42.8, -23.9). **Vector** length 82.1, 18.8% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.63 to 26); *p53 pathway* (hallmark, mean cos +0.58 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.58 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.6 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +18.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | +3.2 | +5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -2.5 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | +0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +2.8 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor NMDA type subunit 2C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:74,842,023-74,861,504 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GluN2C, NR2C; previously NMDAR2C |
| Gene groups (HGNC) | Glutamate ionotropic receptor NMDA type subunits |
| Reactome | 12 pathways, smallest: Synaptic adhesion-like molecules; Unblocking of NMDA receptors, glutamate binding and activation; Negative regulation of NMDA receptor-mediated neuronal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14957](https://www.uniprot.org/uniprotkb/Q14957) (Glutamate receptor ionotropic, NMDA 2C):

> Component of N-methyl-D-aspartate (NMDA) receptors (NMDARs) that function as heterotetrameric, ligand-gated cation channels with high calcium permeability and voltage-dependent block by Mg(2+). Participates in synaptic plasticity for learning and memory formation by contributing to the slow phase of excitatory postsynaptic current and long-term synaptic potentiation (By similarity). Channel activation requires binding of the neurotransmitter L-glutamate to the GluN2 subunit, glycine or D-serine …

**Summary**, from NCBI Gene [2905](https://www.ncbi.nlm.nih.gov/gene/2905):

> This gene encodes a subunit of the N-methyl-D-aspartate (NMDA) receptor, which is a subtype of ionotropic glutamate receptor. NMDA receptors are found in the central nervous system, are permeable to cations and have an important role in physiological processes such as learning, memory, and synaptic development. The receptor is a tetramer of different subunits (typically heterodimer of subunit 1 with one or more of subunits 2A-D), forming a channel that is permeable to calcium, potassium, and …

**Accessions** — [HGNC:4587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4587) · Entrez [2905](https://www.ncbi.nlm.nih.gov/gene/2905) · UniProt [Q14957](https://www.uniprot.org/uniprotkb/Q14957) · Ensembl [ENSG00000161509](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161509)

## Data

Gene col 8433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8433); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8433]; `tensor/DDL_lfc|DDL_z.npy` [8433]; `embed/gene_vectors.npy` [8433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8433 or target_col == 8433). Every well: [[GRIN2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIN2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
