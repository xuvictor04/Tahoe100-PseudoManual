---
symbol: "NR1D1"
type: "gene"
col: 4731
ensembl_id: "ENSG00000126368"
name: "nuclear receptor subfamily 1 group D member 1"
location: "17q21.1"
module: 14
arm: "+"
pooled_cpm: 36.55
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NR1D1

*nuclear receptor subfamily 1 group D member 1* — 17q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 14.7× (z +32.2, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.522× (z -5.6, q 1e-05, down in 18 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.387× (z -4.5, q 0.002, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKB2]] (+0.71, fdr 7e-06), [[NFKBIE]] (+0.68, fdr 7e-06), [[BHLHE40]] (+0.67, fdr 7e-06); moves opposite to [[PDS5A]] (-0.61, fdr 8e-06), [[KPNB1]] (-0.61, fdr 2e-05), [[OPA1]] (-0.61, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NEURL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **14.7×** | +32.2 | 0e+00 | 44/45 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **9.85×** | +19.7 | 0e+00 | 45/45 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.82×** | +17.2 | 0e+00 | 43/45 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.85×** | +14.1 | 5e-43 | 42/45 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.93×** | +12.2 | 3e-32 | 44/46 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **11.8×** | +11.5 | 9e-29 | 46/47 (COLO 205, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.38×** | +10.9 | 1e-25 | 43/45 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.53×** | +8.3 | 8e-15 | 37/46 (A549, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.36×** | +7.7 | 1e-12 | 39/46 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.22×** | +6.7 | 1e-09 | 36/45 (NCI-H2347, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.06×** | +6.4 | 6e-09 | 36/46 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.83×** | +5.2 | 1e-05 | 34/44 (COLO 205, NCI-H460, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +5.1 | 2e-05 | 33/46 (KATO III, Panc 03.27, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.54×** | +3.8 | 0.005 | 22/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~88% of this change | **1.50×** | +3.6 | 0.012 | 21/45 (HOP62, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.014 | 25/46 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.044 | 19/44 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.085 | 16/47 (HCT15, PANC-1, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.085 | 19/46 (SHP-77, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4731.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -5.6 | 1e-05 | 18/32 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.387×** | -4.5 | 0.002 | 32/45 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.615×** | -4.4 | 0.002 | 32/46 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.646×** | -3.9 | 0.010 | 28/46 (PANC-1, NCI-H460, …) | all doses, flat | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.630×** | -3.9 | 0.010 | 25/46 (H4, SW 1271, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.489×** | -3.4 | 0.073 | 25/46 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.691×** | -3.3 | 0.073 | 23/46 (NCI-H1573, J82, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | **0.764×** | -3.2 | 0.083 | 18/46 (LOX-IMVI, A-172, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.508×** | -3.2 | 0.088 | 20/46 (NCI-H1792, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.705×** | -3.1 | 0.088 | 17/46 (HOP62, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.705×** | -3.1 | 0.088 | 20/46 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.709×** | -3.1 | 0.089 | 23/46 (H4, SW 1088, …) | all doses, flat | position effect removed |
| [[Brimonidine (drug)]] 5 µM |  | **0.710×** | -3.1 | 0.089 | 19/46 (SW1417, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.711×** | -3.1 | 0.089 | 20/46 (SHP-77, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~20% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.86 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 44.6 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +20.8) | — |
| [[KATO III (line)]] | alt | 28.2 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +23.8) | — |
| [[AsPC-1 (line)]] | alt | 39.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.7× (z +30.2) | — |
| [[COLO 205 (line)]] | alt | 40.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 50.3× (z +27.8) | — |
| [[SW480 (line)]] | alt | 28.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +18.5) | — |
| [[A549 (line)]] | wt | 34.1 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 26.8× (z +23.9) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 31.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +25.0) | — |
| [[HepG2_C3A (line)]] | wt | 30.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 33.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 61.9 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.100× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 53.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +27.6) | — |
| [[A-172 (line)]] | wt | 76.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +23.4) | — |
| [[Hs 766T (line)]] | wt | 61.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +20.8) | — |
| [[HT-29 (line)]] | alt | 47.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +14.0) | — |
| [[LoVo (line)]] | wt | 17.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +20.9) | — |
| [[NCI-H1792 (line)]] | alt | 32.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +20.2) | — |
| [[PANC-1 (line)]] | alt | 28.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.27× (z +19.0) | — |
| [[A-427 (line)]] | wt | 17.6 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 18.8× (z +13.4) | — |
| [[A498 (line)]] | wt | 44.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +22.3) | — |
| [[C32 (line)]] | wt | 39.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.9× (z +20.8) | — |
| [[HS-578T (line)]] | alt | 52.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +20.1) | — |
| [[J82 (line)]] | alt | 28.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +20.2) | — |
| [[NCI-H2347 (line)]] | alt | 55.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +22.2) | — |
| [[Panc 03.27 (line)]] | alt | 33.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +21.4) | — |
| [[RPMI-7951 (line)]] | alt | 60.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +16.8) | — |
| [[SW 900 (line)]] | alt | 25.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +17.5) | — |
| [[CFPAC-1 (line)]] | alt | 51.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 70.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +20.7) | — |
| [[hTERT-HPNE (line)]] | wt | 45.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +18.5) | — |
| [[LS 180 (line)]] | wt | 11.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +16.3) | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +17.2) | — |
| [[SNU-423 (line)]] | alt | 36.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +17.9) | — |
| [[H4 (line)]] | wt | 46.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +17.8) | — |
| [[HCT15 (line)]] | alt | 29.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +16.2) | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +11.5) | — |
| [[SK-MEL-2 (line)]] | alt | 35.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +19.5) | — |
| [[SNU-1 (line)]] | wt | 22.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.39× (z +11.4) | — |
| [[SW48 (line)]] | wt | 20.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +15.2) | — |
| [[CHP-212 (line)]] | wt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +13.0) | — |
| [[SW 1088 (line)]] | alt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.9× (z +10.5) | — |
| [[SW 1271 (line)]] | alt | 61.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKB2]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[NFKBIE]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[BHLHE40]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 | pathway: Circadian clock; STRING 929 |
| [[ARRDC3]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[BCOR]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[PIM3]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[KLF10]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[NINJ1]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[IRF1]] | +0.62 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SOX9]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[N4BP3]] | +0.62 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZNF217]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDS5A]] | -0.61 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[KPNB1]] | -0.61 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[OPA1]] | -0.61 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[VTI1A]] | -0.60 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[TRRAP]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[COP1]] | -0.60 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[ADPGK]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[HERC2]] | -0.59 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[POP1]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[AHSA1]] | -0.57 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[UFD1]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL3]] | B | NEURL3 activity raises NR1D1's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without NEURL3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[TNFAIP2]] | B | TNFAIP2 activity raises NR1D1's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.60× lower at baseline in the lines without TNFAIP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[GATA6]] | B | GATA6 activity raises NR1D1's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without GATA6 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[HCP5]] | B | HCP5 activity raises NR1D1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.49× lower at baseline in the lines without HCP5 | 0.040 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[IL2RG]] | B | IL2RG activity raises NR1D1's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without IL2RG | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[SOX9]] | B | SOX9 activity raises NR1D1's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without SOX9 | 0.053 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.7, -3.3); signed map (-2.4, 12.9). **Vector** length 108, 34.9% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.2 | +14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +17.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +8.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.0 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.6 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.2 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | -6.6 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -0.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 1 group D member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.1 — chr17:40,092,793-40,100,589 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ear-1, hRev, Rev-ErbAalpha, THRA1, REVERBA, REVERBalpha; previously THRAL |
| Gene groups (HGNC) | Nuclear receptor subfamily 1 group D |
| Reactome | 16 pathways, smallest: Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex; Phosphorylated BMAL1:CLOCK (ARNTL:CLOCK) activates expression of core clock genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P20393](https://www.uniprot.org/uniprotkb/P20393) (Nuclear receptor subfamily 1 group D member 1):

> Transcriptional repressor which coordinates circadian rhythm and metabolic pathways in a heme-dependent manner. Integral component of the complex transcription machinery that governs circadian rhythmicity and forms a critical negative limb of the circadian clock by directly repressing the expression of core clock components BMAL1, CLOCK and CRY1. Also regulates genes involved in metabolic functions, including lipid and bile acid metabolism, adipogenesis, gluconeogenesis and the macrophage …

**Summary**, from NCBI Gene [9572](https://www.ncbi.nlm.nih.gov/gene/9572):

> This gene encodes a transcription factor that is a member of the nuclear receptor subfamily 1. The encoded protein is a ligand-sensitive transcription factor that negatively regulates the expression of core clock proteins. In particular this protein represses the circadian clock transcription factor aryl hydrocarbon receptor nuclear translocator-like protein 1 (ARNTL). This protein may also be involved in regulating genes that function in metabolic, inflammatory and cardiovascular processes. …

**Accessions** — [HGNC:7962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7962) · Entrez [9572](https://www.ncbi.nlm.nih.gov/gene/9572) · UniProt [P20393](https://www.uniprot.org/uniprotkb/P20393) · Ensembl [ENSG00000126368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126368)

## Data

Gene col 4731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4731); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4731]; `tensor/DDL_lfc|DDL_z.npy` [4731]; `embed/gene_vectors.npy` [4731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4731 or target_col == 4731). Every well: [[NR1D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR1D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
