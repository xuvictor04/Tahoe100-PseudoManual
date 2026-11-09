---
symbol: "FKBP4"
type: "gene"
col: 46
ensembl_id: "ENSG00000004478"
name: "FKBP prolyl isomerase 4"
location: "12p13.33"
module: 60
arm: "+"
pooled_cpm: 49.03
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# FKBP4

*FKBP prolyl isomerase 4* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (15 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 6.71× (z +26.0, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 0.225×, RKO 0.230×, A-427 0.399×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT7]] (+0.75, fdr 7e-06), [[STIP1]] (+0.75, fdr 7e-06), [[AHSA1]] (+0.74, fdr 7e-06); moves opposite to [[SEC22A]] (-0.61, fdr 1e-05), [[AFTPH]] (-0.60, fdr 1e-05), [[TNRC6C]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 46.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **6.71×** | +26.0 | 0e+00 | 48/48 (BT-474, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.02×** | +19.0 | 0e+00 | 47/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.72×** | +17.2 | 0e+00 | 41/43 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.78×** | +13.9 | 7e-42 | 44/47 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.60×** | +13.0 | 1e-36 | 44/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +12.9 | 3e-36 | 39/45 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +9.8 | 9e-21 | 31/48 (A-427, SW480, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.05×** | +9.8 | 1e-20 | 46/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.35×** | +9.5 | 2e-19 | 40/48 (NCI-H2347, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.9 | 4e-17 | 36/48 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.45×** | +8.8 | 5e-17 | 42/43 (SW1417, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +7.7 | 6e-13 | 38/48 (PANC-1, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.60×** | +6.4 | 7e-09 | 33/47 (HT-29, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.60×** | +6.1 | 3e-08 | 34/47 (COLO 205, A498, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **2.31×** | +6.0 | 9e-08 | 38/48 (AsPC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.84×** | +5.9 | 1e-07 | 32/48 (NCI-H2347, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.22×** | +5.7 | 5e-07 | 38/48 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **2.17×** | +5.5 | 1e-06 | 33/47 (NCI-H23, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.0 | 1e-05 | 30/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.0 | 2e-05 | 27/48 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.72×** | +3.9 | 0.003 | 24/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.024 | 20/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.030 | 18/47 (NCI-H460, HOP62, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 46.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 0.225×, RKO 0.230×, A-427 0.399×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.835× | -3.5 | 0.24 | 14/48 (A-427, LoVo, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.650× | -3.1 | 0.54 | 13/48 (RKO, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 46. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 73.2 | 9 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.65× (z +19.6) | — |
| [[A498 (line)]] | wt | 30.1 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.02× (z +16.1) | — |
| [[HOP62 (line)]] | alt | 30.7 | 7 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.4× (z +19.8) | — |
| [[NCI-H23 (line)]] | alt | 180 | 6 (3 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.85× (z +15.5) | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -20.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 53.7 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.35× (z +16.5) | — |
| [[Panc 03.27 (line)]] | alt | 84.2 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.88× (z +19.0) | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.98× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 48.2 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 15.6× (z +22.3) | — |
| [[SW480 (line)]] | alt | 60.6 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.59× (z +20.4) | — |
| [[J82 (line)]] | alt | 61.2 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.84× (z +12.0) | — |
| [[KATO III (line)]] | alt | 56.1 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.30× (z +17.1) | — |
| [[NCI-H2030 (line)]] | alt | 55.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +13.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.85× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 30.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.86× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 5.37× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 36.7 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.87× (z +15.7) | — |
| [[A-427 (line)]] | wt | 134 | 3 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 7.58× (z +18.2) | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 50.6 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.2× (z +20.6) | — |
| [[LoVo (line)]] | wt | 60.9 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.4× (z +19.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 79.3 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.65× (z +17.7) | — |
| [[SW 900 (line)]] | alt | 44.2 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.2× (z +15.4) | — |
| [[A-172 (line)]] | wt | 19.3 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.8× (z +15.9) | — |
| [[A549 (line)]] | wt | 34.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.42× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 31.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 7.65× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 81.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 16.0× (z +23.6) | — |
| [[H4 (line)]] | wt | 38.3 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.88× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 28.1 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.01× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 25.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.79× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 5.77× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.77× (z +12.2) | — |
| [[LOX-IMVI (line)]] | wt | 38.3 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.58× (z +15.4) | — |
| [[LS 180 (line)]] | wt | 44.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.77× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 29.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.68× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 28.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.24× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 25.2 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 13.2× (z +16.3) | — |
| [[COLO 205 (line)]] | alt | 29.3 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.4× (z +14.4) | — |
| [[HCT15 (line)]] | alt | 55.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.20× (z +13.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 73.3 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.72× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -17.1) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 31.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.63× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 57.0 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.48× (z +11.9) | — |
| [[C-33 A (line)]] | alt | 62.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.49× (z +14.1) | — |
| [[C32 (line)]] | wt | 21.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.0× (z +14.5) | — |
| [[HepG2_C3A (line)]] | wt | 20.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.35× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 31.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.22× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 61.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.55× (z +14.0) | — |
| [[SW 1271 (line)]] | alt | 73.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.3× (z +9.0) | — |
| [[SW48 (line)]] | wt | 62.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.60× (z +10.8) | — |
| [[AN3 CA (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 46), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT7]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[STIP1]] | +0.75 | +0.70 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_UV_RESPONSE_UP; STRING 979 |
| [[AHSA1]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | STRING 973 |
| [[CCT3]] | +0.72 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[CCT5]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[GPN1]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[NAA50]] | +0.68 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[CCT6A]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[HSPA8]] | +0.66 | +0.67 / +0.73 | both halves | 7e-06 | pathway: Attenuation phase; STRING 942 |
| [[BAG2]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 | pathway: Cellular response to heat stress |
| [[HSPD1]] | +0.65 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SERPINH1]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 | pathway: Attenuation phase |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC22A]] | -0.61 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.60 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.60 | -0.56 / -0.63 | both halves | 1e-05 | pathway: ESR-mediated signaling |
| [[CDKN2D]] | -0.60 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[NECAP1]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[RNF114]] | -0.59 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | -0.59 | -0.62 / -0.47 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[WIPF2]] | -0.58 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.58 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | -0.57 | -0.56 / -0.54 | both halves | 1e-05 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[INIP]] | -0.57 | -0.61 / -0.43 | both halves | 4e-05 |  |
| [[DENND6B]] | -0.56 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TRIM7-AS2]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[PI4KA]] | -0.55 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FKBP4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MLLT11]] | B | MLLT11 activity lowers FKBP4's level | lines that do not express MLLT11 (21) vs lines expressing it (29) | 1.54× higher at baseline in the lines without MLLT11 | 0.081 | ⚠ within organs, on part of the lines; also absent: DZIP1, ADAMTS18, KCNJ6; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.3, -12.0); signed map (-26.6, -29.9). **Vector** length 117, 38.1% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.53 to 13); *Formation of tubulin folding intermediates by CCT/TriC* (reactome, mean cos +0.56 to 5); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.6 | +26.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +13.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.7 | +9.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.5 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.4 | +9.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +13.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +3.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -3.0 | -1.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.8 | -1.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:2,794,970-2,805,423 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FKBP59, FKBP52 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; FKBP prolyl isomerase family |
| Hallmark sets | UV_RESPONSE_UP, ESTROGEN_RESPONSE_LATE, GLYCOLYSIS, ESTROGEN_RESPONSE_EARLY |
| Reactome | 14 pathways, smallest: Attenuation phase; HSF1 activation; HSF1-dependent transactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02790](https://www.uniprot.org/uniprotkb/Q02790) (Peptidyl-prolyl cis-trans isomerase FKBP4):

> Immunophilin protein with PPIase and co-chaperone activities. Component of steroid receptors heterocomplexes through interaction with heat-shock protein 90 (HSP90). May play a role in the intracellular trafficking of heterooligomeric forms of steroid hormone receptors between cytoplasm and nuclear compartments. The isomerase activity controls neuronal growth cones via regulation of TRPC1 channel opening. Also acts as a regulator of microtubule dynamics by inhibiting MAPT/TAU ability to promote …

**Summary**, from NCBI Gene [2288](https://www.ncbi.nlm.nih.gov/gene/2288):

> The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. This encoded protein is a cis-trans prolyl isomerase that binds to the immunosuppressants FK506 and rapamycin. It has high structural and functional similarity to FK506-binding protein 1A (FKBP1A), but unlike FKBP1A, this protein does not have immunosuppressant activity when complexed with FK506. It …

**Accessions** — [HGNC:3720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3720) · Entrez [2288](https://www.ncbi.nlm.nih.gov/gene/2288) · UniProt [Q02790](https://www.uniprot.org/uniprotkb/Q02790) · Ensembl [ENSG00000004478](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004478)

## Data

Gene col 46: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 46); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 46, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 46]; `tensor/DDL_lfc|DDL_z.npy` [46]; `embed/gene_vectors.npy` [46]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 46 or target_col == 46). Every well: [[FKBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
