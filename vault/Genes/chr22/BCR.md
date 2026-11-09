---
symbol: "BCR"
type: "gene"
col: 11849
ensembl_id: "ENSG00000186716"
name: "BCR activator of RhoGEF and GTPase"
location: "22q11.23"
module: 77
arm: "+"
pooled_cpm: 47.25
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# BCR

*BCR activator of RhoGEF and GTPase* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.44× (z +7.9, q 2e-12, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.501× (z -21.1, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITPK1]] (+0.73, fdr 7e-06), [[ATG16L1]] (+0.70, fdr 7e-06), [[LPCAT4]] (+0.67, fdr 1e-05); moves opposite to [[LINC00944]] (-0.66, fdr 2e-05), [[THAP2]] (-0.64, fdr 7e-05), [[LINC02100]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[KRT6A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +7.9 | 2e-12 | 26/46 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.38×** | +7.0 | 9e-10 | 25/46 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.31×** | +5.9 | 7e-07 | 23/46 (PANC-1, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +5.4 | 9e-06 | 22/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +4.7 | 2e-04 | 21/46 (HOP62, SW1417, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +4.6 | 4e-04 | 21/46 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.001 | 19/46 (SW48, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.19× | +3.7 | 0.014 | 14/46 (PANC-1, A549, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +3.3 | 0.069 | 13/46 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.071 | 8/47 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.087 | 15/47 (Panc 03.27, SW1417, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.097 | 14/45 (LoVo, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11849.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.501×** | -21.1 | 0e+00 | 41/45 (NCI-H2347, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.591×** | -16.0 | 0e+00 | 38/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.607×** | -10.8 | 9e-25 | 33/46 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -9.8 | 2e-20 | 25/37 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.631×** | -8.9 | 5e-17 | 28/46 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -8.4 | 4e-15 | 26/46 (HS-578T, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.695×** | -7.8 | 4e-13 | 24/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -7.2 | 3e-11 | 24/47 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -7.2 | 5e-11 | 27/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.713×** | -6.5 | 4e-09 | 22/39 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.750×** | -6.2 | 3e-08 | 26/46 (NCI-H460, LoVo, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.825×** | -5.8 | 2e-07 | 21/46 (Panc 03.27, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.782×** | -5.3 | 5e-06 | 20/45 (NCI-H460, C32, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.809×** | -4.6 | 2e-04 | 14/47 (NCI-H1573, NCI-H1792, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.797×** | -4.4 | 4e-04 | 17/45 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.823×** | -4.2 | 0.001 | 17/45 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.828×** | -4.0 | 0.002 | 17/46 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.847× | -3.8 | 0.005 | 16/47 (NCI-H1573, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.870× | -3.5 | 0.012 | 13/46 (NCI-H1573, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.839× | -3.4 | 0.019 | 12/45 (NCI-H1573, AsPC-1, …) | two highest doses |  |
| [[AZD-7648 (drug)]] 5 µM |  | **0.746×** | -3.3 | 0.026 | 10/45 (SW1417, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.852× | -3.1 | 0.046 | 10/45 (NCI-H1573, SW 1271, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 89.9 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -25.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 56.2 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -24.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -17.2) |
| [[C32 (line)]] | wt | 34.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -17.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.182× (z -13.1) |
| [[HS-578T (line)]] | alt | 47.4 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -19.3) |
| [[A498 (line)]] | wt | 36.5 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.355× (z -12.1) |
| [[LoVo (line)]] | wt | 68.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -15.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.446× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 59.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -17.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 140 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.112× (z -13.1) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.512× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 59.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 54.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -10.5) |
| [[LS 180 (line)]] | wt | 84.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 46.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.5) |
| [[SW480 (line)]] | alt | 38.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 63.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -14.0) |
| [[Hs 766T (line)]] | wt | 129 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 78.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -22.4) |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.4) |
| [[A-427 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AN3 CA (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -10.4) |
| [[J82 (line)]] | alt | 21.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.0) |
| [[KATO III (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 44.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -12.4) |
| [[SNU-1 (line)]] | wt | 45.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.386× (z -8.8) |
| [[SW1417 (line)]] | alt | 71.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -14.2) |
| [[A-172 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 90.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPK1]] | +0.73 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[ATG16L1]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[LPCAT4]] | +0.67 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[CYRIB]] | +0.64 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[ACOT7]] | +0.64 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[EPHB4]] | +0.63 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[BRF1]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[NR2C1]] | +0.62 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[FBXW2]] | +0.62 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[MPRIP]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 | same gene group |
| [[SLC45A4]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[TMEM201]] | +0.61 | +0.45 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00944]] | -0.66 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[THAP2]] | -0.64 | -0.63 / -0.38 | both halves | 7e-05 |  |
| [[LINC02100]] | -0.62 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[DNAI4]] | -0.62 | -0.64 / -0.32 | both halves | 2e-04 |  |
| [[METTL6]] | -0.61 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[CGGBP1]] | -0.61 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[ZC3H6]] | -0.61 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[PATL2]] | -0.61 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[ZNF563]] | -0.61 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[RIPK2-DT]] | -0.61 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[JAM2]] | -0.60 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.60 | -0.70 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT6A]] | B | KRT6A activity raises BCR's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.31× lower at baseline in the lines without KRT6A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[GJB3]] | B | GJB3 activity raises BCR's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 2.18× lower at baseline in the lines without GJB3 | 0.004 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[FERMT1]] | B | FERMT1 activity raises BCR's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 2.04× lower at baseline in the lines without FERMT1 | 0.018 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN |
| [[PDE9A]] | B | PDE9A activity raises BCR's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 1.86× lower at baseline in the lines without PDE9A | 0.079 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[HDAC6]] | B | HDAC6 activity lowers BCR's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers BCR's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TENT5A]] | B | TENT5A activity lowers BCR's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 1.04× higher at baseline in the lines without TENT5A | 0.0999 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[PRR5]] | C | PRR5 activity raises BCR's level | lines that do not express PRR5 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without PRR5 | 0.098 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NECTIN1, PLEKHG3, SNED1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (17.2, 7.2); signed map (-10.8, 42.2). **Vector** length 112, 28.6% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +7.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +5.4 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.4 | +5.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | +4.2 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.1 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -21.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.7 | -16.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -10.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -8.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -2.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.8 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | BCR activator of RhoGEF and GTPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:23,179,704-23,318,037 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D22S662, CML, PHL, ALL; previously D22S11, BCR1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; C2 domain containing; My-T-BRC complex; Atypical protein kinase families; BCR kinase family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 15 pathways, smallest: Signaling by cytosolic FGFR1 fusion mutants; FGFR1 mutant receptor activation; Signaling by FGFR1 in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [P11274](https://www.uniprot.org/uniprotkb/P11274) (Breakpoint cluster region protein):

