---
symbol: "MEIS2"
type: "gene"
col: 5515
ensembl_id: "ENSG00000134138"
name: "Meis homeobox 2"
location: "15q14"
module: 2
arm: "-"
pooled_cpm: 157.11
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 39
n_dd_up_clean: 5
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MEIS2

*Meis homeobox 2* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +8.2, q 1e-13, up in 27 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.286× (z -24.7, q 0e+00, down in 44 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF827]] (+0.69, fdr 7e-06), [[PCDH7]] (+0.65, fdr 7e-06), [[TET2]] (+0.62, fdr 1e-05); moves opposite to [[KCTD21]] (-0.62, fdr 1e-05), [[HDAC11]] (-0.59, fdr 2e-05), [[ABTB1]] (-0.59, fdr 2e-05).
> It sits in the **-** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[HOXB4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.2 | 1e-13 | 27/45 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +6.1 | 3e-07 | 29/44 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.1 | 5e-05 | 24/44 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 0.001 | 24/44 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.20×** | +3.7 | 0.025 | 21/44 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.027 | 19/45 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.048 | 11/44 (A498, KATO III, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.085 | 12/44 (J82, NCI-H2347, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.13 | 17/44 (AsPC-1, HOP62, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.0 | 0.13 | 19/46 (SW480, RKO, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.13 | 12/44 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.286×** | -24.7 | 0e+00 | 44/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.355×** | -20.4 | 0e+00 | 43/44 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.378×** | -19.2 | 0e+00 | 44/44 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -14.7 | 0e+00 | 33/41 (LOX-IMVI, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.484×** | -14.3 | 2e-44 | 37/45 (CHP-212, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.485×** | -14.3 | 3e-44 | 40/44 (KATO III, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.517×** | -12.0 | 2e-31 | 32/42 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -11.8 | 5e-30 | 37/44 (COLO 205, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.584×** | -10.2 | 1e-22 | 32/44 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.716×** | -9.3 | 8e-19 | 28/44 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.645×** | -8.7 | 3e-16 | 38/44 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -8.5 | 7e-16 | 33/44 (CHP-212, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -8.5 | 9e-16 | 37/44 (COLO 205, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.679×** | -7.6 | 1e-12 | 35/44 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.764×** | -7.5 | 3e-12 | 38/45 (COLO 205, CHP-212, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.673×** | -7.4 | 7e-12 | 37/44 (COLO 205, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.509×** | -7.0 | 1e-10 | 32/45 (C32, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.705×** | -6.9 | 2e-10 | 35/44 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.725×** | -6.3 | 7e-09 | 35/44 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.737×** | -6.0 | 5e-08 | 28/44 (C32, RKO, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.733×** | -5.9 | 1e-07 | 35/44 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.777×** | -4.8 | 4e-05 | 31/44 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 572 | 0 | 19 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -22.5) |
| [[NCI-H460 (line)]] | wt | 154 | 0 | 16 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -16.0) |
| [[C32 (line)]] | wt | 414 | 0 | 12 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -21.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.275× (z -17.1) |
| [[CHP-212 (line)]] | wt | 1,875 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -22.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -21.1) |
| [[KATO III (line)]] | alt | 262 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -23.6) |
| [[LOX-IMVI (line)]] | wt | 286 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.273× (z -16.9) |
| [[NCI-H1792 (line)]] | alt | 277 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -20.7) |
| [[CFPAC-1 (line)]] | alt | 244 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -12.4) |
| [[HT-29 (line)]] | alt | 249 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 163 | 1 | 8 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -10.5) |
| [[A-172 (line)]] | wt | 426 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -16.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.216× (z -13.9) |
| [[HOP62 (line)]] | alt | 144 | 1 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.264× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 118 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 231 | 1 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -14.1) |
| [[SNU-1 (line)]] | wt | 278 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -14.1) |
| [[SW480 (line)]] | alt | 87.1 | 1 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +13.7) | [[Panobinostat (drug)]] 5 µM 0.175× (z -28.0) |
| [[AsPC-1 (line)]] | alt | 82.6 | 4 | 3 | [[Binimetinib (drug)]] 0.05 µM 2.03× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -12.1) |
| [[H4 (line)]] | wt | 188 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.243× (z -13.6) |
| [[LoVo (line)]] | wt | 134 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +15.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.367× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 217 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -15.6) |
| [[AN3 CA (line)]] | alt | 372 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -14.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.271× (z -10.7) |
| [[HCT15 (line)]] | alt | 147 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.286× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 77.2 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -14.0) |
| [[Hs 766T (line)]] | wt | 236 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -14.5) |
| [[PANC-1 (line)]] | alt | 123 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.518× (z -10.0) |
| [[RKO (line)]] | wt | 131 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +11.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.239× (z -14.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -11.4) |
| [[SNU-423 (line)]] | alt | 66.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -11.6) |
| [[SW 900 (line)]] | alt | 154 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -16.3) |
| [[A498 (line)]] | wt | 134 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -13.1) |
| [[HepG2_C3A (line)]] | wt | 211 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.316× (z -13.7) |
| [[NCI-H661 (line)]] | alt | 710 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -14.0) |
| [[A549 (line)]] | wt | 93.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -11.5) |
| [[HS-578T (line)]] | alt | 82.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -13.3) |
| [[A-427 (line)]] | wt | 64.8 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.6) ⚠ cell-cycle shift, explains ~41% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.454× (z -8.7) |
| [[J82 (line)]] | alt | 128 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.382× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 92.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.416× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 59.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 116 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.358× (z -11.1) |
| [[SW1417 (line)]] | alt | 73.8 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.338× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 115 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.276× (z -10.3) |
| [[BT-474 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 31.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF827]] | +0.69 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PCDH7]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[TET2]] | +0.62 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LHFPL6]] | +0.57 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[PARP8]] | +0.57 | +0.40 / +0.57 | both halves | 4e-05 |  |
| [[TENT5A]] | +0.56 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[SNHG31]] | +0.55 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[INTS6L]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[GPHN]] | +0.54 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[HFE]] | +0.53 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[BRWD3]] | +0.52 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[MICOS10]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD21]] | -0.62 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[HDAC11]] | -0.59 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ABTB1]] | -0.59 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.59 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[DTD1]] | -0.57 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[CDC16]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 | same gene group |
| [[SNX15]] | -0.56 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ADAMTSL5]] | -0.56 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[SIN3B]] | -0.54 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[PRKCZ]] | -0.53 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[LYSMD4]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[ATP13A2]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXB4]] | C | MEIS2 activity raises HOXB4's level | lines that do not express MEIS2 (4) vs lines expressing it (46) | 1.28× lower at baseline in the lines without MEIS2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | MEIS2's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | MEIS2's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.405 over the table, 0.059 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **-** arm (projection on the module's main direction -0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (13.5, 4.0); signed map (44.8, -0.2). **Vector** length 115, 39.2% of its response variance represented; |z| ≥ 3 in 1,631 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.2 | +8.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +6.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.0 | +0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.6 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +2.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.6 | -20.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.4 | -24.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.5 | -7.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.7 | -6.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -19.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.2 | -6.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | Meis homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:36,889,204-37,101,299 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRG1, HsT18361 |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes; MicroRNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [O14770](https://www.uniprot.org/uniprotkb/O14770) (Homeobox protein Meis2):

> Involved in transcriptional regulation. Binds to HOX or PBX proteins to form dimers, or to a DNA-bound dimer of PBX and HOX proteins and thought to have a role in stabilization of the homeoprotein-DNA complex. Isoform 3 is required for the activity of a PDX1:PBX1b:MEIS2b complex in pancreatic acinar cells involved in the transcriptional activation of the ELA1 enhancer; the complex binds to the enhancer B element and cooperates with the transcription factor 1 complex (PTF1) bound to the enhancer …

**Summary**, from NCBI Gene [4212](https://www.ncbi.nlm.nih.gov/gene/4212):

> This gene encodes a homeobox protein belonging to the TALE ('three amino acid loop extension') family of homeodomain-containing proteins. TALE homeobox proteins are highly conserved transcription regulators, and several members have been shown to be essential contributors to developmental programs. Multiple transcript variants encoding distinct isoforms have been described for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7001) · Entrez [4212](https://www.ncbi.nlm.nih.gov/gene/4212) · UniProt [O14770](https://www.uniprot.org/uniprotkb/O14770) · Ensembl [ENSG00000134138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134138)

## Data

Gene col 5515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5515); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5515]; `tensor/DDL_lfc|DDL_z.npy` [5515]; `embed/gene_vectors.npy` [5515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5515 or target_col == 5515). Every well: [[MEIS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEIS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
