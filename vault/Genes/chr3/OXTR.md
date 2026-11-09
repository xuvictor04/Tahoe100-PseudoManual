---
symbol: "OXTR"
type: "gene"
col: 11147
ensembl_id: "ENSG00000180914"
name: "oxytocin receptor"
location: "3p25.3"
module: 80
arm: "+"
pooled_cpm: 10.93
n_lines_expressing: 45
n_dd_up: 33
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 11
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# OXTR

*oxytocin receptor* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.64× (z +35.3, q 0e+00, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.689× (z -7.6, q 2e-11, down in 18 of 40 measured lines) ⚠ cell-cycle shift, explains ~41% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (PANC-1 0.180×, J82 0.351×; ⚠ cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0903×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.199×; ⚠ cell-cycle shift, explains ~39% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0811×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSUH2]] (+0.66, fdr 7e-06, ⚠ same locus), [[CUBN]] (+0.66, fdr 1e-05), [[SYNPO]] (+0.64, fdr 7e-06), [[NEPRO-AS1]] (+0.64, fdr 1e-05); moves opposite to [[SMARCD2]] (-0.64, fdr 7e-06), [[SDHAP4]] (-0.60, fdr 1e-05), [[NDUFAF7]] (-0.59, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 11 go from it, the strongest it → [[LINC01776]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.64×** | +35.3 | 0e+00 | 33/37 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.05×** | +20.3 | 0e+00 | 37/39 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.02×** | +20.1 | 0e+00 | 32/38 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.27×** | +17.1 | 0e+00 | 29/39 (SW480, NCI-H2347, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.69×** | +14.3 | 3e-44 | 29/40 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +13.2 | 7e-38 | 12/19 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.08×** | +10.6 | 3e-24 | 16/25 (J82, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.21×** | +9.9 | 2e-21 | 9/16 (J82, A-172, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +7.8 | 5e-13 | 18/39 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +6.5 | 4e-09 | 20/42 (SW480, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.55×** | +6.4 | 1e-08 | 19/42 (NCI-H2347, HOP62, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.9 | 1e-07 | 9/30 (CFPAC-1, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +5.6 | 7e-07 | 15/41 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 1e-06 | 12/38 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.45×** | +5.4 | 2e-06 | 16/38 (A-172, AsPC-1, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +4.3 | 5e-04 | 13/36 (NCI-H2347, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.001 | 14/36 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.009 | 8/38 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.60×** | +3.5 | 0.010 | 3/25 (A-172, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.023 | 7/40 (CFPAC-1, AsPC-1, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.027 | 14/39 (A-172, AsPC-1, …) | rises with dose | position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.027 | 8/34 (COLO 205, SW 900, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11147.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (PANC-1 0.180×, J82 0.351×; ⚠ cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0903×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.199×; ⚠ cell-cycle shift, explains ~39% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0811×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.689×** | -7.6 | 2e-11 | 18/40 (PANC-1, J82, …) | rises with dose | low cells (technical?) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.786× | -3.5 | 0.10 | 6/33 (SW480, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.4 | 0.10 | 7/43 (HEC-1-A, HepG2/C3A, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.790× | -3.4 | 0.10 | 10/41 (A-172, NCI-H460, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.778× | -3.3 | 0.10 | 9/36 (SW 900, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 33.0 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +24.0) | — |
| [[J82 (line)]] | alt | 118 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.58× (z +18.9) | [[Selinexor (drug)]] 5 µM 0.351× (z -9.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2347 (line)]] | alt | 24.0 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.5× (z +30.8) | — |
| [[PANC-1 (line)]] | alt | 8.09 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +22.8) | [[Selinexor (drug)]] 5 µM 0.180× (z -16.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[A549 (line)]] | wt | 8.88 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +18.6) | — |
| [[HS-578T (line)]] | alt | 7.17 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +15.8) | — |
| [[NCI-H1792 (line)]] | alt | 3.52 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 111× (z +13.2) | — |
| [[BT-474 (line)]] | alt | 14.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +18.3) | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 98.2× (z +29.6) | — |
| [[HOP62 (line)]] | alt | 5.14 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.3× (z +21.3) | — |
| [[Hs 766T (line)]] | wt | 34.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +17.2) | — |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +18.3) | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0903× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 4.48 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 61.0× (z +18.2) | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +10.4) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0811× (z -10.3) |
| [[SW480 (line)]] | alt | 4.68 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 5.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +15.3) | — |
| [[SW 900 (line)]] | alt | 4.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.3× (z +13.5) | — |
| [[A498 (line)]] | wt | 2.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 3.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 67.9× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 4.15 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0632× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 4.13 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 10.4× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 3.29 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 40.4× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -11.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSUH2]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 | ⚠ same locus (5.3 kb, same strand: neighbours can correlate without regulation) |
| [[CUBN]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | +0.64 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[NANOS3]] | +0.64 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[LINC02516]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ZNF462]] | +0.59 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[TENM3-AS1]] | +0.59 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[TIAM2]] | +0.59 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[HDAC9]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[NAV3]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ZFHX2]] | +0.59 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[DPY19L2P2]] | +0.58 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCD2]] | -0.64 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[SDHAP4]] | -0.60 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.59 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[CDADC1]] | -0.58 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[SNHG30]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[METTL9]] | -0.58 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[NFATC3]] | -0.56 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[SNX1]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[ABHD12]] | -0.56 | -0.60 / -0.43 | both halves | 3e-05 | pathway: G alpha (q) signalling events |
| [[NDUFV1]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.54 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[SHQ1]] | -0.54 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01776]] | B | OXTR activity lowers LINC01776's level | lines that do not express OXTR (5) vs lines expressing it (45) | 2.03× higher at baseline in the lines without OXTR | 0.052 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | B | OXTR activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express OXTR (5) vs lines expressing it (43) | the lines without OXTR: 0.40× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[DIO2]] | B | OXTR activity raises DIO2's level | lines that do not express OXTR (5) vs lines expressing it (45) | 3.55× lower at baseline in the lines without OXTR | 0.077 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[NANOS3]] | B | OXTR activity strengthens NANOS3's drug response | lines that do not express OXTR (5) vs lines expressing it (36) | the lines without OXTR respond 0.72× as strongly (z diff +0.79); strongest at Idarubicin (hydrochloride) 5 µM: 0.33x vs 1.76x (z diff +6.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[LPCAT3]] | B | OXTR activity lowers LPCAT3's level | lines that do not express OXTR (5) vs lines expressing it (45) | 1.81× higher at baseline in the lines without OXTR | 0.084 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[ZNF462]] | B | OXTR activity raises ZNF462's level | lines that do not express OXTR (5) vs lines expressing it (45) | 3.38× lower at baseline in the lines without OXTR | 0.087 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[ADPGK]] | B | OXTR activity raises ADPGK's level | lines that do not express OXTR (5) vs lines expressing it (45) | 1.12× lower at baseline in the lines without OXTR | 0.089 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[CUBN]] | B | OXTR activity lowers CUBN's level | lines that do not express OXTR (5) vs lines expressing it (45) | 3.31× higher at baseline in the lines without OXTR | 0.089 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent; its own permutation p |
| cells under [[Lonafarnib (drug)]] 0.05 µM | B | OXTR activity lowers the cells' numbers under Lonafarnib 0.05 µM (makes them more sensitive) | lines that do not express OXTR (5) vs lines expressing it (43) | the lines without OXTR: 1.16× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[HDAC9]] | B | OXTR activity lowers HDAC9's level | lines that do not express OXTR (5) vs lines expressing it (45) | 1.86× higher at baseline in the lines without OXTR | 0.090 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[SSUH2]] | C | OXTR activity raises SSUH2's level | lines that do not express OXTR (5) vs lines expressing it (45) | 2.20× lower at baseline in the lines without OXTR | 0.092 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.5, 15.5); signed map (27.2, 4.8). **Vector** length 82.2, 15.9% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +35.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +20.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.5 | +20.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +17.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +7.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +1.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.1 | -7.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.4 | -2.2 |
|  | [[Piroxicam (drug)]] 0.05 µM |  | -1.3 | -0.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | oxytocin receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:8,750,381-8,769,628 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OTR |
| Gene groups (HGNC) | Arginine vasopressin and oxytocin receptors |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P30559](https://www.uniprot.org/uniprotkb/P30559) (Oxytocin receptor):

> G protein-coupled receptor for oxytocin (OXT), a neuropeptide hormone released by the posterior pituitary gland that plays a key role in social behavior and other biological processes, such as milk ejection. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as phospholipase C. OXTR is mainly coupled to G(q) G proteins and mediates production of diacylglycerol (DAG) and …

**Summary**, from NCBI Gene [5021](https://www.ncbi.nlm.nih.gov/gene/5021):

> The protein encoded by this gene belongs to the G-protein coupled receptor family and acts as a receptor for oxytocin. Its activity is mediated by G proteins which activate a phosphatidylinositol-calcium second messenger system. The oxytocin-oxytocin receptor system plays an important role in the uterus during parturition. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8529) · Entrez [5021](https://www.ncbi.nlm.nih.gov/gene/5021) · UniProt [P30559](https://www.uniprot.org/uniprotkb/P30559) · Ensembl [ENSG00000180914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180914)

## Data

Gene col 11147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11147); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11147]; `tensor/DDL_lfc|DDL_z.npy` [11147]; `embed/gene_vectors.npy` [11147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11147 or target_col == 11147). Every well: [[OXTR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OXTR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
