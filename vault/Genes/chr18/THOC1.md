---
symbol: "THOC1"
type: "gene"
col: 1241
ensembl_id: "ENSG00000079134"
name: "THO complex subunit 1"
location: "18p11.32"
module: 17
arm: "+"
pooled_cpm: 91.64
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# THOC1

*THO complex subunit 1* — 18p11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.27× (z +12.5, q 4e-33, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.488× (z -13.9, q 2e-41, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.671× (z -10.4, q 6e-23, down in 41 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS31P4]] (+0.74, fdr 7e-06), [[TTC26]] (+0.73, fdr 7e-06), [[TAMM41]] (+0.72, fdr 7e-06); moves opposite to [[ATP11C]] (-0.60, fdr 4e-05), [[DDX5]] (-0.59, fdr 1e-05), [[SFXN5]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NTN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1241.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.27×** | +12.5 | 4e-33 | 47/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.84×** | +12.4 | 1e-32 | 46/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +12.1 | 2e-31 | 39/48 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +9.8 | 2e-20 | 38/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.47×** | +9.6 | 1e-19 | 41/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +9.1 | 1e-17 | 41/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +7.9 | 2e-13 | 37/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +7.0 | 1e-10 | 31/48 (BT-474, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +7.0 | 2e-10 | 38/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +6.8 | 5e-10 | 33/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +6.0 | 1e-07 | 29/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +5.8 | 3e-07 | 29/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.2 | 9e-06 | 28/38 (NCI-H1573, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +4.7 | 9e-05 | 27/48 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.001 | 23/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.002 | 25/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.004 | 19/48 (LOX-IMVI, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.012 | 21/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1241.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -13.9 | 2e-41 | 39/44 (SK-MEL-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -10.4 | 6e-23 | 41/49 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.620×** | -9.7 | 8e-20 | 39/49 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.759×** | -7.6 | 6e-12 | 35/48 (A-427, SNU-423, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.798×** | -4.4 | 0.001 | 27/50 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.828×** | -3.7 | 0.023 | 22/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -3.4 | 0.054 | 0/50 | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.847× | -3.4 | 0.055 | 15/48 (PANC-1, RKO, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 0.851× | -3.3 | 0.068 | 18/48 (A-172, C32, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.854× | -3.2 | 0.077 | 17/48 (hTERT-HPNE, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 80.7 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.01× (z +17.0) | — |
| [[NCI-H460 (line)]] | wt | 63.1 | 8 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -11.9) |
| [[SW480 (line)]] | alt | 103 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 153 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -12.3) |
| [[HOP62 (line)]] | alt | 173 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -8.7) |
| [[RKO (line)]] | wt | 125 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -14.7) |
| [[BT-474 (line)]] | alt | 136 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +11.1) | — |
| [[LoVo (line)]] | wt | 75.9 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 129 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.56× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -11.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 111 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.10× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -17.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 98.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.5) | — |
| [[A-427 (line)]] | wt | 210 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.473× (z -13.6) |
| [[HEC-1-A (line)]] | alt | 92.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 139 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.72× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 80.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 89.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.102× (z -20.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 122 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -20.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 70.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.8) |
| [[HCT15 (line)]] | alt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -18.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 79.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.63× (z +8.7) | — |
| [[J82 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -14.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 90.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.67× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 78.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 97.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.6) | — |
| [[SW48 (line)]] | wt | 130 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -12.2) |
| [[A549 (line)]] | wt | 72.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 53.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +8.5) | — |
| [[C32 (line)]] | wt | 80.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -10.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -9.9) |
| [[COLO 205 (line)]] | alt | 37.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 68.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 52.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 85.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 71.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 57.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +11.0) | — |
| [[SW 1271 (line)]] | alt | 76.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.109× (z -9.2) |
| [[A498 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 94.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P4]] | +0.74 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TTC26]] | +0.73 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[TAMM41]] | +0.72 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[UBXN2B]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[NIPSNAP2]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[DDX19B]] | +0.66 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PRPF39]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[DDX55]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MRPS31P5-1]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ZNF45]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SAAL1]] | +0.63 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ESD]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP11C]] | -0.60 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[DDX5]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SFXN5]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[LRP10]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[LINC00393]] | -0.54 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[PRDX1]] | -0.54 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[LINC00880]] | -0.54 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[ABHD5]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[CFL1]] | -0.53 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SLC6A13]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ARSB]] | -0.52 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[SAXO1]] | -0.52 | -0.43 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN4]] | B | NTN4 activity lowers THOC1's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.57× higher at baseline in the lines without NTN4 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[TOP2A]] | B | TOP2A activity raises THOC1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.4% of all compounds | 0.004 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises THOC1's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.0, -2.3); signed map (-21.9, -15.0). **Vector** length 90.3, 25.9% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intraflagellar transport* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | -13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | -9.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | -1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -3.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.7 | -0.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | THO complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32 — chr18:214,520-268,050 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P84, HPR1 |
| Gene groups (HGNC) | THO complex |
| Reactome | 5 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FV9](https://www.uniprot.org/uniprotkb/Q96FV9) (THO complex subunit 1):

> Component of the THO subcomplex of the TREX complex which is thought to couple mRNA transcription, processing and nuclear export, and which specifically associates with spliced mRNA and not with unspliced pre-mRNA. Required for efficient export of polyadenylated RNA. The THOC1-THOC2-THOC3 core complex alone is sufficient to bind export factor NXF1-NXT1 and promote ATPase activity of DDX39B/UAP56. TREX is recruited to spliced mRNAs by a transcription-independent mechanism, binds to mRNA upstream …

**Summary**, from NCBI Gene [9984](https://www.ncbi.nlm.nih.gov/gene/9984):

> Enables identical protein binding activity. Involved in mRNA export from nucleus. Located in chromosome, telomeric region; cytoplasm; and nuclear speck. Part of THO complex part of transcription export complex. Implicated in autosomal dominant nonsyndromic deafness 86. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19070) · Entrez [9984](https://www.ncbi.nlm.nih.gov/gene/9984) · UniProt [Q96FV9](https://www.uniprot.org/uniprotkb/Q96FV9) · Ensembl [ENSG00000079134](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079134)

## Data

Gene col 1241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1241); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1241]; `tensor/DDL_lfc|DDL_z.npy` [1241]; `embed/gene_vectors.npy` [1241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1241 or target_col == 1241). Every well: [[THOC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THOC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
