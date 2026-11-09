---
symbol: "PSMA3"
type: "gene"
col: 1986
ensembl_id: "ENSG00000100567"
name: "proteasome 20S subunit alpha 3"
location: "14q23.1"
module: 72
arm: "+"
pooled_cpm: 71.94
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMA3

*proteasome 20S subunit alpha 3* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.51× (z +16.0, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.774× (z -4.4, q 0.006, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMA1]] (+0.76, fdr 7e-06), [[PSMB2]] (+0.74, fdr 7e-06), [[PSMC6]] (+0.74, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.55, fdr 2e-05), [[MYL12A]] (-0.54, fdr 3e-05), [[TSPAN4]] (-0.53, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.51×** | +16.0 | 0e+00 | 47/48 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.42×** | +15.3 | 0e+00 | 48/48 (SW480, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.03×** | +11.6 | 7e-29 | 47/48 (SW480, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.50×** | +6.7 | 2e-09 | 35/47 (LoVo, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.2 | 5e-08 | 33/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.64×** | +6.1 | 1e-07 | 41/49 (LOX-IMVI, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 3e-07 | 31/48 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.38×** | +5.5 | 2e-06 | 25/49 (SW480, NCI-H1792, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.83×** | +5.5 | 3e-06 | 30/49 (HOP62, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.9 | 6e-05 | 34/45 (SNU-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.33×** | +4.7 | 1e-04 | 31/48 (NCI-H460, CFPAC-1, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.30×** | +4.5 | 3e-04 | 24/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +4.4 | 5e-04 | 26/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.8 | 0.005 | 20/38 (AsPC-1, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.6 | 0.012 | 21/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.036 | 18/48 (SNU-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1986.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.774×** | -4.4 | 0.006 | 25/48 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.847× | -4.0 | 0.015 | 16/49 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.6 | 0.048 | 17/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.813×** | -3.6 | 0.048 | 22/47 (SNU-423, SW 1271, …) | rises with dose | low cells (technical?) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.087 | 18/48 (SW 1088, KATO III, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.826×** | -3.3 | 0.087 | 18/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.829×** | -3.2 | 0.099 | 17/49 (BT-474, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.1 | 0.11 | 18/48 (A498, HT-29, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.836× | -3.1 | 0.11 | 15/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.830× | -3.1 | 0.11 | 17/47 (SW 1271, A498, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.949× | -3.0 | 0.13 | 0/50 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 56.1 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.53× (z +11.5) | — |
| [[SW480 (line)]] | alt | 61.5 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.20× (z +14.7) | — |
| [[C32 (line)]] | wt | 46.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.41× (z +13.3) | — |
| [[CFPAC-1 (line)]] | alt | 88.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.46× (z +13.1) | — |
| [[HOP62 (line)]] | alt | 44.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.10× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 68.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.73× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 60.8 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.78× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.41× (z +9.7) | — |
| [[A-427 (line)]] | wt | 83.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 58.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.21× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 47.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.96× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 50.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.61× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 69.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.73× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 44.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.50× (z +10.5) | — |
| [[KATO III (line)]] | alt | 72.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.32× (z +12.8) | — |
| [[LoVo (line)]] | wt | 75.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.31× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 48.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.22× (z +11.3) | — |
| [[LS 180 (line)]] | wt | 75.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.59× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 76.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.44× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 92.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.58× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 84.0 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 110 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.45× (z +10.6) | — |
| [[HCT15 (line)]] | alt | 72.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.12× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 65.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.88× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 50.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.82× (z +8.5) | — |
| [[J82 (line)]] | alt | 57.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 83.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 99.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.19× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 67.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.02× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 52.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.74× (z +8.8) | — |
| [[A-172 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA1]] | +0.76 | +0.80 / +0.67 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB2]] | +0.74 | +0.75 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[PSMC6]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[PSMA6]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[TXNL1]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PSMC2]] | +0.62 | +0.67 / +0.51 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[PSMD11]] | +0.62 | +0.70 / +0.56 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMA2]] | +0.60 | +0.65 / +0.59 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[PIR]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[NMI]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PSMA5]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMA4]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.55 | -0.66 / -0.48 | both halves | 2e-05 | pathway: Adherens junctions interactions |
| [[MYL12A]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[TSPAN4]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[MYADM]] | -0.51 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[CD9]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[IER2]] | -0.48 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[PPP1R13L]] | -0.48 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[EGR1]] | -0.48 | -0.43 / -0.41 | both halves | 4e-05 | pathway: Intracellular signaling by second messengers; STRING 599 |
| [[SDC4]] | -0.47 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[MAPK8IP3]] | -0.46 | -0.43 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises PSMA3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.6, -10.1); signed map (-26.5, -23.9). **Vector** length 105, 31.5% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v1* (hallmark, mean cos +0.59 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.1 | +15.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +16.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.4 | +11.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.6 | +4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.0 | +6.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -5.1 | +3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -4.4 | +4.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.5 | -1.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit alpha 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:58,244,843-58,272,012 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HC8 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE, MTORC1_SIGNALING |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P25788](https://www.uniprot.org/uniprotkb/P25788) (Proteasome subunit alpha type-3):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5684](https://www.ncbi.nlm.nih.gov/gene/5684):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9532) · Entrez [5684](https://www.ncbi.nlm.nih.gov/gene/5684) · UniProt [P25788](https://www.uniprot.org/uniprotkb/P25788) · Ensembl [ENSG00000100567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100567)

## Data

Gene col 1986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1986); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1986]; `tensor/DDL_lfc|DDL_z.npy` [1986]; `embed/gene_vectors.npy` [1986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1986 or target_col == 1986). Every well: [[PSMA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
