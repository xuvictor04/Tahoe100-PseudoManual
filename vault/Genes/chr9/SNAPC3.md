---
symbol: "SNAPC3"
type: "gene"
col: 9047
ensembl_id: "ENSG00000164975"
name: "small nuclear RNA activating complex polypeptide 3"
location: "9p22.3"
module: 164
arm: "+"
pooled_cpm: 79.02
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# SNAPC3

*small nuclear RNA activating complex polypeptide 3* — 9p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Radotinib (drug)]] 5 µM: 1.17× (z +4.1, q 0.020, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.249× (z -35.7, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL6]] (+0.79, fdr 7e-06), [[ATG4C]] (+0.78, fdr 1e-05), [[PEX3]] (+0.78, fdr 7e-06); moves opposite to [[MSRA]] (-0.72, fdr 7e-06), [[AVEN]] (-0.71, fdr 4e-05), [[DDX5]] (-0.70, fdr 1e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.1 | 0.020 | 18/48 (RKO, RPMI-7951, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.48×** | +3.7 | 0.052 | 23/48 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 1.41× | +3.3 | 0.19 | 20/49 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.19× | +3.1 | 0.26 | 15/49 (LS 180, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.0 | 0.26 | 7/48 (HEC-1-A, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.249×** | -35.7 | 0e+00 | 48/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.419×** | -22.3 | 0e+00 | 49/49 (HOP62, CHP-212, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.357×** | -18.7 | 0e+00 | 46/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.345×** | -18.6 | 0e+00 | 47/48 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.510×** | -11.7 | 9e-30 | 43/47 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -9.6 | 8e-20 | 34/43 (SW48, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -9.3 | 1e-18 | 43/48 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.609×** | -9.0 | 2e-17 | 40/49 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.621×** | -8.0 | 8e-14 | 31/45 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -7.4 | 5e-12 | 39/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -6.9 | 3e-10 | 38/50 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.701×** | -6.4 | 6e-09 | 34/48 (HOP62, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.711×** | -6.2 | 3e-08 | 28/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -6.0 | 7e-08 | 31/48 (HOP62, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.718×** | -6.0 | 7e-08 | 32/48 (NCI-H460, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.739×** | -5.3 | 5e-06 | 30/48 (LS 180, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.765×** | -4.8 | 4e-05 | 31/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.771×** | -4.7 | 9e-05 | 29/48 (Panc 03.27, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.798×** | -4.1 | 0.001 | 25/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.793×** | -3.9 | 0.002 | 22/47 (NCI-H2347, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.9 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -24.9) |
| [[A-172 (line)]] | wt | 84.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -26.8) |
| [[C32 (line)]] | wt | 69.2 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -25.4) |
| [[HOP62 (line)]] | alt | 115 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -41.6) |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -25.3) |
| [[LOX-IMVI (line)]] | wt | 159 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -30.8) |
| [[SK-MEL-2 (line)]] | alt | 91.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -27.3) |
| [[A498 (line)]] | wt | 81.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -20.5) |
| [[HS-578T (line)]] | alt | 117 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -31.5) |
| [[J82 (line)]] | alt | 90.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -21.7) |
| [[LoVo (line)]] | wt | 68.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -24.4) |
| [[NCI-H1792 (line)]] | alt | 79.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -29.6) |
| [[NCI-H2347 (line)]] | alt | 60.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -24.4) |
| [[Panc 03.27 (line)]] | alt | 88.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -15.8) |
| [[SNU-423 (line)]] | alt | 86.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -26.5) |
| [[SW 900 (line)]] | alt | 80.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -20.9) |
| [[AsPC-1 (line)]] | alt | 34.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -18.7) |
| [[H4 (line)]] | wt | 116 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -29.2) |
| [[Hs 766T (line)]] | wt | 90.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -26.8) |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -23.5) |
| [[SNU-1 (line)]] | wt | 125 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 63.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -20.8) |
| [[COLO 205 (line)]] | alt | 94.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -18.2) |
| [[HepG2_C3A (line)]] | wt | 61.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 77.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -13.9) |
| [[PANC-1 (line)]] | alt | 45.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -23.7) |
| [[SW 1088 (line)]] | alt | 92.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.5) |
| [[A549 (line)]] | wt | 95.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -16.2) |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -12.0) |
| [[HT-29 (line)]] | alt | 79.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -16.8) |
| [[KATO III (line)]] | alt | 60.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -12.6) |
| [[LS 180 (line)]] | wt | 137 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.543× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 56.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -21.7) |
| [[NCI-H2030 (line)]] | alt | 44.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -18.0) |
| [[SW1417 (line)]] | alt | 61.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.5) |
| [[SW480 (line)]] | alt | 61.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -16.6) |
| [[A-427 (line)]] | wt | 50.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.8) |
| [[CHP-212 (line)]] | wt | 129 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -19.5) |
| [[RKO (line)]] | wt | 56.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.4) |
| [[SHP-77 (line)]] | alt | 148 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.337× (z -11.0) |
| [[SW48 (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0694× (z -22.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 86.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.1) |
| [[HCT15 (line)]] | alt | 170 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 78.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -21.8) |
| [[NCI-H596 (line)]] | alt | 87.5 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.131× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 56.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0506× (z -14.5) |
| [[C-33 A (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | +0.79 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.78 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[PEX3]] | +0.78 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[PDK3]] | +0.77 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.77 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[MMS19]] | +0.77 | +0.81 / +0.60 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.76 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.76 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.74 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[RAB3A]] | +0.74 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[YIF1B]] | +0.73 | +0.69 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSRA]] | -0.72 | -0.70 / -0.60 | both halves | 7e-06 |  |
| [[AVEN]] | -0.71 | -0.73 / -0.42 | both halves | 4e-05 |  |
| [[DDX5]] | -0.70 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[ARAP2]] | -0.69 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[PRRC2B]] | -0.67 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.67 | -0.69 / -0.38 | both halves | 6e-05 |  |
| [[TRIP12]] | -0.67 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | -0.67 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[FKRP]] | -0.65 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[PARVA]] | -0.65 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | -0.65 | -0.62 / -0.39 | both halves | 6e-05 |  |
| [[ST7L]] | -0.64 | -0.67 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SNAPC3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.848). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.0, -13.6); signed map (-36.6, 21.9). **Vector** length 127, 40.8% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +7.1 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.5 | -4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.3 | +4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | -0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.9 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.8 | -18.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -35.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -18.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.3 | -4.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.3 | -3.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear RNA activating complex polypeptide 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.3 — chr9:15,422,734-15,465,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNAP50, PTFbeta, MGC33124, MGC132011 |
| Gene groups (HGNC) | SNAP complex |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 3 Promoter; RNA Polymerase III Transcription Initiation; RNA Polymerase III Abortive And Retractive Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92966](https://www.uniprot.org/uniprotkb/Q92966) (snRNA-activating protein complex subunit 3):

> Part of the SNAPc complex required for the transcription of both RNA polymerase II and III small-nuclear RNA genes. Binds to the proximal sequence element (PSE), a non-TATA-box basal promoter element common to these 2 types of genes. Recruits TBP and BRF2 to the U6 snRNA TATA box.

**Summary**, from NCBI Gene [6619](https://www.ncbi.nlm.nih.gov/gene/6619):

> Predicted to enable RNA polymerase III type 3 promoter sequence-specific DNA binding activity and bent DNA binding activity. Predicted to contribute to RNA polymerase II cis-regulatory region sequence-specific DNA binding activity and core promoter sequence-specific DNA binding activity. Predicted to be involved in snRNA transcription by RNA polymerase II and snRNA transcription by RNA polymerase III. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11136) · Entrez [6619](https://www.ncbi.nlm.nih.gov/gene/6619) · UniProt [Q92966](https://www.uniprot.org/uniprotkb/Q92966) · Ensembl [ENSG00000164975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164975)

## Data

Gene col 9047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9047); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9047]; `tensor/DDL_lfc|DDL_z.npy` [9047]; `embed/gene_vectors.npy` [9047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9047 or target_col == 9047). Every well: [[SNAPC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAPC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
