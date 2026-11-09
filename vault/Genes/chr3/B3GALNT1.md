---
symbol: "B3GALNT1"
type: "gene"
col: 9788
ensembl_id: "ENSG00000169255"
name: "beta-1,3-N-acetylgalactosaminyltransferase 1 (Globoside blood group)"
location: "3q26.1"
module: 18
arm: "+"
pooled_cpm: 5.2
n_lines_expressing: 31
n_dd_up: 6
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# B3GALNT1

*beta-1,3-N-acetylgalactosaminyltransferase 1 (Globoside blood group)* — 3q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.41× (z +15.3, q 0e+00, up in 15 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.61× (z +6.9, q 6e-10, up in 12 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1792 11.4×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.524× (z -9.4, q 2e-18, down in 22 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMB]] (+0.73, fdr 7e-06), [[SUSD5]] (+0.63, fdr 1e-05), [[DARS2]] (+0.62, fdr 1e-05); moves opposite to [[INAFM1]] (-0.62, fdr 1e-05), [[TOM1L2]] (-0.58, fdr 1e-05), [[DYNC2I1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9788.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1792 11.4×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.41×** | +15.3 | 0e+00 | 15/18 (NCI-H1792, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.18×** | +11.5 | 4e-28 | 8/9 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.05×** | +10.6 | 4e-24 | 7/11 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +6.9 | 6e-10 | 12/27 (NCI-H1792, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.45×** | +3.9 | 0.013 | 7/25 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.072 | 5/26 (NCI-H1792, SW480, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.36× | +3.2 | 0.11 | 2/27 (PANC-1, J82) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM |  | 1.34× | +3.0 | 0.18 | 6/26 (HCT15, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9788.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.524×** | -9.4 | 2e-18 | 22/25 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.407×** | -9.3 | 5e-18 | 19/27 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.474×** | -7.7 | 2e-12 | 15/27 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.478×** | -7.6 | 4e-12 | 15/27 (SNU-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.526×** | -6.6 | 4e-09 | 14/23 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.520×** | -6.5 | 8e-09 | 14/26 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.594×** | -5.4 | 6e-06 | 13/26 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.625×** | -4.9 | 8e-05 | 10/27 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.683×** | -3.9 | 0.005 | 13/24 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.687×** | -3.9 | 0.006 | 7/27 (HOP62, HCT15, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.490×** | -3.9 | 0.006 | 11/22 (Hs 766T, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.706×** | -3.6 | 0.015 | 12/28 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Idoxuridine (drug)]] 0.05 µM |  | **0.717×** | -3.4 | 0.026 | 6/26 (SW1417, CHP-212, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.808×** | -3.1 | 0.073 | 4/27 (HS-578T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 76.2 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -19.0) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.272× (z -12.6) |
| [[RKO (line)]] | wt | 23.7 | 0 | 8 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0801× (z -14.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.220× (z -12.9) |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.9) |
| [[SW480 (line)]] | alt | 2.38 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0648× (z -10.3) |
| [[A-172 (line)]] | wt | 7.31 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0280× (z -14.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0927× (z -9.9) |
| [[Hs 766T (line)]] | wt | 8.07 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 4.63 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0345× (z -12.2) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.5) ⚠ cell-cycle shift, explains ~6% of this change |
| [[A-427 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -10.2) ⚠ cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 5.65 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.4× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.487 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMB]] | +0.73 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[SUSD5]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[DARS2]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[NIT2]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TMX3]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TMEM33]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ALDH5A1]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ATIC]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[USP46]] | +0.60 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[ZDHHC21]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PDCL3]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ZNF300]] | +0.60 | +0.41 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TOM1L2]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[DYNC2I1]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SIRT2]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[FKBP2]] ⚠ | -0.55 | -0.47 / -0.56 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MTHFR]] | -0.55 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[NOSIP]] | -0.55 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ING2]] | -0.53 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[ZNHIT1]] | -0.52 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[SEC22A]] | -0.52 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[PHLDB3]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[DDT]] | -0.52 | -0.36 / -0.56 | both halves | 9e-05 |  |
| [[SERF2]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-24.5, -31.3); signed map (-13.1, -43.1). **Vector** length 59.5, 12.6% of its response variance represented; |z| ≥ 3 in 630 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +15.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +1.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.3 | -6.6 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,3-N-acetylgalactosaminyltransferase 1 (Globoside blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.1 — chr3:161,083,883-161,105,411 (-) |
| Ensembl biotype | protein_coding |
| Also known as | beta3Gal-T3, galT3, GLOB, B3GALANT1; previously B3GALT3 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases; Blood group antigens |
| Reactome | 4 pathways, smallest: Glycosphingolipid biosynthesis; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O75752](https://www.uniprot.org/uniprotkb/O75752) (UDP-GalNAc:beta-1,3-N-acetylgalactosaminyltransferase 1):

> Transfers N-acetylgalactosamine onto globotriaosylceramide. Plays a critical role in preimplantation stage embryonic development (By similarity).

**Summary**, from NCBI Gene [8706](https://www.ncbi.nlm.nih.gov/gene/8706):

> This gene is a member of the beta-1,3-galactosyltransferase (beta3GalT) gene family. This family encodes type II membrane-bound glycoproteins with diverse enzymatic functions using different donor substrates (UDP-galactose and UDP-N-acetylglucosamine) and different acceptor sugars (N-acetylglucosamine, galactose, N-acetylgalactosamine). The beta3GalT genes are distantly related to the Drosophila Brainiac gene and have the protein coding sequence contained in a single exon. The beta3GalT …

**Accessions** — [HGNC:918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:918) · Entrez [8706](https://www.ncbi.nlm.nih.gov/gene/8706) · UniProt [O75752](https://www.uniprot.org/uniprotkb/O75752) · Ensembl [ENSG00000169255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169255)

## Data

Gene col 9788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9788); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9788]; `tensor/DDL_lfc|DDL_z.npy` [9788]; `embed/gene_vectors.npy` [9788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9788 or target_col == 9788). Every well: [[B3GALNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GALNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
