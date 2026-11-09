---
symbol: "RMI1"
type: "gene"
col: 10980
ensembl_id: "ENSG00000178966"
name: "RecQ mediated genome instability 1"
location: "9q21.32"
module: 91
arm: "+"
pooled_cpm: 24.04
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# RMI1

*RecQ mediated genome instability 1* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.73× (z +21.9, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.460× (z -6.3, q 2e-07, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP1]] (+0.74, fdr 7e-06), [[PRIMPOL]] (+0.74, fdr 7e-06), [[RMI2]] (+0.72, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +21.9 | 0e+00 | 45/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.21×** | +11.8 | 1e-29 | 40/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.92×** | +9.7 | 4e-20 | 38/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.65×** | +7.5 | 1e-11 | 19/31 (NCI-H2030, BT-474, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +7.2 | 9e-11 | 28/48 (J82, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.54×** | +6.5 | 9e-09 | 21/42 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.53×** | +6.3 | 2e-08 | 26/47 (J82, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.46×** | +5.9 | 3e-07 | 20/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.3 | 7e-06 | 21/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.27×** | +5.2 | 1e-05 | 18/48 (SW480, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.9 | 4e-05 | 19/48 (HOP62, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +4.4 | 5e-04 | 19/42 (NCI-H2030, SHP-77, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.005 | 15/48 (HS-578T, NCI-H460, …) | all doses, flat |  |
| [[Thymol (drug)]] 5 µM |  | 1.17× | +3.5 | 0.016 | 9/48 (C-33 A, HEC-1-A, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.17× | +3.5 | 0.016 | 7/48 (HCT15, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.019 | 19/47 (SW480, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.034 | 4/48 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.037 | 5/48 (J82, KATO III, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.046 | 13/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.077 | 5/48 (BT-474, SK-MEL-2, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.14× | +2.9 | 0.091 | 6/48 (NCI-H1573, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -6.3 | 2e-07 | 28/48 (SW 900, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.773×** | -5.6 | 6e-06 | 25/48 (C32, LOX-IMVI, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.519×** | -5.3 | 2e-05 | 22/46 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.730×** | -4.8 | 2e-04 | 22/48 (SNU-1, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.731×** | -4.4 | 0.001 | 19/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.759×** | -4.3 | 0.002 | 20/47 (LoVo, LS 180, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.704×** | -3.9 | 0.009 | 13/48 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.809× | -3.1 | 0.11 | 17/46 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.800× | -3.1 | 0.11 | 10/48 (HOP62, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ivermectin (drug)]] 5 µM |  | 0.821× | -3.0 | 0.13 | 5/48 (SW480, HOP62, …) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.806× | -3.0 | 0.13 | 15/48 (A498, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 59.7 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.376× (z -9.4) ⚠ toxic |
| [[SW480 (line)]] | alt | 30.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +15.5) | — |
| [[NCI-H2030 (line)]] | alt | 11.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 21.1× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 30.8 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -12.2) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 9.65 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +8.7) | [[Drospirenone (drug)]] 0.5 µM 0.114× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 23.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +13.4) | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0592× (z -9.8) |
| [[SW48 (line)]] | wt | 14.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0764× (z -9.6) |
| [[A549 (line)]] | wt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 21.5 | 0 | 1 | — | [[Oxaliplatin (drug)]] 0.05 µM 0.0431× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 8.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +9.2) | — |
| [[C32 (line)]] | wt | 7.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.113× (z -9.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 16.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +9.5) | — |
| [[LoVo (line)]] | wt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 9.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.20× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 24.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 28.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.9) | — |
| [[RKO (line)]] | wt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.01× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.35× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 26.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +13.4) | — |
| [[A-172 (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP1]] | +0.74 | +0.66 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[PRIMPOL]] | +0.74 | +0.66 / +0.70 | both halves | 7e-06 | STRING 542 |
| [[RMI2]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 999 |
| [[BRCA1]] | +0.72 | +0.73 / +0.69 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 915 |
| [[ESCO2]] | +0.72 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[GSTCD]] | +0.71 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[RAD51AP1]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 746 |
| [[DYRK4]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ATAD5]] | +0.70 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PLK4]] | +0.69 | +0.58 / +0.77 | both halves | 8e-06 |  |
| [[ZNF367]] | +0.69 | +0.62 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RMI1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises RMI1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without FAM111B | 0.037 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises RMI1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without E2F2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises RMI1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without MCM10 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises RMI1's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.29× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises RMI1's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without CLSPN | 0.075 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[PKMYT1]] | C | PKMYT1 activity raises RMI1's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without PKMYT1 | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-39.1, -47.0); signed map (-41.9, -47.7). **Vector** length 107, 26.6% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.2 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +21.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.3 | +9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.5 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +5.3 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +2.2 | +1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | -5.1 | +7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.8 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RecQ mediated genome instability 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:83,980,798-84,004,074 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12888, BLAP75; previously C9orf76 |
| Reactome | 28 pathways, smallest: Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9A7](https://www.uniprot.org/uniprotkb/Q9H9A7) (RecQ-mediated genome instability protein 1):

> Essential component of the RMI complex, a complex that plays an important role in the processing of homologous recombination intermediates to limit DNA crossover formation in cells. Promotes TOP3A binding to double Holliday junctions (DHJ) and hence stimulates TOP3A-mediated dissolution. Required for BLM phosphorylation during mitosis. Within the BLM complex, required for BLM and TOP3A stability.

**Summary**, from NCBI Gene [80010](https://www.ncbi.nlm.nih.gov/gene/80010):

> Predicted to enable nucleotide binding activity. Involved in double-strand break repair via homologous recombination and resolution of DNA recombination intermediates. Located in nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25764) · Entrez [80010](https://www.ncbi.nlm.nih.gov/gene/80010) · UniProt [Q9H9A7](https://www.uniprot.org/uniprotkb/Q9H9A7) · Ensembl [ENSG00000178966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178966)

## Data

Gene col 10980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10980); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10980]; `tensor/DDL_lfc|DDL_z.npy` [10980]; `embed/gene_vectors.npy` [10980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10980 or target_col == 10980). Every well: [[RMI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
