---
symbol: "ZNF876P"
type: "gene"
col: 12540
ensembl_id: "ENSG00000198155"
name: "zinc finger protein 876, pseudogene"
location: "4p16.3"
module: 71
arm: "+"
pooled_cpm: 3.59
n_lines_expressing: 33
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# ZNF876P

*zinc finger protein 876, pseudogene* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.13× (z +10.5, q 3e-23, up in 17 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.477× (z -7.0, q 1e-09, down in 16 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF718]] (+0.81, fdr 7e-06, ⚠ same locus), [[ZRANB3]] (+0.75, fdr 7e-06), [[XNDC1N-ZNF705EP-ALG1L9P]] (+0.72, fdr 7e-06), [[HELLPAR]] (+0.66, fdr 7e-06); moves opposite to [[ALAD]] (-0.60, fdr 5e-05), [[PIGH]] (-0.59, fdr 2e-04), [[KDM1B]] (-0.58, fdr 2e-04).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[MTMR10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +10.5 | 3e-23 | 17/22 (A498, J82, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.46×** | +8.6 | 3e-15 | 16/21 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +7.8 | 1e-12 | 1/5 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +6.8 | 2e-09 | 15/23 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.0 | 2e-07 | 11/30 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.85×** | +5.7 | 1e-06 | 10/26 (SW480, J82, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +5.5 | 3e-06 | 1/8 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.55×** | +4.3 | 0.001 | 4/18 (HCT15, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.005 | 4/30 (BT-474, LS 180, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.005 | 11/27 (RKO, SW480, …) | top dose only |  |
| [[Finasteride (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.088 | 2/29 (SW480, A498) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.096 | 0/26 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.477×** | -7.0 | 1e-09 | 16/28 (PANC-1, SNU-1, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.624×** | -4.6 | 9e-04 | 11/22 (COLO 205, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -4.4 | 0.002 | 14/30 (HEC-1-A, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.746×** | -4.1 | 0.006 | 14/27 (HEC-1-A, COLO 205, …) | two highest doses | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -3.5 | 0.060 | 8/30 (HEC-1-A, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | **0.717×** | -3.3 | 0.095 | 4/30 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.792×** | -3.2 | 0.095 | 5/30 (SNU-1, SW48, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **0.795×** | -3.2 | 0.097 | 5/30 (Hs 766T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.734× | -3.0 | 0.15 | 11/30 (SW480, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 9.25 | 0 | 2 (1 ⚠) | — | [[Ponatinib (drug)]] 0.5 µM 0.0540× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 17.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0725× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0505× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 7.21 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 9.08 | 0 | 1 | — | [[Pasireotide (acetate) (drug)]] 0.5 µM 0.0487× (z -10.0) |
| [[A-172 (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.387 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF718]] | +0.81 | +0.75 / +0.75 | both halves | 7e-06 | ⚠ same locus (16.3 kb, same strand: neighbours can correlate without regulation) |
| [[ZRANB3]] | +0.75 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[HELLPAR]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[EPM2A]] | +0.66 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[MSANTD2]] | +0.65 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[XNDC1N]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SNRPB]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[GBX2-AS1]] | +0.64 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[E2F3]] | +0.63 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[LAMTOR5-AS1]] | +0.63 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[KANSL1L-AS1]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DNAAF10]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALAD]] | -0.60 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[PIGH]] | -0.59 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[KDM1B]] | -0.58 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[STAM2]] | -0.58 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[SKIC3]] | -0.58 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[IFT52]] | -0.57 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[FAM229B]] | -0.57 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[RING1]] | -0.57 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[ARNT]] | -0.56 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[PRKAB2]] | -0.56 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[PLD2]] | -0.56 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[STX7]] | -0.55 | -0.45 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF876P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF718]] | C | ZNF718 activity raises ZNF876P's level | lines that do not express ZNF718 (13) vs lines expressing it (37) | 3.12× lower at baseline in the lines without ZNF718 | 0.003 | ⚠ within organs, on part of the lines; also absent: ZNF876P, GALNT12, CDCP1; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTMR10]] | B | ZNF876P activity lowers MTMR10's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.35× higher at baseline in the lines without ZNF876P | 0.014 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[MGME1]] | B | ZNF876P activity raises MGME1's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without ZNF876P | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[SNRPB]] | B | ZNF876P activity raises SNRPB's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without ZNF876P | 0.064 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[WDR33]] | B | ZNF876P activity raises WDR33's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.19× lower at baseline in the lines without ZNF876P | 0.066 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[LINC01341]] | B | ZNF876P activity raises LINC01341's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without ZNF876P | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[RFC3]] | B | ZNF876P activity raises RFC3's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without ZNF876P | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8 |
| [[ZNF718]] | C | ZNF876P activity raises ZNF718's level | lines that do not express ZNF876P (17) vs lines expressing it (33) | 6.89× lower at baseline in the lines without ZNF876P | 1e-05 | ⚠ within organs, on part of the lines; also absent: ZNF718, PAX8; co-absent with the target |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.5, -44.0); signed map (27.0, -30.8). **Vector** length 48.2, 8.29% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +5.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.0 | +1.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.7 | -4.4 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -2.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -0.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 876, pseudogene |
| Locus type | pseudogene |
| Location | 4p16.3 — chr4:218,650-254,841 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49A33](https://www.uniprot.org/uniprotkb/Q49A33) (Putative zinc finger protein 876):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [642280](https://www.ncbi.nlm.nih.gov/gene/642280):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32472) · Entrez [642280](https://www.ncbi.nlm.nih.gov/gene/642280) · UniProt [Q49A33](https://www.uniprot.org/uniprotkb/Q49A33) · Ensembl [ENSG00000198155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198155)

## Data

Gene col 12540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12540); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12540]; `tensor/DDL_lfc|DDL_z.npy` [12540]; `embed/gene_vectors.npy` [12540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12540 or target_col == 12540). Every well: [[ZNF876P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF876P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
