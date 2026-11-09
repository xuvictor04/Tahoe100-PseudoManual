---
symbol: "TBX3"
type: "gene"
col: 5655
ensembl_id: "ENSG00000135111"
name: "T-box transcription factor 3"
location: "12q24.21"
module: 151
arm: "+"
pooled_cpm: 38.66
n_lines_expressing: 40
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# TBX3

*T-box transcription factor 3* — 12q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +17.3, q 0e+00, up in 28 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.713× (z -5.6, q 1e-05, down in 19 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.625× (z -4.0, q 0.015, down in 14 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (HOP62 0.166×, RPMI-7951 0.305×, CHP-212 0.186×, HS-578T 0.356×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (KATO III 0.0718×, HOP62 0.159×, SHP-77 0.100×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RPMI-7951 0.326×, HS-578T 0.474×, HOP62 0.552×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.0973×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB38]] (+0.56, fdr 1e-05), [[CDC42EP3]] (+0.53, fdr 2e-05), [[TUT7]] (+0.53, fdr 2e-05); moves opposite to [[TM9SF2]] (-0.58, fdr 2e-05), [[SEPTIN7P14]] (-0.55, fdr 3e-05), [[NOMO2]] (-0.48, fdr 5e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GYPC]] → it (grade B ⚠); 6 go from it, the strongest it → [[NOMO2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5655.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +17.3 | 0e+00 | 28/38 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.35×** | +14.0 | 3e-42 | 27/36 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +13.8 | 4e-41 | 21/35 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +11.5 | 2e-28 | 29/38 (HS-578T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +11.1 | 2e-26 | 28/38 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +8.2 | 2e-14 | 21/38 (RKO, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +8.1 | 5e-14 | 21/38 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +7.5 | 5e-12 | 21/38 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +6.4 | 8e-09 | 20/38 (A498, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.1 | 6e-08 | 19/34 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +5.9 | 2e-07 | 20/39 (RPMI-7951, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +5.5 | 2e-06 | 17/37 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.1 | 2e-05 | 14/32 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.30×** | +4.3 | 8e-04 | 17/38 (NCI-H1573, A-172, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.003 | 16/38 (PANC-1, SW1417, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.003 | 14/38 (SW1417, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.7 | 0.007 | 14/38 (SW480, PANC-1, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.046 | 5/38 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5655.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 5 lines (HOP62 0.166×, RPMI-7951 0.305×, CHP-212 0.186×, HS-578T 0.356×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (KATO III 0.0718×, HOP62 0.159×, SHP-77 0.100×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (RPMI-7951 0.326×, HS-578T 0.474×, HOP62 0.552×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (COLO 205 0.0973×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.713×** | -5.6 | 1e-05 | 19/32 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.625×** | -4.0 | 0.015 | 14/36 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.790×** | -3.7 | 0.035 | 15/27 (HOP62, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.070 | 17/38 (HOP62, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.844× | -3.3 | 0.11 | 13/38 (A-172, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.947× | -3.1 | 0.18 | 3/38 (HOP62, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5655. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 213 | 2 | 7 (5 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.44× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.166× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 26.8 | 8 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.57× (z +12.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.52× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 180 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.61× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -16.3) |
| [[HS-578T (line)]] | alt | 123 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +18.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 13.1 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 5.06× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 126 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0986× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.186× (z -10.3) |
| [[A498 (line)]] | wt | 16.4 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.47× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 130 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.79× (z +10.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -11.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[H4 (line)]] | wt | 70.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -8.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW1417 (line)]] | alt | 79.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.7) | — |
| [[SW480 (line)]] | alt | 23.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.0) | — |
| [[C32 (line)]] | wt | 23.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 4.53× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -9.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 30.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0718× (z -19.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 12.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +12.9) | — |
| [[RKO (line)]] | wt | 16.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 25.4 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.167× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.253× (z -8.6) |
| [[SW 900 (line)]] | alt | 30.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.4) | — |
| [[A-427 (line)]] | wt | 12.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.42× (z +10.1) | — |
| [[A549 (line)]] | wt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0973× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 80.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -9.0) |
| [[LoVo (line)]] | wt | 62.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.08× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 69.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -16.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.64 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5655), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB38]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CDC42EP3]] | +0.53 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[TUT7]] | +0.53 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[PALM2AKAP2]] | +0.53 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CAMSAP2]] | +0.52 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[MIR100HG]] | +0.51 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[HRH1]] | +0.51 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[UTP3]] | +0.50 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[IPO9-AS1]] | +0.50 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[RCAN1]] | +0.50 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[SVIL]] | +0.50 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[SLC43A3]] | +0.50 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF2]] | -0.58 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[SEPTIN7P14]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[NOMO2]] | -0.48 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PCCB]] | -0.48 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[MRPS31P5-1]] | -0.48 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[RPA1]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[SLC9A6]] | -0.47 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[NAPB]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[NUDT21]] | -0.46 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[SGK3]] | -0.46 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[TMEM50B]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[RCN2]] | -0.46 | -0.36 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GYPC]] | B | GYPC activity raises TBX3's level | lines that do not express GYPC (35) vs lines expressing it (15) | 3.07× lower at baseline in the lines without GYPC | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOMO2]] | B | TBX3 activity raises NOMO2's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 1.24× lower at baseline in the lines without TBX3 | 0.053 | ⚠ within organs, on part of the lines |
| [[GYPC]] | B | TBX3 activity raises GYPC's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without TBX3 | 0.074 | ⚠ within organs, on part of the lines |
| [[ZNF75A]] | B | TBX3 activity raises ZNF75A's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 1.11× lower at baseline in the lines without TBX3 | 0.075 | ⚠ within organs, on part of the lines |
| [[EID2]] | B | TBX3 activity raises EID2's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 1.42× lower at baseline in the lines without TBX3 | 0.076 | ⚠ within organs, on part of the lines |
| cells under [[Pravastatin (sodium) (drug)]] 5 µM | B | TBX3 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express TBX3 (10) vs lines expressing it (38) | the lines without TBX3: 0.87× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines |
| [[ZFP36L1]] | B | TBX3 activity lowers ZFP36L1's level | lines that do not express TBX3 (10) vs lines expressing it (40) | 2.19× higher at baseline in the lines without TBX3 | 0.092 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.1, 3.4); signed map (18.1, 39.3). **Vector** length 102, 23.0% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +8.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.7 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -1.8 | -5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.7 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -0.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | T-box transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.21 — chr12:114,670,255-114,684,175 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TBX3-ISO, XHL; previously UMS |
| Gene groups (HGNC) | T-box transcription factors |
| Reactome | 2 pathways, smallest: Transcriptional and post-translational regulation of MITF-M expression and activity; MITF-M-regulated melanocyte development |
| Matched by | ensembl_id |

