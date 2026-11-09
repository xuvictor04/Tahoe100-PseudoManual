---
symbol: "TMED5"
type: "gene"
col: 3917
ensembl_id: "ENSG00000117500"
name: "transmembrane p24 trafficking protein 5"
location: "1p22.1"
module: 42
arm: "+"
pooled_cpm: 69.76
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TMED5

*transmembrane p24 trafficking protein 5* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.63× (z +9.4, q 5e-18, up in 32 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.30× (z +5.3, q 2e-05, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.564× (z -11.5, q 1e-27, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPN1]] (+0.65, fdr 7e-06), [[TMEM167A]] (+0.59, fdr 1e-05), [[TXNDC5]] (+0.59, fdr 1e-05); moves opposite to [[FCHSD2]] (-0.55, fdr 1e-05), [[NTHL1]] (-0.55, fdr 3e-05), [[PIM3]] (-0.52, fdr 4e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +9.4 | 5e-18 | 32/41 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +8.2 | 5e-14 | 35/49 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +6.3 | 7e-08 | 31/48 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 2e-05 | 29/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +5.2 | 2e-05 | 30/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +5.2 | 2e-05 | 29/44 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.1 | 3e-05 | 28/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 22/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.004 | 18/48 (LOX-IMVI, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.005 | 21/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.4 | 0.034 | 19/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.034 | 16/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.046 | 13/49 (RKO, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.35×** | +3.1 | 0.080 | 18/44 (PANC-1, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3917.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.564×** | -11.5 | 1e-27 | 39/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.582×** | -10.8 | 9e-25 | 38/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.659×** | -8.3 | 1e-14 | 32/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.770×** | -7.4 | 2e-11 | 28/48 (HS-578T, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.825×** | -5.5 | 5e-06 | 20/48 (RKO, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.766×** | -5.3 | 9e-06 | 25/48 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.775×** | -5.1 | 3e-05 | 24/48 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.773×** | -5.0 | 5e-05 | 24/48 (HS-578T, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.821×** | -4.0 | 0.005 | 23/48 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.721×** | -3.4 | 0.035 | 17/49 (A498, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.723×** | -3.4 | 0.035 | 18/49 (HS-578T, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.846× | -3.4 | 0.036 | 14/48 (SW 900, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.852× | -3.2 | 0.058 | 17/48 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.801×** | -3.1 | 0.075 | 13/48 (A498, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 123 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -19.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.315× (z -12.5) |
| [[PANC-1 (line)]] | alt | 47.0 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +12.7) | — |
| [[A-427 (line)]] | wt | 37.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.25× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -15.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 116 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -11.1) |
| [[HOP62 (line)]] | alt | 72.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 130 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 50.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 122 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -11.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.415× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 104 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.5) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.395× (z -9.1) |
| [[SW 900 (line)]] | alt | 99.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.382× (z -10.0) |
| [[SW480 (line)]] | alt | 56.4 | 2 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.06× (z +9.7) | — |
| [[A-172 (line)]] | wt | 37.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[AsPC-1 (line)]] | alt | 84.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +8.7) | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -11.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[H4 (line)]] | wt | 52.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0666× (z -12.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 77.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.324× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 88.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 69.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.431× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -10.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 67.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A549 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 84.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 81.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPN1]] | +0.65 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[TMEM167A]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TXNDC5]] | +0.59 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[MTFR1]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[HYOU1]] | +0.58 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[CMPK1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[TMED2]] | +0.54 | +0.57 / +0.58 | both halves | 9e-06 | same gene group; STRING 954 |
| [[GDI2]] | +0.53 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TPD52L2]] | +0.53 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[CANX]] | +0.52 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CLDND1]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[GOLGA3]] | +0.52 | +0.40 / +0.62 | both halves | 5e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD2]] | -0.55 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[NTHL1]] | -0.55 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[PIM3]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[DBP]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ANKRD33B]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[FAM133B]] | -0.51 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[COIL]] | -0.51 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[TGIF2]] | -0.51 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[NUAK2]] | -0.50 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[SSH2]] | -0.50 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[TRAF2]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SMAD7]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.525). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, -28.6); signed map (-55.9, 3.9). **Vector** length 117, 32.1% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +4.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.2 | +3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.2 |
| fall | [[Radotinib (drug)]] 5 µM |  | -5.4 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -4.4 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.9 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.8 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.2 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:93,149,742-93,180,516 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-100, p24g2, p24gamma2 |
| Gene groups (HGNC) | Transmembrane p24 trafficking proteins |
| Reactome | 2 pathways, smallest: WNT ligand biogenesis and trafficking; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3A6](https://www.uniprot.org/uniprotkb/Q9Y3A6) (Transmembrane emp24 domain-containing protein 5):

> Potential role in vesicular protein trafficking, mainly in the early secretory pathway. Required for the maintenance of the Golgi apparatus; involved in protein exchange between Golgi stacks during assembly. Probably not required for COPI-vesicle-mediated retrograde transport.

**Summary**, from NCBI Gene [50999](https://www.ncbi.nlm.nih.gov/gene/50999):

> Involved in Golgi ribbon formation. Located in cis-Golgi network; endoplasmic reticulum exit site; and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24251](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24251) · Entrez [50999](https://www.ncbi.nlm.nih.gov/gene/50999) · UniProt [Q9Y3A6](https://www.uniprot.org/uniprotkb/Q9Y3A6) · Ensembl [ENSG00000117500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117500)

## Data

Gene col 3917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3917); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3917]; `tensor/DDL_lfc|DDL_z.npy` [3917]; `embed/gene_vectors.npy` [3917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3917 or target_col == 3917). Every well: [[TMED5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
