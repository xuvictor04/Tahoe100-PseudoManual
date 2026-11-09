---
symbol: "ENTPD7"
type: "gene"
col: 12513
ensembl_id: "ENSG00000198018"
name: "ectonucleoside triphosphate diphosphohydrolase 7"
location: "10q24.2"
module: 49
arm: "+"
pooled_cpm: 80.42
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 36
n_dd_up_clean: 12
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# ENTPD7

*ectonucleoside triphosphate diphosphohydrolase 7* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.64× (z +6.2, q 4e-07, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.509× (z -11.6, q 2e-28, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUTC]] (+0.85, fdr 7e-06, ⚠ same locus), [[LINC02693]] (+0.69, fdr 1e-05), [[SEC22B]] (+0.69, fdr 7e-06), [[TMED3]] (+0.68, fdr 7e-06); moves opposite to [[DCUN1D1]] (-0.59, fdr 2e-05), [[ZNF608]] (-0.58, fdr 7e-06), [[BAZ2B]] (-0.58, fdr 6e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[STC1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CUTC]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +6.2 | 4e-07 | 36/48 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +5.8 | 2e-06 | 33/47 (hTERT-HPNE, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +5.5 | 6e-06 | 29/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +5.1 | 5e-05 | 32/47 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +4.7 | 3e-04 | 28/47 (LOX-IMVI, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.45×** | +4.6 | 5e-04 | 32/47 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.41×** | +4.2 | 0.002 | 25/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.0 | 0.005 | 25/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.005 | 21/47 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.006 | 25/47 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.64×** | +3.9 | 0.006 | 25/47 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.76×** | +3.6 | 0.015 | 21/47 (Hs 766T, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.025 | 24/47 (LOX-IMVI, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.4 | 0.032 | 25/47 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.066 | 22/46 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.066 | 19/47 (KATO III, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.19× | +3.1 | 0.068 | 16/48 (A498, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12513.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.509×** | -11.6 | 2e-28 | 34/48 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -7.8 | 1e-12 | 36/47 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.536×** | -7.6 | 7e-12 | 32/47 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.569×** | -6.6 | 7e-09 | 36/49 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -6.3 | 2e-08 | 30/39 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.614×** | -5.9 | 3e-07 | 30/47 (RKO, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.713×** | -5.8 | 5e-07 | 29/47 (NCI-H23, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.717×** | -5.7 | 8e-07 | 30/47 (SK-MEL-2, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.724×** | -5.5 | 2e-06 | 36/47 (A549, HS-578T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.640×** | -5.2 | 1e-05 | 28/46 (AsPC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.645×** | -5.1 | 1e-05 | 30/47 (RKO, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.672×** | -4.8 | 7e-05 | 27/47 (A549, A498, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.671×** | -4.7 | 1e-04 | 26/47 (A549, J82, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.717×** | -4.4 | 4e-04 | 29/47 (RKO, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.700×** | -4.3 | 5e-04 | 30/48 (RKO, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.711×** | -4.1 | 0.001 | 23/47 (RKO, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.790×** | -3.9 | 0.003 | 23/48 (AsPC-1, RKO, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 308 | 0 | 21 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -22.9) |
| [[AsPC-1 (line)]] | alt | 149 | 1 | 14 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.88× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 77.0 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 83.3 | 0 | 8 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.435× (z -22.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.191× (z -18.1) |
| [[HS-578T (line)]] | alt | 95.7 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -16.4) |
| [[A-172 (line)]] | wt | 99.9 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -12.2) |
| [[A498 (line)]] | wt | 156 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -15.6) |
| [[A549 (line)]] | wt | 136 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -15.1) |
| [[J82 (line)]] | alt | 82.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -16.7) |
| [[NCI-H1573 (line)]] | alt | 117 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.60× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 72.1 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.359× (z -11.8) |
| [[SW 900 (line)]] | alt | 125 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.9) |
| [[HOP62 (line)]] | alt | 171 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 98.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 72.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -17.3) |
| [[C32 (line)]] | wt | 101 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 64.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -12.3) |
| [[SNU-423 (line)]] | alt | 84.3 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -9.3) |
| [[H4 (line)]] | wt | 110 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -9.1) |
| [[Hs 766T (line)]] | wt | 62.9 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.22× (z +11.6) ⚠ unreliable plate only | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -9.5) ⚠ cell-cycle shift, explains ~19% of this change |
| [[RPMI-7951 (line)]] | alt | 74.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -11.6) |
| [[A-427 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUTC]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 | STRING 448; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC02693]] | +0.69 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[SEC22B]] | +0.69 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[TMED3]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[NAT9]] | +0.66 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SEC13]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[YKT6]] | +0.66 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[DHDDS]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[PDE4DIP]] | +0.65 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[GP6-AS1]] | +0.64 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[CALU]] | +0.63 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[HM13]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.63 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D1]] | -0.59 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[ZNF608]] | -0.58 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[BAZ2B]] | -0.58 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[USP24]] | -0.57 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[JADE2]] | -0.57 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[CILK1]] | -0.57 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[CFAP418]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[STXBP3]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[NFIB]] | -0.54 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[STAT5A]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[TAPBPL]] | -0.54 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[MED12]] | -0.54 | -0.52 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STC1]] | B | STC1 activity raises ENTPD7's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.33× lower at baseline in the lines without STC1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[TMEM158]] | B | TMEM158 activity raises ENTPD7's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without TMEM158 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[TOP2A]] | B | TOP2A activity raises ENTPD7's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC1A1]] | B | SLC1A1 activity raises ENTPD7's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.60× lower at baseline in the lines without SLC1A1 | 0.067 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[TMEM158]] | B | TMEM158 activity strengthens ENTPD7's drug response | lines that do not express TMEM158 (18) vs lines expressing it (31) | the lines without TMEM158 respond 0.36× as strongly (z diff +3.01); strongest at Idarubicin (hydrochloride) 5 µM: 0.84x vs 0.42x (z diff +5.5) | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B; target measured in part of the lines; artifact flags |
| [[MARCHF3]] | B | MARCHF3 activity raises ENTPD7's level | lines that do not express MARCHF3 (5) vs lines expressing it (45) | 2.03× lower at baseline in the lines without MARCHF3 | 0.089 | ⚠ within organs, on part of the lines; also absent: HIPK2, OPN3, CEMIP2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CUTC]] | C | ENTPD7's natural level strengthens CUTC's drug response | ENTPD7's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.57; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.9, -32.4); signed map (-50.8, 6.9). **Vector** length 126, 45.4% of its response variance represented; |z| ≥ 3 in 1,586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | -0.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.8 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.3 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.1 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleoside triphosphate diphosphohydrolase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:99,659,509-99,711,241 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LALP1, FLJ30978 |
| Gene groups (HGNC) | Ectonucleoside triphosphate diphosphohydrolase family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 3 pathways, smallest: Phosphate bond hydrolysis by NTPDase proteins; Nucleotide catabolism; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQZ7](https://www.uniprot.org/uniprotkb/Q9NQZ7) (Ectonucleoside triphosphate diphosphohydrolase 7):

> Catalyzes the hydrolysis of nucleoside triphosphates and diphosphates in a calcium- or magnesium-dependent manner. Preferentially hydrolyzes nucleoside 5'-triphosphates, with substrate preference for UTP > GTP > CTP. Hydrolyzes ATP and nucleoside diphosphates only to a minor extent.

**Summary**, from NCBI Gene [57089](https://www.ncbi.nlm.nih.gov/gene/57089):

> This gene encodes a purine-converting ectoenzyme which belongs to the ecto-nucleoside triphosphate diphosphohydrolase (E-NTPDase) family. The encoded protein hydrolyzes extracellular nucleoside triphosphates (UTP, GTP, and CTP) to nucleoside monophosphates as part of a purinergic signaling pathway. It contains two transmembrane domains at the N- and C-termini and a large, hydrophobic catalytic domain located in between. This gene affects oxidative stress as well as DNA damage and is a mediator …

**Accessions** — [HGNC:19745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19745) · Entrez [57089](https://www.ncbi.nlm.nih.gov/gene/57089) · UniProt [Q9NQZ7](https://www.uniprot.org/uniprotkb/Q9NQZ7) · Ensembl [ENSG00000198018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198018)

## Data

Gene col 12513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12513); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12513]; `tensor/DDL_lfc|DDL_z.npy` [12513]; `embed/gene_vectors.npy` [12513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12513 or target_col == 12513). Every well: [[ENTPD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTPD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
