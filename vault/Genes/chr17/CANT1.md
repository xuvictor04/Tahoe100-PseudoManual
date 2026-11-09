---
symbol: "CANT1"
type: "gene"
col: 10086
ensembl_id: "ENSG00000171302"
name: "calcium activated nucleotidase 1"
location: "17q25.3"
module: 16
arm: "+"
pooled_cpm: 41.89
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CANT1

*calcium activated nucleotidase 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.64× (z +5.0, q 3e-04, up in 24 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.99×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 1.73×); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 7.74×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.522× (z -17.8, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP7]] (+0.63, fdr 1e-05), [[SNAP47]] (+0.60, fdr 4e-05), [[EIF1AD]] (+0.59, fdr 1e-05); moves opposite to [[CYB5D2]] (-0.56, fdr 5e-05), [[TSTD3]] (-0.55, fdr 2e-04), [[UBXN2A]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10086.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 1.99×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 1.73×); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 7.74×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +5.0 | 3e-04 | 24/49 (BT-474, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.22×** | +3.9 | 0.025 | 19/46 (HS-578T, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.20×** | +3.6 | 0.063 | 19/47 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.17× | +3.1 | 0.24 | 21/48 (SNU-423, Panc 03.27, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -17.8 | 0e+00 | 43/48 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.467×** | -14.7 | 0e+00 | 41/45 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.529×** | -11.8 | 4e-30 | 32/40 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.566×** | -10.2 | 3e-22 | 31/41 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -10.2 | 3e-22 | 40/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.607×** | -9.7 | 4e-20 | 36/47 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -8.9 | 4e-17 | 33/47 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.728×** | -8.7 | 3e-16 | 28/47 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -8.3 | 4e-15 | 35/47 (SK-MEL-2, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.642×** | -8.2 | 1e-14 | 33/48 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.673×** | -7.6 | 1e-12 | 30/48 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -7.4 | 5e-12 | 30/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.676×** | -7.3 | 2e-11 | 38/47 (A498, NCI-H2030, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -6.9 | 2e-10 | 32/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.720×** | -6.3 | 8e-09 | 30/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.735×** | -5.9 | 1e-07 | 27/48 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.760×** | -5.3 | 4e-06 | 27/48 (PANC-1, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.800×** | -4.1 | 0.001 | 18/47 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.888× | -3.2 | 0.036 | 14/48 (RPMI-7951, RKO, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.894× | -3.0 | 0.084 | 9/48 (LoVo, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 73.7 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0629× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -16.9) |
| [[KATO III (line)]] | alt | 80.9 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -20.5) |
| [[LoVo (line)]] | wt | 31.4 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -12.3) |
| [[A498 (line)]] | wt | 56.0 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -11.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 40.2 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 90.5 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.338× (z -11.7) |
| [[A549 (line)]] | wt | 66.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.409× (z -9.2) |
| [[COLO 205 (line)]] | alt | 59.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -14.7) |
| [[HCT15 (line)]] | alt | 54.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 53.5 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -20.0) |
| [[A-427 (line)]] | wt | 39.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -14.6) |
| [[H4 (line)]] | wt | 61.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -11.9) |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 38.7 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 34.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0625× (z -24.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 55.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 48.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.0) |
| [[PANC-1 (line)]] | alt | 48.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -12.1) |
| [[SW480 (line)]] | alt | 36.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0599× (z -33.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 42.3 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 7.74× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 36.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 34.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 51.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -12.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 26.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 35.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.7) |
| [[AN3 CA (line)]] | alt | 29.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -9.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 31.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.3) |
| [[HT-29 (line)]] | alt | 34.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 31.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -9.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 36.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.234× (z -9.2) ⚠ toxic |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP7]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SNAP47]] | +0.60 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[EIF1AD]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RIC8A]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[BCKDK]] | +0.58 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[DNAJC14]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PRPF4]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[POLR3A]] | +0.56 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[TOR4A]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[WDR55]] | +0.54 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[MAP1S]] | +0.53 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[SLC39A3]] | +0.53 | +0.38 / +0.44 | both halves | 6e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB5D2]] | -0.56 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[TSTD3]] | -0.55 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[UBXN2A]] | -0.53 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[KAT2B]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[DNAJC27-AS1]] | -0.51 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[ENO4]] | -0.51 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[MROH8]] | -0.51 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[NR1D2]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[ANXA2R-AS1]] | -0.51 | -0.46 / -0.24 | both halves | 4e-04 |  |
| [[PNISR]] | -0.51 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[RCOR3]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MTUS1-DT]] | -0.49 | -0.47 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CANT1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.167). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.3, -11.5); signed map (-14.8, -28.9). **Vector** length 113, 29.6% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +6.1 | +3.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +5.9 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.9 | +1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +0.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.6 | -14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -17.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -8.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -11.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.7 | -7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium activated nucleotidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,991,716-79,009,867 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SHAPY, SCAN-1 |
| Hallmark sets | DNA_REPAIR, ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVQ1](https://www.uniprot.org/uniprotkb/Q8WVQ1) (Soluble calcium-activated nucleotidase 1):

> Calcium-dependent nucleotidase with a preference for ribonucleosides diphosphate UDP, GDP and IDP, while having very low activity towards ADP and CDP. In vitro, it can also act with low or negligible efficiency on ribonucletides triphosphate UTP, GTP, ITP, ATP and CTP. Does not hydrolyze AMP and GMP. Involved in proteoglycan synthesis.

**Summary**, from NCBI Gene [124583](https://www.ncbi.nlm.nih.gov/gene/124583):

> This protein encoded by this gene belongs to the apyrase family. It functions as a calcium-dependent nucleotidase with a preference for UDP. Mutations in this gene are associated with Desbuquois dysplasia with hand anomalies. Alternatively spliced transcript variants have been noted for this gene.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:19721](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19721) · Entrez [124583](https://www.ncbi.nlm.nih.gov/gene/124583) · UniProt [Q8WVQ1](https://www.uniprot.org/uniprotkb/Q8WVQ1) · Ensembl [ENSG00000171302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171302)

## Data

Gene col 10086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10086); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10086]; `tensor/DDL_lfc|DDL_z.npy` [10086]; `embed/gene_vectors.npy` [10086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10086 or target_col == 10086). Every well: [[CANT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CANT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
