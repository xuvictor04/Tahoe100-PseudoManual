---
symbol: "MCPH1"
type: "gene"
col: 7171
ensembl_id: "ENSG00000147316"
name: "microcephalin 1"
location: "8p23.1"
module: 88
arm: "+"
pooled_cpm: 88.15
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# MCPH1

*microcephalin 1* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +13.8, q 2e-40, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.374× (z -19.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2-AS1]] (+0.78, fdr 1e-05), [[LINC00571]] (+0.77, fdr 1e-05), [[MZF1-AS1]] (+0.77, fdr 1e-05); moves opposite to [[RIMS3]] (-0.72, fdr 1e-05), [[GPR160]] (-0.69, fdr 1e-05), [[CEP131]] (-0.69, fdr 1e-04).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RTN4R]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +13.8 | 2e-40 | 37/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +10.8 | 1e-24 | 36/48 (SW480, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +10.1 | 7e-22 | 41/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +8.1 | 8e-14 | 39/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +7.4 | 1e-11 | 37/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +7.2 | 5e-11 | 37/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.3 | 8e-06 | 30/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.62×** | +5.0 | 3e-05 | 38/49 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +4.9 | 6e-05 | 32/48 (AsPC-1, BT-474, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.5 | 4e-04 | 18/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.007 | 23/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.030 | 18/47 (SW480, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.047 | 21/48 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.047 | 13/49 (SW480, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.067 | 16/47 (SW480, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7171.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.374×** | -19.8 | 0e+00 | 48/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.396×** | -18.6 | 0e+00 | 47/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.410×** | -17.9 | 0e+00 | 48/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.614×** | -9.8 | 1e-20 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -9.3 | 1e-18 | 32/44 (NCI-H23, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.636×** | -9.1 | 7e-18 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.649×** | -8.6 | 5e-16 | 37/49 (KATO III, A-172, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.749×** | -8.2 | 1e-14 | 39/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.501×** | -7.3 | 2e-11 | 46/49 (A549, COLO 205, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.547×** | -6.4 | 1e-08 | 36/48 (A-172, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.780×** | -5.0 | 3e-05 | 31/49 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **0.802×** | -4.5 | 4e-04 | 24/48 (KATO III, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.674×** | -4.2 | 0.001 | 26/47 (A549, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.882× | -3.6 | 0.012 | 9/48 (KATO III, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 126 | 14 (7 ⚠) | 5 | [[Auranofin (drug)]] 5 µM 3.68× (z +18.6) | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -17.0) |
| [[KATO III (line)]] | alt | 173 | 2 | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.321× (z -16.0) |
| [[LoVo (line)]] | wt | 106 | 4 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.252× (z -17.6) |
| [[COLO 205 (line)]] | alt | 110 | 4 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +16.9) | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -16.7) |
| [[A498 (line)]] | wt | 86.9 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -14.0) |
| [[A549 (line)]] | wt | 107 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.309× (z -15.8) |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0936× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.196× (z -15.0) |
| [[NCI-H1573 (line)]] | alt | 69.9 | 4 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +26.8) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.448× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 65.5 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +17.7) | [[Belinostat (drug)]] 5 µM 0.404× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 78.9 | 4 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.83× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +9.8) | [[Belinostat (drug)]] 5 µM 0.404× (z -11.8) |
| [[A-172 (line)]] | wt | 101 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.59× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.349× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 132 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.32× (z +9.8) | [[Belinostat (drug)]] 5 µM 0.386× (z -11.5) |
| [[A-427 (line)]] | wt | 67.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.35× (z +19.1) | [[Dinaciclib (drug)]] 0.5 µM 0.461× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 129 | 2 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.34× (z +10.7) | [[Belinostat (drug)]] 5 µM 0.437× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 84.0 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 55.2 | 1 (1 ⚠) | 4 | [[Niclosamide (olamine) (drug)]] 5 µM 2.41× (z +9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.333× (z -12.4) |
| [[Hs 766T (line)]] | wt | 122 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 112 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.3) | [[Belinostat (drug)]] 5 µM 0.335× (z -12.4) |
| [[LS 180 (line)]] | wt | 98.3 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 112 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.418× (z -11.0) |
| [[PANC-1 (line)]] | alt | 34.9 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.479× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 77.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +19.0) | — |
| [[HCT15 (line)]] | alt | 139 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.249× (z -13.9) |
| [[HT-29 (line)]] | alt | 46.7 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.60× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 56.9 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.8) | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -10.5) |
| [[SNU-423 (line)]] | alt | 50.0 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -10.0) |
| [[SW48 (line)]] | wt | 94.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +16.1) | — |
| [[C-33 A (line)]] | alt | 116 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -10.4) |
| [[H4 (line)]] | wt | 120 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.205× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 64.8 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +17.2) | [[Belinostat (drug)]] 5 µM 0.418× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 57.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -11.7) |
| [[RKO (line)]] | wt | 146 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.380× (z -10.4) |
| [[SHP-77 (line)]] | alt | 147 | 2 | 1 | [[Auranofin (drug)]] 5 µM 2.20× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.471× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 72.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.318× (z -10.9) |
| [[SW 900 (line)]] | alt | 83.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.350× (z -10.9) |
| [[AN3 CA (line)]] | alt | 79.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0795× (z -14.7) |
| [[CHP-212 (line)]] | wt | 144 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.262× (z -9.6) |
| [[SW 1088 (line)]] | alt | 104 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0866× (z -9.4) |
| [[BT-474 (line)]] | alt | 86.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.387× (z -8.7) |
| [[SNU-1 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -15.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.330× (z -9.5) |
| [[C32 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 116 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | +0.78 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[LINC00571]] | +0.77 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[MZF1-AS1]] | +0.77 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[NEK11]] | +0.76 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[GTF2H1]] | +0.76 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CLHC1]] | +0.76 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[DPH5-DT]] | +0.74 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.74 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[ST7L]] | +0.73 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[AEBP2]] | +0.73 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[RFX3-DT]] | +0.72 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | +0.72 | +0.62 / +0.32 | both halves | 1e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS3]] | -0.72 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[GPR160]] | -0.69 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[CEP131]] | -0.69 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[FAM118A]] | -0.68 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[SEMA4F]] | -0.68 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[PPP1R2]] | -0.68 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[INPP5F]] | -0.68 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SLC9A6]] | -0.67 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[ARRB2]] | -0.67 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[DNAAF3]] | -0.66 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[CARHSP1]] | -0.66 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[CDON]] | -0.66 | -0.55 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RTN4R]] | C | RTN4R activity lowers MCPH1's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 1.47× higher at baseline in the lines without RTN4R | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (4.2, 8.0); signed map (18.1, -26.0). **Vector** length 134, 42.0% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.2 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +11.9 | +10.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.9 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +13.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.1 | +3.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -10.0 | -18.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -9.2 | -19.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.2 | -17.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.7 | -9.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -8.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -6.3 | -7.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.4 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.9 | -2.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | microcephalin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:6,406,592-6,648,508 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12847, BRIT1 |
| Reactome | 5 pathways, smallest: Condensation of Prophase Chromosomes; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEM0](https://www.uniprot.org/uniprotkb/Q8NEM0) (Microcephalin):

> Implicated in chromosome condensation and DNA damage induced cellular responses. May play a role in neurogenesis and regulation of the size of the cerebral cortex.

**Summary**, from NCBI Gene [79648](https://www.ncbi.nlm.nih.gov/gene/79648):

> This gene encodes a DNA damage response protein. The encoded protein may play a role in G2/M checkpoint arrest via maintenance of inhibitory phosphorylation of cyclin-dependent kinase 1. Mutations in this gene have been associated with primary autosomal recessive microcephaly 1 and premature chromosome condensation syndrome. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:6954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6954) · Entrez [79648](https://www.ncbi.nlm.nih.gov/gene/79648) · UniProt [Q8NEM0](https://www.uniprot.org/uniprotkb/Q8NEM0) · Ensembl [ENSG00000147316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147316)

## Data

Gene col 7171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7171); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7171]; `tensor/DDL_lfc|DDL_z.npy` [7171]; `embed/gene_vectors.npy` [7171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7171 or target_col == 7171). Every well: [[MCPH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCPH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
