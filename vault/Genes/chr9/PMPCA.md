---
symbol: "PMPCA"
type: "gene"
col: 9168
ensembl_id: "ENSG00000165688"
name: "peptidase, mitochondrial processing subunit alpha"
location: "9q34.3"
module: 42
arm: "+"
pooled_cpm: 24.88
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# PMPCA

*peptidase, mitochondrial processing subunit alpha* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.22× (z +13.7, q 1e-39, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.470× (z -12.5, q 7e-33, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM10B]] (+0.70, fdr 7e-06), [[PDCD6]] (+0.70, fdr 7e-06), [[TMEM248]] (+0.67, fdr 7e-06); moves opposite to [[RNF115]] (-0.64, fdr 7e-06), [[ITSN2]] (-0.64, fdr 1e-05), [[SETD2]] (-0.63, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IL15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.22×** | +13.7 | 1e-39 | 44/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.97×** | +11.6 | 1e-28 | 39/48 (SW480, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.96×** | +11.5 | 2e-28 | 42/48 (SW480, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.43×** | +8.7 | 5e-16 | 29/48 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +7.8 | 7e-13 | 31/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.54×** | +7.4 | 2e-11 | 32/47 (SW480, LS 180, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.41×** | +5.6 | 1e-06 | 23/45 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.40×** | +5.3 | 9e-06 | 21/41 (SK-MEL-2, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.35×** | +5.1 | 2e-05 | 25/46 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 4e-05 | 22/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.8 | 8e-05 | 21/48 (BT-474, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.9 | 0.004 | 13/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.2 | 0.050 | 12/31 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9168.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.470×** | -12.5 | 7e-33 | 44/47 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.573×** | -9.5 | 4e-19 | 40/48 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.706×** | -8.5 | 5e-15 | 29/47 (RKO, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.663×** | -7.0 | 3e-10 | 27/47 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.739×** | -5.0 | 7e-05 | 24/47 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.786×** | -4.1 | 0.003 | 18/48 (hTERT-HPNE, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.793×** | -4.0 | 0.006 | 18/48 (HT-29, A-427, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.795×** | -4.0 | 0.006 | 17/47 (NCI-H23, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -3.8 | 0.008 | 18/48 (C-33 A, A-172, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.795×** | -3.8 | 0.008 | 18/47 (HepG2/C3A, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.860× | -3.7 | 0.011 | 19/48 (A498, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.826×** | -3.7 | 0.012 | 17/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.809×** | -3.6 | 0.012 | 16/46 (HS-578T, SHP-77, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.806×** | -3.6 | 0.015 | 15/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.022 | 13/47 (NCI-H2030, LS 180, …) | two highest doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.051 | 10/48 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.828×** | -3.1 | 0.054 | 18/47 (J82, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 30.2 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +12.0) | — |
| [[A498 (line)]] | wt | 45.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.438× (z -8.5) |
| [[A-427 (line)]] | wt | 18.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 21.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.7) | — |
| [[RKO (line)]] | wt | 69.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -14.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -11.1) |
| [[A549 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[H4 (line)]] | wt | 31.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 26.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.00× (z +9.3) | — |
| [[J82 (line)]] | alt | 33.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.304× (z -10.5) |
| [[LoVo (line)]] | wt | 22.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.291× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RPMI-7951 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM10B]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 | pathway: Mitochondrial protein import; STRING 436 |
| [[PDCD6]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[TMEM248]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[DCAF13]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[SENP5]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[DDB1]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[BCAP31]] | +0.64 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[CHID1]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[SAR1A]] | +0.63 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[NIPA2]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[MLEC]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[FBXW2]] | +0.63 | +0.68 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | -0.64 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[ITSN2]] | -0.64 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[SETD2]] | -0.63 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[SUMO4]] | -0.62 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[THOC7]] | -0.62 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.62 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[LRRC37A2]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[NSMCE3]] | -0.61 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[RAD52]] | -0.61 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[KMT2A]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[CLK4]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[PPP1R12A]] | -0.60 | -0.57 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL15]] | B | IL15 activity lowers PMPCA's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.18× higher at baseline in the lines without IL15 | 0.077 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.1, -28.0); signed map (-48.3, 0.9). **Vector** length 108, 26.3% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.0 | +8.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.8 | +11.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +3.2 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.4 | +1.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -12.1 | -12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -8.7 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.2 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | peptidase, mitochondrial processing subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,410,630-136,427,992 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0123, Alpha-MPP, MAS2; previously INPP5E, SCAR2, CLA1 |
| Gene groups (HGNC) | M16 metallopeptidases |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10713](https://www.uniprot.org/uniprotkb/Q10713) (Mitochondrial-processing peptidase subunit alpha):

> Substrate recognition and binding subunit of the essential mitochondrial processing protease (MPP), which cleaves the mitochondrial sequence off newly imported precursors proteins.

**Summary**, from NCBI Gene [23203](https://www.ncbi.nlm.nih.gov/gene/23203):

> The protein encoded by this gene is found in the mitochondrion, where it represents the alpha subunit of a proteolytic heterodimer. This heterodimer is responsible for cleaving the transit peptide from nuclear-encoded mitochondrial proteins. Defects in this gene are a cause of spinocerebellar ataxia, autosomal recessive 2. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:18667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18667) · Entrez [23203](https://www.ncbi.nlm.nih.gov/gene/23203) · UniProt [Q10713](https://www.uniprot.org/uniprotkb/Q10713) · Ensembl [ENSG00000165688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165688)

## Data

Gene col 9168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9168); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9168]; `tensor/DDL_lfc|DDL_z.npy` [9168]; `embed/gene_vectors.npy` [9168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9168 or target_col == 9168). Every well: [[PMPCA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMPCA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
