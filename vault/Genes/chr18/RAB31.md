---
symbol: "RAB31"
type: "gene"
col: 9654
ensembl_id: "ENSG00000168461"
name: "RAB31, member RAS oncogene family"
location: "18p11.22"
module: 66
arm: "+"
pooled_cpm: 92.9
n_lines_expressing: 34
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# RAB31

*RAB31, member RAS oncogene family* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +7.5, q 5e-11, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.599× (z -11.7, q 6e-29, down in 26 of 32 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB27B]] (+0.58, fdr 1e-05), [[KLHL5]] (+0.56, fdr 7e-05), [[NTN4]] (+0.56, fdr 1e-05); moves opposite to [[SPATA7]] (-0.50, fdr 4e-05), [[TGDS]] (-0.49, fdr 7e-05), [[POM121C]] (-0.47, fdr 4e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HEG1]] → it (grade B ⚠); 5 go from it, the strongest it → [[P3H2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +7.5 | 5e-11 | 21/32 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.1 | 4e-10 | 17/33 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 6e-06 | 19/33 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.25×** | +5.1 | 4e-05 | 18/32 (AsPC-1, A-172, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.34×** | +4.6 | 5e-04 | 15/31 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 7e-04 | 17/31 (hTERT-HPNE, HOP62, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.1 | 0.003 | 15/28 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.008 | 18/33 (A-172, NCI-H1573, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +3.7 | 0.011 | 15/32 (A-172, PANC-1, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.088 | 8/33 (HOP62, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9654.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -11.7 | 6e-29 | 26/32 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.607×** | -11.4 | 1e-27 | 22/32 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.511×** | -10.9 | 2e-25 | 26/32 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.568×** | -9.2 | 6e-18 | 27/32 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -7.6 | 3e-12 | 25/33 (NCI-H460, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.713×** | -5.3 | 1e-05 | 21/32 (NCI-H460, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.728×** | -5.0 | 6e-05 | 18/31 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.563×** | -4.9 | 8e-05 | 19/31 (RPMI-7951, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.743×** | -4.8 | 9e-05 | 18/32 (BT-474, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.753×** | -4.6 | 2e-04 | 17/32 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.764×** | -4.4 | 6e-04 | 17/33 (BT-474, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.633×** | -3.9 | 0.005 | 15/32 (A-172, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.9 | 0.005 | 13/32 (NCI-H460, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.790×** | -3.8 | 0.005 | 15/32 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.780×** | -3.8 | 0.005 | 17/32 (NCI-H460, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.642×** | -3.8 | 0.005 | 18/32 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.869× | -3.2 | 0.034 | 9/32 (A498, SK-MEL-2, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.685×** | -3.2 | 0.034 | 14/31 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.872× | -3.1 | 0.040 | 8/32 (AsPC-1, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.826×** | -3.1 | 0.042 | 11/32 (Panc 03.27, SW 900, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.778×** | -2.9 | 0.079 | 9/32 (NCI-H460, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 304 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -37.2) |
| [[SW 900 (line)]] | alt | 354 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -18.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -12.4) |
| [[A-427 (line)]] | wt | 126 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -11.2) ⚠ cell-cycle shift, explains ~73% of this change |
| [[PANC-1 (line)]] | alt | 219 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -21.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 156 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -13.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -12.0) |
| [[HOP62 (line)]] | alt | 162 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 5 µM 2.65× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 124 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -15.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -15.4) |
| [[A-172 (line)]] | wt | 136 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -16.4) |
| [[Hs 766T (line)]] | wt | 162 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.82× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.359× (z -10.6) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.547× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 229 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -19.4) |
| [[SNU-423 (line)]] | alt | 151 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -13.7) |
| [[A549 (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.405× (z -8.5) |
| [[BT-474 (line)]] | alt | 35.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.87× (z +10.1) | — |
| [[H4 (line)]] | wt | 114 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 40.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.2) |
| [[NCI-H23 (line)]] | alt | 80.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -16.6) |
| [[A498 (line)]] | wt | 27.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.98× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0547× (z -9.2) |
| [[HS-578T (line)]] | alt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -13.0) |
| [[J82 (line)]] | alt | 90.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.84× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 62.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 25.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 115 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.07× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.250× (z -9.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW 1088 (line)]] | alt | 249 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0647× (z -10.8) |
| [[AN3 CA (line)]] | alt | 15.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.71 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.91 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 180 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.49 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.79 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.02 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.36 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB27B]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 | same gene group; pathway: RAB GEFs exchange GTP for GDP on RABs |
| [[KLHL5]] | +0.56 | +0.37 / +0.62 | both halves | 7e-05 |  |
| [[NTN4]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[OSMR]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PALLD]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[PHLDB2]] | +0.55 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[TCIM]] | +0.54 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[IL6]] | +0.52 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[MPDZ]] | +0.50 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[CDKN2B]] | +0.50 | +0.37 / +0.47 | both halves | 8e-05 |  |
| [[CYP1B1]] | +0.49 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[AHR]] | +0.49 | +0.32 / +0.49 | both halves | 2e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA7]] | -0.50 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[TGDS]] | -0.49 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[POM121C]] | -0.47 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[POMT1]] | -0.47 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[COG7]] | -0.46 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[CDK7]] | -0.45 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[PLEKHA2]] | -0.45 | -0.26 / -0.36 | both halves | 3e-04 |  |
| [[PEX11B]] | -0.45 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[SLC25A14]] | -0.44 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[EEF2K]] | -0.44 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[TRMU]] | -0.43 | -0.25 / -0.47 | both halves | 4e-04 |  |
| [[TMEM231]] | -0.43 | -0.20 / -0.52 | ⚠ one half (not replicated) | 7e-04 |  |
| [[MMS19]] | -0.43 | -0.24 / -0.50 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises RAB31's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 4.21× lower at baseline in the lines without HEG1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[FBN1]] | B | FBN1 activity raises RAB31's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.77× lower at baseline in the lines without FBN1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[MTOR]] | B | MTOR activity lowers RAB31's level | compounds that target MTOR: 3 of 8 raise it (Bimiralisib, Rapamycin, Temsirolimus) | 38% of the class's compounds vs 2.0% of all compounds | 0.088 | ⚠ off-target possible; 3 compounds |
| [[GJA1]] | C | GJA1 activity raises RAB31's level | lines that do not express GJA1 (26) vs lines expressing it (24) | 5.49× lower at baseline in the lines without GJA1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1; co-absent with the target |
| [[HECW2]] | C | HECW2 activity raises RAB31's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 5.82× lower at baseline in the lines without HECW2 | 0.059 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H2]] | B | RAB31 activity raises P3H2's level | lines that do not express RAB31 (16) vs lines expressing it (34) | 3.18× lower at baseline in the lines without RAB31 | 0.040 | ⚠ within organs, on part of the lines; also absent: VEGFC, HERC5, NR3C1 |
| [[RCHY1]] | B | RAB31 activity lowers RCHY1's level | lines that do not express RAB31 (16) vs lines expressing it (34) | 1.22× higher at baseline in the lines without RAB31 | 0.082 | ⚠ within organs, on part of the lines; also absent: VEGFC, HERC5, NR3C1 |
| [[RASD1]] | B | RAB31 activity raises RASD1's level | lines that do not express RAB31 (16) vs lines expressing it (34) | 1.01× lower at baseline in the lines without RAB31 | 0.082 | ⚠ within organs, on part of the lines; also absent: VEGFC, HERC5, NR3C1 |
| [[AGPAT4]] | B | RAB31 activity raises AGPAT4's level | lines that do not express RAB31 (16) vs lines expressing it (34) | 2.53× lower at baseline in the lines without RAB31 | 0.097 | ⚠ within organs, on part of the lines; also absent: VEGFC, HERC5, NR3C1 |
| [[GJA1]] | C | RAB31 activity raises GJA1's level | lines that do not express RAB31 (16) vs lines expressing it (34) | 7.24× lower at baseline in the lines without RAB31 | 0.065 | ⚠ within organs, on part of the lines; also absent: VEGFC, HERC5, NR3C1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.8, 20.9); signed map (48.0, 21.4). **Vector** length 105, 29.3% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.5 | +3.9 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[NG25 (drug)]] 5 µM |  | -2.2 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -11.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB31, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:9,708,275-9,862,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Rab22B |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | TGF_BETA_SIGNALING, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 7 pathways, smallest: RAB geranylgeranylation; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13636](https://www.uniprot.org/uniprotkb/Q13636) (Ras-related protein Rab-31):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. Required for the integrity and for normal function of the Golgi apparatus and the trans-Golgi network. Plays a role in …

**Summary**, from NCBI Gene [11031](https://www.ncbi.nlm.nih.gov/gene/11031):

> Enables G protein activity; GDP binding activity; and GTP binding activity. Involved in several processes, including Golgi to plasma membrane protein transport; cellular response to insulin stimulus; and receptor internalization. Located in early endosome; phagocytic vesicle; and trans-Golgi network membrane. Biomarker of severe acute respiratory syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9771) · Entrez [11031](https://www.ncbi.nlm.nih.gov/gene/11031) · UniProt [Q13636](https://www.uniprot.org/uniprotkb/Q13636) · Ensembl [ENSG00000168461](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168461)

## Data

Gene col 9654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9654); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9654]; `tensor/DDL_lfc|DDL_z.npy` [9654]; `embed/gene_vectors.npy` [9654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9654 or target_col == 9654). Every well: [[RAB31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
