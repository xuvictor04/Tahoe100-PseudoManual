---
symbol: "IST1"
type: "gene"
col: 11246
ensembl_id: "ENSG00000182149"
name: "IST1 factor associated with ESCRT-III"
location: "16q22.2"
module: 59
arm: "+"
pooled_cpm: 132.01
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# IST1

*IST1 factor associated with ESCRT-III* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.98× (z +17.4, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.393× (z -18.6, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.797× (z -4.0, q 0.007, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 14 lines (SW480 0.194×, NCI-H1792 0.157×, HT-29 0.259×, Hs 766T 0.198×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.302×; ⚠ toxic; transcription drop); [[GSK1059615 (drug)]] 0.5 µM in 1 line (SW 1271 0.108×); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2347 0.516×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC115]] (+0.71, fdr 7e-06), [[ZNF821]] (+0.71, fdr 1e-05, ⚠ same locus), [[AKAP1-DT]] (+0.70, fdr 1e-05), [[KMT2E]] (+0.70, fdr 7e-06); moves opposite to [[EEFSEC]] (-0.62, fdr 1e-05), [[RUVBL1]] (-0.62, fdr 1e-05), [[EFTUD2]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.98×** | +17.4 | 0e+00 | 48/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.25×** | +16.8 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +15.5 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.32×** | +13.0 | 1e-36 | 48/48 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +12.4 | 3e-33 | 42/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.69×** | +10.9 | 1e-25 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +8.9 | 5e-17 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +6.9 | 3e-10 | 30/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +6.4 | 7e-09 | 40/48 (A-427, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.9 | 2e-07 | 30/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.3 | 9e-04 | 22/49 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.1 | 0.002 | 22/38 (NCI-H1573, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.003 | 24/48 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.20×** | +3.8 | 0.006 | 23/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.026 | 21/49 (Hs 766T, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11246.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 14 lines (SW480 0.194×, NCI-H1792 0.157×, HT-29 0.259×, Hs 766T 0.198×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.302×; ⚠ toxic; transcription drop); [[GSK1059615 (drug)]] 0.5 µM in 1 line (SW 1271 0.108×); [[Belumosudil (drug)]] 5 µM in 1 line (NCI-H2347 0.516×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.393×** | -18.6 | 0e+00 | 43/44 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.501×** | -12.4 | 5e-33 | 45/49 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.721×** | -6.8 | 2e-09 | 34/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.773×** | -5.3 | 1e-05 | 28/48 (HT-29, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.796×** | -4.7 | 3e-04 | 26/48 (HT-29, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.797×** | -4.0 | 0.007 | 23/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.827×** | -3.9 | 0.007 | 24/48 (CFPAC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | 0.849× | -3.4 | 0.049 | 16/48 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.855× | -3.3 | 0.066 | 15/49 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.855× | -3.2 | 0.066 | 13/48 (SW48, NCI-H2030, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.895× | -3.2 | 0.082 | 7/48 (SNU-1, SNU-423, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.860× | -3.1 | 0.084 | 10/48 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.862× | -3.1 | 0.090 | 16/48 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.7 | 12 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.01× (z +23.3) | — |
| [[PANC-1 (line)]] | alt | 88.9 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.49× (z +22.3) | — |
| [[SW480 (line)]] | alt | 198 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -26.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 168 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -13.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 159 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +14.2) | [[Lonafarnib (drug)]] 5 µM 0.247× (z -9.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 150 | 3 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.17× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -21.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 152 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -21.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 234 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.77× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 101 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +16.3) | — |
| [[LOX-IMVI (line)]] | wt | 98.5 | 6 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.26× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 157 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.24× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 110 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.89× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +13.6) | — |
| [[NCI-H2347 (line)]] | alt | 107 | 2 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.516× (z -8.5) |
| [[RKO (line)]] | wt | 142 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.53× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 113 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.85× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 135 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -10.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 136 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.45× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -13.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 131 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -10.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 175 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -15.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 108 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.03× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -19.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 133 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -13.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 161 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.439× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 149 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.62× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -13.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 111 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -14.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 180 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.99× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -9.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 150 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.98× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -20.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 118 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 146 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.29× (z +15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.29× (z +15.7) | — |
| [[Panc 03.27 (line)]] | alt | 108 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.10× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.467× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 111 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.447× (z -10.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 159 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.69× (z +12.9) | — |
| [[J82 (line)]] | alt | 104 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.428× (z -10.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 103 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 103 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 136 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.74× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -12.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 131 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.04× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -14.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 142 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.14× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -10.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -8.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 91.7 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.39× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -15.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 116 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 98.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 144 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.108× (z -9.1) |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 165 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC115]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ZNF821]] | +0.71 | +0.57 / +0.67 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[AKAP1-DT]] | +0.70 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TRA2A]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[GPRC5C]] | +0.66 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ARID4B]] | +0.66 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TSC22D4]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TRAPPC6A]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[PRRT1]] | +0.65 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[EAPP]] | +0.63 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ACSM3]] | +0.63 | +0.34 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.62 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.62 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.62 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[NUP188]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 | pathway: Mitotic Anaphase |
| [[EIF2S1]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[HERC2]] | -0.60 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[VPS4A]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 | pathway: Mitotic Anaphase; STRING 988 |
| [[EIPR1]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[FARSB]] | -0.59 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[DOCK1]] | -0.59 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[UTP11]] | -0.58 | -0.56 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises IST1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FCGRT]] | B | FCGRT activity raises IST1's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 1.16× lower at baseline in the lines without FCGRT | 0.086 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.1, -39.2); signed map (-8.1, 4.0). **Vector** length 85.5, 27.8% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.5 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +6.1 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | -0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.3 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.9 | +10.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.8 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | IST1 factor associated with ESCRT-III |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:71,845,996-71,931,199 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CHMP8; previously KIAA0174 |
| Gene groups (HGNC) | ESCRT-III associated factors |
| Reactome | 9 pathways, smallest: Sealing of the nuclear envelope (NE) by ESCRT-III; Nuclear Envelope (NE) Reassembly; Mitotic Anaphase |
| Matched by | ensembl_id |

**Function**, from UniProt [P53990](https://www.uniprot.org/uniprotkb/P53990) (IST1 homolog):

> ESCRT-III-like protein involved in cytokinesis, nuclear envelope reassembly and endosomal tubulation. Is required for efficient abscission during cytokinesis. Involved in recruiting VPS4A and/or VPS4B to the midbody of dividing cells. During late anaphase, involved in nuclear envelope reassembly and mitotic spindle disassembly together with the ESCRT-III complex: IST1 acts by mediating the recruitment of SPAST to the nuclear membrane, leading to microtubule severing. Recruited to the reforming …

**Summary**, from NCBI Gene [9798](https://www.ncbi.nlm.nih.gov/gene/9798):

> This gene encodes a protein with MIT-interacting motifs that interacts with components of endosomal sorting complexes required for transport (ESCRT). ESCRT functions in vesicle budding, such as that which occurs during membrane abscission in cytokinesis. There is a pseudogene for this gene on chromosome 19. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:28977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28977) · Entrez [9798](https://www.ncbi.nlm.nih.gov/gene/9798) · UniProt [P53990](https://www.uniprot.org/uniprotkb/P53990) · Ensembl [ENSG00000182149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182149)

## Data

Gene col 11246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11246); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11246]; `tensor/DDL_lfc|DDL_z.npy` [11246]; `embed/gene_vectors.npy` [11246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11246 or target_col == 11246). Every well: [[IST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
