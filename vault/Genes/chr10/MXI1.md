---
symbol: "MXI1"
type: "gene"
col: 4142
ensembl_id: "ENSG00000119950"
name: "MAX interactor 1, dimerization protein"
location: "10q25.2"
module: 79
arm: "+"
pooled_cpm: 184.7
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 40
n_dd_up_clean: 5
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# MXI1

*MAX interactor 1, dimerization protein* — 10q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.28× (z +4.7, q 0.001, up in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Dimethyl fumarate (drug)]] 5 µM: 1.37× (z +4.1, q 0.013, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.252× (z -26.1, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM3A]] (+0.84, fdr 7e-06), [[INSIG2]] (+0.79, fdr 7e-06), [[RBPJ]] (+0.78, fdr 7e-06); moves opposite to [[GNL3L]] (-0.71, fdr 7e-06), [[ANAPC7]] (-0.67, fdr 7e-06), [[ARMC6]] (-0.66, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RAB20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.28×** | +4.7 | 0.001 | 32/47 (COLO 205, SNU-1, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.013 | 32/48 (CFPAC-1, HT-29, …) | top dose only | plate-row cell shift; position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.032 | 30/47 (SHP-77, SNU-1, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.032 | 24/47 (A-172, LoVo, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.032 | 34/47 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; position effect removed |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.032 | 32/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.080 | 22/47 (RPMI-7951, LoVo, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.18 | 20/48 (C32, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.252×** | -26.1 | 0e+00 | 47/47 (AsPC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.232×** | -19.6 | 0e+00 | 46/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.304×** | -15.4 | 0e+00 | 47/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.397×** | -11.9 | 2e-30 | 43/46 (CFPAC-1, HCT15, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.415×** | -11.3 | 1e-27 | 44/46 (CFPAC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.410×** | -11.0 | 2e-26 | 39/44 (CFPAC-1, NCI-H2347, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.442×** | -10.9 | 7e-26 | 43/48 (CFPAC-1, NCI-H2347, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.430×** | -10.8 | 1e-25 | 38/43 (CFPAC-1, SNU-423, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.493×** | -9.5 | 2e-19 | 47/47 (SW48, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.524×** | -8.6 | 3e-16 | 39/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.539×** | -8.3 | 7e-15 | 39/47 (CFPAC-1, SNU-423, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.567×** | -7.6 | 2e-12 | 45/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.629×** | -6.2 | 3e-08 | 33/47 (NCI-H2347, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.630×** | -5.8 | 2e-07 | 32/47 (HS-578T, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.647×** | -5.6 | 9e-07 | 40/47 (NCI-H2347, NCI-H1573, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.667×** | -5.4 | 2e-06 | 28/47 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -5.2 | 7e-06 | 36/47 (HT-29, HCT15, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.765×** | -5.0 | 1e-05 | 35/47 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.699×** | -4.8 | 5e-05 | 28/47 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.776×** | -4.8 | 5e-05 | 31/47 (NCI-H2347, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.514×** | -4.7 | 8e-05 | 41/47 (Hs 766T, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.517×** | -4.6 | 1e-04 | 36/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.558×** | -4.1 | 1e-03 | 38/47 (NCI-H23, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.730×** | -4.0 | 0.002 | 32/46 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.758×** | -3.7 | 0.004 | 27/47 (LS 180, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.62 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 173 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -21.8) |
| [[CFPAC-1 (line)]] | alt | 313 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -29.5) |
| [[AsPC-1 (line)]] | alt | 238 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0904× (z -32.8) |
| [[MIA PaCa-2 (line)]] | alt | 147 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0232× (z -38.6) |
| [[SNU-423 (line)]] | alt | 466 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -25.8) |
| [[hTERT-HPNE (line)]] | wt | 263 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.7) |
| [[Panc 03.27 (line)]] | alt | 146 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -19.6) |
| [[Hs 766T (line)]] | wt | 253 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -28.9) |
| [[HS-578T (line)]] | alt | 190 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -27.7) |
| [[LOX-IMVI (line)]] | wt | 305 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -22.8) |
| [[SW 900 (line)]] | alt | 224 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -26.2) |
| [[A-172 (line)]] | wt | 243 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 211 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -23.5) |
| [[PANC-1 (line)]] | alt | 129 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -28.1) |
| [[RPMI-7951 (line)]] | alt | 201 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -22.3) |
| [[HCT15 (line)]] | alt | 288 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -27.8) |
| [[HT-29 (line)]] | alt | 205 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -27.4) |
| [[NCI-H1573 (line)]] | alt | 251 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0820× (z -20.0) |
| [[SNU-1 (line)]] | wt | 231 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.1) |
| [[C-33 A (line)]] | alt | 220 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.375× (z -10.5) |
| [[KATO III (line)]] | alt | 138 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 127 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -21.3) |
| [[SHP-77 (line)]] | alt | 201 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -19.4) |
| [[SW1417 (line)]] | alt | 112 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -16.1) |
| [[A-427 (line)]] | wt | 109 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.420× (z -12.8) |
| [[A549 (line)]] | wt | 157 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -18.9) |
| [[CHP-212 (line)]] | wt | 235 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.8) |
| [[COLO 205 (line)]] | alt | 180 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -24.2) |
| [[NCI-H1792 (line)]] | alt | 221 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 252 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -20.4) |
| [[SW48 (line)]] | wt | 231 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -16.6) |
| [[H4 (line)]] | wt | 275 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -15.0) |
| [[LoVo (line)]] | wt | 152 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -20.4) |
| [[NCI-H2030 (line)]] | alt | 78.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -13.6) |
| [[SW480 (line)]] | alt | 110 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -18.1) |
| [[AN3 CA (line)]] | alt | 310 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0503× (z -21.5) |
| [[HOP62 (line)]] | alt | 159 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -17.7) |
| [[LS 180 (line)]] | wt | 253 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 216 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -11.0) |
| [[J82 (line)]] | alt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -11.2) |
| [[SW 1088 (line)]] | alt | 249 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -13.4) |
| [[A498 (line)]] | wt | 67.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 51.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 227 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM3A]] | +0.84 | +0.83 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[INSIG2]] | +0.79 | +0.86 / +0.71 | both halves | 7e-06 |  |
| [[RBPJ]] | +0.78 | +0.82 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[SAP30-DT]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[FAM13A]] | +0.77 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.75 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[PDK3]] | +0.74 | +0.83 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[P4HA1]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[HERC3]] | +0.72 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.72 | +0.79 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[WDR45B]] | +0.71 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[ZNF395]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL3L]] | -0.71 | -0.69 / -0.67 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.67 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[ARMC6]] | -0.66 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[AVEN]] | -0.64 | -0.72 / -0.52 | both halves | 1e-05 |  |
| [[UTP20]] | -0.64 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[PUS1]] | -0.62 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[WDR4]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[PCBD2]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[DHX37]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[BICD1]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity raises MXI1's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without RAB20 | 0.034 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.875). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.7, -17.1); signed map (-34.6, 24.0). **Vector** length 152, 61.6% of its response variance represented; |z| ≥ 3 in 1,562 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.72 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.9 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.8 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.9 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.3 | -8.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.9 | -8.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.6 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.4 | +3.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +4.4 | +3.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +4.3 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.2 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.4 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -15.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -5.5 | -7.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.8 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.8 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | MAX interactor 1, dimerization protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.2 — chr10:110,207,605-110,287,365 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MXD2, MAD2, MXI, bHLHc11 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; MAX dimerization proteins |
| Hallmark sets | HEME_METABOLISM, GLYCOLYSIS, HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [P50539](https://www.uniprot.org/uniprotkb/P50539) (Max-interacting protein 1):

> Transcriptional repressor. MXI1 binds with MAX to form a sequence-specific DNA-binding protein complex which recognizes the core sequence 5'-CAC[GA]TG-3'. MXI1 thus antagonizes MYC transcriptional activity by competing for MAX.

**Summary**, from NCBI Gene [4601](https://www.ncbi.nlm.nih.gov/gene/4601):

> Expression of the c-myc gene, which produces an oncogenic transcription factor, is tightly regulated in normal cells but is frequently deregulated in human cancers. The protein encoded by this gene is a transcriptional repressor thought to negatively regulate MYC function, and is therefore a potential tumor suppressor. This protein inhibits the transcriptional activity of MYC by competing for MAX, another basic helix-loop-helix protein that binds to MYC and is required for its function. Defects …

**Accessions** — [HGNC:7534](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7534) · Entrez [4601](https://www.ncbi.nlm.nih.gov/gene/4601) · UniProt [P50539](https://www.uniprot.org/uniprotkb/P50539) · Ensembl [ENSG00000119950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119950)

## Data

Gene col 4142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4142); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4142]; `tensor/DDL_lfc|DDL_z.npy` [4142]; `embed/gene_vectors.npy` [4142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4142 or target_col == 4142). Every well: [[MXI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MXI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
