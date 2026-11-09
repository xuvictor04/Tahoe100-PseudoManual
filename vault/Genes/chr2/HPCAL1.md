---
symbol: "HPCAL1"
type: "gene"
col: 3715
ensembl_id: "ENSG00000115756"
name: "hippocalcin like 1"
location: "2p25.1"
module: 174
arm: "+"
pooled_cpm: 179.16
n_lines_expressing: 44
n_dd_up: 6
n_dd_down: 41
n_dd_up_clean: 6
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 21
direction_downstream: 4
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# HPCAL1

*hippocalcin like 1* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.63× (z +18.9, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.485× (z -20.0, q 0e+00, down in 33 of 43 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIBAN2]] (+0.76, fdr 7e-06), [[SLC20A1]] (+0.72, fdr 7e-06), [[PHC2]] (+0.71, fdr 7e-06); moves opposite to [[KLRK1-AS1]] (-0.61, fdr 4e-04), [[DNAI4]] (-0.60, fdr 2e-04), [[NEXN]] (-0.60, fdr 1e-04).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TGM2]] → it (grade B ⚠); 4 go from it, the strongest it → [[PC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.63×** | +18.9 | 0e+00 | 38/42 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +15.7 | 0e+00 | 35/42 (SW1417, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +14.9 | 0e+00 | 34/42 (SW1417, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +7.8 | 8e-13 | 27/42 (SW1417, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.006 | 17/43 (SW1417, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.026 | 23/42 (SW480, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.18× | +3.2 | 0.13 | 18/43 (PANC-1, COLO 205, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.485×** | -20.0 | 0e+00 | 33/43 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.506×** | -18.8 | 0e+00 | 34/42 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.515×** | -12.5 | 1e-33 | 32/41 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -12.4 | 2e-33 | 33/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.581×** | -10.6 | 3e-24 | 35/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.626×** | -9.9 | 3e-21 | 32/44 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.604×** | -9.9 | 5e-21 | 30/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.654×** | -9.1 | 9e-18 | 37/42 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.666×** | -8.0 | 1e-13 | 29/43 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.689×** | -7.3 | 2e-11 | 29/43 (COLO 205, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.683×** | -7.2 | 4e-11 | 25/41 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.710×** | -7.1 | 6e-11 | 30/42 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.686×** | -7.1 | 6e-11 | 27/37 (A549, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.700×** | -7.0 | 1e-10 | 27/41 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -6.9 | 2e-10 | 30/44 (SW 900, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.696×** | -6.8 | 3e-10 | 30/42 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.780×** | -6.7 | 6e-10 | 24/42 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.738×** | -6.6 | 1e-09 | 30/43 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 70.2 | 18 | 2 | [[Clobetasol propionate (drug)]] 0.05 µM 3.88× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.1) |
| [[HOP62 (line)]] | alt | 548 | 0 | 16 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -17.2) |
| [[SK-MEL-2 (line)]] | alt | 210 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -20.8) |
| [[A498 (line)]] | wt | 336 | 3 | 10 (3 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.07× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -29.9) |
| [[PANC-1 (line)]] | alt | 300 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -32.9) |
| [[SW 900 (line)]] | alt | 350 | 0 | 13 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -25.0) |
| [[KATO III (line)]] | alt | 179 | 3 | 7 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 196 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 513 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -24.2) |
| [[HS-578T (line)]] | alt | 106 | 3 | 6 | [[Panobinostat (drug)]] 5 µM 3.49× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 140 | 3 | 6 | [[Panobinostat (drug)]] 5 µM 2.70× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -22.8) |
| [[A549 (line)]] | wt | 195 | 2 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -20.0) |
| [[Panc 03.27 (line)]] | alt | 226 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -21.7) |
| [[NCI-H2030 (line)]] | alt | 141 | 3 | 4 | [[Panobinostat (drug)]] 5 µM 3.08× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -21.3) |
| [[SW480 (line)]] | alt | 203 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -11.7) |
| [[A-427 (line)]] | wt | 63.2 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 2.92× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -22.4) |
| [[MIA PaCa-2 (line)]] | alt | 272 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -26.8) |
| [[SW1417 (line)]] | alt | 89.5 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 4.80× (z +16.9) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.495× (z -10.6) |
| [[COLO 205 (line)]] | alt | 237 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -17.4) |
| [[HCT15 (line)]] | alt | 195 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 45.3 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 248 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -20.9) |
| [[J82 (line)]] | alt | 82.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.63× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 216 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.516× (z -19.2) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 355 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.7) |
| [[A-172 (line)]] | wt | 104 | 2 | 1 | [[Belinostat (drug)]] 5 µM 2.57× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -8.6) |
| [[BT-474 (line)]] | alt | 114 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 2.28× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 88.8 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 2.52× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 46.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.33× (z +12.8) | — |
| [[AN3 CA (line)]] | alt | 69.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0785× (z -13.2) |
| [[H4 (line)]] | wt | 71.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 116 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -12.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -8.9) |
| [[LS 180 (line)]] | wt | 82.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +12.9) | — |
| [[RKO (line)]] | wt | 105 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 285 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -14.8) |
| [[SHP-77 (line)]] | alt | 90.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 118 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -10.6) |
| [[SW48 (line)]] | wt | 76.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 38.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 38.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 42.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 43.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIBAN2]] | +0.76 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[SLC20A1]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[PHC2]] | +0.71 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ABTB3]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ZFYVE28]] | +0.69 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[ETV5]] | +0.68 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SLCO4A1]] | +0.68 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TBC1D8]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[PTPN12]] | +0.67 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[FLNB]] | +0.66 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[DUSP5]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[RASA3]] | +0.65 | +0.65 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRK1-AS1]] | -0.61 | -0.57 / -0.24 | both halves | 4e-04 |  |
| [[DNAI4]] | -0.60 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[NEXN]] | -0.60 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[TBC1D22B]] | -0.60 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[PIGP]] | -0.59 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[AEBP2]] | -0.59 | -0.59 / -0.26 | both halves | 4e-04 |  |
| [[GALNT7-DT]] | -0.59 | -0.58 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[DRAM1]] | -0.59 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[RC3H2]] | -0.59 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[DUSP16]] | -0.59 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PLS3-AS1]] | -0.58 | -0.62 / -0.28 | both halves | 3e-04 |  |
| [[HDAC2-AS2]] | -0.58 | -0.61 / -0.30 | both halves | 2e-04 |  |
| [[AHI1-DT]] | -0.58 | -0.57 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 18, C 3. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGM2]] | B | TGM2 activity raises HPCAL1's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 2.47× lower at baseline in the lines without TGM2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[PLEK2]] | B | PLEK2 activity raises HPCAL1's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without PLEK2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[S100A16]] | B | S100A16 activity raises HPCAL1's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without S100A16 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[SMOX]] | B | SMOX activity raises HPCAL1's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without SMOX | 0.021 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises HPCAL1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.7% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ROR1]] | B | ROR1 activity raises HPCAL1's level | lines that do not express ROR1 (14) vs lines expressing it (36) | 1.92× lower at baseline in the lines without ROR1 | 0.031 | ⚠ within organs, on part of the lines |
| [[RIPK4]] | B | RIPK4 activity raises HPCAL1's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 2.14× lower at baseline in the lines without RIPK4 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[CLMN]] | B | CLMN activity raises HPCAL1's level | lines that do not express CLMN (7) vs lines expressing it (43) | 2.37× lower at baseline in the lines without CLMN | 0.036 | ⚠ within organs, on part of the lines; also absent: ITPR3, NABP1, HTATIP2; maybe low, not absent |
| [[LAPTM5]] | B | LAPTM5 activity raises HPCAL1's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 1.78× lower at baseline in the lines without LAPTM5 | 0.045 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2 |
| [[HDAC6]] | B | HDAC6 activity lowers HPCAL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises HPCAL1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RAC2]] | B | RAC2 activity raises HPCAL1's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.77× lower at baseline in the lines without RAC2 | 0.073 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PC]] | B | HPCAL1 activity raises PC's level | lines that do not express HPCAL1 (6) vs lines expressing it (44) | 2.86× lower at baseline in the lines without HPCAL1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SHB, ARMCX3, ECE1; maybe low, not absent |
| cells under [[Tofacitinib (drug)]] 0.05 µM | B | HPCAL1 activity raises the cells' numbers under Tofacitinib 0.05 µM (protects the cells) | lines that do not express HPCAL1 (6) vs lines expressing it (42) | the lines without HPCAL1: 0.86× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: SHB, ARMCX3, ECE1; maybe low, not absent |
| [[SLCO4A1]] | B | HPCAL1 activity raises SLCO4A1's level | lines that do not express HPCAL1 (6) vs lines expressing it (44) | 3.21× lower at baseline in the lines without HPCAL1 | 0.084 | ⚠ within organs, on part of the lines; also absent: SHB, ARMCX3, ECE1; maybe low, not absent |
| [[GNAI2]] | B | HPCAL1 activity raises GNAI2's level | lines that do not express HPCAL1 (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without HPCAL1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SHB, ARMCX3, ECE1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.5, 4.4); signed map (4.3, 50.3). **Vector** length 149, 50.3% of its response variance represented; |z| ≥ 3 in 1,693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +10.2 | +18.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +10.2 | +14.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +9.8 | +15.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.6 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.9 | +1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.7 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.7 | -18.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -9.6 | -9.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -9.2 | -9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.1 | -20.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.9 | -7.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.4 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.1 | -6.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -7.8 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | hippocalcin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:10,302,889-10,427,617 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BDR1, HLP2, VILIP-3 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P37235](https://www.uniprot.org/uniprotkb/P37235) (Hippocalcin-like protein 1):

> May be involved in the calcium-dependent regulation of rhodopsin phosphorylation.

**Summary**, from NCBI Gene [3241](https://www.ncbi.nlm.nih.gov/gene/3241):

> The protein encoded by this gene is a member of neuron-specific calcium-binding proteins family found in the retina and brain. It is highly similar to human hippocalcin protein and nearly identical to the rat and mouse hippocalcin like-1 proteins. It may be involved in the calcium-dependent regulation of rhodopsin phosphorylation and may be of relevance for neuronal signalling in the central nervous system. Several alternatively spliced transcript variants encoding the same protein have been …

**Accessions** — [HGNC:5145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5145) · Entrez [3241](https://www.ncbi.nlm.nih.gov/gene/3241) · UniProt [P37235](https://www.uniprot.org/uniprotkb/P37235) · Ensembl [ENSG00000115756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115756)

## Data

Gene col 3715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3715); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3715]; `tensor/DDL_lfc|DDL_z.npy` [3715]; `embed/gene_vectors.npy` [3715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3715 or target_col == 3715). Every well: [[HPCAL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPCAL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
