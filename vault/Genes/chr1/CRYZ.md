---
symbol: "CRYZ"
type: "gene"
col: 3840
ensembl_id: "ENSG00000116791"
name: "crystallin zeta"
location: "1p31.1"
module: 25
arm: "+"
pooled_cpm: 23.43
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# CRYZ

*crystallin zeta* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +15.1, q 0e+00, up in 39 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.59× (z +10.9, q 3e-25, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.458× (z -18.2, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPN1]] (+0.74, fdr 7e-06), [[UBQLN1]] (+0.73, fdr 7e-06), [[GFM2]] (+0.72, fdr 7e-06); moves opposite to [[RBX1]] (-0.62, fdr 9e-06), [[FAM193A]] (-0.60, fdr 2e-05), [[TNRC6C]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +15.1 | 0e+00 | 39/42 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +14.6 | 1e-45 | 26/30 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +10.9 | 3e-25 | 35/48 (HS-578T, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +8.6 | 1e-15 | 23/34 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +8.3 | 1e-14 | 29/46 (C32, HS-578T, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **2.17×** | +6.7 | 2e-09 | 29/45 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +6.2 | 5e-08 | 25/47 (AsPC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.45×** | +6.2 | 5e-08 | 25/46 (C32, KATO III, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 6e-05 | 20/47 (RKO, SW1417, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.5 | 3e-04 | 0/48 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.3 | 9e-04 | 15/47 (RKO, SW1417, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.003 | 13/48 (KATO III, COLO 205, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.24×** | +3.5 | 0.017 | 9/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +3.0 | 0.11 | 11/48 (AsPC-1, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.458×** | -18.2 | 0e+00 | 41/47 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.437×** | -13.7 | 4e-40 | 40/47 (H4, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -13.1 | 1e-36 | 38/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.478×** | -12.2 | 5e-32 | 35/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.494×** | -11.7 | 2e-29 | 40/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.511×** | -11.1 | 1e-26 | 37/46 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -9.2 | 2e-18 | 30/46 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.696×** | -6.0 | 1e-07 | 22/47 (HepG2/C3A, SW480, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.715×** | -5.5 | 2e-06 | 23/46 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.746×** | -4.8 | 8e-05 | 21/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.779×** | -4.1 | 0.002 | 17/47 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.623×** | -4.1 | 0.002 | 17/46 (RPMI-7951, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.783×** | -4.0 | 0.002 | 20/46 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.802×** | -3.6 | 0.011 | 16/47 (HEC-1-A, HepG2/C3A, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.034 | 13/47 (KATO III, CFPAC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.690×** | -3.2 | 0.048 | 10/47 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.877× | -3.1 | 0.073 | 13/48 (HCT15, CFPAC-1, …) | rises with dose |  |
| [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM |  | 0.836× | -3.0 | 0.085 | 12/47 (HS-578T, SW 1271, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | 0.836× | -3.0 | 0.085 | 9/48 (NCI-H661, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.7 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.321× (z -16.6) |
| [[MIA PaCa-2 (line)]] | alt | 34.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.262× (z -10.9) |
| [[PANC-1 (line)]] | alt | 15.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +9.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.272× (z -10.5) |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.4) |
| [[SW 900 (line)]] | alt | 29.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 44.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -11.4) |
| [[COLO 205 (line)]] | alt | 18.0 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0797× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.153× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 7.50 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.0) ⚠ toxic; transcription drop | [[Hydroxyurea (drug)]] 0.05 µM 0.160× (z -10.3) |
| [[A498 (line)]] | wt | 65.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 27.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +10.5) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 49.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.411× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 48.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.202× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.399× (z -8.8) |
| [[HS-578T (line)]] | alt | 12.1 | 1 | 1 | [[Selinexor (drug)]] 5 µM 3.50× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -8.9) |
| [[LoVo (line)]] | wt | 14.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.120× (z -15.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 39.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -13.9) |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 2 | — | [[Bergenin (drug)]] 5 µM 0.186× (z -12.5) |
| [[A-427 (line)]] | wt | 32.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -13.7) |
| [[BT-474 (line)]] | alt | 7.48 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0843× (z -9.8) |
| [[C32 (line)]] | wt | 17.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.32× (z +10.7) | — |
| [[H4 (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0654× (z -14.3) |
| [[HCT15 (line)]] | alt | 58.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -17.5) |
| [[HOP62 (line)]] | alt | 8.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -10.9) |
| [[HT-29 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +8.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -8.7) |
| [[J82 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 14.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.79× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 7.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0746× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 35.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 45.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -11.6) |
| [[RKO (line)]] | wt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.9) |
| [[A-172 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPN1]] | +0.74 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[GFM2]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[PFKM]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[TCP1]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[SUDS3]] | +0.61 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.61 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[AHSA1]] | +0.60 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[AGO1]] | +0.60 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[CACYBP]] | +0.60 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[EPDR1]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBX1]] | -0.62 | -0.60 / -0.57 | both halves | 9e-06 | STRING 418 |
| [[FAM193A]] | -0.60 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TNRC6C]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[MIDN]] | -0.58 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[PPP6R2]] | -0.56 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[CHKB]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[PPP1R35]] ⚠ | -0.54 | -0.48 / -0.57 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LCAT]] | -0.53 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[OPA3]] | -0.53 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[RELB]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[KRTCAP2]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ACTR3B]] | -0.52 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[POLR2L]] | -0.51 | -0.55 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers CRYZ's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.0, -14.0); signed map (-29.8, -28.8). **Vector** length 101, 24.0% of its response variance represented; |z| ≥ 3 in 1,146 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.4 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.0 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.8 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.2 | +1.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.1 | +1.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.6 | -11.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -18.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -13.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -1.8 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.7 | -1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | crystallin zeta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:74,705,482-74,733,408 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Oxidoreductases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08257](https://www.uniprot.org/uniprotkb/Q08257) (Zeta-crystallin):

> Multifunctional crystallin endowed with unrelated mRNA stabilization and enzymatic oxidoreductase activities. Binds (AU)-rich elements (ARE) in the 3'-UTR of target mRNA to enhance their stability. Upon metabolic acidosis, stabilizes the mRNA encoding SLC12A1 a cotransporter involved in transepithelial NH4(+) reabsorption in the medullary thick ascending limb in kidney (By similarity). In response to acidosis, also participates to the adaptive increase in renal ammoniagenesis by stabilizing the …

**Summary**, from NCBI Gene [1429](https://www.ncbi.nlm.nih.gov/gene/1429):

> Crystallins are separated into two classes: taxon-specific, or enzyme, and ubiquitous. The latter class constitutes the major proteins of vertebrate eye lens and maintains the transparency and refractive index of the lens. The former class is also called phylogenetically-restricted crystallins. This gene encodes a taxon-specific crystallin protein which has NADPH-dependent quinone reductase activity distinct from other known quinone reductases. It lacks alcohol dehydrogenase activity although …

**Accessions** — [HGNC:2419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2419) · Entrez [1429](https://www.ncbi.nlm.nih.gov/gene/1429) · UniProt [Q08257](https://www.uniprot.org/uniprotkb/Q08257) · Ensembl [ENSG00000116791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116791)

## Data

Gene col 3840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3840); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3840]; `tensor/DDL_lfc|DDL_z.npy` [3840]; `embed/gene_vectors.npy` [3840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3840 or target_col == 3840). Every well: [[CRYZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
