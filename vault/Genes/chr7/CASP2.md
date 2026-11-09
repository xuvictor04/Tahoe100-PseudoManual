---
symbol: "CASP2"
type: "gene"
col: 2727
ensembl_id: "ENSG00000106144"
name: "caspase 2"
location: "7q34"
module: 6
arm: "+"
pooled_cpm: 30.14
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CASP2

*caspase 2* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.59× (z +8.7, q 1e-15, up in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.59× (z +4.6, q 6e-04, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.563× (z -15.3, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHMT1]] (+0.74, fdr 9e-06), [[MSH2]] (+0.74, fdr 7e-06), [[RBL1]] (+0.73, fdr 7e-06); moves opposite to [[KRBOX5]] (-0.64, fdr 3e-05), [[PPP1R12A-AS2]] (-0.63, fdr 1e-05), [[GATAD1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CDCA7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.59×** | +8.7 | 1e-15 | 33/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.59×** | +8.7 | 1e-15 | 32/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.45×** | +7.0 | 4e-10 | 30/48 (SW1417, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +4.6 | 6e-04 | 20/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.26×** | +4.1 | 0.004 | 12/37 (LoVo, Panc 03.27, …) | rises with dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.016 | 14/48 (HT-29, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.22×** | +3.7 | 0.019 | 16/47 (MIA PaCa-2, NCI-H2030, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.6 | 0.023 | 9/48 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.023 | 10/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.032 | 14/47 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.19× | +3.2 | 0.061 | 9/48 (LoVo, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.563×** | -15.3 | 0e+00 | 37/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -11.9 | 3e-30 | 37/48 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.563×** | -10.9 | 3e-25 | 35/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.781×** | -4.7 | 4e-04 | 20/48 (BT-474, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -4.7 | 4e-04 | 18/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.794×** | -4.2 | 0.002 | 19/48 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -4.2 | 0.002 | 17/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.801×** | -4.0 | 0.004 | 24/48 (SW48, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.863× | -4.0 | 0.005 | 18/48 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.821×** | -3.7 | 0.010 | 17/46 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | **0.828×** | -3.6 | 0.018 | 16/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[AZD2858 (drug)]] 5 µM | ⚠ toxic | 0.736× | -3.0 | 0.12 | 7/44 (Hs 766T, A549, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 39.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -15.8) |
| [[SW480 (line)]] | alt | 69.6 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -10.7) |
| [[A-172 (line)]] | wt | 21.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.1) |
| [[Hs 766T (line)]] | wt | 19.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.7) |
| [[KATO III (line)]] | alt | 50.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.3) |
| [[LoVo (line)]] | wt | 34.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 22.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.9) |
| [[RKO (line)]] | wt | 43.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -10.1) |
| [[BT-474 (line)]] | alt | 44.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -9.7) |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.101× (z -8.7) |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -14.7) |
| [[LOX-IMVI (line)]] | wt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -9.5) |
| [[LS 180 (line)]] | wt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.217× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 9.36 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.181× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 32.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -14.8) |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.9) |
| [[SW48 (line)]] | wt | 56.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -12.4) |
| [[A-427 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHMT1]] | +0.74 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[MSH2]] | +0.74 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[RBL1]] | +0.73 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SKP2]] | +0.73 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[UNG]] | +0.71 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[RFC5]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[MCM3]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[PARP1]] | +0.69 | +0.59 / +0.55 | both halves | 1e-05 | STRING 597 |
| [[BLM]] | +0.69 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[DDX12P]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBOX5]] | -0.64 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | -0.63 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[GATAD1]] | -0.63 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[MAPK6]] | -0.62 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[THAP2]] | -0.62 | -0.67 / -0.34 | both halves | 1e-04 |  |
| [[AK9]] | -0.61 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[INTS6-AS1]] | -0.61 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[CCDC90B]] | -0.60 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[DNAH12]] | -0.60 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[BOLA1]] | -0.60 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[MED29]] | -0.60 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[CFAP53]] | -0.59 | -0.59 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7]] | B | CDCA7 activity raises CASP2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.01× lower at baseline in the lines without CDCA7 | 0.019 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises CASP2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without E2F2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CASP2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.96× lower at baseline in the lines without CDC25A | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises CASP2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without TCF19 | 0.048 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises CASP2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[MCM10]] | C | MCM10 activity raises CASP2's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without MCM10 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.3, -43.5); signed map (-35.5, -42.7). **Vector** length 104, 23.5% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.54 to 28); *DNA Replication* (reactome, mean cos +0.53 to 40); *E2F G1/S* (control, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.7 | +7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.5 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.4 | +8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -15.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -10.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.5 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -4.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | caspase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:143,288,215-143,307,696 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ICH1, PPP1R57, MGC2181; previously NEDD2 |
| Gene groups (HGNC) | Caspases; Protein phosphatase 1 regulatory subunits; Caspase recruitment domain containing; Caspase-2 PIDDosome complex |
| Hallmark sets | APOPTOSIS |
| Reactome | 10 pathways, smallest: NADE modulates death signalling; TP53 Regulates Transcription of Caspase Activators and Caspases; NOD1/2 Signaling Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P42575](https://www.uniprot.org/uniprotkb/P42575) (Caspase-2):

> Is a regulator of the cascade of caspases responsible for apoptosis execution. Might function by either activating some proteins required for cell death or inactivating proteins necessary for cell survival. Associates with PIDD1 and CRADD to form the PIDDosome, a complex that activates CASP2 and triggers apoptosis in response to genotoxic stress.; [Isoform 1]: Acts as a positive regulator of apoptosis.; [Isoform 2]: Acts as a negative regulator of apoptosis.; [Isoform 3]: May function as an …

**Summary**, from NCBI Gene [835](https://www.ncbi.nlm.nih.gov/gene/835):

> This gene encodes a member of the cysteine-aspartic acid protease (caspase) family. Caspases mediate cellular apoptosis through the proteolytic cleavage of specific protein substrates. The encoded protein may function in stress-induced cell death pathways, cell cycle maintenance, and the suppression of tumorigenesis. Increased expression of this gene may play a role in neurodegenerative disorders including Alzheimer's disease, Huntington's disease and temporal lobe epilepsy. Alternatively …

**Accessions** — [HGNC:1503](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1503) · Entrez [835](https://www.ncbi.nlm.nih.gov/gene/835) · UniProt [P42575](https://www.uniprot.org/uniprotkb/P42575) · Ensembl [ENSG00000106144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106144)

## Data

Gene col 2727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2727); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2727]; `tensor/DDL_lfc|DDL_z.npy` [2727]; `embed/gene_vectors.npy` [2727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2727 or target_col == 2727). Every well: [[CASP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
