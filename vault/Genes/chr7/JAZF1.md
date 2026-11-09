---
symbol: "JAZF1"
type: "gene"
col: 7739
ensembl_id: "ENSG00000153814"
name: "JAZF zinc finger 1"
location: "7p15.2-p15.1"
module: 82
arm: "+"
pooled_cpm: 103.86
n_lines_expressing: 41
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 12
direction_downstream: 10
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# JAZF1

*JAZF zinc finger 1* — 7p15.2-p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.51× (z +6.8, q 5e-09, up in 23 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.543× (z -14.3, q 2e-43, down in 29 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF12]] (+0.54, fdr 1e-05), [[CAMK4]] (+0.53, fdr 3e-05), [[AKT3]] (+0.53, fdr 3e-05); moves opposite to [[PDCD6P1]] (-0.44, fdr 9e-05), [[ITFG2]] (-0.43, fdr 1e-04), [[GLE1]] (-0.43, fdr 5e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PCNX2]] → it (grade B ⚠); 10 go from it, the strongest it → [[AKT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +6.8 | 5e-09 | 23/39 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +5.8 | 2e-06 | 24/39 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +5.4 | 1e-05 | 21/39 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 8e-05 | 22/40 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.032 | 14/40 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.4 | 0.057 | 14/39 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.22× | +3.1 | 0.15 | 16/38 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.21× | +3.1 | 0.15 | 15/38 (NCI-H460, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -14.3 | 2e-43 | 29/40 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -11.6 | 1e-28 | 29/34 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.503×** | -10.5 | 1e-23 | 28/36 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.462×** | -10.4 | 6e-23 | 30/40 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -7.8 | 6e-13 | 28/38 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -7.6 | 2e-12 | 30/41 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **0.648×** | -7.2 | 5e-11 | 32/39 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -6.7 | 1e-09 | 23/39 (SHP-77, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -6.4 | 8e-09 | 26/39 (HS-578T, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.702×** | -5.6 | 1e-06 | 21/38 (BT-474, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.724×** | -5.4 | 4e-06 | 25/40 (HOP62, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.742×** | -4.9 | 4e-05 | 19/39 (SHP-77, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.746×** | -4.9 | 5e-05 | 22/39 (SHP-77, A-172, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.595×** | -4.5 | 3e-04 | 24/39 (LOX-IMVI, J82, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.615×** | -4.2 | 0.001 | 24/38 (A549, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.814×** | -3.4 | 0.022 | 16/39 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.867× | -3.3 | 0.027 | 13/40 (LOX-IMVI, SHP-77, …) | all doses, flat |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.880× | -3.0 | 0.080 | 6/40 (Panc 03.27, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.801×** | -3.0 | 0.080 | 13/39 (HOP62, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.830×** | -3.0 | 0.080 | 17/40 (SW 1088, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 160 | 0 | 16 (12 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -17.6) |
| [[A-172 (line)]] | wt | 312 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -19.7) |
| [[HEC-1-A (line)]] | alt | 270 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0918× (z -28.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -10.4) |
| [[C32 (line)]] | wt | 242 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -23.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -15.9) |
| [[HOP62 (line)]] | alt | 120 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -15.8) |
| [[HS-578T (line)]] | alt | 174 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -19.6) |
| [[SHP-77 (line)]] | alt | 380 | 0 | 7 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.252× (z -16.2) |
| [[SW480 (line)]] | alt | 68.5 | 4 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +13.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -12.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 53.5 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Osimertinib (mesylate) (drug)]] 5 µM 0.173× (z -11.9) |
| [[J82 (line)]] | alt | 131 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -15.4) |
| [[A498 (line)]] | wt | 149 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 135 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +21.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.74× (z +14.5) | — |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -8.7) |
| [[A549 (line)]] | wt | 85.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 163 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 56.0 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.08× (z +8.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.6) |
| [[RKO (line)]] | wt | 153 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -15.1) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 118 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -10.3) |
| [[Hs 766T (line)]] | wt | 60.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.305× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.2) |
| [[LoVo (line)]] | wt | 48.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -28.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 67.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -14.4) |
| [[PANC-1 (line)]] | alt | 93.4 | 1 | 1 | [[Panobinostat (drug)]] 0.05 µM 2.14× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -9.4) |
| [[AN3 CA (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 50.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -9.8) |
| [[CHP-212 (line)]] | wt | 53.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.112× (z -9.7) |
| [[SW48 (line)]] | wt | 142 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -9.0) |
| [[A-427 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 23.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 117 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.69 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF12]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 | same gene group |
| [[CAMK4]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[AKT3]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[STOX2]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PCNX2]] | +0.50 | +0.38 / +0.49 | both halves | 7e-05 |  |
| [[RBMS1]] | +0.49 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[SCN8A]] | +0.49 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[PRXL2C]] | +0.48 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[SOGA3]] | +0.48 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[PRKD1]] | +0.48 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[FSD1L]] | +0.47 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[MPDZ]] | +0.46 | +0.39 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD6P1]] | -0.44 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[ITFG2]] | -0.43 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[GLE1]] | -0.43 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TXNDC12]] | -0.42 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[TMEM161B-DT]] | -0.41 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[KHDC4]] | -0.41 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[FAM149B1]] | -0.40 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[MBTD1]] | -0.40 | -0.33 / -0.42 | both halves | 1e-04 | same gene group; STRING 917 |
| [[RUSF1]] | -0.40 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[PIGG]] | -0.40 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[PACRGL]] | -0.40 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[ZNF550]] | -0.39 | -0.38 / -0.40 | both halves | 7e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCNX2]] | B | PCNX2 activity raises JAZF1's level | lines that do not express PCNX2 (8) vs lines expressing it (42) | 2.39× lower at baseline in the lines without PCNX2 | 0.030 | ⚠ within organs, on part of the lines; also absent: NAALADL2, PLEKHA5, KLHL29; maybe low, not absent |
| [[AKT3]] | B | AKT3 activity raises JAZF1's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 2.38× lower at baseline in the lines without AKT3 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[KLF12]] | B | KLF12 activity raises JAZF1's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 1.94× lower at baseline in the lines without KLF12 | 0.040 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1 |
| [[TUBA1A]] | B | TUBA1A activity raises JAZF1's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 2.76× lower at baseline in the lines without TUBA1A | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[ATRNL1]] | B | ATRNL1 activity raises JAZF1's level | lines that do not express ATRNL1 (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without ATRNL1 | 0.058 | ⚠ within organs, on part of the lines; also absent: CAMK4, BVES, NEGR1; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises JAZF1's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.20× lower at baseline in the lines without FAM78B | 0.060 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers JAZF1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers JAZF1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KIAA0408]] | B | KIAA0408 activity raises JAZF1's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 2.31× lower at baseline in the lines without KIAA0408 | 0.096 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1 |
| [[TTLL7]] | C | TTLL7 activity raises JAZF1's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 3.03× lower at baseline in the lines without TTLL7 | 0.014 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725; co-absent with the target |
| [[MPDZ]] | C | MPDZ activity raises JAZF1's level | lines that do not express MPDZ (17) vs lines expressing it (33) | 2.73× lower at baseline in the lines without MPDZ | 0.040 | ⚠ within organs, on part of the lines; also absent: GNB4, BVES, BVES-AS1; co-absent with the target |
| [[OSBPL6]] | C | OSBPL6 activity raises JAZF1's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 2.91× lower at baseline in the lines without OSBPL6 | 0.046 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKT3]] | B | JAZF1 activity raises AKT3's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 8.09× lower at baseline in the lines without JAZF1 | 0.007 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[KLF12]] | B | JAZF1 activity raises KLF12's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 3.06× lower at baseline in the lines without JAZF1 | 0.012 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[HCFC2]] | B | JAZF1 activity raises HCFC2's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 1.82× lower at baseline in the lines without JAZF1 | 0.057 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[SOGA3]] | B | JAZF1 activity raises SOGA3's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 4.49× lower at baseline in the lines without JAZF1 | 0.058 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[TUBA1A]] | B | JAZF1 activity raises TUBA1A's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 4.25× lower at baseline in the lines without JAZF1 | 0.065 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[KIAA0408]] | B | JAZF1 activity raises KIAA0408's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 4.50× lower at baseline in the lines without JAZF1 | 0.067 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[FAM171A1]] | B | JAZF1 activity raises FAM171A1's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 1.88× lower at baseline in the lines without JAZF1 | 0.081 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[ODF2L]] | B | JAZF1 activity raises ODF2L's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 1.95× lower at baseline in the lines without JAZF1 | 0.093 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[TTLL7]] | C | JAZF1 activity raises TTLL7's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 5.61× lower at baseline in the lines without JAZF1 | 0.005 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent; co-absent with the target |
| [[MPDZ]] | C | JAZF1 activity raises MPDZ's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 8.96× lower at baseline in the lines without JAZF1 | 0.016 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.395). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, 38.3); signed map (26.6, 32.4). **Vector** length 112, 32.4% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.5 | +5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.3 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.5 | +1.3 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -3.7 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.8 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.7 | -7.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.1 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | JAZF zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2-p15.1 — chr7:27,830,573-28,180,795 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIP27, DKFZp761K2222, ZNF802 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Tip60/Nua4 histone acetyltransferase complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VZ6](https://www.uniprot.org/uniprotkb/Q86VZ6) (Juxtaposed with another zinc finger protein 1):

