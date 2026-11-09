---
symbol: "ZNF25"
type: "gene"
col: 10606
ensembl_id: "ENSG00000175395"
name: "zinc finger protein 25"
location: "10p11.21"
module: 175
arm: "+"
pooled_cpm: 13.17
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 27
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# ZNF25

*zinc finger protein 25* — 10p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 0.5 µM: 1.35× (z +4.8, q 0.001, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.234× (z -22.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF343]] (+0.65, fdr 1e-05), [[ZNF449]] (+0.65, fdr 1e-05), [[ERMARD]] (+0.62, fdr 1e-05); moves opposite to [[LIPH]] (-0.53, fdr 3e-05), [[TCF7L2]] (-0.52, fdr 5e-05), [[SMURF1]] (-0.51, fdr 6e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 0.001 | 16/48 (A-172, SW48, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.4 | 0.004 | 15/48 (A-172, LS 180, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.027 | 16/45 (SW1417, HT-29, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.027 | 4/46 (NCI-H1573, NCI-H23, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.100 | 8/46 (NCI-H2030, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.21× | +3.0 | 0.22 | 4/46 (SW 900, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.234×** | -22.9 | 0e+00 | 46/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.245×** | -22.2 | 0e+00 | 40/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.261×** | -21.2 | 0e+00 | 45/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.388×** | -21.1 | 0e+00 | 39/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.285×** | -19.8 | 0e+00 | 42/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.213×** | -12.7 | 4e-35 | 34/44 (RKO, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.469×** | -11.9 | 7e-31 | 35/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.470×** | -11.9 | 1e-30 | 36/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.471×** | -11.9 | 1e-30 | 33/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.471×** | -11.8 | 1e-30 | 32/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.252×** | -11.3 | 4e-28 | 39/47 (PANC-1, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.473×** | -11.3 | 4e-28 | 33/47 (PANC-1, RPMI-7951, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.497×** | -11.0 | 2e-26 | 34/48 (A-172, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.515×** | -10.1 | 4e-22 | 28/42 (PANC-1, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.530×** | -10.0 | 7e-22 | 37/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.547×** | -9.5 | 8e-20 | 29/47 (C32, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.561×** | -9.1 | 3e-18 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.588×** | -7.9 | 9e-14 | 31/46 (HEC-1-A, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.662×** | -6.5 | 3e-09 | 25/45 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.759×** | -6.1 | 3e-08 | 20/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.706×** | -3.9 | 0.002 | 11/48 (MIA PaCa-2, SW 900, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.6 | 0 | 14 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0856× (z -23.4) |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 11 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0486× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.4) |
| [[A-427 (line)]] | wt | 28.3 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.157× (z -13.7) |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 8 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0397× (z -21.2) |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0741× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.8) |
| [[C32 (line)]] | wt | 12.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -14.2) |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0913× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -12.4) |
| [[SW 900 (line)]] | alt | 18.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -17.2) |
| [[A-172 (line)]] | wt | 36.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.229× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0567× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.146× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -15.2) |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0989× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 19.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -14.5) |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 7.15 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0774× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.119× (z -10.7) |
| [[RKO (line)]] | wt | 19.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -13.0) |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.0667× (z -10.2) |
| [[SW480 (line)]] | alt | 5.82 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.122× (z -11.4) |
| [[A498 (line)]] | wt | 16.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -14.6) |
| [[H4 (line)]] | wt | 13.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0369× (z -12.7) |
| [[J82 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.211× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~51% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.7) |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.106× (z -11.4) |
| [[A549 (line)]] | wt | 13.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -13.7) |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0955× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 7.53 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 4.95 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0419× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 6.22 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.207× (z -8.5) |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.132× (z -9.2) |
| [[SW1417 (line)]] | alt | 6.25 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.100× (z -9.4) |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF343]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 | same gene group |
| [[ZNF449]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 | same gene group |
| [[ERMARD]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[NADK2]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ACAD11]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[DDHD2]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ZNF18]] | +0.59 | +0.59 / +0.57 | both halves | 9e-06 | same gene group |
| [[UBA5]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[C3orf33]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ZNF550]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 | same gene group |
| [[PMS2]] | +0.56 | +0.51 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIPH]] | -0.53 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[TCF7L2]] | -0.52 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[SMURF1]] | -0.51 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[CATSPERB]] | -0.51 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[B3GNT3]] | -0.49 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[MID1]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CLIC5]] | -0.49 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[TMC5]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[STAU2]] | -0.48 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[NECTIN2]] | -0.48 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[ACTN4]] | -0.48 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[ARHGAP42]] | -0.48 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity lowers ZNF25's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.12× higher at baseline in the lines without B3GNT3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[CLIC5]] | B | CLIC5 activity lowers ZNF25's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.16× higher at baseline in the lines without CLIC5 | 6e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[TMEM45B]] | B | TMEM45B activity lowers ZNF25's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.01× higher at baseline in the lines without TMEM45B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[CATSPERB]] | B | CATSPERB activity lowers ZNF25's level | lines that do not express CATSPERB (30) vs lines expressing it (20) | 1.92× higher at baseline in the lines without CATSPERB | 0.002 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[B3GNT3]] | B | B3GNT3 activity weakens ZNF25's drug response | lines that do not express B3GNT3 (31) vs lines expressing it (17) | the lines without B3GNT3 respond 1.48× as strongly (z diff -2.53); strongest at Digitoxin 5 µM: 0.18x vs 0.34x (z diff -3.9) | 0.016 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; target measured in part of the lines; artifact flags |
| [[LIPH]] | B | LIPH activity lowers ZNF25's level | lines that do not express LIPH (27) vs lines expressing it (23) | 1.75× higher at baseline in the lines without LIPH | 0.021 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[FAM216A]] | B | FAM216A activity raises ZNF25's level | lines that do not express FAM216A (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without FAM216A | 0.023 | ⚠ within organs, on part of the lines; also absent: EPB41L2, CEP85L, P3H1; maybe low, not absent |
| [[TMEM45B]] | B | TMEM45B activity weakens ZNF25's drug response | lines that do not express TMEM45B (32) vs lines expressing it (16) | the lines without TMEM45B respond 1.56× as strongly (z diff -2.62); strongest at Homoharringtonine 0.5 µM: 0.33x vs 0.68x (z diff -3.8) | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; target measured in part of the lines; artifact flags |
| [[CLIC5]] | B | CLIC5 activity weakens ZNF25's drug response | lines that do not express CLIC5 (37) vs lines expressing it (11) | the lines without CLIC5 respond 1.63× as strongly (z diff -2.74); strongest at Digitoxin 5 µM: 0.20x vs 0.37x (z diff -4.0) | 0.036 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; target measured in part of the lines; artifact flags |
| [[C3orf18]] | B | C3orf18 activity raises ZNF25's level | lines that do not express C3orf18 (10) vs lines expressing it (40) | 1.41× lower at baseline in the lines without C3orf18 | 0.042 | ⚠ within organs, on part of the lines; also absent: TMCC2, SELENOM; maybe low, not absent |
| [[TMC5]] | B | TMC5 activity lowers ZNF25's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 1.76× higher at baseline in the lines without TMC5 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.7, 19.0); signed map (-31.5, -21.2). **Vector** length 70.4, 13.6% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.7 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -22.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.4 | -19.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -22.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -21.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.21 — chr10:37,949,573-37,976,647 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX19, FLJ31890, Zfp9 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17030](https://www.uniprot.org/uniprotkb/P17030) (Zinc finger protein 25):

> Transcriptional repressor that plays a role in the proper differentiation of skeletal stem cells into osteoblasts.

**Summary**, from NCBI Gene [219749](https://www.ncbi.nlm.nih.gov/gene/219749):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13043) · Entrez [219749](https://www.ncbi.nlm.nih.gov/gene/219749) · UniProt [P17030](https://www.uniprot.org/uniprotkb/P17030) · Ensembl [ENSG00000175395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175395)

## Data

Gene col 10606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10606); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10606]; `tensor/DDL_lfc|DDL_z.npy` [10606]; `embed/gene_vectors.npy` [10606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10606 or target_col == 10606). Every well: [[ZNF25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
