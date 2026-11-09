---
symbol: "WDR53"
type: "gene"
col: 11732
ensembl_id: "ENSG00000185798"
name: "WD repeat domain 53"
location: "3q29"
module: 119
arm: "+"
pooled_cpm: 10.58
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# WDR53

*WD repeat domain 53* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +13.2, q 5e-37, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.797× (z -5.0, q 3e-04, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (Panc 03.27 0.167×, Hs 766T 0.121×, HS-578T 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.153×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Isocorydine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0818×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.196×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SNU-1 0.0745×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTPBP10]] (+0.75, fdr 7e-06), [[ZNF16]] (+0.73, fdr 7e-06), [[DHRS7B]] (+0.70, fdr 7e-06); moves opposite to [[FAM171B]] (-0.54, fdr 2e-04), [[ABLIM1]] (-0.53, fdr 9e-05), [[SPTAN1]] (-0.52, fdr 7e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +13.2 | 5e-37 | 34/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.97×** | +10.4 | 6e-23 | 36/47 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +10.1 | 9e-22 | 32/37 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.77×** | +8.8 | 1e-16 | 29/47 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.67×** | +7.9 | 3e-13 | 27/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +7.3 | 3e-11 | 26/46 (HOP62, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +5.3 | 8e-06 | 17/47 (CFPAC-1, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.9 | 7e-05 | 14/44 (NCI-H1792, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.37×** | +4.9 | 7e-05 | 14/41 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.39×** | +4.9 | 7e-05 | 16/44 (PANC-1, H4, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.23×** | +4.5 | 3e-04 | 7/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +4.4 | 5e-04 | 17/43 (HOP62, HS-578T, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +4.3 | 8e-04 | 19/47 (LOX-IMVI, NCI-H2030, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.003 | 12/47 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.9 | 0.004 | 10/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.035 | 10/44 (CFPAC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.091 | 6/47 (NCI-H2030, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11732.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (Panc 03.27 0.167×, Hs 766T 0.121×, HS-578T 0.232×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.153×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Isocorydine (drug)]] 0.5 µM in 1 line (Hs 766T 0.0818×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.196×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SNU-1 0.0745×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -5.0 | 3e-04 | 17/48 (SW48, NCI-H2030, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -3.6 | 0.067 | 3/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.796×** | -3.6 | 0.067 | 14/46 (NCI-H2347, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.03 | 0 | 2 (1 ⚠) | — | [[Isocorydine (drug)]] 0.5 µM 0.0818× (z -10.5) |
| [[SW480 (line)]] | alt | 15.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 8.41 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.0885× (z -8.6) |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 7.27 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +9.0) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 11.1 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0745× (z -8.8) |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTPBP10]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ZNF16]] | +0.73 | +0.64 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[DHRS7B]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MRPS11]] | +0.66 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[MTG2]] | +0.65 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[PHF5A]] | +0.64 | +0.58 / +0.59 | both halves | 8e-06 | STRING 450 |
| [[TBP]] | +0.64 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 | STRING 510 |
| [[ZNF200]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ZNF251]] | +0.63 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[CWF19L1]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ZNF7]] | +0.63 | +0.60 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM171B]] | -0.54 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[ABLIM1]] | -0.53 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[SPTAN1]] | -0.52 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[GLS]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[MAPRE2]] | -0.52 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.8, 4.5); signed map (-10.5, -15.4). **Vector** length 61.9, 9.21% of its response variance represented; |z| ≥ 3 in 807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +10.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +5.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.6 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.9 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.5 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.4 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.4 | +0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 53 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:196,554,177-196,568,674 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC64882, MGC12928 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q7Z5U6](https://www.uniprot.org/uniprotkb/Q7Z5U6) carries no function annotation.

**Summary**, from NCBI Gene [348793](https://www.ncbi.nlm.nih.gov/gene/348793):

> This gene encodes a protein containing WD domains. The function of this gene is unknown. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28786) · Entrez [348793](https://www.ncbi.nlm.nih.gov/gene/348793) · UniProt [Q7Z5U6](https://www.uniprot.org/uniprotkb/Q7Z5U6) · Ensembl [ENSG00000185798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185798)

## Data

Gene col 11732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11732); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11732]; `tensor/DDL_lfc|DDL_z.npy` [11732]; `embed/gene_vectors.npy` [11732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11732 or target_col == 11732). Every well: [[WDR53 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR53.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
