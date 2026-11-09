---
symbol: "KPNA6"
type: "gene"
col: 367
ensembl_id: "ENSG00000025800"
name: "karyopherin subunit alpha 6"
location: "1p35.2"
module: 118
arm: "+"
pooled_cpm: 108.66
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# KPNA6

*karyopherin subunit alpha 6* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.31× (z +24.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.803× (z -9.2, q 3e-17, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.425×, RKO 0.496×; ⚠ cell-cycle shift, explains ~53% of this change); [[Tucidinostat (drug)]] 5 µM in 2 lines (SW1417 0.648×, SW480 0.732×); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Fluvoxamine (drug)]] 5 µM in 1 line (SW 1088 0.0815×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAGPA]] (+0.64, fdr 1e-05), [[FBXW11]] (+0.62, fdr 9e-06), [[UBE2L3]] (+0.61, fdr 7e-06); moves opposite to [[N4BP3]] (-0.60, fdr 1e-05), [[SH3GL2]] (-0.53, fdr 2e-05), [[SLFN11]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HMSD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 23 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 367.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.31×** | +24.6 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +22.3 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.60×** | +19.7 | 0e+00 | 48/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.74×** | +16.3 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +15.8 | 0e+00 | 46/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +15.2 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +13.2 | 1e-37 | 39/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +12.0 | 3e-31 | 46/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +11.7 | 1e-29 | 33/49 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +11.2 | 2e-27 | 45/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +9.7 | 1e-20 | 41/48 (SW480, LoVo, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.36×** | +8.7 | 2e-16 | 37/47 (LoVo, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.33×** | +8.4 | 2e-15 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +7.4 | 4e-12 | 32/38 (NCI-H1573, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.7 | 6e-10 | 32/45 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 5e-07 | 32/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +4.7 | 5e-05 | 2/49 (CFPAC-1, MIA PaCa-2) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.09× | +3.6 | 0.006 | 3/48 (HS-578T, SNU-423, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 1.13× | +3.4 | 0.011 | 8/49 (J82, RKO, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.12× | +3.4 | 0.012 | 14/48 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 367.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.425×, RKO 0.496×; ⚠ cell-cycle shift, explains ~53% of this change); [[Tucidinostat (drug)]] 5 µM in 2 lines (SW1417 0.648×, SW480 0.732×); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.105×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change); [[Fluvoxamine (drug)]] 5 µM in 1 line (SW 1088 0.0815×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.803×** | -9.2 | 3e-17 | 32/48 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.753×** | -8.4 | 2e-14 | 34/49 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -4.8 | 3e-04 | 0/50 | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.889× | -3.5 | 0.070 | 5/48 (LoVo, NCI-H661, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.890× | -3.3 | 0.10 | 6/49 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift |
| [[Filgotinib (drug)]] 5 µM |  | 0.895× | -3.3 | 0.10 | 4/48 (AsPC-1, A549, …) | inconsistent across doses |  |
| [[Drospirenone (drug)]] 5 µM |  | 0.901× | -3.1 | 0.17 | 0/48 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 112 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +23.4) | — |
| [[PANC-1 (line)]] | alt | 132 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +20.4) | — |
| [[HOP62 (line)]] | alt | 104 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.41× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +12.9) | — |
| [[NCI-H23 (line)]] | alt | 161 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.40× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 98.3 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +19.6) | — |
| [[HS-578T (line)]] | alt | 128 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +14.4) | — |
| [[LoVo (line)]] | wt | 111 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +20.9) | — |
| [[KATO III (line)]] | alt | 91.0 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.60× (z +18.9) | — |
| [[LS 180 (line)]] | wt | 108 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +19.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 145 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 93.8 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.04× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +14.1) | — |
| [[H4 (line)]] | wt | 100 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 85.1 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +13.0) | — |
| [[RKO (line)]] | wt | 144 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.87× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 98.2 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +15.2) | [[Tucidinostat (drug)]] 5 µM 0.648× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 78.1 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +13.9) | — |
| [[BT-474 (line)]] | alt | 117 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +14.0) | — |
| [[HEC-1-A (line)]] | alt | 94.1 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 4.37× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 108 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.69× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 104 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +11.8) | — |
| [[A-427 (line)]] | wt | 133 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.74× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.425× (z -13.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A549 (line)]] | wt | 70.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.10× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 91.0 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.09× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 79.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 158 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.76× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 100 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 142 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.29× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 103 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +11.9) | — |
| [[SW48 (line)]] | wt | 134 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.66× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 102 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 122 | 2 (1 ⚠) | 0 | [[Lonafarnib (drug)]] 5 µM 3.58× (z +9.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 3.18× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 89.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.06× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.7) | — |
| [[A-172 (line)]] | wt | 68.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.44× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A498 (line)]] | wt | 84.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -26.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[HepG2_C3A (line)]] | wt | 106 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 95.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.6) | — |
| [[J82 (line)]] | alt | 113 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 163 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 88.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.49× (z +10.3) | — |
| [[RPMI-7951 (line)]] | alt | 97.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 127 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.92× (z +9.6) | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0815× (z -10.8) |
| [[AN3 CA (line)]] | alt | 152 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 99.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAGPA]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[FBXW11]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[UBE2L3]] | +0.61 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[DNAJC30]] | +0.60 | +0.36 / +0.61 | both halves | 1e-04 |  |
| [[MRPS15]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[GAPVD1]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[BICRA]] | +0.58 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[BABAM1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[FBXO36]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[PEX26]] | +0.56 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[USF3]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[CCDC142]] | +0.56 | +0.41 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP3]] | -0.60 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[SH3GL2]] | -0.53 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[SLFN11]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[CD83]] | -0.50 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[HMSD]] | -0.49 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[PTPRG-AS1]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ZNF184]] | -0.47 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[KDM1B]] | -0.47 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[CSRP1]] | -0.47 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[CYTH4]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[FSCN1]] | -0.46 | -0.52 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMSD]] | B | HMSD activity raises KPNA6's level | lines that do not express HMSD (26) vs lines expressing it (24) | 1.15× lower at baseline in the lines without HMSD | 0.066 | ⚠ within organs, on part of the lines; also absent: LGSN, LRRN2, HEYL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-13.2, -16.1); signed map (-41.5, -24.5). **Vector** length 77.8, 20.7% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +11.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +11.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.4 | +15.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +19.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +5.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -9.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.8 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.8 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.4 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.3 | +6.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.6 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | karyopherin subunit alpha 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:32,108,056-32,176,563 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IPOA7, KPNA7, MGC17918, FLJ11249 |
| Gene groups (HGNC) | Armadillo repeat containing; Importins |
| Reactome | 4 pathways, smallest: Assembly of the ORC complex at the origin of replication; Assembly of the pre-replicative complex; DNA Replication Pre-Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [O60684](https://www.uniprot.org/uniprotkb/O60684) (Importin subunit alpha-7):

> Functions in nuclear protein import as an adapter protein for nuclear receptor KPNB1. Binds specifically and directly to substrates containing either a simple or bipartite NLS motif. Docking of the importin/substrate complex to the nuclear pore complex (NPC) is mediated by KPNB1 through binding to nucleoporin FxFG repeats and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to importin-beta …

**Summary**, from NCBI Gene [23633](https://www.ncbi.nlm.nih.gov/gene/23633):

> Nucleocytoplasmic transport, a signal- and energy-dependent process, takes place through nuclear pore complexes embedded in the nuclear envelope. The import of proteins containing a nuclear localization signal (NLS) requires the NLS import receptor, a heterodimer of importin alpha and beta subunits also known as karyopherins. Importin alpha binds the NLS-containing cargo in the cytoplasm and importin beta docks the complex at the cytoplasmic side of the nuclear pore complex. In the presence of …

**Accessions** — [HGNC:6399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6399) · Entrez [23633](https://www.ncbi.nlm.nih.gov/gene/23633) · UniProt [O60684](https://www.uniprot.org/uniprotkb/O60684) · Ensembl [ENSG00000025800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000025800)

## Data

Gene col 367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 367); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 367]; `tensor/DDL_lfc|DDL_z.npy` [367]; `embed/gene_vectors.npy` [367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 367 or target_col == 367). Every well: [[KPNA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KPNA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
