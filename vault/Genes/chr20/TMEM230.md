---
symbol: "TMEM230"
type: "gene"
col: 1567
ensembl_id: "ENSG00000089063"
name: "transmembrane protein 230"
location: "20p13-p12.3"
module: 52
arm: "+"
pooled_cpm: 33.29
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# TMEM230

*transmembrane protein 230* — 20p13-p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.05× (z +13.3, q 4e-38, up in 44 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +9.8, q 3e-20, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SK-MEL-2 3.69×, PANC-1 2.37×, SNU-423 3.81×, A549 2.87×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (MIA PaCa-2 4.09×, NCI-H1792 4.83×, SNU-423 3.50×, HEC-1-A 2.72×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 3.79×, CFPAC-1 3.78×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.68×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.735× (z -8.1, q 2e-13, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.802× (z -4.1, q 0.007, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCAKD]] (+0.60, fdr 7e-06), [[TMED7-TICAM2]] (+0.59, fdr 1e-05), [[TRNT1]] (+0.58, fdr 1e-05); moves opposite to [[GPBP1]] (-0.55, fdr 3e-05), [[LEO1]] (-0.49, fdr 8e-05), [[TENT4B]] (-0.49, fdr 8e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1567.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SK-MEL-2 3.69×, PANC-1 2.37×, SNU-423 3.81×, A549 2.87×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (MIA PaCa-2 4.09×, NCI-H1792 4.83×, SNU-423 3.50×, HEC-1-A 2.72×, …; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 3.79×, CFPAC-1 3.78×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 2.68×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +13.3 | 4e-38 | 44/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +13.3 | 4e-38 | 31/35 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.8 | 3e-20 | 32/48 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +8.8 | 2e-16 | 29/40 (C32, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +7.0 | 4e-10 | 32/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +4.8 | 2e-04 | 22/48 (COLO 205, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.29×** | +4.7 | 2e-04 | 23/48 (COLO 205, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.27×** | +4.4 | 7e-04 | 20/48 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.2 | 0.002 | 0/48 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.25×** | +3.9 | 0.006 | 18/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.23×** | +3.8 | 0.006 | 10/48 (AsPC-1, KATO III, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.22×** | +3.7 | 0.011 | 11/48 (A498, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.017 | 11/48 (PANC-1, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.031 | 11/34 (HS-578T, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.073 | 16/47 (LS 180, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.088 | 12/48 (A498, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1567.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.735×** | -8.1 | 2e-13 | 31/47 (A549, HEC-1-A, …) | top dose only | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.771×** | -4.6 | 0.001 | 23/48 (NCI-H460, H4, …) | top dose only | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.802×** | -4.1 | 0.007 | 21/48 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.664×** | -4.0 | 0.009 | 16/47 (J82, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Elagolix sodium (drug)]] 0.5 µM |  | **0.822×** | -3.7 | 0.020 | 18/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.822×** | -3.7 | 0.020 | 16/48 (A498, J82, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **0.822×** | -3.7 | 0.020 | 17/48 (Hs 766T, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.815×** | -3.6 | 0.024 | 21/47 (C-33 A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.836× | -3.4 | 0.048 | 12/48 (HS-578T, SW 1088, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.722×** | -3.2 | 0.084 | 19/42 (RKO, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.730× | -3.1 | 0.11 | 15/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.843× | -3.0 | 0.12 | 10/47 (SW480, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 23.8 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.78× (z +9.7) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 29.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 39.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 22.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 6.23× (z +11.2) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 2 | — | [[Baicalin (drug)]] 0.5 µM 0.0479× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 33.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.72× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 31.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +9.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 42.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 33.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.15× (z +8.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -14.6) ⚠ toxic |
| [[H4 (line)]] | wt | 39.9 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.198× (z -9.5) |
| [[HOP62 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0682× (z -10.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -9.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 39.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.167× (z -11.2) |
| [[SW 900 (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.489× (z -8.7) ⚠ cell-cycle shift, explains ~74% of this change |
| [[A-427 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCAKD]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TMED7-TICAM2]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[TRNT1]] | +0.58 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[FUBP3]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[PSKH1]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[STX16-NPEPL1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SENP3]] | +0.56 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[TMEM138]] | +0.55 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[TM9SF3]] | +0.55 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[SZT2]] | +0.54 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[DAP]] | +0.54 | +0.43 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPBP1]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[LEO1]] | -0.49 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[TENT4B]] | -0.49 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[DECR2]] | -0.49 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[SNAPIN]] | -0.49 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[CDC5L]] | -0.48 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[TPR]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[HPF1]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[MYLIP]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[UBB]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[TCAF1]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[TCEAL1]] | -0.46 | -0.50 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.459). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (18.0, -27.8); signed map (-48.6, -0.4). **Vector** length 88.8, 18.4% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +13.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[Lopinavir (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Isocorydine (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.9 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.5 | -8.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.8 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.2 | -3.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Mozavaptan (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 230 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13-p12.3 — chr20:5,068,232-5,113,087 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC274; previously C20orf30 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A57](https://www.uniprot.org/uniprotkb/Q96A57) (Transmembrane protein 230):

> Involved in trafficking and recycling of synaptic vesicles.

**Summary**, from NCBI Gene [29058](https://www.ncbi.nlm.nih.gov/gene/29058):

> This gene encodes a multi-pass transmembrane protein that belongs to the TMEM134/TMEM230 protein family. The encoded protein localizes to secretory and recycling vesicle in the neuron and may be involved in synaptic vesicles trafficking and recycling. Mutations in this gene may be linked to familial Parkinson's disease. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:15876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15876) · Entrez [29058](https://www.ncbi.nlm.nih.gov/gene/29058) · UniProt [Q96A57](https://www.uniprot.org/uniprotkb/Q96A57) · Ensembl [ENSG00000089063](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089063)

## Data

Gene col 1567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1567); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1567]; `tensor/DDL_lfc|DDL_z.npy` [1567]; `embed/gene_vectors.npy` [1567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1567 or target_col == 1567). Every well: [[TMEM230 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM230.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
