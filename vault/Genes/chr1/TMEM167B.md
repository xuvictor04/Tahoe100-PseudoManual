---
symbol: "TMEM167B"
type: "gene"
col: 13272
ensembl_id: "ENSG00000215717"
name: "transmembrane protein 167B"
location: "1p13.3"
module: 41
arm: "+"
pooled_cpm: 31.46
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# TMEM167B

*transmembrane protein 167B* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.60× (z +8.6, q 3e-15, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.741× (z -5.3, q 5e-05, down in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.610× (z -4.8, q 3e-04, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.163×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H2347 0.193×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.357×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change); [[vincristine (drug)]] 5 µM in 1 line (H4 0.0932×); [[Cepharanthine (drug)]] 5 µM in 1 line (Hs 766T 0.497×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UFSP2]] (+0.68, fdr 7e-06), [[GOLGA2]] (+0.64, fdr 7e-06), [[TMF1]] (+0.63, fdr 7e-06); moves opposite to [[NUP50]] (-0.62, fdr 7e-06), [[UTP4]] (-0.61, fdr 1e-05), [[UHRF1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +8.6 | 3e-15 | 36/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +8.2 | 7e-14 | 34/47 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +6.2 | 1e-07 | 23/45 (PANC-1, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +5.7 | 2e-06 | 27/48 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +5.2 | 2e-05 | 21/46 (PANC-1, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.33×** | +5.0 | 6e-05 | 23/48 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.21×** | +5.0 | 6e-05 | 24/47 (PANC-1, A-172, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 4e-04 | 22/48 (C32, NCI-H2030, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.006 | 15/48 (MIA PaCa-2, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.006 | 19/48 (NCI-H23, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.23×** | +3.8 | 0.006 | 19/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +3.8 | 0.006 | 21/45 (SW 900, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.006 | 18/48 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Terfenadine (drug)]] 5 µM |  | 1.15× | +3.7 | 0.008 | 12/48 (A498, SNU-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.008 | 15/48 (C32, LOX-IMVI, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.008 | 9/48 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.036 | 13/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.12× | +2.9 | 0.088 | 5/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13272.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.163×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (NCI-H2347 0.193×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.357×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change); [[vincristine (drug)]] 5 µM in 1 line (H4 0.0932×); [[Cepharanthine (drug)]] 5 µM in 1 line (Hs 766T 0.497×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.741×** | -5.3 | 5e-05 | 24/48 (H4, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.822×** | -5.2 | 7e-05 | 23/47 (Hs 766T, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.610×** | -4.8 | 3e-04 | 23/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.842× | -4.5 | 9e-04 | 19/48 (Panc 03.27, RPMI-7951, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.855× | -4.1 | 0.004 | 12/48 (NCI-H23, Panc 03.27, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.870× | -3.7 | 0.025 | 20/48 (NCI-H1573, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Arbutin (drug)]] 0.05 µM |  | **0.819×** | -3.4 | 0.051 | 16/48 (SNU-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 58.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 0.497× (z -8.7) |
| [[A549 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 60.0 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0932× (z -8.7) |
| [[LoVo (line)]] | wt | 23.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.97× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 39.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 39.2 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.193× (z -10.0) |
| [[SW480 (line)]] | alt | 22.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[A-172 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFSP2]] | +0.68 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[GOLGA2]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TMF1]] | +0.63 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[LYSMD3]] | +0.62 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[ZFPL1]] | +0.61 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[FAM114A1]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[UFL1]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TBC1D23]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[KIF16B]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ARMCX3]] | +0.58 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[EMC2]] | +0.58 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[SAT2]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP50]] | -0.62 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[UTP4]] | -0.61 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[UHRF1]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[PPIA]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[E2F3]] | -0.57 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[SNRPD1]] | -0.55 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[PA2G4]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SUV39H2]] | -0.53 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SYNCRIP]] | -0.53 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[NACC1]] | -0.53 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[MBD3]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.9, -38.5); signed map (-51.0, 15.5). **Vector** length 84.7, 17.3% of its response variance represented; |z| ≥ 3 in 826 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.3 | -4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.7 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.1 | -5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 167B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,090,764-109,096,934 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AD-020, FLJ90710; previously C1orf119 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRX6](https://www.uniprot.org/uniprotkb/Q9NRX6) (Protein kish-B):

> Involved in the early part of the secretory pathway.

**Summary**, from NCBI Gene [56900](https://www.ncbi.nlm.nih.gov/gene/56900):

> Involved in constitutive secretory pathway. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30187) · Entrez [56900](https://www.ncbi.nlm.nih.gov/gene/56900) · UniProt [Q9NRX6](https://www.uniprot.org/uniprotkb/Q9NRX6) · Ensembl [ENSG00000215717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215717)

## Data

Gene col 13272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13272); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13272]; `tensor/DDL_lfc|DDL_z.npy` [13272]; `embed/gene_vectors.npy` [13272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13272 or target_col == 13272). Every well: [[TMEM167B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM167B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
