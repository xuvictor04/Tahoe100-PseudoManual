---
symbol: "ERGIC1"
type: "gene"
col: 3494
ensembl_id: "ENSG00000113719"
name: "endoplasmic reticulum-golgi intermediate compartment 1"
location: "5q35.1"
module: 97
arm: "+"
pooled_cpm: 140.37
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 27
n_dd_up_clean: 18
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# ERGIC1

*endoplasmic reticulum-golgi intermediate compartment 1* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +11.2, q 3e-26, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 1.44× (z +6.5, q 2e-08, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.236× (z -36.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP13]] (+0.67, fdr 1e-05), [[ABLIM3]] (+0.66, fdr 7e-06), [[ZHX3]] (+0.66, fdr 2e-05); moves opposite to [[LINC02100]] (-0.64, fdr 2e-05), [[TTC6]] (-0.60, fdr 5e-05), [[CTSS]] (-0.59, fdr 8e-05).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +11.2 | 3e-26 | 41/49 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.6 | 9e-12 | 33/43 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.44×** | +6.5 | 2e-08 | 28/48 (CFPAC-1, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.40×** | +6.1 | 2e-07 | 30/48 (SW 900, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +5.5 | 5e-06 | 31/45 (C-33 A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 3e-05 | 29/48 (SW 900, NCI-H460, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.30×** | +4.7 | 2e-04 | 25/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +4.7 | 2e-04 | 26/48 (NCI-H460, SW 900, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 7e-04 | 31/48 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.29×** | +4.4 | 7e-04 | 26/49 (SW 900, CFPAC-1, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.27×** | +4.3 | 8e-04 | 25/48 (SW 900, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.003 | 24/48 (SW 900, SNU-423, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.006 | 25/48 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.008 | 25/47 (SW 900, CFPAC-1, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.008 | 23/48 (SW 900, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.014 | 20/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.018 | 23/48 (CFPAC-1, SW 900, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.027 | 23/48 (SW 900, CFPAC-1, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.236×** | -36.6 | 0e+00 | 48/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.337×** | -19.5 | 0e+00 | 47/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.395×** | -16.0 | 0e+00 | 45/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.542×** | -15.5 | 0e+00 | 42/49 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.525×** | -11.5 | 9e-29 | 44/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.723×** | -8.2 | 2e-14 | 39/48 (J82, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.656×** | -7.5 | 4e-12 | 38/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -7.0 | 3e-10 | 37/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -6.6 | 2e-09 | 31/48 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.700×** | -6.4 | 9e-09 | 34/48 (J82, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.711×** | -6.1 | 5e-08 | 30/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.737×** | -5.5 | 2e-06 | 31/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.738×** | -5.4 | 2e-06 | 27/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -5.3 | 4e-06 | 33/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.568×** | -5.3 | 4e-06 | 32/49 (AsPC-1, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.782×** | -4.4 | 4e-04 | 25/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 175 | 16 | 6 | [[Budesonide (drug)]] 0.5 µM 2.50× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -37.8) |
| [[NCI-H460 (line)]] | wt | 135 | 5 | 9 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 2.23× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -39.8) |
| [[SW480 (line)]] | alt | 74.4 | 1 (1 ⚠) | 9 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -25.3) |
| [[CFPAC-1 (line)]] | alt | 112 | 5 | 4 | [[Clobetasol propionate (drug)]] 0.5 µM 2.31× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -26.8) |
| [[J82 (line)]] | alt | 224 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -31.6) |
| [[Hs 766T (line)]] | wt | 261 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -38.5) |
| [[LoVo (line)]] | wt | 77.1 | 1 (1 ⚠) | 7 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -24.1) |
| [[LS 180 (line)]] | wt | 215 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -28.9) |
| [[PANC-1 (line)]] | alt | 268 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -30.4) |
| [[AsPC-1 (line)]] | alt | 302 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0706× (z -44.1) |
| [[HOP62 (line)]] | alt | 242 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -33.0) |
| [[HT-29 (line)]] | alt | 156 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -38.1) |
| [[RKO (line)]] | wt | 73.4 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.7) |
| [[SNU-423 (line)]] | alt | 182 | 2 | 5 | [[Clobetasol propionate (drug)]] 0.5 µM 2.36× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -25.4) |
| [[hTERT-HPNE (line)]] | wt | 198 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -25.4) |
| [[NCI-H23 (line)]] | alt | 75.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -29.6) |
| [[A498 (line)]] | wt | 207 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -16.5) |
| [[A549 (line)]] | wt | 189 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -18.1) |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -17.6) |
| [[HS-578T (line)]] | alt | 163 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -15.7) |
| [[MIA PaCa-2 (line)]] | alt | 91.7 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0719× (z -30.5) |
| [[NCI-H1573 (line)]] | alt | 54.4 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -20.3) |
| [[Panc 03.27 (line)]] | alt | 103 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -23.4) |
| [[RPMI-7951 (line)]] | alt | 95.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -22.4) |
| [[SK-MEL-2 (line)]] | alt | 130 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -32.3) |
| [[SW1417 (line)]] | alt | 107 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -28.0) |
| [[A-427 (line)]] | wt | 97.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -26.1) |
| [[C32 (line)]] | wt | 59.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -13.7) |
| [[COLO 205 (line)]] | alt | 60.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -19.2) |
| [[KATO III (line)]] | alt | 79.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -18.0) |
| [[LOX-IMVI (line)]] | wt | 70.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 96.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -27.5) |
| [[HEC-1-A (line)]] | alt | 208 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -21.1) |
| [[NCI-H2030 (line)]] | alt | 68.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -20.8) |
| [[A-172 (line)]] | wt | 142 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -18.3) |
| [[BT-474 (line)]] | alt | 110 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -13.3) |
| [[C-33 A (line)]] | alt | 76.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.12× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -12.6) |
| [[H4 (line)]] | wt | 90.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.7) |
| [[HCT15 (line)]] | alt | 78.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -20.5) |
| [[SNU-1 (line)]] | wt | 53.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.4) |
| [[SW 1088 (line)]] | alt | 206 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.8) |
| [[SW48 (line)]] | wt | 81.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.5) |
| [[AN3 CA (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0994× (z -15.0) |
| [[NCI-H661 (line)]] | alt | 63.5 | 0 | 1 | — | [[MK-3903 (drug)]] 0.05 µM 0.0709× (z -10.2) |
| [[SHP-77 (line)]] | alt | 95.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -8.5) |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.107× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP13]] | +0.67 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ABLIM3]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ZHX3]] | +0.66 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[RPS6KA2]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TBC1D16]] | +0.64 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ABLIM2]] | +0.64 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[TANC2]] | +0.64 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MT1X]] | +0.64 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[HPCAL1]] | +0.62 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TOX2]] | +0.62 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[DENND3]] | +0.62 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[TBC1D8]] | +0.61 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02100]] | -0.64 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[TTC6]] | -0.60 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[CTSS]] | -0.59 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[SCAMP1-AS1]] | -0.58 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[IDO1]] | -0.58 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[PSMB8]] | -0.57 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[NMI]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[KMO]] | -0.57 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[LINC00944]] | -0.56 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[RASGRP3]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[FYB1]] | -0.56 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[GBP4]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises ERGIC1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[MLPH]] | B | MLPH activity raises ERGIC1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without MLPH | 0.069 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.822). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.2, 11.5); signed map (13.1, 34.4). **Vector** length 120, 42.5% of its response variance represented; |z| ≥ 3 in 1,775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.1 | +4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.8 | +3.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.5 | +4.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +5.8 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.5 | +6.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +5.5 | +3.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +5.4 | +4.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +5.3 | +4.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.9 | -15.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -9.5 | -8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | -6.7 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.8 | -6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -7.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -1.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.7 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | endoplasmic reticulum-golgi intermediate compartment 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:172,834,251-172,952,792 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERGIC32, ERGIC-32, KIAA1181, NET24 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969X5](https://www.uniprot.org/uniprotkb/Q969X5) (Endoplasmic reticulum-Golgi intermediate compartment protein 1):

> Possible role in transport between endoplasmic reticulum and Golgi.

**Summary**, from NCBI Gene [57222](https://www.ncbi.nlm.nih.gov/gene/57222):

> This gene encodes a cycling membrane protein which is an endoplasmic reticulum-golgi intermediate compartment (ERGIC) protein which interacts with other members of this protein family to increase their turnover. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29205) · Entrez [57222](https://www.ncbi.nlm.nih.gov/gene/57222) · UniProt [Q969X5](https://www.uniprot.org/uniprotkb/Q969X5) · Ensembl [ENSG00000113719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113719)

## Data

Gene col 3494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3494); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3494]; `tensor/DDL_lfc|DDL_z.npy` [3494]; `embed/gene_vectors.npy` [3494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3494 or target_col == 3494). Every well: [[ERGIC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERGIC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
