---
symbol: "PCDH10"
type: "gene"
col: 6204
ensembl_id: "ENSG00000138650"
name: "protocadherin 10"
location: "4q28.3"
module: 9
arm: "+"
pooled_cpm: 5.19
n_lines_expressing: 26
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 4
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PCDH10

*protocadherin 10* — 4q28.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.78× (z +23.3, q 0e+00, up in 17 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H23 0.0641×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCDH17]] (+0.75, fdr 7e-06), [[RORB]] (+0.63, fdr 1e-05), [[EPHA7]] (+0.63, fdr 7e-06); moves opposite to [[WIPF1]] (-0.46, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[SLC25A16]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.78×** | +23.3 | 0e+00 | 17/19 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.99×** | +14.5 | 1e-45 | 12/18 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.67×** | +13.9 | 1e-41 | 3/8 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.76×** | +11.5 | 2e-28 | 4/9 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.27×** | +11.1 | 1e-26 | 3/12 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +10.7 | 1e-24 | 20/22 (A-427, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.17×** | +10.3 | 7e-23 | 12/22 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.54×** | +8.7 | 2e-16 | 18/22 (A-427, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.48×** | +8.5 | 1e-15 | 17/22 (A-427, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.21×** | +7.4 | 6e-12 | 17/22 (A-427, A498, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +7.4 | 6e-12 | 17/21 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +7.2 | 3e-11 | 8/18 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +6.9 | 2e-10 | 10/15 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +6.4 | 8e-09 | 4/13 (J82, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +6.2 | 2e-08 | 10/16 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +5.8 | 2e-07 | 19/22 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +5.6 | 7e-07 | 7/19 (HOP62, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.1 | 9e-06 | 7/22 (J82, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +4.9 | 3e-05 | 8/19 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.64×** | +4.6 | 8e-05 | 3/22 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.012 | 6/21 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.023 | 4/21 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H23 0.0641×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.685× | -3.6 | 0.21 | 4/22 (NCI-H2030, RPMI-7951, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.681× | -3.3 | 0.23 | 0/22 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -3.1 | 0.31 | 7/23 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.539× | -3.0 | 0.31 | 2/23 (SK-MEL-2, hTERT-HPNE) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 95.1 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +13.9) | — |
| [[A-427 (line)]] | wt | 2.62 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 44.3× (z +10.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 10.5× (z +9.3) | — |
| [[A498 (line)]] | wt | 3.34 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.0× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 7.68 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.6× (z +16.7) | — |
| [[C32 (line)]] | wt | 3.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 6.14 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 5.50 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +12.2) | — |
| [[H4 (line)]] | wt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +12.6) | — |
| [[J82 (line)]] | alt | 4.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.3× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 3.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.1× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 3.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 2.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 6.10 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0641× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 1.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +10.5) | — |
| [[A549 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.535 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.739 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.469 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCDH17]] | +0.75 | +0.73 / +0.73 | both halves | 7e-06 | same gene group |
| [[RORB]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[EPHA7]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[PCDH9]] | +0.62 | +0.65 / +0.57 | both halves | 1e-05 | same gene group |
| [[TMPRSS15]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[KCNJ6]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RALYL]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PEG10]] | +0.59 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TMEFF2]] | +0.59 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[EPHA4]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CALCRL]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[B3GALT1]] | +0.58 | +0.64 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WIPF1]] | -0.46 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCDH10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FMN2]] | C | FMN2 activity raises PCDH10's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 3.82× lower at baseline in the lines without FMN2 | 0.054 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[ERBB4]] | C | ERBB4 activity raises PCDH10's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 3.28× lower at baseline in the lines without ERBB4 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[UCHL1]] | C | UCHL1 activity raises PCDH10's level | lines that do not express UCHL1 (29) vs lines expressing it (21) | 3.55× lower at baseline in the lines without UCHL1 | 0.074 | ⚠ within organs, on part of the lines; also absent: NEFL, ADD2, CDH4; co-absent with the target |
| [[PCDH17]] | C | PCDH17 activity raises PCDH10's level | lines that do not express PCDH17 (29) vs lines expressing it (21) | 3.96× lower at baseline in the lines without PCDH17 | 0.076 | ⚠ within organs, on part of the lines; also absent: WNK3, PCDH10, PTPRN; co-absent with the target |
| [[MAP1A]] | C | MAP1A activity raises PCDH10's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 2.61× lower at baseline in the lines without MAP1A | 0.082 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises PCDH10's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 3.31× lower at baseline in the lines without PCDH18 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A16]] | B | PCDH10 activity lowers SLC25A16's level | lines that do not express PCDH10 (24) vs lines expressing it (26) | 1.10× higher at baseline in the lines without PCDH10 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TWIST1, PRR16, FMN2 |
| [[UCHL1]] | C | PCDH10 activity raises UCHL1's level | lines that do not express PCDH10 (24) vs lines expressing it (26) | 5.87× lower at baseline in the lines without PCDH10 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TWIST1, PRR16, FMN2; co-absent with the target |
| [[FMN2]] | C | PCDH10 activity raises FMN2's level | lines that do not express PCDH10 (24) vs lines expressing it (26) | 3.84× lower at baseline in the lines without PCDH10 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TWIST1, PRR16, FMN2; co-absent with the target |
| [[MOXD1]] | C | PCDH10 activity raises MOXD1's level | lines that do not express PCDH10 (24) vs lines expressing it (26) | 3.58× lower at baseline in the lines without PCDH10 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TWIST1, PRR16, FMN2; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.1, 30.2); signed map (38.1, 31.0). **Vector** length 53.9, 12.3% of its response variance represented; |z| ≥ 3 in 605 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.8 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +23.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +10.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | +0.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.3 — chr4:133,149,294-133,208,606 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OL-PCDH, KIAA1400 |
| Gene groups (HGNC) | Non-clustered protocadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2E7](https://www.uniprot.org/uniprotkb/Q9P2E7) (Protocadherin-10):

> Potential calcium-dependent cell-adhesion protein.; (Microbial infection) Acts as a receptor for Western equine encephalitis virus.

**Summary**, from NCBI Gene [57575](https://www.ncbi.nlm.nih.gov/gene/57575):

> This gene belongs to the protocadherin gene family, a subfamily of the cadherin superfamily. This family member contains 6 extracellular cadherin domains, a transmembrane domain and a cytoplasmic tail differing from those of the classical cadherins. The encoded protein is a cadherin-related neuronal receptor thought to function in the establishment of specific cell-cell connections in the brain. This gene plays a role in inhibiting cancer cell motility and cell migration. Alternative splicing …

**Accessions** — [HGNC:13404](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13404) · Entrez [57575](https://www.ncbi.nlm.nih.gov/gene/57575) · UniProt [Q9P2E7](https://www.uniprot.org/uniprotkb/Q9P2E7) · Ensembl [ENSG00000138650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138650)

## Data

Gene col 6204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6204); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6204]; `tensor/DDL_lfc|DDL_z.npy` [6204]; `embed/gene_vectors.npy` [6204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6204 or target_col == 6204). Every well: [[PCDH10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDH10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