**Function**, from UniProt [O15119](https://www.uniprot.org/uniprotkb/O15119) (T-box transcription factor TBX3):

> Transcriptional repressor involved in developmental processes. Binds to the palindromic T site 5'-TTCACACCTAGGTGTGAA-3' DNA sequence, or a half-site, which are present in the regulatory region of several genes. Probably plays a role in limb pattern formation. Required for mammary placode induction, and maintenance of the mammary buds during development (By similarity). Involved in branching morphogenesis in both developing lungs and adult mammary glands, via negative modulation of target genes; …

**Summary**, from NCBI Gene [6926](https://www.ncbi.nlm.nih.gov/gene/6926):

> This gene is a member of a phylogenetically conserved family of genes that share a common DNA-binding domain, the T-box. T-box genes encode transcription factors involved in the regulation of developmental processes. This protein is a transcriptional repressor and is thought to play a role in the anterior/posterior axis of the tetrapod forelimb. Mutations in this gene cause ulnar-mammary syndrome, affecting limb, apocrine gland, tooth, hair, and genital development. Alternative splicing of this …

**Accessions** — [HGNC:11602](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11602) · Entrez [6926](https://www.ncbi.nlm.nih.gov/gene/6926) · UniProt [O15119](https://www.uniprot.org/uniprotkb/O15119) · Ensembl [ENSG00000135111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135111)

## Data

Gene col 5655: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5655); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5655, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5655]; `tensor/DDL_lfc|DDL_z.npy` [5655]; `embed/gene_vectors.npy` [5655]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5655 or target_col == 5655). Every well: [[TBX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
