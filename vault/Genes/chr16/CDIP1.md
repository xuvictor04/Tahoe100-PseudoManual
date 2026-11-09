---
symbol: "CDIP1"
type: "gene"
col: 1589
ensembl_id: "ENSG00000089486"
name: "cell death inducing p53 target 1"
location: "16p13.3"
module: 62
arm: "+"
pooled_cpm: 7.45
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# CDIP1

*cell death inducing p53 target 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.74× (z +19.8, q 0e+00, up in 25 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HOP62 0.151×; ⚠ toxic); [[Vilanterol (drug)]] 0.5 µM in 1 line (LS 180 0.0750×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACHE]] (+0.66, fdr 7e-06), [[BTG2]] (+0.63, fdr 7e-06), [[NTN1]] (+0.60, fdr 1e-05); moves opposite to [[DROSHA]] (-0.55, fdr 2e-05), [[HAUS6]] (-0.54, fdr 1e-05), [[PRKDC]] (-0.52, fdr 4e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.74×** | +19.8 | 0e+00 | 25/32 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.13×** | +10.4 | 4e-23 | 21/33 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +9.7 | 4e-20 | 23/34 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.6 | 1e-15 | 19/32 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +8.2 | 2e-14 | 20/31 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +8.0 | 1e-13 | 21/30 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +7.4 | 1e-11 | 15/27 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.3 | 2e-08 | 14/23 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +6.2 | 4e-08 | 16/33 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.1 | 7e-08 | 11/34 (A498, CFPAC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.50×** | +5.6 | 9e-07 | 15/33 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.9 | 4e-05 | 11/34 (A498, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.7 | 1e-04 | 13/32 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 4e-04 | 8/32 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.3 | 7e-04 | 12/34 (NCI-H460, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 0.001 | 7/34 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1589.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HOP62 0.151×; ⚠ toxic); [[Vilanterol (drug)]] 0.5 µM in 1 line (LS 180 0.0750×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.766× | -3.6 | 0.20 | 10/24 (HOP62, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 40.8 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +15.7) | — |
| [[NCI-H460 (line)]] | wt | 5.19 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +20.8) | — |
| [[AsPC-1 (line)]] | alt | 8.08 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.83 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +12.1) | — |
| [[A549 (line)]] | wt | 4.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.89× (z +9.6) | — |
| [[HepG2_C3A (line)]] | wt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 5.89 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -9.0) ⚠ toxic |
| [[J82 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.55× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 3.74 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0750× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +10.7) | — |
| [[A-172 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.987 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACHE]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[BTG2]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[NTN1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CDKN1A]] | +0.59 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[CES2]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[KCTD11]] | +0.57 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[DNAI3]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[APBA3]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[PINCR]] | +0.55 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[NBEAP1]] | +0.55 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[FLCN]] | +0.54 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[ZFYVE1]] | +0.54 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DROSHA]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[HAUS6]] | -0.54 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[NCAPD3]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[HERC2]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SKP2]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TUBGCP3]] | -0.51 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[NUP93]] | -0.50 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[STIMATE]] | -0.50 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[GMPS]] | -0.50 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[FAR1]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[UGGT1]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDIP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[S100A3]] | B | S100A3 activity lowers CDIP1's level | lines that do not express S100A3 (15) vs lines expressing it (35) | 1.43× higher at baseline in the lines without S100A3 | 0.021 | ⚠ within organs, on part of the lines; also absent: S100A4; maybe low, not absent |
| [[NBEAP1]] | B | NBEAP1 activity lowers CDIP1's level | lines that do not express NBEAP1 (27) vs lines expressing it (23) | 1.04× higher at baseline in the lines without NBEAP1 | 0.046 | ⚠ within organs, on part of the lines; also absent: EYA2, VAV3, GRAMD1B |
| [[GLS2]] | B | GLS2 activity raises CDIP1's level | lines that do not express GLS2 (14) vs lines expressing it (36) | 1.08× lower at baseline in the lines without GLS2 | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.3, 38.4); signed map (43.9, -21.9). **Vector** length 56.6, 9.79% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +19.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.4 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.3 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.1 | +8.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +4.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.2 | +6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cell death inducing p53 target 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,510,669-4,538,828 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDIP, LITAFL; previously C16orf5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H305](https://www.uniprot.org/uniprotkb/Q9H305) (Cell death-inducing p53-target protein 1):

> Acts as an important p53/TP53-apoptotic effector. Regulates TNF-mediated apoptosis in a p53/TP53-dependent manner.

**Summary**, from NCBI Gene [29965](https://www.ncbi.nlm.nih.gov/gene/29965):

> Predicted to enable zinc ion binding activity. Acts upstream of or within intrinsic apoptotic signaling pathway in response to DNA damage by p53 class mediator. Located in bounding membrane of organelle; centrosome; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13234) · Entrez [29965](https://www.ncbi.nlm.nih.gov/gene/29965) · UniProt [Q9H305](https://www.uniprot.org/uniprotkb/Q9H305) · Ensembl [ENSG00000089486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089486)

## Data

Gene col 1589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1589); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1589]; `tensor/DDL_lfc|DDL_z.npy` [1589]; `embed/gene_vectors.npy` [1589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1589 or target_col == 1589). Every well: [[CDIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
