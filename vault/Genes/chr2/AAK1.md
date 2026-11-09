---
symbol: "AAK1"
type: "gene"
col: 3746
ensembl_id: "ENSG00000115977"
name: "AP2 associated kinase 1"
location: "2p13.3"
module: 72
arm: "+"
pooled_cpm: 161.89
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# AAK1

*AP2 associated kinase 1* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.85× (z +13.1, q 1e-36, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.617× (z -10.5, q 3e-23, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 0.812× (z -4.4, q 8e-04, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANO10]] (+0.67, fdr 1e-05), [[TANGO2]] (+0.66, fdr 7e-06), [[SGTB]] (+0.65, fdr 1e-05); moves opposite to [[BCLAF1]] (-0.56, fdr 4e-05), [[NFKB1]] (-0.56, fdr 2e-05), [[YAP1]] (-0.56, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01564]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.85×** | +13.1 | 1e-36 | 47/48 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +11.5 | 2e-28 | 45/48 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +9.1 | 2e-17 | 38/48 (LoVo, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +8.2 | 2e-14 | 41/48 (LoVo, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +8.0 | 1e-13 | 39/48 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +8.0 | 2e-13 | 39/45 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +7.8 | 6e-13 | 36/48 (SW480, LoVo, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.26×** | +7.3 | 2e-11 | 28/48 (SNU-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +7.0 | 1e-10 | 30/48 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +6.6 | 3e-09 | 32/48 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +6.3 | 1e-08 | 30/48 (COLO 205, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +5.6 | 9e-07 | 20/49 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +5.3 | 5e-06 | 22/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 3e-05 | 26/48 (SNU-1, RKO, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.24×** | +4.9 | 3e-05 | 29/47 (SNU-1, RKO, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.50×** | +4.5 | 3e-04 | 24/48 (PANC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.22×** | +4.4 | 3e-04 | 23/48 (NCI-H1573, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +4.4 | 3e-04 | 25/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.617×** | -10.5 | 3e-23 | 35/44 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.722×** | -10.2 | 4e-22 | 32/48 (NCI-H1792, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.650×** | -9.0 | 3e-17 | 35/45 (Panc 03.27, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.679×** | -8.8 | 3e-16 | 35/49 (Panc 03.27, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.743×** | -6.5 | 1e-08 | 27/48 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.764×** | -6.1 | 9e-08 | 29/48 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -6.1 | 9e-08 | 30/47 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.779×** | -5.7 | 1e-06 | 24/48 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.812×** | -4.4 | 8e-04 | 25/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.827×** | -4.3 | 9e-04 | 25/48 (NCI-H460, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -4.2 | 0.001 | 24/48 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -4.2 | 0.001 | 21/48 (HS-578T, A-172, …) | rises with dose | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.898× | -3.4 | 0.028 | 6/48 (SW480, SW 1271, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -3.1 | 0.074 | 19/45 (RPMI-7951, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.803×** | -3.1 | 0.074 | 17/48 (SW 900, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.875× | -3.0 | 0.080 | 18/48 (LoVo, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 139 | 3 | 8 (8 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.87× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.414× (z -10.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 180 | 3 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -10.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 134 | 5 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.94× (z +17.0) | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -11.2) ⚠ cell-cycle shift, explains ~54% of this change |
| [[PANC-1 (line)]] | alt | 202 | 6 (2 ⚠) | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.20× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.626× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 277 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -18.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[C32 (line)]] | wt | 233 | 1 | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.82× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 203 | 3 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.94× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.203× (z -21.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 114 | 6 (3 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 2.75× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 144 | 3 (1 ⚠) | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.81× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.520× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 261 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -29.3) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A498 (line)]] | wt | 250 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.30× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.466× (z -10.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 206 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -14.1) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HS-578T (line)]] | alt | 226 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -14.9) ⚠ cell-cycle shift, explains ~54% of this change |
| [[KATO III (line)]] | alt | 167 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LS 180 (line)]] | wt | 92.7 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.39× (z +12.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.390× (z -9.9) ⚠ cell-cycle shift, explains ~95% of this change |
| [[SNU-1 (line)]] | wt | 144 | 3 (1 ⚠) | 1 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.33× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 137 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.16× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 209 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -15.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[J82 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.383× (z -14.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 183 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.374× (z -10.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 168 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AsPC-1 (line)]] | alt | 134 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.32× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 153 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -12.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 106 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.78× (z +9.6) | — |
| [[RKO (line)]] | wt | 185 | 2 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 1.88× (z +10.1) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 136 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.22× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -9.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 212 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.662× (z -8.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[AN3 CA (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -14.9) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HCT15 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 2.09× (z +8.7) ⚠ cell-cycle shift, explains ~11% of this change | — |
| [[HEC-1-A (line)]] | alt | 61.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -8.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[HOP62 (line)]] | alt | 205 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 1.87× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 71.5 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.54× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.463× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.499× (z -11.1) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 222 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -12.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SK-MEL-2 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -11.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW48 (line)]] | wt | 94.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.266× (z -8.8) ⚠ cell-cycle shift, explains ~95% of this change |
| [[BT-474 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 239 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 127 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANO10]] | +0.67 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SGTB]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[GTPBP2]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[UBE2Q2P2-1]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[MAP1B]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PCYT1A]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[LARP6]] | +0.63 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[LIMK1]] | +0.63 | +0.63 / +0.57 | both halves | 8e-06 |  |
| [[XPOT]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[SESN2]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[SARS1]] | +0.62 | +0.52 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCLAF1]] | -0.56 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[NFKB1]] | -0.56 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[YAP1]] | -0.56 | -0.43 / -0.53 | both halves | 4e-05 |  |
| [[ZNF608]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[NFYC]] | -0.55 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[TNFAIP3]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[NFKBIA]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[TGIF2]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SETDB2]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PNRC2]] | -0.51 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[HNRNPD]] | -0.51 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[H6PD]] | -0.51 | -0.55 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01564]] | B | LINC01564 activity lowers AAK1's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 1.32× higher at baseline in the lines without LINC01564 | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent |
| [[DEPDC7]] | B | DEPDC7 activity raises AAK1's level | lines that do not express DEPDC7 (13) vs lines expressing it (37) | 1.45× lower at baseline in the lines without DEPDC7 | 0.048 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.2, 43.9); signed map (-10.3, 24.3). **Vector** length 145, 50.2% of its response variance represented; |z| ≥ 3 in 1,626 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +11.6 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +11.1 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.5 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.8 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.3 | +8.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.4 | +7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.8 | +5.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.9 | +5.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -9.0 | -10.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -6.2 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.0 | -5.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | -6.0 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -5.7 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.7 | -4.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.8 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -0.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | AP2 associated kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:69,457,997-69,674,349 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1048, DKFZp686K16132 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Numb-associated kinase family |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2M2I8](https://www.uniprot.org/uniprotkb/Q2M2I8) (AP2-associated protein kinase 1):

