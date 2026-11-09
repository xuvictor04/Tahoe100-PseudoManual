---
symbol: "DNAI3"
type: "gene"
col: 8553
ensembl_id: "ENSG00000162643"
name: "dynein axonemal intermediate chain 3"
location: "1p22.3"
module: 62
arm: "+"
pooled_cpm: 6.24
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# DNAI3

*dynein axonemal intermediate chain 3* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +20.2, q 0e+00, up in 40 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.837× (z -7.7, q 1e-11, down in 27 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.707× (z -4.4, q 0.003, down in 15 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H23 0.109×, J82 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.174×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change); [[5-Fluorouracil (drug)]] 5 µM in 1 line (AsPC-1 0.0458×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF423]] (+0.76, fdr 7e-06), [[PINCR]] (+0.71, fdr 1e-05), [[RPS27L]] (+0.71, fdr 7e-06); moves opposite to [[CS]] (-0.56, fdr 2e-05), [[FBXW2]] (-0.53, fdr 1e-04), [[FANCG]] (-0.52, fdr 5e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NTN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +20.2 | 0e+00 | 40/42 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.61×** | +12.1 | 2e-31 | 35/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +11.8 | 1e-29 | 32/40 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +11.0 | 3e-26 | 31/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +8.9 | 4e-17 | 29/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.4 | 1e-11 | 21/47 (A-172, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.6 | 3e-09 | 19/38 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.6 | 3e-09 | 20/43 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +6.6 | 4e-09 | 21/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.55×** | +5.3 | 6e-06 | 12/32 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.3 | 7e-06 | 17/47 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.1 | 1e-05 | 15/39 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +4.7 | 9e-05 | 15/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.03×** | +4.7 | 1e-04 | 9/45 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.28×** | +4.3 | 5e-04 | 17/47 (LOX-IMVI, A498, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.009 | 13/44 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.021 | 9/39 (A-172, C-33 A, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8553.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H23 0.109×, J82 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.174×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change); [[5-Fluorouracil (drug)]] 5 µM in 1 line (AsPC-1 0.0458×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.837× | -7.7 | 1e-11 | 27/48 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.707×** | -4.4 | 0.003 | 15/46 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.787× | -3.0 | 0.41 | 6/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.48 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 7.72 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.0× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 5.71 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 18.8× (z +13.4) | — |
| [[C32 (line)]] | wt | 15.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +12.2) | — |
| [[J82 (line)]] | alt | 4.84 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[LoVo (line)]] | wt | 13.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LOX-IMVI (line)]] | wt | 8.19 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +9.2) | [[Harringtonine (drug)]] 0.5 µM 0.136× (z -8.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A-172 (line)]] | wt | 7.73 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 4.99× (z +8.8) | — |
| [[A549 (line)]] | wt | 6.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 2.21 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 5 µM 0.0458× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 7.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 7.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +9.8) | — |
| [[SW480 (line)]] | alt | 6.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF423]] | +0.76 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[PINCR]] | +0.71 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[RPS27L]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[SPATA18]] | +0.70 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PURPL]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[INKA2]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ARL14EP-DT]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[TYMSOS]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ACTA2]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[INSYN2A]] | +0.66 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[USH2A]] | +0.65 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.65 | +0.47 / +0.68 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CS]] | -0.56 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[FBXW2]] | -0.53 | -0.64 / -0.34 | both halves | 1e-04 | same gene group |
| [[FANCG]] | -0.52 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[ICMT]] | -0.51 | -0.37 / -0.44 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN1]] | B | NTN1 activity raises DNAI3's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 1.52× lower at baseline in the lines without NTN1 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DNAI3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FDXR]] | B | FDXR activity raises DNAI3's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without FDXR | 0.081 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[PINCR]] | B | PINCR activity strengthens DNAI3's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.82× as strongly (z diff +0.48); strongest at Doxorubicin (hydrochloride) 5 µM: 1.62x vs 3.09x (z diff +2.6) | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[TP53]] | B | TP53 activity strengthens DNAI3's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.82× as strongly (z diff +0.53); strongest at Doxorubicin (hydrochloride) 5 µM: 1.59x vs 3.54x (z diff +3.1) | 0.098 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.0, 36.8); signed map (43.2, -23.3). **Vector** length 61.0, 8.94% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.54 to 26); *apoptosis* (hallmark, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +20.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.4 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -7.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -4.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.3 | +8.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -1.6 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal intermediate chain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:84,999,147-85,133,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIC3, FLJ30067, NYD-SP29; previously WDR63 |
| Gene groups (HGNC) | WD repeat domain containing; Dyneins, axonemal inner arm I1/f complex subunits; Dynein intermediate chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWG1](https://www.uniprot.org/uniprotkb/Q8IWG1) (Dynein axonemal intermediate chain 3):

> Acts as a negative regulator of cell migration, invasion, and metastasis downstream of p53/TP53, through inhibition of Arp2/3 complex-mediated actin polymerization. Via its association with the multisubunit axonemal dynein complex, is potentially involved in the regulation of cilia function (By similarity). May play a role in osteogenesis of dental tissue-derived mesenchymal stem cells (By similarity).

**Summary**, from NCBI Gene [126820](https://www.ncbi.nlm.nih.gov/gene/126820):

> Enables Arp2/3 complex binding activity. Involved in negative regulation of Arp2/3 complex-mediated actin nucleation and negative regulation of cell migration. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30711) · Entrez [126820](https://www.ncbi.nlm.nih.gov/gene/126820) · UniProt [Q8IWG1](https://www.uniprot.org/uniprotkb/Q8IWG1) · Ensembl [ENSG00000162643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162643)

## Data

Gene col 8553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8553); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8553]; `tensor/DDL_lfc|DDL_z.npy` [8553]; `embed/gene_vectors.npy` [8553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8553 or target_col == 8553). Every well: [[DNAI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
