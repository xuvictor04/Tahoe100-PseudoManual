---
symbol: "WDR44"
type: "gene"
col: 5236
ensembl_id: "ENSG00000131725"
name: "WD repeat domain 44"
location: "Xq24"
module: 3
arm: "+"
pooled_cpm: 104.53
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# WDR44

*WD repeat domain 44* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.36× (z +9.6, q 6e-19, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.353× (z -23.2, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.642× (z -9.9, q 8e-21, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX12]] (+0.62, fdr 1e-05), [[ORMDL2]] (+0.62, fdr 1e-05), [[MACO1]] (+0.61, fdr 1e-05); moves opposite to [[SRSF1]] (-0.61, fdr 1e-05), [[POMK]] (-0.60, fdr 1e-05), [[DUS3L]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MGMT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +9.6 | 6e-19 | 28/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +8.1 | 2e-13 | 36/48 (HT-29, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +6.7 | 4e-09 | 31/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +5.6 | 3e-06 | 22/48 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.30×** | +5.6 | 3e-06 | 30/47 (H4, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.5 | 4e-06 | 28/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.28×** | +5.4 | 4e-06 | 26/48 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +5.4 | 6e-06 | 24/48 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +4.7 | 2e-04 | 24/48 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.4 | 6e-04 | 24/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.20×** | +4.1 | 0.002 | 22/47 (NCI-H2030, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.0 | 0.003 | 22/48 (SW1417, HT-29, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.8 | 0.005 | 11/49 (LS 180, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +3.7 | 0.009 | 15/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.009 | 21/50 (C32, SW 900, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.022 | 6/48 (A-427, SW48, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.026 | 17/48 (RKO, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.353×** | -23.2 | 0e+00 | 46/49 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.389×** | -20.2 | 0e+00 | 42/44 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.405×** | -18.6 | 0e+00 | 39/45 (SNU-423, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.642×** | -9.9 | 8e-21 | 37/48 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.726×** | -7.1 | 1e-10 | 37/48 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.754×** | -6.0 | 1e-07 | 31/47 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.768×** | -5.6 | 1e-06 | 26/47 (SK-MEL-2, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.781×** | -5.3 | 9e-06 | 28/48 (NCI-H460, RKO, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.809×** | -4.7 | 2e-04 | 24/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.876× | -4.2 | 0.002 | 9/48 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.703×** | -4.1 | 0.002 | 20/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.718×** | -3.8 | 0.006 | 21/49 (J82, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.848× | -3.7 | 0.010 | 10/48 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.860× | -3.4 | 0.031 | 14/48 (AsPC-1, RPMI-7951, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.812×** | -3.3 | 0.034 | 19/47 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.874× | -3.0 | 0.088 | 8/49 (HT-29, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 129 | 3 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.303× (z -14.8) |
| [[SW480 (line)]] | alt | 116 | 4 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.460× (z -11.7) |
| [[HT-29 (line)]] | alt | 82.1 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -13.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 68.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 157 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.183× (z -20.8) |
| [[COLO 205 (line)]] | alt | 78.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0970× (z -21.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 125 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -9.8) |
| [[HS-578T (line)]] | alt | 84.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -11.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 113 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -19.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 198 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.306× (z -15.1) |
| [[SW1417 (line)]] | alt | 74.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +17.9) | [[Dinaciclib (drug)]] 0.05 µM 0.405× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 94.6 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -18.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 98.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -16.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 131 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Allantoin (drug)]] 0.5 µM 0.433× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 141 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -17.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 87.9 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.312× (z -12.4) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 147 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.531× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 109 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -18.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 128 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -20.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 104 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -16.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 135 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -16.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -16.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.482× (z -9.1) |
| [[LS 180 (line)]] | wt | 81.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.77× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 84.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -14.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 75.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.358× (z -9.4) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -15.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.337× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 66.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 82.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 99.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 99.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.334× (z -11.8) |
| [[NCI-H596 (line)]] | alt | 105 | 1 | 1 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 2.41× (z +8.6) | [[Oxaprozin (drug)]] 5 µM 0.153× (z -19.2) |
| [[RPMI-7951 (line)]] | alt | 84.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -16.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 69.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.1) | — |
| [[C32 (line)]] | wt | 61.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +13.1) | — |
| [[CHP-212 (line)]] | wt | 88.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -11.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 74.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 78.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.330× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 76.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -9.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX12]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[ORMDL2]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MACO1]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CCDC82]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[KIF1B]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 | same gene group |
| [[MORC3]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[RUBCN]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 | same gene group |
| [[PLIN3]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[ULBP2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[KLC1]] | +0.59 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[PPP1R21]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF1]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[POMK]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[DUS3L]] | -0.57 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[EWSR1]] | -0.56 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[MRRF]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[COG8]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[U2AF2]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[BACE1-AS]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CYP4A22-AS1]] | -0.53 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[TGFBRAP1]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TMEM147-AS1]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[PFAS]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGMT]] | B | MGMT activity raises WDR44's level | lines that do not express MGMT (11) vs lines expressing it (39) | 1.19× lower at baseline in the lines without MGMT | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02666, CDCP1, ZNF718 |
| [[CLTCL1]] | C | CLTCL1 activity weakens WDR44's drug response | lines that do not express CLTCL1 (3) vs lines expressing it (46) | the lines without CLTCL1 respond 1.33× as strongly (z diff -1.00); strongest at Ixazomib citrate 5 µM: 2.90x vs 1.34x (z diff -6.1) | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.2, -0.7); signed map (-15.5, 17.9). **Vector** length 108, 33.2% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.0 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.8 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.6 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.3 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.5 | -9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -18.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:118,346,073-118,449,961 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686L20145, RPH11, RAB11BP, SYM-4 |
| Gene groups (HGNC) | WD repeat domain containing; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JSH3](https://www.uniprot.org/uniprotkb/Q5JSH3) (WD repeat-containing protein 44):

> Downstream effector for Rab11 which regulates Rab11 intracellular membrane trafficking functions such as endocytic recycling, intracellular ciliogenesis and protein export. ATK1-mediated phosphorylation of WDR44 induces binding to Rab11 which activates endocytic recycling of transferrin receptor back to the plasma membrane. When bound to Rab11, prevents the formation of the ciliogenic Rab11-Rabin8/RAB3IP-RAB11FIP3 complex, therefore inhibiting preciliary trafficking and ciliogenesis. …

**Summary**, from NCBI Gene [54521](https://www.ncbi.nlm.nih.gov/gene/54521):

> This gene encodes a protein that interacts with the small GTPase rab11. A similar protein in rat binds the GTP-containing active form of rab11. This protein may play a role in endosome recycling. Alternate splicing results in multiple transcript variants.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:30512](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30512) · Entrez [54521](https://www.ncbi.nlm.nih.gov/gene/54521) · UniProt [Q5JSH3](https://www.uniprot.org/uniprotkb/Q5JSH3) · Ensembl [ENSG00000131725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131725)

## Data

Gene col 5236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5236); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5236]; `tensor/DDL_lfc|DDL_z.npy` [5236]; `embed/gene_vectors.npy` [5236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5236 or target_col == 5236). Every well: [[WDR44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
