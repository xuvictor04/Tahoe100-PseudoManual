---
symbol: "ANTXR1"
type: "gene"
col: 9824
ensembl_id: "ENSG00000169604"
name: "ANTXR cell adhesion molecule 1"
location: "2p13.3"
module: 66
arm: "+"
pooled_cpm: 90.24
n_lines_expressing: 33
n_dd_up: 5
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 11
direction_downstream: 16
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# ANTXR1

*ANTXR cell adhesion molecule 1* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.75× (z +10.2, q 8e-22, up in 22 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.48× (z +5.8, q 1e-06, up in 22 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 5.63×, A498 3.59×, HEC-1-A 2.75×, PANC-1 3.26×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A549 4.59×, A498 3.23×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.28×, C-33 A 2.86×; ⚠ cell-cycle shift, explains ~2% of this change).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.298× (z -18.0, q 0e+00, down in 28 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A1]] (+0.67, fdr 7e-06), [[COL4A2]] (+0.67, fdr 7e-06), [[ERLIN2]] (+0.65, fdr 2e-05); moves opposite to [[RASSF7]] (-0.66, fdr 1e-05), [[SIRT7]] (-0.56, fdr 4e-05), [[PTK6]] (-0.55, fdr 2e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[WNT5A]] → it (grade B ⚠); 16 go from it, the strongest it → [[CSTB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9824.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A549 5.63×, A498 3.59×, HEC-1-A 2.75×, PANC-1 3.26×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A549 4.59×, A498 3.23×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A498 2.28×, C-33 A 2.86×; ⚠ cell-cycle shift, explains ~2% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +10.2 | 8e-22 | 22/27 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +5.9 | 1e-06 | 19/28 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.8 | 1e-06 | 22/31 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +5.5 | 7e-06 | 24/32 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.43×** | +3.8 | 0.019 | 20/31 (RPMI-7951, J82, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | 1.33× | +3.0 | 0.21 | 18/31 (A549, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.34× | +3.0 | 0.21 | 14/31 (C-33 A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9824.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.298×** | -18.0 | 0e+00 | 28/30 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.412×** | -9.3 | 4e-18 | 27/30 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.433×** | -8.8 | 3e-16 | 28/31 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.455×** | -8.3 | 2e-14 | 30/31 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.465×** | -8.0 | 1e-13 | 25/31 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.466×** | -7.7 | 1e-12 | 28/31 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.497×** | -6.9 | 3e-10 | 25/31 (CHP-212, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.538×** | -6.5 | 5e-09 | 26/31 (H4, CHP-212, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.538×** | -6.5 | 5e-09 | 24/31 (NCI-H460, CHP-212, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.572×** | -5.9 | 3e-07 | 23/31 (CHP-212, H4, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.574×** | -5.8 | 3e-07 | 27/31 (C32, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -4.2 | 0.001 | 18/31 (NCI-H460, CHP-212, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.693×** | -3.8 | 0.005 | 18/31 (CHP-212, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.693×** | -3.8 | 0.005 | 16/31 (CHP-212, SHP-77, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.504×** | -3.8 | 0.006 | 19/31 (SW480, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.573×** | -3.7 | 0.008 | 20/31 (NCI-H460, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.518×** | -3.6 | 0.010 | 19/31 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.627×** | -3.5 | 0.015 | 19/31 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.711×** | -3.4 | 0.018 | 20/30 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.794×** | -3.4 | 0.018 | 17/32 (H4, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 617 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 389 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0435× (z -28.5) |
| [[PANC-1 (line)]] | alt | 151 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -18.3) |
| [[C32 (line)]] | wt | 87.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.7) |
| [[HOP62 (line)]] | alt | 290 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -19.1) |
| [[J82 (line)]] | alt | 157 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -19.2) |
| [[A498 (line)]] | wt | 47.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 56.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0364× (z -24.8) |
| [[NCI-H1792 (line)]] | alt | 183 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -13.1) |
| [[SW480 (line)]] | alt | 36.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.256× (z -11.0) |
| [[A549 (line)]] | wt | 138 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.63× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -11.4) |
| [[H4 (line)]] | wt | 168 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 86.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 129 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -20.3) |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -12.3) |
| [[A-172 (line)]] | wt | 168 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.275× (z -8.9) |
| [[HS-578T (line)]] | alt | 56.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.5) |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 199 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -17.2) |
| [[SHP-77 (line)]] | alt | 64.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.243× (z -11.1) |
| [[SNU-1 (line)]] | wt | 87.9 | 0 | 2 | — | [[Sonidegib (drug)]] 5 µM 0.0650× (z -10.2) |
| [[C-33 A (line)]] | alt | 39.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +9.5) ⚠ cell-cycle shift, explains ~2% of this change | — |
| [[NCI-H2030 (line)]] | alt | 105 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -16.3) |
| [[Panc 03.27 (line)]] | alt | 49.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 92.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.1) |
| [[SNU-423 (line)]] | alt | 73.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -15.6) |
| [[SW 1271 (line)]] | alt | 112 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0543× (z -12.6) |
| [[SW 900 (line)]] | alt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.6) |
| [[A-427 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.80 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.93 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A1]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 | pathway: Bacterial Infection Pathways |
| [[COL4A2]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | same gene group; pathway: Bacterial Infection Pathways |
| [[ERLIN2]] | +0.65 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[FSTL1]] | +0.60 | +0.49 / +0.54 | both halves | 1e-05 | same gene group |
| [[TGFBI]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PDIA3P1]] | +0.59 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[LAMC1]] | +0.58 | +0.39 / +0.62 | both halves | 6e-05 | pathway: Bacterial Infection Pathways |
| [[LINC01116]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[IGFBP7]] | +0.57 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[COL3A1]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[CHST14]] | +0.57 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[F2R]] | +0.56 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF7]] | -0.66 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SIRT7]] | -0.56 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PTK6]] | -0.55 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[TUBB2B]] | -0.53 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[FUT2]] | -0.52 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[CSTB]] | -0.52 | -0.49 / -0.32 | both halves | 1e-04 |  |
| [[FAM83E]] | -0.52 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[PWWP2B]] | -0.52 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[MKNK2]] | -0.52 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[RDH13]] | -0.52 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[SLC35E4]] | -0.51 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ARID3A]] | -0.51 | -0.33 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT5A]] | B | WNT5A activity raises ANTXR1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.24× lower at baseline in the lines without WNT5A | 0.075 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[PDGFRB]] | B | PDGFRB activity raises ANTXR1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 4.51× lower at baseline in the lines without PDGFRB | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[HECW2]] | C | HECW2 activity raises ANTXR1's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 5.63× lower at baseline in the lines without HECW2 | 0.003 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041; co-absent with the target |
| [[FLI1]] | C | FLI1 activity raises ANTXR1's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 3.97× lower at baseline in the lines without FLI1 | 0.014 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615; co-absent with the target |
| [[CNRIP1]] | C | CNRIP1 activity raises ANTXR1's level | lines that do not express CNRIP1 (25) vs lines expressing it (25) | 5.51× lower at baseline in the lines without CNRIP1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047; co-absent with the target |
| [[DOCK2]] | C | DOCK2 activity raises ANTXR1's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 6.06× lower at baseline in the lines without DOCK2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent; co-absent with the target |
| [[TBX18]] | C | TBX18 activity raises ANTXR1's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 3.73× lower at baseline in the lines without TBX18 | 0.027 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251; co-absent with the target |
| [[HTRA1]] | C | HTRA1 activity raises ANTXR1's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 3.12× lower at baseline in the lines without HTRA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises ANTXR1's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 4.71× lower at baseline in the lines without MMP2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[PCDHGC3]] | C | PCDHGC3 activity raises ANTXR1's level | lines that do not express PCDHGC3 (18) vs lines expressing it (32) | 4.76× lower at baseline in the lines without PCDHGC3 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, ITGB3, EGFEM1P; co-absent with the target |
| [[MSRB3]] | C | MSRB3 activity raises ANTXR1's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 4.13× lower at baseline in the lines without MSRB3 | 0.053 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 9, C 7. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSTB]] | B | ANTXR1 activity lowers CSTB's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 1.80× higher at baseline in the lines without ANTXR1 | 0.011 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[CHROMR]] | B | ANTXR1 activity raises CHROMR's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 2.82× lower at baseline in the lines without ANTXR1 | 0.014 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[KIAA1522]] | B | ANTXR1 activity lowers KIAA1522's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 2.92× higher at baseline in the lines without ANTXR1 | 0.025 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[BCAT2]] | B | ANTXR1 activity raises BCAT2's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without ANTXR1 | 0.031 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[DZIP1L]] | B | ANTXR1 activity raises DZIP1L's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 3.21× lower at baseline in the lines without ANTXR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[RASSF7]] | B | ANTXR1 activity lowers RASSF7's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 2.42× higher at baseline in the lines without ANTXR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[CDK15]] | B | ANTXR1 activity raises CDK15's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 1.92× lower at baseline in the lines without ANTXR1 | 0.042 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[PCDHGA2]] | B | ANTXR1 activity raises PCDHGA2's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 2.89× lower at baseline in the lines without ANTXR1 | 0.069 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[TRIM11]] | B | ANTXR1 activity lowers TRIM11's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 1.21× higher at baseline in the lines without ANTXR1 | 0.084 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804 |
| [[HECW2]] | C | ANTXR1 activity raises HECW2's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 4.28× lower at baseline in the lines without ANTXR1 | 0.011 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804; co-absent with the target |
| [[MSRB3]] | C | ANTXR1 activity raises MSRB3's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 5.52× lower at baseline in the lines without ANTXR1 | 0.028 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804; co-absent with the target |
| [[PCDHGC3]] | C | ANTXR1 activity raises PCDHGC3's level | lines that do not express ANTXR1 (17) vs lines expressing it (33) | 2.77× lower at baseline in the lines without ANTXR1 | 0.060 | ⚠ within organs, on part of the lines; also absent: VASH1, RFLNB, ENSG00000285804; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.479). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.8, 22.4); signed map (24.7, 41.6). **Vector** length 100, 33.1% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.52 to 8); *Fibronectin matrix formation* (reactome, mean cos +0.54 to 6); *Collagen chain trimerization* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | +4.6 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -1.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.9 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -8.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.4 | -3.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.0 | -6.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | ANTXR cell adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:69,013,176-69,249,327 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TEM8, FLJ21776, FLJ10601, ATR |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Uptake and function of anthrax toxins; Uptake and actions of bacterial toxins; Bacterial Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6X2](https://www.uniprot.org/uniprotkb/Q9H6X2) (Anthrax toxin receptor 1):

