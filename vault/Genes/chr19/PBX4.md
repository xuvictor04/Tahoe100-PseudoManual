---
symbol: "PBX4"
type: "gene"
col: 2653
ensembl_id: "ENSG00000105717"
name: "PBX homeobox 4"
location: "19p13.11"
module: 77
arm: "+"
pooled_cpm: 31.63
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 24
n_dd_up_clean: 11
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# PBX4

*PBX homeobox 4* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.54× (z +25.5, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.588× (z -10.7, q 5e-24, down in 27 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.707× (z -9.9, q 2e-20, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A1]] (+0.69, fdr 3e-05), [[CLTCL1]] (+0.69, fdr 1e-05), [[MYO9B]] (+0.69, fdr 3e-05); moves opposite to [[MCTS1]] (-0.69, fdr 1e-05), [[UFL1-AS1]] (-0.68, fdr 1e-04), [[TMEM202-AS1]] (-0.68, fdr 1e-04).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[PTPN3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2653.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.54×** | +25.5 | 0e+00 | 44/45 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.74×** | +20.3 | 0e+00 | 42/45 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.72×** | +20.2 | 0e+00 | 43/45 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +8.1 | 1e-13 | 27/44 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +7.9 | 2e-13 | 27/45 (CFPAC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +6.4 | 1e-08 | 26/45 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 9e-07 | 19/44 (SW1417, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +5.3 | 7e-06 | 17/45 (PANC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.2 | 1e-05 | 16/38 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 1e-04 | 15/45 (MIA PaCa-2, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.64×** | +4.8 | 1e-04 | 17/45 (NCI-H2347, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 3e-04 | 20/45 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.062 | 8/44 (PANC-1, A-427, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.091 | 5/45 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2653.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.588×** | -10.7 | 5e-24 | 27/40 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -9.9 | 2e-20 | 28/45 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.626×** | -7.3 | 4e-11 | 19/36 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.695×** | -7.3 | 4e-11 | 22/43 (SW480, HOP62, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -7.2 | 6e-11 | 23/45 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.701×** | -7.1 | 9e-11 | 24/44 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -7.1 | 1e-10 | 26/45 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -6.7 | 1e-09 | 24/45 (A-172, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.797×** | -6.5 | 6e-09 | 20/44 (A-427, A-172, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.512×** | -6.4 | 6e-09 | 25/45 (A-172, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.3 | 2e-08 | 23/44 (A-427, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.736×** | -5.9 | 1e-07 | 23/45 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.815×** | -5.8 | 3e-07 | 23/45 (NCI-H2347, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.766×** | -5.1 | 1e-05 | 19/44 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.781×** | -5.0 | 2e-05 | 14/45 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.621×** | -4.6 | 1e-04 | 14/45 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.795×** | -4.4 | 3e-04 | 18/44 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -4.4 | 3e-04 | 19/45 (SNU-1, A-427, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.859× | -4.3 | 4e-04 | 11/45 (RKO, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2653. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 76.7 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.338× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 58.6 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 15.8 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.21× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.112× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.157× (z -13.4) |
| [[SW480 (line)]] | alt | 53.5 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +10.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -10.0) |
| [[A-427 (line)]] | wt | 25.8 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -22.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 30.4 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.42× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0680× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -8.8) |
| [[HOP62 (line)]] | alt | 19.9 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 4.42× (z +11.6) | [[Harringtonine (drug)]] 5 µM 0.299× (z -9.1) |
| [[A498 (line)]] | wt | 112 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -18.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 70.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Alpelisib (drug)]] 5 µM 0.0768× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 24.8 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.42× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.1) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 36.8 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.490× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 23.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.09× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -8.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 54.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.34× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -8.9) |
| [[KATO III (line)]] | alt | 16.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.77× (z +10.8) | — |
| [[LoVo (line)]] | wt | 16.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.60× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.79× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 28.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -20.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -10.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 77.7 | 0 | 2 (1 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.346× (z -9.6) |
| [[C32 (line)]] | wt | 14.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.214× (z -8.5) |
| [[H4 (line)]] | wt | 19.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.44× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 11.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.91× (z +9.3) | — |
| [[J82 (line)]] | alt | 20.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.43× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 20.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.31× (z +10.7) | — |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.234× (z -9.9) |
| [[RKO (line)]] | wt | 11.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 11.6× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0715× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 25.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.93× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 30.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.05× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 66.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 7.98 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.0546× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -10.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 18.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0437× (z -14.4) |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2653), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | +0.69 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[CLTCL1]] | +0.69 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.69 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[SLC8B1]] | +0.68 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.67 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[GNA12]] | +0.67 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[FLNB]] | +0.67 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[MAST3]] | +0.66 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[FANCE]] | +0.66 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[CRLF3]] | +0.66 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.65 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[TPST2]] | +0.65 | +0.64 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCTS1]] | -0.69 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | -0.68 | -0.61 / -0.32 | both halves | 1e-04 |  |
| [[TMEM202-AS1]] | -0.68 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[TSGA10]] | -0.68 | -0.64 / -0.22 | both halves | 6e-04 |  |
| [[PATL2]] | -0.67 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[RIPK2-DT]] | -0.67 | -0.61 / -0.43 | both halves | 4e-05 |  |
| [[DECR1]] | -0.66 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[PLBD1-AS1]] | -0.65 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[ANXA2R-AS1]] | -0.65 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[PCNX4-DT]] | -0.65 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[ZNF747]] | -0.65 | -0.65 / -0.28 | both halves | 3e-04 |  |
| [[TAPBPL]] | -0.64 | -0.58 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PBX4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RBKS]] | B | RBKS activity raises PBX4's level | lines that do not express RBKS (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without RBKS | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GALNT12]] | B | GALNT12 activity raises PBX4's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without GALNT12 | 0.047 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[HDAC6]] | B | HDAC6 activity lowers PBX4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers PBX4's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PRR5]] | C | PRR5 activity raises PBX4's level | lines that do not express PRR5 (4) vs lines expressing it (46) | 3.00× lower at baseline in the lines without PRR5 | 0.029 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NECTIN1, PLEKHG3, SNED1 |
| [[PTPN3]] | C | PTPN3 activity raises PBX4's level | lines that do not express PTPN3 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without PTPN3 | 0.068 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4; co-absent with the target |
| [[RTN4R]] | C | RTN4R activity raises PBX4's level | lines that do not express RTN4R (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without RTN4R | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MMP15, RASSF7, ZDHHC11B; maybe low, not absent |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN3]] | C | PBX4 activity raises PTPN3's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 5.10× lower at baseline in the lines without PBX4 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561; co-absent with the target |
| [[UBR5]] | C | PBX4 activity weakens UBR5's drug response | lines that do not express PBX4 (3) vs lines expressing it (46) | the lines without PBX4 respond 0.99× as strongly (z diff -0.16); strongest at Dinaciclib 0.05 µM: 0.27x vs 0.64x (z diff -5.1) | 0.006 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561; target measured in part of the lines; both ways; artifact flags |
| [[HDAC11]] | C | PBX4 activity raises HDAC11's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without PBX4 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |
| [[PEF1]] | C | PBX4 activity raises PEF1's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 1.50× lower at baseline in the lines without PBX4 | 0.031 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |
| cells under [[Amsacrine (drug)]] 5 µM | C | PBX4 activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express PBX4 (3) vs lines expressing it (45) | the lines without PBX4: 0.73× the cells of the other lines | 0.032 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |
| [[GRK6]] | C | PBX4 activity raises GRK6's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without PBX4 | 0.040 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |
| [[CTNNBIP1]] | C | PBX4 activity raises CTNNBIP1's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without PBX4 | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |
| [[LDLRAP1]] | C | PBX4 activity raises LDLRAP1's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without PBX4 | 0.047 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |
| [[BMP8B]] | C | PBX4 activity raises BMP8B's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 2.42× lower at baseline in the lines without PBX4 | 0.066 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561; co-absent with the target |
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | C | PBX4 activity raises the cells' numbers under Mitoxantrone (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express PBX4 (3) vs lines expressing it (45) | the lines without PBX4: 0.70× the cells of the other lines | 0.074 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |
| cells under [[Pralsetinib (drug)]] 5 µM | C | PBX4 activity lowers the cells' numbers under Pralsetinib 5 µM (makes them more sensitive) | lines that do not express PBX4 (3) vs lines expressing it (45) | the lines without PBX4: 1.74× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |
| [[CABLES2]] | C | PBX4 activity raises CABLES2's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 1.85× lower at baseline in the lines without PBX4 | 0.098 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.741). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (4.2, 3.9); signed map (-41.4, -5.7). **Vector** length 118, 30.5% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +8.4 | +25.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.1 | +20.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.6 | +20.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +4.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -7.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | PBX homeobox 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,561,707-19,618,693 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

UniProt [Q9BYU1](https://www.uniprot.org/uniprotkb/Q9BYU1) carries no function annotation.

**Summary**, from NCBI Gene [80714](https://www.ncbi.nlm.nih.gov/gene/80714):

> This gene encodes a member of the pre-B cell leukemia transcription factor family. These proteins are homeobox proteins that play critical roles in embryonic development and cellular differentiation both as Hox cofactors and through Hox-independent pathways. The encoded protein contains a homeobox DNA-binding domain, but specific functions of the protein have not been determined. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:13403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13403) · Entrez [80714](https://www.ncbi.nlm.nih.gov/gene/80714) · UniProt [Q9BYU1](https://www.uniprot.org/uniprotkb/Q9BYU1) · Ensembl [ENSG00000105717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105717)

## Data

Gene col 2653: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2653); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2653, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2653]; `tensor/DDL_lfc|DDL_z.npy` [2653]; `embed/gene_vectors.npy` [2653]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2653 or target_col == 2653). Every well: [[PBX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PBX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
