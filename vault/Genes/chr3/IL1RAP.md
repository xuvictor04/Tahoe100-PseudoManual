---
symbol: "IL1RAP"
type: "gene"
col: 12127
ensembl_id: "ENSG00000196083"
name: "interleukin 1 receptor accessory protein"
location: "3q28"
module: 84
arm: "+"
pooled_cpm: 139.59
n_lines_expressing: 42
n_dd_up: 3
n_dd_down: 43
n_dd_up_clean: 3
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 15
direction_downstream: 24
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# IL1RAP

*interleukin 1 receptor accessory protein* — 3q28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +7.7, q 1e-11, up in 29 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.411× (z -20.9, q 0e+00, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHD4]] (+0.65, fdr 7e-06), [[COL13A1]] (+0.64, fdr 7e-06), [[LOXL2]] (+0.64, fdr 7e-06); moves opposite to [[TXNRD2]] (-0.57, fdr 2e-05), [[FAIM]] (-0.55, fdr 1e-04), [[GABPB2]] (-0.55, fdr 4e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[EFCAB13]] → it (grade B ⚠); 24 go from it, the strongest it → [[ITGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +7.7 | 1e-11 | 29/40 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +5.4 | 2e-05 | 25/40 (NCI-H2030, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +4.3 | 0.003 | 25/41 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 1.22× | +3.3 | 0.10 | 19/40 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.22× | +3.3 | 0.10 | 16/40 (PANC-1, HT-29, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 1.45× | +3.2 | 0.12 | 17/40 (RKO, COLO 205, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12127.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.411×** | -20.9 | 0e+00 | 32/40 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.306×** | -18.9 | 0e+00 | 39/40 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.403×** | -15.1 | 0e+00 | 35/40 (RKO, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.448×** | -12.8 | 1e-35 | 27/35 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.593×** | -12.3 | 2e-32 | 33/40 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.466×** | -12.2 | 2e-32 | 32/39 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.487×** | -11.5 | 1e-28 | 35/39 (HepG2/C3A, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.534×** | -10.4 | 1e-23 | 34/40 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.540×** | -10.2 | 8e-23 | 33/41 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.549×** | -10.0 | 1e-21 | 34/40 (KATO III, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.550×** | -9.9 | 1e-21 | 36/40 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.577×** | -8.6 | 3e-16 | 33/40 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.597×** | -8.6 | 4e-16 | 29/40 (C32, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -7.0 | 1e-10 | 29/40 (C32, SK-MEL-2, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.748×** | -6.8 | 4e-10 | 29/41 (C32, COLO 205, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.688×** | -6.2 | 2e-08 | 25/41 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.722×** | -5.4 | 2e-06 | 25/40 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.740×** | -5.0 | 2e-05 | 28/40 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.747×** | -4.8 | 4e-05 | 28/41 (COLO 205, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 503 | 0 | 29 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -18.0) |
| [[SK-MEL-2 (line)]] | alt | 449 | 0 | 23 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -19.2) |
| [[KATO III (line)]] | alt | 320 | 1 (1 ⚠) | 16 (8 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.39× (z +10.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -25.1) |
| [[PANC-1 (line)]] | alt | 138 | 1 | 14 (7 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.31× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -27.9) |
| [[SNU-423 (line)]] | alt | 270 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 245 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -25.8) |
| [[HOP62 (line)]] | alt | 162 | 0 | 12 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.227× (z -15.7) |
| [[J82 (line)]] | alt | 311 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -17.1) |
| [[HepG2_C3A (line)]] | wt | 218 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -27.0) |
| [[A549 (line)]] | wt | 137 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -23.3) |
| [[CFPAC-1 (line)]] | alt | 160 | 0 | 8 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.406× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 163 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 559 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.314× (z -16.6) |
| [[COLO 205 (line)]] | alt | 90.1 | 3 (2 ⚠) | 4 | [[Daptomycin (drug)]] 0.5 µM 3.52× (z +10.4) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 3.36× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.206× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 82.7 | 4 (1 ⚠) | 3 | [[Tucidinostat (drug)]] 5 µM 1.97× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -15.7) |
| [[LoVo (line)]] | wt | 37.9 | 6 (3 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 3.44× (z +11.9) | [[Harringtonine (drug)]] 5 µM 0.355× (z -9.4) |
| [[HT-29 (line)]] | alt | 83.6 | 5 (2 ⚠) | 1 | [[Daptomycin (drug)]] 5 µM 3.23× (z +11.6) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.28× (z +11.5) | [[Selinexor (drug)]] 5 µM 0.493× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 44.7 | 5 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 5.21× (z +14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 4.55× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 36.6 | 3 (2 ⚠) | 3 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.63× (z +9.3) | [[Harringtonine (drug)]] 5 µM 0.204× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 151 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.6) |
| [[RKO (line)]] | wt | 65.8 | 1 | 5 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.32× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -20.9) |
| [[Hs 766T (line)]] | wt | 185 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 95.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -25.1) |
| [[A-427 (line)]] | wt | 40.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +10.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.93× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -13.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 198 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.356× (z -10.8) |
| [[BT-474 (line)]] | alt | 96.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.351× (z -9.6) |
| [[A-172 (line)]] | wt | 171 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.322× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.337× (z -10.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.342× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.0) |
| [[SW 1271 (line)]] | alt | 368 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 69.1 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.0660× (z -11.4) |
| [[H4 (line)]] | wt | 72.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0763× (z -17.7) |
| [[HCT15 (line)]] | alt | 47.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.5) |
| [[LS 180 (line)]] | wt | 47.0 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.40× (z +11.1) | [[Harringtonine (drug)]] 5 µM 0.295× (z -10.6) |
| [[SW1417 (line)]] | alt | 82.5 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.11× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -8.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 124 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.268× (z -11.8) |
| [[SW 900 (line)]] | alt | 70.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -12.4) |
| [[A498 (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 20.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[COL13A1]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[LOXL2]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[GALNT18]] | +0.61 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[UBA6]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ELL2]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[AFAP1]] | +0.58 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[SEMA4B]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[CHSY1]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[RGS17]] | +0.57 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SLC2A3]] | +0.57 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[UXS1]] | +0.57 | +0.51 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNRD2]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[FAIM]] | -0.55 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[GABPB2]] | -0.55 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[DIS3L]] | -0.54 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[KEAP1]] | -0.53 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[RNF115]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[IQCH-AS1]] | -0.52 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[RPRD2]] | -0.52 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[VPS33A]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[PGGT1B]] | -0.51 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[RBM33]] | -0.50 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[MAU2]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 13, C 2. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFCAB13]] | B | EFCAB13 activity raises IL1RAP's level | lines that do not express EFCAB13 (14) vs lines expressing it (36) | 2.77× lower at baseline in the lines without EFCAB13 | 0.014 | ⚠ within organs, on part of the lines; also absent: KCNS3, TRIM6, GPR176; maybe low, not absent |
| [[ELL2]] | B | ELL2 activity raises IL1RAP's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 3.35× lower at baseline in the lines without ELL2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[ADAM19]] | B | ADAM19 activity raises IL1RAP's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 2.72× lower at baseline in the lines without ADAM19 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises IL1RAP's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.90× lower at baseline in the lines without TNFRSF11A | 0.019 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[IGFBP3]] | B | IGFBP3 activity raises IL1RAP's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 2.53× lower at baseline in the lines without IGFBP3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers IL1RAP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[EPAS1]] | B | EPAS1 activity raises IL1RAP's level | lines that do not express EPAS1 (9) vs lines expressing it (41) | 3.26× lower at baseline in the lines without EPAS1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SEMA4A, ANKEF1, MARCKS |
| [[ITGB3]] | B | ITGB3 activity raises IL1RAP's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.73× lower at baseline in the lines without ITGB3 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[MTSS1]] | B | MTSS1 activity raises IL1RAP's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without MTSS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[SERPINB1]] | B | SERPINB1 activity raises IL1RAP's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.18× lower at baseline in the lines without SERPINB1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[TREM1]] | B | TREM1 activity raises IL1RAP's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without TREM1 | 0.068 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[PRKCA]] | B | PRKCA activity raises IL1RAP's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 2.55× lower at baseline in the lines without PRKCA | 0.069 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 22, C 2. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2]] | B | IL1RAP activity raises ITGA2's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 5.53× lower at baseline in the lines without IL1RAP | 0.006 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[RELL1]] | B | IL1RAP activity raises RELL1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without IL1RAP | 0.011 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[EPAS1]] | B | IL1RAP activity raises EPAS1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 4.49× lower at baseline in the lines without IL1RAP | 0.020 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[CIB1]] | B | IL1RAP activity raises CIB1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.68× lower at baseline in the lines without IL1RAP | 0.024 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[DIS3L]] | B | IL1RAP activity lowers DIS3L's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.15× higher at baseline in the lines without IL1RAP | 0.024 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[PRKCA]] | B | IL1RAP activity raises PRKCA's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without IL1RAP | 0.028 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[EFCAB13]] | B | IL1RAP activity raises EFCAB13's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 3.90× lower at baseline in the lines without IL1RAP | 0.030 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[SEMA4B]] | B | IL1RAP activity raises SEMA4B's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.62× lower at baseline in the lines without IL1RAP | 0.034 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[EHD4]] | B | IL1RAP activity raises EHD4's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without IL1RAP | 0.034 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[TRPT1]] | B | IL1RAP activity raises TRPT1's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.25× lower at baseline in the lines without IL1RAP | 0.036 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[GABPB2]] | B | IL1RAP activity raises GABPB2's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without IL1RAP | 0.037 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[SHB]] | B | IL1RAP activity raises SHB's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.49× lower at baseline in the lines without IL1RAP | 0.039 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.3, 5.6); signed map (3.2, 51.0). **Vector** length 136, 45.9% of its response variance represented; |z| ≥ 3 in 1,693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.9 | +5.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.8 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | -0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.8 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +1.0 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.5 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.6 | -12.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.5 | -18.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -8.0 | -10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -15.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.5 | -10.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.0 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -5.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.1 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 receptor accessory protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q28 — chr3:190,514,051-190,659,750 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL-1RAcP, IL1R3, C3orf13 |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Interleukin receptors; TIR domain containing |
| Reactome | 12 pathways, smallest: Interleukin-33 signaling; Receptor-type tyrosine-protein phosphatases; Protein-protein interactions at synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPH3](https://www.uniprot.org/uniprotkb/Q9NPH3) (Interleukin-1 receptor accessory protein):

> Coreceptor for IL1RL2 in the IL-36 signaling system (By similarity). Coreceptor with IL1R1 in the IL-1 signaling system. Associates with IL1R1 bound to IL1B to form the high affinity interleukin-1 receptor complex which mediates interleukin-1-dependent activation of NF-kappa-B and other pathways. Signaling involves the recruitment of adapter molecules such as TOLLIP, MYD88, and IRAK1 or IRAK2 via the respective TIR domains of the receptor/coreceptor subunits. Recruits TOLLIP to the signaling …

**Summary**, from NCBI Gene [3556](https://www.ncbi.nlm.nih.gov/gene/3556):

> This gene encodes a component of the interleukin 1 receptor complex, which initiates signalling events that result in the activation of interleukin 1-responsive genes. Alternative splicing of this gene results in membrane-bound and soluble isoforms differing in their C-terminus. The ratio of soluble to membrane-bound forms increases during acute-phase induction or stress. [provided by RefSeq, Jul 2018]

**Accessions** — [HGNC:5995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5995) · Entrez [3556](https://www.ncbi.nlm.nih.gov/gene/3556) · UniProt [Q9NPH3](https://www.uniprot.org/uniprotkb/Q9NPH3) · Ensembl [ENSG00000196083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196083)

## Data

Gene col 12127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12127); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12127]; `tensor/DDL_lfc|DDL_z.npy` [12127]; `embed/gene_vectors.npy` [12127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12127 or target_col == 12127). Every well: [[IL1RAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL1RAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
