---
symbol: "PRMT5"
type: "gene"
col: 1967
ensembl_id: "ENSG00000100462"
name: "protein arginine methyltransferase 5"
location: "14q11.2"
module: 1
arm: "+"
pooled_cpm: 25.95
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PRMT5

*protein arginine methyltransferase 5* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.05× (z +11.6, q 2e-28, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.759× (z -6.3, q 1e-07, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.196×, HCT15 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.378×); [[Pimozide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0879×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IMP4]] (+0.79, fdr 7e-06), [[IFRD2]] (+0.77, fdr 7e-06), [[PES1]] (+0.74, fdr 7e-06); moves opposite to [[GNAS]] (-0.66, fdr 7e-06), [[ATP5F1E]] (-0.61, fdr 1e-05), [[SEPTIN1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.05×** | +11.6 | 2e-28 | 45/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +9.3 | 6e-18 | 42/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.76×** | +9.2 | 8e-18 | 31/43 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +8.9 | 6e-17 | 38/47 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +7.8 | 5e-13 | 34/47 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +6.9 | 5e-10 | 33/48 (LoVo, PANC-1, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.56×** | +6.9 | 5e-10 | 23/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.33×** | +6.5 | 5e-09 | 22/47 (PANC-1, A549, …) | all doses, flat | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.3 | 2e-08 | 26/45 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +6.2 | 2e-08 | 33/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +6.2 | 3e-08 | 29/47 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +5.5 | 2e-06 | 28/48 (C32, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.39×** | +5.3 | 5e-06 | 23/46 (NCI-H2347, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.37×** | +4.7 | 1e-04 | 20/40 (SNU-423, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 3e-04 | 19/47 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.002 | 17/48 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.031 | 14/45 (SNU-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.038 | 18/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.038 | 11/47 (NCI-H1573, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.039 | 9/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.039 | 10/48 (LOX-IMVI, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.044 | 20/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.196×, HCT15 0.231×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.378×); [[Pimozide (drug)]] 0.5 µM in 1 line (AN3 CA 0.0879×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.759×** | -6.3 | 1e-07 | 26/48 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -3.9 | 0.033 | 15/48 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.852× | -3.7 | 0.045 | 15/48 (SNU-1, A-427, …) | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 0.810× | -3.3 | 0.14 | 16/47 (A498, HEC-1-A, …) | top dose only | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.817× | -3.1 | 0.16 | 9/47 (A-427, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.818× | -3.1 | 0.16 | 13/47 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.876× | -3.0 | 0.19 | 9/48 (CFPAC-1, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 24.5 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.17× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 24.6 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.24× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 28.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 26.3 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.55× (z +9.1) | — |
| [[A549 (line)]] | wt | 22.3 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.82× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0879× (z -9.9) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 42.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 22.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.15× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 48.9 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.82× (z +9.0) | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -10.4) |
| [[SNU-423 (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IMP4]] | +0.79 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[IFRD2]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[PES1]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[RBM28]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[DRG2]] | +0.70 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[NOL6]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[BYSL]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[MAK16]] | +0.69 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[PSMG1]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[BCS1L]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PTCD2]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.66 | -0.60 / -0.73 | both halves | 7e-06 |  |
| [[ATP5F1E]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[SEPTIN1]] | -0.60 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SERF2]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.3, -39.0); signed map (-2.8, -43.3). **Vector** length 95.1, 22.4% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.57 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.59 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.59 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +9.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | protein arginine methyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:22,920,525-22,929,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SKB1Hs; previously HRMT1L5, SKB1 |
| Gene groups (HGNC) | 7BS protein arginine methyltranferases; Arginine methyltransferases |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 9 pathways, smallest: Regulation of TP53 Activity through Methylation; RMTs methylate histone arginines; Metabolism of non-coding RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O14744](https://www.uniprot.org/uniprotkb/O14744) (Protein arginine N-methyltransferase 5):

> Arginine methyltransferase that can both catalyze the formation of omega-N monomethylarginine (MMA) and symmetrical dimethylarginine (sDMA), with a preference for the formation of MMA. Specifically mediates the symmetrical dimethylation of arginine residues in the small nuclear ribonucleoproteins Sm D1 (SNRPD1) and Sm D3 (SNRPD3); such methylation being required for the assembly and biogenesis of snRNP core particles. Methylates SUPT5H and may regulate its transcriptional elongation properties. …

**Summary**, from NCBI Gene [10419](https://www.ncbi.nlm.nih.gov/gene/10419):

> This gene encodes an enzyme that belongs to the methyltransferase family. The encoded protein catalyzes the transfer of methyl groups to the amino acid arginine, in target proteins that include histones, transcriptional elongation factors and the tumor suppressor p53. This gene plays a role in several cellular processes, including transcriptional regulation, and the assembly of small nuclear ribonucleoproteins. A pseudogene of this gene has been defined on chromosome 4. Alternative splicing …

**Accessions** — [HGNC:10894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10894) · Entrez [10419](https://www.ncbi.nlm.nih.gov/gene/10419) · UniProt [O14744](https://www.uniprot.org/uniprotkb/O14744) · Ensembl [ENSG00000100462](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100462)

## Data

Gene col 1967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1967); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1967]; `tensor/DDL_lfc|DDL_z.npy` [1967]; `embed/gene_vectors.npy` [1967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1967 or target_col == 1967). Every well: [[PRMT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRMT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
