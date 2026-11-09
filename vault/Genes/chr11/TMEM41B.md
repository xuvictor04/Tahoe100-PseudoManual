---
symbol: "TMEM41B"
type: "gene"
col: 9314
ensembl_id: "ENSG00000166471"
name: "transmembrane protein 41B"
location: "11p15.4"
module: 42
arm: "+"
pooled_cpm: 238.78
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 20
n_dd_up_clean: 13
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TMEM41B

*transmembrane protein 41B* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.38× (z +14.4, q 2e-44, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.548× (z -14.1, q 2e-42, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM17]] (+0.72, fdr 7e-06), [[HSPA5]] (+0.67, fdr 7e-06), [[GP6-AS1]] (+0.67, fdr 1e-05); moves opposite to [[RNF146]] (-0.66, fdr 1e-05), [[ZNF747]] (-0.65, fdr 1e-05), [[LATS1]] (-0.64, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.38×** | +14.4 | 2e-44 | 46/48 (LoVo, A-172, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +8.1 | 1e-13 | 43/47 (J82, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +8.1 | 1e-13 | 39/48 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +7.7 | 2e-12 | 41/48 (LoVo, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.58×** | +7.7 | 2e-12 | 37/48 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +7.2 | 7e-11 | 37/48 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +6.3 | 3e-08 | 36/48 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.31×** | +6.3 | 3e-08 | 35/49 (A549, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 9e-06 | 38/48 (C-33 A, LoVo, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +5.3 | 9e-06 | 24/48 (A549, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 2e-05 | 38/49 (C-33 A, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.7 | 1e-04 | 25/48 (C-33 A, AN3 CA, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.1 | 0.002 | 29/45 (C-33 A, J82, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.005 | 27/49 (H4, C32, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.014 | 23/48 (SW480, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.548×** | -14.1 | 2e-42 | 41/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -11.1 | 3e-26 | 42/49 (RKO, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -10.4 | 4e-23 | 40/48 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.536×** | -10.3 | 6e-23 | 45/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.553×** | -9.5 | 4e-19 | 43/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.641×** | -7.4 | 2e-11 | 40/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -5.6 | 1e-06 | 37/48 (H4, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.719×** | -5.5 | 3e-06 | 38/48 (NCI-H1792, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -5.1 | 2e-05 | 33/50 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.805×** | -5.1 | 2e-05 | 28/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.757×** | -4.4 | 5e-04 | 31/48 (LS 180, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -4.1 | 0.002 | 26/48 (SW1417, HT-29, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.817×** | -4.0 | 0.003 | 26/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **0.804×** | -3.6 | 0.012 | 24/48 (SW 1088, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.790×** | -3.6 | 0.012 | 25/47 (H4, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.842× | -3.5 | 0.017 | 20/48 (NCI-H23, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.818×** | -3.3 | 0.026 | 25/48 (A-427, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 155 | 6 (1 ⚠) | 4 | [[Auranofin (drug)]] 5 µM 3.73× (z +17.8) | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -12.0) |
| [[J82 (line)]] | alt | 273 | 5 (1 ⚠) | 5 | [[Niclosamide (olamine) (drug)]] 5 µM 2.40× (z +11.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 2.15× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -15.9) |
| [[C-33 A (line)]] | alt | 274 | 8 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 3.70× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -12.5) |
| [[LoVo (line)]] | wt | 217 | 5 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 5.65× (z +18.7) | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -12.9) |
| [[PANC-1 (line)]] | alt | 492 | 1 | 6 | [[Auranofin (drug)]] 5 µM 2.38× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -19.5) |
| [[A-427 (line)]] | wt | 917 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.83× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -13.1) |
| [[A549 (line)]] | wt | 167 | 5 | 1 | [[Cepharanthine (drug)]] 5 µM 1.87× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.9) |
| [[H4 (line)]] | wt | 236 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -12.9) |
| [[HT-29 (line)]] | alt | 290 | 1 | 5 | [[Auranofin (drug)]] 5 µM 3.97× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 173 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 2.69× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -18.9) |
| [[NCI-H23 (line)]] | alt | 271 | 0 | 6 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.664× (z -16.3) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -12.9) |
| [[C32 (line)]] | wt | 92.8 | 4 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 5.02× (z +15.1) | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.7) |
| [[HS-578T (line)]] | alt | 216 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -19.4) |
| [[hTERT-HPNE (line)]] | wt | 130 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -13.7) |
| [[LS 180 (line)]] | wt | 280 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.79× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 199 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.40× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -15.3) |
| [[SNU-1 (line)]] | wt | 334 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.43× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 209 | 1 | 4 | [[Auranofin (drug)]] 5 µM 2.19× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.344× (z -12.5) |
| [[SW480 (line)]] | alt | 282 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.52× (z +11.3) | — |
| [[RKO (line)]] | wt | 351 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.04× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 158 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.7) |
| [[AN3 CA (line)]] | alt | 283 | 2 | 1 | [[Auranofin (drug)]] 5 µM 5.66× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.5) |
| [[HCT15 (line)]] | alt | 320 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.02× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -13.4) |
| [[HepG2_C3A (line)]] | wt | 182 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.57× (z +9.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.399× (z -9.4) |
| [[KATO III (line)]] | alt | 183 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.355× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 483 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.81× (z +13.0) | [[Adagrasib (drug)]] 0.05 µM 0.616× (z -16.8) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 149 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.59× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 133 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.45× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 150 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.14× (z +11.8) | — |
| [[SK-MEL-2 (line)]] | alt | 107 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.52× (z +11.0) | — |
| [[A498 (line)]] | wt | 156 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.51× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.449× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 140 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.39× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -8.5) |
| [[Hs 766T (line)]] | wt | 182 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.17× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 105 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.351× (z -9.2) |
| [[SW48 (line)]] | wt | 243 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 280 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.40× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 149 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.29× (z +11.0) | — |
| [[HOP62 (line)]] | alt | 194 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 99.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.61× (z +10.2) | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0572× (z -12.1) ⚠ transcription drop; cell-cycle shift, explains ~13% of this change |
| [[SW1417 (line)]] | alt | 343 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.08× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 300 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 199 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM17]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[HSPA5]] | +0.67 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[GP6-AS1]] | +0.67 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CSNK2A1]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MVD]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.65 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[UBE2Q2P2-1]] | +0.64 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TPST2]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[UQCRH]] | +0.64 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[PWWP3A]] | +0.63 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[UBE2Q2P2]] | +0.63 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.62 | +0.55 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF146]] | -0.66 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[ZNF747]] | -0.65 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[LATS1]] | -0.64 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[TRMT5]] | -0.64 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.64 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[NFYB]] | -0.63 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | -0.63 | -0.69 / -0.33 | both halves | 1e-04 |  |
| [[ZNF462]] | -0.63 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ZBTB33]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[DECR1]] | -0.63 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[DDX20]] | -0.62 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[ZNF532]] | -0.62 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TMEM41B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.3, 6.9); signed map (-42.8, 8.4). **Vector** length 162, 60.3% of its response variance represented; |z| ≥ 3 in 1,653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.3 | +14.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +10.7 | +7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +10.1 | +8.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +9.6 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +4.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +5.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.9 | +5.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -16.1 | -10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -12.3 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.9 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -11.8 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.7 | -14.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -7.0 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -5.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.0 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 41B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:9,280,654-9,314,636 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0033 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5BJD5](https://www.uniprot.org/uniprotkb/Q5BJD5) (Transmembrane protein 41B):

> Phospholipid scramblase involved in lipid homeostasis and membrane dynamics processes. Has phospholipid scramblase activity toward cholesterol and phosphatidylserine, as well as phosphatidylethanolamine and phosphatidylcholine. Required for autophagosome formation: participates in early stages of autophagosome biogenesis at the endoplasmic reticulum (ER) membrane by reequilibrating the leaflets of the ER as lipids are extracted by ATG2 (ATG2A or ATG2B) to mediate autophagosome assembly. In …

**Summary**, from NCBI Gene [440026](https://www.ncbi.nlm.nih.gov/gene/440026):

> Enables phospholipid scramblase activity. Involved in autophagosome assembly and intracellular lipid transport. Located in mitochondria-associated endoplasmic reticulum membrane contact site. Is active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28948) · Entrez [440026](https://www.ncbi.nlm.nih.gov/gene/440026) · UniProt [Q5BJD5](https://www.uniprot.org/uniprotkb/Q5BJD5) · Ensembl [ENSG00000166471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166471)

## Data

Gene col 9314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9314); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9314]; `tensor/DDL_lfc|DDL_z.npy` [9314]; `embed/gene_vectors.npy` [9314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9314 or target_col == 9314). Every well: [[TMEM41B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM41B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
