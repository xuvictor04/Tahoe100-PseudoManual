---
symbol: "R3HCC1"
type: "gene"
col: 2481
ensembl_id: "ENSG00000104679"
name: "R3H domain and coiled-coil containing 1"
location: "8p21.3"
module: 12
arm: "+"
pooled_cpm: 9.25
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# R3HCC1

*R3H domain and coiled-coil containing 1* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +11.2, q 3e-26, up in 31 of 46 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.04× (z +9.0, q 6e-17, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.700× (z -4.3, q 0.007, down in 22 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW 900 0.136×, RPMI-7951 0.153×); [[Simotinib (drug)]] 5 µM in 1 line (NCI-H2347 0.0321×; ⚠ toxic); [[XRK3F2 (drug)]] 0.5 µM in 1 line (KATO III 0.0572×); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0919×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED19]] (+0.71, fdr 7e-06), [[LENG1]] (+0.70, fdr 7e-06), [[ELOF1]] (+0.66, fdr 7e-06); moves opposite to [[STT3B]] (-0.65, fdr 1e-05), [[FKBP9]] (-0.63, fdr 1e-05), [[RBBP4]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.90×** | +11.2 | 3e-26 | 31/46 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.04×** | +9.0 | 6e-17 | 40/48 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.9 | 2e-16 | 28/43 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +8.1 | 1e-13 | 30/42 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +7.9 | 3e-13 | 37/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +7.4 | 2e-11 | 35/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +7.3 | 2e-11 | 32/46 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.80×** | +7.2 | 6e-11 | 28/46 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +6.4 | 1e-08 | 25/47 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +6.3 | 2e-08 | 23/38 (SHP-77, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.46×** | +4.8 | 7e-05 | 16/42 (HCT15, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.6 | 2e-04 | 17/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +4.5 | 4e-04 | 16/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.31×** | +3.4 | 0.024 | 12/45 (LS 180, AN3 CA, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.045 | 8/44 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.058 | 7/47 (SW480, CFPAC-1, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.087 | 10/43 (LoVo, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2481.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW 900 0.136×, RPMI-7951 0.153×); [[Simotinib (drug)]] 5 µM in 1 line (NCI-H2347 0.0321×; ⚠ toxic); [[XRK3F2 (drug)]] 0.5 µM in 1 line (KATO III 0.0572×); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0919×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -4.3 | 0.007 | 22/45 (SW 900, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.716×** | -4.2 | 0.007 | 8/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.751×** | -3.6 | 0.055 | 8/48 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.741×** | -3.5 | 0.055 | 11/28 (HCT15, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.759×** | -3.5 | 0.055 | 15/47 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.839× | -3.0 | 0.23 | 13/48 (KATO III, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 14.9 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.96× (z +8.9) | — |
| [[SW480 (line)]] | alt | 9.97 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.26× (z +14.9) | — |
| [[LoVo (line)]] | wt | 8.63 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.39× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 6.24 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 11.1× (z +9.5) | [[Hydroxyurea (drug)]] 0.5 µM 0.110× (z -8.6) |
| [[A498 (line)]] | wt | 9.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +10.3) | — |
| [[A549 (line)]] | wt | 13.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0919× (z -9.5) |
| [[KATO III (line)]] | alt | 12.0 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0572× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 8.98 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +9.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0321× (z -24.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 7.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +9.9) | — |
| [[RKO (line)]] | wt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -8.5) |
| [[SW 900 (line)]] | alt | 9.19 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -8.6) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED19]] | +0.71 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[LENG1]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ELOF1]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[NSMCE3]] | +0.64 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[RNF113A]] | +0.64 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.64 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[CCDC127]] | +0.63 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | +0.63 | +0.55 / +0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC9A3R2]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PHAX]] | +0.62 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ASB8]] | +0.62 | +0.66 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.65 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.63 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[RBBP4]] | -0.61 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[MOB1A]] | -0.61 | -0.38 / -0.67 | both halves | 7e-05 |  |
| [[HNRNPA3]] | -0.59 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[LRPPRC]] | -0.59 | -0.46 / -0.63 | both halves | 3e-05 |  |
| [[PRPS2]] | -0.58 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.58 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[IPO5]] | -0.58 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[CMPK1]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[CRTAP]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.57 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.711). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.8, 0.5); signed map (-1.4, -16.2). **Vector** length 66.1, 10.7% of its response variance represented; |z| ≥ 3 in 773 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.4 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.2 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.8 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.3 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | R3H domain and coiled-coil containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:23,270,120-23,296,279 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp564N123 |
| Matched by | ensembl_id |

UniProt [Q9Y3T6](https://www.uniprot.org/uniprotkb/Q9Y3T6) carries no function annotation.

**Summary**, from NCBI Gene [203069](https://www.ncbi.nlm.nih.gov/gene/203069):

> Predicted to enable nucleic acid binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27329) · Entrez [203069](https://www.ncbi.nlm.nih.gov/gene/203069) · UniProt [Q9Y3T6](https://www.uniprot.org/uniprotkb/Q9Y3T6) · Ensembl [ENSG00000104679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104679)

## Data

Gene col 2481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2481); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2481]; `tensor/DDL_lfc|DDL_z.npy` [2481]; `embed/gene_vectors.npy` [2481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2481 or target_col == 2481). Every well: [[R3HCC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/R3HCC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
