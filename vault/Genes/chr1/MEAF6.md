---
symbol: "MEAF6"
type: "gene"
col: 8799
ensembl_id: "ENSG00000163875"
name: "MYST/Esa1 associated factor 6"
location: "1p34.3"
module: 74
arm: "+"
pooled_cpm: 44.59
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# MEAF6

*MYST/Esa1 associated factor 6* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +8.5, q 9e-15, up in 38 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.25× (z +4.6, q 5e-04, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.628× (z -6.8, q 5e-09, down in 37 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.551× (z -4.4, q 0.003, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.315×, A-427 0.463×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.455×, SW 1271 0.102×; ⚠ cell-cycle shift, explains ~20% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.483×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRBN]] (+0.60, fdr 2e-05), [[EZH1]] (+0.58, fdr 2e-05), [[PLEKHM3]] (+0.55, fdr 4e-05); moves opposite to [[PIK3R3]] (-0.48, fdr 7e-05), [[SYTL5]] (-0.47, fdr 3e-05), [[ETNK1]] (-0.45, fdr 1e-04).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[STS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +8.5 | 9e-15 | 38/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +7.5 | 1e-11 | 37/41 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +5.2 | 3e-05 | 31/44 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +4.6 | 5e-04 | 28/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 0.001 | 26/48 (A549, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.033 | 23/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.5 | 0.042 | 23/47 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.071 | 17/48 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.079 | 18/48 (SW48, HCT15, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.088 | 19/48 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.51× | +3.0 | 0.12 | 15/42 (LS 180, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8799.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.315×, A-427 0.463×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.455×, SW 1271 0.102×; ⚠ cell-cycle shift, explains ~20% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.483×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.628×** | -6.8 | 5e-09 | 37/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.551×** | -4.4 | 0.003 | 28/48 (SNU-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.822×** | -4.1 | 0.009 | 24/47 (RKO, SW 1271, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.639× | -3.3 | 0.12 | 19/47 (HT-29, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.0 | 0.28 | 25/48 (NCI-H1792, A-427, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 76.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.483× (z -9.6) |
| [[SW480 (line)]] | alt | 43.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 33.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.464× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 31.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 52.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.388× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 48.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.65× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1792 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 68.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -10.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -9.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A-172 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRBN]] | +0.60 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[EZH1]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 | same gene group |
| [[PLEKHM3]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[AUH]] | +0.51 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[MCUR1]] ⚠ | +0.50 | +0.50 / +0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FBXO3]] | +0.50 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[PRXL2C]] | +0.49 | +0.44 / +0.40 | both halves | 5e-05 |  |
| [[RAB4A]] | +0.49 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[WDR48]] | +0.49 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[TMOD2]] | +0.48 | +0.46 / +0.33 | both halves | 1e-04 |  |
| [[FLVCR2]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 | same gene group |
| [[ESD]] | +0.48 | +0.55 / +0.31 | both halves | 2e-04 |  |
| [[MAOA]] | +0.47 | +0.43 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3R3]] | -0.48 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[SYTL5]] | -0.47 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ETNK1]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[MPDU1]] | -0.45 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[SRMS]] | -0.44 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[MTFR2]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[INTS6L]] | -0.43 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[STS]] | -0.43 | -0.49 / -0.30 | both halves | 2e-04 | same gene group |
| [[FER1L4]] | -0.43 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[SLC12A2]] | -0.43 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[SECISBP2]] | -0.42 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[CEMIP]] | -0.42 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STS]] | B | STS activity lowers MEAF6's level | lines that do not express STS (11) vs lines expressing it (39) | 1.28× higher at baseline in the lines without STS | 0.023 | ⚠ within organs, on part of the lines; also absent: FBXO39, KPNA7; maybe low, not absent |
| [[SYTL5]] | B | SYTL5 activity lowers MEAF6's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 1.40× higher at baseline in the lines without SYTL5 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[TLR2]] | B | TLR2 activity lowers MEAF6's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 1.28× higher at baseline in the lines without TLR2 | 0.081 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.282). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.2, -47.7); signed map (-15.9, 7.2). **Vector** length 95.9, 25.1% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +2.9 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.9 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.0 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MYST/Esa1 associated factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,489,993-37,514,766 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NY-SAR-91, FLJ11730, Eaf6, CENP-28; previously C1orf149 |
| Gene groups (HGNC) | Tip60/Nua4 histone acetyltransferase complex subunits; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: Regulation of TP53 Activity through Acetylation; HATs acetylate histones; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAF1](https://www.uniprot.org/uniprotkb/Q9HAF1) (Chromatin modification-related protein MEAF6):

> Component of the NuA4 histone acetyltransferase complex which is involved in transcriptional activation of select genes principally by acetylation of nucleosomal histone H4 and H2A. This modification may both alter nucleosome - DNA interactions and promote interaction of the modified histones with other proteins which positively regulate transcription. Component of HBO1 complexes, which specifically mediate acetylation of histone H3 at 'Lys-14' (H3K14ac), and have reduced activity toward …

**Summary**, from NCBI Gene [64769](https://www.ncbi.nlm.nih.gov/gene/64769):

> This gene encodes a nuclear protein involved in transcriptional activation. The encoded protein may form a component of several different histone acetyltransferase complexes. There is a pseudogene for this gene on chromosome 2. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:25674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25674) · Entrez [64769](https://www.ncbi.nlm.nih.gov/gene/64769) · UniProt [Q9HAF1](https://www.uniprot.org/uniprotkb/Q9HAF1) · Ensembl [ENSG00000163875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163875)

## Data

Gene col 8799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8799); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8799]; `tensor/DDL_lfc|DDL_z.npy` [8799]; `embed/gene_vectors.npy` [8799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8799 or target_col == 8799). Every well: [[MEAF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEAF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
