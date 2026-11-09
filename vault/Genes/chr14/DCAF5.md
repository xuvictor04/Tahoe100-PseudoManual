---
symbol: "DCAF5"
type: "gene"
col: 6363
ensembl_id: "ENSG00000139990"
name: "DDB1 and CUL4 associated factor 5"
location: "14q24.1"
module: 169
arm: "+"
pooled_cpm: 94.99
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/169"]
generated_by: "tahoemap"
---

# DCAF5

*DDB1 and CUL4 associated factor 5* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 4.43× (z +19.6, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.445× (z -19.6, q 0e+00, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.513× (z -16.8, q 0e+00, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C16orf87]] (+0.73, fdr 7e-06), [[SECISBP2L]] (+0.68, fdr 7e-06), [[TBC1D12]] (+0.68, fdr 7e-06); moves opposite to [[NUP188]] (-0.60, fdr 1e-05), [[RNF123]] (-0.60, fdr 1e-05), [[THOC6]] (-0.60, fdr 7e-06).
> It is in [[Module 169]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.43×** | +19.6 | 0e+00 | 48/49 (SW480, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +14.0 | 4e-42 | 31/49 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.26×** | +10.7 | 1e-24 | 40/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.14× | +4.6 | 5e-04 | 8/48 (A498, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.010 | 20/47 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.10× | +3.5 | 0.041 | 2/48 (NCI-H2030, SNU-1) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.15× | +3.5 | 0.041 | 13/48 (SW48, LoVo, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.10× | +3.4 | 0.056 | 6/48 (RKO, HEC-1-A, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.14× | +3.2 | 0.10 | 8/49 (NCI-H1792, A-172, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -19.6 | 0e+00 | 38/44 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.513×** | -16.8 | 0e+00 | 41/48 (SW480, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.521×** | -16.4 | 0e+00 | 44/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.504×** | -16.0 | 0e+00 | 40/45 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -15.0 | 0e+00 | 42/48 (SW480, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.771×** | -6.3 | 3e-08 | 25/47 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.780×** | -6.2 | 4e-08 | 27/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.849× | -5.8 | 4e-07 | 21/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -5.4 | 4e-06 | 22/48 (CFPAC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.820×** | -5.0 | 3e-05 | 22/48 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | 0.838× | -4.4 | 5e-04 | 22/48 (NCI-H2347, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.888× | -4.2 | 0.001 | 12/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.853× | -4.0 | 0.003 | 22/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.897× | -3.9 | 0.005 | 4/48 (C-33 A, HS-578T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.858× | -3.7 | 0.009 | 17/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.016 | 18/47 (SHP-77, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.822×** | -3.5 | 0.016 | 15/48 (HOP62, C-33 A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 217 | 0 | 14 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.357× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 184 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -14.2) |
| [[SW480 (line)]] | alt | 98.6 | 3 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.05× (z +20.1) | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 122 | 4 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.60× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.444× (z -9.5) |
| [[HOP62 (line)]] | alt | 101 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.443× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 142 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.61× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.443× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 116 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.293× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -10.1) |
| [[SW 900 (line)]] | alt | 144 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.43× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.445× (z -10.1) |
| [[C32 (line)]] | wt | 103 | 1 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 4.72× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 83.9 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -14.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 83.0 | 2 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.82× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.288× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.460× (z -9.0) |
| [[SW1417 (line)]] | alt | 95.3 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.473× (z -8.7) |
| [[SW48 (line)]] | wt | 116 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.56× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -16.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 87.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.351× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.497× (z -9.4) |
| [[BT-474 (line)]] | alt | 128 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.54× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.384× (z -11.5) |
| [[KATO III (line)]] | alt | 82.5 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.42× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.345× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 84.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 76.2 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 91.3 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.60× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.422× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 96.6 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -14.7) |
| [[LoVo (line)]] | wt | 67.5 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 91.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 198 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.04× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 108 | 1 | 2 | [[Salicylic acid (drug)]] 0.5 µM 2.29× (z +10.1) | [[Oxaprozin (drug)]] 5 µM 0.348× (z -12.4) |
| [[A-172 (line)]] | wt | 67.5 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -9.7) |
| [[A-427 (line)]] | wt | 45.7 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.36× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 79.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.61× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -16.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 88.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 16.2× (z +13.5) | — |
| [[H4 (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.375× (z -9.0) |
| [[HCT15 (line)]] | alt | 135 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.430× (z -9.5) |
| [[HT-29 (line)]] | alt | 50.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.07× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 98.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.43× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.408× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 75.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.93× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -15.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 45.3 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.36× (z +11.6) | — |
| [[RKO (line)]] | wt | 97.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.19× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 77.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 94.7 | 0 | 2 | — | [[Mozavaptan (drug)]] 0.5 µM 0.0817× (z -10.1) |
| [[A498 (line)]] | wt | 66.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -10.1) |
| [[AN3 CA (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0610× (z -19.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.409× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 78.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 66.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 65.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -9.9) |
| [[CHP-212 (line)]] | wt | 93.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 66.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 94.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf87]] | +0.73 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SECISBP2L]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[TBC1D12]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[ARL6IP5]] | +0.68 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[CWC15]] | +0.67 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[RELCH]] | +0.66 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[CDK7]] | +0.65 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[CCDC115]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[ASB7]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 | pathway: Neddylation |
| [[VPS37D]] | +0.65 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[ARID4B]] | +0.64 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[KLHDC10]] | +0.63 | +0.66 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.60 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[RNF123]] | -0.60 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[THOC6]] | -0.60 | -0.59 / -0.62 | both halves | 7e-06 | same gene group |
| [[IPO9]] | -0.59 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[PANK3]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.58 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[REXO1]] | -0.58 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.58 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[SACS]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.57 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[RANGAP1]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ELK4]] | -0.56 | -0.66 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DCAF5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 169]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.1, -19.9); signed map (-24.2, -4.4). **Vector** length 134, 41.8% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +14.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.1 | +19.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.4 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +10.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.7 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.3 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -16.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.3 | -2.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:69,050,881-69,153,150 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCRP2, D14S1461E, BCRG2, KIAA1824; previously WDR22 |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JK2](https://www.uniprot.org/uniprotkb/Q96JK2) (DDB1- and CUL4-associated factor 5):

> Is a substrate receptor for the CUL4-DDB1 E3 ubiquitin-protein ligase complex (CRL4). The complex CRL4-DCAF5 is involved in the ubiquitination of a set of methylated non-histone proteins, including SOX2, DNMT1 and E2F1.

**Summary**, from NCBI Gene [8816](https://www.ncbi.nlm.nih.gov/gene/8816):

> Predicted to be involved in negative regulation of fatty acid biosynthetic process. Part of Cul4-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20224) · Entrez [8816](https://www.ncbi.nlm.nih.gov/gene/8816) · UniProt [Q96JK2](https://www.uniprot.org/uniprotkb/Q96JK2) · Ensembl [ENSG00000139990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139990)

## Data

Gene col 6363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6363); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6363]; `tensor/DDL_lfc|DDL_z.npy` [6363]; `embed/gene_vectors.npy` [6363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6363 or target_col == 6363). Every well: [[DCAF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
