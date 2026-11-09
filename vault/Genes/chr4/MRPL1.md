---
symbol: "MRPL1"
type: "gene"
col: 9791
ensembl_id: "ENSG00000169288"
name: "mitochondrial ribosomal protein L1"
location: "4q21.1"
module: 213
arm: "+"
pooled_cpm: 59.27
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# MRPL1

*mitochondrial ribosomal protein L1* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.58× (z +10.9, q 7e-25, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.811× (z -7.0, q 2e-09, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.262×, CHP-212 0.155×, SHP-77 0.469×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 0.210×, NCI-H460 0.430×, SW480 0.573×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 0.640×, NCI-H460 0.578×, Hs 766T 0.490×); [[(S)-Crizotinib (drug)]] 5 µM in 1 line (SW 1088 0.0692×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.395×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CINP]] (+0.71, fdr 7e-06), [[ALKBH3]] (+0.67, fdr 7e-06), [[DHX57]] (+0.66, fdr 7e-06); moves opposite to [[HECA]] (-0.53, fdr 1e-05).
> It is in [[Module 213]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9791.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +10.9 | 7e-25 | 41/48 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.29×** | +10.2 | 3e-22 | 41/49 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +7.2 | 1e-10 | 24/48 (NCI-H2347, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +6.8 | 1e-09 | 33/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +6.5 | 1e-08 | 29/48 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.28×** | +5.6 | 2e-06 | 24/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +5.5 | 3e-06 | 24/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.50×** | +5.0 | 4e-05 | 25/47 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.43×** | +4.4 | 6e-04 | 20/48 (PANC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.2 | 0.001 | 10/48 (AsPC-1, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 21/48 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.1 | 0.002 | 20/48 (HEC-1-A, LOX-IMVI, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | 1.18× | +3.9 | 0.004 | 21/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.004 | 19/48 (HEC-1-A, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.9 | 0.004 | 14/48 (LOX-IMVI, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.012 | 15/48 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.013 | 16/48 (A498, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.017 | 14/48 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.035 | 11/48 (SK-MEL-2, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9791.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HEC-1-A 0.262×, CHP-212 0.155×, SHP-77 0.469×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 3 lines (C32 0.210×, NCI-H460 0.430×, SW480 0.573×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 0.640×, NCI-H460 0.578×, Hs 766T 0.490×); [[(S)-Crizotinib (drug)]] 5 µM in 1 line (SW 1088 0.0692×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.395×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -7.0 | 2e-09 | 23/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.9 | 0.015 | 17/50 (RKO, SW480, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.848× | -3.9 | 0.015 | 15/47 (NCI-H2030, LoVo, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.891× | -3.9 | 0.015 | 13/48 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.864× | -3.5 | 0.057 | 16/48 (C-33 A, RKO, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -3.4 | 0.064 | 21/48 (C32, NCI-H460, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | 0.776× | -3.1 | 0.12 | 9/48 (LoVo, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.958× | -3.1 | 0.12 | 0/49 | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.779× | -3.1 | 0.12 | 11/48 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.880× | -3.0 | 0.14 | 6/47 (H4, HOP62, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9791. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 98.3 | 4 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.62× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 79.0 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.14× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 71.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.33× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 53.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.69× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -9.9) |
| [[C32 (line)]] | wt | 44.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 69.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 52.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.233× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[Hs 766T (line)]] | wt | 55.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 39.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.288× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 36.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[RPMI-7951 (line)]] | alt | 59.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.395× (z -8.6) |
| [[SHP-77 (line)]] | alt | 93.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.469× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 83.3 | 0 | 1 | — | [[(S)-Crizotinib (drug)]] 5 µM 0.0692× (z -9.3) |
| [[A-172 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 61.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9791), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CINP]] | +0.71 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[ALKBH3]] | +0.67 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[DHX57]] | +0.66 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ZNF573]] | +0.66 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[TTC26]] | +0.65 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NUBPL]] | +0.65 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[RBM26]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[MRPS9]] | +0.65 | +0.56 / +0.70 | both halves | 1e-05 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 995 |
| [[CCDC43]] | +0.64 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[NDUFS4]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 | STRING 427 |
| [[NUFIP1]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SMARCAD1]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECA]] | -0.53 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-23.3, -1.4); signed map (-13.9, -17.8). **Vector** length 108, 26.2% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.0 | +7.2 |
|  | [[NG25 (drug)]] 5 µM |  | +5.5 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +10.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.2 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:77,862,830-77,952,785 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BM022, uL1m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9BYD6](https://www.uniprot.org/uniprotkb/Q9BYD6) carries no function annotation.

**Summary**, from NCBI Gene [65008](https://www.ncbi.nlm.nih.gov/gene/65008):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14275) · Entrez [65008](https://www.ncbi.nlm.nih.gov/gene/65008) · UniProt [Q9BYD6](https://www.uniprot.org/uniprotkb/Q9BYD6) · Ensembl [ENSG00000169288](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169288)

## Data

Gene col 9791: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9791); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9791, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9791]; `tensor/DDL_lfc|DDL_z.npy` [9791]; `embed/gene_vectors.npy` [9791]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9791 or target_col == 9791). Every well: [[MRPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
