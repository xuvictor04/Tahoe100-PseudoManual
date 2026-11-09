---
symbol: "AP1S1"
type: "gene"
col: 2752
ensembl_id: "ENSG00000106367"
name: "adaptor related protein complex 1 subunit sigma 1"
location: "7q22.1"
module: 10
arm: "-"
pooled_cpm: 33.03
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# AP1S1

*adaptor related protein complex 1 subunit sigma 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.22× (z +8.5, q 9e-15, up in 39 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 3.24×, A-172 2.77×, HT-29 3.27×, NCI-H1792 5.51×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.267× (z -20.0, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC1]] (+0.76, fdr 7e-06), [[IGSF8]] (+0.75, fdr 7e-06), [[AP2S1]] (+0.74, fdr 7e-06); moves opposite to [[GABPB2]] (-0.76, fdr 3e-05), [[KRCC1]] (-0.72, fdr 8e-05), [[ZXDA]] (-0.70, fdr 7e-05).
> It sits in the **-** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2752.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 3.24×, A-172 2.77×, HT-29 3.27×, NCI-H1792 5.51×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.22×** | +8.5 | 9e-15 | 39/45 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.02×** | +7.2 | 2e-10 | 29/37 (C32, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.67×** | +5.4 | 1e-05 | 32/46 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.0 | 0.010 | 27/45 (SW48, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | 1.38× | +3.2 | 0.15 | 20/42 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.267×** | -20.0 | 0e+00 | 47/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.296×** | -13.0 | 3e-36 | 43/47 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.438×** | -8.5 | 4e-15 | 42/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.673×** | -4.2 | 0.003 | 27/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.639×** | -4.2 | 0.004 | 31/48 (AsPC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.501×** | -3.9 | 0.011 | 30/47 (NCI-H2030, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.700×** | -3.8 | 0.011 | 25/48 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.517×** | -3.7 | 0.016 | 27/47 (SW 900, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -3.4 | 0.038 | 21/47 (A-427, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.728×** | -3.1 | 0.092 | 25/48 (AsPC-1, CHP-212, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.572×** | -3.1 | 0.092 | 23/48 (LOX-IMVI, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 44.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -19.1) |
| [[A498 (line)]] | wt | 63.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -15.5) |
| [[HT-29 (line)]] | alt | 40.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -17.7) |
| [[J82 (line)]] | alt | 23.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -19.8) |
| [[PANC-1 (line)]] | alt | 27.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0645× (z -29.3) |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 2 | — | [[Canagliflozin (drug)]] 5 µM 0.0684× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 64.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -19.3) |
| [[C32 (line)]] | wt | 61.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.5) |
| [[H4 (line)]] | wt | 42.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0822× (z -14.4) |
| [[HCT15 (line)]] | alt | 38.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 27.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.1) |
| [[HS-578T (line)]] | alt | 31.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -10.2) |
| [[KATO III (line)]] | alt | 53.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 26.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -18.3) |
| [[NCI-H23 (line)]] | alt | 31.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 24.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -13.6) |
| [[RKO (line)]] | wt | 51.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 23.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -10.7) |
| [[SW 900 (line)]] | alt | 35.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -17.2) |
| [[SW480 (line)]] | alt | 37.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -18.6) |
| [[A549 (line)]] | wt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.2) |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -12.4) |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -16.3) |
| [[HepG2_C3A (line)]] | wt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.6) |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.5) |
| [[Hs 766T (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.370× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -18.8) |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.7) |
| [[SW1417 (line)]] | alt | 41.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.1) |
| [[SW48 (line)]] | wt | 49.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.5) |
| [[A-427 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC1]] | +0.76 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[IGSF8]] | +0.75 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[AP2S1]] | +0.74 | +0.73 / +0.62 | both halves | 7e-06 | pathway: HIV Infection; STRING 921 |
| [[TUSC2]] | +0.73 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[ANKRD13D]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[KYAT1]] | +0.67 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[B3GAT3]] | +0.66 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[MOSPD3]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[LPCAT4]] | +0.66 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[GM2A]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SBNO1]] | +0.65 | +0.69 / +0.50 | both halves | 1e-05 | same gene group |
| [[MPG]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB2]] | -0.76 | -0.77 / -0.45 | both halves | 3e-05 |  |
| [[KRCC1]] | -0.72 | -0.80 / -0.37 | both halves | 8e-05 |  |
| [[ZXDA]] | -0.70 | -0.70 / -0.37 | both halves | 7e-05 |  |
| [[CCT6P3]] | -0.69 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[PPP3CB-AS1]] | -0.68 | -0.70 / -0.36 | both halves | 9e-05 |  |
| [[TIA1]] | -0.67 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.66 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[THOC7]] | -0.65 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[ZNF181]] | -0.64 | -0.71 / -0.29 | both halves | 3e-04 |  |
| [[WARS2-AS1]] | -0.64 | -0.68 / -0.34 | both halves | 1e-04 |  |
| [[PCNX4-DT]] | -0.64 | -0.75 / -0.21 | both halves | 6e-04 |  |
| [[RBM26-AS1]] | -0.63 | -0.69 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.9, 0.3); signed map (-35.2, 13.5). **Vector** length 75.3, 19.3% of its response variance represented; |z| ≥ 3 in 675 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.3 | +0.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.3 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -13.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.8 | -4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -20.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 1 subunit sigma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,154,456-101,161,596 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AP19, SIGMA1A, WUGSC:H_DJ0747G18.2; previously CLAPS1, EKV3 |
| Gene groups (HGNC) | Adaptor related protein complex 1; MicroRNA protein coding host genes |
| Reactome | 13 pathways, smallest: Nef mediated downregulation of MHC class I complex cell surface expression; Nef-mediates down modulation of cell surface receptors by recruiting them to clathrin adapters; The role of Nef in HIV-1 replication and disease pathogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P61966](https://www.uniprot.org/uniprotkb/P61966) (AP-1 complex subunit sigma-1A):

> Subunit of clathrin-associated adaptor protein complex 1 that plays a role in protein sorting in the late-Golgi/trans-Golgi network (TGN) and/or endosomes. The AP complexes mediate both the recruitment of clathrin to membranes and the recognition of sorting signals within the cytosolic tails of transmembrane cargo molecules.

**Summary**, from NCBI Gene [1174](https://www.ncbi.nlm.nih.gov/gene/1174):

> The protein encoded by this gene is part of the clathrin coat assembly complex which links clathrin to receptors in coated vesicles. These vesicles are involved in endocytosis and Golgi processing. This protein, as well as beta-prime-adaptin, gamma-adaptin, and the medium (mu) chain AP47, form the AP-1 assembly protein complex located at the Golgi vesicle. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:559) · Entrez [1174](https://www.ncbi.nlm.nih.gov/gene/1174) · UniProt [P61966](https://www.uniprot.org/uniprotkb/P61966) · Ensembl [ENSG00000106367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106367)

## Data

Gene col 2752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2752); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2752]; `tensor/DDL_lfc|DDL_z.npy` [2752]; `embed/gene_vectors.npy` [2752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2752 or target_col == 2752). Every well: [[AP1S1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1S1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
