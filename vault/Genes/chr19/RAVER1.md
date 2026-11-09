---
symbol: "RAVER1"
type: "gene"
col: 8455
ensembl_id: "ENSG00000161847"
name: "ribonucleoprotein, PTB binding 1"
location: "19p13.2"
module: 138
arm: "+"
pooled_cpm: 22.08
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# RAVER1

*ribonucleoprotein, PTB binding 1* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.49× (z +14.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.775× (z -5.6, q 2e-05, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.728× (z -5.1, q 8e-05, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM28]] (+0.63, fdr 1e-05), [[HNRNPUL1]] (+0.63, fdr 1e-05), [[ZNF574]] (+0.61, fdr 1e-05); moves opposite to [[TALAM1]] (-0.59, fdr 3e-05), [[MALAT1]] (-0.57, fdr 3e-05), [[NDFIP1]] (-0.50, fdr 8e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8455.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.49×** | +14.7 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.80×** | +12.6 | 6e-34 | 35/47 (A498, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.38×** | +12.5 | 2e-33 | 45/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.82×** | +9.7 | 6e-20 | 36/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +8.1 | 5e-14 | 35/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +7.9 | 2e-13 | 34/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.57×** | +7.3 | 2e-11 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.60×** | +7.3 | 3e-11 | 32/47 (PANC-1, A498, …) | rises with dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.8 | 1e-04 | 21/48 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.30×** | +4.2 | 0.001 | 18/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.0 | 0.003 | 17/43 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.29×** | +3.9 | 0.004 | 17/47 (NCI-H23, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.29×** | +3.8 | 0.007 | 14/40 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | composition shift; position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.085 | 10/48 (NCI-H23, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.775×** | -5.6 | 2e-05 | 23/48 (A-427, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.728×** | -5.1 | 8e-05 | 24/48 (A498, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.749×** | -4.7 | 6e-04 | 23/48 (SNU-1, A-172, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.010 | 10/48 (PANC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.786×** | -3.9 | 0.010 | 20/48 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.842× | -3.9 | 0.010 | 18/48 (A498, RPMI-7951, …) | rises with dose | position effect removed |
| [[Hydroxyurea (drug)]] 0.5 µM |  | **0.788×** | -3.8 | 0.010 | 15/47 (J82, SW1417, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.790×** | -3.8 | 0.010 | 20/48 (A498, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.649×** | -3.7 | 0.016 | 14/48 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.040 | 7/48 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.814×** | -3.3 | 0.045 | 8/48 (A498, BT-474, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **0.815×** | -3.3 | 0.045 | 10/48 (NCI-H661, HT-29, …) | inconsistent across doses | position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.827×** | -3.1 | 0.083 | 13/48 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.827×** | -3.1 | 0.083 | 10/48 (SW48, NCI-H1792, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.861× | -3.1 | 0.083 | 9/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.828×** | -3.0 | 0.083 | 17/48 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 36.8 | 2 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +18.2) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 5 µM 0.330× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.399× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 16.0 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.59× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 20.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +10.4) | — |
| [[A-172 (line)]] | wt | 26.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AsPC-1 (line)]] | alt | 21.1 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 33.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.2) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.322× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 32.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0694× (z -19.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A549 (line)]] | wt | 16.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +13.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0608× (z -9.1) |
| [[HCT15 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HEC-1-A (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[J82 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 15.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.24× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 15.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +12.3) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 26.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM28]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[HNRNPUL1]] | +0.63 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ZNF574]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[RBM4]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 | same gene group |
| [[CHERP]] | +0.60 | +0.63 / +0.62 | both halves | 7e-06 | STRING 757 |
| [[PTBP1]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 | same gene group; STRING 882 |
| [[CACTIN]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ESPL1]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CPSF7]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 | same gene group |
| [[HNRNPL]] | +0.57 | +0.65 / +0.49 | both halves | 1e-05 | same gene group; STRING 693 |
| [[SUV39H1]] | +0.56 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[SETD1A]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TALAM1]] | -0.59 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[MALAT1]] | -0.57 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[NDFIP1]] | -0.50 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[MYO6]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[WWP1]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ABI1]] | -0.47 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[FNBP1L]] | -0.47 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[STX7]] | -0.46 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[CAST]] | -0.46 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[CHMP2B]] | -0.45 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[LDAF1]] | -0.45 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[KRAS]] | -0.45 | -0.43 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 5 µM | C | RAVER1's natural level raises the cells' numbers under ERK5-IN-2 5 µM (protects the cells) | RAVER1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.339 over the table, 0.096 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.7, -32.0); signed map (-8.9, -34.5). **Vector** length 75.5, 14.1% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.0 | +12.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +12.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.4 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +7.9 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.7 | +1.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.6 | +1.1 |
|  | [[Pentoxifylline (drug)]] 0.5 µM |  | +1.5 | +0.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.5 | +0.4 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -3.8 | -4.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.6 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ribonucleoprotein, PTB binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,316,212-10,333,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1978 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY67](https://www.uniprot.org/uniprotkb/Q8IY67) (Ribonucleoprotein PTB-binding 1):

> Cooperates with PTBP1 to modulate regulated alternative splicing events. Promotes exon skipping. Cooperates with PTBP1 to modulate switching between mutually exclusive exons during maturation of the TPM1 pre-mRNA (By similarity).

**Summary**, from NCBI Gene [125950](https://www.ncbi.nlm.nih.gov/gene/125950):

> Enables RNA binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30296) · Entrez [125950](https://www.ncbi.nlm.nih.gov/gene/125950) · UniProt [Q8IY67](https://www.uniprot.org/uniprotkb/Q8IY67) · Ensembl [ENSG00000161847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161847)

## Data

Gene col 8455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8455); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8455]; `tensor/DDL_lfc|DDL_z.npy` [8455]; `embed/gene_vectors.npy` [8455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8455 or target_col == 8455). Every well: [[RAVER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAVER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
