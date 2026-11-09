---
symbol: "VPS29"
type: "gene"
col: 3206
ensembl_id: "ENSG00000111237"
name: "VPS29 retromer complex component"
location: "12q24.11"
module: 64
arm: "+"
pooled_cpm: 35.62
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# VPS29

*VPS29 retromer complex component* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.36× (z +14.9, q 0e+00, up in 43 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.55× (z +7.6, q 6e-12, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.639× (z -7.8, q 5e-12, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHKB]] (+0.56, fdr 8e-05), [[PDZD11]] (+0.56, fdr 3e-05), [[TALDO1]] (+0.55, fdr 5e-05); moves opposite to [[SRF]] (-0.52, fdr 3e-05), [[ZIC2]] (-0.48, fdr 3e-04), [[FZD7]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CABLES1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3206.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +14.9 | 0e+00 | 43/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +12.3 | 5e-32 | 31/36 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +9.5 | 4e-19 | 32/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +7.6 | 6e-12 | 41/48 (NCI-H1573, PANC-1, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +5.9 | 4e-07 | 27/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +5.8 | 6e-07 | 26/48 (NCI-H1573, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.36×** | +5.4 | 7e-06 | 25/48 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 4e-05 | 30/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +4.8 | 1e-04 | 26/48 (SW480, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **1.33×** | +4.7 | 1e-04 | 27/45 (RKO, NCI-H1573, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.001 | 22/48 (RKO, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.26×** | +3.9 | 0.004 | 22/48 (HOP62, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **1.23×** | +3.6 | 0.013 | 15/46 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.4 | 0.025 | 19/47 (Hs 766T, J82, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.066 | 11/48 (SW1417, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3206.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -7.8 | 5e-12 | 37/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.741×** | -7.3 | 6e-11 | 27/47 (J82, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -6.6 | 6e-09 | 34/48 (LoVo, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.713×** | -5.9 | 6e-07 | 26/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.588×** | -4.8 | 2e-04 | 26/47 (A-427, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.3 | 0.001 | 24/48 (RPMI-7951, KATO III, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -4.0 | 0.006 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.803×** | -3.8 | 0.010 | 17/48 (SW 1088, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3206. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 31.5 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.340× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.348× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 55.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.327× (z -11.0) |
| [[PANC-1 (line)]] | alt | 47.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +12.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +8.8) ⚠ toxic; transcription drop | [[Bosentan (hydrate) (drug)]] 5 µM 0.147× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 28.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.5) |
| [[A498 (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +11.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -8.9) |
| [[H4 (line)]] | wt | 27.1 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.163× (z -9.8) |
| [[Hs 766T (line)]] | wt | 44.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -8.6) |
| [[J82 (line)]] | alt | 41.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.5) |
| [[LS 180 (line)]] | wt | 35.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.3) |
| [[SNU-423 (line)]] | alt | 31.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.23× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0628× (z -8.8) |
| [[SW480 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3206), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKB]] | +0.56 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[PDZD11]] | +0.56 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[TALDO1]] | +0.55 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[ORC3]] | +0.55 | +0.54 / +0.43 | both halves | 4e-05 |  |
| [[HTT]] | +0.55 | +0.57 / +0.37 | both halves | 9e-05 |  |
| [[DCTN2]] | +0.54 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[TPRKB]] | +0.54 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[PSMD13]] | +0.54 | +0.60 / +0.37 | both halves | 8e-05 | pathway: Signaling by WNT |
| [[NUP43]] | +0.53 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[PSMC5]] | +0.53 | +0.53 / +0.52 | both halves | 1e-05 | pathway: Signaling by WNT |
| [[ANXA7]] | +0.53 | +0.58 / +0.46 | both halves | 3e-05 | STRING 787 |
| [[CYB5R1]] | +0.52 | +0.49 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRF]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ZIC2]] | -0.48 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[FZD7]] | -0.46 | -0.32 / -0.38 | both halves | 2e-04 | pathway: Signaling by WNT |
| [[KLHL15]] | -0.46 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[STIM2]] | -0.46 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZNF703]] | -0.44 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[NR4A3]] | -0.44 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[CCNL1]] | -0.44 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[AZU1]] | -0.44 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[HES1]] | -0.44 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[LAG3]] | -0.43 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[PSD]] | -0.43 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CABLES1]] | B | CABLES1 activity raises VPS29's level | lines that do not express CABLES1 (6) vs lines expressing it (44) | 1.34× lower at baseline in the lines without CABLES1 | 0.068 | ⚠ within organs, on part of the lines; also absent: BAIAP2L1, ARMH1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.454). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-20.6, -13.8); signed map (-36.8, -31.2). **Vector** length 78.0, 15.9% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.4 | +5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -7.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.3 | -3.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | VPS29 retromer complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,491,083-110,502,111 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEP11, DC7, DC15 |
| Gene groups (HGNC) | Retriever complex |
| Reactome | 2 pathways, smallest: WNT ligand biogenesis and trafficking; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBQ0](https://www.uniprot.org/uniprotkb/Q9UBQ0) (Vacuolar protein sorting-associated protein 29):

> Component of the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. Component of the retriever complex, which is a heterotrimeric complex related to retromer cargo-selective complex (CSC) and essential for retromer-independent retrieval and recycling of numerous cargos such as integrin alpha-5/beta-1 (ITGA5:ITGB1). Component of the retromer cargo-selective complex (CSC). The …

**Summary**, from NCBI Gene [51699](https://www.ncbi.nlm.nih.gov/gene/51699):

> This gene belongs to a group of vacuolar protein sorting (VPS) genes that, when functionally impaired, disrupt the efficient delivery of vacuolar hydrolases. The protein encoded by this gene is a component of a large multimeric complex, termed the retromer complex, which is involved in retrograde transport of proteins from endosomes to the trans-Golgi network. This VPS protein may be involved in the formation of the inner shell of the retromer coat for retrograde vesicles leaving the …

**Accessions** — [HGNC:14340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14340) · Entrez [51699](https://www.ncbi.nlm.nih.gov/gene/51699) · UniProt [Q9UBQ0](https://www.uniprot.org/uniprotkb/Q9UBQ0) · Ensembl [ENSG00000111237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111237)

## Data

Gene col 3206: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3206); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3206, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3206]; `tensor/DDL_lfc|DDL_z.npy` [3206]; `embed/gene_vectors.npy` [3206]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3206 or target_col == 3206). Every well: [[VPS29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
