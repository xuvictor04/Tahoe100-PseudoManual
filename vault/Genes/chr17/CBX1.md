---
symbol: "CBX1"
type: "gene"
col: 2951
ensembl_id: "ENSG00000108468"
name: "chromobox 1"
location: "17q21.32"
module: 57
arm: "+"
pooled_cpm: 71.56
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# CBX1

*chromobox 1* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.56× (z +14.9, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 3.76×, PANC-1 3.96×, A-172 3.60×, KATO III 3.81×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 3.86×, PANC-1 3.59×, A-172 3.34×, CFPAC-1 3.19×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.475× (z -15.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA1]] (+0.70, fdr 1e-05), [[USP48]] (+0.67, fdr 9e-06), [[SKP2]] (+0.66, fdr 1e-05); moves opposite to [[NEPRO-AS1]] (-0.65, fdr 1e-05), [[ANGPT2]] (-0.65, fdr 3e-05), [[LINC01004]] (-0.63, fdr 4e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 14 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2951.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 3.76×, PANC-1 3.96×, A-172 3.60×, KATO III 3.81×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 3.86×, PANC-1 3.59×, A-172 3.34×, CFPAC-1 3.19×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.56×** | +14.9 | 0e+00 | 48/49 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +13.2 | 2e-37 | 41/42 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +9.8 | 1e-20 | 36/45 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.33×** | +4.5 | 0.001 | 28/48 (hTERT-HPNE, LS 180, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.32×** | +4.4 | 0.001 | 29/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.30×** | +4.1 | 0.003 | 29/48 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.64×** | +4.1 | 0.003 | 27/49 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.63×** | +4.1 | 0.003 | 30/47 (C32, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | **1.27×** | +3.8 | 0.009 | 27/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **1.28×** | +3.8 | 0.009 | 22/47 (PANC-1, J82, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.27×** | +3.7 | 0.009 | 28/48 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.27×** | +3.7 | 0.009 | 24/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.4 | 0.034 | 16/48 (CHP-212, RKO, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.2 | 0.052 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +3.1 | 0.078 | 20/47 (NCI-H23, HOP62, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2951.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.475×** | -15.4 | 0e+00 | 47/48 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.566×** | -8.6 | 2e-15 | 42/48 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.631×** | -7.3 | 7e-11 | 40/48 (NCI-H2347, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.802×** | -4.6 | 6e-04 | 30/48 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.010 | 26/48 (MIA PaCa-2, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.66× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -20.0) |
| [[PANC-1 (line)]] | alt | 102 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -10.8) |
| [[SNU-423 (line)]] | alt | 55.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.9) |
| [[SW480 (line)]] | alt | 61.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -8.6) |
| [[A-172 (line)]] | wt | 113 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 61.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 47.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 62.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -18.5) |
| [[NCI-H2347 (line)]] | alt | 104 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -18.3) |
| [[SK-MEL-2 (line)]] | alt | 76.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.4) |
| [[SW 900 (line)]] | alt | 87.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.9) |
| [[A-427 (line)]] | wt | 91.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -9.7) |
| [[A498 (line)]] | wt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 59.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 65.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.9) |
| [[H4 (line)]] | wt | 75.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -14.6) |
| [[HEC-1-A (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HOP62 (line)]] | alt | 80.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 63.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[KATO III (line)]] | alt | 50.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 30.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 105 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.1) |
| [[RKO (line)]] | wt | 89.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.5) |
| [[SW1417 (line)]] | alt | 60.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -9.6) |
| [[AN3 CA (line)]] | alt | 138 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -9.3) |
| [[CHP-212 (line)]] | wt | 131 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -8.6) |
| [[COLO 205 (line)]] | alt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.1) |
| [[Hs 766T (line)]] | wt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 51.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LoVo (line)]] | wt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 89.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 86.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 42.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.9) |
| [[SHP-77 (line)]] | alt | 99.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 53.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.4) |
| [[SW48 (line)]] | wt | 60.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.1) |
| [[BT-474 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 72.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | +0.70 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[USP48]] | +0.67 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[SKP2]] | +0.66 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.65 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[PARP1]] | +0.65 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[HACE1]] | +0.64 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[NDRG3]] | +0.63 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[NUDT21]] | +0.63 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[KDM1A]] | +0.62 | +0.67 / +0.61 | both halves | 7e-06 | STRING 513 |
| [[PAPSS1]] | +0.61 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[IARS2]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CEP57L1]] | +0.60 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEPRO-AS1]] | -0.65 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ANGPT2]] | -0.65 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[LINC01004]] | -0.63 | -0.66 / -0.40 | both halves | 4e-05 |  |
| [[SLC9A8]] | -0.62 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[NEK8]] | -0.62 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | -0.62 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[PHLDA2]] | -0.61 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[GCNT4]] | -0.60 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[SPHK1]] | -0.60 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[BOLA1]] | -0.59 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[C14orf119]] | -0.59 | -0.57 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises CBX1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without KATNAL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[LINC00520]] | B | LINC00520 activity lowers CBX1's level | lines that do not express LINC00520 (31) vs lines expressing it (19) | 1.41× higher at baseline in the lines without LINC00520 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224322, LINC00589, LINC02930 |
| [[HLTF]] | B | HLTF activity raises CBX1's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without HLTF | 0.086 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[GGH]] | B | GGH activity raises CBX1's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without GGH | 0.099 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (2.0, -10.7); signed map (-37.2, -12.3). **Vector** length 116, 34.6% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.3 | +4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.1 | +2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | +5.0 | +3.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.6 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.4 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.5 | -15.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.5 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.7 | -7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +0.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.9 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -0.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | chromobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,070,052-48,101,478 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HP1Hs-beta, M31, MOD1, CBX, HP1-BETA, Hp1beta |
| Gene groups (HGNC) | Chromobox family |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 8 pathways, smallest: ChAHP complex assembly; CHD3, CHD4, CHD5 subfamily; HCMV Early Events |
| Matched by | ensembl_id |

**Function**, from UniProt [P83916](https://www.uniprot.org/uniprotkb/P83916) (Chromobox protein homolog 1):

> Component of heterochromatin, which recognizes and binds histone H3 tails methylated at 'Lys-9', leading to epigenetic repression. Also recognizes and binds histone H1.4 methylated at 'Lys-26' (H1.4K26me). Excluded from chromatin when histone H1.4 is Simultaneously methylated at Lys-26 (H1.4K26me) and phosphorylated at Ser-27 (H1.4S27Ph). Interaction with lamin B receptor (LBR) can contribute to the association of the heterochromatin with the inner nuclear membrane (By similarity).

**Summary**, from NCBI Gene [10951](https://www.ncbi.nlm.nih.gov/gene/10951):

> This gene encodes a highly conserved nonhistone protein, which is a member of the heterochromatin protein family . The protein is enriched in the heterochromatin and associated with centromeres. The protein has a single N-terminal chromodomain which can bind to histone proteins via methylated lysine residues, and a C-terminal chromo shadow-domain (CSD) which is responsible for the homodimerization and interaction with a number of chromatin-associated nonhistone proteins. The protein may play an …

**Accessions** — [HGNC:1551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1551) · Entrez [10951](https://www.ncbi.nlm.nih.gov/gene/10951) · UniProt [P83916](https://www.uniprot.org/uniprotkb/P83916) · Ensembl [ENSG00000108468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108468)

## Data

Gene col 2951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2951); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2951]; `tensor/DDL_lfc|DDL_z.npy` [2951]; `embed/gene_vectors.npy` [2951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2951 or target_col == 2951). Every well: [[CBX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