> Regulates clathrin-mediated endocytosis by phosphorylating the AP2M1/mu2 subunit of the adaptor protein complex 2 (AP-2) which ensures high affinity binding of AP-2 to cargo membrane proteins during the initial stages of endocytosis. Isoform 1 and isoform 2 display similar levels of kinase activity towards AP2M1. Preferentially, may phosphorylate substrates on threonine residues. Regulates phosphorylation of other AP-2 subunits as well as AP-2 localization and AP-2-mediated internalization of …

**Summary**, from NCBI Gene [22848](https://www.ncbi.nlm.nih.gov/gene/22848):

> This gene encodes a member of the SNF1 subfamily of serine/threonine protein kinases. Adaptor-related protein complex 2 (AP-2 complexes) functions during receptor-mediated endocytosis to trigger clathrin assembly, interact with membrane-bound receptors, and recruit encodytic accessory factors. The encoded protein interacts with and phosphorylates a subunit of the AP-2 complex, which promotes binding of AP-2 to sorting signals found in membrane-bound receptors and subsequent receptor …

**Accessions** — [HGNC:19679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19679) · Entrez [22848](https://www.ncbi.nlm.nih.gov/gene/22848) · UniProt [Q2M2I8](https://www.uniprot.org/uniprotkb/Q2M2I8) · Ensembl [ENSG00000115977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115977)

## Data

Gene col 3746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3746); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3746]; `tensor/DDL_lfc|DDL_z.npy` [3746]; `embed/gene_vectors.npy` [3746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3746 or target_col == 3746). Every well: [[AAK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AAK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
