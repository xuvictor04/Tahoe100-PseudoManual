---
symbol: "ACSF3"
type: "gene"
col: 10744
ensembl_id: "ENSG00000176715"
name: "acyl-CoA synthetase family member 3"
location: "16q24.3"
module: 1
arm: "+"
pooled_cpm: 23.03
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ACSF3

*acyl-CoA synthetase family member 3* — 16q24.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.248× (z -27.7, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD54L2]] (+0.68, fdr 7e-06), [[MTG1]] (+0.66, fdr 1e-05), [[AGK]] (+0.65, fdr 1e-05); moves opposite to [[CXCR4]] (-0.61, fdr 4e-05), [[GNAS]] (-0.60, fdr 1e-05), [[TMEM59]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IGFBP6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.47 | 15/47 (LOX-IMVI, HOP62, …) | two highest doses |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.47 | 6/48 (C32, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.248×** | -27.7 | 0e+00 | 46/47 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.429×** | -11.5 | 6e-28 | 38/47 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.489×** | -9.7 | 8e-20 | 36/48 (C-33 A, SNU-1, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.503×** | -9.3 | 2e-18 | 34/45 (LoVo, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.525×** | -9.1 | 1e-17 | 32/48 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.526×** | -8.7 | 3e-16 | 35/47 (COLO 205, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.564×** | -8.1 | 6e-14 | 38/47 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.738×** | -6.1 | 1e-07 | 26/47 (C32, A-172, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.681×** | -5.4 | 4e-06 | 27/47 (NCI-H1573, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.488×** | -5.3 | 8e-06 | 28/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.688×** | -5.3 | 8e-06 | 26/47 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.788×** | -4.7 | 1e-04 | 25/48 (A-172, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.789×** | -4.7 | 1e-04 | 23/48 (HOP62, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.718×** | -4.7 | 1e-04 | 21/47 (NCI-H23, BT-474, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.819×** | -4.0 | 0.003 | 18/48 (J82, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.792×** | -3.3 | 0.030 | 12/48 (NCI-H661, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.793×** | -3.3 | 0.030 | 16/48 (J82, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.642×** | -3.3 | 0.030 | 15/45 (A-427, SNU-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.804×** | -2.9 | 0.079 | 10/48 (HOP62, J82, …) | top dose only | position effect removed |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | **0.815×** | -2.9 | 0.095 | 5/47 (NCI-H2030, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 26.4 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.212× (z -9.9) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -9.4) |
| [[C32 (line)]] | wt | 23.6 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -15.1) |
| [[COLO 205 (line)]] | alt | 52.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 39.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0842× (z -26.5) |
| [[SNU-1 (line)]] | wt | 25.9 | 0 | 4 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0947× (z -11.4) |
| [[SW480 (line)]] | alt | 21.3 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -22.2) |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0351× (z -16.4) |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 3 | — | [[PH-797804 (drug)]] 0.5 µM 0.0628× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -17.2) |
| [[HOP62 (line)]] | alt | 25.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -18.0) |
| [[J82 (line)]] | alt | 25.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -15.0) |
| [[KATO III (line)]] | alt | 28.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -17.3) |
| [[LoVo (line)]] | wt | 24.8 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -14.8) |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -11.0) |
| [[PANC-1 (line)]] | alt | 16.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -18.1) |
| [[A-172 (line)]] | wt | 33.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -17.0) |
| [[A549 (line)]] | wt | 24.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0724× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 32.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 28.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.5) |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -11.9) |
| [[A-427 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.304× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[A498 (line)]] | wt | 19.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -9.5) |
| [[H4 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.104× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.9) |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -16.9) |
| [[HS-578T (line)]] | alt | 15.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -12.5) |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 28.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0581× (z -29.0) |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 18.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -18.8) |
| [[Panc 03.27 (line)]] | alt | 23.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 21.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -11.6) |
| [[SHP-77 (line)]] | alt | 28.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -10.8) |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0986× (z -19.9) |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -8.9) |
| [[AN3 CA (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD54L2]] | +0.68 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[MTG1]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[AGK]] | +0.65 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[EIF2B3]] | +0.63 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[TCERG1]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[METTL2A]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ZNF202]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[CUL9]] | +0.62 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[EEFSEC]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[RAD51D]] | +0.62 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[CLPB]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[DRG2]] | +0.62 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CXCR4]] | -0.61 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[GNAS]] | -0.60 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CDC14A]] | -0.60 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[CERT1]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.59 | -0.34 / -0.76 | both halves | 1e-04 |  |
| [[LNX2]] | -0.58 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.58 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MORC3]] | -0.57 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[CDIPT]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[HBP1]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ATOSA]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFBP6]] | B | IGFBP6 activity lowers ACSF3's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 1.37× higher at baseline in the lines without IGFBP6 | 0.024 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[TOP2A]] | B | TOP2A activity raises ACSF3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.0, -40.4); signed map (-8.6, -47.2). **Vector** length 78.8, 16.3% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +0.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -27.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -9.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -4.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.7 | -1.6 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:89,088,375-89,164,121 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Reactome | 4 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G176](https://www.uniprot.org/uniprotkb/Q4G176) (Malonate--CoA ligase ACSF3, mitochondrial):

> Catalyzes the initial reaction in intramitochondrial fatty acid synthesis, by activating malonate and methylmalonate, but not acetate, into their respective CoA thioester. May have some preference toward very-long-chain substrates.

**Summary**, from NCBI Gene [197322](https://www.ncbi.nlm.nih.gov/gene/197322):

> This gene encodes a member of the acyl-CoA synthetase family of enzymes that activate fatty acids by catalyzing the formation of a thioester linkage between fatty acids and coenzyme A. The encoded protein is localized to mitochondria, has high specificity for malonate and methylmalonate and possesses malonyl-CoA synthetase activity. Mutations in this gene are a cause of combined malonic and methylmalonic aciduria. Alternatively spliced transcript variants have been observed for this gene. …

**Accessions** — [HGNC:27288](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27288) · Entrez [197322](https://www.ncbi.nlm.nih.gov/gene/197322) · UniProt [Q4G176](https://www.uniprot.org/uniprotkb/Q4G176) · Ensembl [ENSG00000176715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176715)

## Data

Gene col 10744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10744); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10744]; `tensor/DDL_lfc|DDL_z.npy` [10744]; `embed/gene_vectors.npy` [10744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10744 or target_col == 10744). Every well: [[ACSF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
