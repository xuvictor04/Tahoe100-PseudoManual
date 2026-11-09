---
symbol: "ARGLU1"
type: "gene"
col: 5620
ensembl_id: "ENSG00000134884"
name: "arginine and glutamate rich 1"
location: "13q33.3"
module: 21
arm: "+"
pooled_cpm: 146.65
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ARGLU1

*arginine and glutamate rich 1* — 13q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.15× (z +14.1, q 4e-42, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.03× (z +13.0, q 3e-36, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.630× (z -8.5, q 9e-15, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRSF5]] (+0.67, fdr 4e-05), [[ANKRD10]] (+0.66, fdr 1e-05), [[HOXB-AS3]] (+0.65, fdr 2e-05); moves opposite to [[MRPL10]] (-0.61, fdr 3e-05), [[MLX]] (-0.60, fdr 3e-05), [[SNAPC2]] (-0.58, fdr 6e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +14.1 | 4e-42 | 48/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +13.0 | 3e-36 | 48/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +10.7 | 2e-24 | 42/45 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.77×** | +10.5 | 2e-23 | 45/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.69×** | +9.6 | 7e-20 | 45/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +9.4 | 4e-19 | 45/49 (SW480, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +8.3 | 8e-15 | 42/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +8.2 | 1e-14 | 35/49 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.5 | 3e-12 | 30/49 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.2 | 4e-11 | 30/44 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.36×** | +5.6 | 9e-07 | 33/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +5.1 | 1e-05 | 31/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.9 | 3e-05 | 31/50 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 6e-05 | 34/48 (J82, LoVo, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.8 | 6e-05 | 23/48 (SW480, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 2e-04 | 27/48 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.5 | 3e-04 | 28/48 (SHP-77, C32, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 25/48 (RPMI-7951, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.8 | 0.004 | 16/48 (LS 180, RKO, …) | rises with dose | position effect removed |
| [[Oxaliplatin (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.005 | 24/48 (SW480, LoVo, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.630×** | -8.5 | 9e-15 | 40/48 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.687×** | -6.9 | 1e-09 | 37/48 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.719×** | -6.1 | 2e-07 | 31/48 (J82, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.829×** | -3.5 | 0.075 | 23/49 (NCI-H661, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.832×** | -3.4 | 0.078 | 19/48 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.837× | -3.3 | 0.090 | 15/48 (HCT15, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 85.9 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.62× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +13.7) | — |
| [[C32 (line)]] | wt | 86.0 | 7 (3 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 8.62× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 115 | 7 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.10× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 171 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 124 | 6 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.9) | — |
| [[SW48 (line)]] | wt | 157 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +10.5) | — |
| [[SW480 (line)]] | alt | 339 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.65× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 389 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.95× (z +12.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +10.1) | — |
| [[KATO III (line)]] | alt | 207 | 4 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.65× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.506× (z -9.1) |
| [[LoVo (line)]] | wt | 173 | 4 (2 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.45× (z +12.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.533× (z -9.0) |
| [[HT-29 (line)]] | alt | 249 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.19× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.92× (z +9.2) | — |
| [[A498 (line)]] | wt | 122 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.485× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 160 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.89× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.525× (z -9.1) |
| [[J82 (line)]] | alt | 229 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.441× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 180 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.39× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 299 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.66× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.1) | — |
| [[SW 900 (line)]] | alt | 112 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.97× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +10.2) | — |
| [[A-172 (line)]] | wt | 88.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +10.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 54.1 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.34× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 144 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.80× (z +8.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 151 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 116 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 91.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.18× (z +11.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 67.2 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.60× (z +9.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.41× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 84.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.5) | — |
| [[NCI-H596 (line)]] | alt | 192 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.199× (z -8.7) |
| [[RKO (line)]] | wt | 184 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.07× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 242 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.41× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 88.6 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0691× (z -10.0) |
| [[SW 1271 (line)]] | alt | 66.4 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0695× (z -10.3) |
| [[A-427 (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 99.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 213 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 83.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF5]] | +0.67 | +0.42 / +0.58 | both halves | 4e-05 | STRING 505 |
| [[ANKRD10]] | +0.66 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[HOXB-AS3]] | +0.65 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[CCNL2]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[HNRNPK-AS1]] | +0.60 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[RPL41]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[NIPBL-DT]] | +0.58 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[RAD51-AS1]] | +0.57 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[GOLGA8A]] | +0.57 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[HOXB6]] | +0.56 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[PABPN1]] | +0.56 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[HOTAIR]] | +0.56 | +0.43 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL10]] | -0.61 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[MLX]] | -0.60 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SNAPC2]] | -0.58 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[ISCA2]] | -0.58 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[MYG1]] | -0.58 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[TWF2]] | -0.58 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[NOA1]] | -0.57 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[LTN1]] | -0.55 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[MRPL17]] | -0.55 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[MEA1]] | -0.55 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[PUSL1]] | -0.54 | -0.24 / -0.40 | both halves | 5e-04 |  |
| [[SNAPIN]] | -0.53 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARGLU1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises ARGLU1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.389). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.8, 25.2); signed map (32.4, -16.9). **Vector** length 109, 34.0% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +1.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.8 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | -0.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.9 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -0.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.1 | +0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.9 | +0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | arginine and glutamate rich 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.3 — chr13:106,541,673-106,568,137 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10154 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWB6](https://www.uniprot.org/uniprotkb/Q9NWB6) (Arginine and glutamate-rich protein 1):

> Dual function regulator of gene expression; regulator of transcription and modulator of alternative splicing. General coactivator of nuclear receptor-induced gene expression, including genes activated by the glucocorticoid receptor NR3C1. Binds to a subset of pre-mRNAs and to components of the spliceosome machinery to directly modulate basal alternative splicing; involved in simple and complex cassette exon splicing events. Binds its own pre-mRNA and regulates its alternative splicing and …

**Summary**, from NCBI Gene [55082](https://www.ncbi.nlm.nih.gov/gene/55082):

> Enables pre-mRNA binding activity and transcription coactivator activity. Involved in regulation of alternative mRNA splicing, via spliceosome. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25482) · Entrez [55082](https://www.ncbi.nlm.nih.gov/gene/55082) · UniProt [Q9NWB6](https://www.uniprot.org/uniprotkb/Q9NWB6) · Ensembl [ENSG00000134884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134884)

## Data

Gene col 5620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5620); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5620]; `tensor/DDL_lfc|DDL_z.npy` [5620]; `embed/gene_vectors.npy` [5620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5620 or target_col == 5620). Every well: [[ARGLU1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARGLU1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
