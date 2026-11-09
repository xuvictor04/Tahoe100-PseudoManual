---
symbol: "LIF"
type: "gene"
col: 4879
ensembl_id: "ENSG00000128342"
name: "LIF interleukin 6 family cytokine"
location: "22q12.2"
module: 112
arm: "+"
pooled_cpm: 37.43
n_lines_expressing: 40
n_dd_up: 17
n_dd_down: 66
n_dd_up_clean: 11
n_dd_down_clean: 53
in_vector_space: true
direction_upstream: 16
direction_downstream: 14
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# LIF

*LIF interleukin 6 family cytokine* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.41× (z +10.1, q 2e-21, up in 24 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 66 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.123× (z -24.7, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF1]] (+0.75, fdr 7e-06), [[LINC00973]] (+0.72, fdr 7e-06), [[PHLDA1]] (+0.72, fdr 7e-06); moves opposite to [[CLASP1]] (-0.59, fdr 1e-05), [[TSC22D3]] (-0.55, fdr 1e-05), [[CMKLR2]] (-0.55, fdr 1e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[DELEC1]] → it (grade B ⚠); 14 go from it, the strongest it → [[ETV3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +10.1 | 2e-21 | 24/37 (A498, C32, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +8.2 | 6e-14 | 27/38 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +7.0 | 5e-10 | 21/38 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +5.7 | 2e-06 | 23/37 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +5.1 | 3e-05 | 23/38 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +5.1 | 3e-05 | 20/34 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +5.0 | 4e-05 | 25/38 (RPMI-7951, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.31×** | +4.6 | 3e-04 | 20/37 (A498, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 7e-04 | 20/38 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.001 | 21/38 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.003 | 18/38 (NCI-H460, C32, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.8 | 0.006 | 19/38 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.018 | 13/37 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.4 | 0.024 | 12/36 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.4 | 0.030 | 17/37 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bexarotene (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.031 | 11/38 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.051 | 13/37 (SW48, NCI-H2030, …) | two highest doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 68 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 66 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.123×** | -24.7 | 0e+00 | 37/38 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.126×** | -24.3 | 0e+00 | 37/38 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.167×** | -21.0 | 0e+00 | 36/38 (SW 900, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.506×** | -11.3 | 2e-27 | 29/38 (SW 900, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Cobimetinib (drug)]] 5 µM | ⚠ position correction uncertain | **0.390×** | -10.6 | 3e-24 | 36/37 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.500×** | -10.0 | 1e-21 | 32/38 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.426×** | -10.0 | 1e-21 | 35/38 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.433×** | -10.0 | 1e-21 | 34/38 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.548×** | -8.5 | 2e-15 | 31/38 (SW480, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.490×** | -8.4 | 3e-15 | 31/37 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.245×** | -8.4 | 3e-15 | 34/38 (SW 900, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.501×** | -8.1 | 3e-14 | 32/38 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.518×** | -8.1 | 3e-14 | 31/38 (SW480, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.490×** | -8.0 | 3e-14 | 31/37 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.526×** | -7.5 | 2e-12 | 24/38 (NCI-H1573, hTERT-HPNE, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.528×** | -7.5 | 3e-12 | 34/38 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.557×** | -6.9 | 2e-10 | 27/38 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 79.4 | 0 | 26 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0583× (z -21.7) |
| [[HOP62 (line)]] | alt | 56.9 | 1 | 14 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.87× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.0928× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 64.8 | 0 | 15 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0750× (z -17.8) |
| [[A498 (line)]] | wt | 85.8 | 6 (1 ⚠) | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +20.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.04× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.168× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 70.5 | 1 (1 ⚠) | 13 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.10× (z +9.5) ⚠ unreliable plate only | [[Panobinostat (drug)]] 0.5 µM 0.0678× (z -18.1) |
| [[NCI-H460 (line)]] | wt | 45.6 | 9 (2 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +14.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.16× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.0749× (z -20.8) |
| [[NCI-H2030 (line)]] | alt | 61.8 | 1 | 11 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 6.63× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -14.0) |
| [[SW480 (line)]] | alt | 14.5 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0627× (z -16.9) |
| [[SW 900 (line)]] | alt | 83.6 | 0 | 11 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0867× (z -18.5) |
| [[hTERT-HPNE (line)]] | wt | 52.3 | 3 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.20× (z +15.6) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 11.0× (z +12.8) | [[Ponatinib (drug)]] 5 µM 0.136× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 58.2 | 4 (2 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +10.5) | [[Adagrasib (drug)]] 0.05 µM 0.485× (z -18.8) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.106× (z -16.5) |
| [[SW48 (line)]] | wt | 31.7 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0709× (z -12.0) |
| [[HS-578T (line)]] | alt | 62.2 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +12.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.81× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.0613× (z -18.6) |
| [[SNU-423 (line)]] | alt | 64.7 | 2 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +13.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.91× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.0528× (z -21.0) |
| [[A-172 (line)]] | wt | 41.0 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.6) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 12.4× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.0651× (z -19.4) |
| [[AsPC-1 (line)]] | alt | 38.8 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +14.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.72× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 79.5 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0922× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 35.1 | 3 (1 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 5.93× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.126× (z -11.5) |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0458× (z -16.2) |
| [[A549 (line)]] | wt | 58.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0663× (z -19.7) |
| [[C32 (line)]] | wt | 17.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 25.3× (z +13.6) | — |
| [[RKO (line)]] | wt | 54.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -13.8) |
| [[H4 (line)]] | wt | 26.3 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 8.77× (z +12.3) ⚠ cell-cycle shift, explains ~58% of this change | [[Panobinostat (drug)]] 5 µM 0.0927× (z -9.3) |
| [[J82 (line)]] | alt | 24.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -12.0) |
| [[LS 180 (line)]] | wt | 16.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0463× (z -16.1) |
| [[PANC-1 (line)]] | alt | 31.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0913× (z -18.5) |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -9.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0955× (z -8.9) |
| [[SW1417 (line)]] | alt | 39.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -14.8) |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 23.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -13.1) |
| [[COLO 205 (line)]] | alt | 19.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0478× (z -9.6) |
| [[HT-29 (line)]] | alt | 9.78 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0776× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 13.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.124× (z -9.5) |
| [[A-427 (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.66 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.74 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF1]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[LINC00973]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[CXCL8]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 731 |
| [[IER3]] | +0.70 | +0.68 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[CSF2]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 780 |
| [[FOSL1]] | +0.67 | +0.71 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[HCG20]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SHB]] | +0.66 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[GOLGA7B]] | +0.66 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[EHD1]] | +0.66 | +0.71 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[B4GALT6]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLASP1]] | -0.59 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TSC22D3]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[CMKLR2]] | -0.55 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[TNRC6A]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R12B]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DELEC1]] | B | DELEC1 activity raises LIF's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 3.21× lower at baseline in the lines without DELEC1 | 0.007 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[CD274]] | B | CD274 activity raises LIF's level | lines that do not express CD274 (18) vs lines expressing it (32) | 2.79× lower at baseline in the lines without CD274 | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[RUNX1]] | B | RUNX1 activity raises LIF's level | lines that do not express RUNX1 (5) vs lines expressing it (45) | 3.21× lower at baseline in the lines without RUNX1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: KIFC3, STAMBPL1, TRIB1; maybe low, not absent |
| [[CEMIP]] | B | CEMIP activity raises LIF's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without CEMIP | 0.030 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[KIAA1217]] | B | KIAA1217 activity raises LIF's level | lines that do not express KIAA1217 (10) vs lines expressing it (40) | 2.42× lower at baseline in the lines without KIAA1217 | 0.036 | ⚠ within organs, on part of the lines; also absent: FAM107B, MET, S100A16 |
| [[PHLDA2]] | B | PHLDA2 activity raises LIF's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 3.35× lower at baseline in the lines without PHLDA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[ANXA10]] | B | ANXA10 activity raises LIF's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 2.23× lower at baseline in the lines without ANXA10 | 0.044 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP |
| [[GEM]] | B | GEM activity raises LIF's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.41× lower at baseline in the lines without GEM | 0.059 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[ROR1-AS1]] | B | ROR1-AS1 activity raises LIF's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.17× lower at baseline in the lines without ROR1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2 |
| [[CD44]] | B | CD44 activity raises LIF's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without CD44 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[G0S2]] | B | G0S2 activity raises LIF's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.49× lower at baseline in the lines without G0S2 | 0.077 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[ARC]] | B | ARC activity raises LIF's level | lines that do not express ARC (19) vs lines expressing it (31) | 1.26× lower at baseline in the lines without ARC | 0.086 | ⚠ within organs, on part of the lines; also absent: PCSK2, ENSG00000259345, SNAP25; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETV3]] | B | LIF activity raises ETV3's level | lines that do not express LIF (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without LIF | 0.039 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[GJC1]] | B | LIF activity strengthens GJC1's drug response | lines that do not express LIF (7) vs lines expressing it (28) | the lines without LIF respond 0.47× as strongly (z diff +1.98); strongest at Homoharringtonine 5 µM: 1.25x vs 2.39x (z diff +3.6) | 0.047 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213; target measured in part of the lines; the reference differs; artifact flags |
| [[IER3]] | B | LIF activity raises IER3's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.39× lower at baseline in the lines without LIF | 0.053 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[TSC22D3]] | B | LIF activity raises TSC22D3's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without LIF | 0.063 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[FAM107B]] | B | LIF activity raises FAM107B's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without LIF | 0.067 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[ZNF697]] | B | LIF activity raises ZNF697's level | lines that do not express LIF (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without LIF | 0.081 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[FAM43A]] | B | LIF activity raises FAM43A's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without LIF | 0.084 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[BHLHE40]] | B | LIF activity raises BHLHE40's level | lines that do not express LIF (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without LIF | 0.084 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[ZFPM2-AS1]] | B | LIF activity raises ZFPM2-AS1's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.98× lower at baseline in the lines without LIF | 0.092 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[ROR1-AS1]] | B | LIF activity raises ROR1-AS1's level | lines that do not express LIF (10) vs lines expressing it (40) | 2.12× lower at baseline in the lines without LIF | 0.095 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[BCAN-AS1]] | B | LIF activity raises BCAN-AS1's level | lines that do not express LIF (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without LIF | 0.096 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[LIF-AS2]] | B | LIF activity raises LIF-AS2's level | lines that do not express LIF (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without LIF | 0.098 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.5, 1.4); signed map (9.5, 45.1). **Vector** length 127, 43.6% of its response variance represented; |z| ≥ 3 in 1,707 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +5.5 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +3.5 |
| fall | [[NG25 (drug)]] 5 µM |  | -7.0 | -5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.7 | -10.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.5 | -10.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.2 | -7.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -5.9 | -6.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -5.8 | -6.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -5.7 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | LIF interleukin 6 family cytokine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,240,453-30,246,759 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDF, DIA, HILDA |
| Gene groups (HGNC) | Receptor ligands; Interleukin 6 type cytokine family |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 6 pathways, smallest: IL-6-type cytokine receptor ligand interactions; Interleukin-6 family signaling; Interleukin-10 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P15018](https://www.uniprot.org/uniprotkb/P15018) (Leukemia inhibitory factor):

> Functions as a cytokine that binds to the LIF receptor complex. The LIF receptor complex indeed consists of two signaling receptor subunits IL6ST/gp130 and LIFR that transduce the signal into the cell. Functionally, regulates cell self-renewal, differentiation and survival of embryonic stem cells (ESCs) and is crucial for embryonic implantation (By similarity). Mechanistically, ligand binding to LIFR, induces heterodimerization with IL6ST/gp130 activating JAK tyrosine kinases (JAK1 or JAK2 and …

**Summary**, from NCBI Gene [3976](https://www.ncbi.nlm.nih.gov/gene/3976):

> The protein encoded by this gene is a pleiotropic cytokine with roles in several different systems. It is involved in the induction of hematopoietic differentiation in normal and myeloid leukemia cells, induction of neuronal cell differentiation, regulator of mesenchymal to epithelial conversion during kidney development, and may also have a role in immune tolerance at the maternal-fetal interface. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this …

**Accessions** — [HGNC:6596](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6596) · Entrez [3976](https://www.ncbi.nlm.nih.gov/gene/3976) · UniProt [P15018](https://www.uniprot.org/uniprotkb/P15018) · Ensembl [ENSG00000128342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128342)

## Data

Gene col 4879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4879); `tables/drug_effects.parquet` (85 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4879]; `tensor/DDL_lfc|DDL_z.npy` [4879]; `embed/gene_vectors.npy` [4879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4879 or target_col == 4879). Every well: [[LIF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
