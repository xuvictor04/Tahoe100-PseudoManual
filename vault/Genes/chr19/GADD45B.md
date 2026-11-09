---
symbol: "GADD45B"
type: "gene"
col: 1821
ensembl_id: "ENSG00000099860"
name: "growth arrest and DNA damage inducible beta"
location: "19p13.3"
module: 113
arm: "+"
pooled_cpm: 43.46
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# GADD45B

*growth arrest and DNA damage inducible beta* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 18.0× (z +28.4, q 0e+00, up in 46 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB10]] (+0.63, fdr 7e-06), [[PER1]] (+0.60, fdr 7e-06), [[NFKBIA]] (+0.59, fdr 1e-05); moves opposite to [[MCM9]] (-0.58, fdr 1e-05), [[TOMM40]] (-0.57, fdr 2e-05), [[HERC2]] (-0.56, fdr 1e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **18.0×** | +28.4 | 0e+00 | 46/46 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **10.5×** | +16.3 | 0e+00 | 45/46 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **11.6×** | +16.3 | 0e+00 | 45/47 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.88×** | +11.0 | 7e-26 | 45/46 (SNU-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **4.46×** | +10.4 | 4e-23 | 46/47 (SNU-1, SW48, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +10.2 | 2e-22 | 46/46 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **4.33×** | +10.2 | 3e-22 | 36/45 (NCI-H460, LoVo, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.41×** | +8.5 | 1e-15 | 40/47 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.28×** | +8.2 | 1e-14 | 36/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.40×** | +8.2 | 2e-14 | 38/45 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.86×** | +7.3 | 2e-11 | 39/47 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +6.3 | 1e-08 | 42/47 (KATO III, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.68×** | +6.3 | 1e-08 | 32/40 (LoVo, NCI-H1573, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.60×** | +6.2 | 2e-08 | 43/48 (SNU-1, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.35×** | +5.9 | 1e-07 | 35/47 (SW480, KATO III, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.77×** | +4.0 | 0.002 | 33/47 (SNU-1, SW48, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.009 | 30/47 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.033 | 24/47 (LS 180, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.36×** | +3.1 | 0.041 | 22/46 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.045 | 26/47 (J82, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +3.0 | 0.050 | 27/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1821.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.853× | -3.9 | 0.056 | 20/48 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.78 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.1 | 15 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +18.0) | — |
| [[SW480 (line)]] | alt | 32.3 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +17.3) | — |
| [[SNU-1 (line)]] | wt | 68.9 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +19.4) | — |
| [[SW48 (line)]] | wt | 46.2 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +16.1) | — |
| [[KATO III (line)]] | alt | 18.4 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 29.5× (z +24.6) | — |
| [[C32 (line)]] | wt | 35.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 129× (z +22.8) | — |
| [[AsPC-1 (line)]] | alt | 45.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.1× (z +30.7) | — |
| [[HEC-1-A (line)]] | alt | 26.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +22.0) | — |
| [[NCI-H1573 (line)]] | alt | 31.2 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.6× (z +19.6) | — |
| [[PANC-1 (line)]] | alt | 58.8 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +25.2) | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.0× (z +19.2) | — |
| [[SW 900 (line)]] | alt | 26.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 38.6× (z +21.2) | — |
| [[A-427 (line)]] | wt | 32.4 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.92× (z +11.6) | — |
| [[LoVo (line)]] | wt | 18.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +14.6) | — |
| [[LOX-IMVI (line)]] | wt | 54.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.20× (z +19.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.8× (z +19.7) | — |
| [[NCI-H1792 (line)]] | alt | 26.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 61.6× (z +21.1) | — |
| [[NCI-H23 (line)]] | alt | 23.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +21.5) | — |
| [[SW1417 (line)]] | alt | 99.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +24.0) | — |
| [[A-172 (line)]] | wt | 91.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +19.3) | — |
| [[BT-474 (line)]] | alt | 19.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 34.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.4× (z +21.1) | — |
| [[HS-578T (line)]] | alt | 84.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +15.0) | — |
| [[LS 180 (line)]] | wt | 26.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 43.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +22.8) | — |
| [[RPMI-7951 (line)]] | alt | 58.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +14.8) | — |
| [[A498 (line)]] | wt | 48.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.9× (z +24.6) | — |
| [[A549 (line)]] | wt | 30.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +19.2) | — |
| [[H4 (line)]] | wt | 24.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.4× (z +15.0) | — |
| [[HepG2_C3A (line)]] | wt | 56.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +17.3) | — |
| [[hTERT-HPNE (line)]] | wt | 54.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 70.9× (z +22.6) | — |
| [[J82 (line)]] | alt | 63.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +20.3) | — |
| [[NCI-H2030 (line)]] | alt | 54.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.6× (z +18.9) | — |
| [[NCI-H2347 (line)]] | alt | 86.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +20.2) | — |
| [[CFPAC-1 (line)]] | alt | 81.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +24.4) | — |
| [[HT-29 (line)]] | alt | 20.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +16.0) | — |
| [[SHP-77 (line)]] | alt | 17.0 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.80× (z +9.8) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 99.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +18.8) | — |
| [[C-33 A (line)]] | alt | 15.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 31.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.95× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 39.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +17.6) | — |
| [[RKO (line)]] | wt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +11.0) | — |
| [[SW 1088 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.6× (z +10.8) | — |
| [[SW 1271 (line)]] | alt | 60.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.4× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB10]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PER1]] | +0.60 | +0.62 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[NFKBIA]] | +0.59 | +0.75 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 648 |
| [[PPP1R15A]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 642 |
| [[GCH1]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_APOPTOSIS |
| [[PNRC1]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CDKN1C]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[KLF6]] | +0.56 | +0.63 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 414 |
| [[BCL6]] | +0.56 | +0.48 / +0.59 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[ZFP36L1]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[IFRD1]] | +0.56 | +0.61 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_MYOGENESIS; STRING 490 |
| [[MAFF]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM9]] | -0.58 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[TOMM40]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[HERC2]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[MTAP]] | -0.55 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[RNGTT]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ARMC6]] | -0.54 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[MRPS27]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[RAB28]] | -0.54 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[ZDHHC5]] | -0.53 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[BLTP2]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[NUP50]] | -0.52 | -0.56 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.443). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.2, -3.6); signed map (14.5, 27.8). **Vector** length 88.5, 29.9% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +28.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.1 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | +1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | growth arrest and DNA damage inducible beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,476,122-2,478,259 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GADD45BETA, DKFZP566B133; previously MYD118 |
| Gene groups (HGNC) | Growth arrest and DNA damage inducible family |
| Hallmark sets | MYOGENESIS, APOPTOSIS, IL2_STAT5_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [O75293](https://www.uniprot.org/uniprotkb/O75293) (Growth arrest and DNA damage-inducible protein GADD45 beta):

> Involved in the regulation of growth and apoptosis. Mediates activation of stress-responsive MTK1/MEKK4 MAPKKK.

**Summary**, from NCBI Gene [4616](https://www.ncbi.nlm.nih.gov/gene/4616):

> This gene is a member of a group of genes whose transcript levels are increased following stressful growth arrest conditions and treatment with DNA-damaging agents. The genes in this group respond to environmental stresses by mediating activation of the p38/JNK pathway. This activation is mediated via their proteins binding and activating MTK1/MEKK4 kinase, which is an upstream activator of both p38 and JNK MAPKs. The function of these genes or their protein products is involved in the …

**Accessions** — [HGNC:4096](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4096) · Entrez [4616](https://www.ncbi.nlm.nih.gov/gene/4616) · UniProt [O75293](https://www.uniprot.org/uniprotkb/O75293) · Ensembl [ENSG00000099860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099860)

## Data

Gene col 1821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1821); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1821]; `tensor/DDL_lfc|DDL_z.npy` [1821]; `embed/gene_vectors.npy` [1821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1821 or target_col == 1821). Every well: [[GADD45B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GADD45B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
