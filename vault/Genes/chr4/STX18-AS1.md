---
symbol: "STX18-AS1"
type: "gene"
col: 14504
ensembl_id: "ENSG00000247708"
name: "STX18 antisense RNA 1"
location: "4p16.2"
module: 4
arm: "+"
pooled_cpm: 30.0
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 34
n_dd_up_clean: 5
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# STX18-AS1

*STX18 antisense RNA 1* — 4p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.53× (z +4.7, q 0.001, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.294× (z -19.0, q 0e+00, down in 40 of 46 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.219× (z -16.7, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSEN2]] (+0.74, fdr 7e-06), [[MDN1]] (+0.72, fdr 7e-06), [[DPH6]] (+0.70, fdr 7e-06); moves opposite to [[SELENOK]] (-0.56, fdr 2e-05), [[SHOC2]] (-0.55, fdr 1e-05), [[ZFYVE1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SLC5A4-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +4.7 | 0.001 | 29/47 (SW480, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.022 | 26/46 (COLO 205, NCI-H1792, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.024 | 19/47 (BT-474, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.024 | 23/47 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.066 | 19/46 (A549, BT-474, …) | all doses, flat |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.31× | +3.0 | 0.23 | 8/47 (LS 180, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.294×** | -19.0 | 0e+00 | 40/46 (A498, NCI-H1573, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.219×** | -16.7 | 0e+00 | 46/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.298×** | -13.3 | 5e-38 | 42/46 (J82, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.367×** | -11.0 | 7e-26 | 44/46 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.349×** | -11.0 | 7e-26 | 41/47 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.410×** | -9.8 | 2e-20 | 40/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.415×** | -9.6 | 4e-20 | 40/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.421×** | -9.5 | 2e-19 | 40/46 (LoVo, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.440×** | -9.0 | 1e-17 | 35/46 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.240×** | -8.2 | 2e-14 | 38/47 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.253×** | -7.9 | 2e-13 | 37/45 (COLO 205, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.483×** | -7.6 | 2e-12 | 36/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.542×** | -6.3 | 1e-08 | 34/47 (SW480, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -6.1 | 5e-08 | 29/47 (LOX-IMVI, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.567×** | -5.9 | 1e-07 | 28/45 (HepG2/C3A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.756×** | -4.3 | 6e-04 | 26/47 (KATO III, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.669×** | -4.0 | 0.002 | 26/47 (PANC-1, AN3 CA, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.513×** | -3.8 | 0.004 | 26/45 (SW480, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -3.5 | 0.011 | 22/46 (C-33 A, MIA PaCa-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.734×** | -3.2 | 0.028 | 19/46 (H4, COLO 205, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -3.1 | 0.031 | 22/47 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.1 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -18.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.219× (z -11.3) |
| [[LoVo (line)]] | wt | 75.1 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0634× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -16.1) |
| [[PANC-1 (line)]] | alt | 19.2 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -20.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -16.0) |
| [[SW480 (line)]] | alt | 51.1 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 38.2 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0595× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -12.5) |
| [[A-427 (line)]] | wt | 54.4 | 0 | 7 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0909× (z -17.7) |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -16.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -9.4) |
| [[SNU-1 (line)]] | wt | 54.4 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0307× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0880× (z -14.3) |
| [[COLO 205 (line)]] | alt | 45.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -19.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0241× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 43.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -21.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -15.5) |
| [[A498 (line)]] | wt | 37.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0715× (z -22.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.8) |
| [[LS 180 (line)]] | wt | 42.4 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -9.7) |
| [[BT-474 (line)]] | alt | 17.7 | 0 | 4 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0817× (z -11.8) |
| [[C-33 A (line)]] | alt | 69.6 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.222× (z -10.7) |
| [[C32 (line)]] | wt | 23.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 28.6 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -9.1) |
| [[HOP62 (line)]] | alt | 21.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -9.6) |
| [[J82 (line)]] | alt | 24.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0237× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 44.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -12.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -11.6) |
| [[SW1417 (line)]] | alt | 20.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -9.6) |
| [[SW48 (line)]] | wt | 54.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -9.0) |
| [[A549 (line)]] | wt | 16.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -11.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 58.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.354× (z -9.5) |
| [[RKO (line)]] | wt | 24.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -13.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -10.8) |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -15.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -10.3) |
| [[HT-29 (line)]] | alt | 14.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0805× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.191× (z -10.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 1271 (line)]] | alt | 44.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0318× (z -10.5) |
| [[A-172 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -9.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0891× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -12.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.140× (z -9.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 8.45 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -8.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[KATO III (line)]] | alt | 24.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0384× (z -15.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[AsPC-1 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSEN2]] | +0.74 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[MDN1]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DPH6]] | +0.70 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[CLYBL]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[CAD]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[CMSS1]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.64 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[PFAS]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[NUBPL]] | +0.63 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[NAA15]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[METAP1D]] | +0.62 | +0.65 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.56 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[SHOC2]] | -0.55 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[OTUD5]] | -0.54 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[TP53INP2]] | -0.53 | -0.36 / -0.58 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity raises STX18-AS1's level | lines that do not express SLC5A4-AS1 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without SLC5A4-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888 |
| [[WWOX]] | B | WWOX activity raises STX18-AS1's level | lines that do not express WWOX (5) vs lines expressing it (45) | 2.31× lower at baseline in the lines without WWOX | 0.059 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent |
| [[SLC5A4-AS1]] | B | SLC5A4-AS1 activity strengthens STX18-AS1's drug response | lines that do not express SLC5A4-AS1 (14) vs lines expressing it (33) | the lines without SLC5A4-AS1 respond 0.77× as strongly (z diff +1.43); strongest at Ixazomib citrate 5 µM: 0.52x vs 0.37x (z diff +2.5) | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000290888; target measured in part of the lines; artifact flags |
| [[ENTPD1-AS1]] | C | ENTPD1-AS1 activity raises STX18-AS1's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 2.62× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.5, -36.4); signed map (-6.2, -49.6). **Vector** length 68.5, 17.1% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | -0.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.7 | -19.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.3 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | +0.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -1.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | STX18 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p16.2 — chr4:4,542,131-4,787,359 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48877) · Entrez [100507266](https://www.ncbi.nlm.nih.gov/gene/100507266) · Ensembl [ENSG00000247708](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247708)

## Data

Gene col 14504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14504); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14504]; `tensor/DDL_lfc|DDL_z.npy` [14504]; `embed/gene_vectors.npy` [14504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14504 or target_col == 14504). Every well: [[STX18-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX18-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
