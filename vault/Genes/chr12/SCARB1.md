---
symbol: "SCARB1"
type: "gene"
col: 1042
ensembl_id: "ENSG00000073060"
name: "scavenger receptor class B member 1"
location: "12q24.31"
module: 16
arm: "-"
pooled_cpm: 75.94
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SCARB1

*scavenger receptor class B member 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.57× (z +7.3, q 1e-10, up in 28 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[HI-TOPK-032 (drug)]] 5 µM: 1.72× (z +4.9, q 3e-04, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.403× (z -21.4, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3C2A]] (+0.65, fdr 7e-06), [[P4HA1]] (+0.60, fdr 1e-05), [[RAB6A]] (+0.56, fdr 2e-05); moves opposite to [[NHLRC2]] (-0.59, fdr 1e-05), [[ZNF620]] (-0.55, fdr 1e-05), [[ZNF776]] (-0.54, fdr 2e-05).
> It sits in the **-** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DRD4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.57×** | +7.3 | 1e-10 | 28/47 (HEC-1-A, A-172, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.72×** | +4.9 | 3e-04 | 28/46 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +4.7 | 4e-04 | 23/47 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.53×** | +4.4 | 0.002 | 23/48 (HEC-1-A, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.002 | 24/47 (SHP-77, NCI-H2347, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +3.7 | 0.020 | 15/47 (C32, NCI-H23, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.097 | 11/47 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.13 | 14/47 (LOX-IMVI, NCI-H2347, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | 1.41× | +3.1 | 0.13 | 13/47 (COLO 205, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | 1.20× | +3.0 | 0.14 | 14/47 (PANC-1, A549, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.403×** | -21.4 | 0e+00 | 40/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.358×** | -17.0 | 0e+00 | 42/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.408×** | -15.4 | 0e+00 | 38/47 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.489×** | -11.8 | 6e-30 | 37/45 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.711×** | -8.0 | 1e-13 | 34/47 (NCI-H1792, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.628×** | -8.0 | 2e-13 | 30/47 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.661×** | -6.8 | 7e-10 | 27/42 (SW48, SNU-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.664×** | -6.5 | 6e-09 | 27/44 (SNU-1, A-427, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.703×** | -6.0 | 1e-07 | 31/47 (HCT15, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.710×** | -5.9 | 2e-07 | 27/47 (COLO 205, SNU-423, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.747×** | -5.0 | 3e-05 | 25/47 (COLO 205, A-172, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -4.9 | 5e-05 | 4/49 (AsPC-1, NCI-H661, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.753×** | -4.9 | 5e-05 | 25/46 (COLO 205, BT-474, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.766×** | -4.6 | 2e-04 | 26/47 (COLO 205, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.769×** | -4.5 | 3e-04 | 25/46 (A-172, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.785×** | -4.1 | 0.001 | 23/47 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.799×** | -3.8 | 0.004 | 18/47 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.808×** | -3.7 | 0.007 | 15/48 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.814×** | -3.5 | 0.012 | 18/47 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.818×** | -3.4 | 0.016 | 18/47 (SW 1088, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.869× | -3.3 | 0.024 | 10/47 (HCT15, RKO, …) | all doses, flat |  |
| [[OTS514 (drug)]] 5 µM |  | **0.698×** | -3.2 | 0.029 | 13/45 (H4, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.830×** | -3.2 | 0.031 | 12/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 237 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.184× (z -15.2) |
| [[SNU-423 (line)]] | alt | 206 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -26.7) |
| [[A549 (line)]] | wt | 91.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -20.7) |
| [[A-172 (line)]] | wt | 47.9 | 3 (2 ⚠) | 4 | [[Ixazomib citrate (drug)]] 5 µM 3.31× (z +10.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.58× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.141× (z -16.9) |
| [[HCT15 (line)]] | alt | 293 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -22.6) |
| [[HepG2_C3A (line)]] | wt | 207 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 113 | 1 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.248× (z -14.1) |
| [[PANC-1 (line)]] | alt | 107 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -24.2) |
| [[AsPC-1 (line)]] | alt | 92.5 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.237× (z -11.4) |
| [[CHP-212 (line)]] | wt | 186 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0581× (z -23.9) |
| [[HS-578T (line)]] | alt | 51.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 63.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -18.8) |
| [[SNU-1 (line)]] | wt | 97.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.6) |
| [[SW480 (line)]] | alt | 65.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.366× (z -12.0) |
| [[A498 (line)]] | wt | 73.8 | 1 (1 ⚠) | 2 | [[Bortezomib (drug)]] 0.05 µM 2.85× (z +9.4) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -11.6) |
| [[C-33 A (line)]] | alt | 97.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.5) |
| [[C32 (line)]] | wt | 200 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -22.5) |
| [[HEC-1-A (line)]] | alt | 24.9 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.50× (z +13.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.47× (z +10.5) | — |
| [[KATO III (line)]] | alt | 44.8 | 2 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.18× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.1) |
| [[SW1417 (line)]] | alt | 52.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.1) |
| [[BT-474 (line)]] | alt | 85.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[HOP62 (line)]] | alt | 55.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 81.0 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -20.3) |
| [[NCI-H661 (line)]] | alt | 77.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0335× (z -14.9) |
| [[A-427 (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 83.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0802× (z -13.9) |
| [[H4 (line)]] | wt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0772× (z -11.4) |
| [[HT-29 (line)]] | alt | 50.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 34.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.164× (z -10.0) |
| [[LoVo (line)]] | wt | 51.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.337× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 25.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 89.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H2347 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +14.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 73.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 81.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.9) |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.1) |
| [[SW48 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0718× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 84.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3C2A]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[RAB6A]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ZDHHC9]] | +0.55 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[MED26]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[HSPA5]] | +0.54 | +0.56 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[NEAT1]] | +0.54 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[ERO1A]] | +0.54 | +0.59 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_HYPOXIA |
| [[KDM4B]] | +0.54 | +0.48 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[ADAM17]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[SCD]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 | STRING 721 |
| [[CD81]] | +0.53 | +0.55 / +0.51 | both halves | 1e-05 | STRING 995 |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[VEZF1]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CHAMP1]] | -0.53 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[PPP1R1C]] | -0.53 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H7B]] | -0.52 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SENP1]] | -0.52 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ERCC4]] | -0.52 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[CMTR2]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[AMIGO2]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ZNF268]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DRD4]] | B | DRD4 activity strengthens SCARB1's drug response | lines that do not express DRD4 (5) vs lines expressing it (42) | the lines without DRD4 respond 0.38× as strongly (z diff +3.39); strongest at Homoharringtonine 0.5 µM: 0.90x vs 0.37x (z diff +6.5) | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers SCARB1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DRD4]] | B | DRD4 activity raises SCARB1's level | lines that do not express DRD4 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without DRD4 | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **-** arm (projection on the module's main direction -0.547). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (15.3, -18.2); signed map (-35.2, 22.8). **Vector** length 128, 36.8% of its response variance represented; |z| ≥ 3 in 1,203 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.9 | +4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.7 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -15.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.2 | -17.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -21.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.0 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -4.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.2 | -3.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.7 | -2.7 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | scavenger receptor class B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:124,776,856-124,882,668 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRB1, CLA-1, CLA1, SR-BI; previously CD36L1 |
| Gene groups (HGNC) | Scavenger receptors |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, HYPOXIA, ADIPOGENESIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 7 pathways, smallest: HDL clearance; Scavenging by Class B Receptors; Binding and Uptake of Ligands by Scavenger Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WTV0](https://www.uniprot.org/uniprotkb/Q8WTV0) (Scavenger receptor class B member 1):

> Receptor for different ligands such as phospholipids, cholesterol ester, lipoproteins, phosphatidylserine and apoptotic cells. Receptor for HDL, mediating selective uptake of cholesteryl ether and HDL-dependent cholesterol efflux. Also facilitates the flux of free and esterified cholesterol between the cell surface and apoB-containing lipoproteins and modified lipoproteins, although less efficiently than HDL. May be involved in the phagocytosis of apoptotic cells, via its phosphatidylserine …

**Summary**, from NCBI Gene [949](https://www.ncbi.nlm.nih.gov/gene/949):

> The protein encoded by this gene is a plasma membrane receptor for high density lipoprotein cholesterol (HDL). The encoded protein mediates cholesterol transfer to and from HDL. In addition, this protein is a receptor for hepatitis C virus glycoprotein E2 and facilitates cell entry by the virus, SARS-CoV2. [provided by RefSeq, Oct 2021]

**Accessions** — [HGNC:1664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1664) · Entrez [949](https://www.ncbi.nlm.nih.gov/gene/949) · UniProt [Q8WTV0](https://www.uniprot.org/uniprotkb/Q8WTV0) · Ensembl [ENSG00000073060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073060)

## Data

Gene col 1042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1042); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1042]; `tensor/DDL_lfc|DDL_z.npy` [1042]; `embed/gene_vectors.npy` [1042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1042 or target_col == 1042). Every well: [[SCARB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCARB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
