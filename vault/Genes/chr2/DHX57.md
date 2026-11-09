---
symbol: "DHX57"
type: "gene"
col: 8653
ensembl_id: "ENSG00000163214"
name: "DExH-box helicase 57"
location: "2p22.1"
module: 129
arm: "+"
pooled_cpm: 56.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# DHX57

*DExH-box helicase 57* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.06× (z +18.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.494× (z -17.1, q 0e+00, down in 34 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.695× (z -9.2, q 7e-18, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CINP]] (+0.77, fdr 7e-06), [[POLR3A]] (+0.76, fdr 7e-06), [[CDK5RAP1]] (+0.74, fdr 7e-06); moves opposite to [[MOB1A]] (-0.64, fdr 1e-05), [[CD164]] (-0.63, fdr 1e-05), [[PRKAR1A]] (-0.63, fdr 1e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF420]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +18.2 | 0e+00 | 46/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +16.9 | 0e+00 | 47/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +16.0 | 0e+00 | 45/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +11.8 | 6e-30 | 41/49 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +10.2 | 2e-22 | 41/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +9.9 | 3e-21 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +7.7 | 1e-12 | 31/47 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +7.6 | 3e-12 | 34/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +6.9 | 3e-10 | 29/48 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +6.6 | 2e-09 | 30/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +6.6 | 2e-09 | 37/48 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +5.3 | 6e-06 | 21/48 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.15× | +5.0 | 3e-05 | 17/48 (HS-578T, KATO III, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.9 | 3e-05 | 20/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 3e-04 | 21/48 (COLO 205, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 0.001 | 11/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.036 | 8/48 (LS 180, hTERT-HPNE, …) | two highest doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.043 | 6/49 (HT-29, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8653.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -17.1 | 0e+00 | 34/43 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.530×** | -16.0 | 0e+00 | 35/49 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -13.4 | 2e-38 | 36/45 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -9.2 | 7e-18 | 37/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -8.3 | 1e-14 | 32/47 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.733×** | -7.8 | 4e-13 | 29/48 (NCI-H460, SW 1088, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.739×** | -7.6 | 2e-12 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -6.9 | 3e-10 | 24/48 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -5.7 | 1e-06 | 24/48 (A498, CHP-212, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.661×** | -5.5 | 3e-06 | 22/48 (SW480, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -5.1 | 2e-05 | 20/49 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Gefitinib (drug)]] 5 µM |  | 0.872× | -3.4 | 0.027 | 15/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.4 | 0.027 | 18/48 (RKO, A-172, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.872× | -3.3 | 0.038 | 14/47 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.878× | -3.1 | 0.074 | 5/48 (KATO III, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 65.7 | 3 | 9 (7 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.06× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -15.1) |
| [[PANC-1 (line)]] | alt | 59.1 | 4 | 6 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.19× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.417× (z -13.5) |
| [[SW480 (line)]] | alt | 68.0 | 4 | 5 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.04× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.275× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -10.6) |
| [[A-427 (line)]] | wt | 92.3 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.07× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 120 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.25× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -19.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 47.8 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 93.4 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.91× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -16.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 51.3 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 90.4 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.471× (z -9.7) |
| [[A-172 (line)]] | wt | 43.6 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.52× (z +8.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 57.3 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 55.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -12.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 17.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.51× (z +11.4) | — |
| [[LoVo (line)]] | wt | 37.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +10.8) | — |
| [[C32 (line)]] | wt | 44.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 63.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 52.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.37× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.454× (z -8.6) ⚠ toxic |
| [[KATO III (line)]] | alt | 44.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -14.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 22.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.26× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -31.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 37.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.20× (z +9.2) | — |
| [[RKO (line)]] | wt | 59.4 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 75.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -17.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 48.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.62× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -13.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 96.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -10.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 43.9 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.340× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CINP]] | +0.77 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[POLR3A]] | +0.76 | +0.67 / +0.73 | both halves | 7e-06 | STRING 467 |
| [[CDK5RAP1]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[KLHL20]] | +0.73 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[DDX55]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 | STRING 409 |
| [[ZNF329]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[NVL]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[PPIL2]] | +0.70 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF461]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[GTF2H2]] | +0.70 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.69 | +0.79 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.64 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[CD164]] | -0.63 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.63 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[LSMEM1]] | -0.61 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[UBE2A]] | -0.60 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[EDEM1]] | -0.59 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[DDX3X]] | -0.59 | -0.40 / -0.53 | both halves | 5e-05 | STRING 503 |
| [[EIF4G2]] | -0.59 | -0.37 / -0.55 | both halves | 9e-05 |  |
| [[CHRAC1]] | -0.59 | -0.54 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF420]] | B | ZNF420 activity raises DHX57's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 1.70× lower at baseline in the lines without ZNF420 | 0.041 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |
| [[ZNF71]] | B | ZNF71 activity raises DHX57's level | lines that do not express ZNF71 (15) vs lines expressing it (35) | 1.51× lower at baseline in the lines without ZNF71 | 0.076 | ⚠ within organs, on part of the lines; also absent: ZIM2-AS1, ZNF470, ZFP28 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.761). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.4, -8.2); signed map (-17.5, -18.5). **Vector** length 119, 34.0% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.3 | +11.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.9 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.1 | +7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.1 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +4.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.9 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.8 | -9.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.2 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.1 | -8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.8 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | DExH-box helicase 57 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:38,797,729-38,875,934 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DDX57 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; DEAH-box helicases; RWD domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P158](https://www.uniprot.org/uniprotkb/Q6P158) (Putative ATP-dependent RNA helicase DHX57):

> Probable ATP-binding RNA helicase.

**Summary**, from NCBI Gene [90957](https://www.ncbi.nlm.nih.gov/gene/90957):

> Enables RNA binding activity. Predicted to be involved in positive regulation of translation. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20086) · Entrez [90957](https://www.ncbi.nlm.nih.gov/gene/90957) · UniProt [Q6P158](https://www.uniprot.org/uniprotkb/Q6P158) · Ensembl [ENSG00000163214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163214)

## Data

Gene col 8653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8653); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8653]; `tensor/DDL_lfc|DDL_z.npy` [8653]; `embed/gene_vectors.npy` [8653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8653 or target_col == 8653). Every well: [[DHX57 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX57.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
