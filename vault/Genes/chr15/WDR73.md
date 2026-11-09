---
symbol: "WDR73"
type: "gene"
col: 10788
ensembl_id: "ENSG00000177082"
name: "WD repeat domain 73"
location: "15q25.2"
module: 89
arm: "+"
pooled_cpm: 22.62
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# WDR73

*WD repeat domain 73* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +20.4, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.859× (z -4.7, q 0.001, down in 13 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.123×, SW480 0.362×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.115×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (COLO 205 0.246×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD4]] (+0.68, fdr 1e-05), [[TMEM199]] (+0.67, fdr 4e-05), [[TMEM69]] (+0.65, fdr 1e-05); moves opposite to [[INPP5F]] (-0.57, fdr 2e-04), [[OSBPL6]] (-0.55, fdr 8e-05), [[CYTH3]] (-0.54, fdr 1e-04).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +20.4 | 0e+00 | 43/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +14.2 | 4e-43 | 36/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +11.8 | 4e-30 | 33/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +11.4 | 4e-28 | 36/48 (LoVo, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +11.4 | 7e-28 | 35/48 (Panc 03.27, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +10.7 | 2e-24 | 35/44 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +9.8 | 6e-21 | 33/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +9.1 | 5e-18 | 32/45 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +7.8 | 3e-13 | 32/48 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +7.6 | 2e-12 | 29/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.40×** | +7.5 | 5e-12 | 31/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.38×** | +7.1 | 7e-11 | 25/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.0 | 1e-10 | 25/47 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.39×** | +6.9 | 2e-10 | 26/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +6.6 | 2e-09 | 24/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +6.0 | 5e-08 | 20/48 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.6 | 9e-05 | 14/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.001 | 15/47 (PANC-1, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.074 | 3/46 (NCI-H1792, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10788.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.123×, SW480 0.362×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.115×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (COLO 205 0.246×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -4.7 | 0.001 | 13/48 (SNU-1, HEC-1-A, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.818×** | -4.2 | 0.006 | 19/46 (A-172, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pentoxifylline (drug)]] 0.5 µM |  | 0.871× | -3.0 | 0.34 | 9/48 (SW48, SHP-77, …) | two highest doses |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | 0.871× | -3.0 | 0.34 | 15/47 (LS 180, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 24.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 22.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.2) | — |
| [[A-172 (line)]] | wt | 20.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.3) | — |
| [[A498 (line)]] | wt | 21.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.0) | — |
| [[SW480 (line)]] | alt | 27.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.83× (z +9.2) | — |
| [[A549 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 29.5 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.246× (z -8.6) |
| [[HCT15 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.28× (z +8.5) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 22.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.54× (z +8.6) | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD4]] | +0.68 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TMEM199]] | +0.67 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[TMEM69]] | +0.65 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ZC3HC1]] | +0.65 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[ALKBH1]] | +0.64 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[POLR3C]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[RAE1]] | +0.62 | +0.53 / +0.52 | both halves | 1e-05 | same gene group |
| [[THBS4]] | +0.62 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[MTHFSD]] | +0.61 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TEFM]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.61 | +0.67 / +0.37 | both halves | 7e-05 |  |
| [[ZNF629]] | +0.61 | +0.61 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5F]] | -0.57 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[OSBPL6]] | -0.55 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[CYTH3]] | -0.54 | -0.59 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.9, 11.8); signed map (-7.5, -20.7). **Vector** length 74.7, 13.3% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +11.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +20.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +9.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +4.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.0 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | +2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.9 | +7.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 73 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:84,639,285-84,654,343 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14888, HSPC264 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P4I2](https://www.uniprot.org/uniprotkb/Q6P4I2) (Integrator complex assembly factor WDR73):

> Component of a multiprotein complex required for the assembly of the RNA endonuclease module of the integrator complex. Associates with INTS9 and INTS11 in the cytoplasm, stabilizing the INTS9-INTS11 heterodimer and blocking the active site of INTS11. BRAT1 then joins the complex and plugs the active site of INTS11, leading to WDR73 release and nuclear import of INTS9 and INTS11.

**Summary**, from NCBI Gene [84942](https://www.ncbi.nlm.nih.gov/gene/84942):

> The protein encoded by this gene is thought to contain multiple WD40 repeats. WD40 repeats are motifs that contain 40-60 amino acids, and usually end with Trp-Asp (WD). This protein is found in the cytoplasm during interphase, but accumulates at the spindle poles and astral microtubules during mitosis. Reduced expression of this gene results in abnormalities in the size and morphology of the nucleus. Mutations in this gene have been associated with Galloway-Mowat syndrome PMID: 25466283), which …

**Accessions** — [HGNC:25928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25928) · Entrez [84942](https://www.ncbi.nlm.nih.gov/gene/84942) · UniProt [Q6P4I2](https://www.uniprot.org/uniprotkb/Q6P4I2) · Ensembl [ENSG00000177082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177082)

## Data

Gene col 10788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10788); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10788]; `tensor/DDL_lfc|DDL_z.npy` [10788]; `embed/gene_vectors.npy` [10788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10788 or target_col == 10788). Every well: [[WDR73 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR73.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
