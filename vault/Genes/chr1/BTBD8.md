---
symbol: "BTBD8"
type: "gene"
col: 12103
ensembl_id: "ENSG00000189195"
name: "BTB domain containing 8"
location: "1p22.1"
module: 76
arm: "+"
pooled_cpm: 16.07
n_lines_expressing: 48
n_dd_up: 3
n_dd_down: 50
n_dd_up_clean: 3
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# BTBD8

*BTB domain containing 8* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Bimiralisib (drug)]] 5 µM: 1.81× (z +3.8, q 0.044, up in 14 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (18 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.178× (z -20.8, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALBP1]] (+0.57, fdr 3e-05), [[WDR48]] (+0.57, fdr 1e-04), [[UBXN7]] (+0.54, fdr 4e-05); moves opposite to [[UBE2G2]] (-0.49, fdr 3e-04), [[ATAD3B]] (-0.49, fdr 4e-05), [[SELENOI]] (-0.48, fdr 9e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12103.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | **1.81×** | +3.8 | 0.044 | 14/45 (HEC-1-A, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.044 | 14/45 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.044 | 13/45 (KATO III, LS 180, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | 1.70× | +3.4 | 0.10 | 11/44 (LS 180, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.31× | +3.3 | 0.10 | 14/45 (LS 180, KATO III, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.20 | 11/45 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.30× | +3.0 | 0.20 | 9/46 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12103.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.178×** | -20.8 | 0e+00 | 45/45 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.204×** | -19.1 | 0e+00 | 43/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.331×** | -18.8 | 0e+00 | 40/45 (Panc 03.27, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.220×** | -18.2 | 0e+00 | 44/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.279×** | -15.4 | 0e+00 | 41/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.314×** | -13.9 | 5e-42 | 42/45 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.355×** | -12.5 | 1e-33 | 38/44 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.380×** | -11.2 | 4e-27 | 37/40 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.543×** | -10.3 | 3e-23 | 33/44 (LOX-IMVI, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.441×** | -9.8 | 5e-21 | 35/45 (MIA PaCa-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.440×** | -9.5 | 2e-19 | 31/45 (NCI-H1792, A549, …) | rises with dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.456×** | -9.4 | 2e-19 | 36/45 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.478×** | -8.9 | 3e-17 | 34/45 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.259×** | -8.5 | 8e-16 | 36/45 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.259×** | -8.5 | 8e-16 | 35/44 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.470×** | -8.4 | 2e-15 | 33/46 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.282×** | -8.0 | 6e-14 | 36/44 (SW 900, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.297×** | -7.6 | 7e-13 | 32/44 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.436×** | -7.1 | 3e-11 | 36/46 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.380×** | -6.1 | 3e-08 | 27/42 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12103. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.1 | 0 | 17 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0249× (z -30.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0407× (z -26.4) |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 11 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0676× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0728× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 38.0 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0534× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -12.8) |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0446× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0724× (z -14.5) |
| [[LoVo (line)]] | wt | 19.7 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.169× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 21.8 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0806× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0860× (z -14.0) |
| [[A-427 (line)]] | wt | 24.6 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0791× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0654× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0773× (z -18.1) |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 6 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0634× (z -16.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -10.2) |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.151× (z -9.5) |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -11.1) |
| [[A549 (line)]] | wt | 18.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -16.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -11.5) |
| [[HCT15 (line)]] | alt | 36.7 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0244× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0297× (z -18.2) |
| [[HEC-1-A (line)]] | alt | 23.2 | 0 | 5 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -11.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0564× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0658× (z -11.6) |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0630× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.180× (z -15.5) |
| [[J82 (line)]] | alt | 9.62 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -11.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -10.9) |
| [[LS 180 (line)]] | wt | 24.2 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0735× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0885× (z -15.1) |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0868× (z -12.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -10.3) |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.155× (z -12.6) |
| [[SW48 (line)]] | wt | 21.0 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0424× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 20.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0673× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -10.2) |
| [[A498 (line)]] | wt | 15.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0852× (z -14.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 8.30 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0717× (z -11.4) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.114× (z -9.7) |
| [[RKO (line)]] | wt | 15.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0655× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0781× (z -11.9) |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0120× (z -23.8) |
| [[NCI-H460 (line)]] | wt | 7.00 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0418× (z -15.0) |
| [[AsPC-1 (line)]] | alt | 6.14 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0547× (z -10.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[BT-474 (line)]] | alt | 5.54 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0647× (z -8.8) |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0827× (z -11.8) |
| [[C32 (line)]] | wt | 7.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0917× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -10.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 31.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0422× (z -9.0) |
| [[A-172 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.88 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12103), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALBP1]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[WDR48]] | +0.57 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[UBXN7]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[PLEKHM3]] | +0.54 | +0.28 / +0.57 | both halves | 3e-04 |  |
| [[CCDC28A]] | +0.53 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[IFTAP]] | +0.52 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[C1orf115]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PHF3]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[SLU7]] | +0.49 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[YPEL2]] | +0.49 | +0.29 / +0.52 | both halves | 2e-04 |  |
| [[TNRC6B]] | +0.49 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[YPEL3]] | +0.49 | +0.38 / +0.52 | both halves | 7e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G2]] | -0.49 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[ATAD3B]] | -0.49 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[SELENOI]] | -0.48 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[CAPN15]] | -0.47 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[RNASEH1]] | -0.46 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ANKUB1]] | -0.46 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[TRNT1]] | -0.46 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[PUS1]] | -0.45 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[TIMM23B-AGAP6]] | -0.45 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[FUBP3]] | -0.44 | -0.19 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[STX16-NPEPL1]] | -0.44 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[ZNF587]] | -0.44 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[ACLY]] | -0.44 | -0.37 / -0.52 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BTBD8's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.486). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.7, -45.7); signed map (-15.9, 8.6). **Vector** length 69.8, 16.4% of its response variance represented; |z| ≥ 3 in 1,365 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -0.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +0.9 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +1.7 | +3.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[IQ 1 (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +1.3 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -13.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -8.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -5.8 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -6.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -8.5 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:92,080,305-92,184,725 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APache; previously KIAA1107 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5XKL5](https://www.uniprot.org/uniprotkb/Q5XKL5) (BTB/POZ domain-containing protein 8):

> Involved in clathrin-mediated endocytosis at the synapse. Plays a role in neuronal development and in synaptic vesicle recycling in mature neurons, a process required for normal synaptic transmission.

**Summary**, from NCBI Gene [284697](https://www.ncbi.nlm.nih.gov/gene/284697):

> Predicted to be involved in synaptic vesicle budding from endosome and synaptic vesicle endocytosis. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21019) · Entrez [284697](https://www.ncbi.nlm.nih.gov/gene/284697) · UniProt [Q5XKL5](https://www.uniprot.org/uniprotkb/Q5XKL5) · Ensembl [ENSG00000189195](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189195)

## Data

Gene col 12103: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12103); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12103, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12103]; `tensor/DDL_lfc|DDL_z.npy` [12103]; `embed/gene_vectors.npy` [12103]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12103 or target_col == 12103). Every well: [[BTBD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
