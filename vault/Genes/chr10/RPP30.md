---
symbol: "RPP30"
type: "gene"
col: 7306
ensembl_id: "ENSG00000148688"
name: "ribonuclease P/MRP subunit p30"
location: "10q23.31"
module: 57
arm: "+"
pooled_cpm: 29.48
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# RPP30

*ribonuclease P/MRP subunit p30* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.72× (z +11.5, q 5e-28, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.607× (z -11.9, q 5e-30, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRS2]] (+0.71, fdr 7e-06), [[COPS7B]] (+0.71, fdr 7e-06), [[MRPS35]] (+0.70, fdr 7e-06); moves opposite to [[INTS6]] (-0.61, fdr 1e-05), [[PPIEL-1]] (-0.61, fdr 1e-05), [[ZNF335]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRIM72]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.72×** | +11.5 | 5e-28 | 45/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +9.1 | 2e-17 | 34/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.67×** | +8.6 | 1e-15 | 35/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +8.0 | 1e-13 | 30/48 (A-427, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +7.5 | 8e-12 | 38/48 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.2 | 5e-11 | 29/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +7.2 | 6e-11 | 30/47 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.9 | 3e-10 | 29/48 (A549, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +6.7 | 1e-09 | 38/48 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.4 | 1e-08 | 31/47 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 4e-08 | 28/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +5.8 | 3e-07 | 26/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.6 | 7e-07 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.5 | 3e-04 | 19/48 (SNU-423, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +4.3 | 6e-04 | 20/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +4.1 | 0.001 | 14/48 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.010 | 16/48 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.029 | 7/47 (C-33 A, AsPC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.034 | 21/48 (LS 180, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -11.9 | 5e-30 | 38/48 (HepG2/C3A, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.787×** | -3.9 | 0.026 | 22/48 (AN3 CA, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.805×** | -3.7 | 0.042 | 12/48 (LS 180, RPMI-7951, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.27 | 5/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.837× | -3.0 | 0.27 | 12/47 (RKO, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.4 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 26.9 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 34.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +14.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -9.6) |
| [[SW480 (line)]] | alt | 35.4 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.4) | — |
| [[A-427 (line)]] | wt | 24.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.98× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0625× (z -11.9) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 40.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -10.7) |
| [[SW 900 (line)]] | alt | 39.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -8.8) |
| [[A-172 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRS2]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[COPS7B]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[MRPS35]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[HBS1L]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[FBXO7]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[RFXAP]] | +0.67 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[TRIT1]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 | pathway: tRNA processing |
| [[NUDT21]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[NDUFAF5]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ZNF112]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[CYB5R4]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[DLD]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[PPIEL-1]] | -0.61 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[ZNF335]] | -0.60 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RIPK1]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | -0.58 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[C6orf62]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[DMPK]] | -0.56 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[RRP12]] | -0.56 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[TRIM72]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[BOLA1]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM72]] | C | TRIM72 activity lowers RPP30's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.32× higher at baseline in the lines without TRIM72 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.0, -12.1); signed map (-33.5, -18.2). **Vector** length 97.9, 23.9% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.4 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.4 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +4.5 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +8.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.2 | -11.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.1 | +0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.8 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease P/MRP subunit p30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:90,871,952-90,908,553 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSG15 |
| Gene groups (HGNC) | Nuclear RNase P complex subunits; RNase MRP complex subunits |
| Reactome | 6 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Major pathway of rRNA processing in the nucleolus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [P78346](https://www.uniprot.org/uniprotkb/P78346) (Ribonuclease P protein subunit p30):

> Component of ribonuclease P, a ribonucleoprotein complex that generates mature tRNA molecules by cleaving their 5'-ends. Also a component of the MRP ribonuclease complex, which cleaves pre-rRNA sequences.

**Summary**, from NCBI Gene [10556](https://www.ncbi.nlm.nih.gov/gene/10556):

> Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Part of multimeric ribonuclease P complex and ribonuclease MRP complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17688) · Entrez [10556](https://www.ncbi.nlm.nih.gov/gene/10556) · UniProt [P78346](https://www.uniprot.org/uniprotkb/P78346) · Ensembl [ENSG00000148688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148688)

## Data

Gene col 7306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7306); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7306]; `tensor/DDL_lfc|DDL_z.npy` [7306]; `embed/gene_vectors.npy` [7306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7306 or target_col == 7306). Every well: [[RPP30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPP30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
