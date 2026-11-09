---
symbol: "TRIO"
type: "gene"
col: 454
ensembl_id: "ENSG00000038382"
name: "trio Rho guanine nucleotide exchange factor"
location: "5p15.2"
module: 116
arm: "+"
pooled_cpm: 1205.21
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# TRIO

*trio Rho guanine nucleotide exchange factor* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +12.1, q 4e-31, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.399× (z -19.3, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.403× (z -19.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DST]] (+0.71, fdr 7e-06), [[RASAL2]] (+0.67, fdr 7e-06), [[SAMD4A]] (+0.62, fdr 1e-05); moves opposite to [[ECD]] (-0.51, fdr 4e-05), [[HMCES]] (-0.48, fdr 4e-05), [[STARD3]] (-0.46, fdr 5e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HEG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +12.1 | 4e-31 | 31/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +10.7 | 4e-24 | 46/49 (A549, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.33×** | +8.4 | 1e-14 | 34/49 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.49×** | +8.3 | 1e-14 | 43/48 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.0 | 2e-13 | 32/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +6.7 | 2e-09 | 39/47 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +6.4 | 1e-08 | 40/48 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 6e-08 | 34/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.38×** | +6.1 | 9e-08 | 36/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +6.0 | 1e-07 | 35/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +5.6 | 1e-06 | 39/48 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 1e-04 | 29/48 (HT-29, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.5 | 2e-04 | 28/48 (HT-29, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +4.3 | 7e-04 | 25/48 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 7e-04 | 27/47 (HT-29, AN3 CA, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 8e-04 | 25/48 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.010 | 23/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.399×** | -19.3 | 0e+00 | 46/48 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.403×** | -19.1 | 0e+00 | 47/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.403×** | -18.4 | 0e+00 | 47/47 (NCI-H2030, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -17.9 | 0e+00 | 41/49 (NCI-H1792, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.482×** | -15.3 | 0e+00 | 46/49 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.479×** | -14.8 | 0e+00 | 41/44 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.561×** | -12.1 | 6e-32 | 42/48 (HepG2/C3A, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.603×** | -10.6 | 2e-24 | 45/48 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.588×** | -10.3 | 4e-23 | 35/45 (A-172, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.709×** | -6.9 | 2e-10 | 33/48 (NCI-H460, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.747×** | -5.9 | 2e-07 | 33/50 (A-172, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.783×** | -5.1 | 1e-05 | 36/48 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | 0.856× | -4.6 | 2e-04 | 20/48 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.863× | -4.4 | 5e-04 | 20/48 (C32, RKO, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.819×** | -4.2 | 1e-03 | 26/48 (A549, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.812×** | -4.1 | 0.002 | 30/47 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.002 | 23/49 (J82, H4, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.841× | -3.6 | 0.008 | 22/48 (NCI-H23, BT-474, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.845× | -3.5 | 0.011 | 21/48 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.026 | 17/48 (KATO III, H4, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.897× | -3.2 | 0.033 | 3/49 (Panc 03.27, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 615 | 11 (3 ⚠) | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.333× (z -21.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -20.3) |
| [[HT-29 (line)]] | alt | 506 | 13 (4 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +25.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.431× (z -13.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.490× (z -12.1) |
| [[PANC-1 (line)]] | alt | 1,875 | 2 | 14 (11 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -24.3) |
| [[CFPAC-1 (line)]] | alt | 1,029 | 7 (1 ⚠) | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +22.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -14.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 1,481 | 5 (1 ⚠) | 10 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 4.93× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -25.0) |
| [[A-172 (line)]] | wt | 2,520 | 2 | 12 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +16.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -26.9) |
| [[A549 (line)]] | wt | 953 | 7 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +31.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -24.8) |
| [[HS-578T (line)]] | alt | 2,537 | 3 | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -26.4) |
| [[MIA PaCa-2 (line)]] | alt | 906 | 6 (1 ⚠) | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +32.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -17.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 1,083 | 3 | 11 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 5.26× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -20.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 832 | 5 (1 ⚠) | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -15.9) |
| [[J82 (line)]] | alt | 2,945 | 2 | 11 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -27.8) |
| [[SK-MEL-2 (line)]] | alt | 617 | 6 (3 ⚠) | 7 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.74× (z +11.4) | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -19.1) |
| [[A498 (line)]] | wt | 1,683 | 2 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -25.3) |
| [[hTERT-HPNE (line)]] | wt | 1,341 | 1 | 11 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 1,549 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -23.7) |
| [[NCI-H1573 (line)]] | alt | 539 | 6 (2 ⚠) | 5 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.84× (z +14.5) | [[Panobinostat (drug)]] 5 µM 0.367× (z -17.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.412× (z -15.1) |
| [[NCI-H23 (line)]] | alt | 999 | 3 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +25.5) | [[Panobinostat (drug)]] 5 µM 0.343× (z -15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 1,126 | 4 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.370× (z -14.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -10.6) |
| [[SW 900 (line)]] | alt | 1,560 | 3 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.97× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -14.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.361× (z -13.7) |
| [[C-33 A (line)]] | alt | 634 | 7 (2 ⚠) | 3 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.79× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.443× (z -12.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.645× (z -9.1) |
| [[C32 (line)]] | wt | 442 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +16.3) | [[Selinexor (drug)]] 5 µM 0.637× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 1,103 | 1 | 9 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 3.76× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.272× (z -20.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.302× (z -18.4) |
| [[SNU-423 (line)]] | alt | 2,078 | 1 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -21.1) |
| [[BT-474 (line)]] | alt | 1,029 | 3 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 697 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -15.8) |
| [[Hs 766T (line)]] | wt | 1,818 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 602 | 2 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.328× (z -16.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.366× (z -15.0) |
| [[COLO 205 (line)]] | alt | 933 | 4 (2 ⚠) | 4 (3 ⚠) | [[Peretinoin (drug)]] 5 µM 2.18× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.331× (z -15.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.392× (z -12.7) |
| [[H4 (line)]] | wt | 1,308 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -14.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -14.5) |
| [[HOP62 (line)]] | alt | 2,447 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -15.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 1,546 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -29.1) |
| [[NCI-H2347 (line)]] | alt | 1,527 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -18.1) |
| [[RKO (line)]] | wt | 772 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.378× (z -12.4) |
| [[CHP-212 (line)]] | wt | 1,287 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -20.8) |
| [[AN3 CA (line)]] | alt | 912 | 6 (2 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 3.00× (z +10.6) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 2.16× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 886 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.452× (z -12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.499× (z -11.3) |
| [[A-427 (line)]] | wt | 649 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +29.9) | [[Dinaciclib (drug)]] 0.05 µM 0.484× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 527 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -13.6) |
| [[SNU-1 (line)]] | wt | 499 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.89× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.427× (z -11.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 309 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.08× (z +10.4) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.78× (z +8.5) | — |
| [[SW 1088 (line)]] | alt | 1,678 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.5) |
| [[SW 1271 (line)]] | alt | 981 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -10.4) |
| [[SW1417 (line)]] | alt | 554 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.493× (z -11.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.543× (z -10.5) |
| [[LoVo (line)]] | wt | 458 | 1 (1 ⚠) | 1 (1 ⚠) | [[Daptomycin (drug)]] 5 µM 1.61× (z +9.0) ⚠ unreliable plate only | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.524× (z -12.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 398 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.93× (z +9.6) | — |
| [[SW48 (line)]] | wt | 566 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.521× (z -8.7) |
| [[NCI-H2122 (line)]] | alt | 834 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1,093 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 951 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DST]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MITOTIC_SPINDLE |
| [[RASAL2]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[SAMD4A]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[CREB5]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC1P4]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[EGFR]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 | pathway: G alpha (q) signalling events |
| [[ETS1]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NGF]] | +0.55 | +0.46 / +0.44 | both halves | 3e-05 | pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[SMS]] | +0.55 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SYTL2]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[FER]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[RERGL]] | +0.55 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECD]] | -0.51 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[HMCES]] | -0.48 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[STARD3]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SPICE1]] | -0.45 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[SNHG30]] | -0.45 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[DUSP11]] | -0.44 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[MLEC]] | -0.43 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[ZNF684]] | -0.43 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[KHDC4]] | -0.43 | -0.42 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises TRIO's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without HEG1 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |
| [[ADAMTS16]] | B | ADAMTS16 activity raises TRIO's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without ADAMTS16 | 0.049 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5 |
| [[FGF5]] | B | FGF5 activity raises TRIO's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 1.81× lower at baseline in the lines without FGF5 | 0.050 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[TOP2A]] | B | TOP2A activity raises TRIO's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CLIP4]] | B | CLIP4 activity raises TRIO's level | lines that do not express CLIP4 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without CLIP4 | 0.073 | ⚠ within organs, on part of the lines; also absent: RTL8C, ENSG00000289526, MSN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.428). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.6, 12.5); signed map (12.2, 39.5). **Vector** length 114, 45.7% of its response variance represented; |z| ≥ 3 in 2,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.0 | +12.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +8.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +7.6 | +6.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.4 | +8.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.3 | +8.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +6.0 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.5 | -18.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.8 | -10.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.2 | -1.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | -3.1 | -3.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | +1.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.4 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | trio Rho guanine nucleotide exchange factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:14,143,342-14,532,128 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARHGEF23 |
| Gene groups (HGNC) | I-set domain containing; Dbl family Rho GEFs; TRIO family; Spectrin repeat containing; CRAL-TRIO lipid binding domain containing; SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 22 pathways, smallest: DCC mediated attractive signaling; Netrin-1 signaling; RHOJ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O75962](https://www.uniprot.org/uniprotkb/O75962) (Triple functional domain protein):

> Guanine nucleotide exchange factor (GEF) for RHOA and RAC1 GTPases. Involved in coordinating actin remodeling, which is necessary for cell migration and growth. Plays a key role in the regulation of neurite outgrowth and lamellipodia formation. In developing hippocampal neurons, limits dendrite formation, without affecting the establishment of axon polarity. Once dendrites are formed, involved in the control of synaptic function by regulating the endocytosis of AMPA-selective glutamate …

**Summary**, from NCBI Gene [7204](https://www.ncbi.nlm.nih.gov/gene/7204):

> This gene encodes a large protein that functions as a GDP to GTP exchange factor. This protein promotes the reorganization of the actin cytoskeleton, thereby playing a role in cell migration and growth. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:12303](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12303) · Entrez [7204](https://www.ncbi.nlm.nih.gov/gene/7204) · UniProt [O75962](https://www.uniprot.org/uniprotkb/O75962) · Ensembl [ENSG00000038382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038382)

## Data

Gene col 454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 454); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 454]; `tensor/DDL_lfc|DDL_z.npy` [454]; `embed/gene_vectors.npy` [454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 454 or target_col == 454). Every well: [[TRIO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
