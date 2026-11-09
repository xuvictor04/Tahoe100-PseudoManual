---
symbol: "TAP1"
type: "gene"
col: 9641
ensembl_id: "ENSG00000168394"
name: "transporter 1, ATP binding cassette subfamily B member"
location: "6p21.32"
module: 70
arm: "+"
pooled_cpm: 43.32
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 34
n_dd_up_clean: 31
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 40
direction_downstream: 10
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# TAP1

*transporter 1, ATP binding cassette subfamily B member* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +12.4, q 1e-32, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.322× (z -16.6, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB8]] (+0.84, fdr 7e-06, ⚠ same locus), [[PSMB9]] (+0.84, fdr 7e-06, ⚠ same locus), [[PSME2]] (+0.81, fdr 7e-06), [[PARP10]] (+0.81, fdr 7e-06), [[IFIH1]] (+0.80, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 10 go from it, the strongest it → [[IFIT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +12.4 | 1e-32 | 40/47 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.56×** | +9.2 | 1e-17 | 28/47 (HEC-1-A, J82, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +8.9 | 1e-16 | 36/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.44×** | +6.5 | 2e-08 | 32/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +6.3 | 4e-08 | 32/45 (PANC-1, SW1417, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.55×** | +6.2 | 4e-08 | 29/47 (HEC-1-A, NCI-H2030, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.2 | 6e-08 | 35/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.1 | 7e-08 | 28/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 1e-07 | 31/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.45×** | +5.9 | 2e-07 | 30/48 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 4e-07 | 33/48 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.6 | 1e-06 | 28/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 1e-06 | 32/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +5.0 | 2e-05 | 28/47 (NCI-H23, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 4e-05 | 29/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.8 | 5e-05 | 27/48 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.26×** | +4.7 | 7e-05 | 25/48 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +4.2 | 9e-04 | 27/47 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.004 | 20/47 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 3 with an alert ⚠; shown: the 15 strongest. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9641.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.322×** | -16.6 | 0e+00 | 44/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.338×** | -15.9 | 0e+00 | 43/48 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.398×** | -13.5 | 2e-39 | 43/48 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.581×** | -11.2 | 3e-27 | 32/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.466×** | -11.2 | 5e-27 | 41/48 (KATO III, LoVo, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.546×** | -8.9 | 7e-17 | 32/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.562×** | -8.5 | 2e-15 | 37/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.545×** | -8.4 | 3e-15 | 33/48 (LoVo, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.577×** | -8.1 | 5e-14 | 36/48 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.583×** | -7.9 | 1e-13 | 29/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -7.9 | 1e-13 | 32/48 (BT-474, KATO III, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.694×** | -7.5 | 2e-12 | 29/48 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.604×** | -7.4 | 6e-12 | 29/48 (HepG2/C3A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.616×** | -7.1 | 5e-11 | 32/48 (LoVo, RPMI-7951, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.637×** | -6.6 | 2e-09 | 34/48 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 62.6 | 1 | 13 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +8.8) | [[Tofacitinib (drug)]] 5 µM 0.259× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 80.2 | 1 (1 ⚠) | 13 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.84× (z +9.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Tofacitinib (drug)]] 5 µM 0.352× (z -14.2) |
| [[A549 (line)]] | wt | 65.5 | 0 | 13 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -18.3) |
| [[LoVo (line)]] | wt | 51.1 | 0 | 12 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.304× (z -15.1) |
| [[A-172 (line)]] | wt | 103 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 102 | 1 (1 ⚠) | 8 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.9) ⚠ cell-cycle shift, explains ~32% of this change | [[Tofacitinib (drug)]] 5 µM 0.330× (z -16.7) |
| [[KATO III (line)]] | alt | 62.3 | 0 | 9 | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 44.1 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -14.4) |
| [[BT-474 (line)]] | alt | 36.6 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.116× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 60.3 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -11.6) |
| [[PANC-1 (line)]] | alt | 41.5 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +15.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 80.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -13.1) |
| [[J82 (line)]] | alt | 32.5 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +15.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +12.0) | — |
| [[RKO (line)]] | wt | 38.3 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.183× (z -10.5) |
| [[A498 (line)]] | wt | 65.1 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -13.2) |
| [[COLO 205 (line)]] | alt | 50.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0891× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 28.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +18.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.82× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 72.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 27.3 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.301× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 72.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -12.9) |
| [[C-33 A (line)]] | alt | 29.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0894× (z -12.7) |
| [[C32 (line)]] | wt | 17.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.43× (z +13.1) | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.207× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0674× (z -11.8) |
| [[HOP62 (line)]] | alt | 11.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 28.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.305× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 40.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.224× (z -9.0) |
| [[H4 (line)]] | wt | 41.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.204× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 40.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 23.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.245× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 37.5 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.292× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 74.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.336× (z -9.6) |
| [[SNU-423 (line)]] | alt | 75.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.289× (z -9.5) |
| [[SW1417 (line)]] | alt | 32.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -11.1) |
| [[SW48 (line)]] | wt | 24.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +8.5) | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB8]] | +0.84 | +0.72 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 973; ⚠ same locus (0.5 kb, same strand: neighbours can correlate without regulation) |
| [[PSMB9]] | +0.84 | +0.79 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 981; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PSME2]] | +0.81 | +0.76 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 586 |
| [[PARP10]] | +0.81 | +0.69 / +0.84 | both halves | 7e-06 |  |
| [[IFIH1]] | +0.80 | +0.70 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 508 |
| [[GBP1]] | +0.80 | +0.75 / +0.79 | both halves | 7e-06 | STRING 786 |
| [[PARP14]] | +0.79 | +0.70 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 537 |
| [[ADAR]] | +0.79 | +0.74 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 422 |
| [[HLA-F]] | +0.79 | +0.70 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_UP; STRING 832 |
| [[TRIM22]] | +0.78 | +0.67 / +0.82 | both halves | 7e-06 |  |
| [[GBP4]] | +0.78 | +0.70 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 479 |
| [[APOL6]] | +0.77 | +0.67 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PARP9]] | +0.77 | +0.68 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 585 |
| [[TRANK1]] | +0.77 | +0.70 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 25, C 15. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity strengthens TAP1's drug response | lines that do not express OAS2 (14) vs lines expressing it (34) | the lines without OAS2 respond 0.61× as strongly (z diff +1.31); strongest at Auranofin 5 µM: 0.56x vs 0.42x (z diff +3.4) | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[MX1]] | B | MX1 activity strengthens TAP1's drug response | lines that do not express MX1 (19) vs lines expressing it (29) | the lines without MX1 respond 0.74× as strongly (z diff +0.88); strongest at Auranofin 5 µM: 0.57x vs 0.40x (z diff +3.8) | 0.016 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1; target measured in part of the lines; artifact flags |
| [[MX1]] | B | MX1 activity raises TAP1's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without MX1 | 0.020 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[SAMD9]] | B | SAMD9 activity raises TAP1's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without SAMD9 | 0.031 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[OAS3]] | B | OAS3 activity raises TAP1's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without OAS3 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[OAS2]] | B | OAS2 activity raises TAP1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without OAS2 | 0.040 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[IFI44L]] | B | IFI44L activity raises TAP1's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.59× lower at baseline in the lines without IFI44L | 0.042 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[BATF2]] | B | BATF2 activity raises TAP1's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.66× lower at baseline in the lines without BATF2 | 0.042 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises TAP1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without IFI44 | 0.043 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[IFI6]] | B | IFI6 activity strengthens TAP1's drug response | lines that do not express IFI6 (13) vs lines expressing it (35) | the lines without IFI6 respond 0.61× as strongly (z diff +1.33); strongest at Auranofin 5 µM: 0.63x vs 0.41x (z diff +4.2) | 0.050 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[EPSTI1]] | B | EPSTI1 activity raises TAP1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.65× lower at baseline in the lines without EPSTI1 | 0.059 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[OAS1]] | B | OAS1 activity raises TAP1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without OAS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT5]] | C | TAP1's natural level strengthens IFIT5's drug response | TAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.70; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB8]] | C | TAP1's natural level strengthens PSMB8's drug response | TAP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.44; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NMI]] | C | TAP1's natural level strengthens NMI's drug response | TAP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.52; direction not clear | 0.014 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB9]] | C | TAP1's natural level strengthens PSMB9's drug response | TAP1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.42; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[PARP12]] | C | TAP1's natural level strengthens PARP12's drug response | TAP1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.63; direction not clear | 0.040 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRANK1]] | C | TAP1's natural level strengthens TRANK1's drug response | TAP1's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.53; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SAMHD1]] | C | TAP1's natural level strengthens SAMHD1's drug response | TAP1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.47; direction not clear | 0.049 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PHF11]] | C | TAP1's natural level strengthens PHF11's drug response | TAP1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.39; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CMTR1]] | C | TAP1's natural level strengthens CMTR1's drug response | TAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.48; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[OASL]] | C | TAP1's natural level strengthens OASL's drug response | TAP1's natural level across 39 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.24; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.865). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.5, 51.2); signed map (63.3, 29.1). **Vector** length 157, 55.0% of its response variance represented; |z| ≥ 3 in 1,655 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.71 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.71 to 8); *Interferon alpha/beta signaling* (reactome, mean cos +0.67 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.2 | +12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.9 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.9 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +6.8 | +5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.6 | +6.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +6.5 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +6.4 | +5.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.9 | -11.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -9.6 | -11.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.0 | -8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.9 | -8.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.7 | -8.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.4 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | transporter 1, ATP binding cassette subfamily B member |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,845,209-32,853,816 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSF1, RING4, D6S114E; previously ABCB2 |
| Gene groups (HGNC) | ATP binding cassette subfamily B |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, ALLOGRAFT_REJECTION, APOPTOSIS, UV_RESPONSE_UP, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 5 pathways, smallest: Antigen Presentation: Folding, assembly and peptide loading of class I MHC; ER-Phagosome pathway; Antigen processing-Cross presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03518](https://www.uniprot.org/uniprotkb/Q03518) (Antigen peptide transporter 1):

> ABC transporter associated with antigen processing. In complex with TAP2 mediates unidirectional translocation of peptide antigens from cytosol to endoplasmic reticulum (ER) for loading onto MHC class I (MHCI) molecules. Uses the chemical energy of ATP to export peptides against the concentration gradient. During the transport cycle alternates between 'inward-facing' state with peptide binding site facing the cytosol to 'outward-facing' state with peptide binding site facing the ER lumen. …

**Summary**, from NCBI Gene [6890](https://www.ncbi.nlm.nih.gov/gene/6890):

> The membrane-associated protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MDR/TAP subfamily. Members of the MDR/TAP subfamily are involved in multidrug resistance. The protein encoded by this gene is involved in the pumping of …

**Accessions** — [HGNC:43](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43) · Entrez [6890](https://www.ncbi.nlm.nih.gov/gene/6890) · UniProt [Q03518](https://www.uniprot.org/uniprotkb/Q03518) · Ensembl [ENSG00000168394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168394)

## Data

Gene col 9641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9641); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9641]; `tensor/DDL_lfc|DDL_z.npy` [9641]; `embed/gene_vectors.npy` [9641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9641 or target_col == 9641). Every well: [[TAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
