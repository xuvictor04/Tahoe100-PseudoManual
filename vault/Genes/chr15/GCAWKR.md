---
symbol: "GCAWKR"
type: "gene"
col: 15744
ensembl_id: "ENSG00000272808"
name: "gastric cancer associated WDR5 and KAT2A binding lncRNA"
location: "15q26.3"
module: 10
arm: "+"
pooled_cpm: 2.01
n_lines_expressing: 30
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# GCAWKR

*gastric cancer associated WDR5 and KAT2A binding lncRNA* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.28× (z +8.1, q 3e-13, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.49× (z +4.0, q 0.012, up in 10 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.383× (z -6.8, q 7e-09, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGBL2]] (+0.60, fdr 1e-05), [[ANKRD20A21P]] (+0.59, fdr 3e-05), [[CFL1P1-1]] (+0.55, fdr 3e-05); moves opposite to [[COPS8]] (-0.40, fdr 2e-04), [[SHC1]] (-0.40, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ANKRD20A21P]] → it (grade B ⚠); 6 go from it, the strongest it → [[JHY]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +8.1 | 3e-13 | 1/3 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.7 | 7e-04 | 5/19 (CFPAC-1, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.012 | 10/26 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 1.59× | +3.3 | 0.11 | 5/22 (LoVo, RPMI-7951, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.59× | +3.3 | 0.11 | 4/22 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Filgotinib (drug)]] 5 µM |  | 1.57× | +3.2 | 0.12 | 3/27 (NCI-H1792, HOP62, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.58× | +3.1 | 0.14 | 1/9 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.53× | +3.0 | 0.18 | 3/9 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.383×** | -6.8 | 7e-09 | 18/26 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.471×** | -5.1 | 9e-05 | 13/22 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.603×** | -5.0 | 9e-05 | 12/19 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.512×** | -4.7 | 3e-04 | 13/24 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.548×** | -4.2 | 0.003 | 9/25 (SK-MEL-2, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.588×** | -3.7 | 0.018 | 8/22 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.609×** | -3.5 | 0.040 | 9/24 (SW480, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.398×** | -3.4 | 0.048 | 10/21 (CFPAC-1, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.636×** | -3.2 | 0.091 | 6/26 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.624×** | -3.1 | 0.097 | 14/23 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.645× | -3.1 | 0.11 | 6/26 (NCI-H1792, SW 900, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 5.50 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.108× (z -10.3) |
| [[PANC-1 (line)]] | alt | 4.22 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0696× (z -12.3) |
| [[A549 (line)]] | wt | 2.19 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0660× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0409× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 5.15 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0291× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 0.135 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.174 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.149 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.158 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.130 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.201 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.139 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.191 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.680 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.166 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGBL2]] | +0.60 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD20A21P]] | +0.59 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[CFL1P1-1]] | +0.55 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[FAM66C]] | +0.54 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[LMO7-AS1]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[FKBP14-AS1]] | +0.51 | +0.56 / +0.49 | both halves | 2e-05 |  |
| [[ERICH6-AS1]] | +0.51 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[MEI1]] | +0.50 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[CNTNAP3]] | +0.50 | +0.48 / +0.37 | both halves | 9e-05 |  |
| [[ZNF706]] | +0.50 | +0.40 / +0.52 | both halves | 5e-05 |  |
| [[NOTUM]] | +0.50 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[WBP2NL]] | +0.48 | +0.60 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS8]] | -0.40 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[SHC1]] | -0.40 | -0.29 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD20A21P]] | B | ANKRD20A21P activity strengthens GCAWKR's drug response | lines that do not express ANKRD20A21P (15) vs lines expressing it (11) | the lines without ANKRD20A21P respond 0.58× as strongly (z diff +1.41); strongest at Harringtonine 5 µM: 0.39x vs 0.17x (z diff +3.7) | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000229618, PAX2, ANKRD20A11P; target measured in part of the lines; artifact flags |
| [[KLHL14]] | B | KLHL14 activity strengthens GCAWKR's drug response | lines that do not express KLHL14 (21) vs lines expressing it (5) | the lines without KLHL14 respond 0.48× as strongly (z diff +1.84); strongest at Harringtonine 5 µM: 0.33x vs 0.16x (z diff +3.7) | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; target measured in part of the lines; the reference differs; artifact flags |
| [[ANKRD20A11P]] | B | ANKRD20A11P activity raises GCAWKR's level | lines that do not express ANKRD20A11P (29) vs lines expressing it (21) | 1.39× lower at baseline in the lines without ANKRD20A11P | 0.067 | ⚠ within organs, on part of the lines; also absent: KCNQ2, RBM11, ANKRD20A21P |
| [[FMNL1-DT]] | C | FMNL1-DT activity raises GCAWKR's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 1.67× lower at baseline in the lines without FMNL1-DT | 0.027 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent; co-absent with the target |
| [[CNTNAP3C]] | C | CNTNAP3C activity raises GCAWKR's level | lines that do not express CNTNAP3C (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without CNTNAP3C | 0.033 | ⚠ within organs, on part of the lines; also absent: CNTNAP3, CNTNAP3B, IL31RA; co-absent with the target |
| [[CNTNAP3]] | C | CNTNAP3 activity raises GCAWKR's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without CNTNAP3 | 0.043 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[BASP1-AS1]] | C | BASP1-AS1 activity raises GCAWKR's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without BASP1-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JHY]] | B | GCAWKR activity raises JHY's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 2.72× lower at baseline in the lines without GCAWKR | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[FAM66C]] | B | GCAWKR activity raises FAM66C's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.68× lower at baseline in the lines without GCAWKR | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[TESMIN]] | B | GCAWKR activity raises TESMIN's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.68× lower at baseline in the lines without GCAWKR | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[CCDC3]] | B | GCAWKR activity raises CCDC3's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.36× lower at baseline in the lines without GCAWKR | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[ALDH1A3-AS1]] | B | GCAWKR activity raises ALDH1A3-AS1's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.24× lower at baseline in the lines without GCAWKR | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |
| [[SMCO2]] | B | GCAWKR activity raises SMCO2's level | lines that do not express GCAWKR (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without GCAWKR | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000232386, IL31RA, BEX2 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.311). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.9, 30.3); signed map (36.9, -8.7). **Vector** length 39.8, 6.99% of its response variance represented; |z| ≥ 3 in 558 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.7 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -4.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | gastric cancer associated WDR5 and KAT2A binding lncRNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q26.3 — chr15:100,849,831-100,876,836 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53740) · Entrez [105369201](https://www.ncbi.nlm.nih.gov/gene/105369201) · Ensembl [ENSG00000272808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272808)

## Data

Gene col 15744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15744); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15744]; `tensor/DDL_lfc|DDL_z.npy` [15744]; `embed/gene_vectors.npy` [15744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15744 or target_col == 15744). Every well: [[GCAWKR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCAWKR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
