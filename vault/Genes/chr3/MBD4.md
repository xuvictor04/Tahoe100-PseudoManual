---
symbol: "MBD4"
type: "gene"
col: 4945
ensembl_id: "ENSG00000129071"
name: "methyl-CpG binding domain 4, DNA glycosylase"
location: "3q21.3"
module: 111
arm: "+"
pooled_cpm: 42.95
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# MBD4

*methyl-CpG binding domain 4, DNA glycosylase* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.45× (z +6.4, q 9e-08, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.540× (z -5.5, q 2e-05, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.266×, A498 0.506×, LoVo 0.508×, NCI-H460 0.525×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (AN3 CA 0.116×, A-427 0.399×, RKO 0.287×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.348×, SHP-77 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WHAMM]] (+0.55, fdr 3e-05), [[ZNF684]] (+0.55, fdr 3e-05), [[FAAP24]] (+0.53, fdr 1e-04); moves opposite to [[CDC42]] (-0.60, fdr 4e-05), [[GNB1]] (-0.57, fdr 1e-05), [[FLNA]] (-0.54, fdr 1e-04).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4945.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +6.4 | 9e-08 | 33/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.7 | 3e-06 | 29/48 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.38×** | +5.5 | 8e-06 | 29/48 (SK-MEL-2, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.36×** | +5.3 | 2e-05 | 29/48 (A-172, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.36×** | +5.2 | 2e-05 | 31/48 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.34×** | +4.8 | 1e-04 | 26/47 (SW480, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.22×** | +4.8 | 1e-04 | 21/48 (J82, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.33×** | +4.7 | 1e-04 | 24/47 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +4.4 | 6e-04 | 27/47 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 7e-04 | 22/48 (SW480, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.003 | 22/47 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.16× | +3.5 | 0.020 | 10/48 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.051 | 19/48 (LoVo, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4945.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.266×, A498 0.506×, LoVo 0.508×, NCI-H460 0.525×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (AN3 CA 0.116×, A-427 0.399×, RKO 0.287×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.348×, SHP-77 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.540×** | -5.5 | 2e-05 | 28/48 (A498, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.587×** | -4.8 | 5e-04 | 26/48 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.823× | -3.3 | 0.14 | 15/48 (HS-578T, HCT15, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | 0.693× | -3.3 | 0.14 | 13/48 (SHP-77, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 56.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.30× (z +16.7) | — |
| [[A-427 (line)]] | wt | 70.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.38× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 54.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 40.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.76× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 55.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 33.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0998× (z -11.0) ⚠ toxic |
| [[J82 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +11.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 27.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 55.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.7) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW480 (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +11.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WHAMM]] | +0.55 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[ZNF684]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[FAAP24]] | +0.53 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[TMF1]] | +0.53 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[TRAPPC2B]] | +0.52 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[RBMX2]] | +0.52 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[TRAPPC4]] | +0.52 | +0.26 / +0.61 | both halves | 3e-04 |  |
| [[NKAP]] | +0.52 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[MRPS18C]] | +0.52 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[TMEM101]] | +0.51 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[SLC4A1AP]] | +0.51 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ACTR6]] | +0.50 | +0.45 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42]] | -0.60 | -0.42 / -0.69 | both halves | 4e-05 |  |
| [[GNB1]] | -0.57 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[FLNA]] | -0.54 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[RMRP]] | -0.53 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[RPSA]] | -0.52 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[SCRIB]] | -0.51 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[WDR1]] | -0.50 | -0.29 / -0.57 | both halves | 3e-04 |  |
| [[SZRD1]] | -0.50 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[CROCC]] | -0.49 | +0.02 / -0.59 | ⚠ one half (not replicated) | 1.00 |  |
| [[SF1]] | -0.49 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[RPS3A]] | -0.48 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[SMG1P3]] | -0.48 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[ACTB]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction -0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.8, -17.7); signed map (-45.3, -33.7). **Vector** length 80.1, 17.3% of its response variance represented; |z| ≥ 3 in 698 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.0 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.2 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | +1.2 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.7 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.5 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -7.1 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -4.8 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.1 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | methyl-CpG binding domain 4, DNA glycosylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:129,430,947-129,440,179 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MED1 |
| Gene groups (HGNC) | DNA glycosylases; Methyl-CpG binding domain containing |
| Reactome | 8 pathways, smallest: Displacement of DNA glycosylase by APEX1; Cleavage of the damaged pyrimidine; Depyrimidination |
| Matched by | ensembl_id |

**Function**, from UniProt [O95243](https://www.uniprot.org/uniprotkb/O95243) (Methyl-CpG-binding domain protein 4):

> Mismatch-specific DNA N-glycosylase involved in DNA repair. Has thymine glycosylase activity and is specific for G:T mismatches within methylated and unmethylated CpG sites. Can also remove uracil or 5-fluorouracil in G:U mismatches. Has no lyase activity. Was first identified as methyl-CpG-binding protein.

**Summary**, from NCBI Gene [8930](https://www.ncbi.nlm.nih.gov/gene/8930):

> The protein encoded by this gene is a member of a family of nuclear proteins related by the presence of a methyl-CpG binding domain (MBD). These proteins are capable of binding specifically to methylated DNA, and some members can also repress transcription from methylated gene promoters. This protein contains an MBD domain at the N-terminus that functions both in binding to methylated DNA and in protein interactions and a C-terminal mismatch-specific glycosylase domain that is involved in DNA …

**Accessions** — [HGNC:6919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6919) · Entrez [8930](https://www.ncbi.nlm.nih.gov/gene/8930) · UniProt [O95243](https://www.uniprot.org/uniprotkb/O95243) · Ensembl [ENSG00000129071](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129071)

## Data

Gene col 4945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4945); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4945]; `tensor/DDL_lfc|DDL_z.npy` [4945]; `embed/gene_vectors.npy` [4945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4945 or target_col == 4945). Every well: [[MBD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
