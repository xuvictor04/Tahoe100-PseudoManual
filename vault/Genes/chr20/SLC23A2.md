---
symbol: "SLC23A2"
type: "gene"
col: 1565
ensembl_id: "ENSG00000089057"
name: "solute carrier family 23 member 2"
location: "20p13"
module: 159
arm: "+"
pooled_cpm: 72.72
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# SLC23A2

*solute carrier family 23 member 2* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.96× (z +15.5, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.600× (z -16.7, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP4A]] (+0.69, fdr 7e-06), [[RSAD1]] (+0.67, fdr 1e-05), [[PACC1]] (+0.66, fdr 7e-06); moves opposite to [[THAP2]] (-0.71, fdr 1e-05), [[UBE3B]] (-0.66, fdr 1e-05), [[CPEB2-DT]] (-0.65, fdr 1e-04).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +15.5 | 0e+00 | 46/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +13.6 | 6e-40 | 44/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +11.9 | 3e-30 | 40/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +11.8 | 8e-30 | 41/48 (HT-29, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +8.1 | 5e-14 | 34/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +6.9 | 4e-10 | 32/49 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +6.0 | 2e-07 | 29/48 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +5.9 | 2e-07 | 30/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +5.9 | 3e-07 | 34/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.28×** | +5.8 | 5e-07 | 29/48 (HS-578T, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.29×** | +5.5 | 2e-06 | 26/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.24×** | +4.9 | 5e-05 | 25/48 (H4, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 1e-04 | 23/48 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.6 | 2e-04 | 24/48 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 6e-04 | 20/48 (C-33 A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.006 | 18/48 (KATO III, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -16.7 | 0e+00 | 44/49 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.619×** | -11.0 | 7e-26 | 42/48 (SNU-1, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.809×** | -6.9 | 1e-09 | 23/48 (SNU-1, SW 1271, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.772×** | -5.7 | 1e-06 | 25/48 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.845× | -5.5 | 5e-06 | 22/48 (SK-MEL-2, A-172, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.830×** | -4.1 | 0.003 | 23/48 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | 0.837× | -4.1 | 0.003 | 19/48 (J82, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.845× | -3.9 | 0.008 | 22/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.897× | -3.5 | 0.026 | 13/48 (LOX-IMVI, KATO III, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.5 | 0.029 | 23/50 (SW48, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.869× | -3.2 | 0.056 | 19/48 (A-172, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | 0.859× | -3.2 | 0.056 | 19/45 (LOX-IMVI, SW48, …) | inconsistent across doses | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **0.815×** | -3.1 | 0.072 | 16/48 (SK-MEL-2, C32, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 84.3 | 1 | 4 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.64× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -17.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 85.4 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -13.6) |
| [[A549 (line)]] | wt | 122 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -13.0) |
| [[C32 (line)]] | wt | 83.9 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.48× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 48.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 35.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.14× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -11.8) |
| [[PANC-1 (line)]] | alt | 67.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.57× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 131 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.8) |
| [[KATO III (line)]] | alt | 64.8 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.20× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 64.7 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -13.4) |
| [[SHP-77 (line)]] | alt | 78.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.385× (z -12.3) |
| [[SNU-423 (line)]] | alt | 65.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +11.1) | — |
| [[SW480 (line)]] | alt | 78.4 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 1.70× (z +10.9) | — |
| [[A498 (line)]] | wt | 42.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +10.4) | [[Harringtonine (drug)]] 5 µM 0.359× (z -12.3) ⚠ cell-cycle shift, explains ~59% of this change |
| [[BT-474 (line)]] | alt | 119 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.16× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 83.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.146× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[COLO 205 (line)]] | alt | 43.9 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.48× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -8.9) |
| [[HOP62 (line)]] | alt | 85.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -13.1) |
| [[HT-29 (line)]] | alt | 28.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.56× (z +14.1) | — |
| [[hTERT-HPNE (line)]] | wt | 51.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +10.2) | — |
| [[J82 (line)]] | alt | 53.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -10.3) |
| [[LoVo (line)]] | wt | 57.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -12.0) |
| [[RKO (line)]] | wt | 102 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -18.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 50.2 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.90× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.397× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 85.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.45× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A-427 (line)]] | wt | 85.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 82.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[H4 (line)]] | wt | 55.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.58× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 90.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[HepG2_C3A (line)]] | wt | 196 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.12× (z +14.0) | — |
| [[HS-578T (line)]] | alt | 64.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -10.1) |
| [[LS 180 (line)]] | wt | 48.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.87× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | — |
| [[NCI-H1792 (line)]] | alt | 37.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 60.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -10.2) |
| [[SW 1088 (line)]] | alt | 82.0 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 5 µM 0.0757× (z -8.7) |
| [[SW 1271 (line)]] | alt | 113 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.255× (z -9.7) |
| [[SW 900 (line)]] | alt | 78.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -10.3) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP4A]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[RSAD1]] | +0.67 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PACC1]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[MIPOL1]] | +0.64 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[SERAC1]] | +0.64 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[GTF2E2]] | +0.64 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.64 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[BRF1]] | +0.63 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[METAP1]] | +0.62 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[FXN]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | -0.71 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[UBE3B]] | -0.66 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | -0.65 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[GPANK1]] | -0.65 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[INO80D]] | -0.64 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[DNASE1]] | -0.64 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[USP11]] | -0.64 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[LINC00571]] | -0.63 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ZNF341-AS1]] | -0.63 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[NEK8]] | -0.63 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[ATXN1L]] | -0.63 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ERI2]] | -0.63 | -0.61 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC23A2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises SLC23A2's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[SOAT1]] | C | SOAT1 activity raises SLC23A2's level | lines that do not express SOAT1 (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without SOAT1 | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, CEP85L, CFL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.8, 3.1); signed map (-41.4, -8.3). **Vector** length 114, 30.9% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +8.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +15.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +11.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.4 | -16.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.2 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.8 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -7.5 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.9 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.8 | -6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 23 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:4,852,356-5,010,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SVCT2, KIAA0238, YSPL2; previously SLC23A1 |
| Gene groups (HGNC) | Solute carrier family 23 |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 3 pathways, smallest: Vitamin C (ascorbate) metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGH3](https://www.uniprot.org/uniprotkb/Q9UGH3) (Solute carrier family 23 member 2):

> Sodium/ascorbate cotransporter. Mediates electrogenic uptake of vitamin C, with a stoichiometry of 2 Na(+) for each ascorbate.

**Summary**, from NCBI Gene [9962](https://www.ncbi.nlm.nih.gov/gene/9962):

> The absorption of vitamin C into the body and its distribution to organs requires two sodium-dependent vitamin C transporters. This gene encodes one of the two required transporters and the encoded protein accounts for tissue-specific uptake of vitamin C. Previously, this gene had an official symbol of SLC23A1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10973) · Entrez [9962](https://www.ncbi.nlm.nih.gov/gene/9962) · UniProt [Q9UGH3](https://www.uniprot.org/uniprotkb/Q9UGH3) · Ensembl [ENSG00000089057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089057)

## Data

Gene col 1565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1565); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1565]; `tensor/DDL_lfc|DDL_z.npy` [1565]; `embed/gene_vectors.npy` [1565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1565 or target_col == 1565). Every well: [[SLC23A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC23A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
