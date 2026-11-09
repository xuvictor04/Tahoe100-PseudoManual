---
symbol: "TUBB6"
type: "gene"
col: 10670
ensembl_id: "ENSG00000176014"
name: "tubulin beta 6 class V"
location: "18p11.21"
module: 110
arm: "+"
pooled_cpm: 85.81
n_lines_expressing: 39
n_dd_up: 8
n_dd_down: 25
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# TUBB6

*tubulin beta 6 class V* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Peretinoin (drug)]] 5 µM: 1.47× (z +6.5, q 4e-08, up in 29 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.654× (z -10.5, q 3e-23, down in 26 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK10]] (+0.68, fdr 7e-06), [[CORO2B]] (+0.65, fdr 7e-06), [[EFL1]] (+0.63, fdr 7e-06); moves opposite to [[MINDY1]] (-0.60, fdr 1e-05), [[HINT3]] (-0.58, fdr 1e-05), [[CHASERR]] (-0.56, fdr 1e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HS3ST3A1]] → it (grade B ⚠); 9 go from it, the strongest it → [[PLIN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Peretinoin (drug)]] 5 µM |  | **1.47×** | +6.5 | 4e-08 | 29/36 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.43×** | +6.2 | 1e-07 | 27/37 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +5.4 | 1e-05 | 20/38 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.33×** | +5.0 | 9e-05 | 23/36 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.60×** | +4.2 | 0.004 | 18/35 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 1.16× | +3.8 | 0.013 | 11/37 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.013 | 17/36 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.068 | 8/37 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.074 | 15/37 (MIA PaCa-2, NCI-H1573, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.20× | +3.2 | 0.089 | 8/37 (PANC-1, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -10.5 | 3e-23 | 26/37 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.645×** | -7.7 | 4e-12 | 23/37 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.739×** | -7.5 | 9e-12 | 24/37 (A-172, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.648×** | -7.0 | 3e-10 | 22/35 (A-427, HOP62, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -7.0 | 3e-10 | 21/36 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.779×** | -5.4 | 7e-06 | 22/37 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.749×** | -5.1 | 3e-05 | 20/37 (A-172, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -5.0 | 5e-05 | 24/39 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.758×** | -4.9 | 7e-05 | 22/37 (BT-474, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.588×** | -4.7 | 1e-04 | 20/37 (HEC-1-A, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.754×** | -4.7 | 1e-04 | 19/37 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.792×** | -4.6 | 2e-04 | 19/37 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.836× | -4.4 | 5e-04 | 20/37 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.773×** | -4.4 | 5e-04 | 19/35 (HOP62, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.783×** | -4.3 | 6e-04 | 23/37 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.779×** | -4.2 | 8e-04 | 19/37 (A-172, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **0.796×** | -4.0 | 0.002 | 16/37 (HS-578T, HOP62, …) | inconsistent across doses | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.803×** | -3.9 | 0.003 | 15/37 (BT-474, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.839× | -3.7 | 0.006 | 16/37 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 211 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -24.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -21.0) |
| [[MIA PaCa-2 (line)]] | alt | 221 | 1 | 10 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.79× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -17.6) |
| [[HOP62 (line)]] | alt | 490 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -20.2) |
| [[SK-MEL-2 (line)]] | alt | 155 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -13.6) |
| [[HEC-1-A (line)]] | alt | 135 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -14.9) |
| [[HS-578T (line)]] | alt | 168 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 76.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 69.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 62.9 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.27× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 62.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -9.1) |
| [[A-427 (line)]] | wt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -14.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 70.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -14.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 67.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 34.6 | 1 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 2.92× (z +8.6) ⚠ unreliable plate only | — |
| [[NCI-H1792 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 49.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H596 (line)]] | alt | 72.6 | 1 | 0 | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 3.06× (z +11.6) | — |
| [[NCI-H661 (line)]] | alt | 54.7 | 0 | 1 | — | [[MK-3903 (drug)]] 0.05 µM 0.0754× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.9) |
| [[A498 (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.80 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.09 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 18.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.82 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.58 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK10]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[EFL1]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[PDLIM7]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CCM2]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ARHGAP22]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[MPP3]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PLIN3]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 | pathway: Autophagy |
| [[ZNF274]] | +0.60 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[MTMR9]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[WNT9A]] | +0.59 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LRRC8C]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY1]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[HINT3]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CHASERR]] | -0.56 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[MBNL2]] | -0.56 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CSDE1]] | -0.55 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TMEM123]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SCP2]] | -0.54 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[PPP1CB]] | -0.54 | -0.40 / -0.57 | both halves | 5e-05 | pathway: G2/M Transition |
| [[PON2]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[EPHX2]] | -0.53 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[RAVER2]] | -0.53 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises TUBB6's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without HS3ST3A1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[MEIS3]] | B | MEIS3 activity raises TUBB6's level | lines that do not express MEIS3 (12) vs lines expressing it (38) | 3.14× lower at baseline in the lines without MEIS3 | 0.065 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[TRIM2]] | B | TRIM2 activity lowers TUBB6's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 2.51× higher at baseline in the lines without TRIM2 | 0.093 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLIN3]] | B | TUBB6 activity raises PLIN3's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without TUBB6 | 0.011 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[TMEM44]] | B | TUBB6 activity raises TMEM44's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 1.25× lower at baseline in the lines without TUBB6 | 0.055 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[AKAP12]] | B | TUBB6 activity raises AKAP12's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 5.18× lower at baseline in the lines without TUBB6 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[PLXNA2]] | B | TUBB6 activity lowers PLXNA2's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 2.69× higher at baseline in the lines without TUBB6 | 0.068 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[NFIA]] | B | TUBB6 activity lowers NFIA's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 3.14× higher at baseline in the lines without TUBB6 | 0.083 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | B | TUBB6 activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express TUBB6 (11) vs lines expressing it (37) | the lines without TUBB6: 0.88× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[CPLX1]] | B | TUBB6 activity lowers CPLX1's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 2.08× higher at baseline in the lines without TUBB6 | 0.089 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[TUBA1C]] | B | TUBB6 activity raises TUBA1C's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 1.12× lower at baseline in the lines without TUBB6 | 0.092 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[DNAAF9]] | C | TUBB6 activity raises DNAAF9's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 8.13× lower at baseline in the lines without TUBB6 | 0.046 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1; co-absent with the target |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.4, 2.0); signed map (-1.0, 33.9). **Vector** length 131, 39.6% of its response variance represented; |z| ≥ 3 in 1,156 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Peretinoin (drug)]] 5 µM |  | +5.6 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.4 | +5.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.2 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.4 | +3.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +4.3 | +3.8 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | -3.8 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.5 | -5.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | tubulin beta 6 class V |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:12,307,669-12,344,320 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4083, HsT1601 |
| Gene groups (HGNC) | Tubulin beta family |
| Reactome | 83 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUF5](https://www.uniprot.org/uniprotkb/Q9BUF5) (Tubulin beta-6 chain):

> Tubulin is the major constituent of microtubules, a cylinder consisting of laterally associated linear protofilaments composed of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin.

**Summary**, from NCBI Gene [84617](https://www.ncbi.nlm.nih.gov/gene/84617):

> Predicted to enable GTP binding activity. Predicted to be a structural constituent of cytoskeleton. Predicted to be involved in microtubule cytoskeleton organization and mitotic cell cycle. Located in microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20776](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20776) · Entrez [84617](https://www.ncbi.nlm.nih.gov/gene/84617) · UniProt [Q9BUF5](https://www.uniprot.org/uniprotkb/Q9BUF5) · Ensembl [ENSG00000176014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176014)

## Data

Gene col 10670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10670); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10670]; `tensor/DDL_lfc|DDL_z.npy` [10670]; `embed/gene_vectors.npy` [10670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10670 or target_col == 10670). Every well: [[TUBB6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBB6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
