---
symbol: "ARVCF"
type: "gene"
col: 1824
ensembl_id: "ENSG00000099889"
name: "ARVCF delta catenin family member"
location: "22q11.21"
module: 189
arm: "+"
pooled_cpm: 5.04
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# ARVCF

*ARVCF delta catenin family member* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.16× (z +10.5, q 6e-23, up in 24 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.308× (z -5.9, q 2e-06, down in 20 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0491×; ⚠ cell-cycle shift, explains ~22% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0379×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0540×); [[Cobimetinib (drug)]] 5 µM in 1 line (Hs 766T 0.0696×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM50A]] (+0.65, fdr 7e-06), [[DUSP8]] (+0.65, fdr 7e-06), [[DNAJB2]] (+0.64, fdr 7e-06); moves opposite to [[SDHD]] (-0.55, fdr 3e-05), [[NAF1]] (-0.53, fdr 3e-05), [[LAMB1]] (-0.51, fdr 3e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HID1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +10.5 | 6e-23 | 24/36 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +8.4 | 1e-14 | 30/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.28×** | +8.0 | 3e-13 | 27/44 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **2.18×** | +7.2 | 8e-11 | 24/39 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **2.01×** | +6.7 | 2e-09 | 25/45 (HT-29, COLO 205, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +6.5 | 1e-08 | 23/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.60×** | +6.4 | 1e-08 | 20/43 (HT-29, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.87×** | +6.0 | 1e-07 | 23/42 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.74×** | +5.2 | 1e-05 | 15/35 (HT-29, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +5.0 | 3e-05 | 13/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.68×** | +5.0 | 3e-05 | 18/43 (HT-29, COLO 205, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.68×** | +4.8 | 8e-05 | 20/41 (HT-29, COLO 205, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.94×** | +4.6 | 2e-04 | 14/32 (NCI-H23, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.59×** | +4.5 | 3e-04 | 19/41 (HT-29, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.4 | 5e-04 | 14/44 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 6e-04 | 13/35 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +3.5 | 0.016 | 12/42 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1824.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2030 0.0491×; ⚠ cell-cycle shift, explains ~22% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0379×); [[Ipatasertib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0540×); [[Cobimetinib (drug)]] 5 µM in 1 line (Hs 766T 0.0696×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.308×** | -5.9 | 2e-06 | 20/38 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.401×** | -4.6 | 0.001 | 18/31 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.673×** | -3.8 | 0.024 | 10/34 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.6 | 0.051 | 10/46 (HCT15, HS-578T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.727× | -3.1 | 0.22 | 11/45 (H4, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 17.9 | 2 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 4.30× (z +8.7) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[A498 (line)]] | wt | 2.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 5.13 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0696× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 3.60 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0379× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 4.36 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0491× (z -11.7) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H2347 (line)]] | alt | 3.00 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0540× (z -9.4) |
| [[A-172 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.725 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM50A]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[DUSP8]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[DNAJB2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[LZTS3]] | +0.64 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[GDPD5]] | +0.64 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[DLGAP4]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SLC12A4]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[PIK3CD]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.62 | +0.47 / +0.64 | both halves | 2e-05 | same gene group |
| [[LCAT]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[GLIPR2]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MEGF6]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHD]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[NAF1]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[LAMB1]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[XRCC5]] | -0.50 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[TMEM123]] | -0.49 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ECHDC1]] | -0.48 | -0.37 / -0.45 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HID1]] | B | HID1 activity raises ARVCF's level | lines that do not express HID1 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without HID1 | 0.089 | ⚠ within organs, on part of the lines; also absent: NRARP, HAP1, FAM169A; its own permutation p |
| [[TMEM40]] | B | TMEM40 activity raises ARVCF's level | lines that do not express TMEM40 (24) vs lines expressing it (26) | 1.36× lower at baseline in the lines without TMEM40 | 0.093 | ⚠ within organs, on part of the lines; also absent: LRG1, LRRN1, WNT7A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.0, -1.3); signed map (-4.1, 24.0). **Vector** length 76.2, 14.0% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +10.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +6.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.9 | +6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +4.4 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -5.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.4 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ARVCF delta catenin family member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,969,896-20,016,823 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Armadillo repeat containing; Armadillo like helical domain containing; p120 catenin family |
| Matched by | ensembl_id |

**Function**, from UniProt [O00192](https://www.uniprot.org/uniprotkb/O00192) (Splicing regulator ARVCF):

> Contributes to the regulation of alternative splicing of pre-mRNAs.

**Summary**, from NCBI Gene [421](https://www.ncbi.nlm.nih.gov/gene/421):

> Armadillo Repeat gene deleted in Velo-Cardio-Facial syndrome (ARVCF) is a member of the catenin family. This family plays an important role in the formation of adherens junction complexes, which are thought to facilitate communication between the inside and outside environments of a cell. The ARVCF gene was isolated in the search for the genetic defect responsible for the autosomal dominant Velo-Cardio-Facial syndrome (VCFS), a relatively common human disorder with phenotypic features including …

**Accessions** — [HGNC:728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:728) · Entrez [421](https://www.ncbi.nlm.nih.gov/gene/421) · UniProt [O00192](https://www.uniprot.org/uniprotkb/O00192) · Ensembl [ENSG00000099889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099889)

## Data

Gene col 1824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1824); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1824]; `tensor/DDL_lfc|DDL_z.npy` [1824]; `embed/gene_vectors.npy` [1824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1824 or target_col == 1824). Every well: [[ARVCF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARVCF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