> Protein with a unique structure having two opposing regulatory activities toward small GTP-binding proteins. The C-terminus is a GTPase-activating protein (GAP) domain which stimulates GTP hydrolysis by RAC1, RAC2 and CDC42. Accelerates the intrinsic rate of GTP hydrolysis of RAC1 or CDC42, leading to down-regulation of the active GTP-bound form. The central Dbl homology (DH) domain functions as guanine nucleotide exchange factor (GEF) that modulates the GTPases CDC42, RHOA and RAC1. Promotes …

**Summary**, from NCBI Gene [613](https://www.ncbi.nlm.nih.gov/gene/613):

> A reciprocal translocation between chromosomes 22 and 9 produces the Philadelphia chromosome, which is often found in patients with chronic myelogenous leukemia. The chromosome 22 breakpoint for this translocation is located within the BCR gene. The translocation produces a fusion protein which is encoded by sequence from both BCR and ABL, the gene at the chromosome 9 breakpoint. Although the BCR-ABL fusion protein has been extensively studied, the function of the normal BCR gene product is not …

**Accessions** — [HGNC:1014](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1014) · Entrez [613](https://www.ncbi.nlm.nih.gov/gene/613) · UniProt [P11274](https://www.uniprot.org/uniprotkb/P11274) · Ensembl [ENSG00000186716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186716)

## Data

Gene col 11849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11849); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11849]; `tensor/DDL_lfc|DDL_z.npy` [11849]; `embed/gene_vectors.npy` [11849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11849 or target_col == 11849). Every well: [[BCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
