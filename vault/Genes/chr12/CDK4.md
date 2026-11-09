---
symbol: "CDK4"
type: "gene"
col: 5705
ensembl_id: "ENSG00000135446"
name: "cyclin dependent kinase 4"
location: "12q14.1"
module: 4
arm: "+"
pooled_cpm: 21.57
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CDK4

*cyclin dependent kinase 4* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.63× (z +15.5, q 0e+00, up in 42 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.63× (z +5.8, q 7e-07, up in 34 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.330×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.419×; ⚠ cell-cycle shift, explains ~96% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPG21]] (+0.60, fdr 1e-05), [[FOXRED2]] (+0.54, fdr 1e-05), [[PFKM]] (+0.53, fdr 2e-05); moves opposite to [[ULK1]] (-0.46, fdr 3e-05), [[CDC37L1]] (-0.46, fdr 1e-04), [[STX12]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.63×** | +15.5 | 0e+00 | 42/43 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.24×** | +13.6 | 1e-39 | 33/36 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.60×** | +10.6 | 7e-24 | 32/38 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.8 | 7e-07 | 34/47 (A-172, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.52×** | +4.8 | 2e-04 | 26/46 (NCI-H1792, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.45×** | +4.5 | 7e-04 | 25/46 (J82, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.1 | 0.003 | 23/44 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.79×** | +3.7 | 0.018 | 15/47 (SW480, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.72×** | +3.4 | 0.042 | 15/48 (NCI-H1792, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.056 | 12/46 (SNU-423, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5705.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 0.330×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.419×; ⚠ cell-cycle shift, explains ~96% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.758× | -3.3 | 0.41 | 14/48 (SW480, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.759× | -3.2 | 0.41 | 18/47 (COLO 205, NCI-H661, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.616× | -3.0 | 0.45 | 14/47 (SNU-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 40.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW480 (line)]] | alt | 26.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 24.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 28.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 18.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 45.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.47× (z +16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.44× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 21.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.63× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AsPC-1 (line)]] | alt | 9.35 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.34× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.0) ⚠ cell-cycle shift, explains ~96% of this change |
| [[SNU-423 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPG21]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[FOXRED2]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PFKM]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[MTHFD1]] | +0.53 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PFAS]] | +0.52 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[CYB5RL]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[TRIP13]] | +0.51 | +0.46 / +0.47 | both halves | 3e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[NCR3LG1]] | +0.51 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LRPPRC]] | +0.50 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[UTP18]] | +0.50 | +0.31 / +0.57 | both halves | 2e-04 |  |
| [[IPO4]] | +0.49 | +0.42 / +0.54 | both halves | 4e-05 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[ENOPH1]] | +0.49 | +0.38 / +0.51 | both halves | 6e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ULK1]] | -0.46 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CDC37L1]] | -0.46 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[STX12]] | -0.45 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[ARL8A]] | -0.45 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[TNFSF13B]] | -0.44 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[HOXA9]] | -0.44 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[DUSP18]] | -0.44 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[GUCA1B]] | -0.44 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[EIF1B]] | -0.43 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[BSDC1]] | -0.43 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[MTIF3]] | -0.43 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[DYNLL1]] | -0.43 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[GNRH1]] | -0.43 | -0.50 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.382). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.9, -34.0); signed map (5.8, -39.1). **Vector** length 66.2, 13.7% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +5.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.5 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +10.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,747,727-57,756,013 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSK-J3 |
| Gene groups (HGNC) | Cyclin dependent kinases; MicroRNA protein coding host genes |
| Hallmark sets | MYC_TARGETS_V2, PI3K_AKT_MTOR_SIGNALING, G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 47 pathways, smallest: Diseases of Cellular Senescence; Diseases of cellular response to stress; Evasion of Oncogene Induced Senescence Due to Defective p16INK4A binding to CDK4 and CDK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [P11802](https://www.uniprot.org/uniprotkb/P11802) (Cyclin-dependent kinase 4):

> Ser/Thr-kinase component of cyclin D-CDK4 (DC) complexes that phosphorylate and inhibit members of the retinoblastoma (RB) protein family including RB1 and regulate the cell-cycle during G(1)/S transition. Phosphorylation of RB1 allows dissociation of the transcription factor E2F from the RB/E2F complexes and the subsequent transcription of E2F target genes which are responsible for the progression through the G(1) phase. Hypophosphorylates RB1 in early G(1) phase. Cyclin D-CDK4 complexes are …

**Summary**, from NCBI Gene [1019](https://www.ncbi.nlm.nih.gov/gene/1019):

> The protein encoded by this gene is a member of the Ser/Thr protein kinase family. This protein is highly similar to the gene products of S. cerevisiae cdc28 and S. pombe cdc2. It is a catalytic subunit of the protein kinase complex that is important for cell cycle G1 phase progression. The activity of this kinase is restricted to the G1-S phase, which is controlled by the regulatory subunits D-type cyclins and CDK inhibitor p16(INK4a). This kinase was shown to be responsible for the …

**Accessions** — [HGNC:1773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1773) · Entrez [1019](https://www.ncbi.nlm.nih.gov/gene/1019) · UniProt [P11802](https://www.uniprot.org/uniprotkb/P11802) · Ensembl [ENSG00000135446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135446)

## Data

Gene col 5705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5705); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5705]; `tensor/DDL_lfc|DDL_z.npy` [5705]; `embed/gene_vectors.npy` [5705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5705 or target_col == 5705). Every well: [[CDK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
