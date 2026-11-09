---
symbol: "TSPAN5"
type: "gene"
col: 9699
ensembl_id: "ENSG00000168785"
name: "tetraspanin 5"
location: "4q23"
module: 84
arm: "+"
pooled_cpm: 118.99
n_lines_expressing: 41
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 11
direction_downstream: 10
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# TSPAN5

*tetraspanin 5* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.45× (z +8.0, q 1e-12, up in 26 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.483× (z -14.9, q 0e+00, down in 30 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.734× (z -9.4, q 2e-18, down in 20 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A10]] (+0.55, fdr 1e-04), [[DLC1]] (+0.53, fdr 4e-05), [[AMOTL1]] (+0.52, fdr 4e-05); moves opposite to [[RNF14]] (-0.49, fdr 1e-04), [[MED24]] (-0.48, fdr 9e-05), [[SBDSP1]] (-0.47, fdr 5e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[PKIA]] → it (grade B ⚠); 10 go from it, the strongest it → [[RGS17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +8.0 | 1e-12 | 26/39 (LoVo, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +6.7 | 5e-09 | 31/40 (LoVo, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +5.0 | 1e-04 | 23/39 (LoVo, A-427, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.8 | 2e-04 | 16/39 (LoVo, SW1417, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.013 | 20/39 (BT-474, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.049 | 20/40 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.049 | 16/39 (LoVo, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +3.4 | 0.049 | 18/38 (LS 180, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.081 | 17/40 (LoVo, RKO, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +3.1 | 0.12 | 15/39 (LS 180, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -14.9 | 0e+00 | 30/33 (C-33 A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.505×** | -14.6 | 0e+00 | 33/40 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.734×** | -9.4 | 2e-18 | 20/39 (RKO, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.635×** | -9.0 | 3e-17 | 25/36 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.709×** | -7.4 | 2e-11 | 29/39 (CFPAC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -7.2 | 5e-11 | 26/38 (HT-29, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.726×** | -6.6 | 4e-09 | 24/39 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.741×** | -6.4 | 1e-08 | 23/39 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.745×** | -6.3 | 2e-08 | 23/39 (COLO 205, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.815×** | -6.2 | 3e-08 | 21/39 (NCI-H2347, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -5.6 | 1e-06 | 24/39 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.780×** | -5.1 | 1e-05 | 20/38 (COLO 205, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.801×** | -4.7 | 9e-05 | 20/39 (A-172, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.809×** | -4.5 | 2e-04 | 19/39 (A-427, SNU-1, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.816×** | -4.3 | 5e-04 | 19/39 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.822×** | -4.2 | 1e-03 | 20/39 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.828×** | -4.0 | 0.002 | 19/39 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.847× | -3.6 | 0.010 | 15/40 (HS-578T, J82, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.876× | -3.4 | 0.019 | 11/39 (J82, HS-578T, …) | two highest doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.856× | -3.3 | 0.019 | 16/39 (SW480, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.856× | -3.3 | 0.019 | 12/39 (HOP62, SW 1088, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.878× | -3.2 | 0.025 | 11/40 (J82, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.866× | -3.0 | 0.060 | 15/39 (J82, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 80.2 | 6 (2 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.376× (z -11.4) |
| [[A-427 (line)]] | wt | 197 | 3 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.57× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -21.3) |
| [[HT-29 (line)]] | alt | 189 | 0 | 9 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.273× (z -14.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.447× (z -9.5) |
| [[J82 (line)]] | alt | 95.9 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -20.7) |
| [[RKO (line)]] | wt | 67.2 | 1 | 7 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.06× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -22.2) |
| [[HOP62 (line)]] | alt | 278 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.387× (z -11.3) |
| [[PANC-1 (line)]] | alt | 233 | 3 (2 ⚠) | 4 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 1.91× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.532× (z -14.2) |
| [[C-33 A (line)]] | alt | 137 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0587× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -14.2) |
| [[COLO 205 (line)]] | alt | 162 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.395× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 140 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.14× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.460× (z -13.3) |
| [[SW480 (line)]] | alt | 168 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.393× (z -9.8) |
| [[H4 (line)]] | wt | 120 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.301× (z -10.2) |
| [[LS 180 (line)]] | wt | 184 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.454× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 91.3 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.303× (z -12.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.432× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 139 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.308× (z -12.8) |
| [[BT-474 (line)]] | alt | 203 | 1 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 6.52× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.558× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 151 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.7) |
| [[A-172 (line)]] | wt | 120 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.1) |
| [[A498 (line)]] | wt | 128 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.517× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 136 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 185 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 44.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.5) | — |
| [[CHP-212 (line)]] | wt | 71.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -10.4) |
| [[HCT15 (line)]] | alt | 75.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.6) |
| [[Hs 766T (line)]] | wt | 124 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 159 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 6.30× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 235 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 55.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.352× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.379× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.342× (z -13.0) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SW48 (line)]] | wt | 70.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 74.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -21.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 52.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.289× (z -8.5) |
| [[SNU-423 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0896× (z -10.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -12.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 52.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.95× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 172 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 97.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A10]] | +0.55 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[DLC1]] | +0.53 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[AMOTL1]] | +0.52 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[TNIK]] | +0.51 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[MAGI1]] | +0.51 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[SH3GL3]] | +0.51 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[DPF3]] | +0.51 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[CAMK1D]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[MAMLD1]] | +0.50 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[FAM117B]] | +0.50 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[SNX25]] | +0.50 | +0.44 / +0.44 | both halves | 3e-05 | STRING 420 |
| [[GALNT18]] | +0.50 | +0.53 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF14]] | -0.49 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[MED24]] | -0.48 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[SBDSP1]] | -0.47 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SLC3A2]] | -0.47 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[FBXW4]] | -0.47 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[CIZ1]] | -0.46 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[EIF2D]] | -0.46 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[VRK2]] | -0.46 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[PARP3]] | -0.46 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[DDX59]] | -0.45 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[CDC23]] | -0.45 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[SRP14-DT]] | -0.44 | -0.42 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIA]] | B | PKIA activity raises TSPAN5's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without PKIA | 0.019 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[PRKCA]] | B | PRKCA activity raises TSPAN5's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 3.85× lower at baseline in the lines without PRKCA | 0.020 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[RGS17]] | B | RGS17 activity raises TSPAN5's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 2.28× lower at baseline in the lines without RGS17 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[CAMK1D]] | B | CAMK1D activity raises TSPAN5's level | lines that do not express CAMK1D (9) vs lines expressing it (41) | 2.79× lower at baseline in the lines without CAMK1D | 0.032 | ⚠ within organs, on part of the lines; also absent: OBSCN |
| [[LRRC8C]] | B | LRRC8C activity raises TSPAN5's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 2.33× lower at baseline in the lines without LRRC8C | 0.042 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[ANKH]] | B | ANKH activity raises TSPAN5's level | lines that do not express ANKH (6) vs lines expressing it (44) | 3.08× lower at baseline in the lines without ANKH | 0.058 | ⚠ within organs, on part of the lines; also absent: GCNT1, LCA5, CA13; maybe low, not absent |
| [[JHY]] | B | JHY activity raises TSPAN5's level | lines that do not express JHY (15) vs lines expressing it (35) | 2.56× lower at baseline in the lines without JHY | 0.060 | ⚠ within organs, on part of the lines; also absent: RGS17, KCNS3, BHLHE41 |
| [[FYN]] | B | FYN activity raises TSPAN5's level | lines that do not express FYN (8) vs lines expressing it (42) | 2.63× lower at baseline in the lines without FYN | 0.063 | ⚠ within organs, on part of the lines; also absent: RHOBTB3; maybe low, not absent |
| [[UBASH3B]] | B | UBASH3B activity raises TSPAN5's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without UBASH3B | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[HDAC6]] | B | HDAC6 activity lowers TSPAN5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KLF12]] | C | KLF12 activity raises TSPAN5's level | lines that do not express KLF12 (9) vs lines expressing it (41) | 3.37× lower at baseline in the lines without KLF12 | 0.014 | ⚠ within organs, on part of the lines; also absent: RHOBTB1, ZC3H12C, GNAI1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS17]] | B | TSPAN5 activity raises RGS17's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 3.20× lower at baseline in the lines without TSPAN5 | 0.009 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[PKIA]] | B | TSPAN5 activity raises PKIA's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 4.62× lower at baseline in the lines without TSPAN5 | 0.020 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[LRRC8C]] | B | TSPAN5 activity raises LRRC8C's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 2.18× lower at baseline in the lines without TSPAN5 | 0.031 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[DUSP5]] | B | TSPAN5 activity raises DUSP5's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 2.32× lower at baseline in the lines without TSPAN5 | 0.037 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[ARSJ]] | B | TSPAN5 activity raises ARSJ's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 3.42× lower at baseline in the lines without TSPAN5 | 0.055 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[JHY]] | B | TSPAN5 activity raises JHY's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 2.58× lower at baseline in the lines without TSPAN5 | 0.057 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[DPF3]] | B | TSPAN5 activity raises DPF3's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without TSPAN5 | 0.060 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[SLC9A7]] | B | TSPAN5 activity raises SLC9A7's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 1.82× lower at baseline in the lines without TSPAN5 | 0.064 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[TRIM9]] | B | TSPAN5 activity raises TRIM9's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without TSPAN5 | 0.088 | ⚠ within organs, on part of the lines; also absent: KLF12 |
| [[KLF12]] | C | TSPAN5 activity raises KLF12's level | lines that do not express TSPAN5 (9) vs lines expressing it (41) | 4.10× lower at baseline in the lines without TSPAN5 | 0.003 | ⚠ within organs, on part of the lines; also absent: KLF12; co-absent with the target |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.9, 7.7); signed map (3.5, 52.0). **Vector** length 113, 29.9% of its response variance represented; |z| ≥ 3 in 1,385 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +7.5 | +5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.4 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -6.4 | -6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -14.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | -4.8 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -6.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:98,470,367-98,658,611 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Tspan-5, NET-4; previously TM4SF9 |
| Gene groups (HGNC) | Tetraspanin family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 1 pathways, smallest: Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62079](https://www.uniprot.org/uniprotkb/P62079) (Tetraspanin-5):

> Part of TspanC8 subgroup, composed of 6 members that interact with the transmembrane metalloprotease ADAM10. This interaction is required for ADAM10 exit from the endoplasmic reticulum and for enzymatic maturation and trafficking to the cell surface as well as substrate specificity. Different TspanC8/ADAM10 complexes have distinct substrates. Promotes ADAM10-mediated cleavage of CD44. Seems to regulate VE-cadherin expression in endothelial cells probably through interaction with ADAM10, …

**Summary**, from NCBI Gene [10098](https://www.ncbi.nlm.nih.gov/gene/10098):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17753](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17753) · Entrez [10098](https://www.ncbi.nlm.nih.gov/gene/10098) · UniProt [P62079](https://www.uniprot.org/uniprotkb/P62079) · Ensembl [ENSG00000168785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168785)

## Data

Gene col 9699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9699); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9699]; `tensor/DDL_lfc|DDL_z.npy` [9699]; `embed/gene_vectors.npy` [9699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9699 or target_col == 9699). Every well: [[TSPAN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
