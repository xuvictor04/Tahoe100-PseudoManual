---
symbol: "BSCL2"
type: "gene"
col: 9576
ensembl_id: "ENSG00000168000"
name: "BSCL2 lipid droplet biogenesis associated, seipin"
location: "11q12.3"
module: 212
arm: "+"
pooled_cpm: 18.32
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# BSCL2

*BSCL2 lipid droplet biogenesis associated, seipin* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.16× (z +15.0, q 0e+00, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +13.7, q 5e-40, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.765× (z -5.2, q 9e-05, down in 22 of 47 measured lines) ⚠ cell-cycle shift, explains ~19% of this change. The strongest without an alert is [[Verteporfin (drug)]] 5 µM: 0.786× (z -4.4, q 0.002, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (H4 0.0575×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (HCT15 0.191×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.478×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM14-RBM4]] (+0.63, fdr 1e-05), [[SYS1-DBNDD2]] (+0.58, fdr 1e-05), [[RAB5C]] (+0.58, fdr 1e-05); moves opposite to [[WDR75]] (-0.53, fdr 3e-05), [[TMA16]] (-0.50, fdr 3e-05), [[MIOS]] (-0.50, fdr 3e-05).
> It is in [[Module 212]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9576.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.16×** | +15.0 | 0e+00 | 39/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +13.7 | 5e-40 | 37/47 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +13.6 | 5e-40 | 40/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.98×** | +13.3 | 4e-38 | 31/41 (NCI-H460, SW480, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +11.9 | 2e-30 | 38/47 (A-172, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.76×** | +11.0 | 3e-26 | 34/47 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.66×** | +9.3 | 1e-18 | 24/33 (SHP-77, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.63×** | +8.8 | 1e-16 | 24/37 (A-427, A549, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.47×** | +7.1 | 8e-11 | 23/43 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +6.6 | 2e-09 | 24/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.34×** | +5.7 | 6e-07 | 18/48 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.30×** | +4.8 | 7e-05 | 15/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 9e-05 | 17/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.28×** | +4.5 | 3e-04 | 17/46 (NCI-H23, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.26×** | +4.4 | 3e-04 | 15/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 5e-04 | 18/48 (A-427, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +3.8 | 0.005 | 10/48 (NCI-H460, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.005 | 13/45 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.012 | 8/46 (LS 180, SHP-77, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +3.4 | 0.017 | 5/48 (A-172, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.038 | 6/48 (KATO III, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9576.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.187×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Harringtonine (drug)]] 0.05 µM in 1 line (H4 0.0575×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (HCT15 0.191×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.478×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.765×** | -5.2 | 9e-05 | 22/47 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.786×** | -4.4 | 0.002 | 15/47 (A-427, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -3.6 | 0.050 | 14/48 (LOX-IMVI, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.3 | 0.16 | 14/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9576. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 26.0 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.22× (z +9.0) | — |
| [[SW480 (line)]] | alt | 21.9 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.62× (z +9.9) | — |
| [[A-427 (line)]] | wt | 32.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.478× (z -9.3) |
| [[A549 (line)]] | wt | 12.9 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.19× (z +9.7) | — |
| [[A-172 (line)]] | wt | 20.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.23× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 8.21 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.74× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 1 | — | [[Triamcinolone (drug)]] 5 µM 0.131× (z -8.5) |
| [[H4 (line)]] | wt | 18.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0575× (z -11.5) |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.191× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW1417 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.161× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9576), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM14-RBM4]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SYS1-DBNDD2]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RAB5C]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[DDB1]] | +0.57 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[ISY1-RAB43]] | +0.57 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PLOD3]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[ALKBH5]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ATP2A1]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[MBOAT7]] | +0.53 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[P3H1]] | +0.53 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[WDR37]] | +0.53 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[EPN1]] | +0.52 | +0.40 / +0.52 | both halves | 5e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR75]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[TMA16]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[MIOS]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZNF330]] | -0.50 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[CMTR2]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[CSF3]] | -0.50 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[TIGD2]] | -0.49 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[MRPL15]] | -0.48 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[DNAH14]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[SSB]] | -0.47 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[MRPS17]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[DDX52]] | -0.47 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.536). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.2, -29.5); signed map (-54.7, -11.0). **Vector** length 78.4, 14.4% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.3 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +3.9 | +13.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.3 | +8.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +4.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -4.8 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | BSCL2 lipid droplet biogenesis associated, seipin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,689,289-62,709,845 (-) |
| Ensembl biotype | protein_coding |
| Also known as | seipin; previously GNG3LG, SPG17 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G97](https://www.uniprot.org/uniprotkb/Q96G97) (Seipin):

> Mediates the formation of lipid droplets during the differentiation and maturation of adipocytes. Together with LDAF1, defines the sites of lipid droplet formation in the endoplasmic reticulum and promotes the aggregation of triacylglycerol molecules to form the core of a lipid droplet (nucleation) in the endoplasmic reticulum and drive budding of lipid droplets into the cytoplasm. BSCL2 and LDAF1 also regulate protein and lipid delivery from the endoplasmic reticulum into growing lipid …

**Summary**, from NCBI Gene [26580](https://www.ncbi.nlm.nih.gov/gene/26580):

> This gene encodes the multi-pass transmembrane protein seipin. This protein localizes to the endoplasmic reticulum and may be important for lipid droplet morphology. Mutations in this gene have been associated with congenital generalized lipodystrophy type 2 or Berardinelli-Seip syndrome, a rare autosomal recessive disease characterized by a near absence of adipose tissue and severe insulin resistance. Alternatively spliced transcript variants encoding different isoforms have been found for …

**Accessions** — [HGNC:15832](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15832) · Entrez [26580](https://www.ncbi.nlm.nih.gov/gene/26580) · UniProt [Q96G97](https://www.uniprot.org/uniprotkb/Q96G97) · Ensembl [ENSG00000168000](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168000)

## Data

Gene col 9576: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9576); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9576, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9576]; `tensor/DDL_lfc|DDL_z.npy` [9576]; `embed/gene_vectors.npy` [9576]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9576 or target_col == 9576). Every well: [[BSCL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BSCL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
