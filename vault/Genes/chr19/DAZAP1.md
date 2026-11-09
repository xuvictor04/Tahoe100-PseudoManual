---
symbol: "DAZAP1"
type: "gene"
col: 990
ensembl_id: "ENSG00000071626"
name: "DAZ associated protein 1"
location: "19p13.3"
module: 18
arm: "+"
pooled_cpm: 69.53
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# DAZAP1

*DAZ associated protein 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.30× (z +17.0, q 0e+00, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.51× (z +8.4, q 6e-15, up in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (LoVo 4.29×, SW480 2.80×, J82 3.21×, PANC-1 2.50×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 3.11×, LoVo 3.18×, A-427 3.40×, PANC-1 2.62×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 1.83×, NCI-H23 2.11×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.613× (z -10.0, q 1e-20, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTA1]] (+0.76, fdr 7e-06), [[TBCD]] (+0.65, fdr 7e-06), [[CPSF1]] (+0.64, fdr 7e-06); moves opposite to [[SNRPB2]] (-0.63, fdr 1e-05), [[IFI27L2]] (-0.62, fdr 3e-05), [[MPLKIP]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 990.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (LoVo 4.29×, SW480 2.80×, J82 3.21×, PANC-1 2.50×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SW480 3.11×, LoVo 3.18×, A-427 3.40×, PANC-1 2.62×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 1.83×, NCI-H23 2.11×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.30×** | +17.0 | 0e+00 | 42/49 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +14.7 | 0e+00 | 40/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +8.8 | 3e-16 | 36/45 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +8.4 | 6e-15 | 39/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.2 | 1e-10 | 35/47 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +6.7 | 2e-09 | 34/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +6.4 | 9e-09 | 34/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.7 | 2e-04 | 24/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +4.3 | 0.001 | 24/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.22×** | +4.1 | 0.002 | 24/48 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.0 | 0.003 | 16/49 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.035 | 9/48 (PANC-1, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.095 | 11/47 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.16× | +3.0 | 0.10 | 18/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.613×** | -10.0 | 1e-20 | 42/48 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.639×** | -9.1 | 2e-17 | 41/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.671×** | -8.1 | 1e-13 | 39/48 (SK-MEL-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.761×** | -7.9 | 6e-13 | 31/48 (AsPC-1, HCT15, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -7.7 | 1e-12 | 37/48 (A498, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -5.7 | 1e-06 | 33/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.824×** | -5.5 | 2e-06 | 24/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -5.4 | 5e-06 | 32/48 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -5.1 | 2e-05 | 20/48 (A498, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.789×** | -4.8 | 8e-05 | 29/48 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.682×** | -4.1 | 0.002 | 24/49 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.880× | -3.7 | 0.011 | 17/49 (MIA PaCa-2, HCT15, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.839× | -3.6 | 0.016 | 17/48 (A498, A-427, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.847× | -3.4 | 0.030 | 18/49 (SNU-1, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.848× | -3.2 | 0.050 | 21/48 (CHP-212, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 82.9 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.397× (z -13.9) |
| [[A498 (line)]] | wt | 68.4 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.53× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.478× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.520× (z -8.9) |
| [[LoVo (line)]] | wt | 81.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +19.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 96.4 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.475× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 94.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.94× (z +12.6) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.181× (z -10.9) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 84.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -15.2) |
| [[CFPAC-1 (line)]] | alt | 35.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 59.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 85.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +17.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -12.5) |
| [[A-427 (line)]] | wt | 87.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +14.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 50.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.71× (z +13.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 110 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.92× (z +9.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 76.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +13.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 85.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +11.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 105 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -10.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.561× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 43.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 51.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +11.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 89.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -8.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 80.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -8.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 81.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.210× (z -9.0) |
| [[COLO 205 (line)]] | alt | 44.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 67.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 71.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.3) |
| [[KATO III (line)]] | alt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +12.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 73.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 51.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.293× (z -9.6) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 61.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 63.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTA1]] | +0.76 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[TBCD]] | +0.65 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[AKT1]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[GTPBP6]] | +0.64 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CPNE7]] | +0.63 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TCF3]] | +0.62 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[QSOX2]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FAM120A]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[UBE2G2]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SUGP2]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CPSF6]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB2]] | -0.63 | -0.56 / -0.65 | both halves | 1e-05 | same gene group |
| [[IFI27L2]] | -0.62 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[MPLKIP]] | -0.58 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[NDUFA7]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[TCEAL8]] | -0.56 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[SCAND1]] | -0.55 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[NRBF2]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[CTR9]] | -0.54 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[DCP1A]] | -0.54 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[MARCKS]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[KLHL4]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[RIPK2]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DAZAP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DAZAP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GAS6]] | B | GAS6 activity raises DAZAP1's level | lines that do not express GAS6 (8) vs lines expressing it (42) | 1.18× lower at baseline in the lines without GAS6 | 0.094 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-13.0, -27.7); signed map (-2.1, -55.5). **Vector** length 98.6, 26.3% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +4.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.2 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -3.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.7 | -4.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -7.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -5.1 |
|  | [[Thymol (drug)]] 5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DAZ associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,407,569-1,435,687 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC19907 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EP5](https://www.uniprot.org/uniprotkb/Q96EP5) (DAZ-associated protein 1):

> RNA-binding protein, which may be required during spermatogenesis.

**Summary**, from NCBI Gene [26528](https://www.ncbi.nlm.nih.gov/gene/26528):

> In mammals, the Y chromosome directs the development of the testes and plays an important role in spermatogenesis. A high percentage of infertile men have deletions that map to regions of the Y chromosome. The DAZ (deleted in azoospermia) gene cluster maps to the AZFc region of the Y chromosome and is deleted in many azoospermic and severely oligospermic men. It is thought that the DAZ gene cluster arose from the transposition, amplification, and pruning of the ancestral autosomal gene DAZL …

**Accessions** — [HGNC:2683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2683) · Entrez [26528](https://www.ncbi.nlm.nih.gov/gene/26528) · UniProt [Q96EP5](https://www.uniprot.org/uniprotkb/Q96EP5) · Ensembl [ENSG00000071626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071626)

## Data

Gene col 990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 990); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 990]; `tensor/DDL_lfc|DDL_z.npy` [990]; `embed/gene_vectors.npy` [990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 990 or target_col == 990). Every well: [[DAZAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAZAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
