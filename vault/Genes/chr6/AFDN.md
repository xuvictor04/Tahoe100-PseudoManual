---
symbol: "AFDN"
type: "gene"
col: 5061
ensembl_id: "ENSG00000130396"
name: "afadin, adherens junction formation factor"
location: "6q27"
module: 83
arm: "-"
pooled_cpm: 292.21
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# AFDN

*afadin, adherens junction formation factor* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.25× (z +6.3, q 2e-07, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.559× (z -16.2, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP5F]] (+0.63, fdr 5e-05), [[TNK2]] (+0.59, fdr 5e-05), [[PICALM]] (+0.59, fdr 1e-05); moves opposite to [[AKAP8]] (-0.61, fdr 1e-04), [[SPART-AS1]] (-0.61, fdr 4e-05), [[LRRC41]] (-0.59, fdr 3e-04).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.3 | 2e-07 | 26/47 (Hs 766T, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.2 | 2e-07 | 26/47 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.3 | 2e-05 | 30/48 (Hs 766T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +4.7 | 3e-04 | 28/47 (BT-474, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.3 | 0.002 | 25/46 (COLO 205, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.23×** | +4.1 | 0.004 | 26/47 (NCI-H1573, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.7 | 0.017 | 24/47 (BT-474, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.5 | 0.028 | 23/47 (BT-474, KATO III, …) | rises with dose |  |
| [[Tadalafil (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.048 | 23/47 (LS 180, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.20×** | +3.3 | 0.048 | 21/47 (A498, PANC-1, …) | top dose only | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.3 | 0.048 | 18/48 (CHP-212, NCI-H1573, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.048 | 23/47 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.20× | +3.3 | 0.048 | 22/46 (H4, hTERT-HPNE, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 5 µM |  | 1.12× | +3.2 | 0.048 | 3/47 (CFPAC-1, SW 1271, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.059 | 15/47 (HEC-1-A, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.559×** | -16.2 | 0e+00 | 45/48 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.495×** | -12.7 | 2e-34 | 43/46 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.579×** | -10.8 | 7e-25 | 37/48 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.553×** | -10.7 | 2e-24 | 34/43 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.644×** | -8.0 | 1e-13 | 32/44 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.666×** | -8.0 | 1e-13 | 40/47 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.758×** | -7.7 | 8e-13 | 31/47 (C32, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -7.0 | 2e-10 | 36/47 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -6.4 | 1e-08 | 30/47 (A-172, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.730×** | -5.7 | 8e-07 | 32/49 (A-172, C32, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.774×** | -5.0 | 2e-05 | 33/47 (SW 900, C32, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.849× | -4.6 | 2e-04 | 16/47 (A-172, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -3.3 | 0.045 | 21/47 (SW 1271, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Arbutin (drug)]] 5 µM |  | 0.841× | -3.1 | 0.072 | 18/47 (A-427, NCI-H2030, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.855× | -3.1 | 0.072 | 20/47 (Panc 03.27, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 300 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -19.8) |
| [[HOP62 (line)]] | alt | 302 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -18.3) |
| [[C32 (line)]] | wt | 394 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.313× (z -20.0) |
| [[PANC-1 (line)]] | alt | 454 | 4 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +18.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 367 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -22.0) |
| [[SW 900 (line)]] | alt | 388 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -15.3) |
| [[BT-474 (line)]] | alt | 175 | 5 (3 ⚠) | 1 | [[Digitoxin (drug)]] 0.5 µM 2.34× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 910 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 652 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -20.9) |
| [[SW480 (line)]] | alt | 282 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -15.3) |
| [[LoVo (line)]] | wt | 396 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -13.9) |
| [[RKO (line)]] | wt | 190 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.6) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.593× (z -9.4) |
| [[A498 (line)]] | wt | 159 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +25.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 227 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.6) ⚠ cell-cycle shift, explains ~37% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -19.4) |
| [[HEC-1-A (line)]] | alt | 460 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -14.8) |
| [[KATO III (line)]] | alt | 386 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 191 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.24× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.439× (z -10.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 187 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 366 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.2) ⚠ cell-cycle shift, explains ~37% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -19.2) |
| [[HCT15 (line)]] | alt | 258 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.488× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 447 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -14.1) |
| [[SW 1271 (line)]] | alt | 282 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.223× (z -10.5) |
| [[SW1417 (line)]] | alt | 541 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -17.8) |
| [[A-427 (line)]] | wt | 213 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.426× (z -13.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 378 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 330 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 210 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.484× (z -12.2) |
| [[LS 180 (line)]] | wt | 395 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.505× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 164 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 328 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.8) |
| [[SNU-423 (line)]] | alt | 449 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -17.1) |
| [[C-33 A (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -10.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.78× (z +9.7) ⚠ toxic | — |
| [[Hs 766T (line)]] | wt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -8.8) |
| [[J82 (line)]] | alt | 151 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -9.6) |
| [[SHP-77 (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 207 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -10.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 238 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 92.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 141 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 343 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 236 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5F]] | +0.63 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[TNK2]] | +0.59 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[PICALM]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SPAG9]] | +0.57 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[NCAM1]] | +0.56 | +0.30 / +0.42 | both halves | 2e-04 |  |
| [[DOP1B]] | +0.55 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[FLNB]] | +0.55 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[TMOD2]] | +0.54 | +0.44 / +0.35 | both halves | 1e-04 |  |
| [[ATP1A3]] | +0.53 | +0.22 / +0.37 | both halves | 6e-04 |  |
| [[RMC1]] | +0.53 | +0.37 / +0.38 | both halves | 9e-05 |  |
| [[MYO6]] | +0.53 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[SPATA13]] | +0.52 | +0.46 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP8]] | -0.61 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[SPART-AS1]] | -0.61 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[LRRC41]] | -0.59 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[ACAD9]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[YARS2]] | -0.57 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[ECHDC1]] | -0.55 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[PDHX]] | -0.55 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[ZNF785]] | -0.55 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[KIAA0753]] | -0.54 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[MCPH1]] | -0.53 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[UQCC1]] | -0.53 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[TIRAP]] | -0.53 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AFDN's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ESPN]] | B | ESPN activity raises AFDN's level | lines that do not express ESPN (26) vs lines expressing it (24) | 1.57× lower at baseline in the lines without ESPN | 0.057 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[CACNG4]] | B | CACNG4 activity raises AFDN's level | lines that do not express CACNG4 (21) vs lines expressing it (29) | 1.24× lower at baseline in the lines without CACNG4 | 0.061 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, PCSK1N |
| [[TSPAN15]] | B | TSPAN15 activity raises AFDN's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.58× lower at baseline in the lines without TSPAN15 | 0.063 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[SVIP]] | B | SVIP activity raises AFDN's level | lines that do not express SVIP (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without SVIP | 0.067 | ⚠ within organs, on part of the lines; also absent: PLEKHA5, LRRCC1, USP53; maybe low, not absent; its own permutation p |
| [[KLF2]] | C | KLF2 activity lowers AFDN's level | lines that do not express KLF2 (3) vs lines expressing it (47) | 2.46× higher at baseline in the lines without KLF2 | 0.070 | ⚠ few lines (3 vs 47); across organs; also absent: LEKR1, CBR3, DPP7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-17.0, 30.5); signed map (-14.0, 31.0). **Vector** length 110, 37.1% of its response variance represented; |z| ≥ 3 in 1,410 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.1 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.6 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.9 | -7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.4 | -12.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -16.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.1 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | afadin, adherens junction formation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:167,826,893-167,972,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AF-6, AF6; previously MLLT4 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P55196](https://www.uniprot.org/uniprotkb/P55196) (Afadin):

> Belongs to an adhesion system, probably together with the E-cadherin-catenin system, which plays a role in the organization of homotypic, interneuronal and heterotypic cell-cell adherens junctions (AJs) (By similarity). Nectin- and actin-filament-binding protein that connects nectin to the actin cytoskeleton. May play a key role in the organization of epithelial structures of the embryonic ectoderm (By similarity). Essential for the organization of adherens junctions.

**Summary**, from NCBI Gene [4301](https://www.ncbi.nlm.nih.gov/gene/4301):

> This gene encodes a multi-domain protein involved in signaling and organization of cell junctions during embryogenesis. It has also been identified as the fusion partner of acute lymphoblastic leukemia (ALL-1) gene, involved in acute myeloid leukemias with t(6;11)(q27;q23) translocation. Alternatively spliced transcript variants encoding different isoforms have been described for this gene, however, not all have been fully characterized.[provided by RefSeq, May 2011]

**Accessions** — [HGNC:7137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7137) · Entrez [4301](https://www.ncbi.nlm.nih.gov/gene/4301) · UniProt [P55196](https://www.uniprot.org/uniprotkb/P55196) · Ensembl [ENSG00000130396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130396)

## Data

Gene col 5061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5061); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5061]; `tensor/DDL_lfc|DDL_z.npy` [5061]; `embed/gene_vectors.npy` [5061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5061 or target_col == 5061). Every well: [[AFDN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFDN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