> Acts as a transcriptional corepressor of orphan nuclear receptor NR2C2. Inhibits expression of the gluconeogenesis enzyme PCK2 through inhibition of NR2C2 activity (By similarity). Also involved in transcriptional activation of NAMPT by promoting expression of PPARA and PPARD (By similarity). Plays a role in lipid metabolism by suppressing lipogenesis, increasing lipolysis and decreasing lipid accumulation in adipose tissue (By similarity). Plays a role in glucose homeostasis by improving …

**Summary**, from NCBI Gene [221895](https://www.ncbi.nlm.nih.gov/gene/221895):

> This gene encodes a nuclear protein with three C2H2-type zinc fingers, and functions as a transcriptional repressor. Chromosomal aberrations involving this gene are associated with endometrial stromal tumors. Alternatively spliced variants which encode different protein isoforms have been described; however, not all variants have been fully characterized [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:28917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28917) · Entrez [221895](https://www.ncbi.nlm.nih.gov/gene/221895) · UniProt [Q86VZ6](https://www.uniprot.org/uniprotkb/Q86VZ6) · Ensembl [ENSG00000153814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153814)

## Data

Gene col 7739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7739); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7739]; `tensor/DDL_lfc|DDL_z.npy` [7739]; `embed/gene_vectors.npy` [7739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7739 or target_col == 7739). Every well: [[JAZF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAZF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
