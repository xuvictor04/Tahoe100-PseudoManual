---
symbol: "ZKSCAN2-DT"
type: "gene"
col: 15832
ensembl_id: "ENSG00000274925"
name: "ZKSCAN2 divergent transcript"
location: "16p12.1"
module: 114
arm: "+"
pooled_cpm: 7.4
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 17
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# ZKSCAN2-DT

*ZKSCAN2 divergent transcript* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.45× (z +11.0, q 1e-25, up in 31 of 35 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.64× (z +6.4, q 5e-08, up in 22 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 8.23×; ⚠ toxic).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.468× (z -9.3, q 5e-18, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPN2]] (+0.65, fdr 3e-05), [[PGLS-DT]] (+0.64, fdr 2e-05), [[MIRLET7A1HG]] (+0.62, fdr 3e-05); moves opposite to [[MDH1]] (-0.58, fdr 1e-05), [[COPS6]] (-0.56, fdr 1e-05), [[DMXL2]] (-0.51, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF418]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15832.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (KATO III 8.23×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +11.0 | 1e-25 | 31/35 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +6.4 | 5e-08 | 22/45 (HT-29, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15832.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.468×** | -9.3 | 5e-18 | 34/46 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.551×** | -7.6 | 6e-12 | 31/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.575×** | -7.1 | 3e-10 | 30/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.588×** | -6.8 | 1e-09 | 22/32 (NCI-H1573, A-172, …) | inconsistent across doses | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.623×** | -6.1 | 1e-07 | 24/47 (BT-474, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.657×** | -5.4 | 7e-06 | 20/46 (COLO 205, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.655×** | -5.2 | 2e-05 | 19/39 (C32, HepG2/C3A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.669×** | -4.9 | 5e-05 | 19/43 (A-172, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.679×** | -4.8 | 1e-04 | 18/40 (A-172, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -4.7 | 1e-04 | 19/46 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.694×** | -4.7 | 1e-04 | 17/43 (HepG2/C3A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.773×** | -4.7 | 2e-04 | 20/45 (SNU-423, AsPC-1, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.750×** | -3.7 | 0.010 | 12/36 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.762×** | -3.5 | 0.020 | 13/47 (J82, hTERT-HPNE, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.829×** | -3.4 | 0.026 | 17/43 (H4, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.10 | 0 | 3 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 9.37 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -11.2) |
| [[A549 (line)]] | wt | 5.99 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.108× (z -9.0) |
| [[C32 (line)]] | wt | 5.95 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0881× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 13.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.103× (z -9.9) |
| [[J82 (line)]] | alt | 6.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 8.75 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 8.23× (z +10.0) ⚠ toxic | — |
| [[LS 180 (line)]] | wt | 7.18 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0780× (z -11.6) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 5.02 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0756× (z -9.1) |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 8.80 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -8.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 6.17 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0937× (z -9.5) |
| [[SW1417 (line)]] | alt | 8.81 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0683× (z -13.5) ⚠ transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPN2]] | +0.65 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[PGLS-DT]] | +0.64 | +0.46 / +0.67 | both halves | 2e-05 | same gene group |
| [[MIRLET7A1HG]] | +0.62 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[ZNF251]] | +0.61 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[LINC01772]] | +0.60 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[ZNF35]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[ZNF302]] | +0.60 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[CDC20-DT]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 | same gene group |
| [[SLC25A17]] | +0.59 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[ZNF586]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[ZNF418]] | +0.59 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[C19orf25]] | +0.59 | +0.58 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MDH1]] | -0.58 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[COPS6]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[DMXL2]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[SPTBN1]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CD2AP]] | -0.50 | -0.43 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF418]] | B | ZNF418 activity raises ZKSCAN2-DT's level | lines that do not express ZNF418 (10) vs lines expressing it (40) | 1.26× lower at baseline in the lines without ZNF418 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZNF304, MOCS1, A1BG |
| [[LINC03046]] | B | LINC03046 activity raises ZKSCAN2-DT's level | lines that do not express LINC03046 (38) vs lines expressing it (12) | 1.24× lower at baseline in the lines without LINC03046 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, LINC00824, LINC01205 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.3, 24.5); signed map (2.1, -1.3). **Vector** length 62.6, 8.84% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.7 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.5 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.2 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | -3.0 | -6.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | -2.9 | -5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.8 | +0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.3 | -4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ZKSCAN2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p12.1 — chr16:25,257,952-25,261,066 (+) |
| Ensembl biotype | lncRNA |
| Also known as | CTD-2547G23.4 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53912) · Entrez [112577464](https://www.ncbi.nlm.nih.gov/gene/112577464) · Ensembl [ENSG00000274925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274925)

## Data

Gene col 15832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15832); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15832]; `tensor/DDL_lfc|DDL_z.npy` [15832]; `embed/gene_vectors.npy` [15832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15832 or target_col == 15832). Every well: [[ZKSCAN2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZKSCAN2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
