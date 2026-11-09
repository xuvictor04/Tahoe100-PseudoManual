---
symbol: "ZNF79"
type: "gene"
col: 12141
ensembl_id: "ENSG00000196152"
name: "zinc finger protein 79"
location: "9q33.3"
module: 62
arm: "+"
pooled_cpm: 7.79
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# ZNF79

*zinc finger protein 79* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +19.9, q 0e+00, up in 39 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.119×, Hs 766T 0.116×; ⚠ toxic; transcription drop); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (HT-29 0.0649×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (NCI-H23 0.0952×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.106×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MDM2]] (+0.72, fdr 7e-06), [[SPATA18]] (+0.68, fdr 1e-05), [[FDXR]] (+0.67, fdr 1e-05); moves opposite to [[LRBA]] (-0.52, fdr 1e-04), [[ELOVL5]] (-0.51, fdr 4e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PINCR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12141.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +19.9 | 0e+00 | 39/44 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +18.2 | 0e+00 | 38/42 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **13.7×** | +18.1 | 0e+00 | 47/47 (NCI-H460, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +12.1 | 2e-31 | 33/42 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **5.40×** | +11.7 | 2e-29 | 33/42 (SW480, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.19×** | +10.4 | 2e-23 | 37/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.08×** | +9.7 | 2e-20 | 37/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.02×** | +9.3 | 1e-18 | 35/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **2.10×** | +8.7 | 1e-16 | 21/34 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +7.7 | 6e-13 | 27/46 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.89×** | +7.5 | 3e-12 | 23/45 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.39×** | +6.1 | 5e-08 | 21/47 (RKO, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.6 | 7e-07 | 23/48 (RKO, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.53×** | +5.6 | 8e-07 | 20/46 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.52×** | +5.5 | 1e-06 | 19/46 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.7 | 8e-05 | 15/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 1e-04 | 16/46 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +4.1 | 1e-03 | 13/44 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.002 | 4/47 (A-427, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.003 | 9/47 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.003 | 10/44 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.2 | 0.028 | 13/47 (A549, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.031 | 11/47 (LS 180, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12141.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.119×, Hs 766T 0.116×; ⚠ toxic; transcription drop); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (HT-29 0.0649×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (NCI-H23 0.0952×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.6 | 0.15 | 9/48 (COLO 205, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.746× | -3.5 | 0.15 | 9/16 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.780× | -3.3 | 0.18 | 16/33 (LS 180, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Flutamide (drug)]] 5 µM |  | 0.796× | -3.0 | 0.34 | 10/47 (HS-578T, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12141. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 8.62 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -9.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 13.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 6.37 | 0 | 3 (1 ⚠) | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.106× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 10.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +14.2) | — |
| [[RKO (line)]] | wt | 17.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +13.0) | — |
| [[SW480 (line)]] | alt | 7.27 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.9) | — |
| [[A498 (line)]] | wt | 10.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +12.0) | — |
| [[A-172 (line)]] | wt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +9.5) | — |
| [[C32 (line)]] | wt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 3.16 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0594× (z -8.7) |
| [[HT-29 (line)]] | alt | 4.44 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0649× (z -10.4) |
| [[J82 (line)]] | alt | 9.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 9.20 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 47.0× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 6.50 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0952× (z -9.4) |
| [[PANC-1 (line)]] | alt | 5.25 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.13 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.113× (z -8.8) |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12141), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDM2]] | +0.72 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[SPATA18]] | +0.68 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[FDXR]] | +0.67 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[DCP1B]] | +0.67 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ACTA2]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[GRIN2C]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ZMAT3]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[BAX]] | +0.66 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[PHLDA3]] | +0.65 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[EDA2R]] | +0.65 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[PINCR]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[CES2]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRBA]] | -0.52 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[ELOVL5]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PINCR]] | B | PINCR activity raises ZNF79's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.44× lower at baseline in the lines without PINCR | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[PINCR]] | B | PINCR activity strengthens ZNF79's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.80× as strongly (z diff +0.72); strongest at Idarubicin (hydrochloride) 5 µM: 2.35x vs 3.53x (z diff +2.7) | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[EDA2R]] | B | EDA2R activity raises ZNF79's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.32× lower at baseline in the lines without EDA2R | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[TOP2A]] | B | TOP2A activity lowers ZNF79's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises ZNF79's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.38× lower at baseline in the lines without PTCHD4 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[FDXR]] | B | FDXR activity raises ZNF79's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without FDXR | 0.049 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[TP53]] | B | TP53 activity strengthens ZNF79's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.82× as strongly (z diff +0.65); strongest at Idarubicin (hydrochloride) 5 µM: 2.30x vs 4.04x (z diff +3.1) | 0.065 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |
| [[GRIN2C]] | B | GRIN2C activity raises ZNF79's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without GRIN2C | 0.081 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.2, 36.3); signed map (42.2, -24.2). **Vector** length 73.3, 13.2% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 pathway* (hallmark, mean cos +0.51 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.57 to 6); *apoptosis* (hallmark, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +18.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +19.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +4.4 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.3 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +1.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 79 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:127,424,374-127,445,372 (+) |
| Ensembl biotype | protein_coding |
| Also known as | pT7 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15937](https://www.uniprot.org/uniprotkb/Q15937) (Zinc finger protein 79):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7633](https://www.ncbi.nlm.nih.gov/gene/7633):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13153) · Entrez [7633](https://www.ncbi.nlm.nih.gov/gene/7633) · UniProt [Q15937](https://www.uniprot.org/uniprotkb/Q15937) · Ensembl [ENSG00000196152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196152)

## Data

Gene col 12141: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12141); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12141, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12141]; `tensor/DDL_lfc|DDL_z.npy` [12141]; `embed/gene_vectors.npy` [12141]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12141 or target_col == 12141). Every well: [[ZNF79 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF79.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
