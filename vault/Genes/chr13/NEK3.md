---
symbol: "NEK3"
type: "gene"
col: 5810
ensembl_id: "ENSG00000136098"
name: "NIMA related kinase 3"
location: "13q14.3"
module: 17
arm: "+"
pooled_cpm: 14.65
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NEK3

*NIMA related kinase 3* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 1.28× (z +4.5, q 0.003, up in 11 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.325× (z -21.8, q 0e+00, down in 38 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESD]] (+0.63, fdr 2e-05), [[SAAL1]] (+0.62, fdr 2e-05), [[COMMD2]] (+0.59, fdr 1e-05); moves opposite to [[EOLA2-DT]] (-0.57, fdr 5e-05), [[FANK1]] (-0.56, fdr 3e-05), [[TICAM2]] (-0.56, fdr 6e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Radotinib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +4.5 | 0.003 | 11/44 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.17× | +4.4 | 0.003 | 11/45 (PANC-1, NCI-H661, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 0.003 | 14/44 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.23×** | +4.0 | 0.008 | 11/44 (NCI-H2347, NCI-H1573, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.045 | 11/39 (HCT15, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.2 | 0.096 | 9/45 (NCI-H1573, NCI-H2347, …) | two highest doses |  |
| [[Bexarotene (drug)]] 5 µM |  | 1.18× | +3.2 | 0.096 | 6/44 (LOX-IMVI, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.325×** | -21.8 | 0e+00 | 38/44 (SW480, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.531×** | -17.4 | 0e+00 | 35/43 (HepG2/C3A, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.520×** | -12.2 | 6e-32 | 32/42 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.651×** | -11.8 | 7e-30 | 24/42 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -9.7 | 2e-20 | 25/44 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -8.6 | 1e-15 | 22/44 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -8.0 | 1e-13 | 23/44 (SW480, J82, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.688×** | -7.3 | 3e-11 | 21/44 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.701×** | -6.9 | 3e-10 | 21/44 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.716×** | -6.5 | 5e-09 | 21/44 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -6.1 | 4e-08 | 19/44 (J82, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -5.9 | 2e-07 | 17/45 (Hs 766T, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.744×** | -5.8 | 4e-07 | 19/44 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.588×** | -5.4 | 3e-06 | 21/42 (SW480, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.773×** | -5.0 | 2e-05 | 17/42 (SW480, A498, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.788×** | -4.6 | 1e-04 | 12/44 (A-172, H4, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.799×** | -4.4 | 4e-04 | 13/44 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.661×** | -4.2 | 8e-04 | 18/41 (A-427, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.675×** | -4.0 | 0.002 | 13/43 (SW 900, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.8 | 0 | 9 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.220× (z -15.1) |
| [[A498 (line)]] | wt | 25.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -16.5) |
| [[A-172 (line)]] | wt | 16.1 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -10.7) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -9.3) |
| [[A549 (line)]] | wt | 20.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.8) |
| [[COLO 205 (line)]] | alt | 42.6 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.116× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -11.7) |
| [[J82 (line)]] | alt | 10.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.198× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -14.5) |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.290× (z -10.4) |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0771× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.270× (z -9.6) |
| [[HOP62 (line)]] | alt | 7.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.6) |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -9.1) |
| [[HT-29 (line)]] | alt | 19.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.232× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -12.0) |
| [[KATO III (line)]] | alt | 25.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.223× (z -10.9) |
| [[LoVo (line)]] | wt | 9.04 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 23.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.305× (z -9.6) |
| [[LS 180 (line)]] | wt | 24.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.244× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 9.06 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.198× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 8.22 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.0) |
| [[RKO (line)]] | wt | 22.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.145× (z -11.6) |
| [[SHP-77 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.120× (z -11.0) |
| [[SW 900 (line)]] | alt | 6.73 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0924× (z -9.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESD]] | +0.63 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[SAAL1]] | +0.62 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[COMMD2]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[VPS54]] | +0.56 | +0.46 / +0.67 | both halves | 2e-05 |  |
| [[ZNHIT6]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[FCSK]] | +0.55 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[COMMD7]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[UBXN2B]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[GEMIN2]] | +0.54 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MRPS31P4]] | +0.54 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[MDM1]] | +0.54 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[BBS5]] | +0.53 | +0.44 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOLA2-DT]] | -0.57 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[FANK1]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[TICAM2]] | -0.56 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[SLC9A5]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[TRPV1]] | -0.52 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[DNHD1]] | -0.51 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[VWCE]] | -0.51 | -0.43 / -0.53 | both halves | 4e-05 |  |
| [[COL20A1]] | -0.50 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[FER1L4]] | -0.50 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[GOSR2]] | -0.50 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[LINC02245]] | -0.50 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TTC41P]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NEK3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Radotinib (drug)]] 5 µM | C | NEK3 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express NEK3 (3) vs lines expressing it (45) | the lines without NEK3: 0.81× the cells of the other lines | 0.041 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP36, IQCN, SLC22A20P |
| [[VPS54]] | C | NEK3 activity strengthens VPS54's drug response | lines that do not express NEK3 (3) vs lines expressing it (47) | the lines without NEK3 respond 0.59× as strongly (z diff +2.88); strongest at Idarubicin (hydrochloride) 5 µM: 0.98x vs 0.59x (z diff +6.4) | 0.083 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP36, IQCN, SLC22A20P; artifact flags |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.4, -2.3); signed map (-22.9, -15.6). **Vector** length 79.5, 14.4% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.0 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.7 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.8 | -21.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -5.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -6.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | NIMA related kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:52,132,639-52,159,597 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPK36, MGC29949 |
| Gene groups (HGNC) | NIMA related kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [P51956](https://www.uniprot.org/uniprotkb/P51956) (Serine/threonine-protein kinase Nek3):

> Protein kinase which influences neuronal morphogenesis and polarity through effects on microtubules. Regulates microtubule acetylation in neurons. Contributes to prolactin-mediated phosphorylation of PXN and VAV2. Implicated in prolactin-mediated cytoskeletal reorganization and motility of breast cancer cells through mechanisms involving RAC1 activation and phosphorylation of PXN and VAV2.

**Summary**, from NCBI Gene [4752](https://www.ncbi.nlm.nih.gov/gene/4752):

> This gene encodes a member of the NimA (never in mitosis A) family of serine/threonine protein kinases. The encoded protein differs from other NimA family members in that it is not cell cycle regulated and is found primarily in the cytoplasm. The kinase is activated by prolactin stimulation, leading to phosphorylation of VAV2 guanine nucleotide exchange factor, paxillin, and activation of the RAC1 GTPase. Two functional alleles for this gene have been identified in humans. The reference genome …

**Accessions** — [HGNC:7746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7746) · Entrez [4752](https://www.ncbi.nlm.nih.gov/gene/4752) · UniProt [P51956](https://www.uniprot.org/uniprotkb/P51956) · Ensembl [ENSG00000136098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136098)

## Data

Gene col 5810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5810); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5810]; `tensor/DDL_lfc|DDL_z.npy` [5810]; `embed/gene_vectors.npy` [5810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5810 or target_col == 5810). Every well: [[NEK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
