---
symbol: "RRAS"
type: "gene"
col: 4737
ensembl_id: "ENSG00000126458"
name: "RAS related"
location: "19q13.33"
module: 192
arm: "+"
pooled_cpm: 15.02
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# RRAS

*RAS related* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +4.5, q 0.003, up in 12 of 24 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.252× (z -18.0, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNASE1L1]] (+0.78, fdr 7e-06), [[YIF1B]] (+0.77, fdr 1e-05), [[MGST3]] (+0.76, fdr 7e-06); moves opposite to [[KRR1]] (-0.69, fdr 3e-05), [[UTP20]] (-0.67, fdr 1e-05), [[CRPPA]] (-0.67, fdr 1e-04).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EHD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.5 | 0.003 | 12/24 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.53×** | +3.9 | 0.024 | 23/41 (Panc 03.27, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.41× | +3.2 | 0.30 | 14/33 (NCI-H2030, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.26× | +3.1 | 0.30 | 9/46 (HS-578T, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4737.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.252×** | -18.0 | 0e+00 | 42/45 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.225×** | -13.8 | 6e-41 | 42/44 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -6.8 | 3e-09 | 35/45 (HT-29, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.487×** | -6.4 | 2e-08 | 31/45 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.505×** | -6.3 | 3e-08 | 35/46 (LoVo, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.506×** | -6.3 | 3e-08 | 30/46 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.511×** | -5.9 | 4e-07 | 28/44 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.556×** | -5.4 | 4e-06 | 28/45 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.556×** | -5.4 | 4e-06 | 30/45 (hTERT-HPNE, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.559×** | -5.4 | 4e-06 | 30/46 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.582×** | -5.0 | 3e-05 | 27/45 (LOX-IMVI, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.601×** | -4.7 | 1e-04 | 28/45 (A-172, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.603×** | -4.4 | 4e-04 | 27/45 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -3.8 | 0.005 | 23/46 (HCT15, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.663×** | -3.8 | 0.006 | 21/44 (A-172, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.353×** | -3.7 | 0.006 | 23/45 (NCI-H1792, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 34.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.8) |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0706× (z -10.6) |
| [[HS-578T (line)]] | alt | 33.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -16.4) |
| [[HT-29 (line)]] | alt | 13.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.5) |
| [[A-427 (line)]] | wt | 29.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.1) |
| [[A498 (line)]] | wt | 16.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0735× (z -22.7) |
| [[A549 (line)]] | wt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.8) |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0927× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 9.07 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.6) |
| [[H4 (line)]] | wt | 20.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0294× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -8.8) |
| [[J82 (line)]] | alt | 17.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.4) |
| [[KATO III (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.0) |
| [[LoVo (line)]] | wt | 5.80 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.115× (z -8.9) |
| [[LS 180 (line)]] | wt | 9.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 9.88 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0656× (z -12.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 6.73 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0583× (z -20.1) |
| [[Panc 03.27 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -10.4) |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -9.1) |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.4) |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -12.5) |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNASE1L1]] | +0.78 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[YIF1B]] | +0.77 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[MGST3]] | +0.76 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[WASF2]] | +0.73 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.73 | +0.69 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[FAM89B]] | +0.72 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[TMEM256]] | +0.72 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PLD3]] | +0.72 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PCMT1]] | +0.72 | +0.70 / +0.32 | both halves | 2e-04 |  |
| [[CARD19]] | +0.71 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TRAPPC1]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ARL3]] | +0.71 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRR1]] | -0.69 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[UTP20]] | -0.67 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[CRPPA]] | -0.67 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[HNRNPU]] | -0.66 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[SNX5]] | -0.66 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[DNAJC11]] | -0.65 | -0.71 / -0.43 | both halves | 3e-05 |  |
| [[ZNF507]] | -0.65 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.65 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[ZFP91]] | -0.64 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[ST7L]] | -0.64 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.63 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD18A]] | -0.63 | -0.56 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EHD2]] | B | EHD2 activity strengthens RRAS's drug response | lines that do not express EHD2 (13) vs lines expressing it (33) | the lines without EHD2 respond 0.56× as strongly (z diff +1.31); strongest at Harringtonine 0.5 µM: 0.77x vs 0.49x (z diff +1.9) | 0.093 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.5, -1.4); signed map (-29.6, 16.3). **Vector** length 92.5, 24.8% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +0.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | -0.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -13.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -6.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | RAS related |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,635,292-49,640,143 (-) |
| Ensembl biotype | protein_coding |
| Also known as | R-Ras, RRAS1 |
| Gene groups (HGNC) | RAS type GTPase family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 6 pathways, smallest: Sema4D mediated inhibition of cell attachment and migration; SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; Sema4D in semaphorin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P10301](https://www.uniprot.org/uniprotkb/P10301) (Ras-related protein R-Ras):

> GTP-binding protein with GTPase activity, likely involved in the regulation of MAPK signaling pathway and thereby controlling multiple cellular processes. Regulates the organization of the actin cytoskeleton. With OSPBL3, modulates integrin beta-1 (ITGB1) activity.

**Summary**, from NCBI Gene [6237](https://www.ncbi.nlm.nih.gov/gene/6237):

> The protein encoded by this gene is a small GTPase involved in diverse processes including angiogenesis, vascular homeostasis and regeneration, cell adhesion, and neuronal axon guidance. Mutations in this gene are found in many invasive cancers. [provided by RefSeq, Jul 2015]

**Accessions** — [HGNC:10447](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10447) · Entrez [6237](https://www.ncbi.nlm.nih.gov/gene/6237) · UniProt [P10301](https://www.uniprot.org/uniprotkb/P10301) · Ensembl [ENSG00000126458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126458)

## Data

Gene col 4737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4737); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4737]; `tensor/DDL_lfc|DDL_z.npy` [4737]; `embed/gene_vectors.npy` [4737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4737 or target_col == 4737). Every well: [[RRAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
