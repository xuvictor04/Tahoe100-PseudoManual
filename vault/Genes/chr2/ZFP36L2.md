---
symbol: "ZFP36L2"
type: "gene"
col: 7638
ensembl_id: "ENSG00000152518"
name: "ZFP36 like 2 zinc finger CCCH-type"
location: "2p21"
module: 123
arm: "+"
pooled_cpm: 56.38
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# ZFP36L2

*ZFP36 like 2 zinc finger CCCH-type* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.01× (z +17.9, q 0e+00, up in 40 of 46 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.95× (z +7.7, q 2e-12, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.580× (z -6.3, q 2e-07, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF3]] (+0.70, fdr 7e-06), [[RHOU]] (+0.66, fdr 7e-06), [[MAFB]] (+0.64, fdr 7e-06); moves opposite to [[BTAF1]] (-0.61, fdr 1e-05), [[NAP1L4]] (-0.57, fdr 1e-05), [[STRAP]] (-0.56, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[EDN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7638.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.01×** | +17.9 | 0e+00 | 40/46 (HEC-1-A, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.11×** | +12.6 | 1e-33 | 41/47 (A-172, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.10×** | +8.6 | 2e-15 | 33/46 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.7 | 2e-12 | 36/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.94×** | +7.6 | 3e-12 | 27/46 (NCI-H460, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.70×** | +6.1 | 1e-07 | 26/47 (NCI-H460, HEC-1-A, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +5.3 | 7e-06 | 29/46 (J82, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.52×** | +4.8 | 1e-04 | 27/45 (NCI-H2030, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +4.7 | 2e-04 | 26/47 (PANC-1, HOP62, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.006 | 18/46 (NCI-H1792, SW 900, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.8 | 0.006 | 19/44 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.38×** | +3.7 | 0.011 | 18/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.6 | 0.015 | 2/48 (MIA PaCa-2, NCI-H1792) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.022 | 19/47 (SW1417, COLO 205, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.030 | 21/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7638.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.580×** | -6.3 | 2e-07 | 35/47 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -4.7 | 7e-04 | 24/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.702×** | -4.1 | 0.008 | 22/46 (A549, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.693×** | -4.0 | 0.009 | 22/47 (A498, LS 180, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.731×** | -3.6 | 0.032 | 21/46 (KATO III, LS 180, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.081 | 24/47 (HepG2/C3A, KATO III, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -3.3 | 0.081 | 22/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.759×** | -3.2 | 0.098 | 23/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7638. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 258 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.221× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 23.5 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +16.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.75× (z +12.5) | — |
| [[KATO III (line)]] | alt | 236 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.219× (z -10.0) |
| [[A-172 (line)]] | wt | 44.3 | 4 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +20.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 7.26× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.277× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 27.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +20.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.73× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 24.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +13.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.77× (z +8.6) | — |
| [[A549 (line)]] | wt | 23.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +13.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 20.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +16.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HT-29 (line)]] | alt | 126 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.259× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 29.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +12.7) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 5 µM 0.148× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 162 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 32.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.9) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 5 µM 0.350× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 57.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +15.7) ⚠ cell-cycle shift, explains ~32% of this change | [[Bortezomib (drug)]] 0.05 µM 0.261× (z -10.1) ⚠ cell-cycle shift, explains ~52% of this change |
| [[CFPAC-1 (line)]] | alt | 35.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +16.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 3.52× (z +8.5) | — |
| [[J82 (line)]] | alt | 27.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +17.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 22.4 | 2 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.82× (z +12.5) ⚠ position not correctable | — |
| [[SK-MEL-2 (line)]] | alt | 24.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +13.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 22.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +16.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW48 (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 17.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +11.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 23.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.22× (z +10.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 32.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +11.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +12.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.33× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SW1417 (line)]] | alt | 173 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 146 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 53.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7638), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF3]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[RHOU]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[MAFB]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[EDN1]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[KLF4]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[CEBPD]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[IRX3]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[MT1M]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ZFP36L1]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 | same gene group; STRING 917 |
| [[ZNF608]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[FOXQ1]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TRIM47]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTAF1]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.57 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[STRAP]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 | STRING 455 |
| [[NOMO2]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[GDAP2]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[THOC5]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ATP2C1]] | -0.54 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | -0.54 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[CRYBB2P1-1]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TIMM10B]] | -0.53 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TMEM167A]] | -0.53 | -0.53 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDN1]] | B | EDN1 activity raises ZFP36L2's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.98× lower at baseline in the lines without EDN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[TRIM15]] | B | TRIM15 activity raises ZFP36L2's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 2.67× lower at baseline in the lines without TRIM15 | 0.028 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[FOXQ1]] | B | FOXQ1 activity raises ZFP36L2's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 2.26× lower at baseline in the lines without FOXQ1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[PLEKHG6]] | B | PLEKHG6 activity raises ZFP36L2's level | lines that do not express PLEKHG6 (26) vs lines expressing it (24) | 2.12× lower at baseline in the lines without PLEKHG6 | 0.035 | ⚠ within organs, on part of the lines; also absent: SCNN1A, KDF1, RNF39; maybe low, not absent |
| [[SHROOM3]] | B | SHROOM3 activity raises ZFP36L2's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without SHROOM3 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[CYP3A5]] | B | CYP3A5 activity raises ZFP36L2's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.22× lower at baseline in the lines without CYP3A5 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[HDAC6]] | B | HDAC6 activity raises ZFP36L2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.2, 13.2); signed map (49.5, 11.9). **Vector** length 131, 39.8% of its response variance represented; |z| ≥ 3 in 1,179 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +10.3 | +17.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +9.7 | +12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.9 | +8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +7.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.0 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.2 | +3.9 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.0 | +3.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.8 | +2.0 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.1 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.0 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.5 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ZFP36 like 2 zinc finger CCCH-type |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:43,222,402-43,226,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERF2, TIS11D; previously BRF2 |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Reactome | 2 pathways, smallest: M-decay: degradation of maternal mRNAs by maternally stored factors; Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [P47974](https://www.uniprot.org/uniprotkb/P47974) (mRNA decay activator protein ZFP36L2):

> Zinc-finger RNA-binding protein that destabilizes several cytoplasmic AU-rich element (ARE)-containing mRNA transcripts by promoting their poly(A) tail removal or deadenylation, and hence provide a mechanism for attenuating protein synthesis. Acts as a 3'-untranslated region (UTR) ARE mRNA-binding adapter protein to communicate signaling events to the mRNA decay machinery. Functions by recruiting the CCR4-NOT deadenylase complex and probably other components of the cytoplasmic RNA decay …

**Summary**, from NCBI Gene [678](https://www.ncbi.nlm.nih.gov/gene/678):

> This gene is a member of the TIS11 family of early response genes. Family members are induced by various agonists such as the phorbol ester TPA and the polypeptide mitogen EGF. The encoded protein contains a distinguishing putative zinc finger domain with a repeating cys-his motif. This putative nuclear transcription factor most likely functions in regulating the response to growth factors. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1108) · Entrez [678](https://www.ncbi.nlm.nih.gov/gene/678) · UniProt [P47974](https://www.uniprot.org/uniprotkb/P47974) · Ensembl [ENSG00000152518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152518)

## Data

Gene col 7638: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7638); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7638, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7638]; `tensor/DDL_lfc|DDL_z.npy` [7638]; `embed/gene_vectors.npy` [7638]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7638 or target_col == 7638). Every well: [[ZFP36L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP36L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
