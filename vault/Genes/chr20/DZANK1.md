---
symbol: "DZANK1"
type: "gene"
col: 1568
ensembl_id: "ENSG00000089091"
name: "double zinc ribbon and ankyrin repeat domains 1"
location: "20p11.23"
module: 205
arm: "+"
pooled_cpm: 12.13
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 19
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# DZANK1

*double zinc ribbon and ankyrin repeat domains 1* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.36× (z +19.3, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.391× (z -12.3, q 5e-32, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.397× (z -12.1, q 3e-31, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEP89]] (+0.73, fdr 7e-06), [[SLC25A14]] (+0.60, fdr 4e-05), [[TCTN2]] (+0.58, fdr 3e-05); moves opposite to [[NTRK3]] (-0.56, fdr 2e-04), [[SOHLH2]] (-0.53, fdr 7e-04), [[GPM6A]] (-0.51, fdr 4e-04).
> It is in [[Module 205]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.36×** | +19.3 | 0e+00 | 47/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.91×** | +17.9 | 0e+00 | 46/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.32×** | +15.7 | 0e+00 | 45/47 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +12.7 | 1e-34 | 41/45 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +8.3 | 1e-14 | 28/44 (SNU-423, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +8.2 | 3e-14 | 31/47 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.66×** | +6.6 | 3e-09 | 22/42 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.8 | 4e-07 | 26/47 (SW480, SW1417, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.31×** | +5.7 | 6e-07 | 25/47 (SW480, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.35×** | +5.5 | 2e-06 | 18/47 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.2 | 1e-05 | 21/46 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.33×** | +3.7 | 0.009 | 12/47 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.33×** | +3.7 | 0.009 | 9/46 (SHP-77, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.009 | 10/47 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.3 | 0.033 | 1/47 (NCI-H23) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.033 | 10/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.034 | 14/46 (SW480, SNU-423, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.065 | 6/47 (LoVo, HCT15, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.068 | 3/47 (NCI-H2347, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1568.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.391×** | -12.3 | 5e-32 | 38/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.397×** | -12.1 | 3e-31 | 35/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -8.0 | 2e-13 | 35/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.543×** | -8.0 | 2e-13 | 35/46 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.620×** | -6.3 | 4e-08 | 25/46 (H4, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.639×** | -5.9 | 4e-07 | 25/46 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.681×** | -4.8 | 1e-04 | 21/40 (SNU-423, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.510×** | -4.6 | 3e-04 | 13/42 (LS 180, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.707×** | -4.6 | 3e-04 | 21/46 (SW 1271, MIA PaCa-2, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -4.5 | 4e-04 | 22/47 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.786×** | -4.5 | 4e-04 | 24/47 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.723×** | -4.3 | 9e-04 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.707×** | -4.2 | 0.001 | 15/27 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -3.9 | 0.003 | 18/46 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.592×** | -3.6 | 0.012 | 20/47 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.786×** | -3.0 | 0.069 | 12/46 (SW48, A-427, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.8 | 4 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.68× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.195× (z -11.4) |
| [[PANC-1 (line)]] | alt | 14.8 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.15× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.173× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -11.9) |
| [[LoVo (line)]] | wt | 4.09 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 15.4× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0866× (z -9.7) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0351× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -9.4) |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0628× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 11.0 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 6.22× (z +11.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -10.0) |
| [[A498 (line)]] | wt | 14.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.19× (z +12.6) | — |
| [[A549 (line)]] | wt | 21.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.39× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 18.2 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.20× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.0861× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.132× (z -10.0) |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -9.1) |
| [[HT-29 (line)]] | alt | 6.73 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +9.9) | — |
| [[KATO III (line)]] | alt | 6.53 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 17.0× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.37× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -9.7) ⚠ toxic |
| [[RKO (line)]] | wt | 7.84 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 12.6× (z +9.8) | [[Oxaprozin (drug)]] 0.05 µM 0.0635× (z -10.7) |
| [[H4 (line)]] | wt | 10.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0520× (z -10.5) |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0802× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 0.05 µM 0.0876× (z -8.9) |
| [[Hs 766T (line)]] | wt | 7.60 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 9.87× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.0521× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 27.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -11.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 33.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -9.3) |
| [[A-427 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.117× (z -9.2) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 3.65 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.3× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.44× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 7.64 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 15.2× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 6.08 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.0× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.60× (z +9.0) | — |
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP89]] | +0.73 | +0.60 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SLC25A14]] | +0.60 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[TCTN2]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ZNF487]] | +0.58 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[ANKRD42]] | +0.56 | +0.44 / +0.61 | both halves | 3e-05 | same gene group |
| [[FAM174A]] | +0.56 | +0.27 / +0.62 | both halves | 3e-04 |  |
| [[TMEM67]] | +0.55 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[ULK4]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[RNF213-AS1]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CCDC157]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ZNF324]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ALDH6A1]] | +0.53 | +0.30 / +0.48 | both halves | 2e-04 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTRK3]] | -0.56 | -0.30 / -0.62 | both halves | 2e-04 |  |
| [[SOHLH2]] | -0.53 | -0.21 / -0.45 | both halves | 7e-04 |  |
| [[GPM6A]] | -0.51 | -0.24 / -0.45 | both halves | 4e-04 |  |
| [[LINC00592]] | -0.51 | -0.13 / -0.46 | ⚠ not reproduced | 0.002 |  |
| [[DMD]] | -0.50 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[KCND3]] | -0.50 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[TRIM58]] | -0.50 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[PDGFD]] | -0.49 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[PPFIA2]] | -0.49 | -0.17 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[DSEL]] | -0.48 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[CCDC169]] | -0.48 | -0.20 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[SLC47A1]] | -0.48 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[TMEFF2]] | -0.48 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[ENAH]] | -0.48 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[RGS7]] | -0.48 | -0.24 / -0.46 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DZANK1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NUDT11]] | B | NUDT11 activity raises DZANK1's level | lines that do not express NUDT11 (24) vs lines expressing it (26) | 1.62× lower at baseline in the lines without NUDT11 | 0.026 | ⚠ within organs, on part of the lines; also absent: RNF182, ADAMTS10, NPTX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.6, 21.7); signed map (-19.8, 5.0). **Vector** length 58.6, 9.70% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.1 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.5 | +19.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.5 | +17.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.2 | +15.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +0.9 | +1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +0.8 | +1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +0.8 | +0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +0.8 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.5 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -6.7 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | -3.3 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.1 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | double zinc ribbon and ankyrin repeat domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:18,383,367-18,467,281 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10600, dJ568F9.2, FLJ30892, bA189K21.8, ANKRD64; previously C20orf84, C20orf12 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVP4](https://www.uniprot.org/uniprotkb/Q9NVP4) (Double zinc ribbon and ankyrin repeat-containing protein 1):

> Involved in vesicle transport in photoreceptor cells.

**Summary**, from NCBI Gene [55184](https://www.ncbi.nlm.nih.gov/gene/55184):

> This gene contains two ankyrin repeat-encoding regions. Ankyrin repeats are tandemly repeated modules of about 33 amino acids described as L-shaped structures consisting of a beta-hairpin and two alpha-helices. Ankyrin repeats occur in a large number of functionally diverse proteins, mainly from eukaryotes, and are known to function as protein-protein interaction domains. [provided by RefSeq, Dec 2018]

**Accessions** — [HGNC:15858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15858) · Entrez [55184](https://www.ncbi.nlm.nih.gov/gene/55184) · UniProt [Q9NVP4](https://www.uniprot.org/uniprotkb/Q9NVP4) · Ensembl [ENSG00000089091](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089091)

## Data

Gene col 1568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1568); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1568]; `tensor/DDL_lfc|DDL_z.npy` [1568]; `embed/gene_vectors.npy` [1568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1568 or target_col == 1568). Every well: [[DZANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DZANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
