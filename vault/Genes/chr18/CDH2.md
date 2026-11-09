---
symbol: "CDH2"
type: "gene"
col: 9974
ensembl_id: "ENSG00000170558"
name: "cadherin 2"
location: "18q12.1"
module: 197
arm: "+"
pooled_cpm: 78.76
n_lines_expressing: 28
n_dd_up: 27
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/197"]
generated_by: "tahoemap"
---

# CDH2

*cadherin 2* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.82× (z +21.3, q 0e+00, up in 21 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.72× (z +15.5, q 0e+00, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.720× (z -6.4, q 7e-08, down in 14 of 26 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 0.787× (z -4.6, q 7e-04, down in 11 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK6]] (+0.68, fdr 7e-06), [[THBS1]] (+0.68, fdr 7e-06), [[CRIM1]] (+0.66, fdr 7e-06); moves opposite to [[IL17RA]] (-0.60, fdr 1e-05), [[ACOX3]] (-0.58, fdr 1e-05), [[PEX16]] (-0.57, fdr 6e-05).
> It is in [[Module 197]], a single-armed module (Nervous system development).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 9 go from it, the strongest it → [[TPM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +21.3 | 0e+00 | 21/26 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.99×** | +19.3 | 0e+00 | 16/26 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.65×** | +19.3 | 0e+00 | 20/23 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +15.5 | 0e+00 | 22/26 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +15.5 | 0e+00 | 20/24 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +14.6 | 0e+00 | 17/26 (A549, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +10.6 | 2e-24 | 23/25 (NCI-H1792, SNU-423, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +10.6 | 3e-24 | 19/26 (NCI-H2347, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.53×** | +8.4 | 4e-15 | 15/26 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +8.0 | 7e-14 | 16/26 (NCI-H2347, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +7.8 | 4e-13 | 13/20 (SNU-423, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.36×** | +6.3 | 1e-08 | 13/25 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.7 | 6e-07 | 11/27 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.5 | 1e-06 | 12/26 (CFPAC-1, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +5.3 | 5e-06 | 13/26 (NCI-H1792, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.8 | 6e-05 | 13/26 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +4.6 | 1e-04 | 12/25 (HS-578T, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.5 | 2e-04 | 8/26 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 3e-04 | 11/25 (A-172, HS-578T, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.003 | 10/26 (H4, A-172, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.014 | 8/27 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.019 | 9/26 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.031 | 7/24 (A-172, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9974.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.720×** | -6.4 | 7e-08 | 14/26 (H4, HepG2/C3A, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.789×** | -4.9 | 2e-04 | 11/26 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.787×** | -4.6 | 7e-04 | 11/26 (A498, HS-578T, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.664×** | -4.4 | 0.001 | 12/26 (A498, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.878× | -3.8 | 0.019 | 8/26 (A498, H4, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.830×** | -3.6 | 0.028 | 11/26 (A498, HS-578T, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.887× | -3.4 | 0.051 | 10/26 (A-172, A498, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.851× | -3.4 | 0.051 | 10/26 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | **0.736×** | -3.3 | 0.051 | 8/23 (A-172, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.854× | -3.3 | 0.051 | 9/26 (A498, SW 1088, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.892× | -3.3 | 0.051 | 4/26 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.859× | -3.2 | 0.070 | 12/26 (A-172, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 539 | 7 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +19.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.64× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 310 | 4 (4 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.51× (z +12.9) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.522× (z -9.6) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 0.647× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 83.6 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +18.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.49× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 23.5 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +16.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.57× (z +10.7) | — |
| [[A549 (line)]] | wt | 62.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +20.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.88× (z +13.4) | — |
| [[CFPAC-1 (line)]] | alt | 35.6 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +18.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.70× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 49.1 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +17.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[HS-578T (line)]] | alt | 248 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 76.6 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +17.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[PANC-1 (line)]] | alt | 96.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +13.5) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.564× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 76.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.48× (z +11.3) | — |
| [[SHP-77 (line)]] | alt | 249 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 431 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 34.2 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.98× (z +17.5) | — |
| [[LOX-IMVI (line)]] | wt | 36.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.3) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 92.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 223 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 33.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 30.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.24× (z +11.0) | — |
| [[SW 900 (line)]] | alt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.70 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 232 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.80 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.78 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK6]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 | STRING 509 |
| [[THBS1]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 585 |
| [[CRIM1]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PLCB4]] | +0.66 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ALCAM]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 | same gene group; STRING 448 |
| [[TPM1]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[COL12A1]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CCDC50]] | +0.60 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[MYLK]] | +0.59 | +0.43 / +0.73 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[FAT1]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[AKR1B1]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MOXD1]] | +0.59 | +0.42 / +0.62 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.60 | -0.56 / -0.52 | both halves | 1e-05 | same gene group |
| [[ACOX3]] | -0.58 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[PEX16]] | -0.57 | -0.38 / -0.61 | both halves | 6e-05 |  |
| [[FBXL12]] | -0.56 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[KRBOX4]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SCNM1]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ZNF568]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CCDC32]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ATAT1]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[C19orf25]] | -0.53 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MRPL2]] | -0.52 | -0.37 / -0.49 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises CDH2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CNN3]] | B | CNN3 activity raises CDH2's level | lines that do not express CNN3 (5) vs lines expressing it (45) | 5.54× lower at baseline in the lines without CNN3 | 0.098 | ⚠ within organs, on part of the lines; also absent: SLC9A9, SLC35F1, CNN3-DT |
| [[NECTIN3]] | C | NECTIN3 activity raises CDH2's level | lines that do not express NECTIN3 (11) vs lines expressing it (39) | 6.23× lower at baseline in the lines without NECTIN3 | 0.020 | ⚠ within organs, on part of the lines; also absent: CD96, NECTIN3-AS1, GPR176; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises CDH2's level | lines that do not express POSTN (38) vs lines expressing it (12) | 7.64× lower at baseline in the lines without POSTN | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[CFAP299]] | C | CFAP299 activity raises CDH2's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 5.27× lower at baseline in the lines without CFAP299 | 0.052 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2; co-absent with the target |
| [[TPM1]] | C | TPM1 activity raises CDH2's level | lines that do not express TPM1 (3) vs lines expressing it (47) | 4.23× lower at baseline in the lines without TPM1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, SSUH2, XIRP2; maybe low, not absent; its own permutation p |
| [[MOXD1]] | C | MOXD1 activity raises CDH2's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 4.97× lower at baseline in the lines without MOXD1 | 0.090 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[SLIT2]] | C | SLIT2 activity raises CDH2's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 4.79× lower at baseline in the lines without SLIT2 | 0.099 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPM1]] | B | CDH2 activity raises TPM1's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 2.41× lower at baseline in the lines without CDH2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1 |
| [[RBFOX2]] | B | CDH2 activity raises RBFOX2's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 1.11× lower at baseline in the lines without CDH2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1 |
| [[CNN3]] | B | CDH2 activity raises CNN3's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without CDH2 | 0.080 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1 |
| [[TGFB2]] | B | CDH2 activity strengthens TGFB2's drug response | lines that do not express CDH2 (9) vs lines expressing it (25) | the lines without CDH2 respond 0.12× as strongly (z diff +3.38); strongest at Homoharringtonine 5 µM: 0.86x vs 2.30x (z diff +7.9) | 0.081 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1; target measured in part of the lines; artifact flags |
| [[SEMA3C]] | B | CDH2 activity strengthens SEMA3C's drug response | lines that do not express CDH2 (16) vs lines expressing it (25) | the lines without CDH2 respond 0.79× as strongly (z diff +1.33); strongest at Dinaciclib 0.5 µM: 1.19x vs 2.10x (z diff +4.1) | 0.081 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1; target measured in part of the lines; artifact flags |
| [[NRP2]] | B | CDH2 activity raises NRP2's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 2.89× lower at baseline in the lines without CDH2 | 0.086 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1 |
| [[SLIT2]] | C | CDH2 activity raises SLIT2's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 3.85× lower at baseline in the lines without CDH2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1; co-absent with the target |
| [[LINC00842]] | C | CDH2 activity raises LINC00842's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without CDH2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1; co-absent with the target |
| [[PEG10]] | C | CDH2 activity raises PEG10's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 4.18× lower at baseline in the lines without CDH2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 197]] — Nervous system development; 16 genes; every member is in the + arm (projection on the module's main direction 0.806). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.4, 15.2); signed map (45.9, 18.9). **Vector** length 98.7, 30.9% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +21.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +15.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +10.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.1 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.7 | -4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.5 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -4.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:27,932,879-28,177,946 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDHN, CD325; previously NCAD |
| Gene groups (HGNC) | CD molecules; Type I classical cadherins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 10 pathways, smallest: Regulation of MITF-M-dependent genes involved in extracellular matrix, focal adhesion and epithelial-to-mesenchymal transition; Myogenesis; Post-translational protein phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P19022](https://www.uniprot.org/uniprotkb/P19022) (Cadherin-2):

> Calcium-dependent cell adhesion protein; preferentially mediates homotypic cell-cell adhesion by dimerization with a CDH2 chain from another cell. Cadherins may thus contribute to the sorting of heterogeneous cell types. Acts as a regulator of neural stem cells quiescence by mediating anchorage of neural stem cells to ependymocytes in the adult subependymal zone: upon cleavage by MMP24, CDH2-mediated anchorage is affected, leading to modulate neural stem cell quiescence. Plays a role in …

**Summary**, from NCBI Gene [1000](https://www.ncbi.nlm.nih.gov/gene/1000):

> This gene encodes a classical cadherin and member of the cadherin superfamily. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein is proteolytically processed to generate a calcium-dependent cell adhesion molecule and glycoprotein. This protein plays a role in the establishment of left-right asymmetry, development of the nervous system and the formation of cartilage and bone. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:1759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1759) · Entrez [1000](https://www.ncbi.nlm.nih.gov/gene/1000) · UniProt [P19022](https://www.uniprot.org/uniprotkb/P19022) · Ensembl [ENSG00000170558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170558)

## Data

Gene col 9974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9974); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9974]; `tensor/DDL_lfc|DDL_z.npy` [9974]; `embed/gene_vectors.npy` [9974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9974 or target_col == 9974). Every well: [[CDH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
