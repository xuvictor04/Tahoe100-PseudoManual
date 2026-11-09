---
symbol: "GALNT18"
type: "gene"
col: 3129
ensembl_id: "ENSG00000110328"
name: "polypeptide N-acetylgalactosaminyltransferase 18"
location: "11p15.4"
module: 84
arm: "+"
pooled_cpm: 93.43
n_lines_expressing: 40
n_dd_up: 9
n_dd_down: 35
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 7
direction_downstream: 16
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# GALNT18

*polypeptide N-acetylgalactosaminyltransferase 18* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.56× (z +5.9, q 2e-06, up in 29 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.498× (z -9.1, q 4e-17, down in 32 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.546× (z -7.9, q 4e-13, down in 31 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF215]] (+0.65, fdr 7e-06), [[ZFYVE28]] (+0.64, fdr 1e-05), [[SLCO4A1]] (+0.64, fdr 1e-05); moves opposite to [[KANSL1L]] (-0.54, fdr 4e-05), [[YPEL5]] (-0.52, fdr 3e-05), [[AHI1-DT]] (-0.52, fdr 9e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NAV2]] → it (grade B ⚠); 16 go from it, the strongest it → [[SLCO4A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +5.9 | 2e-06 | 29/38 (SW1417, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.56×** | +5.8 | 2e-06 | 23/38 (SW1417, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.54×** | +5.7 | 2e-06 | 24/38 (SW1417, A498, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.50×** | +5.4 | 1e-05 | 27/38 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.6 | 5e-04 | 26/38 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 6e-04 | 21/38 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.003 | 17/38 (SW1417, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.032 | 17/39 (SW1417, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.086 | 16/39 (SW1417, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3129.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.498×** | -9.1 | 4e-17 | 32/38 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.497×** | -8.8 | 4e-16 | 29/37 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.504×** | -8.6 | 1e-15 | 24/32 (C32, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.546×** | -7.9 | 4e-13 | 31/38 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.563×** | -7.5 | 7e-12 | 30/38 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.685×** | -7.0 | 3e-10 | 22/38 (C32, RKO, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.614×** | -6.4 | 2e-08 | 26/38 (C32, NCI-H1792, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -6.3 | 2e-08 | 24/39 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -6.2 | 3e-08 | 21/37 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.622×** | -5.9 | 3e-07 | 30/38 (C32, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.653×** | -5.6 | 1e-06 | 22/38 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.444×** | -5.5 | 1e-06 | 28/39 (C32, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -5.5 | 2e-06 | 21/38 (C32, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -5.1 | 1e-05 | 19/38 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.664×** | -4.9 | 3e-05 | 22/35 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -4.8 | 5e-05 | 21/38 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.750×** | -4.4 | 3e-04 | 25/38 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.735×** | -4.0 | 0.002 | 22/38 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.652×** | -4.0 | 0.002 | 22/38 (HEC-1-A, SW480, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -4.0 | 0.002 | 22/38 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.739×** | -3.9 | 0.002 | 21/39 (MIA PaCa-2, SW480, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.731×** | -3.9 | 0.002 | 19/40 (SK-MEL-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 332 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -20.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.144× (z -15.8) |
| [[RKO (line)]] | wt | 313 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -17.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0223× (z -36.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.293× (z -11.6) |
| [[SW1417 (line)]] | alt | 28.5 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +17.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 4.70× (z +14.2) | — |
| [[A-172 (line)]] | wt | 151 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.446× (z -11.1) |
| [[J82 (line)]] | alt | 291 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -14.0) |
| [[PANC-1 (line)]] | alt | 177 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -15.8) |
| [[NCI-H1792 (line)]] | alt | 353 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -12.4) |
| [[A498 (line)]] | wt | 69.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +16.0) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[BT-474 (line)]] | alt | 168 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.9) ⚠ cell-cycle shift, explains ~43% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.7) |
| [[C-33 A (line)]] | alt | 56.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -16.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -12.2) |
| [[HOP62 (line)]] | alt | 76.8 | 0 | 4 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.555× (z -13.1) ⚠ position not correctable · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.166× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 56.9 | 1 (1 ⚠) | 3 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.60× (z +8.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -12.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 54.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 208 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -10.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 69.5 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.200× (z -9.9) |
| [[HCT15 (line)]] | alt | 70.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -13.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[HEC-1-A (line)]] | alt | 84.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 70.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -9.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.344× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 46.7 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.424× (z -19.8) ⚠ position not correctable · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.270× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 25.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.43× (z +10.6) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H23 (line)]] | alt | 38.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.71× (z +8.5) ⚠ cell-cycle shift, explains ~52% of this change | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -9.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[Panc 03.27 (line)]] | alt | 69.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +13.7) ⚠ cell-cycle shift, explains ~43% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.3) |
| [[A549 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.2) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2347 (line)]] | alt | 78.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.6) |
| [[NCI-H596 (line)]] | alt | 78.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.149× (z -10.0) |
| [[SW480 (line)]] | alt | 133 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.25× (z +8.6) ⚠ unreliable plate only | — |
| [[A-427 (line)]] | wt | 15.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.45 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.91 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.66 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF215]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ZFYVE28]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SLCO4A1]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PHC2]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[IL1RAP]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[TXNDC17]] | +0.60 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[COL13A1]] | +0.59 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[GLDC]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[TRIM9]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PYGL]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[DCBLD1]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CPNE5]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANSL1L]] | -0.54 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[YPEL5]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[AHI1-DT]] | -0.52 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[GIPC2]] | -0.51 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[CSDE1]] | -0.51 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[N4BP2L2]] | -0.50 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[TMUB2]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[GABARAPL1]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ZNF846]] | -0.49 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[NCOA2]] | -0.48 | -0.46 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV2]] | B | NAV2 activity raises GALNT18's level | lines that do not express NAV2 (17) vs lines expressing it (33) | 2.70× lower at baseline in the lines without NAV2 | 0.017 | ⚠ within organs, on part of the lines; also absent: NAV1, ROR1-AS1, CSF1 |
| [[ARFGEF3]] | B | ARFGEF3 activity raises GALNT18's level | lines that do not express ARFGEF3 (6) vs lines expressing it (44) | 2.43× lower at baseline in the lines without ARFGEF3 | 0.037 | ⚠ within organs, on part of the lines; also absent: ARHGEF37, RHBDF2, DBNDD1; maybe low, not absent |
| [[ICAM1]] | B | ICAM1 activity raises GALNT18's level | lines that do not express ICAM1 (19) vs lines expressing it (31) | 2.28× lower at baseline in the lines without ICAM1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ITGB3, ZNF43, ENSG00000259753 |
| [[ITGB3]] | B | ITGB3 activity raises GALNT18's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without ITGB3 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GALNT18's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers GALNT18's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LAPTM5]] | B | LAPTM5 activity raises GALNT18's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.15× lower at baseline in the lines without LAPTM5 | 0.088 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO4A1]] | B | GALNT18 activity raises SLCO4A1's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without GALNT18 | 0.013 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[NAV2]] | B | GALNT18 activity raises NAV2's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 3.63× lower at baseline in the lines without GALNT18 | 0.014 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[ACTN1]] | B | GALNT18 activity raises ACTN1's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without GALNT18 | 0.016 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[SLC9A7]] | B | GALNT18 activity raises SLC9A7's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.85× lower at baseline in the lines without GALNT18 | 0.020 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[ADGRE2]] | B | GALNT18 activity raises ADGRE2's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 3.04× lower at baseline in the lines without GALNT18 | 0.044 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[NCOA2]] | B | GALNT18 activity lowers NCOA2's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.33× higher at baseline in the lines without GALNT18 | 0.048 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[ARFGEF3]] | B | GALNT18 activity raises ARFGEF3's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without GALNT18 | 0.056 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[ANGPTL4]] | B | GALNT18 activity strengthens ANGPTL4's drug response | lines that do not express GALNT18 (6) vs lines expressing it (30) | the lines without GALNT18 respond 0.62× as strongly (z diff +1.86); strongest at Homoharringtonine 5 µM: 0.39x vs 0.11x (z diff +3.0) | 0.057 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A; target measured in part of the lines; artifact flags |
| [[RHBDF2]] | B | GALNT18 activity raises RHBDF2's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without GALNT18 | 0.060 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[AFAP1L1]] | B | GALNT18 activity raises AFAP1L1's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 2.82× lower at baseline in the lines without GALNT18 | 0.076 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[LINC03009-1]] | B | GALNT18 activity raises LINC03009-1's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.37× lower at baseline in the lines without GALNT18 | 0.078 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[TRIM9]] | B | GALNT18 activity raises TRIM9's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 3.04× lower at baseline in the lines without GALNT18 | 0.082 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.5, 4.9); signed map (2.2, 50.9). **Vector** length 136, 43.7% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.8 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.2 | +5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +0.4 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -6.2 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -8.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -4.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -5.4 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.3 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.2 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:11,270,877-11,622,005 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC71806, GALNT15, GalNAc-T18; previously GALNTL4 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P9A2](https://www.uniprot.org/uniprotkb/Q6P9A2) (Polypeptide N-acetylgalactosaminyltransferase 18):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine (GalNAc) residue from UDP-GalNAc to a serine or threonine residue on the protein receptor.

**Summary**, from NCBI Gene [374378](https://www.ncbi.nlm.nih.gov/gene/374378):

> Enables polypeptide N-acetylgalactosaminyltransferase activity. Involved in protein O-linked glycosylation via N-acetyl-galactosamine. Predicted to be located in Golgi membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30488) · Entrez [374378](https://www.ncbi.nlm.nih.gov/gene/374378) · UniProt [Q6P9A2](https://www.uniprot.org/uniprotkb/Q6P9A2) · Ensembl [ENSG00000110328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110328)

## Data

Gene col 3129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3129); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3129]; `tensor/DDL_lfc|DDL_z.npy` [3129]; `embed/gene_vectors.npy` [3129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3129 or target_col == 3129). Every well: [[GALNT18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
