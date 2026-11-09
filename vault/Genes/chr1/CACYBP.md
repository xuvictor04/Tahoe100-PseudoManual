---
symbol: "CACYBP"
type: "gene"
col: 3769
ensembl_id: "ENSG00000116161"
name: "calcyclin binding protein"
location: "1q25.1"
module: 60
arm: "+"
pooled_cpm: 59.63
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# CACYBP

*calcyclin binding protein* — 1q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 7.53× (z +20.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.637× (z -6.4, q 9e-08, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (AsPC-1 0.240×, A-427 0.280×, NCI-H23 0.328×, BT-474 0.376×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.227×, AsPC-1 0.262×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0807×; ⚠ cell-cycle shift, explains ~58% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPD1]] (+0.79, fdr 7e-06), [[HSPE1]] (+0.79, fdr 7e-06), [[HSP90AA2P]] (+0.78, fdr 7e-06); moves opposite to [[METTL25B]] (-0.64, fdr 7e-06), [[H6PD]] (-0.60, fdr 1e-05), [[EP300]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DGKG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3769.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **7.53×** | +20.2 | 0e+00 | 48/48 (BT-474, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **5.27×** | +16.6 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.68×** | +15.4 | 0e+00 | 48/48 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **4.65×** | +15.4 | 0e+00 | 48/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.28×** | +14.0 | 3e-42 | 40/42 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.39×** | +11.5 | 1e-28 | 48/48 (CFPAC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **5.09×** | +8.5 | 1e-15 | 43/43 (CFPAC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.36×** | +8.2 | 1e-14 | 44/47 (COLO 205, C32, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.60×** | +8.2 | 2e-14 | 40/45 (HS-578T, A-172, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **3.32×** | +6.3 | 2e-08 | 45/47 (J82, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.81×** | +6.0 | 1e-07 | 42/49 (CFPAC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.76×** | +5.6 | 1e-06 | 41/46 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.45×** | +5.2 | 7e-06 | 41/48 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **2.60×** | +5.0 | 3e-05 | 41/48 (BT-474, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.006 | 31/47 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.008 | 27/48 (C32, NCI-H1792, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.015 | 26/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **1.84×** | +3.2 | 0.040 | 23/46 (HOP62, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.040 | 25/48 (A549, HOP62, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.71×** | +3.1 | 0.049 | 22/48 (SW 900, HOP62, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.050 | 23/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.051 | 23/48 (NCI-H1573, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3769.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (AsPC-1 0.240×, A-427 0.280×, NCI-H23 0.328×, BT-474 0.376×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.227×, AsPC-1 0.262×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0807×; ⚠ cell-cycle shift, explains ~58% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.637×** | -6.4 | 9e-08 | 36/48 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.652×** | -4.3 | 0.005 | 30/48 (A-427, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.683× | -3.3 | 0.21 | 27/49 (RKO, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.559× | -3.0 | 0.30 | 24/49 (AN3 CA, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Baicalin (drug)]] 5 µM |  | 0.810× | -3.0 | 0.30 | 21/49 (hTERT-HPNE, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3769. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 73.1 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.8× (z +19.1) | — |
| [[A-427 (line)]] | wt | 146 | 5 (2 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 6.18× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.2) |
| [[A498 (line)]] | wt | 70.4 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.81× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 7.63× (z +13.7) | — |
| [[HS-578T (line)]] | alt | 40.8 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.11× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.06× (z +13.2) | — |
| [[C32 (line)]] | wt | 22.9 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 33.3× (z +17.5) | — |
| [[CFPAC-1 (line)]] | alt | 51.6 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.33× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 49.5 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 13.8× (z +17.8) | — |
| [[HT-29 (line)]] | alt | 40.9 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 15.5× (z +17.2) | — |
| [[J82 (line)]] | alt | 82.2 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.11× (z +13.2) | — |
| [[KATO III (line)]] | alt | 46.3 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.90× (z +14.2) | — |
| [[LoVo (line)]] | wt | 48.7 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 16.7× (z +18.9) | — |
| [[LS 180 (line)]] | wt | 52.6 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.91× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 47.6 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.61× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 63.7 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.20× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 67.4 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.76× (z +17.7) | — |
| [[A549 (line)]] | wt | 43.5 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.6× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.99× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 82.8 | 4 | 1 | [[Auranofin (drug)]] 5 µM 19.1× (z +22.6) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 82.5 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.1× (z +19.0) | — |
| [[Hs 766T (line)]] | wt | 57.5 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.73× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.9× (z +13.1) | — |
| [[LOX-IMVI (line)]] | wt | 55.7 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.1× (z +16.0) | — |
| [[NCI-H1573 (line)]] | alt | 29.3 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 6.35× (z +10.2) | — |
| [[RPMI-7951 (line)]] | alt | 38.4 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.0× (z +14.6) | — |
| [[SNU-423 (line)]] | alt | 41.5 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.5× (z +15.4) | — |
| [[SW480 (line)]] | alt | 62.4 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.50× (z +16.8) | — |
| [[AsPC-1 (line)]] | alt | 79.4 | 2 | 2 | [[Auranofin (drug)]] 5 µM 5.02× (z +11.5) | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 65.2 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 12.6× (z +16.3) | — |
| [[NCI-H2030 (line)]] | alt | 40.4 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.52× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 81.9 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.36× (z +13.3) | — |
| [[SK-MEL-2 (line)]] | alt | 66.6 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.10× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 52.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.43× (z +14.0) | — |
| [[COLO 205 (line)]] | alt | 31.1 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 10.4× (z +11.6) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 7.41× (z +10.3) | — |
| [[H4 (line)]] | wt | 42.2 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.60× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 57.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.53× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 54.9 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 6.19× (z +12.3) | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 67.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.71× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.86× (z +12.3) | — |
| [[RKO (line)]] | wt | 83.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 11.7× (z +15.3) | — |
| [[NCI-H1792 (line)]] | alt | 26.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 60.4 | 1 | 1 | [[Auranofin (drug)]] 5 µM 12.5× (z +15.3) | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.1) |
| [[AN3 CA (line)]] | alt | 54.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.6× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 75.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.72× (z +15.3) | — |
| [[CHP-212 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0807× (z -9.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HepG2_C3A (line)]] | wt | 38.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.69× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 76.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.72× (z +10.0) | — |
| [[SW48 (line)]] | wt | 66.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.46× (z +12.3) | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3769), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPD1]] | +0.79 | +0.78 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 436 |
| [[HSPE1]] | +0.79 | +0.79 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 556 |
| [[HSP90AA2P]] | +0.78 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AA1]] | +0.78 | +0.72 / +0.82 | both halves | 7e-06 | STRING 863 |
| [[CHORDC1]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 | STRING 582 |
| [[AHSA1]] | +0.75 | +0.77 / +0.70 | both halves | 7e-06 | STRING 730 |
| [[HIBCH]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[HSP90AB3P]] | +0.74 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ATP2C1]] | +0.74 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[CCT4]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 | STRING 404 |
| [[CCT3]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 | STRING 456 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL25B]] | -0.64 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[H6PD]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[EP300]] | -0.59 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[HLA-A]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[TNRC6C]] | -0.57 | -0.66 / -0.38 | both halves | 6e-05 |  |
| [[RELB]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NFKB2]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[H2AJ]] | -0.57 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[PER2]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[DOP1A]] | -0.57 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[TXNIP]] | -0.56 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[REL]] | -0.56 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKG]] | B | DGKG activity lowers CACYBP's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.33× higher at baseline in the lines without DGKG | 0.087 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.868). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.2, -11.1); signed map (-26.4, -28.2). **Vector** length 101, 39.7% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.60 to 13); *Attenuation phase* (reactome, mean cos +0.58 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.57 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.5 | +15.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.7 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.4 | +15.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.5 | +20.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.8 | +8.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.4 | +6.0 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.9 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | +0.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -1.8 | +0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.6 | +0.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | calcyclin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.1 — chr1:174,999,163-175,012,027 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIP, S100A6BP |
| Hallmark sets | MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB71](https://www.uniprot.org/uniprotkb/Q9HB71) (Calcyclin-binding protein):

> May be involved in calcium-dependent ubiquitination and subsequent proteasomal degradation of target proteins. Probably serves as a molecular bridge in ubiquitin E3 complexes. Participates in the ubiquitin-mediated degradation of beta-catenin (CTNNB1).

**Summary**, from NCBI Gene [27101](https://www.ncbi.nlm.nih.gov/gene/27101):

> The protein encoded by this gene is a calcyclin binding protein. It may be involved in calcium-dependent ubiquitination and subsequent proteosomal degradation of target proteins. It probably serves as a molecular bridge in ubiquitin E3 complexes and participates in the ubiquitin-mediated degradation of beta-catenin. Two alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30423) · Entrez [27101](https://www.ncbi.nlm.nih.gov/gene/27101) · UniProt [Q9HB71](https://www.uniprot.org/uniprotkb/Q9HB71) · Ensembl [ENSG00000116161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116161)

## Data

Gene col 3769: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3769); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3769, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3769]; `tensor/DDL_lfc|DDL_z.npy` [3769]; `embed/gene_vectors.npy` [3769]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3769 or target_col == 3769). Every well: [[CACYBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACYBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
