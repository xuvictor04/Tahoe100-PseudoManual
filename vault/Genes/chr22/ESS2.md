---
symbol: "ESS2"
type: "gene"
col: 1854
ensembl_id: "ENSG00000100056"
name: "ess-2 spliceosome associated protein"
location: "22q11.21"
module: 107
arm: "+"
pooled_cpm: 7.3
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# ESS2

*ess-2 spliceosome associated protein* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.07× (z +20.0, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.728× (z -4.5, q 0.003, down in 20 of 33 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HS-578T 0.118×, Panc 03.27 0.132×, J82 0.0923×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.0636×, HS-578T 0.0990×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.135×; ⚠ toxic; cell-cycle shift, explains ~27% of this change); [[Clotrimazole (drug)]] 0.5 µM in 1 line (Hs 766T 0.0832×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0523×); [[Menadione (drug)]] 5 µM in 1 line (C-33 A 0.0797×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL55]] (+0.71, fdr 1e-05), [[LCMT1]] (+0.69, fdr 1e-05), [[PRPF6]] (+0.69, fdr 1e-05); moves opposite to [[LSMEM1]] (-0.59, fdr 9e-05), [[CLOCK]] (-0.59, fdr 4e-05), [[STK26]] (-0.58, fdr 4e-05).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.07×** | +20.0 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.60×** | +18.3 | 0e+00 | 46/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.69×** | +14.1 | 4e-43 | 45/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.68×** | +13.0 | 3e-36 | 41/47 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +7.6 | 2e-12 | 22/40 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.4 | 1e-08 | 4/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +6.1 | 7e-08 | 22/43 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +6.1 | 7e-08 | 14/46 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +5.3 | 8e-06 | 15/45 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.2 | 0.001 | 9/46 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.36×** | +4.2 | 0.001 | 9/37 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.004 | 14/42 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.004 | 6/46 (HOP62, SW480, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.20× | +3.7 | 0.010 | 5/47 (PANC-1, Panc 03.27, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.013 | 8/45 (RKO, CFPAC-1, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.016 | 8/43 (A498, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.077 | 9/46 (HEC-1-A, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1854.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HS-578T 0.118×, Panc 03.27 0.132×, J82 0.0923×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.0636×, HS-578T 0.0990×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.135×; ⚠ toxic; cell-cycle shift, explains ~27% of this change); [[Clotrimazole (drug)]] 0.5 µM in 1 line (Hs 766T 0.0832×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0523×); [[Menadione (drug)]] 5 µM in 1 line (C-33 A 0.0797×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.728×** | -4.5 | 0.003 | 20/33 (HS-578T, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.808× | -3.0 | 0.50 | 3/47 (hTERT-HPNE, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 9.31 | 0 | 3 | — | [[Menadione (drug)]] 5 µM 0.0797× (z -9.8) |
| [[SW480 (line)]] | alt | 7.21 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.95× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 13.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0990× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.42 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.109× (z -9.4) ⚠ toxic |
| [[A498 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0636× (z -16.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 8.21 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0974× (z -9.2) |
| [[Hs 766T (line)]] | wt | 7.35 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0832× (z -10.1) |
| [[J82 (line)]] | alt | 5.52 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0923× (z -10.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 5.85 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.72× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 7.03 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.49× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.26 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.38× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 6.46 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.107× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -11.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 5.92 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0523× (z -9.9) |
| [[SW1417 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.135× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL55]] | +0.71 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.69 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PRPF6]] | +0.69 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[WRAP73]] | +0.69 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RNF41]] | +0.68 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.68 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[HDGFL2]] | +0.68 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TFIP11]] | +0.68 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[HARS2]] | +0.67 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D13]] | +0.66 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.66 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[FHIP1B]] | +0.65 | +0.53 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSMEM1]] | -0.59 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[CLOCK]] | -0.59 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[STK26]] | -0.58 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[LACTB2]] | -0.58 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[SNX5]] | -0.58 | -0.47 / -0.26 | both halves | 4e-04 |  |
| [[GABPB1-AS1]] | -0.57 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[RXYLT1]] | -0.57 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[PSMD6-AS1]] | -0.56 | -0.38 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.0, -5.7); signed map (-34.9, 1.0). **Vector** length 67.8, 10.5% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +18.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.5 | +20.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +13.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +7.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +14.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +0.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | +0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | +0.0 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ess-2 spliceosome associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,130,279-19,144,684 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DGSI, Es2el, ES2, DGS-H, ESS-2, bis1; previously DGCR13, DGCR14 |
| Gene groups (HGNC) | Spliceosomal P complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DF8](https://www.uniprot.org/uniprotkb/Q96DF8) (Splicing factor ESS-2 homolog):

> May be involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [8220](https://www.ncbi.nlm.nih.gov/gene/8220):

> This gene is located within the minimal DGS critical region (MDGCR) thought to contain the gene(s) responsible for a group of developmental disorders. These disorders include DiGeorge syndrome, velocardiofacial syndrome, conotruncal anomaly face syndrome, and some familial or sporadic conotruncal cardiac defects which have been associated with microdeletion of 22q11.2. The encoded protein may be a component of C complex spliceosomes, and the orthologous protein in the mouse localizes to the …

**Accessions** — [HGNC:16817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16817) · Entrez [8220](https://www.ncbi.nlm.nih.gov/gene/8220) · UniProt [Q96DF8](https://www.uniprot.org/uniprotkb/Q96DF8) · Ensembl [ENSG00000100056](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100056)

## Data

Gene col 1854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1854); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1854]; `tensor/DDL_lfc|DDL_z.npy` [1854]; `embed/gene_vectors.npy` [1854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1854 or target_col == 1854). Every well: [[ESS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
