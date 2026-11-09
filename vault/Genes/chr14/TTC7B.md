---
symbol: "TTC7B"
type: "gene"
col: 9205
ensembl_id: "ENSG00000165914"
name: "tetratricopeptide repeat domain 7B"
location: "14q32.11"
module: 36
arm: "+"
pooled_cpm: 47.67
n_lines_expressing: 41
n_dd_up: 9
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 15
direction_downstream: 7
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# TTC7B

*tetratricopeptide repeat domain 7B* — 14q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 1.39× (z +5.3, q 8e-05, up in 28 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.434× (z -19.0, q 0e+00, down in 36 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ULK2]] (+0.64, fdr 7e-06), [[FSD1L]] (+0.63, fdr 7e-06), [[HOMER2]] (+0.62, fdr 1e-05); moves opposite to [[TPCN1]] (-0.54, fdr 1e-05), [[BPNT1]] (-0.50, fdr 3e-05), [[PEX13]] (-0.49, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[WNT5B]] → it (grade B ⚠); 7 go from it, the strongest it → [[WIPF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **1.39×** | +5.3 | 8e-05 | 28/39 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.35×** | +4.7 | 8e-04 | 23/38 (NCI-H2030, SNU-423, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +4.4 | 0.002 | 20/38 (CFPAC-1, NCI-H1792, …) | two highest doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.66×** | +4.3 | 0.002 | 17/34 (SW480, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +4.3 | 0.002 | 19/39 (SW480, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.009 | 19/38 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.015 | 18/38 (NCI-H2030, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.26×** | +3.7 | 0.016 | 19/39 (CFPAC-1, NCI-H1792, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.022 | 15/39 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.25×** | +3.3 | 0.055 | 14/39 (SW480, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9205.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.434×** | -19.0 | 0e+00 | 36/39 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.449×** | -12.4 | 7e-33 | 26/39 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.504×** | -11.0 | 4e-26 | 29/39 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.512×** | -10.8 | 5e-25 | 30/39 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -10.1 | 7e-22 | 32/39 (A-172, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.540×** | -9.9 | 3e-21 | 31/39 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -9.3 | 1e-18 | 28/39 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.590×** | -8.2 | 2e-14 | 23/35 (NCI-H2030, A-172, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.398×** | -7.8 | 5e-13 | 28/39 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.715×** | -7.6 | 1e-12 | 24/39 (MIA PaCa-2, HEC-1-A, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.721×** | -7.5 | 5e-12 | 24/39 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.612×** | -6.8 | 5e-10 | 25/39 (A-172, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.647×** | -6.5 | 4e-09 | 21/37 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.665×** | -6.3 | 1e-08 | 25/38 (MIA PaCa-2, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.708×** | -5.6 | 9e-07 | 21/39 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.698×** | -5.6 | 9e-07 | 26/39 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -4.8 | 5e-05 | 21/39 (J82, A-172, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.749×** | -4.7 | 9e-05 | 18/39 (HOP62, A-172, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.633×** | -3.9 | 0.003 | 19/39 (NCI-H23, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.806×** | -3.5 | 0.012 | 14/39 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **0.818×** | -3.1 | 0.040 | 13/39 (HS-578T, A549, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.873× | -3.1 | 0.042 | 13/39 (A498, HS-578T, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.704×** | -2.9 | 0.062 | 12/39 (LOX-IMVI, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.6 | 0 | 15 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -13.2) |
| [[A-172 (line)]] | wt | 127 | 0 | 13 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -19.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -18.8) |
| [[MIA PaCa-2 (line)]] | alt | 89.8 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -15.4) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -11.0) |
| [[J82 (line)]] | alt | 60.4 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 74.9 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 197 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -20.7) |
| [[HEC-1-A (line)]] | alt | 61.1 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -14.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.3) |
| [[A549 (line)]] | wt | 65.6 | 0 | 7 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.215× (z -13.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 57.7 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -16.0) |
| [[PANC-1 (line)]] | alt | 44.2 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.218× (z -15.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.2) |
| [[A-427 (line)]] | wt | 97.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[HS-578T (line)]] | alt | 41.0 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -13.6) |
| [[LoVo (line)]] | wt | 72.6 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.5) ⚠ cell-cycle shift, explains ~78% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.253× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.7) |
| [[SNU-1 (line)]] | wt | 93.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.1) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.8) |
| [[SNU-423 (line)]] | alt | 53.5 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -12.9) |
| [[AN3 CA (line)]] | alt | 83.7 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0556× (z -13.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[C-33 A (line)]] | alt | 60.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 65.4 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -13.4) |
| [[C32 (line)]] | wt | 58.0 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -9.6) |
| [[BT-474 (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[CHP-212 (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.129× (z -9.1) ⚠ toxic |
| [[HOP62 (line)]] | alt | 45.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -12.1) |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 46.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -9.9) |
| [[SW 1271 (line)]] | alt | 77.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -8.9) |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -8.7) |
| [[SW480 (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.4) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[A498 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.15 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.40 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ULK2]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[FSD1L]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[HOMER2]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CPNE2]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MVB12B]] | +0.60 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[RANBP17]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CROCCP3-1]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[EXOC2]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[MPP3]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SNX24]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[TTC28]] | +0.54 | +0.50 / +0.53 | both halves | 1e-05 | same gene group |
| [[PTPN9]] | +0.54 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPCN1]] | -0.54 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[BPNT1]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PEX13]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ATOSA]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[GPRC5C]] | -0.49 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[PLAG1]] | -0.49 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[EFNA1]] | -0.49 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[CDKN1B]] | -0.48 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[FAAH2]] | -0.47 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TBC1D8B]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[BCL6]] | -0.46 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[GRAMD2B]] | -0.46 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 9, C 6. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT5B]] | B | WNT5B activity raises TTC7B's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 3.66× lower at baseline in the lines without WNT5B | 7e-04 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[GNAZ]] | B | GNAZ activity raises TTC7B's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 2.88× lower at baseline in the lines without GNAZ | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[FAAH2]] | B | FAAH2 activity weakens TTC7B's drug response | lines that do not express FAAH2 (25) vs lines expressing it (14) | the lines without FAAH2 respond 2.23× as strongly (z diff -3.05); strongest at Homoharringtonine 5 µM: 0.64x vs 0.93x (z diff -4.1) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CHD5]] | B | CHD5 activity raises TTC7B's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without CHD5 | 0.030 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises TTC7B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WNT5B]] | B | WNT5B activity strengthens TTC7B's drug response | lines that do not express WNT5B (13) vs lines expressing it (26) | the lines without WNT5B respond 0.40× as strongly (z diff +3.67); strongest at Panobinostat 5 µM: 0.84x vs 0.43x (z diff +5.5) | 0.049 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1; target measured in part of the lines; artifact flags |
| [[DOCK3]] | B | DOCK3 activity raises TTC7B's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 2.45× lower at baseline in the lines without DOCK3 | 0.074 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[FAAH2]] | B | FAAH2 activity lowers TTC7B's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.43× higher at baseline in the lines without FAAH2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers TTC7B's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM124A]] | C | FAM124A activity raises TTC7B's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 4.72× lower at baseline in the lines without FAM124A | 0.002 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |
| [[RASSF8]] | C | RASSF8 activity raises TTC7B's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 4.09× lower at baseline in the lines without RASSF8 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1; co-absent with the target |
| [[RILPL1]] | C | RILPL1's natural level strengthens TTC7B's drug response | RILPL1's natural level across 39 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.56; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WIPF1]] | B | TTC7B activity raises WIPF1's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 6.07× lower at baseline in the lines without TTC7B | 0.068 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF |
| [[PCOLCE2]] | B | TTC7B activity raises PCOLCE2's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 3.75× lower at baseline in the lines without TTC7B | 0.077 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF |
| [[ST3GAL3]] | B | TTC7B activity raises ST3GAL3's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 2.49× lower at baseline in the lines without TTC7B | 0.087 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF |
| [[RASSF8]] | C | TTC7B activity raises RASSF8's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 5.51× lower at baseline in the lines without TTC7B | 0.008 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF; co-absent with the target |
| [[FAM124A]] | C | TTC7B activity raises FAM124A's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 2.83× lower at baseline in the lines without TTC7B | 0.037 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF; co-absent with the target |
| [[MYO5A]] | C | TTC7B activity raises MYO5A's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 3.67× lower at baseline in the lines without TTC7B | 0.053 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF; co-absent with the target |
| [[KHDC1-AS1]] | C | TTC7B activity raises KHDC1-AS1's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 3.26× lower at baseline in the lines without TTC7B | 0.082 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF; co-absent with the target |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (17.9, -12.8); signed map (-8.4, 25.1). **Vector** length 113, 33.4% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +6.2 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.6 | +5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | +4.9 | +3.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | +4.6 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +4.6 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.5 | -7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -10.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.0 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -9.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.3 | -5.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 7B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11 — chr14:90,524,564-90,816,479 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TTC7L1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; PI4KA lipid kinase complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TV6](https://www.uniprot.org/uniprotkb/Q86TV6) (Tetratricopeptide repeat protein 7B):

> Component of a complex required to localize phosphatidylinositol 4-kinase (PI4K) to the plasma membrane. The complex acts as a regulator of phosphatidylinositol 4-phosphate (PtdIns(4)P) synthesis. In the complex, plays a central role in bridging PI4KA to EFR3B and HYCC1, via direct interactions.

**Summary**, from NCBI Gene [145567](https://www.ncbi.nlm.nih.gov/gene/145567):

> Involved in phosphatidylinositol phosphate biosynthetic process and protein localization to plasma membrane. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19858) · Entrez [145567](https://www.ncbi.nlm.nih.gov/gene/145567) · UniProt [Q86TV6](https://www.uniprot.org/uniprotkb/Q86TV6) · Ensembl [ENSG00000165914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165914)

## Data

Gene col 9205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9205); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9205]; `tensor/DDL_lfc|DDL_z.npy` [9205]; `embed/gene_vectors.npy` [9205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9205 or target_col == 9205). Every well: [[TTC7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
