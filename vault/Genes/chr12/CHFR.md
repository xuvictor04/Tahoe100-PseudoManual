---
symbol: "CHFR"
type: "gene"
col: 1024
ensembl_id: "ENSG00000072609"
name: "checkpoint with forkhead and ring finger domains"
location: "12q24.33"
module: 52
arm: "+"
pooled_cpm: 59.77
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# CHFR

*checkpoint with forkhead and ring finger domains* — 12q24.33

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (16 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.507× (z -8.5, q 1e-14, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.819× (z -3.7, q 0.008, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA3]] (+0.75, fdr 7e-06, ⚠ same locus), [[RER1]] (+0.73, fdr 7e-06), [[SZT2]] (+0.71, fdr 7e-06), [[YKT6]] (+0.70, fdr 7e-06); moves opposite to [[DLEU1]] (-0.56, fdr 1e-05), [[FOXP1]] (-0.55, fdr 1e-05), [[MAP3K1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Baicalin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.79 | 12/49 (A549, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.507×** | -8.5 | 1e-14 | 41/48 (A-172, C32, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.669×** | -7.5 | 2e-11 | 32/47 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.609×** | -6.2 | 1e-07 | 27/42 (NCI-H460, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.636×** | -6.0 | 4e-07 | 38/48 (A549, A-172, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **0.643×** | -5.8 | 7e-07 | 29/48 (SW 1271, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.627×** | -5.7 | 1e-06 | 27/43 (SW480, SHP-77, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.651×** | -5.6 | 1e-06 | 32/48 (SK-MEL-2, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.749×** | -5.4 | 5e-06 | 31/49 (A549, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.666×** | -5.4 | 5e-06 | 31/48 (SK-MEL-2, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.672×** | -5.2 | 1e-05 | 37/48 (J82, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.677×** | -5.1 | 1e-05 | 31/49 (SK-MEL-2, NCI-H460, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~60% of this change | **0.700×** | -4.4 | 4e-04 | 25/47 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.718×** | -4.4 | 6e-04 | 26/48 (LOX-IMVI, H4, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.008 | 24/48 (NCI-H2347, SW 1088, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.021 | 16/48 (HEC-1-A, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.021 | 23/48 (A-427, AN3 CA, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.044 | 20/49 (HS-578T, HOP62, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **0.779×** | -3.1 | 0.049 | 19/48 (HS-578T, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 41.3 | 0 | 5 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 79.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SW 1271 (line)]] | alt | 72.7 | 0 | 3 (2 ⚠) | — | [[Radotinib (drug)]] 0.5 µM 0.0879× (z -9.5) |
| [[A-427 (line)]] | wt | 49.2 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -16.6) ⚠ cell-cycle shift, explains ~56% of this change |
| [[C32 (line)]] | wt | 38.1 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.263× (z -8.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HS-578T (line)]] | alt | 55.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -9.7) ⚠ cell-cycle shift, explains ~89% of this change |
| [[NCI-H460 (line)]] | wt | 88.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0288× (z -31.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SK-MEL-2 (line)]] | alt | 93.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.6) ⚠ cell-cycle shift, explains ~89% of this change |
| [[AN3 CA (line)]] | alt | 32.2 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0961× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 66.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.4) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HOP62 (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.0) ⚠ cell-cycle shift, explains ~89% of this change |
| [[HT-29 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[MIA PaCa-2 (line)]] | alt | 75.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H1573 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.259× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[NCI-H1792 (line)]] | alt | 78.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.297× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~60% of this change |
| [[SHP-77 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.316× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SW480 (line)]] | alt | 50.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[A498 (line)]] | wt | 83.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA3]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RER1]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[SZT2]] | +0.71 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[YKT6]] | +0.70 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[ZNF587]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[DPH7]] | +0.64 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[PMM2]] | +0.64 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[PIGG]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[B4GALT7]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[DPP9]] | +0.61 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[FUBP3]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[AP1M1]] | +0.61 | +0.69 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU1]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[FOXP1]] | -0.55 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[MAP3K1]] | -0.55 | -0.45 / -0.61 | both halves | 3e-05 | same gene group |
| [[ARHGAP12]] | -0.54 | -0.24 / -0.61 | both halves | 4e-04 |  |
| [[SPPL3]] | -0.53 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[CA8]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TCF7L2]] | -0.52 | -0.26 / -0.58 | both halves | 3e-04 |  |
| [[RAB38]] | -0.51 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TRERF1]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[ARL15]] | -0.50 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TBL1XR1]] | -0.50 | -0.27 / -0.52 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.1, -28.1); signed map (-50.8, 3.1). **Vector** length 76.6, 17.6% of its response variance represented; |z| ≥ 3 in 797 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +1.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.0 | +2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.9 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -4.0 | -7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -2.9 | -8.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | checkpoint with forkhead and ring finger domains |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,822,187-132,956,304 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10796, RNF196 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EP1](https://www.uniprot.org/uniprotkb/Q96EP1) (E3 ubiquitin-protein ligase CHFR):

> E3 ubiquitin-protein ligase that functions in the antephase checkpoint by actively delaying passage into mitosis in response to microtubule poisons. Acts in early prophase before chromosome condensation, when the centrosome move apart from each other along the periphery of the nucleus. Probably involved in signaling the presence of mitotic stress caused by microtubule poisons by mediating the 'Lys-48'-linked ubiquitination of target proteins, leading to their degradation by the proteasome. …

**Summary**, from NCBI Gene [55743](https://www.ncbi.nlm.nih.gov/gene/55743):

> This gene encodes an E3 ubiquitin-protein ligase required for the maintenance of the antephase checkpoint that regulates cell cycle entry into mitosis and, therefore, may play a key role in cell cycle progression and tumorigenesis. The encoded protein has an N-terminal forkhead-associated domain, a central RING-finger domain, and a cysteine-rich C-terminal region. Alternatively spliced transcript variants that encode different protein isoforms have been described. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:20455](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20455) · Entrez [55743](https://www.ncbi.nlm.nih.gov/gene/55743) · UniProt [Q96EP1](https://www.uniprot.org/uniprotkb/Q96EP1) · Ensembl [ENSG00000072609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072609)

## Data

Gene col 1024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1024); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1024]; `tensor/DDL_lfc|DDL_z.npy` [1024]; `embed/gene_vectors.npy` [1024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1024 or target_col == 1024). Every well: [[CHFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
