---
symbol: "MTDH"
type: "gene"
col: 7209
ensembl_id: "ENSG00000147649"
name: "metadherin"
location: "8q22.1"
module: 56
arm: "+"
pooled_cpm: 303.74
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# MTDH

*metadherin* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.58× (z +7.9, q 1e-12, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.642× (z -10.8, q 2e-24, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC63]] (+0.68, fdr 7e-06), [[RWDD1]] (+0.64, fdr 3e-05), [[SRP72]] (+0.63, fdr 8e-06); moves opposite to [[NEMP1]] (-0.54, fdr 4e-05), [[CFL1]] (-0.53, fdr 3e-05), [[PNRC2]] (-0.52, fdr 2e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +7.9 | 1e-12 | 44/48 (C32, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.9 | 1e-09 | 45/49 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.6 | 8e-09 | 32/44 (NCI-H1792, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +6.5 | 1e-08 | 36/45 (NCI-H1792, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.29×** | +4.3 | 0.002 | 28/47 (COLO 205, NCI-H1792, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +4.0 | 0.006 | 35/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.006 | 29/49 (COLO 205, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.006 | 33/48 (NCI-H1792, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.008 | 30/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.013 | 34/48 (NCI-H2030, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.079 | 27/48 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.13× | +3.1 | 0.11 | 5/48 (NCI-H1792, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -10.8 | 2e-24 | 43/49 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.652×** | -7.4 | 4e-11 | 41/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.699×** | -6.2 | 1e-07 | 39/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -4.2 | 0.004 | 20/48 (HOP62, LoVo, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.793×** | -4.0 | 0.007 | 29/48 (SW480, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.826×** | -3.3 | 0.090 | 25/48 (BT-474, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.775×** | -3.3 | 0.090 | 30/48 (RKO, SW1417, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 330 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.02× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.421× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 194 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +14.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 263 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.333× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 424 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 202 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -9.0) |
| [[SHP-77 (line)]] | alt | 253 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -12.9) |
| [[A498 (line)]] | wt | 552 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -13.3) |
| [[BT-474 (line)]] | alt | 355 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -12.3) |
| [[C32 (line)]] | wt | 416 | 1 | 1 | [[Auranofin (drug)]] 5 µM 1.94× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -10.5) |
| [[H4 (line)]] | wt | 312 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -11.0) |
| [[Hs 766T (line)]] | wt | 295 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.14× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.644× (z -8.5) |
| [[KATO III (line)]] | alt | 298 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.466× (z -9.2) |
| [[LoVo (line)]] | wt | 345 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -18.4) |
| [[MIA PaCa-2 (line)]] | alt | 234 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.373× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 221 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +13.9) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 154 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.426× (z -9.2) |
| [[SW1417 (line)]] | alt | 304 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -10.5) |
| [[SW48 (line)]] | wt | 389 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.45× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -13.5) |
| [[A-172 (line)]] | wt | 321 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.87× (z +9.2) | — |
| [[A549 (line)]] | wt | 232 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.32× (z +9.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 311 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -10.7) |
| [[CHP-212 (line)]] | wt | 277 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -10.1) |
| [[COLO 205 (line)]] | alt | 238 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.45× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 345 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 288 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -12.0) |
| [[J82 (line)]] | alt | 386 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 338 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -11.4) |
| [[RKO (line)]] | wt | 709 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -16.3) |
| [[RPMI-7951 (line)]] | alt | 296 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.28× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 185 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.473× (z -8.6) |
| [[SNU-1 (line)]] | wt | 283 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -12.2) |
| [[SNU-423 (line)]] | alt | 211 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 366 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.1) |
| [[A-427 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 206 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 185 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 555 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 254 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 283 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 299 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 392 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 393 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 331 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC63]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RWDD1]] | +0.64 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[SRP72]] | +0.63 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[EPRS1]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CLINT1]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[GFPT1]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[DNAJC2]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[EIF3M]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[NFXL1]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[EIF2A]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | +0.55 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[LINC00662]] | +0.54 | +0.53 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEMP1]] | -0.54 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[CFL1]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PNRC2]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CDC42EP2]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[APOBEC3B]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[AGRN]] | -0.47 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[GPAA1]] | -0.47 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[SMAD3]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RMI2]] | -0.46 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[PPP1CA]] | -0.45 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ZNF217]] | -0.45 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[EIF4EBP2]] | -0.45 | -0.59 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MTDH's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.4, -19.3); signed map (-59.0, 11.3). **Vector** length 108, 40.1% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | -0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -10.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.8 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -2.0 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | metadherin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:97,644,184-97,730,260 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LYRIC, 3D3, AEG-1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UE4](https://www.uniprot.org/uniprotkb/Q86UE4) (Protein LYRIC):

> Down-regulates SLC1A2/EAAT2 promoter activity when expressed ectopically. Activates the nuclear factor kappa-B (NF-kappa-B) transcription factor. Promotes anchorage-independent growth of immortalized melanocytes and astrocytes which is a key component in tumor cell expansion. Promotes lung metastasis and also has an effect on bone and brain metastasis, possibly by enhancing the seeding of tumor cells to the target organ endothelium. Induces chemoresistance.

**Summary**, from NCBI Gene [92140](https://www.ncbi.nlm.nih.gov/gene/92140):

> Enables NF-kappaB binding activity; double-stranded RNA binding activity; and transcription coactivator activity. Involved in several processes, including lipopolysaccharide-mediated signaling pathway; positive regulation of angiogenesis; and positive regulation of intracellular signal transduction. Located in endoplasmic reticulum; nuclear body; and perinuclear region of cytoplasm. Implicated in hepatocellular carcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29608](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29608) · Entrez [92140](https://www.ncbi.nlm.nih.gov/gene/92140) · UniProt [Q86UE4](https://www.uniprot.org/uniprotkb/Q86UE4) · Ensembl [ENSG00000147649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147649)

## Data

Gene col 7209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7209); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7209]; `tensor/DDL_lfc|DDL_z.npy` [7209]; `embed/gene_vectors.npy` [7209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7209 or target_col == 7209). Every well: [[MTDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
