---
symbol: "ME3"
type: "gene"
col: 7514
ensembl_id: "ENSG00000151376"
name: "malic enzyme 3"
location: "11q14.2"
module: 1
arm: "+"
pooled_cpm: 27.43
n_lines_expressing: 37
n_dd_up: 4
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ME3

*malic enzyme 3* — 11q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.34× (z +5.0, q 3e-04, up in 20 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.321× (z -14.0, q 2e-41, down in 29 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRA3]] (+0.67, fdr 1e-05), [[CCND1]] (+0.64, fdr 1e-05), [[ABCE1]] (+0.64, fdr 1e-05); moves opposite to [[CNOT8]] (-0.65, fdr 1e-05), [[ANG]] (-0.64, fdr 1e-05), [[RAB6A]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NRP1]] → it (grade B ⚠); 11 go from it, the strongest it → [[PRSS23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7514.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.0 | 3e-04 | 20/35 (CFPAC-1, Hs 766T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 0.003 | 17/35 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +3.6 | 0.059 | 13/28 (NCI-H460, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Demeclocycline (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.059 | 12/35 (J82, KATO III, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.31× | +3.3 | 0.10 | 7/35 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7514.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.321×** | -14.0 | 2e-41 | 29/35 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.354×** | -12.7 | 9e-35 | 30/35 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.355×** | -12.7 | 9e-35 | 28/35 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.618×** | -8.4 | 9e-15 | 27/34 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.607×** | -6.1 | 9e-08 | 25/35 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.603×** | -5.9 | 4e-07 | 22/35 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.647×** | -5.4 | 7e-06 | 21/35 (SHP-77, SW48, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.671×** | -4.9 | 7e-05 | 21/35 (KATO III, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.678×** | -4.8 | 1e-04 | 23/35 (HOP62, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.481×** | -4.7 | 1e-04 | 19/35 (HOP62, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.701×** | -4.4 | 6e-04 | 21/35 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.780×** | -4.3 | 7e-04 | 17/35 (J82, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.512×** | -4.3 | 7e-04 | 19/35 (NCI-H23, SNU-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **0.707×** | -4.3 | 8e-04 | 18/32 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -3.9 | 0.003 | 20/33 (SNU-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.729×** | -3.5 | 0.015 | 19/35 (SW 1088, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.756×** | -3.1 | 0.053 | 8/35 (NCI-H1792, SW 1088, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7514. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 41.1 | 0 | 11 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -13.4) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -12.4) |
| [[J82 (line)]] | alt | 81.2 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 64.0 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -11.3) |
| [[SW1417 (line)]] | alt | 44.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -12.3) |
| [[LoVo (line)]] | wt | 23.0 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 13.1 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.23× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 36.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.228× (z -9.8) |
| [[PANC-1 (line)]] | alt | 82.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -11.0) |
| [[SNU-1 (line)]] | wt | 55.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0898× (z -14.9) |
| [[SW480 (line)]] | alt | 26.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -11.7) |
| [[LS 180 (line)]] | wt | 38.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -11.2) |
| [[RKO (line)]] | wt | 37.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -9.8) |
| [[SW48 (line)]] | wt | 39.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.196× (z -8.8) |
| [[A-172 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0782× (z -10.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 31.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -8.7) |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.257× (z -8.8) |
| [[A-427 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7514), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRA3]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CCND1]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.64 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CTPS1]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[ATXN10]] | +0.61 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[UTP20]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | +0.60 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[SLC39A10]] | +0.60 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[PARVA]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[CDK6]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TRIM44]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNOT8]] | -0.65 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ANG]] | -0.64 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.62 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[LMBR1L]] | -0.59 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[KLHL7]] | -0.59 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[CAMLG]] | -0.59 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[CRYZL1]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[MACO1]] | -0.58 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[PLEKHH3]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[PDCD10]] | -0.58 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[ANKRD9]] | -0.58 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TRIM62]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP1]] | B | NRP1 activity raises ME3's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without NRP1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[PRSS23]] | B | PRSS23 activity raises ME3's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without PRSS23 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[ZNF469]] | B | ZNF469 activity raises ME3's level | lines that do not express ZNF469 (20) vs lines expressing it (30) | 1.82× lower at baseline in the lines without ZNF469 | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | ME3 activity raises PRSS23's level | lines that do not express ME3 (13) vs lines expressing it (37) | 3.03× lower at baseline in the lines without ME3 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[ZNF469]] | B | ME3 activity raises ZNF469's level | lines that do not express ME3 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without ME3 | 0.008 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[NRP1]] | B | ME3 activity raises NRP1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 2.84× lower at baseline in the lines without ME3 | 0.009 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[EIF4G1]] | B | ME3 activity lowers EIF4G1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.27× higher at baseline in the lines without ME3 | 0.044 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[CBLB]] | B | ME3 activity raises CBLB's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without ME3 | 0.052 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[SDHAP2]] | B | ME3 activity raises SDHAP2's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without ME3 | 0.062 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[ABCE1]] | B | ME3 activity lowers ABCE1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.23× higher at baseline in the lines without ME3 | 0.075 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 5 µM | B | ME3 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express ME3 (13) vs lines expressing it (35) | the lines without ME3: 0.93× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[LRRK1]] | B | ME3 activity raises LRRK1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without ME3 | 0.081 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[THOC6]] | B | ME3 activity lowers THOC6's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.37× higher at baseline in the lines without ME3 | 0.092 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[CTPS1]] | B | ME3 activity lowers CTPS1's level | lines that do not express ME3 (13) vs lines expressing it (37) | 1.41× higher at baseline in the lines without ME3 | 0.099 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (7.1, -17.1); signed map (10.0, -42.4). **Vector** length 88.9, 22.8% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.0 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.9 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | -12.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -14.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | malic enzyme 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.2 — chr11:86,441,108-86,672,636 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Malic enzyme family |
| Reactome | 2 pathways, smallest: Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16798](https://www.uniprot.org/uniprotkb/Q16798) (NADP-dependent malic enzyme, mitochondrial):

> Catalyzes the oxidative decarboxylation of (S)-malate to pyruvate using NADP(+), and is able to reverse the reaction but only with significantly lower efficiency. Can also catalyze the decarboxylation of oxaloacetate into pyruvate (By similarity).

**Summary**, from NCBI Gene [10873](https://www.ncbi.nlm.nih.gov/gene/10873):

> Malic enzyme catalyzes the oxidative decarboxylation of malate to pyruvate using either NAD+ or NADP+ as a cofactor. Mammalian tissues contain 3 distinct isoforms of malic enzyme: a cytosolic NADP(+)-dependent isoform, a mitochondrial NADP(+)-dependent isoform, and a mitochondrial NAD(+)-dependent isoform. This gene encodes a mitochondrial NADP(+)-dependent isoform. Multiple alternatively spliced transcript variants have been found for this gene, but the biological validity of some variants has …

**Accessions** — [HGNC:6985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6985) · Entrez [10873](https://www.ncbi.nlm.nih.gov/gene/10873) · UniProt [Q16798](https://www.uniprot.org/uniprotkb/Q16798) · Ensembl [ENSG00000151376](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151376)

## Data

Gene col 7514: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7514); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7514, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7514]; `tensor/DDL_lfc|DDL_z.npy` [7514]; `embed/gene_vectors.npy` [7514]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7514 or target_col == 7514). Every well: [[ME3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ME3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
