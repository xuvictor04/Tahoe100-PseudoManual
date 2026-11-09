---
symbol: "CCDC200"
type: "gene"
col: 14076
ensembl_id: "ENSG00000236383"
name: "coiled-coil domain containing 200"
location: "17q21.31"
module: 54
arm: "-"
pooled_cpm: 11.76
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# CCDC200

*coiled-coil domain containing 200* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.18× (z +17.0, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.561× (z -4.8, q 0.001, down in 21 of 38 measured lines) ⚠ toxic. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 0.752× (z -3.5, q 0.090, down in 17 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HOP62 0.114×; ⚠ toxic); [[Sunitinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0760×; ⚠ toxic); [[Vilanterol (drug)]] 0.5 µM in 1 line (HCT15 0.0985×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEX14]] (+0.75, fdr 7e-06), [[CROCC]] (+0.72, fdr 1e-05), [[LINC00910]] (+0.69, fdr 7e-06, ⚠ same locus), [[BHLHE40-AS1]] (+0.69, fdr 7e-06); moves opposite to [[C15orf61]] (-0.77, fdr 1e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[MALSU1]] (-0.73, fdr 7e-06), [[PET117]] (-0.67, fdr 1e-04), [[POP7]] (-0.67, fdr 1e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.18×** | +17.0 | 0e+00 | 42/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.58×** | +14.4 | 1e-44 | 35/37 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.54×** | +13.9 | 1e-41 | 21/21 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.78×** | +12.2 | 5e-32 | 32/42 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.75×** | +12.1 | 2e-31 | 40/48 (HOP62, A-172, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.29×** | +11.4 | 7e-28 | 26/27 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +8.7 | 3e-16 | 32/45 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +6.3 | 3e-08 | 29/44 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.97×** | +5.7 | 9e-07 | 27/47 (A-427, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +5.1 | 2e-05 | 25/45 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.94×** | +4.8 | 1e-04 | 19/41 (PANC-1, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +4.4 | 6e-04 | 24/45 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.68×** | +4.3 | 6e-04 | 19/46 (A549, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +4.3 | 7e-04 | 20/44 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fluvoxamine (drug)]] 0.05 µM |  | **1.58×** | +3.5 | 0.015 | 14/46 (NCI-H2030, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.024 | 15/46 (SK-MEL-2, NCI-H2030, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.031 | 15/45 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Nevirapine (drug)]] 0.05 µM |  | **1.48×** | +3.0 | 0.071 | 14/45 (NCI-H2030, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.073 | 7/48 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.47×** | +3.0 | 0.074 | 6/42 (H4, SNU-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14076.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HOP62 0.114×; ⚠ toxic); [[Sunitinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0760×; ⚠ toxic); [[Vilanterol (drug)]] 0.5 µM in 1 line (HCT15 0.0985×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.561×** | -4.8 | 0.001 | 21/38 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.611×** | -4.2 | 0.007 | 21/46 (hTERT-HPNE, COLO 205, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.752×** | -3.5 | 0.090 | 17/46 (C32, LoVo, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.679× | -3.3 | 0.12 | 11/46 (A549, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.685× | -3.3 | 0.12 | 16/47 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | 0.769× | -3.2 | 0.12 | 14/47 (KATO III, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 4.63 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 9.19 | 4 (2 ⚠) | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 7.21× (z +12.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -9.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 11.3 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 18.6× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.84× (z +12.3) | — |
| [[A549 (line)]] | wt | 15.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 22.3× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +9.7) | — |
| [[LoVo (line)]] | wt | 15.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.30× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.71× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 24.1× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 5.85 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.38× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 7.03 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 17.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 16.3× (z +9.2) ⚠ toxic; transcription drop | [[Sunitinib (drug)]] 5 µM 0.0760× (z -8.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 5.96 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 6.64× (z +9.2) | — |
| [[A-427 (line)]] | wt | 24.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.37× (z +9.9) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 25.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0985× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.99× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 4.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +11.3) | — |
| [[HS-578T (line)]] | alt | 6.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.95× (z +9.1) | — |
| [[KATO III (line)]] | alt | 9.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 8.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +9.6) | — |
| [[RKO (line)]] | wt | 4.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 9.78 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0767× (z -8.6) ⚠ cell-cycle shift, explains <1% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.83× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 14.1 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 4.69× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX14]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[CROCC]] | +0.72 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[LINC00910]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 | ⚠ same locus (33.3 kb, same strand: neighbours can correlate without regulation) |
| [[BHLHE40-AS1]] | +0.69 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CLASP1-AS1]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[PITRM1]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[DDX5]] | +0.66 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[MAPRE1]] | +0.64 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[UBE2D3-AS1]] | +0.64 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[MC1R]] | +0.63 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[MPDU1]] | +0.62 | +0.69 / +0.39 | both halves | 6e-05 |  |
| [[SDCBP2-AS1]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CCNT2-AS1]] | +0.61 | +0.66 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf61]] ⚠ | -0.77 | -0.51 / -0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MALSU1]] | -0.73 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[PET117]] | -0.67 | -0.36 / -0.68 | both halves | 1e-04 |  |
| [[POP7]] | -0.67 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[LSM2]] | -0.67 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[GPATCH11]] | -0.64 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[MRPS34]] | -0.64 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[MRPL34]] | -0.63 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[ISCA2]] | -0.62 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[CCZ1]] | -0.62 | -0.73 / -0.47 | both halves | 2e-05 |  |
| [[ZNF45]] | -0.62 | -0.32 / -0.63 | both halves | 2e-04 |  |
| [[CAPN7]] | -0.60 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ATP5MJ]] | -0.60 | -0.43 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC200's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (27.6, -26.2); signed map (17.4, -1.7). **Vector** length 89.1, 18.1% of its response variance represented; |z| ≥ 3 in 1,061 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +11.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +12.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +1.9 | +1.9 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.5 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +0.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.1 |
|  | [[Saquinavir (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 200 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,216,941-43,305,397 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TMEM106A-AS1, LINC00854 |
| Matched by | ensembl_id |

UniProt [A0A1B0GVQ3](https://www.uniprot.org/uniprotkb/A0A1B0GVQ3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43658) · Entrez [100874261](https://www.ncbi.nlm.nih.gov/gene/100874261) · UniProt [A0A1B0GVQ3](https://www.uniprot.org/uniprotkb/A0A1B0GVQ3) · Ensembl [ENSG00000236383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236383)

## Data

Gene col 14076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14076); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14076]; `tensor/DDL_lfc|DDL_z.npy` [14076]; `embed/gene_vectors.npy` [14076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14076 or target_col == 14076). Every well: [[CCDC200 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC200.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
