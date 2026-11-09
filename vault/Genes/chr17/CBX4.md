---
symbol: "CBX4"
type: "gene"
col: 6555
ensembl_id: "ENSG00000141582"
name: "chromobox 4"
location: "17q25.3"
module: 59
arm: "+"
pooled_cpm: 30.39
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# CBX4

*chromobox 4* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.99× (z +16.4, q 0e+00, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HT-29 0.139×, SW480 0.250×, MIA PaCa-2 0.123×, SW1417 0.270×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW1417 0.172×, NCI-H2347 0.230×, A-427 0.201×, COLO 205 0.168×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.177×, HT-29 0.249×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBX8]] (+0.71, fdr 7e-06, ⚠ same locus), [[PIM3]] (+0.71, fdr 7e-06), [[GLIS2]] (+0.68, fdr 7e-06), [[SAT2]] (+0.63, fdr 8e-06); moves opposite to [[ZNF731P]] (-0.64, fdr 7e-06), [[XRCC5]] (-0.59, fdr 9e-06), [[EFTUD2]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CNKSR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.99×** | +16.4 | 0e+00 | 44/47 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +7.0 | 5e-10 | 31/47 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +6.9 | 8e-10 | 38/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +6.5 | 7e-09 | 33/48 (LoVo, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +6.5 | 7e-09 | 38/48 (KATO III, NCI-H2347, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.75×** | +5.7 | 1e-06 | 31/48 (PANC-1, NCI-H460, …) | top dose only | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +5.7 | 1e-06 | 34/48 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.6 | 2e-06 | 30/45 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +5.2 | 1e-05 | 31/48 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.4 | 6e-04 | 25/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +4.3 | 0.001 | 28/48 (C32, NCI-H2030, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.46×** | +4.0 | 0.003 | 25/46 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +3.8 | 0.005 | 25/48 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.44×** | +3.8 | 0.005 | 22/46 (NCI-H460, LS 180, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.39×** | +3.5 | 0.020 | 22/48 (NCI-H460, LS 180, …) | top dose only | composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.025 | 21/46 (SNU-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.033 | 21/48 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.033 | 22/48 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.095 | 19/48 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.47×** | +2.9 | 0.100 | 15/48 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6555.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (HT-29 0.139×, SW480 0.250×, MIA PaCa-2 0.123×, SW1417 0.270×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW1417 0.172×, NCI-H2347 0.230×, A-427 0.201×, COLO 205 0.168×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.177×, HT-29 0.249×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.708× | -3.6 | 0.19 | 17/37 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.745× | -3.2 | 0.43 | 17/47 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.8) | — |
| [[SW1417 (line)]] | alt | 53.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -13.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +17.5) | — |
| [[COLO 205 (line)]] | alt | 47.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +14.1) | — |
| [[HOP62 (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +18.4) | — |
| [[HT-29 (line)]] | alt | 58.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -14.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +16.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.55× (z +9.0) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.123× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 34.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 43.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.92× (z +8.9) | — |
| [[A-427 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 63.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +14.5) | — |
| [[A549 (line)]] | wt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0778× (z -9.3) ⚠ cell-cycle shift, explains ~82% of this change |
| [[AsPC-1 (line)]] | alt | 21.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +13.1) | — |
| [[HepG2_C3A (line)]] | wt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +11.2) | — |
| [[J82 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +12.3) | — |
| [[KATO III (line)]] | alt | 77.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.5) | — |
| [[LoVo (line)]] | wt | 44.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.64× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 9.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 23.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 31.3 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.00× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 30.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX8]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 | same gene group; pathway: Cellular Senescence; STRING 999; ⚠ same locus (31.5 kb, same strand: neighbours can correlate without regulation) |
| [[PIM3]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[GLIS2]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SAT2]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[HOOK2]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[IER5L]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[RPAIN]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ATF4]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MKNK2]] | +0.61 | +0.38 / +0.70 | both halves | 6e-05 |  |
| [[DBP]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[DDIT3]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[BBC3]] | +0.60 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ARRDC2]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.64 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[XRCC5]] | -0.59 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[EFTUD2]] | -0.59 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[NUP205]] | -0.58 | -0.55 / -0.58 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[NAA50]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[MAPKAP1]] | -0.58 | -0.29 / -0.69 | both halves | 2e-04 | pathway: Intracellular signaling by second messengers |
| [[EIF2S1]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[TMX3]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[STMP1]] | -0.57 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[IPO5]] | -0.56 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[XRCC6]] | -0.56 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[NUP155]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNKSR1]] | B | CNKSR1 activity raises CBX4's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without CNKSR1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[CXXC5]] | B | CXXC5 activity raises CBX4's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without CXXC5 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[CHAC1]] | B | CHAC1 activity raises CBX4's level | lines that do not express CHAC1 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without CHAC1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TERT; maybe low, not absent |
| [[ADGRG1]] | B | ADGRG1 activity raises CBX4's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without ADGRG1 | 0.046 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[NUPR1]] | B | NUPR1 activity raises CBX4's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.28× lower at baseline in the lines without NUPR1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[GPRC5C]] | B | GPRC5C activity raises CBX4's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without GPRC5C | 0.068 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[SYTL1]] | B | SYTL1 activity raises CBX4's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 1.36× lower at baseline in the lines without SYTL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[VASN]] | B | VASN activity raises CBX4's level | lines that do not express VASN (6) vs lines expressing it (44) | 1.19× lower at baseline in the lines without VASN | 0.091 | ⚠ within organs, on part of the lines; also absent: PAQR7, DBN1, C5AR1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (22.5, -3.7); signed map (-4.0, 13.4). **Vector** length 114, 32.0% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +16.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +6.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +6.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.7 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.6 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | +0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | chromobox 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:79,833,156-79,839,440 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hPC2, PC2, NBP16 |
| Gene groups (HGNC) | Chromobox family |
| Reactome | 19 pathways, smallest: SUMOylation of DNA methylation proteins; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; SUMOylation of transcription cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [O00257](https://www.uniprot.org/uniprotkb/O00257) (E3 SUMO-protein ligase CBX4):

> E3 SUMO-protein ligase that catalyzes sumoylation of target proteins by promoting the transfer of SUMO from the E2 enzyme to the substrate. Also acts as a histone reader, which specifically recognizes and binds histone H3 trimethylated at 'Lys-9' and 'Lys-27' (H3K9me3 and H3K27me3, respectively) via its chromo domain (By similarity). Catalyzes sumoylation of HNRNPK, a p53/TP53 transcriptional coactivator, hence indirectly regulates p53/TP53 transcriptional activation resulting in p21/CDKN1A …

**Summary**, from NCBI Gene [8535](https://www.ncbi.nlm.nih.gov/gene/8535):

> Enables SUMO binding activity; SUMO ligase activity; and enzyme binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in nuclear body. Part of PRC1 complex. Implicated in hepatocellular carcinoma. Biomarker of hepatocellular carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1554) · Entrez [8535](https://www.ncbi.nlm.nih.gov/gene/8535) · UniProt [O00257](https://www.uniprot.org/uniprotkb/O00257) · Ensembl [ENSG00000141582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141582)

## Data

Gene col 6555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6555); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6555]; `tensor/DDL_lfc|DDL_z.npy` [6555]; `embed/gene_vectors.npy` [6555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6555 or target_col == 6555). Every well: [[CBX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
