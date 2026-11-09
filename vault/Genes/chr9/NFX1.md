---
symbol: "NFX1"
type: "gene"
col: 1454
ensembl_id: "ENSG00000086102"
name: "nuclear transcription factor, X-box binding 1"
location: "9p13.3"
module: 11
arm: "+"
pooled_cpm: 132.74
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# NFX1

*nuclear transcription factor, X-box binding 1* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +19.5, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.487× (z -22.3, q 0e+00, down in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.812× (z -9.1, q 9e-18, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (COLO 205 0.0564×, PANC-1 0.276×, NCI-H460 0.246×, RKO 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A-427 0.131×, SW480 0.346×, A498 0.255×, HEC-1-A 0.305×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.183×, Panc 03.27 0.268×, PANC-1 0.311×, KATO III 0.239×; ⚠ toxic; transcription drop); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (BT-474 0.492×); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 0.715×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (J82 0.531×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOSR1]] (+0.75, fdr 7e-06), [[CCDC174]] (+0.71, fdr 7e-06), [[TRIM4]] (+0.69, fdr 7e-06); moves opposite to [[ZDHHC20]] (-0.69, fdr 7e-06), [[FAM102B]] (-0.62, fdr 1e-05), [[MAPK9]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +19.5 | 0e+00 | 37/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +16.1 | 0e+00 | 42/48 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +12.1 | 3e-31 | 37/49 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +9.4 | 7e-19 | 34/48 (LoVo, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.22×** | +6.0 | 2e-07 | 23/48 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | 1.10× | +4.1 | 0.004 | 4/48 (Hs 766T, H4, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.12× | +3.5 | 0.030 | 9/48 (hTERT-HPNE, Hs 766T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.5 | 0.030 | 8/48 (A-427, AsPC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.039 | 6/50 (NCI-H460, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.08× | +3.4 | 0.041 | 8/48 (RKO, A-427, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.11× | +3.3 | 0.043 | 7/49 (RKO, J82, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.11× | +3.3 | 0.054 | 6/48 (SW 900, Panc 03.27, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.064 | 9/47 (LoVo, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 1.11× | +3.1 | 0.072 | 10/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | 1.10× | +3.0 | 0.093 | 1/48 (HS-578T) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1454.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (COLO 205 0.0564×, PANC-1 0.276×, NCI-H460 0.246×, RKO 0.266×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 5 lines (A-427 0.131×, SW480 0.346×, A498 0.255×, HEC-1-A 0.305×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 0.183×, Panc 03.27 0.268×, PANC-1 0.311×, KATO III 0.239×; ⚠ toxic; transcription drop); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (BT-474 0.492×); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 0.715×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (J82 0.531×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.487×** | -22.3 | 0e+00 | 41/49 (COLO 205, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.472×** | -21.6 | 0e+00 | 39/45 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -15.3 | 0e+00 | 40/44 (NCI-H460, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.709×** | -10.3 | 1e-22 | 31/47 (LoVo, SNU-423, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -9.1 | 9e-18 | 28/48 (SW480, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.779×** | -7.8 | 8e-13 | 28/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.808×** | -6.6 | 3e-09 | 28/48 (RPMI-7951, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.809×** | -6.6 | 3e-09 | 28/48 (LoVo, SK-MEL-2, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.677×** | -6.3 | 2e-08 | 30/45 (SW48, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.824×** | -6.0 | 1e-07 | 23/49 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.840× | -5.4 | 3e-06 | 21/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | 0.873× | -4.2 | 0.001 | 23/48 (HOP62, LS 180, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.961× | -4.1 | 0.002 | 0/50 | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.882× | -3.7 | 0.008 | 15/47 (BT-474, HepG2/C3A, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.891× | -3.5 | 0.021 | 6/48 (Panc 03.27, HOP62, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.868× | -3.1 | 0.052 | 12/48 (COLO 205, hTERT-HPNE, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.901× | -3.1 | 0.054 | 15/48 (A498, NCI-H2030, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.907× | -2.9 | 0.095 | 9/47 (A-172, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 251 | 17 (2 ⚠) | 4 (4 ⚠) | [[Binimetinib (drug)]] 5 µM 2.94× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -23.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 171 | 4 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +14.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.376× (z -15.5) ⚠ toxic |
| [[LS 180 (line)]] | wt | 136 | 2 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -11.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 153 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -14.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 143 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.531× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 105 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 141 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -12.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 213 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -17.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 187 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -20.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 119 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.60× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -19.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 110 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -13.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 225 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -18.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 160 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.198× (z -15.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 105 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -14.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 177 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -17.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 87.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +17.6) | — |
| [[RKO (line)]] | wt | 131 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.41× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -18.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 105 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -14.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 115 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -16.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 75.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.27× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -23.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 150 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -17.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 163 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -11.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 113 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -12.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 118 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.471× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 111 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 161 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.488× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.492× (z -9.3) |
| [[COLO 205 (line)]] | alt | 155 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0564× (z -32.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 107 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 96.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +14.6) | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -11.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 92.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.378× (z -11.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -14.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -15.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 70.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +13.8) | — |
| [[NCI-H661 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0931× (z -10.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -18.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.388× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 170 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.166× (z -8.6) |
| [[SW 1271 (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.1000× (z -11.0) ⚠ transcription drop; cell-cycle shift, explains ~61% of this change |
| [[AN3 CA (line)]] | alt | 109 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOSR1]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.71 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.69 | +0.69 / +0.64 | both halves | 7e-06 | same gene group |
| [[HELQ]] | +0.68 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[HMGXB4]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.66 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[TM9SF4]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[LINS1]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZNF146]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC20]] | -0.69 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[FAM102B]] | -0.62 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.62 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[HDAC1]] | -0.60 | -0.63 / -0.49 | both halves | 1e-05 | STRING 470 |
| [[TWSG1]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[METAP1]] | -0.57 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[WRNIP1]] | -0.57 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[STRN]] | -0.57 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[USB1]] | -0.57 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[HAGLR]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[JAM3]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CLSTN1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NFX1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises NFX1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.4, 4.7); signed map (-1.4, -15.2). **Vector** length 131, 39.7% of its response variance represented; |z| ≥ 3 in 1,206 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.5 | +16.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +19.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +12.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.0 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -9.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.2 | -10.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | -5.7 | -6.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -15.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.4 | -1.0 |
|  | [[Benproperine (phosphate) (drug)]] 5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | nuclear transcription factor, X-box binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:33,290,512-33,371,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NFX2, MGC20369, Tex42, TEG-42 |
| Gene groups (HGNC) | Ring finger proteins; PHD finger proteins; Zinc fingers NFX1-type |
| Hallmark sets | DNA_REPAIR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12986](https://www.uniprot.org/uniprotkb/Q12986) (Transcriptional repressor NF-X1):

> Binds to the X-box motif of MHC class II genes and represses their expression. May play an important role in regulating the duration of an inflammatory response by limiting the period in which MHC class II molecules are induced by interferon-gamma. Isoform 3 binds to the X-box motif of TERT promoter and represses its expression. Together with PABPC1 or PABPC4, isoform 1 acts as a coactivator for TERT expression. Mediates E2-dependent ubiquitination.

**Summary**, from NCBI Gene [4799](https://www.ncbi.nlm.nih.gov/gene/4799):

> MHC class II gene expression is controlled primarily at the transcriptional level by transcription factors that bind to the X and Y boxes, two highly conserved elements in the proximal promoter of MHC class II genes. The protein encoded by this gene is a transcriptional repressor capable of binding to the conserved X box motif of HLA-DRA and other MHC class II genes in vitro. The protein may play a role in regulating the duration of an inflammatory response by limiting the period in which class …

**Accessions** — [HGNC:7803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7803) · Entrez [4799](https://www.ncbi.nlm.nih.gov/gene/4799) · UniProt [Q12986](https://www.uniprot.org/uniprotkb/Q12986) · Ensembl [ENSG00000086102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086102)

## Data

Gene col 1454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1454); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1454]; `tensor/DDL_lfc|DDL_z.npy` [1454]; `embed/gene_vectors.npy` [1454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1454 or target_col == 1454). Every well: [[NFX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
