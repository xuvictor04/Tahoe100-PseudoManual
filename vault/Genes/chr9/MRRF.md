---
symbol: "MRRF"
type: "gene"
col: 7250
ensembl_id: "ENSG00000148187"
name: "mitochondrial ribosome recycling factor"
location: "9q33.2"
module: 1
arm: "+"
pooled_cpm: 36.88
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MRRF

*mitochondrial ribosome recycling factor* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.54× (z +9.9, q 4e-20, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.679× (z -9.3, q 9e-18, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (HEC-1-A 0.491×, NCI-H460 0.534×, SHP-77 0.453×, LoVo 0.532×, …); [[Nimesulide (drug)]] 5 µM in 1 line (AN3 CA 0.0647×; ⚠ toxic; unreliable plate only); [[Flutamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0756×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDAH]] (+0.82, fdr 7e-06), [[ZNF507]] (+0.76, fdr 7e-06), [[GUF1]] (+0.76, fdr 7e-06); moves opposite to [[CDK2AP2]] (-0.70, fdr 3e-05), [[NARF]] (-0.67, fdr 1e-05), [[CARD19]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.54×** | +9.9 | 4e-20 | 40/48 (RKO, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.33×** | +6.9 | 1e-09 | 35/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.41×** | +6.9 | 1e-09 | 28/48 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.3 | 2e-05 | 24/47 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.0 | 4e-05 | 21/38 (A549, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.34×** | +5.0 | 4e-05 | 28/48 (Hs 766T, RKO, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +4.9 | 7e-05 | 26/48 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.8 | 1e-04 | 23/46 (AsPC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.8 | 1e-04 | 26/48 (A549, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.32×** | +4.6 | 2e-04 | 24/47 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +4.1 | 0.002 | 19/44 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.008 | 19/48 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.009 | 16/47 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.013 | 19/47 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.16× | +3.5 | 0.019 | 10/48 (COLO 205, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.021 | 15/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.057 | 9/48 (NCI-H460, BT-474, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.19× | +3.1 | 0.070 | 14/48 (A498, Hs 766T, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.080 | 7/48 (A498, BT-474, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7250.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (HEC-1-A 0.491×, NCI-H460 0.534×, SHP-77 0.453×, LoVo 0.532×, …); [[Nimesulide (drug)]] 5 µM in 1 line (AN3 CA 0.0647×; ⚠ toxic; unreliable plate only); [[Flutamide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0756×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -9.3 | 9e-18 | 36/48 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.721×** | -5.7 | 4e-06 | 31/48 (J82, SW480, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.771×** | -4.5 | 0.001 | 23/48 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.776×** | -4.4 | 0.001 | 23/48 (SW480, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.778×** | -4.4 | 0.001 | 20/47 (PANC-1, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.775×** | -4.3 | 0.002 | 22/47 (SW 1271, SW480, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -4.0 | 0.005 | 16/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.833× | -3.2 | 0.10 | 15/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.838× | -3.1 | 0.13 | 10/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 57.5 | 2 | 1 | [[PH-797804 (drug)]] 5 µM 5.40× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -11.5) |
| [[A-172 (line)]] | wt | 36.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 39.8 | 0 | 2 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0647× (z -12.4) ⚠ toxic; unreliable plate only · without an alert: [[Flutamide (drug)]] 0.5 µM 0.0756× (z -11.6) |
| [[A-427 (line)]] | wt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +8.6) | — |
| [[A549 (line)]] | wt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 45.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 51.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -9.7) |
| [[PANC-1 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.436× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[RKO (line)]] | wt | 71.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.26× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 49.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -8.8) |
| [[SNU-423 (line)]] | alt | 34.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -8.8) |
| [[A498 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 45.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDAH]] | +0.82 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.76 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[GUF1]] | +0.76 | +0.63 / +0.79 | both halves | 7e-06 | STRING 688 |
| [[METAP1D]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[UTP15]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[MTPAP]] | +0.72 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[MTHFSD]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[RRP15]] | +0.71 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[SF3B3]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[COA7]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[FKTN]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK2AP2]] | -0.70 | -0.43 / -0.75 | both halves | 3e-05 |  |
| [[NARF]] | -0.67 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[CARD19]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[CIB1]] | -0.66 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[ANKRD37]] | -0.64 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[MACO1]] | -0.64 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.63 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[TMEM184B]] | -0.63 | -0.57 / -0.60 | both halves | 9e-06 |  |
| [[ZCCHC24]] | -0.62 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[RNF122]] | -0.62 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[TESK2]] | -0.62 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[CARHSP1]] | -0.61 | -0.43 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MRRF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01535]] | B | LINC01535 activity raises MRRF's level | lines that do not express LINC01535 (21) vs lines expressing it (29) | 1.17× lower at baseline in the lines without LINC01535 | 0.0998 | ⚠ within organs, on part of the lines; also absent: MIR3681HG, AFF3, KCNJ6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.3, -16.9); signed map (2.0, -39.5). **Vector** length 115, 28.7% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial mRNA modification* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.7 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.2 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.1 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.6 | -2.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.9 | -2.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosome recycling factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:122,264,603-122,331,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | mtRRF, RRF |
| Reactome | 3 pathways, smallest: Mitochondrial translation termination; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E11](https://www.uniprot.org/uniprotkb/Q96E11) (Ribosome-recycling factor, mitochondrial):

> Responsible for the disassembly of ribosomes from messenger RNA at the termination of mitochondrial protein biosynthesis. Acts in collaboration with GFM2. Promotes mitochondrial ribosome recycling by dissolution of intersubunit contacts.

**Summary**, from NCBI Gene [92399](https://www.ncbi.nlm.nih.gov/gene/92399):

> This gene encodes a ribosome recycling factor, which is a component of the mitochondrial translational machinery. The encoded protein, along with mitochondrial elongation factor 2, functions in ribosomal recycling at the termination of mitochondrial translation by mediating the disassembly of ribosomes from messenger RNA. A pseudogene of this gene has been identified on chromosome X. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:7234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7234) · Entrez [92399](https://www.ncbi.nlm.nih.gov/gene/92399) · UniProt [Q96E11](https://www.uniprot.org/uniprotkb/Q96E11) · Ensembl [ENSG00000148187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148187)

## Data

Gene col 7250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7250); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7250]; `tensor/DDL_lfc|DDL_z.npy` [7250]; `embed/gene_vectors.npy` [7250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7250 or target_col == 7250). Every well: [[MRRF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRRF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
