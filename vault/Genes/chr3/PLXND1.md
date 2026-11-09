---
symbol: "PLXND1"
type: "gene"
col: 43
ensembl_id: "ENSG00000004399"
name: "plexin D1"
location: "3q22.1"
module: 23
arm: "-"
pooled_cpm: 27.76
n_lines_expressing: 43
n_dd_up: 11
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PLXND1

*plexin D1* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.63× (z +8.5, q 2e-14, up in 19 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.31× (z +4.7, q 4e-04, up in 12 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.388× (z -23.0, q 0e+00, down in 36 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL18A1]] (+0.65, fdr 1e-05), [[NCOR2]] (+0.64, fdr 1e-05), [[LPCAT4]] (+0.63, fdr 4e-05); moves opposite to [[SBF2-AS1]] (-0.65, fdr 3e-05), [[KRBOX5]] (-0.65, fdr 5e-05), [[THAP6]] (-0.63, fdr 4e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF441]] → it (grade B ⚠); 4 go from it, the strongest it → [[ZNF441]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 43.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +8.5 | 2e-14 | 19/33 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.2 | 9e-08 | 16/26 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +6.2 | 9e-08 | 14/30 (A-427, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +4.7 | 4e-04 | 12/40 (A-172, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +4.4 | 0.001 | 20/40 (NCI-H460, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 0.002 | 15/40 (NCI-H460, H4, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.9 | 0.006 | 12/36 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.007 | 13/41 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.23×** | +3.6 | 0.017 | 13/41 (NCI-H2347, H4, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.23×** | +3.6 | 0.020 | 12/41 (NCI-H2347, H4, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.5 | 0.020 | 11/41 (MIA PaCa-2, A-172, …) | two highest doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.3 | 0.042 | 6/31 (J82, A498, …) | top dose only | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.11 | 8/39 (HS-578T, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 43.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.388×** | -23.0 | 0e+00 | 36/40 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.359×** | -17.7 | 0e+00 | 36/39 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.372×** | -16.4 | 0e+00 | 30/40 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.577×** | -13.4 | 2e-38 | 32/38 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.495×** | -12.1 | 7e-32 | 31/41 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.566×** | -9.8 | 1e-20 | 27/40 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.643×** | -7.6 | 2e-12 | 21/41 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -7.1 | 1e-10 | 22/36 (Panc 03.27, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -6.3 | 3e-08 | 19/39 (KATO III, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -5.5 | 3e-06 | 18/41 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -4.7 | 1e-04 | 2/41 (COLO 205, SW 1271) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.593×** | -4.7 | 1e-04 | 18/40 (SK-MEL-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.762×** | -4.7 | 1e-04 | 17/40 (SNU-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -4.6 | 2e-04 | 18/40 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.771×** | -4.5 | 3e-04 | 16/39 (HT-29, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -4.3 | 5e-04 | 17/39 (HT-29, LoVo, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.637×** | -4.1 | 0.001 | 12/39 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.657×** | -3.8 | 0.005 | 13/38 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 43. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.6 | 0 | 16 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -17.5) |
| [[HT-29 (line)]] | alt | 53.1 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0688× (z -28.2) |
| [[LoVo (line)]] | wt | 34.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -26.7) |
| [[A-427 (line)]] | wt | 32.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -16.9) |
| [[HOP62 (line)]] | alt | 33.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 10.3 | 2 (1 ⚠) | 2 | [[Ixazomib citrate (drug)]] 5 µM 4.03× (z +10.2) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.45× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -12.2) |
| [[RKO (line)]] | wt | 25.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -14.0) |
| [[A498 (line)]] | wt | 84.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -13.9) |
| [[KATO III (line)]] | alt | 11.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 44.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0708× (z -13.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 62.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.4) |
| [[SW 900 (line)]] | alt | 18.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -10.9) |
| [[A-172 (line)]] | wt | 112 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -14.6) |
| [[J82 (line)]] | alt | 19.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.2) |
| [[PANC-1 (line)]] | alt | 50.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.437× (z -9.0) |
| [[C32 (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -9.9) |
| [[Hs 766T (line)]] | wt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -11.1) |
| [[HS-578T (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.369× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0748× (z -13.5) |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0730× (z -8.6) |
| [[SNU-423 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.2) |
| [[SW48 (line)]] | wt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -9.8) |
| [[A549 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.94 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 43), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL18A1]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[NCOR2]] | +0.64 | +0.61 / +0.51 | both halves | 1e-05 | pathway: Signaling by NOTCH |
| [[LPCAT4]] | +0.63 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[ABCA2]] | +0.63 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[IQSEC1]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[TCF3]] | +0.61 | +0.64 / +0.36 | both halves | 1e-04 |  |
| [[ST6GALNAC4]] | +0.60 | +0.68 / +0.26 | both halves | 4e-04 |  |
| [[APMAP]] | +0.60 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[DNM1]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[KIAA0930]] | +0.58 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SPATA13]] | +0.58 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[PARP1]] | +0.58 | +0.41 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBF2-AS1]] | -0.65 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[KRBOX5]] | -0.65 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[THAP6]] | -0.63 | -0.69 / -0.41 | both halves | 4e-05 |  |
| [[ZNF563]] | -0.63 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[ZNF407-AS1]] | -0.61 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[NMNAT1]] | -0.61 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[METTL6]] | -0.61 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[SMIM19]] | -0.61 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[OXA1L-DT]] | -0.60 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[BCDIN3D]] | -0.60 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[RC3H2]] | -0.60 | -0.66 / -0.32 | both halves | 2e-04 |  |
| [[SENP8]] | -0.60 | -0.60 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF441]] | B | ZNF441 activity raises PLXND1's level | lines that do not express ZNF441 (7) vs lines expressing it (43) | 2.66× lower at baseline in the lines without ZNF441 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000286098, ZNF442, ZNF433 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PLXND1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[PSMB5]] | B | PSMB5 activity lowers PLXND1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF441]] | B | PLXND1 activity raises ZNF441's level | lines that do not express PLXND1 (7) vs lines expressing it (43) | 3.30× lower at baseline in the lines without PLXND1 | 0.015 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ZNF627]] | B | PLXND1 activity raises ZNF627's level | lines that do not express PLXND1 (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without PLXND1 | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FOXK1]] | B | PLXND1 activity raises FOXK1's level | lines that do not express PLXND1 (7) vs lines expressing it (43) | 1.48× lower at baseline in the lines without PLXND1 | 0.080 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RC3H2]] | B | PLXND1 activity raises RC3H2's level | lines that do not express PLXND1 (7) vs lines expressing it (43) | 1.27× lower at baseline in the lines without PLXND1 | 0.093 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.9, 12.0); signed map (-14.5, 33.2). **Vector** length 98.8, 22.1% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.0 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.2 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.2 | +3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -17.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -12.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -23.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -16.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | plexin D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:129,555,214-129,606,676 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0620 |
| Gene groups (HGNC) | Plexins; IPT domain containing |
| Reactome | 11 pathways, smallest: Other semaphorin interactions; NOTCH3 Intracellular Domain Regulates Transcription; RND2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4D7](https://www.uniprot.org/uniprotkb/Q9Y4D7) (Plexin-D1):

> Cell surface receptor for SEMA4A and for class 3 semaphorins, such as SEMA3A, SEMA3C and SEMA3E. Plays an important role in cell-cell signaling, and in regulating the migration of a wide spectrum of cell types. Regulates the migration of thymocytes in the medulla. Regulates endothelial cell migration. Plays an important role in ensuring the specificity of synapse formation. Required for normal development of the heart and vasculature (By similarity). Mediates anti-angiogenic signaling in …

**Summary**, from NCBI Gene [23129](https://www.ncbi.nlm.nih.gov/gene/23129):

> Enables protein domain specific binding activity. Predicted to be involved in several processes, including positive regulation of axonogenesis; semaphorin-plexin signaling pathway; and synapse assembly. Predicted to act upstream of or within circulatory system development; dichotomous subdivision of terminal units involved in salivary gland branching; and kidney development. Located in lamellipodium. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9107) · Entrez [23129](https://www.ncbi.nlm.nih.gov/gene/23129) · UniProt [Q9Y4D7](https://www.uniprot.org/uniprotkb/Q9Y4D7) · Ensembl [ENSG00000004399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004399)

## Data

Gene col 43: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 43); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 43, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 43]; `tensor/DDL_lfc|DDL_z.npy` [43]; `embed/gene_vectors.npy` [43]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 43 or target_col == 43). Every well: [[PLXND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
