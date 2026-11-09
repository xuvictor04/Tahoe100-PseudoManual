---
symbol: "COG7"
type: "gene"
col: 9650
ensembl_id: "ENSG00000168434"
name: "component of oligomeric golgi complex 7"
location: "16p12.2"
module: 207
arm: "+"
pooled_cpm: 63.0
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/207"]
generated_by: "tahoemap"
---

# COG7

*component of oligomeric golgi complex 7* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.57× (z +4.6, q 0.002, up in 27 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.454× (z -14.8, q 0e+00, down in 38 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.485× (z -14.1, q 1e-42, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLC4]] (+0.75, fdr 7e-06), [[DNAJC4]] (+0.72, fdr 7e-06), [[EGFL8]] (+0.70, fdr 7e-06); moves opposite to [[TMEM185B]] (-0.73, fdr 7e-06), [[SACS]] (-0.68, fdr 7e-06), [[GMFB]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 207]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF518B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +4.6 | 0.002 | 27/49 (HEC-1-A, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +4.2 | 0.008 | 24/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.016 | 21/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.42×** | +3.6 | 0.050 | 18/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.15 | 19/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Rifaximin (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.16 | 10/48 (A-172, SNU-423, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.16 | 4/49 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.18× | +3.1 | 0.16 | 8/49 (HT-29, PANC-1, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -14.8 | 0e+00 | 38/43 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.470×** | -14.7 | 0e+00 | 41/48 (NCI-H1792, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.485×** | -14.1 | 1e-42 | 48/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.465×** | -13.8 | 6e-41 | 37/45 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.526×** | -12.5 | 1e-33 | 46/48 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.542×** | -11.9 | 8e-31 | 48/48 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.685×** | -10.4 | 2e-23 | 45/48 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -10.3 | 3e-23 | 36/48 (AN3 CA, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.598×** | -10.0 | 1e-21 | 41/48 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.688×** | -7.3 | 2e-11 | 28/48 (AsPC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.717×** | -6.5 | 5e-09 | 35/48 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.713×** | -6.5 | 5e-09 | 32/48 (MIA PaCa-2, SW 900, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.738×** | -5.9 | 2e-07 | 35/49 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.754×** | -5.5 | 2e-06 | 29/48 (Panc 03.27, Hs 766T, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -5.3 | 5e-06 | 29/48 (SNU-1, H4, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.759×** | -5.3 | 5e-06 | 29/48 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.759×** | -5.2 | 8e-06 | 31/48 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.625×** | -4.8 | 5e-05 | 26/49 (A498, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 88.3 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.234× (z -11.9) |
| [[HS-578T (line)]] | alt | 79.0 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.389× (z -10.1) |
| [[HOP62 (line)]] | alt | 60.3 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -10.5) |
| [[SW 900 (line)]] | alt | 74.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.391× (z -10.1) |
| [[A498 (line)]] | wt | 98.7 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.403× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 86.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.424× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 64.7 | 0 | 5 (2 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.560× (z -10.7) |
| [[C32 (line)]] | wt | 78.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.283× (z -11.8) |
| [[KATO III (line)]] | alt | 69.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -10.3) |
| [[LoVo (line)]] | wt | 60.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.388× (z -10.1) |
| [[PANC-1 (line)]] | alt | 65.6 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.423× (z -10.5) |
| [[SNU-423 (line)]] | alt | 54.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.383× (z -8.8) |
| [[A549 (line)]] | wt | 76.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.415× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 58.6 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.247× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 54.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.456× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 86.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -19.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 51.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.388× (z -10.1) |
| [[C-33 A (line)]] | alt | 60.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -11.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 92.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -16.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 59.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -14.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 85.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.515× (z -9.3) |
| [[HT-29 (line)]] | alt | 54.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -12.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 59.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.423× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 60.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 77.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -11.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 76.5 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.261× (z -14.9) |
| [[SW1417 (line)]] | alt | 56.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.388× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.447× (z -8.9) |
| [[A-427 (line)]] | wt | 50.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -16.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 80.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0867× (z -15.7) |
| [[HepG2_C3A (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 72.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 32.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0883× (z -9.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 89.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -17.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -12.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC4]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[DNAJC4]] | +0.72 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[EGFL8]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.70 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[PMS2P4-1]] | +0.69 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[FAM193B]] | +0.69 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[SRP54]] | +0.68 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[TULP3]] | +0.67 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[MCEE]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.66 | +0.65 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[TTC9C]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | -0.73 | -0.68 / -0.75 | both halves | 7e-06 |  |
| [[SACS]] | -0.68 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[GMFB]] | -0.68 | -0.64 / -0.69 | both halves | 7e-06 |  |
| [[VMA21]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[CHML]] | -0.65 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[SLC25A24]] | -0.63 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ZNF518B]] | -0.63 | -0.57 / -0.70 | both halves | 9e-06 |  |
| [[ACTR3]] | -0.63 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[B3GALT9]] | -0.62 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[ACTB]] | -0.62 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[YWHAZ]] | -0.61 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[DNAH14]] | -0.60 | -0.58 / -0.67 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF518B]] | B | ZNF518B activity raises COG7's level | lines that do not express ZNF518B (16) vs lines expressing it (34) | 1.20× lower at baseline in the lines without ZNF518B | 0.014 | ⚠ within organs, on part of the lines; also absent: EHD3, KCNG1, TUB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 207]]; 15 genes; this gene is in the **+** arm (projection on the module's main direction 0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (-3.2, -18.7); signed map (-27.7, 8.9). **Vector** length 116, 36.4% of its response variance represented; |z| ≥ 3 in 1,252 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +11.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.6 | +2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +3.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +2.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.3 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +1.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.2 | -10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -10.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.6 | -5.3 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | component of oligomeric golgi complex 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:23,388,493-23,453,189 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Components of oligomeric golgi complex |
| Reactome | 9 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P83436](https://www.uniprot.org/uniprotkb/P83436) (Conserved oligomeric Golgi complex subunit 7):

> Required for normal Golgi function.

**Summary**, from NCBI Gene [91949](https://www.ncbi.nlm.nih.gov/gene/91949):

> The protein encoded by this gene resides in the golgi, and constitutes one of the 8 subunits of the conserved oligomeric Golgi (COG) complex, which is required for normal golgi morphology and localization. Mutations in this gene are associated with the congenital disorder of glycosylation type IIe.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:18622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18622) · Entrez [91949](https://www.ncbi.nlm.nih.gov/gene/91949) · UniProt [P83436](https://www.uniprot.org/uniprotkb/P83436) · Ensembl [ENSG00000168434](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168434)

## Data

Gene col 9650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9650); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9650]; `tensor/DDL_lfc|DDL_z.npy` [9650]; `embed/gene_vectors.npy` [9650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9650 or target_col == 9650). Every well: [[COG7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COG7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
