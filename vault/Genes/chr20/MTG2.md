---
symbol: "MTG2"
type: "gene"
col: 2085
ensembl_id: "ENSG00000101181"
name: "mitochondrial ribosome associated GTPase 2"
location: "20q13.33"
module: 114
arm: "+"
pooled_cpm: 29.42
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# MTG2

*mitochondrial ribosome associated GTPase 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.19× (z +14.1, q 3e-42, up in 42 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +12.0, q 1e-30, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.658× (z -7.5, q 2e-11, down in 23 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.771× (z -4.9, q 2e-04, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMS1P4-1]] (+0.77, fdr 7e-06), [[ZNF721]] (+0.76, fdr 7e-06), [[AFG3L1P]] (+0.75, fdr 7e-06); moves opposite to [[CREG1]] (-0.65, fdr 1e-05), [[HDAC1]] (-0.61, fdr 3e-05), [[NPTN]] (-0.61, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HOXC8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2085.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +14.1 | 3e-42 | 42/45 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +12.0 | 1e-30 | 37/47 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +11.2 | 1e-26 | 36/47 (LOX-IMVI, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +9.0 | 4e-17 | 30/47 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.4 | 2e-08 | 33/48 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +6.0 | 2e-07 | 25/47 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.0 | 2e-07 | 27/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +5.5 | 3e-06 | 27/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 1e-05 | 20/47 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +5.1 | 2e-05 | 26/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.8 | 1e-04 | 23/47 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.010 | 10/48 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.020 | 13/48 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.023 | 11/32 (A-427, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.13× | +3.3 | 0.034 | 8/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.038 | 13/47 (SW1417, RPMI-7951, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.055 | 11/45 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2085.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -7.5 | 2e-11 | 23/37 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.716×** | -6.3 | 1e-07 | 26/44 (NCI-H23, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.771×** | -4.9 | 2e-04 | 22/48 (SW1417, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.779×** | -4.7 | 4e-04 | 22/48 (SW1417, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.787×** | -4.5 | 6e-04 | 20/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.779×** | -4.5 | 6e-04 | 21/46 (SHP-77, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -4.3 | 0.001 | 19/48 (A-172, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.4 | 0.047 | 17/48 (NCI-H23, SW1417, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.851× | -3.0 | 0.15 | 11/48 (C32, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2085. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 35.0 | 3 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.68× (z +11.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 41.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -11.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 61.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -17.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 35.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.93× (z +13.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -13.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 35.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.80× (z +8.8) ⚠ toxic | [[Niclosamide (olamine) (drug)]] 5 µM 0.321× (z -9.7) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 43.1 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.52× (z +10.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 28.8 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.46× (z +10.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 32.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -11.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 24.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 53.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -10.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.85× (z +10.4) ⚠ toxic | — |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.199× (z -8.9) |
| [[HOP62 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.98× (z +8.8) ⚠ toxic | — |
| [[HT-29 (line)]] | alt | 30.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.97× (z +12.5) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 22.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.26× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -18.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 30.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.413× (z -9.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.109× (z -9.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 61.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2085), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P4-1]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[ZNF721]] | +0.76 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[AFG3L1P]] | +0.75 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[ZCCHC10]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[DOHH]] | +0.71 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[RPP38]] | +0.70 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[ZNF3]] | +0.70 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[ZCCHC3]] | +0.70 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ZNF689]] | +0.70 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[ZNF7]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.69 | +0.73 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREG1]] | -0.65 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[HDAC1]] | -0.61 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[NPTN]] | -0.61 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[MPP1]] | -0.61 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[IDS]] | -0.60 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[MGAT4A]] | -0.59 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[SNX30]] | -0.59 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[LAMP2]] | -0.59 | -0.47 / -0.71 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC8]] | B | HOXC8 activity raises MTG2's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without HOXC8 | 0.019 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |
| [[HDAC6]] | B | HDAC6 activity raises MTG2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers MTG2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.851). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.4, 6.4); signed map (-3.8, -14.3). **Vector** length 107, 25.1% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +9.1 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +6.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.3 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +3.3 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.1 | -4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -7.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.0 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.0 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -1.7 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -2.3 | -2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosome associated GTPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,183,028-62,203,568 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10741, dJ1005F21.2, ObgH1; previously GTPBP5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4K7](https://www.uniprot.org/uniprotkb/Q9H4K7) (Mitochondrial ribosome-associated GTPase 2):

> Mitochondrial GTPase involved in biogenesis of the mitochondrial large ribosomal subunit (mt-LSU), particularly during its late-stage maturation. Required for formation of mature, translationally competent 55S mitoribosomes necessary for efficient mitochondrial translation. Cooperates with NSUN4 during mt-LSU biogenesis to promote structural rearrangements and folding of functionally important regions of 16S mitochondrial rRNA (16S mt-rRNA), facilitating MRM2-dependent methylation and …

**Summary**, from NCBI Gene [26164](https://www.ncbi.nlm.nih.gov/gene/26164):

> Small G proteins, such as GTPBP5, act as molecular switches that play crucial roles in the regulation of fundamental cellular processes such as protein synthesis, nuclear transport, membrane trafficking, and signal transduction (Hirano et al., 2006 [PubMed 17054726]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16239](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16239) · Entrez [26164](https://www.ncbi.nlm.nih.gov/gene/26164) · UniProt [Q9H4K7](https://www.uniprot.org/uniprotkb/Q9H4K7) · Ensembl [ENSG00000101181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101181)

## Data

Gene col 2085: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2085); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2085, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2085]; `tensor/DDL_lfc|DDL_z.npy` [2085]; `embed/gene_vectors.npy` [2085]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2085 or target_col == 2085). Every well: [[MTG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
