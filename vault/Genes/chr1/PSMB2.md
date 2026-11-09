---
symbol: "PSMB2"
type: "gene"
col: 4712
ensembl_id: "ENSG00000126067"
name: "proteasome 20S subunit beta 2"
location: "1p34.3"
module: 72
arm: "+"
pooled_cpm: 56.74
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMB2

*proteasome 20S subunit beta 2* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (16 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 3.51× (z +20.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.798× (z -5.2, q 1e-04, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 0.280×, A-427 0.505×, BT-474 0.447×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMA1]] (+0.80, fdr 7e-06), [[USP5]] (+0.75, fdr 7e-06), [[PSMA3]] (+0.74, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.62, fdr 7e-06), [[GCAT]] (-0.61, fdr 1e-05), [[BTG1]] (-0.61, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM241A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.51×** | +20.2 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.47×** | +20.0 | 0e+00 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.87×** | +16.0 | 0e+00 | 48/48 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.15×** | +12.3 | 1e-32 | 44/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.10×** | +11.5 | 2e-28 | 32/42 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.81×** | +9.5 | 1e-19 | 41/48 (PANC-1, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.36×** | +9.3 | 9e-19 | 43/49 (PANC-1, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.83×** | +9.0 | 2e-17 | 35/44 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.68×** | +8.4 | 3e-15 | 41/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +8.0 | 6e-14 | 39/48 (COLO 205, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.98×** | +7.7 | 8e-13 | 42/48 (LOX-IMVI, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.53×** | +6.5 | 3e-09 | 35/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.47×** | +6.2 | 2e-08 | 32/48 (PANC-1, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.38×** | +5.5 | 2e-06 | 30/48 (LS 180, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.33×** | +4.5 | 2e-04 | 30/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.001 | 29/48 (J82, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | 1.16× | +3.4 | 0.018 | 6/48 (HS-578T, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +2.9 | 0.086 | 11/48 (HOP62, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4712.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (RKO 0.280×, A-427 0.505×, BT-474 0.447×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.798×** | -5.2 | 1e-04 | 28/48 (SW1417, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.816× | -3.3 | 0.26 | 22/48 (SW480, CHP-212, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.817× | -3.1 | 0.36 | 16/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.7 | 8 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.91× (z +15.0) | — |
| [[NCI-H460 (line)]] | wt | 38.9 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.43× (z +15.9) | — |
| [[SW480 (line)]] | alt | 55.2 | 7 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.37× (z +18.1) | — |
| [[LS 180 (line)]] | wt | 63.9 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.06× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 50.6 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.48× (z +14.8) | — |
| [[KATO III (line)]] | alt | 57.2 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.00× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 35.3 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.80× (z +13.7) | — |
| [[C32 (line)]] | wt | 42.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.38× (z +12.3) | — |
| [[COLO 205 (line)]] | alt | 38.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.37× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 60.7 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.85× (z +13.1) | — |
| [[LoVo (line)]] | wt | 56.4 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.57× (z +15.9) | — |
| [[NCI-H23 (line)]] | alt | 71.8 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.13× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 42.2 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.55× (z +12.1) | — |
| [[A-427 (line)]] | wt | 98.4 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.41× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 77.5 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.51× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 44.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.44× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 55.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.41× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 60.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.94× (z +13.4) | — |
| [[HepG2_C3A (line)]] | wt | 53.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.57× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 36.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.94× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 40.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.37× (z +14.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 61.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.92× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 40.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.58× (z +16.1) | — |
| [[NCI-H2347 (line)]] | alt | 69.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +10.5) | — |
| [[RKO (line)]] | wt | 59.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.62× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 58.9 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.73× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 67.1 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.65× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 54.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.40× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 50.7 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.26× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 47.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.34× (z +9.6) | — |
| [[A-172 (line)]] | wt | 38.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A549 (line)]] | wt | 36.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 53.2 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.05× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 51.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.01× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 64.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.95× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 82.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.99× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 67.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.80× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 60.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.95× (z +10.4) | — |
| [[SW1417 (line)]] | alt | 51.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +9.3) | — |
| [[SW48 (line)]] | wt | 67.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.15× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA1]] | +0.80 | +0.83 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[USP5]] | +0.75 | +0.76 / +0.74 | both halves | 7e-06 | pathway: Deubiquitination |
| [[PSMA3]] | +0.74 | +0.75 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[PSMB7]] | +0.74 | +0.75 / +0.74 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB3]] | +0.73 | +0.80 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[BABAM1]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PSMD11]] | +0.72 | +0.67 / +0.77 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMD1]] | +0.70 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[TALDO1]] | +0.68 | +0.79 / +0.70 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[PSMA6]] | +0.67 | +0.76 / +0.60 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[UBE2L3]] | +0.67 | +0.72 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[UBQLN1]] | +0.67 | +0.70 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.62 | -0.67 / -0.62 | both halves | 7e-06 | pathway: Adherens junctions interactions |
| [[GCAT]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[BTG1]] | -0.61 | -0.65 / -0.52 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[NBPF10]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[SP4]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NBPF19]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[NBPF14]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[N4BP3]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM241A]] | B | FAM241A activity lowers PSMB2's level | lines that do not express FAM241A (7) vs lines expressing it (43) | 1.28× higher at baseline in the lines without FAM241A | 0.053 | ⚠ within organs, on part of the lines; also absent: TES, TRIB1, LRRCC1; maybe low, not absent |
| [[GPX3]] | B | GPX3 activity lowers PSMB2's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.13× higher at baseline in the lines without GPX3 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.0, -10.2); signed map (-26.6, -25.0). **Vector** length 88.8, 26.7% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.2 | +20.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.6 | +20.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +16.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.9 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.3 | -1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +2.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,599,541-35,641,526 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HC7-I |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE, MYC_TARGETS_V1 |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P49721](https://www.uniprot.org/uniprotkb/P49721) (Proteasome subunit beta type-2):

> Non-catalytic component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or …

**Summary**, from NCBI Gene [5690](https://www.ncbi.nlm.nih.gov/gene/5690):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9539) · Entrez [5690](https://www.ncbi.nlm.nih.gov/gene/5690) · UniProt [P49721](https://www.uniprot.org/uniprotkb/P49721) · Ensembl [ENSG00000126067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126067)

## Data

Gene col 4712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4712); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4712]; `tensor/DDL_lfc|DDL_z.npy` [4712]; `embed/gene_vectors.npy` [4712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4712 or target_col == 4712). Every well: [[PSMB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
