---
symbol: "KLF11"
type: "gene"
col: 10206
ensembl_id: "ENSG00000172059"
name: "KLF transcription factor 11"
location: "2p25.1"
module: 16
arm: "+"
pooled_cpm: 14.91
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 13
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# KLF11

*KLF transcription factor 11* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.95× (z +25.1, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.443× (z -19.0, q 0e+00, down in 40 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLF6]] (+0.60, fdr 1e-05), [[RTL6]] (+0.59, fdr 1e-05), [[ZNF480]] (+0.59, fdr 1e-05); moves opposite to [[SURF4]] (-0.61, fdr 1e-05), [[MLEC]] (-0.59, fdr 1e-05), [[BTAF1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +25.1 | 0e+00 | 37/44 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +10.4 | 1e-22 | 32/45 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +10.2 | 5e-22 | 28/44 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.7 | 2e-12 | 23/45 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +7.6 | 2e-12 | 27/41 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +6.2 | 6e-08 | 21/44 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.8 | 5e-07 | 7/47 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +5.4 | 4e-06 | 15/45 (NCI-H460, C-33 A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 0.001 | 13/44 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.27×** | +3.8 | 0.007 | 4/46 (J82, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.007 | 9/46 (SW480, SHP-77, …) | top dose only | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.8 | 0.007 | 14/46 (SW480, SNU-1, …) | two highest doses | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.26×** | +3.8 | 0.007 | 9/46 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +3.8 | 0.007 | 6/46 (NCI-H460, Panc 03.27, …) | rises with dose | position effect removed |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.013 | 8/42 (PANC-1, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.013 | 3/46 (LS 180, Hs 766T, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.015 | 8/46 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.027 | 11/45 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mifepristone (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.042 | 9/44 (SNU-423, LS 180, …) | rises with dose |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.045 | 4/46 (KATO III, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.443×** | -19.0 | 0e+00 | 40/45 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -8.8 | 5e-16 | 28/44 (SK-MEL-2, SW48, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.586×** | -7.7 | 3e-12 | 27/43 (SW48, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.775×** | -6.0 | 4e-07 | 22/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.708×** | -5.7 | 1e-06 | 23/45 (LS 180, MIA PaCa-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.524×** | -5.2 | 2e-05 | 20/43 (Panc 03.27, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.734×** | -5.1 | 2e-05 | 18/45 (A-427, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.745×** | -4.9 | 8e-05 | 19/46 (LS 180, A-172, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.749×** | -4.8 | 1e-04 | 16/46 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.755×** | -4.6 | 2e-04 | 19/43 (SK-MEL-2, SW48, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.768×** | -4.4 | 7e-04 | 19/46 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.5 µM |  | **0.816×** | -3.4 | 0.034 | 7/46 (SNU-423, SW 900, …) | inconsistent across doses |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.876× | -3.1 | 0.076 | 5/45 (BT-474, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.831×** | -3.1 | 0.087 | 15/33 (A-427, NCI-H2030, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 35.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -13.5) |
| [[SW48 (line)]] | wt | 31.9 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +12.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0696× (z -12.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -9.2) |
| [[SW480 (line)]] | alt | 18.2 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -12.7) |
| [[A-427 (line)]] | wt | 37.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0972× (z -19.5) |
| [[LoVo (line)]] | wt | 14.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -13.6) |
| [[LS 180 (line)]] | wt | 26.8 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 8.91 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +15.8) | — |
| [[KATO III (line)]] | alt | 22.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +9.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -9.8) |
| [[A498 (line)]] | wt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +10.9) | — |
| [[H4 (line)]] | wt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 7.34 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -9.7) |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -9.3) |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -16.7) |
| [[NCI-H1573 (line)]] | alt | 5.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.00× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 9.17 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -8.5) |
| [[SW 900 (line)]] | alt | 7.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 7.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +12.1) | — |
| [[A549 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF6]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 | same gene group |
| [[RTL6]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ZNF480]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 | same gene group |
| [[TPPP]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[KAT5]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PRXL2C]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[SLC31A2]] | +0.57 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LGALSL]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PWWP2B]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CYP2U1]] | +0.55 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[YWHAH]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[RAPGEF1]] | +0.54 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF4]] | -0.61 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[MLEC]] | -0.59 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[BTAF1]] | -0.57 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[SNHG30]] | -0.57 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[GLUD1P3]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[SPICE1]] | -0.56 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[CRYBB2P1-1]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TM9SF3]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[P3H1]] | -0.55 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[MFN1]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SAR1A]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[MESD]] | -0.54 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KLF11's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KLF4]] | B | KLF4 activity strengthens KLF11's drug response | lines that do not express KLF4 (6) vs lines expressing it (41) | the lines without KLF4 respond 0.65× as strongly (z diff +1.32); strongest at Homoharringtonine 5 µM: 1.09x vs 3.08x (z diff +6.5) | 0.058 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.3, 15.5); signed map (6.1, -8.2). **Vector** length 94.5, 20.0% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +25.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +7.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.4 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.6 | -7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -19.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.1 | -5.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:10,042,849-10,054,836 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Tieg3, MODY7, FKLF; previously TIEG2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [O14901](https://www.uniprot.org/uniprotkb/O14901) (Krueppel-like factor 11):

> Transcription factor. Activates the epsilon- and gamma-globin gene promoters and, to a much lower degree, the beta-globin gene and represses promoters containing SP1-like binding inhibiting cell growth. Represses transcription of SMAD7 which enhances TGF-beta signaling (By similarity). Induces apoptosis (By similarity).

**Summary**, from NCBI Gene [8462](https://www.ncbi.nlm.nih.gov/gene/8462):

> The protein encoded by this gene is a zinc finger transcription factor that binds to SP1-like sequences in epsilon- and gamma-globin gene promoters. This binding inhibits cell growth and causes apoptosis. Defects in this gene are a cause of maturity-onset diabetes of the young type 7 (MODY7). Three transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Apr 2010]

**Accessions** — [HGNC:11811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11811) · Entrez [8462](https://www.ncbi.nlm.nih.gov/gene/8462) · UniProt [O14901](https://www.uniprot.org/uniprotkb/O14901) · Ensembl [ENSG00000172059](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172059)

## Data

Gene col 10206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10206); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10206]; `tensor/DDL_lfc|DDL_z.npy` [10206]; `embed/gene_vectors.npy` [10206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10206 or target_col == 10206). Every well: [[KLF11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
