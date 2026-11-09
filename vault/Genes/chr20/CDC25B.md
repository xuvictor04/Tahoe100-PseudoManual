---
symbol: "CDC25B"
type: "gene"
col: 2100
ensembl_id: "ENSG00000101224"
name: "cell division cycle 25B"
location: "20p13"
module: 22
arm: "+"
pooled_cpm: 38.16
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 28
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CDC25B

*cell division cycle 25B* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +6.4, q 7e-08, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.429× (z -11.4, q 2e-27, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TROAP]] (+0.66, fdr 7e-06), [[KIF20A]] (+0.66, fdr 7e-06), [[KPNA2]] (+0.62, fdr 7e-06); moves opposite to [[COX19]] (-0.49, fdr 9e-05), [[NDUFB9]] (-0.46, fdr 8e-05), [[DNAJC2]] (-0.46, fdr 5e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +6.4 | 7e-08 | 31/48 (LoVo, HEC-1-A, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.2 | 2e-07 | 24/36 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +5.7 | 3e-06 | 29/46 (HOP62, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.8 | 2e-04 | 24/47 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.7 | 3e-04 | 26/45 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.004 | 21/48 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.004 | 19/48 (J82, AsPC-1, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.004 | 21/48 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.004 | 16/48 (A549, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +3.9 | 0.006 | 17/38 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.017 | 13/48 (SW1417, SHP-77, …) | rises with dose | position effect removed |
| [[Pentoxifylline (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.019 | 11/48 (SW1417, SW480, …) | rises with dose | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.2 | 0.055 | 11/39 (RPMI-7951, J82, …) | top dose only | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.082 | 11/48 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.084 | 8/47 (Hs 766T, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.429×** | -11.4 | 2e-27 | 38/48 (LS 180, HT-29, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.495×** | -10.0 | 3e-21 | 36/46 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.614×** | -9.9 | 1e-20 | 30/47 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.617×** | -6.9 | 7e-10 | 30/48 (H4, HT-29, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.423×** | -6.4 | 1e-08 | 33/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.437×** | -6.2 | 6e-08 | 28/43 (SK-MEL-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.673×** | -5.7 | 1e-06 | 26/48 (PANC-1, SW 900, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.705×** | -5.0 | 4e-05 | 27/48 (PANC-1, SW 900, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -4.8 | 1e-04 | 23/48 (LS 180, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.544×** | -4.6 | 3e-04 | 27/47 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.732×** | -4.5 | 4e-04 | 18/48 (A549, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.736×** | -4.4 | 5e-04 | 23/48 (A-172, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.737×** | -4.4 | 5e-04 | 24/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.740×** | -4.1 | 0.001 | 24/45 (A498, hTERT-HPNE, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.819×** | -4.1 | 0.002 | 19/48 (LS 180, A549, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.005 | 18/47 (A549, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.789×** | -3.4 | 0.020 | 20/48 (SNU-1, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.731×** | -3.2 | 0.037 | 14/48 (HT-29, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.804×** | -3.1 | 0.044 | 15/48 (SNU-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.860× | -3.1 | 0.054 | 16/48 (CFPAC-1, COLO 205, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 64.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.0) |
| [[LoVo (line)]] | wt | 25.7 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.79× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -9.2) |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.107× (z -13.4) |
| [[PANC-1 (line)]] | alt | 49.2 | 0 | 3 | — | [[Bortezomib (drug)]] 0.05 µM 0.314× (z -9.0) |
| [[SW480 (line)]] | alt | 71.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -15.4) |
| [[A-172 (line)]] | wt | 34.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +9.2) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.235× (z -9.5) |
| [[A498 (line)]] | wt | 33.1 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.311× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.360× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 40.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.3) |
| [[COLO 205 (line)]] | alt | 59.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -16.9) |
| [[H4 (line)]] | wt | 34.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0406× (z -16.3) |
| [[HT-29 (line)]] | alt | 55.0 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.176× (z -12.5) |
| [[KATO III (line)]] | alt | 49.7 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.202× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.73× (z +12.2) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 42.3 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.239× (z -12.1) |
| [[SHP-77 (line)]] | alt | 56.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 30.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.5) |
| [[C32 (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 41.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.276× (z -8.9) |
| [[J82 (line)]] | alt | 37.8 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.330× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -8.7) |
| [[SNU-1 (line)]] | wt | 74.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -8.7) |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TROAP]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KIF20A]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[KPNA2]] | +0.62 | +0.58 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDCA3]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[NCAPD2]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[PIF1]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SPAG5]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[BUB1]] | +0.59 | +0.58 / +0.59 | both halves | 8e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 475 |
| [[CCNB2]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 847 |
| [[PSRC1]] | +0.58 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[NUSAP1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[FAM72B]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX19]] | -0.49 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[NDUFB9]] | -0.46 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[DNAJC2]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[PFDN1]] | -0.46 | -0.41 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDC25B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.5, -58.3); signed map (-52.3, -43.0). **Vector** length 119, 32.5% of its response variance represented; |z| ≥ 3 in 1,097 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.52 to 28); *Polo-like kinase mediated events* (reactome, mean cos +0.52 to 7); *G2/M DNA replication checkpoint* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +6.2 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.1 | +1.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -6.7 | -11.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.3 | -6.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.8 | -6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -4.4 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 25B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,786,772-3,806,121 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MPIP2 |
| Gene groups (HGNC) | Class III Cys-based CDC25 phosphatases |
| Hallmark sets | APOPTOSIS, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 14 pathways, smallest: Regulation of MITF-M-dependent genes involved in cell cycle and proliferation; Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models; Neurodegenerative Diseases |
| Matched by | ensembl_id |

**Function**, from UniProt [P30305](https://www.uniprot.org/uniprotkb/P30305) (M-phase inducer phosphatase 2):

> Tyrosine protein phosphatase which functions as a dosage-dependent inducer of mitotic progression. Directly dephosphorylates CDK1 and stimulates its kinase activity. Required for G2/M phases of the cell cycle progression and abscission during cytokinesis in a ECT2-dependent manner. The three isoforms seem to have a different level of activity.

**Summary**, from NCBI Gene [994](https://www.ncbi.nlm.nih.gov/gene/994):

> CDC25B is a member of the CDC25 family of phosphatases. CDC25B activates the cyclin dependent kinase CDC2 by removing two phosphate groups and it is required for entry into mitosis. CDC25B shuttles between the nucleus and the cytoplasm due to nuclear localization and nuclear export signals. The protein is nuclear in the M and G1 phases of the cell cycle and moves to the cytoplasm during S and G2. CDC25B has oncogenic properties, although its role in tumor formation has not been determined. …

**Accessions** — [HGNC:1726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1726) · Entrez [994](https://www.ncbi.nlm.nih.gov/gene/994) · UniProt [P30305](https://www.uniprot.org/uniprotkb/P30305) · Ensembl [ENSG00000101224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101224)

## Data

Gene col 2100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2100); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2100]; `tensor/DDL_lfc|DDL_z.npy` [2100]; `embed/gene_vectors.npy` [2100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2100 or target_col == 2100). Every well: [[CDC25B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC25B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
