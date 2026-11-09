---
symbol: "CWC22"
type: "gene"
col: 8703
ensembl_id: "ENSG00000163510"
name: "CWC22 spliceosome associated protein"
location: "2q31.3"
module: 11
arm: "+"
pooled_cpm: 69.65
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CWC22

*CWC22 spliceosome associated protein* — 2q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.72× (z +21.4, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.09× (z +21.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.554× (z -23.2, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEBPZ]] (+0.79, fdr 7e-06), [[MRFAP1L1]] (+0.77, fdr 7e-06), [[LARP7]] (+0.75, fdr 7e-06); moves opposite to [[MFSD14B]] (-0.71, fdr 7e-06), [[SEC61A2]] (-0.69, fdr 7e-06), [[ABHD12]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CD163L1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.72×** | +21.4 | 0e+00 | 43/48 (A498, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.09×** | +21.1 | 0e+00 | 47/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.91×** | +20.4 | 0e+00 | 46/49 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +17.1 | 0e+00 | 41/48 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +16.1 | 0e+00 | 42/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +13.2 | 6e-38 | 42/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +12.9 | 7e-36 | 45/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +12.0 | 3e-31 | 43/48 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +11.3 | 1e-27 | 39/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +10.6 | 1e-24 | 39/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +7.0 | 1e-10 | 26/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +6.0 | 7e-08 | 26/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **1.24×** | +5.9 | 1e-07 | 26/47 (LoVo, SHP-77, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +5.7 | 5e-07 | 22/47 (LOX-IMVI, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +5.4 | 2e-06 | 22/48 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.9 | 0.003 | 17/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.018 | 11/48 (hTERT-HPNE, HT-29, …) | two highest doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.12× | +3.4 | 0.018 | 7/48 (A-427, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -23.2 | 0e+00 | 44/49 (LOX-IMVI, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.585×** | -15.3 | 0e+00 | 39/49 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.587×** | -15.2 | 0e+00 | 45/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.614×** | -13.9 | 1e-41 | 42/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.610×** | -13.6 | 7e-40 | 41/48 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.637×** | -12.9 | 6e-36 | 42/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -12.9 | 6e-36 | 34/44 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -11.1 | 1e-26 | 37/50 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.692×** | -10.5 | 6e-24 | 32/48 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.696×** | -10.3 | 3e-23 | 43/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.693×** | -9.7 | 2e-20 | 32/45 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.688×** | -5.6 | 1e-06 | 27/49 (NCI-H460, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.826×** | -5.2 | 7e-06 | 17/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.867× | -5.1 | 1e-05 | 16/48 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.840× | -5.0 | 2e-05 | 21/50 (NCI-H1573, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.883× | -4.9 | 4e-05 | 11/48 (A549, PANC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.852× | -4.6 | 2e-04 | 17/49 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.859× | -4.2 | 8e-04 | 18/49 (A-427, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.866× | -4.1 | 0.001 | 19/48 (SW 1088, SW 900, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 89.0 | 11 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +18.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -21.1) |
| [[NCI-H460 (line)]] | wt | 76.4 | 9 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +15.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 104 | 10 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.28× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -10.8) |
| [[SW480 (line)]] | alt | 77.8 | 7 (1 ⚠) | 5 | [[TAK-901 (drug)]] 5 µM 5.82× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 71.8 | 6 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.55× (z +11.1) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -12.2) |
| [[LS 180 (line)]] | wt | 85.4 | 8 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +15.9) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -9.6) |
| [[A498 (line)]] | wt | 77.3 | 5 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +21.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.56× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -16.5) |
| [[A549 (line)]] | wt | 68.1 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +18.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.03× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -15.5) |
| [[HT-29 (line)]] | alt | 63.4 | 3 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 73.4 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 65.1 | 4 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.84× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -13.2) |
| [[HOP62 (line)]] | alt | 64.7 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.00× (z +11.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.4) |
| [[LoVo (line)]] | wt | 60.7 | 5 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -9.5) |
| [[PANC-1 (line)]] | alt | 74.8 | 4 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.05× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -13.4) |
| [[A-172 (line)]] | wt | 59.2 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +15.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.69× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -14.4) |
| [[BT-474 (line)]] | alt | 47.2 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.46× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 48.9 | 2 (2 ⚠) | 3 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.86× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 0.5 µM 0.485× (z -9.7) |
| [[RKO (line)]] | wt | 87.4 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -11.2) |
| [[COLO 205 (line)]] | alt | 60.9 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 9.75× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -9.3) |
| [[Hs 766T (line)]] | wt | 46.9 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.3) |
| [[KATO III (line)]] | alt | 58.5 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.0636× (z -29.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 53.5 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.84× (z +9.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.372× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~55% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.467× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 87.5 | 2 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.98× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 91.6 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -20.2) |
| [[SNU-1 (line)]] | wt | 74.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 66.9 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -13.5) |
| [[H4 (line)]] | wt | 77.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -12.3) |
| [[HS-578T (line)]] | alt | 49.5 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +9.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 64.9 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.101× (z -11.1) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 64.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.55× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 59.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -10.2) |
| [[SW 900 (line)]] | alt | 70.6 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.4) |
| [[A-427 (line)]] | wt | 58.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.22× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 80.6 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 66.8 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 60.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 108 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 73.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -9.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -13.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 77.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 86.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +9.2) | — |
| [[J82 (line)]] | alt | 59.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.488× (z -9.4) |
| [[SW 1088 (line)]] | alt | 78.5 | 0 | 1 | — | [[Rifaximin (drug)]] 0.5 µM 0.0824× (z -9.5) |
| [[C32 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 58.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 68.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPZ]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 | STRING 462 |
| [[MRFAP1L1]] | +0.77 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[LARP7]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | STRING 476 |
| [[THUMPD3]] | +0.74 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[EPC1]] | +0.74 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[ESF1]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[PRPF38B]] | +0.73 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[GSPT2]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[SNW1]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[COIL]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.70 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14B]] | -0.71 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[SEC61A2]] | -0.69 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[ABHD12]] | -0.67 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[SETD3]] | -0.67 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[ADAM15]] | -0.61 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[DCUN1D4]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[RNF38]] | -0.61 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[COLGALT1]] | -0.60 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SRD5A1]] | -0.60 | -0.50 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD163L1]] | B | CD163L1 activity raises CWC22's level | lines that do not express CD163L1 (24) vs lines expressing it (26) | 1.14× lower at baseline in the lines without CD163L1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, ENSG00000230647, CNRIP1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CWC22's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF880]] | B | ZNF880 activity lowers CWC22's level | lines that do not express ZNF880 (22) vs lines expressing it (28) | 1.14× higher at baseline in the lines without ZNF880 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, ZNF354C |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-36.2, 6.3); signed map (-0.2, -20.5). **Vector** length 97.7, 28.5% of its response variance represented; |z| ≥ 3 in 1,472 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +17.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.1 | +21.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +16.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.5 | +3.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.4 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -13.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -10.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -11.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.4 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | +0.3 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -2.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | CWC22 spliceosome associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.3 — chr2:179,944,876-180,007,297 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1604, EIF4GL, fSAPb, NCM |
| Gene groups (HGNC) | NTC associated proteins; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex; MIF4G domain containing proteins |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCG8](https://www.uniprot.org/uniprotkb/Q9HCG8) (Pre-mRNA-splicing factor CWC22 homolog):

> Required for pre-mRNA splicing as component of the spliceosome. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable). Promotes exon-junction complex (EJC) assembly. Hinders EIF4A3 from non-specifically binding RNA and escorts it to the splicing machinery to promote EJC assembly on mature mRNAs. Through its role in EJC assembly, required for nonsense-mediated mRNA decay.

**Summary**, from NCBI Gene [57703](https://www.ncbi.nlm.nih.gov/gene/57703):

> Enables RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nuclear speck. Part of U2-type catalytic step 1 spliceosome; U2-type catalytic step 2 spliceosome; and U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29322](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29322) · Entrez [57703](https://www.ncbi.nlm.nih.gov/gene/57703) · UniProt [Q9HCG8](https://www.uniprot.org/uniprotkb/Q9HCG8) · Ensembl [ENSG00000163510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163510)

## Data

Gene col 8703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8703); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8703]; `tensor/DDL_lfc|DDL_z.npy` [8703]; `embed/gene_vectors.npy` [8703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8703 or target_col == 8703). Every well: [[CWC22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CWC22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
