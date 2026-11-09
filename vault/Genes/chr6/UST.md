---
symbol: "UST"
type: "gene"
col: 3310
ensembl_id: "ENSG00000111962"
name: "uronyl 2-sulfotransferase"
location: "6q25.1"
module: 68
arm: "+"
pooled_cpm: 52.02
n_lines_expressing: 38
n_dd_up: 26
n_dd_down: 18
n_dd_up_clean: 21
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# UST

*uronyl 2-sulfotransferase* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.61× (z +22.8, q 0e+00, up in 32 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.452× (z -13.4, q 5e-38, down in 27 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.487× (z -12.1, q 3e-31, down in 27 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRIP1]] (+0.60, fdr 3e-05), [[MCOLN3]] (+0.58, fdr 4e-05), [[GYG1]] (+0.56, fdr 4e-05); moves opposite to [[TSFM]] (-0.55, fdr 8e-05), [[ERI1]] (-0.54, fdr 9e-05), [[FBXW2]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FGF2]] → it (grade B ⚠); 4 go from it, the strongest it → [[NEO1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +22.8 | 0e+00 | 32/36 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +11.8 | 2e-29 | 30/36 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +10.6 | 6e-24 | 22/36 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.55×** | +10.4 | 3e-23 | 27/36 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.69×** | +8.8 | 1e-16 | 31/36 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.65×** | +8.4 | 3e-15 | 30/36 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +8.1 | 4e-14 | 25/36 (NCI-H23, SW1417, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.1 | 1e-10 | 25/36 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +6.9 | 3e-10 | 26/36 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +5.6 | 2e-06 | 19/35 (C32, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +4.5 | 3e-04 | 17/37 (C32, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.4 | 5e-04 | 16/36 (C32, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 6e-04 | 15/35 (C32, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 8e-04 | 15/36 (C32, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 17/36 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.004 | 14/36 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.012 | 16/36 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.20× | +3.5 | 0.013 | 12/36 (BT-474, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.024 | 15/36 (HCT15, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.452×** | -13.4 | 5e-38 | 27/36 (RKO, Panc 03.27, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.487×** | -12.1 | 3e-31 | 27/36 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.497×** | -11.8 | 9e-30 | 26/36 (LOX-IMVI, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.507×** | -11.0 | 5e-26 | 17/29 (LoVo, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.495×** | -10.9 | 8e-26 | 25/33 (SNU-423, HS-578T, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.573×** | -9.4 | 6e-19 | 24/36 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.626×** | -7.9 | 2e-13 | 24/36 (KATO III, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.458×** | -6.9 | 4e-10 | 22/37 (LOX-IMVI, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.500×** | -6.1 | 6e-08 | 17/29 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.597×** | -4.6 | 3e-04 | 16/36 (HEC-1-A, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.759×** | -4.5 | 4e-04 | 16/35 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.768×** | -4.4 | 4e-04 | 20/36 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.604×** | -4.4 | 4e-04 | 20/36 (LOX-IMVI, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.615×** | -4.3 | 7e-04 | 17/36 (LOX-IMVI, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.792×** | -3.9 | 0.003 | 16/35 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.648×** | -3.8 | 0.005 | 15/35 (KATO III, J82, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.854× | -3.8 | 0.006 | 13/36 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.815×** | -3.5 | 0.017 | 12/36 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | 0.867× | -3.4 | 0.019 | 10/36 (A498, Panc 03.27, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.718×** | -2.9 | 0.095 | 11/36 (LOX-IMVI, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 127 | 0 | 18 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -19.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.133× (z -18.7) |
| [[HS-578T (line)]] | alt | 141 | 1 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -18.1) |
| [[LoVo (line)]] | wt | 196 | 5 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.233× (z -17.7) |
| [[A498 (line)]] | wt | 81.8 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.198× (z -8.7) |
| [[C32 (line)]] | wt | 59.6 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.64× (z +21.0) | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 136 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.370× (z -8.9) |
| [[BT-474 (line)]] | alt | 77.7 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +15.7) | — |
| [[HEC-1-A (line)]] | alt | 32.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +19.3) | — |
| [[Panc 03.27 (line)]] | alt | 132 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +17.7) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 28.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +15.2) | — |
| [[A-172 (line)]] | wt | 98.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[J82 (line)]] | alt | 62.9 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[KATO III (line)]] | alt | 97.5 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.150× (z -18.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.156× (z -17.8) |
| [[RKO (line)]] | wt | 118 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0612× (z -24.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.172× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 95.2 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 70.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -11.1) |
| [[SW1417 (line)]] | alt | 13.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.82× (z +14.5) | — |
| [[AN3 CA (line)]] | alt | 319 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LS 180 (line)]] | wt | 66.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0769× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 39.7 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.47× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 30.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.314× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 42.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 17.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +12.9) | — |
| [[hTERT-HPNE (line)]] | wt | 71.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.0512× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 24.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.88× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0916× (z -18.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +16.0) | — |
| [[H4 (line)]] | wt | 60.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +14.4) | — |
| [[HCT15 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[NCI-H1573 (line)]] | alt | 25.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 68.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.0) | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0894× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.66 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIP1]] | +0.60 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[MCOLN3]] | +0.58 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[GYG1]] | +0.56 | +0.53 / +0.42 | both halves | 4e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[ARHGEF40]] | +0.55 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[ARHGAP24]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[MARK1]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[LITAF]] | +0.54 | +0.54 / +0.31 | both halves | 2e-04 |  |
| [[ZFPM2]] | +0.54 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[TCEAL4]] | +0.54 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[CACHD1]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CAMK2D]] | +0.54 | +0.55 / +0.37 | both halves | 9e-05 |  |
| [[ARHGAP10]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSFM]] | -0.55 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[ERI1]] | -0.54 | -0.53 / -0.37 | both halves | 9e-05 |  |
| [[FBXW2]] | -0.54 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[WDR37]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[STRAP]] | -0.52 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[INTS11]] | -0.52 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[SEPTIN7P14]] | -0.51 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[SEC24C]] | -0.50 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[NOMO2]] | -0.50 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[GUSBP1]] | -0.50 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[B4GALT7]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 | pathway: Glycosaminoglycan metabolism; STRING 404 |
| [[ATG16L1]] | -0.47 | -0.45 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF2]] | B | FGF2 activity raises UST's level | lines that do not express FGF2 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without FGF2 | 0.025 | ⚠ within organs, on part of the lines; also absent: F2R, EML1, DPY19L2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers UST's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEO1]] | B | UST activity raises NEO1's level | lines that do not express UST (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without UST | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC1A1, SH3GL3 |
| [[ARHGAP10]] | B | UST activity raises ARHGAP10's level | lines that do not express UST (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without UST | 0.086 | ⚠ within organs, on part of the lines; also absent: SLC1A1, SH3GL3 |
| [[GRIP1]] | B | UST activity raises GRIP1's level | lines that do not express UST (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without UST | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC1A1, SH3GL3 |
| [[B4GALT7]] | B | UST activity raises B4GALT7's level | lines that do not express UST (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without UST | 0.092 | ⚠ within organs, on part of the lines; also absent: SLC1A1, SH3GL3 |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (18.7, 13.9); signed map (41.4, -16.9). **Vector** length 115, 31.0% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.1 | +11.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +7.2 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +22.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.0 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +8.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.3 | +4.4 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.3 | -11.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -12.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.2 | -9.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.1 | -3.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | uronyl 2-sulfotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:148,747,030-149,076,990 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 2OST |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Reactome | 5 pathways, smallest: DS-GAG biosynthesis; CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2C2](https://www.uniprot.org/uniprotkb/Q9Y2C2) (Uronyl 2-sulfotransferase):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) to catalyze the transfer of a sulfo group to the 2-OH position of uronyl residues in glycosaminoglycan chains. Has mainly activity toward iduronyl residues in dermatan sulfate, and toward glucuronyl residues of chondroitin sulfate. Has little to no activity toward desulfated N-resulfated heparin or N-sulfoheparosan.

**Summary**, from NCBI Gene [10090](https://www.ncbi.nlm.nih.gov/gene/10090):

> Uronyl 2-sulfotransferase transfers sulfate to the 2-position of uronyl residues, such as iduronyl residues in dermatan sulfate and glucuronyl residues in chondroitin sulfate (Kobayashi et al., 1999 [PubMed 10187838]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17223) · Entrez [10090](https://www.ncbi.nlm.nih.gov/gene/10090) · UniProt [Q9Y2C2](https://www.uniprot.org/uniprotkb/Q9Y2C2) · Ensembl [ENSG00000111962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111962)

## Data

Gene col 3310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3310); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3310]; `tensor/DDL_lfc|DDL_z.npy` [3310]; `embed/gene_vectors.npy` [3310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3310 or target_col == 3310). Every well: [[UST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
