---
symbol: "ZNF77"
type: "gene"
col: 10637
ensembl_id: "ENSG00000175691"
name: "zinc finger protein 77"
location: "19p13.3"
module: 12
arm: "+"
pooled_cpm: 5.09
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ZNF77

*zinc finger protein 77* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.66× (z +27.6, q 0e+00, up in 39 of 41 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (SHP-77 0.118×; ⚠ transcription drop); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0834×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF57]] (+0.66, fdr 1e-05, ⚠ same locus), [[ZNF555]] (+0.64, fdr 9e-06), [[PPFIA3]] (+0.56, fdr 1e-05), [[CCDC144NL-1]] (+0.55, fdr 1e-05); moves opposite to [[TMX1]] (-0.49, fdr 2e-05), [[LDHB]] (-0.48, fdr 3e-04), [[ARPC5]] (-0.48, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.66×** | +27.6 | 0e+00 | 39/41 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.55×** | +21.7 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.31×** | +21.1 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.18×** | +18.1 | 0e+00 | 46/47 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +18.1 | 0e+00 | 39/40 (HOP62, AsPC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.99×** | +13.9 | 1e-41 | 34/38 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.37×** | +10.9 | 7e-26 | 24/45 (SW480, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +10.1 | 4e-22 | 30/45 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.02×** | +8.9 | 4e-17 | 28/40 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +8.9 | 4e-17 | 34/47 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +8.6 | 4e-16 | 17/29 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +7.4 | 5e-12 | 21/38 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +6.8 | 4e-10 | 23/46 (SW1417, SW480, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.64×** | +5.8 | 3e-07 | 5/13 (SW480, SW1417, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +5.6 | 1e-06 | 12/47 (SW1417, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +5.5 | 1e-06 | 21/47 (SW1417, SW480, …) | two highest doses | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +4.4 | 3e-04 | 13/42 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +3.8 | 0.004 | 4/43 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.022 | 3/45 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10637.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Allantoin (drug)]] 0.05 µM in 1 line (SHP-77 0.118×; ⚠ transcription drop); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0834×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | 0.780× | -3.2 | 0.91 | 5/46 (COLO 205, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.71 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +16.7) | — |
| [[LoVo (line)]] | wt | 5.23 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 6.98 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.66× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 17.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +17.9) | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +12.5) | — |
| [[A-172 (line)]] | wt | 5.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 2.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +8.8) | — |
| [[KATO III (line)]] | alt | 4.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 3.47 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0834× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 4.67 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.74× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 2.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 4.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.06× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 5.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 3.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 5.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 5.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 8.87 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.118× (z -8.6) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 4.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +10.3) | — |
| [[A-427 (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF57]] | +0.66 | +0.73 / +0.52 | both halves | 1e-05 | same gene group; ⚠ same locus (14.7 kb: neighbours can correlate without regulation) |
| [[ZNF555]] | +0.64 | +0.77 / +0.57 | both halves | 9e-06 | same gene group |
| [[PPFIA3]] | +0.56 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CCDC144NL-1]] | +0.55 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[GMEB2]] | +0.55 | +0.63 / +0.38 | both halves | 7e-05 |  |
| [[ZNF316]] | +0.54 | +0.63 / +0.45 | both halves | 3e-05 | same gene group |
| [[FKBP2]] ⚠ | +0.53 | +0.55 / +0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PARP16]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[SLC25A20]] | +0.51 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CIDECP1]] | +0.51 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[NFKBIL1]] | +0.51 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[HOTAIRM1]] | +0.50 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[GCAT]] | +0.50 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[ZNF707]] | +0.50 | +0.55 / +0.41 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX1]] | -0.49 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[LDHB]] | -0.48 | -0.62 / -0.28 | both halves | 3e-04 |  |
| [[ARPC5]] | -0.48 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TMX3]] | -0.47 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[XRCC5]] | -0.45 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[TSPAN6]] | -0.44 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[PRDX3]] | -0.44 | -0.55 / -0.27 | both halves | 3e-04 |  |
| [[ATP5F1A]] | -0.43 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[NIT2]] | -0.43 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[LRPPRC]] | -0.43 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[MOB1A]] | -0.43 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[CCT3]] | -0.43 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.293). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-54.7, 1.6); signed map (-7.1, -8.1). **Vector** length 47.9, 5.93% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +27.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +18.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.0 | +13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.0 | +10.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +0.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +1.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.4 | +4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | -1.3 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | +0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | +1.3 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.0 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 77 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,933,218-2,944,971 (-) |
| Ensembl biotype | protein_coding |
| Also known as | pT1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15935](https://www.uniprot.org/uniprotkb/Q15935) (Zinc finger protein 77):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [58492](https://www.ncbi.nlm.nih.gov/gene/58492):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13150) · Entrez [58492](https://www.ncbi.nlm.nih.gov/gene/58492) · UniProt [Q15935](https://www.uniprot.org/uniprotkb/Q15935) · Ensembl [ENSG00000175691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175691)

## Data

Gene col 10637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10637); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10637]; `tensor/DDL_lfc|DDL_z.npy` [10637]; `embed/gene_vectors.npy` [10637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10637 or target_col == 10637). Every well: [[ZNF77 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF77.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
