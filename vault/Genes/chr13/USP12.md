---
symbol: "USP12"
type: "gene"
col: 7634
ensembl_id: "ENSG00000152484"
name: "ubiquitin specific peptidase 12"
location: "13q12.13"
module: 14
arm: "+"
pooled_cpm: 137.0
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# USP12

*ubiquitin specific peptidase 12* — 13q12.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.55× (z +8.7, q 2e-15, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.603× (z -6.9, q 3e-09, down in 30 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.815× (z -4.1, q 0.005, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC30A4]] (+0.53, fdr 3e-05), [[SLC41A2]] (+0.53, fdr 3e-05), [[AKT3]] (+0.51, fdr 1e-05); moves opposite to [[NUP214]] (-0.52, fdr 8e-05), [[TYW1]] (-0.48, fdr 9e-05), [[PPP2R5C]] (-0.48, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ELOVL7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7634.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +8.7 | 2e-15 | 40/48 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +5.9 | 8e-07 | 35/48 (COLO 205, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.0 | 1e-04 | 32/47 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 1e-04 | 37/48 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +4.5 | 9e-04 | 35/48 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.4 | 0.001 | 29/48 (COLO 205, A498, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +4.1 | 0.004 | 37/49 (NCI-H1573, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.012 | 24/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.042 | 28/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.2 | 0.089 | 25/48 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.25× | +3.1 | 0.11 | 22/48 (CFPAC-1, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7634.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.603×** | -6.9 | 3e-09 | 30/44 (SW 900, NCI-H23, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.626×** | -6.6 | 9e-09 | 38/48 (HOP62, A549, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.632×** | -6.5 | 2e-08 | 33/49 (A-172, RKO, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.650×** | -6.1 | 1e-07 | 34/48 (HOP62, PANC-1, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.815×** | -4.1 | 0.005 | 27/48 (C32, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.833×** | -3.7 | 0.023 | 23/48 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.781×** | -3.5 | 0.038 | 25/48 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -3.3 | 0.063 | 26/48 (HOP62, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7634. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 203 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 135 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 211 | 1 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.28× (z +9.2) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -16.0) ⚠ cell-cycle shift, explains ~77% of this change |
| [[A549 (line)]] | wt | 139 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.291× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 173 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +14.6) | — |
| [[HOP62 (line)]] | alt | 135 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -13.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 81.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +14.4) | — |
| [[LoVo (line)]] | wt | 93.7 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.40× (z +13.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.29× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 312 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -16.3) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H1573 (line)]] | alt | 104 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.41× (z +9.7) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 9.02× (z +9.5) | — |
| [[A-427 (line)]] | wt | 72.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 243 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.1) | — |
| [[J82 (line)]] | alt | 193 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 148 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -8.6) ⚠ cell-cycle shift, explains ~77% of this change |
| [[NCI-H23 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.373× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[AsPC-1 (line)]] | alt | 190 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.3) | — |
| [[BT-474 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[C-33 A (line)]] | alt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.358× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 97.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.49× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 93.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.0) | — |
| [[CHP-212 (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 113 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 93.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 152 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 54.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 96.3 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 8.14× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 212 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 200 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7634), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A4]] | +0.53 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[SLC41A2]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[AKT3]] | +0.51 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MB21D2]] | +0.50 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ATXN1-AS1]] | +0.50 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[DENND5A]] | +0.50 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RIPK2]] | +0.49 | +0.57 / +0.39 | both halves | 5e-05 | pathway: Deubiquitination |
| [[TCTA]] | +0.47 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[GATM]] | +0.47 | +0.30 / +0.45 | both halves | 2e-04 |  |
| [[NR3C1]] | +0.47 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[CCDC3]] | +0.46 | +0.27 / +0.41 | both halves | 3e-04 |  |
| [[PRRT2]] | +0.46 | +0.35 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP214]] | -0.52 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[TYW1]] | -0.48 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[PPP2R5C]] | -0.48 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[METTL16]] | -0.47 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[AGAP4]] | -0.47 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[DDX19A]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[TM9SF4]] | -0.47 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.46 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[AVL9]] | -0.46 | -0.39 / -0.40 | both halves | 5e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[SFSWAP]] | -0.43 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TRMT44]] | -0.43 | -0.24 / -0.55 | both halves | 4e-04 |  |
| [[GTF3C2]] | -0.43 | -0.30 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELOVL7]] | B | ELOVL7 activity lowers USP12's level | lines that do not express ELOVL7 (11) vs lines expressing it (39) | 1.12× higher at baseline in the lines without ELOVL7 | 0.082 | ⚠ within organs, on part of the lines; also absent: KRT86; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.389). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, -1.6); signed map (44.2, 11.1). **Vector** length 99.4, 32.2% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.2 | +1.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.9 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +0.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | +4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +1.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | +3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.13 — chr13:27,066,156-27,171,811 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously USP12L1 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [O75317](https://www.uniprot.org/uniprotkb/O75317) (Ubiquitin carboxyl-terminal hydrolase 12):

> Deubiquitinating enzyme that plays various roles in the regulation of the immune response and inflammation. During TCR engagement and activation, translocates into the cytoplasm and deubiquitinates its substrates LAT and TRAT1 and prevents their lysosome-dependent degradation to stabilize the TCR signaling complex at the plasma membrane. Plays an essential role in the selective LPS-induced macrophage response through the activation of NF-kappa-B pathway. In addition, promotes that antiviral …

**Summary**, from NCBI Gene [219333](https://www.ncbi.nlm.nih.gov/gene/219333):

> Enables cysteine-type deubiquitinase activity and cysteine-type endopeptidase activity. Involved in protein deubiquitination. Located in cytoplasm; nucleus; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20485](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20485) · Entrez [219333](https://www.ncbi.nlm.nih.gov/gene/219333) · UniProt [O75317](https://www.uniprot.org/uniprotkb/O75317) · Ensembl [ENSG00000152484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152484)

## Data

Gene col 7634: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7634); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7634, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7634]; `tensor/DDL_lfc|DDL_z.npy` [7634]; `embed/gene_vectors.npy` [7634]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7634 or target_col == 7634). Every well: [[USP12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
