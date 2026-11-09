---
symbol: "EXOC2"
type: "gene"
col: 3394
ensembl_id: "ENSG00000112685"
name: "exocyst complex component 2"
location: "6p25.3"
module: 36
arm: "+"
pooled_cpm: 95.09
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# EXOC2

*exocyst complex component 2* — 6p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.39× (z +5.9, q 3e-06, up in 35 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.27× (z +4.5, q 0.002, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.463× (z -20.8, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERC2]] (+0.80, fdr 7e-06), [[HERC2P9]] (+0.75, fdr 7e-06), [[VPS13D]] (+0.75, fdr 7e-06); moves opposite to [[ZNF490]] (-0.62, fdr 3e-05), [[FAM117A]] (-0.61, fdr 1e-05), [[RSRP1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3394.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.39×** | +5.9 | 3e-06 | 35/48 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 0.002 | 27/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.24×** | +4.1 | 0.008 | 26/48 (COLO 205, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.024 | 24/47 (HEC-1-A, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.1 | 0.26 | 19/48 (SNU-423, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3394.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.463×** | -20.8 | 0e+00 | 47/49 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.475×** | -20.1 | 0e+00 | 43/48 (A-172, J82, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.448×** | -14.7 | 0e+00 | 43/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.521×** | -11.9 | 2e-30 | 35/44 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.564×** | -10.9 | 9e-26 | 41/49 (RKO, J82, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -10.4 | 2e-23 | 36/50 (NCI-H23, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.607×** | -9.6 | 1e-19 | 32/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -8.4 | 5e-15 | 32/48 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.630×** | -8.2 | 2e-14 | 35/45 (J82, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -5.8 | 4e-07 | 31/48 (A-172, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **0.774×** | -4.9 | 5e-05 | 26/48 (C32, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.798×** | -4.3 | 7e-04 | 22/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.799×** | -4.3 | 7e-04 | 23/48 (SW48, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -4.1 | 0.002 | 20/48 (C32, J82, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.768×** | -3.6 | 0.012 | 24/48 (SW48, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.840× | -3.3 | 0.026 | 17/48 (J82, C32, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.802×** | -3.0 | 0.074 | 14/49 (NCI-H1573, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.896× | -3.0 | 0.074 | 17/48 (A-172, HOP62, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.856× | -3.0 | 0.074 | 17/48 (BT-474, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3394. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 148 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -32.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -21.6) |
| [[NCI-H460 (line)]] | wt | 97.8 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -21.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.277× (z -15.9) |
| [[C32 (line)]] | wt | 112 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -26.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -18.2) |
| [[J82 (line)]] | alt | 151 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -31.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -20.1) |
| [[LoVo (line)]] | wt | 111 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -24.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 90.5 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.1) |
| [[SW48 (line)]] | wt | 111 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.133× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 106 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -15.6) |
| [[HEC-1-A (line)]] | alt | 85.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -20.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.317× (z -13.3) |
| [[RKO (line)]] | wt | 101 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -11.6) |
| [[SW480 (line)]] | alt | 104 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -17.2) |
| [[A549 (line)]] | wt | 82.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -18.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -16.7) |
| [[HOP62 (line)]] | alt | 95.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -21.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.0) |
| [[HS-578T (line)]] | alt | 90.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -22.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -15.5) |
| [[hTERT-HPNE (line)]] | wt | 96.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -19.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 107 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.279× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.323× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 86.7 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.330× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 188 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -12.7) |
| [[PANC-1 (line)]] | alt | 103 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -16.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.367× (z -14.3) |
| [[SW1417 (line)]] | alt | 79.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -18.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -12.7) |
| [[A498 (line)]] | wt | 53.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -17.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.283× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 47.2 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -13.7) |
| [[KATO III (line)]] | alt | 88.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.359× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 117 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -17.8) |
| [[LS 180 (line)]] | wt | 95.6 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 76.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -13.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.447× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 69.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.6) |
| [[SNU-423 (line)]] | alt | 88.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -20.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.319× (z -10.2) |
| [[SW 900 (line)]] | alt | 56.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.345× (z -9.6) |
| [[AN3 CA (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 98.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.6) |
| [[CHP-212 (line)]] | wt | 128 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -9.1) |
| [[SHP-77 (line)]] | alt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 141 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 64.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -8.7) |
| [[HT-29 (line)]] | alt | 74.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -14.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 44.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -8.9) |
| [[SW 1271 (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 98.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 80.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3394), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.75 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[VPS13D]] | +0.75 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[RNF216]] | +0.74 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[PACC1]] | +0.72 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[INPP4A]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 | pathway: Organelle biogenesis and maintenance |
| [[HERC2P2]] | +0.69 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[EP400]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[SPATA5]] | +0.67 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[LIMK1]] | +0.66 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ERI3]] | +0.66 | +0.65 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF490]] | -0.62 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[FAM117A]] | -0.61 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ABCA10]] | -0.60 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[MALINC1]] | -0.60 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[NFKBID]] | -0.60 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[ABCA5]] | -0.59 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[SPEN-AS1]] | -0.58 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[SGO1-AS1]] | -0.58 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[TP53]] | -0.58 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[ZNF44]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PAN2]] | -0.57 | -0.63 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers EXOC2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-6.6, -31.7); signed map (-16.2, -52.4). **Vector** length 117, 38.9% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +8.2 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +7.9 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.4 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -9.0 | -20.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -20.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.4 | -14.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -1.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | exocyst complex component 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.3 — chr6:485,154-693,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11026, Sec5; previously SEC5L1 |
| Gene groups (HGNC) | Exocyst complex; IPT domain containing |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 10 pathways, smallest: VxPx cargo-targeting to cilium; Insulin processing; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KP1](https://www.uniprot.org/uniprotkb/Q96KP1) (Exocyst complex component 2):

> Component of the exocyst complex involved in the docking of exocytic vesicles with fusion sites on the plasma membrane.

**Summary**, from NCBI Gene [55770](https://www.ncbi.nlm.nih.gov/gene/55770):

> The protein encoded by this gene is a component of the exocyst complex, a multi-protein complex essential for the polarized targeting of exocytic vesicles to specific docking sites on the plasma membrane. Though best characterized in yeast, the component proteins and the functions of the exocyst complex have been demonstrated to be highly conserved in higher eukaryotes. At least eight components of the exocyst complex, including this protein, are found to interact with the actin cytoskeletal …

**Accessions** — [HGNC:24968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24968) · Entrez [55770](https://www.ncbi.nlm.nih.gov/gene/55770) · UniProt [Q96KP1](https://www.uniprot.org/uniprotkb/Q96KP1) · Ensembl [ENSG00000112685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112685)

## Data

Gene col 3394: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3394); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3394, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3394]; `tensor/DDL_lfc|DDL_z.npy` [3394]; `embed/gene_vectors.npy` [3394]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3394 or target_col == 3394). Every well: [[EXOC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
