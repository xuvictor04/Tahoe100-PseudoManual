---
symbol: "MLH3"
type: "gene"
col: 4097
ensembl_id: "ENSG00000119684"
name: "mutL homolog 3"
location: "14q24.3"
module: 1
arm: "+"
pooled_cpm: 43.56
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MLH3

*mutL homolog 3* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.05 µM: 1.23× (z +3.8, q 0.048, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.580× (z -15.2, q 0e+00, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.489× (z -14.2, q 4e-43, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIX23]] (+0.68, fdr 7e-06), [[TSR1]] (+0.66, fdr 7e-06), [[THUMPD3]] (+0.65, fdr 9e-06); moves opposite to [[TMEM219]] (-0.58, fdr 2e-05), [[PDXDC2P]] (-0.57, fdr 3e-05), [[ALDH6A1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CYP46A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.048 | 18/46 (SW480, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.048 | 18/48 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.3 | 0.21 | 11/48 (NCI-H23, NCI-H2347, …) | top dose only |  |
| [[Finasteride (drug)]] 5 µM |  | 1.18× | +3.2 | 0.21 | 13/47 (A549, A-172, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.24 | 13/48 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.16× | +3.0 | 0.24 | 14/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4097.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.580×** | -15.2 | 0e+00 | 36/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.489×** | -14.2 | 4e-43 | 43/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.495×** | -13.9 | 9e-42 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -13.8 | 5e-41 | 38/47 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.520×** | -12.9 | 4e-36 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.538×** | -12.3 | 2e-32 | 43/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -10.6 | 4e-24 | 38/46 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.612×** | -9.3 | 6e-19 | 32/47 (NCI-H460, MIA PaCa-2, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.629×** | -9.2 | 3e-18 | 30/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.726×** | -6.3 | 1e-08 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.563×** | -5.9 | 1e-07 | 28/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.726×** | -5.8 | 3e-07 | 25/43 (A-427, HEC-1-A, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.840× | -4.8 | 6e-05 | 21/48 (RKO, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.749×** | -4.6 | 1e-04 | 25/48 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.811×** | -4.1 | 0.001 | 21/47 (HEC-1-A, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 54.2 | 0 | 13 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -20.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 34.8 | 0 | 11 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.237× (z -16.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 59.8 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -14.9) |
| [[MIA PaCa-2 (line)]] | alt | 77.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -19.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.327× (z -11.7) |
| [[SW480 (line)]] | alt | 47.4 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -16.2) |
| [[RKO (line)]] | wt | 73.8 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.0) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.378× (z -10.7) |
| [[A549 (line)]] | wt | 53.9 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0836× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.424× (z -8.9) |
| [[C32 (line)]] | wt | 51.9 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[J82 (line)]] | alt | 38.3 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.245× (z -13.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.353× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 57.9 | 0 | 5 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -17.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.449× (z -9.0) |
| [[SNU-423 (line)]] | alt | 38.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -14.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 61.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -9.4) |
| [[C-33 A (line)]] | alt | 59.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0850× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.299× (z -10.3) |
| [[HOP62 (line)]] | alt | 44.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 55.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.376× (z -11.2) |
| [[SW48 (line)]] | wt | 50.3 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0665× (z -17.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 43.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -9.5) |
| [[LS 180 (line)]] | wt | 35.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 49.6 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -8.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 38.7 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0918× (z -9.1) |
| [[HCT15 (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 69.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0845× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.213× (z -11.8) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 40.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.264× (z -8.8) |
| [[SW 1271 (line)]] | alt | 64.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0929× (z -8.9) ⚠ toxic |
| [[SW1417 (line)]] | alt | 37.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.357× (z -8.6) |
| [[A498 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIX23]] | +0.68 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TSR1]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[THUMPD3]] | +0.65 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[DNAJC11]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[RPL7L1]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[NOC3L]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TATDN1]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[GPATCH4]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MRM3]] | +0.62 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[ZNF507]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM219]] | -0.58 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PDXDC2P]] | -0.57 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[ALDH6A1]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[CHP1]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PHF1]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TBC1D10A]] | -0.56 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[BAD]] | -0.56 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ORMDL3]] | -0.55 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[LAPTM4A]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[GBF1]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[CBFA2T2]] | -0.54 | -0.45 / -0.43 | both halves | 4e-05 | pathway: Reproduction |
| [[ABHD12]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP46A1]] | B | CYP46A1 activity raises MLH3's level | lines that do not express CYP46A1 (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without CYP46A1 | 0.079 | ⚠ within organs, on part of the lines; also absent: CCDC102A, TPST1, DZIP1L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-37.4, 7.1); signed map (2.2, -42.4). **Vector** length 83.8, 19.8% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.7 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.5 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | -0.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.6 | -10.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -14.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.2 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -3.8 | -5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[8-Hydroxyquinoline (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.3 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | mutL homolog 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:75,013,769-75,051,532 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MutL homologs |
| Reactome | 4 pathways, smallest: Meiotic recombination; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHC1](https://www.uniprot.org/uniprotkb/Q9UHC1) (DNA mismatch repair protein Mlh3):

> Probably involved in the repair of mismatches in DNA.

**Summary**, from NCBI Gene [27030](https://www.ncbi.nlm.nih.gov/gene/27030):

> This gene is a member of the MutL-homolog (MLH) family of DNA mismatch repair (MMR) genes. MLH genes are implicated in maintaining genomic integrity during DNA replication and after meiotic recombination. The protein encoded by this gene functions as a heterodimer with other family members. Somatic mutations in this gene frequently occur in tumors exhibiting microsatellite instability, and germline mutations have been linked to hereditary nonpolyposis colorectal cancer type 7 (HNPCC7). Several …

**Accessions** — [HGNC:7128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7128) · Entrez [27030](https://www.ncbi.nlm.nih.gov/gene/27030) · UniProt [Q9UHC1](https://www.uniprot.org/uniprotkb/Q9UHC1) · Ensembl [ENSG00000119684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119684)

## Data

Gene col 4097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4097); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4097]; `tensor/DDL_lfc|DDL_z.npy` [4097]; `embed/gene_vectors.npy` [4097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4097 or target_col == 4097). Every well: [[MLH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
