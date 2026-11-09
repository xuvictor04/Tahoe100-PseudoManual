---
symbol: "NME6"
type: "gene"
col: 10211
ensembl_id: "ENSG00000172113"
name: "NME/NM23 nucleoside diphosphate kinase 6"
location: "3p21.31"
module: 11
arm: "+"
pooled_cpm: 13.97
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NME6

*NME/NM23 nucleoside diphosphate kinase 6* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.54× (z +5.9, q 2e-06, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.398× (z -12.5, q 3e-33, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL14EP]] (+0.80, fdr 7e-06), [[ERCC4]] (+0.80, fdr 7e-06), [[RPP38]] (+0.77, fdr 7e-06); moves opposite to [[NPTN]] (-0.64, fdr 1e-05), [[ITM2C]] (-0.63, fdr 1e-05), [[GM2A]] (-0.62, fdr 5e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10211.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +5.9 | 2e-06 | 24/47 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 1e-04 | 22/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.007 | 13/45 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.34×** | +4.0 | 0.007 | 15/42 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.51×** | +4.0 | 0.007 | 17/44 (SK-MEL-2, HCT15, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.9 | 0.007 | 19/41 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.047 | 17/48 (PANC-1, LS 180, …) | all doses, flat |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.068 | 10/44 (SNU-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.17× | +3.0 | 0.16 | 16/47 (MIA PaCa-2, RPMI-7951, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10211.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.398×** | -12.5 | 3e-33 | 41/47 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.458×** | -10.6 | 5e-24 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.458×** | -10.6 | 5e-24 | 41/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.490×** | -9.7 | 4e-20 | 32/46 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.494×** | -9.6 | 1e-19 | 43/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -7.6 | 3e-12 | 31/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -7.5 | 4e-12 | 33/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.624×** | -6.4 | 1e-08 | 29/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.562×** | -4.1 | 0.002 | 10/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.563×** | -4.1 | 0.002 | 20/44 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.746×** | -4.0 | 0.004 | 16/47 (J82, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -3.9 | 0.004 | 18/41 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.580×** | -3.9 | 0.005 | 8/44 (Hs 766T, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -3.7 | 0.008 | 15/47 (RPMI-7951, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.770×** | -3.6 | 0.014 | 19/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -3.6 | 0.014 | 14/48 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.782×** | -3.4 | 0.024 | 15/46 (Panc 03.27, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10211. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.6 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.289× (z -10.3) |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.222× (z -9.2) |
| [[C-33 A (line)]] | alt | 14.3 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.109× (z -9.7) |
| [[LoVo (line)]] | wt | 15.7 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.234× (z -10.4) |
| [[PANC-1 (line)]] | alt | 14.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.305× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -11.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.88 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.148× (z -9.6) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 1 | — | [[SBI-0640756 (drug)]] 5 µM 0.0617× (z -8.6) |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -8.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SNU-423 (line)]] | alt | 13.6 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0597× (z -13.5) |
| [[A-172 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10211), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL14EP]] | +0.80 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.80 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[RPP38]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.76 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.76 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ZNF181]] | +0.75 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[NAIF1]] | +0.74 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[INTS14]] | +0.71 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[MRPL38]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[PHAX]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.70 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.70 | +0.80 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTN]] | -0.64 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[ITM2C]] | -0.63 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[GM2A]] | -0.62 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[BRK1]] | -0.62 | -0.68 / -0.36 | both halves | 1e-04 |  |
| [[HDAC3]] | -0.61 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[COL18A1]] | -0.61 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[HERC3]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises NME6's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.35× lower at baseline in the lines without PODXL2 | 0.003 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.821). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.3, 6.6); signed map (1.6, -21.1). **Vector** length 80.5, 15.6% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.6 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +6.0 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.8 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | -0.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +0.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -9.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -6.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.3 | -10.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -12.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | NME/NM23 nucleoside diphosphate kinase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,290,722-48,301,685 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NM23-H6, IPIA-ALPHA |
| Gene groups (HGNC) | NME/NM23 family |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [O75414](https://www.uniprot.org/uniprotkb/O75414) (Nucleoside diphosphate kinase 6, mitochondrial):

> Catalytic subunit of a complex with RCC1L, which catalyzes the transfer of a gamma-phosphoryl group from a nucleoside triphosphate, mainly ATP, to a nucleoside diphosphate via a ping-pong mechanism involving the formation of a phosphohistidine intermediate. Participates in the regulation of mitochondrial nucleotide levels, mitoribosome biogenesis, and mitochondrial RNA abundances. Supplies pyrimidine ribonucleoside triphosphates (rNTPs) for mitochondrial transcription and is required for the …

**Summary**, from NCBI Gene [10201](https://www.ncbi.nlm.nih.gov/gene/10201):

> Nucleoside diphosphate (NDP) kinases (EC 2.7.4.6), such as NME6, are ubiquitous enzymes that catalyze transfer of gamma-phosphates, via a phosphohistidine intermediate, between nucleoside and dioxynucleoside tri- and diphosphates (Mehus et al., 1999 [PubMed 10453732]).[supplied by OMIM, Jul 2010]

**Accessions** — [HGNC:20567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20567) · Entrez [10201](https://www.ncbi.nlm.nih.gov/gene/10201) · UniProt [O75414](https://www.uniprot.org/uniprotkb/O75414) · Ensembl [ENSG00000172113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172113)

## Data

Gene col 10211: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10211); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10211, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10211]; `tensor/DDL_lfc|DDL_z.npy` [10211]; `embed/gene_vectors.npy` [10211]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10211 or target_col == 10211). Every well: [[NME6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NME6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
