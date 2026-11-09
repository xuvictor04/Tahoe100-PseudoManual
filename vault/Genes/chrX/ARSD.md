---
symbol: "ARSD"
type: "gene"
col: 130
ensembl_id: "ENSG00000006756"
name: "arylsulfatase D"
location: "Xp22.33"
module: 10
arm: "+"
pooled_cpm: 14.63
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 31
n_dd_up_clean: 9
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ARSD

*arylsulfatase D* — Xp22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.72× (z +12.5, q 6e-33, up in 26 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +4.7, q 3e-04, up in 17 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.281× (z -22.4, q 0e+00, down in 37 of 40 measured lines).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02086]] (+0.63, fdr 4e-05), [[CYB561A3]] (+0.63, fdr 7e-05), [[SRSF5]] (+0.63, fdr 3e-05); moves opposite to [[SH3PXD2B]] (-0.58, fdr 2e-04), [[MRPS34]] (-0.56, fdr 2e-04), [[CAMKK1]] (-0.55, fdr 7e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTSO]] → it (grade B ⚠); 1 goes from it, the strongest it → [[C2orf88]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +12.5 | 6e-33 | 26/32 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +12.2 | 1e-31 | 21/21 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +8.8 | 3e-16 | 21/28 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.7 | 3e-04 | 17/40 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +4.3 | 0.001 | 13/43 (PANC-1, BT-474, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.27×** | +4.3 | 0.001 | 18/44 (A498, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.001 | 13/44 (A498, A-172, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.61×** | +4.3 | 0.001 | 16/41 (A-427, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.003 | 14/40 (BT-474, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.035 | 9/41 (SK-MEL-2, A-172, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.035 | 8/43 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.035 | 11/44 (KATO III, A498, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.080 | 12/43 (HEC-1-A, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.281×** | -22.4 | 0e+00 | 37/40 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.236×** | -18.0 | 0e+00 | 41/44 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.245×** | -17.5 | 0e+00 | 38/43 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.259×** | -16.8 | 0e+00 | 41/43 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.334×** | -13.7 | 2e-40 | 42/44 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.369×** | -12.4 | 2e-33 | 36/44 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.379×** | -12.1 | 9e-32 | 30/39 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.405×** | -11.3 | 1e-27 | 34/38 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.418×** | -10.9 | 1e-25 | 36/43 (LS 180, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.404×** | -10.9 | 1e-25 | 32/42 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.453×** | -9.9 | 3e-21 | 31/40 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.461×** | -9.6 | 2e-20 | 32/42 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -9.4 | 3e-19 | 31/42 (J82, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.521×** | -7.7 | 7e-13 | 27/41 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.541×** | -7.7 | 7e-13 | 29/41 (RKO, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.340×** | -7.0 | 7e-11 | 31/43 (KATO III, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 36.2 | 3 (3 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.8) |
| [[COLO 205 (line)]] | alt | 35.1 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -16.1) |
| [[HT-29 (line)]] | alt | 29.6 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -18.0) |
| [[LS 180 (line)]] | wt | 30.4 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0797× (z -17.8) |
| [[KATO III (line)]] | alt | 43.7 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.88× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.115× (z -17.3) |
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.7) |
| [[RKO (line)]] | wt | 14.9 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0562× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.2) |
| [[A549 (line)]] | wt | 20.4 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.109× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.1) |
| [[BT-474 (line)]] | alt | 49.8 | 0 | 4 | — | [[Belinostat (drug)]] 0.5 µM 0.213× (z -11.8) |
| [[J82 (line)]] | alt | 17.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0613× (z -23.1) |
| [[LoVo (line)]] | wt | 11.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -15.0) |
| [[A-172 (line)]] | wt | 17.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.9) |
| [[A498 (line)]] | wt | 15.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.48× (z +8.5) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 5 µM 0.0544× (z -10.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.423× (z -8.6) |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0924× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 9.90 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.0657× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -11.8) |
| [[A-427 (line)]] | wt | 5.76 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0692× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0895× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -17.2) |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 5.13 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0880× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 7.82 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0646× (z -11.0) |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 6.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.60× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 9.62 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.7) |
| [[PANC-1 (line)]] | alt | 7.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.9) |
| [[SW1417 (line)]] | alt | 13.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.205× (z -8.7) |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02086]] | +0.63 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[CYB561A3]] | +0.63 | +0.42 / +0.37 | both halves | 7e-05 |  |
| [[SRSF5]] | +0.63 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[LINC01376]] | +0.63 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[IDNK]] | +0.62 | +0.41 / +0.38 | both halves | 7e-05 |  |
| [[NIPAL2]] | +0.62 | +0.46 / +0.25 | both halves | 4e-04 |  |
| [[TAFA2]] | +0.61 | +0.41 / +0.37 | both halves | 7e-05 |  |
| [[CRPPA]] | +0.61 | +0.35 / +0.37 | both halves | 1e-04 |  |
| [[PPP3CB-AS1]] | +0.61 | +0.40 / +0.35 | both halves | 1e-04 |  |
| [[WAC-AS1]] | +0.61 | +0.34 / +0.41 | both halves | 1e-04 |  |
| [[CYP4V2]] | +0.60 | +0.47 / +0.28 | both halves | 3e-04 |  |
| [[PBLD]] | +0.60 | +0.28 / +0.41 | both halves | 3e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3PXD2B]] | -0.58 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[MRPS34]] | -0.56 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[CAMKK1]] | -0.55 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[KIAA1328]] | -0.55 | -0.37 / -0.20 | both halves | 7e-04 |  |
| [[PUSL1]] | -0.53 | -0.24 / -0.20 | both halves | 7e-04 |  |
| [[GPATCH11]] | -0.53 | -0.22 / -0.36 | both halves | 6e-04 |  |
| [[TTBK2]] | -0.53 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[CFDP1]] | -0.53 | -0.40 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[CAMK2G]] | -0.52 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[NAA10]] ⚠ | -0.52 | -0.23 / -0.23 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[YIF1B]] | -0.52 | -0.22 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[PEDS1]] | -0.52 | -0.33 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSO]] | B | CTSO activity raises ARSD's level | lines that do not express CTSO (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without CTSO | 0.032 | ⚠ within organs, on part of the lines; also absent: ARHGAP31, SYTL2, FRG1-DT |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf88]] | C | ARSD activity lowers C2orf88's level | lines that do not express ARSD (4) vs lines expressing it (46) | 1.52× higher at baseline in the lines without ARSD | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MYH16, SGK2, SAT1; its own permutation p |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-0.6, 21.3); signed map (29.8, -21.8). **Vector** length 74.2, 16.4% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +12.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +4.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +4.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -11.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.0 | -13.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -17.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -10.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -5.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | arylsulfatase D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 — chrX:2,903,972-2,929,349 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASD |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 6 pathways, smallest: The activation of arylsulfatases; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

UniProt [P51689](https://www.uniprot.org/uniprotkb/P51689) carries no function annotation.

**Summary**, from NCBI Gene [414](https://www.ncbi.nlm.nih.gov/gene/414):

> The protein encoded by this gene is a member of the sulfatase family. Sulfatases are essential for the correct composition of bone and cartilage matrix. The encoded protein is postranslationally glycosylated and localized to the lysosome. This gene is located within a cluster of similar arylsulfatase genes on chromosome X. A related pseudogene has been identified in the pseudoautosomal region of chromosome Y. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:717) · Entrez [414](https://www.ncbi.nlm.nih.gov/gene/414) · UniProt [P51689](https://www.uniprot.org/uniprotkb/P51689) · Ensembl [ENSG00000006756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006756)

## Data

Gene col 130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 130); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 130]; `tensor/DDL_lfc|DDL_z.npy` [130]; `embed/gene_vectors.npy` [130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 130 or target_col == 130). Every well: [[ARSD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARSD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
