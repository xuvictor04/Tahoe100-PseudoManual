---
symbol: "BCL9L"
type: "gene"
col: 11786
ensembl_id: "ENSG00000186174"
name: "BCL9 like"
location: "11q23.3"
module: 14
arm: "+"
pooled_cpm: 83.14
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BCL9L

*BCL9 like* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.57× (z +20.5, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.313× (z -19.0, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H12A]] (+0.70, fdr 7e-06), [[FOSL2]] (+0.66, fdr 7e-06), [[SYNPO]] (+0.66, fdr 7e-06); moves opposite to [[SCAI]] (-0.57, fdr 1e-05), [[COG5]] (-0.55, fdr 1e-05), [[FAM20B]] (-0.54, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SAMSN1]] → it (grade B ⚠); 4 go from it, the strongest it → [[MYOF]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.57×** | +20.5 | 0e+00 | 41/45 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.39×** | +13.8 | 1e-40 | 41/45 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +9.8 | 2e-20 | 32/44 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.70×** | +8.5 | 2e-15 | 34/46 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 1e-04 | 22/45 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +4.8 | 1e-04 | 23/45 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.21× | +3.2 | 0.11 | 19/45 (HOP62, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | 1.20× | +3.0 | 0.16 | 18/45 (hTERT-HPNE, HOP62, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.16 | 16/45 (HOP62, hTERT-HPNE, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.313×** | -19.0 | 0e+00 | 45/45 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.345×** | -17.4 | 0e+00 | 44/45 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.493×** | -11.6 | 1e-28 | 41/45 (NCI-H1573, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.557×** | -9.0 | 3e-17 | 40/45 (SW 900, A498, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.631×** | -7.5 | 6e-12 | 37/45 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.634×** | -7.4 | 1e-11 | 31/46 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.645×** | -7.2 | 7e-11 | 31/45 (SW 900, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.645×** | -6.9 | 4e-10 | 27/40 (A-427, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.668×** | -6.3 | 2e-08 | 31/44 (CFPAC-1, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.500×** | -5.9 | 2e-07 | 29/42 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.773×** | -3.9 | 0.005 | 21/41 (CHP-212, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.019 | 17/45 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.849× | -3.5 | 0.019 | 21/46 (HEC-1-A, HT-29, …) | top dose only | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.027 | 21/44 (A498, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.818×** | -3.3 | 0.040 | 17/46 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.042 | 18/45 (CFPAC-1, J82, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.760×** | -3.2 | 0.042 | 20/44 (C-33 A, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 5 µM |  | 0.857× | -3.2 | 0.042 | 8/46 (NCI-H2347, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.829×** | -3.0 | 0.062 | 14/45 (CHP-212, SW 1088, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.829×** | -3.0 | 0.062 | 19/46 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 0.876× | -3.0 | 0.078 | 8/45 (J82, hTERT-HPNE, …) | all doses, flat |  |
| [[Hydroxyurea (drug)]] 0.5 µM |  | 0.835× | -2.9 | 0.081 | 16/44 (H4, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 93.6 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.203× (z -13.7) |
| [[CFPAC-1 (line)]] | alt | 160 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +26.5) | [[Panobinostat (drug)]] 5 µM 0.244× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 103 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -19.4) |
| [[HS-578T (line)]] | alt | 86.3 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.243× (z -13.1) |
| [[PANC-1 (line)]] | alt | 93.4 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +25.9) | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -12.4) |
| [[A-172 (line)]] | wt | 59.3 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -16.3) |
| [[A498 (line)]] | wt | 61.5 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.348× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 144 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +15.0) | [[Panobinostat (drug)]] 5 µM 0.217× (z -14.2) |
| [[HT-29 (line)]] | alt | 121 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.194× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 176 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -23.3) |
| [[SNU-423 (line)]] | alt | 113 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -13.3) |
| [[A-427 (line)]] | wt | 51.6 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.318× (z -10.0) |
| [[HOP62 (line)]] | alt | 52.0 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.283× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 66.2 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.3) | [[Ixazomib citrate (drug)]] 5 µM 0.344× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 116 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +18.4) | [[Bortezomib (drug)]] 5 µM 0.152× (z -11.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 105 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -13.0) |
| [[J82 (line)]] | alt | 56.6 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +18.9) | [[Panobinostat (drug)]] 5 µM 0.359× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 61.0 | 1 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.58× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.267× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 70.1 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.243× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 116 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.456× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 54.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -13.5) |
| [[BT-474 (line)]] | alt | 111 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.156× (z -16.5) |
| [[C32 (line)]] | wt | 106 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.303× (z -11.5) |
| [[CHP-212 (line)]] | wt | 83.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.189× (z -8.6) |
| [[COLO 205 (line)]] | alt | 57.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.236× (z -10.9) |
| [[Hs 766T (line)]] | wt | 141 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.236× (z -13.6) |
| [[hTERT-HPNE (line)]] | wt | 58.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -9.0) |
| [[LS 180 (line)]] | wt | 53.6 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.313× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 99.5 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 4.26× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -8.6) |
| [[SW48 (line)]] | wt | 98.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 45.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +20.8) | — |
| [[KATO III (line)]] | alt | 121 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.5) | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0802× (z -9.2) |
| [[SW480 (line)]] | alt | 89.3 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 3.71× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -9.2) |
| [[LoVo (line)]] | wt | 41.1 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.23× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 63.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.6) | — |
| [[NCI-H661 (line)]] | alt | 59.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -12.4) |
| [[SW1417 (line)]] | alt | 145 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 93.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H12A]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[FOSL2]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SYNPO]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[BCL3]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[TRIM47]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CAV1]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 | pathway: Signaling by WNT |
| [[BHLHE41]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CSF1]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[FSTL3]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TNS2]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SLC39A1]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[TNKS1BP1]] | +0.61 | +0.68 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAI]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[COG5]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[FAM20B]] | -0.54 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[UQCRH]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[DIP2A]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ANKRD39]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PCBD1]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[DYM]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TRMT2B]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[WRN]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMSN1]] | B | SAMSN1 activity raises BCL9L's level | lines that do not express SAMSN1 (6) vs lines expressing it (44) | 1.82× lower at baseline in the lines without SAMSN1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SYTL2, GNA14, ENSG00000235609; maybe low, not absent |
| [[MYOF]] | B | MYOF activity raises BCL9L's level | lines that do not express MYOF (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without MYOF | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYOF]] | C | BCL9L activity raises MYOF's level | lines that do not express BCL9L (3) vs lines expressing it (47) | 3.26× lower at baseline in the lines without BCL9L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[WRN]] | C | BCL9L activity lowers WRN's level | lines that do not express BCL9L (3) vs lines expressing it (47) | 2.05× higher at baseline in the lines without BCL9L | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent |
| [[ZFAND5]] | C | BCL9L activity raises ZFAND5's level | lines that do not express BCL9L (3) vs lines expressing it (47) | 1.36× lower at baseline in the lines without BCL9L | 0.077 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent |
| [[USP43]] | C | BCL9L activity raises USP43's level | lines that do not express BCL9L (3) vs lines expressing it (47) | 2.95× lower at baseline in the lines without BCL9L | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, 8.4); signed map (28.9, 8.2). **Vector** length 139, 45.4% of its response variance represented; |z| ≥ 3 in 1,285 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.9 | +20.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.7 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.6 | +2.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.5 | +2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +3.4 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -8.1 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.8 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.6 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -17.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.6 | -5.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.6 | -1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.6 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | BCL9 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,893,875-118,925,926 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DLNB11, B9L, Bcl9-2 |
| Gene groups (HGNC) | Wnt enhanceosome complex |
| Reactome | 4 pathways, smallest: Deactivation of the beta-catenin transactivating complex; Formation of the beta-catenin:TCF transactivating complex; TCF dependent signaling in response to WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UU0](https://www.uniprot.org/uniprotkb/Q86UU0) (B-cell CLL/lymphoma 9-like protein):

> Transcriptional regulator that acts as an activator. Promotes beta-catenin transcriptional activity. Plays a role in tumorigenesis. Enhances the neoplastic transforming activity of CTNNB1 (By similarity).

**Summary**, from NCBI Gene [283149](https://www.ncbi.nlm.nih.gov/gene/283149):

> Enables beta-catenin binding activity. Involved in several processes, including negative regulation of transforming growth factor beta receptor signaling pathway; positive regulation of epithelial to mesenchymal transition; and positive regulation of transcription by RNA polymerase II. Located in fibrillar center and nucleoplasm. Part of beta-catenin-TCF complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23688) · Entrez [283149](https://www.ncbi.nlm.nih.gov/gene/283149) · UniProt [Q86UU0](https://www.uniprot.org/uniprotkb/Q86UU0) · Ensembl [ENSG00000186174](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186174)

## Data

Gene col 11786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11786); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11786]; `tensor/DDL_lfc|DDL_z.npy` [11786]; `embed/gene_vectors.npy` [11786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11786 or target_col == 11786). Every well: [[BCL9L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL9L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