> Plays a role in cell attachment and migration. Interacts with extracellular matrix proteins and with the actin cytoskeleton and thereby plays an important role in normal extracellular matrix (ECM) homeostasis. Mediates adhesion of cells to type 1 collagen and gelatin, reorganization of the actin cytoskeleton and promotes cell spreading. Plays a role in the angiogenic response of cultured umbilical vein endothelial cells. May also act as a receptor for PLAU. Upon ligand binding, stimulates the …

**Summary**, from NCBI Gene [84168](https://www.ncbi.nlm.nih.gov/gene/84168):

> This gene encodes a type I transmembrane protein and is a tumor-specific endothelial marker that has been implicated in colorectal cancer. The encoded protein has been shown to also be a docking protein or receptor for Bacillus anthracis toxin, the causative agent of the disease, anthrax. The binding of the protective antigen (PA) component, of the tripartite anthrax toxin, to this receptor protein mediates delivery of toxin components to the cytosol of cells. Once inside the cell, the other …

**Accessions** — [HGNC:21014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21014) · Entrez [84168](https://www.ncbi.nlm.nih.gov/gene/84168) · UniProt [Q9H6X2](https://www.uniprot.org/uniprotkb/Q9H6X2) · Ensembl [ENSG00000169604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169604)

## Data

Gene col 9824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9824); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9824]; `tensor/DDL_lfc|DDL_z.npy` [9824]; `embed/gene_vectors.npy` [9824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9824 or target_col == 9824). Every well: [[ANTXR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANTXR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
