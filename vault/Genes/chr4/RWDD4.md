---
symbol: "RWDD4"
type: "gene"
col: 11300
ensembl_id: "ENSG00000182552"
name: "RWD domain containing 4"
location: "4q35.1"
module: 175
arm: "+"
pooled_cpm: 7.68
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# RWDD4

*RWD domain containing 4* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.55× (z +12.4, q 1e-32, up in 12 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.42× (z +6.9, q 8e-10, up in 22 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pentamidine (isethionate) (drug)]] 0.05 µM in 1 line (SHP-77 0.0646×); [[Bortezomib (drug)]] 5 µM in 1 line (NCI-H460 0.0773×; ⚠ toxic; cell-cycle shift, explains ~14% of this change); [[Sulfisoxazole (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0625×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C-33 A 0.108×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GK5]] (+0.61, fdr 8e-06), [[CIZ1]] (+0.61, fdr 2e-05), [[MRS2]] (+0.60, fdr 1e-05); moves opposite to [[ADNP2]] (-0.61, fdr 1e-05), [[ZSWIM6]] (-0.60, fdr 1e-05), [[CSNK1A1]] (-0.52, fdr 3e-05).
> It is in [[Module 175]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +12.4 | 1e-32 | 12/14 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +9.2 | 2e-17 | 21/33 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +7.3 | 5e-11 | 22/36 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +6.9 | 8e-10 | 22/43 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.7 | 1e-06 | 17/48 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +5.5 | 4e-06 | 20/43 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 6e-05 | 15/41 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.43×** | +4.6 | 3e-04 | 11/23 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.38×** | +4.4 | 7e-04 | 15/47 (C32, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.33×** | +4.0 | 0.004 | 9/47 (LS 180, A498, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.006 | 10/46 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.6 | 0.015 | 1/18 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.30×** | +3.6 | 0.015 | 13/43 (NCI-H1792, LoVo, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.31×** | +3.5 | 0.016 | 7/43 (A-427, HS-578T, …) | top dose only |  |
| [[Asciminib (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.022 | 3/47 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.022 | 9/43 (Panc 03.27, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.048 | 10/44 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.079 | 3/47 (AN3 CA, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.085 | 7/46 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.085 | 6/42 (A498, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11300.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pentamidine (isethionate) (drug)]] 0.05 µM in 1 line (SHP-77 0.0646×); [[Bortezomib (drug)]] 5 µM in 1 line (NCI-H460 0.0773×; ⚠ toxic; cell-cycle shift, explains ~14% of this change); [[Sulfisoxazole (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0625×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (C-33 A 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Saquinavir (drug)]] 5 µM |  | 0.851× | -3.2 | 0.31 | 6/43 (NCI-H1573, KATO III, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.797× | -3.2 | 0.31 | 10/46 (SNU-423, C32, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.797× | -3.1 | 0.31 | 4/48 (SK-MEL-2, HOP62, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.803× | -3.1 | 0.32 | 9/47 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 9.65 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.108× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 6.89 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0625× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0773× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~14% of this change |
| [[SHP-77 (line)]] | alt | 6.08 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 0.05 µM 0.0646× (z -10.0) |
| [[A-172 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GK5]] | +0.61 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[CIZ1]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[MRS2]] | +0.60 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[PMS2P1]] | +0.60 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ABCB10]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CTC1]] | +0.59 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[ATPAF1]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[DDHD2]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TIGD1]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[NDFIP1]] | +0.57 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TMEM237]] | +0.57 | +0.42 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADNP2]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.60 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[CSNK1A1]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[HES1]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TUBB4B]] | -0.51 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[YWHAB]] | -0.51 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[IER5]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SPEN]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MIDN]] | -0.50 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[SON]] | -0.49 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[CCDC144CP]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[UCKL1-AS1]] | -0.48 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.8, -14.0); signed map (-35.8, -22.1). **Vector** length 53.6, 6.93% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +12.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.1 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +2.6 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | +0.9 | +0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -1.5 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | +0.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[Thymol (drug)]] 5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | RWD domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:183,639,635-183,659,203 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10198; previously FAM28A, RWDD4A |
| Gene groups (HGNC) | RWD domain containing |
| Matched by | ensembl_id |

UniProt [Q6NW29](https://www.uniprot.org/uniprotkb/Q6NW29) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23750) · Entrez [201965](https://www.ncbi.nlm.nih.gov/gene/201965) · UniProt [Q6NW29](https://www.uniprot.org/uniprotkb/Q6NW29) · Ensembl [ENSG00000182552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182552)

## Data

Gene col 11300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11300); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11300]; `tensor/DDL_lfc|DDL_z.npy` [11300]; `embed/gene_vectors.npy` [11300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11300 or target_col == 11300). Every well: [[RWDD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RWDD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
