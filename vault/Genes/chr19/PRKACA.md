---
symbol: "PRKACA"
type: "gene"
col: 1002
ensembl_id: "ENSG00000072062"
name: "protein kinase cAMP-activated catalytic subunit alpha"
location: "19p13.12"
module: 50
arm: "+"
pooled_cpm: 15.27
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PRKACA

*protein kinase cAMP-activated catalytic subunit alpha* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.10× (z +25.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.793× (z -4.2, q 0.011, down in 16 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.800× (z -4.1, q 0.011, down in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.220×; ⚠ cell-cycle shift, explains ~11% of this change); [[Flumatinib (mesylate) (drug)]] 0.05 µM in 1 line (SW48 0.0549×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.178×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP2A1]] (+0.71, fdr 7e-06), [[AGPAT1]] (+0.70, fdr 8e-06), [[CLSTN1]] (+0.68, fdr 7e-06); moves opposite to [[NIFK]] (-0.66, fdr 1e-05), [[MRPL46]] (-0.63, fdr 1e-05), [[METAP2]] (-0.62, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SORT1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SART3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1002.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.10×** | +25.7 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.80×** | +24.3 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.75×** | +24.0 | 0e+00 | 47/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.15×** | +20.1 | 0e+00 | 26/26 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.98×** | +19.8 | 0e+00 | 40/41 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +16.5 | 0e+00 | 41/46 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.27×** | +13.7 | 4e-41 | 30/35 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +13.4 | 5e-39 | 44/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.03×** | +12.9 | 3e-36 | 43/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.67×** | +9.3 | 6e-19 | 37/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.57×** | +7.8 | 3e-13 | 30/46 (NCI-H460, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +7.8 | 3e-13 | 24/43 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.53×** | +7.7 | 8e-13 | 31/48 (SW480, HepG2/C3A, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.5 | 3e-12 | 30/48 (SW1417, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.47×** | +6.7 | 7e-10 | 27/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.6 | 9e-07 | 19/47 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +4.2 | 6e-04 | 11/48 (RKO, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.7 | 0.005 | 7/48 (SK-MEL-2, A498, …) | top dose only |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.011 | 2/47 (C-33 A, A-172) | inconsistent across doses | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.042 | 10/48 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.062 | 3/48 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.070 | 3/46 (RPMI-7951, SHP-77, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1002.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.220×; ⚠ cell-cycle shift, explains ~11% of this change); [[Flumatinib (mesylate) (drug)]] 0.05 µM in 1 line (SW48 0.0549×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.178×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.793×** | -4.2 | 0.011 | 16/47 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.800×** | -4.1 | 0.011 | 14/47 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.792×** | -4.0 | 0.011 | 16/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.698×** | -3.4 | 0.083 | 11/37 (SW 900, C32, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.839× | -3.2 | 0.14 | 14/47 (A-172, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.18 | 10/47 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1002. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.1 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.86× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.04× (z +10.5) | — |
| [[A498 (line)]] | wt | 15.8 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.19× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 25.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.49× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 14.2 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.21× (z +11.7) | — |
| [[LoVo (line)]] | wt | 9.28 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.58× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 12.5 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.38× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.74× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 16.8 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.20× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 9.15 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.64× (z +11.9) | — |
| [[RKO (line)]] | wt | 17.5 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.69× (z +9.2) | — |
| [[SW480 (line)]] | alt | 17.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.89× (z +15.5) | — |
| [[AsPC-1 (line)]] | alt | 7.50 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.20× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 22.6 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 13.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.50× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 28.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.30× (z +11.1) | — |
| [[A549 (line)]] | wt | 8.90 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +10.6) | — |
| [[J82 (line)]] | alt | 17.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +9.2) | — |
| [[KATO III (line)]] | alt | 11.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.14× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 9.22 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.35× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A-427 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -11.0) ⚠ cell-cycle shift, explains ~11% of this change |
| [[Hs 766T (line)]] | wt | 16.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.46× (z +8.7) | — |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.178× (z -8.6) |
| [[SW48 (line)]] | wt | 13.4 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0549× (z -10.9) |
| [[AN3 CA (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1002), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP2A1]] | +0.71 | +0.64 / +0.60 | both halves | 7e-06 | pathway: Neuronal System |
| [[AGPAT1]] | +0.70 | +0.69 / +0.57 | both halves | 8e-06 | pathway: Integration of energy metabolism |
| [[CLSTN1]] | +0.68 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[PIGS]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[TMEM30A]] | +0.66 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[BSG]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[GPAA1]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[MAPK1]] | +0.64 | +0.46 / +0.59 | both halves | 2e-05 | pathway: Activation of NMDA receptors and postsynaptic events; STRING 929 |
| [[TWSG1]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CALM3]] | +0.64 | +0.67 / +0.41 | both halves | 4e-05 | STRING 989 |
| [[GANAB]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[MXRA7]] | +0.63 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIFK]] | -0.66 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.63 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[METAP2]] | -0.62 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[DNTTIP2]] | -0.62 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[DNAJC2]] | -0.62 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[ESF1]] | -0.62 | -0.40 / -0.69 | both halves | 4e-05 |  |
| [[DHX36]] | -0.61 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[YDJC]] | -0.61 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CCDC137]] | -0.60 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[BRIX1]] | -0.60 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[CEBPZ]] | -0.60 | -0.37 / -0.65 | both halves | 7e-05 |  |
| [[RSL1D1]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORT1]] | B | SORT1 activity raises PRKACA's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.51× lower at baseline in the lines without SORT1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[MEX3A]] | B | MEX3A activity raises PRKACA's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without MEX3A | 0.026 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PRKACA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PRKACA's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CERCAM]] | B | CERCAM activity raises PRKACA's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without CERCAM | 0.055 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SART3]] | C | PRKACA's natural level weakens SART3's drug response | PRKACA's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.28; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.8, -21.7); signed map (-27.8, -38.6). **Vector** length 77.3, 15.7% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.5 | +20.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +6.3 | +19.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.0 | +13.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.3 | +7.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | +3.6 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +9.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.4 | +3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.2 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -4.5 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.2 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase cAMP-activated catalytic subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,091,688-14,118,084 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKACa |
| Gene groups (HGNC) | Protein kinase A subunits; Protein kinase A family |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 104 pathways, smallest: PKA-mediated phosphorylation of key metabolic factors; Loss of phosphorylation of MECP2 at T308; HDL assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P17612](https://www.uniprot.org/uniprotkb/P17612) (cAMP-dependent protein kinase catalytic subunit alpha):

> Phosphorylates a large number of substrates in the cytoplasm and the nucleus. Phosphorylates CDC25B, ABL1, NFKB1, CLDN3, histone H1.4 (H1-4), PSMC5/RPT6, PJA2, RYR2, RORA, SLC6A6, SOX9, UHRF1 and VASP. Regulates the abundance of compartmentalized pools of its regulatory subunits through phosphorylation of PJA2 which binds and ubiquitinates these subunits, leading to their subsequent proteolysis. RORA is activated by phosphorylation. Required for glucose-mediated adipogenic differentiation …

**Summary**, from NCBI Gene [5566](https://www.ncbi.nlm.nih.gov/gene/5566):

> This gene encodes one of the catalytic subunits of protein kinase A, which exists as a tetrameric holoenzyme with two regulatory subunits and two catalytic subunits, in its inactive form. cAMP causes the dissociation of the inactive holoenzyme into a dimer of regulatory subunits bound to four cAMP and two free monomeric catalytic subunits. Four different regulatory subunits and three catalytic subunits have been identified in humans. cAMP-dependent phosphorylation of proteins by protein kinase …

**Accessions** — [HGNC:9380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9380) · Entrez [5566](https://www.ncbi.nlm.nih.gov/gene/5566) · UniProt [P17612](https://www.uniprot.org/uniprotkb/P17612) · Ensembl [ENSG00000072062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072062)

## Data

Gene col 1002: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1002); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1002, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1002]; `tensor/DDL_lfc|DDL_z.npy` [1002]; `embed/gene_vectors.npy` [1002]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1002 or target_col == 1002). Every well: [[PRKACA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKACA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
