---
symbol: "SLCO1B3"
type: "gene"
col: 3265
ensembl_id: "ENSG00000111700"
name: "solute carrier organic anion transporter family member 1B3"
location: "12p12.2"
module: 73
arm: "+"
pooled_cpm: 133.8
n_lines_expressing: 22
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# SLCO1B3

*solute carrier organic anion transporter family member 1B3* — 12p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.99× (z +12.6, q 7e-34, up in 2 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.40× (z +6.2, q 2e-07, up in 0 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.463× (z -14.1, q 2e-42, down in 19 of 20 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLCO1B3-SLCO1B7]] (+0.84, fdr 7e-06, ⚠ same locus), [[LINC02582]] (+0.65, fdr 7e-06), [[CALB1]] (+0.61, fdr 1e-05), [[DSG4]] (+0.61, fdr 1e-05); moves opposite to [[RCOR3]] (-0.40, fdr 1e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 4 go from it, the strongest it → [[LINC00707]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3265.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +12.6 | 7e-34 | 2/21 (SW1417, HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +6.2 | 2e-07 | 0/20 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +5.7 | 2e-06 | 0/18 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +5.6 | 3e-06 | 2/19 (HT-29, A-427) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.009 | 5/20 (A-427, HT-29, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.012 | 0/22 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.026 | 0/20 | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.026 | 1/21 (A-427) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.20×** | +3.4 | 0.044 | 0/20 | inconsistent across doses | low cells (technical?) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.046 | 0/21 | inconsistent across doses | position effect removed |
| [[Temuterkib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.052 | 0/20 | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.095 | 0/20 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.1 | 0.095 | 15/20 (A-427, HCT15, …) | rises with dose | position effect removed |
| [[Pralsetinib (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.11 | 0/21 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3265.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.463×** | -14.1 | 2e-42 | 19/20 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -12.1 | 2e-31 | 20/20 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.549×** | -11.0 | 1e-25 | 20/20 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.709×** | -8.9 | 8e-17 | 18/20 (SW48, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.671×** | -7.0 | 3e-10 | 15/20 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.724×** | -5.9 | 4e-07 | 14/20 (LS 180, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.550×** | -5.7 | 9e-07 | 12/21 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.737×** | -5.6 | 2e-06 | 12/20 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.583×** | -5.2 | 2e-05 | 14/21 (A549, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.745×** | -5.0 | 4e-05 | 2/20 (HEC-1-A, RKO) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.755×** | -4.7 | 1e-04 | 1/20 (HEC-1-A) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.774×** | -4.7 | 1e-04 | 17/20 (HS-578T, SW48, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.845× | -4.3 | 7e-04 | 18/21 (SW48, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.803×** | -4.0 | 0.003 | 4/20 (H4, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.804×** | -3.8 | 0.005 | 17/20 (SW48, LS 180, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.008 | 12/20 (SW48, KATO III, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | **0.809×** | -3.6 | 0.012 | 0/20 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3265. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 486 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -29.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.120× (z -20.3) |
| [[LS 180 (line)]] | wt | 695 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0740× (z -26.8) |
| [[LoVo (line)]] | wt | 1,076 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -20.8) |
| [[A-172 (line)]] | wt | 217 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -19.2) |
| [[A549 (line)]] | wt | 349 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -20.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.203× (z -13.6) |
| [[H4 (line)]] | wt | 111 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0833× (z -19.0) |
| [[MIA PaCa-2 (line)]] | alt | 457 | 2 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -12.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW48 (line)]] | wt | 494 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -23.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.317× (z -10.8) |
| [[HCT15 (line)]] | alt | 453 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.221× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.152× (z -12.9) |
| [[Hs 766T (line)]] | wt | 356 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -14.0) |
| [[HT-29 (line)]] | alt | 75.9 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.196× (z -13.4) |
| [[A-427 (line)]] | wt | 123 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.92× (z +11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.91× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -9.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -17.4) |
| [[RKO (line)]] | wt | 83.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -14.9) |
| [[HS-578T (line)]] | alt | 60.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.333× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -9.4) |
| [[SW1417 (line)]] | alt | 41.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -8.5) |
| [[A498 (line)]] | wt | 7.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.72 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 26.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.85 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.75 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.64 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.16 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.17 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.62 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.18 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3265), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLCO1B3-SLCO1B7]] | +0.84 | +0.82 / +0.87 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC02582]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[CALB1]] | +0.61 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[DSG4]] | +0.61 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[B3GALT5]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[NOSTRIN]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[HEPH]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 | pathway: Disorders of transmembrane transporters |
| [[TPTEP1-1]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[NPSR1]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[SPON1]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ZNF736P9Y]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NPSR1-AS1]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[XACT]] | +0.53 | +0.54 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.40 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity strengthens SLCO1B3's drug response | lines that do not express F3 (8) vs lines expressing it (13) | the lines without F3 respond 0.83× as strongly (z diff +0.23); strongest at Belinostat 5 µM: 0.49x vs 0.30x (z diff +3.7) | 0.081 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA; target measured in part of the lines; both ways; artifact flags |
| [[SLCO1B3-SLCO1B7]] | C | SLCO1B3-SLCO1B7 activity raises SLCO1B3's level | lines that do not express SLCO1B3-SLCO1B7 (27) vs lines expressing it (23) | 11.50× lower at baseline in the lines without SLCO1B3-SLCO1B7 | 8e-06 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3, SLCO1B1; co-absent with the target |
| [[CASC19]] | C | CASC19 activity raises SLCO1B3's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 6.09× lower at baseline in the lines without CASC19 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises SLCO1B3's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 6.81× lower at baseline in the lines without LINC02582 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[DSG4]] | C | DSG4 activity raises SLCO1B3's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 10.74× lower at baseline in the lines without DSG4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031; co-absent with the target |
| [[MYO16-AS1]] | C | MYO16-AS1 activity raises SLCO1B3's level | lines that do not express MYO16-AS1 (23) vs lines expressing it (27) | 4.03× lower at baseline in the lines without MYO16-AS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000275216, KRT18, LAMC2; co-absent with the target |
| [[EDN1]] | C | EDN1 activity raises SLCO1B3's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 2.88× lower at baseline in the lines without EDN1 | 0.079 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00707]] | B | SLCO1B3 activity raises LINC00707's level | lines that do not express SLCO1B3 (28) vs lines expressing it (22) | 2.21× lower at baseline in the lines without SLCO1B3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3-SLCO1B7, SLCO1B1 |
| [[SLCO1B3-SLCO1B7]] | C | SLCO1B3 activity raises SLCO1B3-SLCO1B7's level | lines that do not express SLCO1B3 (28) vs lines expressing it (22) | 8.81× lower at baseline in the lines without SLCO1B3 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3-SLCO1B7, SLCO1B1; co-absent with the target |
| [[CASC19]] | C | SLCO1B3 activity raises CASC19's level | lines that do not express SLCO1B3 (28) vs lines expressing it (22) | 4.77× lower at baseline in the lines without SLCO1B3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3-SLCO1B7, SLCO1B1; co-absent with the target |
| [[LINC02582]] | C | SLCO1B3 activity raises LINC02582's level | lines that do not express SLCO1B3 (28) vs lines expressing it (22) | 3.25× lower at baseline in the lines without SLCO1B3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3-SLCO1B7, SLCO1B1; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.2, 50.7); signed map (66.4, 8.0). **Vector** length 81.1, 26.0% of its response variance represented; |z| ≥ 3 in 675 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.4 | +1.9 |
| fall | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -5.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -1.8 | -4.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier organic anion transporter family member 1B3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.2 — chr12:20,810,702-20,916,911 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OATP8, OATP1B3; previously SLC21A8 |
| Gene groups (HGNC) | Solute carrier organic anion transporter family |
| Reactome | 14 pathways, smallest: Atorvastatin ADME; Organic anion transport by SLCO transporters; Recycling of bile acids and salts |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPD5](https://www.uniprot.org/uniprotkb/Q9NPD5) (Solute carrier organic anion transporter family member 1B3):

> Mediates the Na(+)-independent uptake of organic anions. Shows broad substrate specificity, can transport both organic anions such as bile acid taurocholate (cholyltaurine) and conjugated steroids (17-beta-glucuronosyl estradiol, dehydroepiandrosterone sulfate (DHEAS), and estrone 3-sulfate), as well as eicosanoid leukotriene C4, prostaglandin E2 and L-thyroxine (T4). Hydrogencarbonate/HCO3(-) acts as the probable counteranion that exchanges for organic anions. Shows a pH-sensitive substrate …

**Summary**, from NCBI Gene [28234](https://www.ncbi.nlm.nih.gov/gene/28234):

> This gene encodes a liver-specific member of the organic anion transporter family. The encoded protein is a transmembrane receptor that mediates the sodium-independent uptake of endogenous and xenobiotic compounds and plays a critical role in bile acid and bilirubin transport. Mutations in this gene are a cause of Rotor type hyperbilirubinemia. Alternative splicing of this gene and the use of alternative promoters results in transcript variants encoding different isoforms that differ in their …

**Accessions** — [HGNC:10961](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10961) · Entrez [28234](https://www.ncbi.nlm.nih.gov/gene/28234) · UniProt [Q9NPD5](https://www.uniprot.org/uniprotkb/Q9NPD5) · Ensembl [ENSG00000111700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111700)

## Data

Gene col 3265: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3265); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3265, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3265]; `tensor/DDL_lfc|DDL_z.npy` [3265]; `embed/gene_vectors.npy` [3265]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3265 or target_col == 3265). Every well: [[SLCO1B3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO1B3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
