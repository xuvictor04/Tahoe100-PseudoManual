---
symbol: "MGMT"
type: "gene"
col: 9952
ensembl_id: "ENSG00000170430"
name: "O-6-methylguanine-DNA methyltransferase"
location: "10q26.3"
module: 4
arm: "+"
pooled_cpm: 42.59
n_lines_expressing: 39
n_dd_up: 0
n_dd_down: 51
n_dd_up_clean: 0
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MGMT

*O-6-methylguanine-DNA methyltransferase* — 10q26.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.169× (z -32.8, q 0e+00, down in 37 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02666]] (+0.62, fdr 7e-06, ⚠ read-through risk), [[CDKAL1]] (+0.60, fdr 3e-05), [[MSH3]] (+0.51, fdr 2e-05), [[FARS2]] (+0.50, fdr 6e-05); moves opposite to [[TSHZ3-AS1]] (-0.59, fdr 1e-05), [[TSHZ3]] (-0.46, fdr 7e-05), [[OVOL1]] (-0.46, fdr 7e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02666]] → it (grade C ⚠); 3 go from it, the strongest it → [[HDAC8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9952.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.21× | +3.5 | 0.18 | 15/37 (AsPC-1, LoVo, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.30× | +3.4 | 0.18 | 18/37 (CFPAC-1, PANC-1, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.28× | +3.2 | 0.28 | 16/37 (NCI-H2347, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9952.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.169×** | -32.8 | 0e+00 | 37/37 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.179×** | -22.4 | 0e+00 | 36/37 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.209×** | -20.4 | 0e+00 | 35/37 (LS 180, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.203×** | -20.0 | 0e+00 | 35/37 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.437×** | -15.2 | 0e+00 | 36/37 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.312×** | -15.2 | 0e+00 | 37/37 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.341×** | -14.0 | 1e-42 | 34/37 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.328×** | -14.0 | 2e-42 | 31/37 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.368×** | -13.0 | 7e-37 | 34/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.232×** | -10.0 | 1e-21 | 34/37 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.507×** | -8.5 | 1e-15 | 29/37 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.568×** | -7.3 | 1e-11 | 30/37 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.578×** | -7.1 | 4e-11 | 30/37 (J82, Panc 03.27, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.395×** | -6.3 | 1e-08 | 29/37 (SK-MEL-2, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.506×** | -6.3 | 1e-08 | 26/37 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.628×** | -6.0 | 6e-08 | 27/37 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -5.7 | 3e-07 | 22/37 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.732×** | -5.7 | 3e-07 | 26/37 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -5.1 | 8e-06 | 22/37 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9952. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 59.5 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0927× (z -27.5) |
| [[PANC-1 (line)]] | alt | 61.2 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -30.5) |
| [[SNU-1 (line)]] | wt | 103 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -19.1) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -24.7) |
| [[NCI-H23 (line)]] | alt | 88.9 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -32.6) |
| [[NCI-H1573 (line)]] | alt | 74.1 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -30.7) |
| [[Panc 03.27 (line)]] | alt | 65.0 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -18.7) |
| [[LoVo (line)]] | wt | 72.8 | 0 | 11 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0710× (z -26.9) |
| [[COLO 205 (line)]] | alt | 68.3 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -22.0) |
| [[J82 (line)]] | alt | 38.5 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0832× (z -27.3) |
| [[HT-29 (line)]] | alt | 65.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -20.8) |
| [[C-33 A (line)]] | alt | 83.1 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0885× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -16.4) |
| [[HOP62 (line)]] | alt | 30.2 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -18.7) |
| [[Hs 766T (line)]] | wt | 63.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -20.0) |
| [[LS 180 (line)]] | wt | 38.2 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0518× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -14.4) |
| [[RKO (line)]] | wt | 102 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -28.6) |
| [[HepG2_C3A (line)]] | wt | 49.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -16.7) |
| [[KATO III (line)]] | alt | 39.7 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0852× (z -17.4) |
| [[CFPAC-1 (line)]] | alt | 45.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -17.8) |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -18.3) |
| [[SW 900 (line)]] | alt | 34.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -15.1) |
| [[A498 (line)]] | wt | 34.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0808× (z -28.8) |
| [[AsPC-1 (line)]] | alt | 28.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -17.5) |
| [[H4 (line)]] | wt | 21.9 | 0 | 5 (2 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0584× (z -13.6) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -9.1) |
| [[HCT15 (line)]] | alt | 55.4 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -13.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -20.7) |
| [[A549 (line)]] | wt | 21.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -18.9) |
| [[AN3 CA (line)]] | alt | 149 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0683× (z -22.8) |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0340× (z -16.8) |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.111× (z -10.8) |
| [[SW1417 (line)]] | alt | 36.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -14.6) |
| [[BT-474 (line)]] | alt | 25.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.344× (z -8.8) |
| [[SW480 (line)]] | alt | 12.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 29.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -18.4) |
| [[A-172 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9952), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02666]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 | ⚠ **readthrough risk**: LINC02666 lies 14.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[CDKAL1]] | +0.60 | +0.44 / +0.63 | both halves | 3e-05 | same gene group |
| [[MSH3]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 | STRING 575 |
| [[FARS2]] | +0.50 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[NUBPL]] | +0.49 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[STX18-AS1]] | +0.48 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[SPIDR]] | +0.48 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[DIS3L2]] | +0.47 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[LCLAT1]] | +0.47 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[ALDH5A1]] | +0.47 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[UNG]] | +0.46 | +0.43 / +0.45 | both halves | 3e-05 | STRING 523 |
| [[IPO11]] | +0.46 | +0.29 / +0.56 | both halves | 3e-04 |  |
| [[FAM98B]] | +0.46 | +0.38 / +0.43 | both halves | 6e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSHZ3-AS1]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TSHZ3]] | -0.46 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[OVOL1]] | -0.46 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[CCNYL1]] | -0.44 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[MEIS3]] | -0.43 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[HAS2-AS1]] | -0.43 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[NFATC4]] | -0.43 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[CDKN2B]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 | STRING 589 |
| [[ZCCHC24]] | -0.43 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[BVES]] | -0.43 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[MSC-AS1]] | -0.42 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[HNRNPLL]] | -0.42 | -0.38 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02666]] | C | LINC02666 activity raises MGMT's level | lines that do not express LINC02666 (14) vs lines expressing it (36) | 8.32× lower at baseline in the lines without LINC02666 | 4e-06 | ⚠ within organs, on part of the lines; also absent: MGMT; co-absent with the target |
| [[PUDP]] | C | PUDP activity raises MGMT's level | lines that do not express PUDP (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without PUDP | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF264, ENSG00000287188 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC8]] | B | MGMT activity raises HDAC8's level | lines that do not express MGMT (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without MGMT | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC02666, CDCP1, ZNF718 |
| [[WDR44]] | B | MGMT activity raises WDR44's level | lines that do not express MGMT (11) vs lines expressing it (39) | 1.19× lower at baseline in the lines without MGMT | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02666, CDCP1, ZNF718 |
| [[LINC02666]] | C | MGMT activity raises LINC02666's level | lines that do not express MGMT (11) vs lines expressing it (39) | 3.27× lower at baseline in the lines without MGMT | 2e-04 | ⚠ within organs, on part of the lines; also absent: LINC02666, CDCP1, ZNF718; co-absent with the target |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-15.4, -13.6); signed map (-14.9, -49.2). **Vector** length 77.6, 21.9% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.2 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +1.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.4 | +1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Encorafenib (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | -6.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -15.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.5 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | -4.2 | -5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -5.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | +0.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Saquinavir (drug)]] 5 µM |  | -1.8 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | O-6-methylguanine-DNA methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:129,467,190-129,770,983 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DNA/RNA methyltransferases; Methyltransferases with unique structures |
| Hallmark sets | UV_RESPONSE_DN, APOPTOSIS |
| Reactome | 2 pathways, smallest: DNA Damage Reversal; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [P16455](https://www.uniprot.org/uniprotkb/P16455) (Methylated-DNA--protein-cysteine methyltransferase):

> Involved in the cellular defense against the biological effects of O6-methylguanine (O6-MeG) and O4-methylthymine (O4-MeT) in DNA. Repairs the methylated nucleobase in DNA by stoichiometrically transferring the methyl group to a cysteine residue in the enzyme. This is a suicide reaction: the enzyme is irreversibly inactivated.

**Summary**, from NCBI Gene [4255](https://www.ncbi.nlm.nih.gov/gene/4255):

> Alkylating agents are potent carcinogens that can result in cell death, mutation and cancer. The protein encoded by this gene is a DNA repair protein that is involved in cellular defense against mutagenesis and toxicity from alkylating agents. The protein catalyzes transfer of methyl groups from O(6)-alkylguanine and other methylated moieties of the DNA to its own molecule, which repairs the toxic lesions. Methylation of the genes promoter has been associated with several cancer types, …

**Accessions** — [HGNC:7059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7059) · Entrez [4255](https://www.ncbi.nlm.nih.gov/gene/4255) · UniProt [P16455](https://www.uniprot.org/uniprotkb/P16455) · Ensembl [ENSG00000170430](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170430)

## Data

Gene col 9952: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9952); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9952, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9952]; `tensor/DDL_lfc|DDL_z.npy` [9952]; `embed/gene_vectors.npy` [9952]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9952 or target_col == 9952). Every well: [[MGMT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGMT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
