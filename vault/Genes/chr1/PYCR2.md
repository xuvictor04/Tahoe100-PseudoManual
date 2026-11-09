---
symbol: "PYCR2"
type: "gene"
col: 6808
ensembl_id: "ENSG00000143811"
name: "pyrroline-5-carboxylate reductase 2"
location: "1q42.12"
module: 124
arm: "+"
pooled_cpm: 14.8
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# PYCR2

*pyrroline-5-carboxylate reductase 2* — 1q42.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.85× (z +14.8, q 0e+00, up in 39 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.45× (z +11.9, q 3e-30, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.353× (z -5.1, q 2e-04, down in 30 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.150×; ⚠ cell-cycle shift, would explain all of this change); [[Simotinib (drug)]] 5 µM in 1 line (BT-474 0.102×; ⚠ toxic).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM5]] (+0.67, fdr 3e-05), [[RXYLT1]] (+0.66, fdr 2e-05), [[KLHL42]] (+0.63, fdr 4e-05); moves opposite to [[CFD]] (-0.61, fdr 4e-04), [[OSBPL9]] (-0.60, fdr 1e-04), [[SLC27A1]] (-0.58, fdr 0.001, ⚠ one half only (not replicated)), [[HDAC1]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.85×** | +14.8 | 0e+00 | 39/39 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.29×** | +13.1 | 7e-37 | 24/24 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +11.9 | 3e-30 | 45/46 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.52×** | +8.0 | 2e-13 | 31/32 (HOP62, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +7.5 | 8e-12 | 38/46 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +7.5 | 8e-12 | 35/46 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +6.3 | 3e-08 | 36/42 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.90×** | +5.8 | 5e-07 | 33/46 (SW480, NCI-H1792, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +5.8 | 5e-07 | 34/46 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.83×** | +5.6 | 1e-06 | 31/41 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.4 | 5e-04 | 25/48 (Hs 766T, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.002 | 22/46 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.52×** | +3.8 | 0.007 | 19/41 (SNU-423, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +3.3 | 0.045 | 17/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.26×** | +3.1 | 0.076 | 19/48 (PANC-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6808.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.150×; ⚠ cell-cycle shift, would explain all of this change); [[Simotinib (drug)]] 5 µM in 1 line (BT-474 0.102×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.353×** | -5.1 | 2e-04 | 30/44 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.526× | -3.2 | 0.36 | 19/48 (SW480, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.699× | -3.1 | 0.36 | 15/47 (A498, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +9.6) | — |
| [[A-427 (line)]] | wt | 20.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 11.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.57× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LOX-IMVI (line)]] | wt | 9.31 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.55× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 8.22 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 16.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.45× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 18.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.5) | — |
| [[SW480 (line)]] | alt | 16.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 8.45 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.35× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AsPC-1 (line)]] | alt | 9.03 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.0× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[BT-474 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.102× (z -9.6) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.69× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[Hs 766T (line)]] | wt | 13.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HT-29 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.13× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.1) | — |
| [[A498 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM5]] | +0.67 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[RXYLT1]] | +0.66 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[KLHL42]] | +0.63 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[ZNF337-AS1]] | +0.62 | +0.65 / +0.39 | both halves | 6e-05 |  |
| [[MRPS16]] | +0.61 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[PIGW]] | +0.61 | +0.61 / +0.30 | both halves | 2e-04 |  |
| [[FBF1]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[LINC01829]] | +0.61 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[ENOX2]] | +0.60 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[CCNJ]] | +0.60 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[ZNF689]] | +0.60 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[TIMMDC1]] | +0.60 | +0.70 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFD]] | -0.61 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[OSBPL9]] | -0.60 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.58 | -0.66 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[HDAC1]] | -0.56 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[LMTK3]] | -0.55 | -0.52 / -0.26 | both halves | 3e-04 |  |
| [[MAST3]] | -0.55 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[STX7]] | -0.55 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[CYB5R4]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[RPS5]] | -0.53 | -0.56 / -0.21 | both halves | 7e-04 | pathway: Metabolism of amino acids and derivatives |
| [[GUSBP18]] | -0.53 | -0.52 / -0.24 | both halves | 4e-04 |  |
| [[PRUNE1]] | -0.53 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[STARD3NL]] | -0.53 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[RAB3A]] | -0.53 | -0.37 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PYCR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.0, 8.2); signed map (22.8, -26.4). **Vector** length 65.9, 13.7% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +11.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +0.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | pyrroline-5-carboxylate reductase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.12 — chr1:225,919,877-225,924,340 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P5CR2 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Pyrroline-5-carboxylate reductase family |
| Reactome | 2 pathways, smallest: Glutamate and glutamine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96C36](https://www.uniprot.org/uniprotkb/Q96C36) (Pyrroline-5-carboxylate reductase 2):

> Oxidoreductase that catalyzes the last step in proline biosynthesis, which corresponds to the reduction of pyrroline-5-carboxylate to L-proline using NAD(P)H. At physiologic concentrations, has higher specific activity in the presence of NADH. Involved in cellular response to oxidative stress. In some cell types, such as erythrocytes, its primary function may be the generation of NADP(+).

**Summary**, from NCBI Gene [29920](https://www.ncbi.nlm.nih.gov/gene/29920):

> This gene belongs to the pyrroline-5-carboxylate reductase family. The encoded mitochondrial protein catalyzes the conversion of pyrroline-5-carboxylate to proline, which is the last step in proline biosynthesis. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:30262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30262) · Entrez [29920](https://www.ncbi.nlm.nih.gov/gene/29920) · UniProt [Q96C36](https://www.uniprot.org/uniprotkb/Q96C36) · Ensembl [ENSG00000143811](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143811)

## Data

Gene col 6808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6808); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6808]; `tensor/DDL_lfc|DDL_z.npy` [6808]; `embed/gene_vectors.npy` [6808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6808 or target_col == 6808). Every well: [[PYCR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYCR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
