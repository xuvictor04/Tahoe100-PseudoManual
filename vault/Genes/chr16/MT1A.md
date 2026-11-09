---
symbol: "MT1A"
type: "gene"
col: 12973
ensembl_id: "ENSG00000205362"
name: "metallothionein 1A"
location: "16q13"
module: 113
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 17
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# MT1A

*metallothionein 1A* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.39× (z +8.9, q 3e-16, up in 5 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 3.22× (z +7.9, q 4e-13, up in 14 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.401× (z -4.1, q 0.022, down in 8 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.117×; ⚠ cell-cycle shift, explains ~50% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.111×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1X]] (+0.76, fdr 7e-06, ⚠ same locus), [[MT2A]] (+0.72, fdr 7e-06, ⚠ same locus), [[MT1E]] (+0.71, fdr 7e-06, ⚠ read-through risk), [[SAA1]] (+0.67, fdr 1e-05), [[CCL20]] (+0.67, fdr 2e-05), [[TLR2]] (+0.64, fdr 7e-06); moves opposite to [[BBOX1-AS1]] (-0.59, fdr 1e-05), [[TMEM234]] (-0.51, fdr 1e-04), [[FANK1]] (-0.48, fdr 6e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR3C1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MT1E]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12973.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.39×** | +8.9 | 3e-16 | 5/10 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.68×** | +8.0 | 3e-13 | 2/4 (CFPAC-1, MIA PaCa-2) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.22×** | +7.9 | 4e-13 | 14/14 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.34×** | +6.5 | 1e-08 | 2/8 (LoVo, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.03×** | +5.3 | 1e-05 | 12/12 (CFPAC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **2.60×** | +4.6 | 4e-04 | 9/13 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.46×** | +4.3 | 0.001 | 2/9 (PANC-1, CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.44×** | +4.3 | 0.001 | 8/12 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.52×** | +4.3 | 0.001 | 4/10 (Hs 766T, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.20×** | +3.8 | 0.009 | 9/12 (Hs 766T, SW 900, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.19×** | +3.7 | 0.010 | 8/14 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **2.16×** | +3.7 | 0.011 | 8/13 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.10×** | +3.5 | 0.017 | 9/13 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.5 | 0.019 | 3/11 (PANC-1, Hs 766T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.04×** | +3.4 | 0.025 | 8/13 (Hs 766T, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.01×** | +3.3 | 0.031 | 7/13 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.99×** | +3.0 | 0.075 | 7/12 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +2.9 | 0.091 | 2/13 (CFPAC-1, SW 900) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +2.9 | 0.093 | 3/11 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12973.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.117×; ⚠ cell-cycle shift, explains ~50% of this change); [[Bortezomib (drug)]] 0.05 µM in 1 line (PANC-1 0.111×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.401×** | -4.1 | 0.022 | 8/14 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | 0.535× | -3.1 | 0.50 | 5/14 (A549, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.514× | -3.0 | 0.50 | 1/13 (LoVo) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12973. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 24.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.97× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -11.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[CFPAC-1 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +14.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HOP62 (line)]] | alt | 2.59 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.6× (z +11.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[PANC-1 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.111× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.214 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.239 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.922 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.278 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12973), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1X]] | +0.76 | +0.63 / +0.77 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 677; ⚠ same locus (42.4 kb, same strand: neighbours can correlate without regulation) |
| [[MT2A]] | +0.72 | +0.60 / +0.68 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 429; ⚠ same locus (29.2 kb, same strand: neighbours can correlate without regulation) |
| [[MT1E]] | +0.71 | +0.59 / +0.70 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 479; ⚠ **readthrough risk**: this gene lies 11.6 kb 3′ of MT1E on the same strand (can correlate by spillover, not regulation) |
| [[SAA1]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[MT1F]] | +0.67 | +0.51 / +0.74 | both halves | 1e-05 | same gene group; pathway: Metallothioneins bind metals; ⚠ same locus (17.6 kb, same strand: neighbours can correlate without regulation) |
| [[CCL20]] | +0.67 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[MT1M]] | +0.65 | +0.57 / +0.72 | both halves | 9e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 481; ⚠ same locus (4.7 kb, same strand: neighbours can correlate without regulation) |
| [[TLR2]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[SLC45A1]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[CEBPB]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[OSBPL5]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[BIRC3]] | +0.62 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ID1]] | +0.60 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[VSTM2L]] | +0.60 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[MAOA]] | +0.59 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TBC1D8]] | +0.59 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[HS3ST3B1]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBOX1-AS1]] | -0.59 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[TMEM234]] | -0.51 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[FANK1]] | -0.48 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[NEK11]] | -0.48 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[IQCK]] | -0.47 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[MFSD1]] | -0.47 | -0.29 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises MT1A's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MT1E]] | C | MT1A activity raises MT1E's level | lines that do not express MT1A (33) vs lines expressing it (17) | 3.12× lower at baseline in the lines without MT1A | 0.042 | ⚠ within organs, on part of the lines; also absent: WT1-AS, KRT5, ENSG00000238178; co-absent with the target |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.5, 13.4); signed map (14.4, 31.6). **Vector** length 44.3, 13.3% of its response variance represented; |z| ≥ 3 in 417 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.53 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +3.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.8 | +4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +1.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.7 | +4.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -0.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | metallothionein 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,638,666-56,640,087 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MT1, MT1S |
| Gene groups (HGNC) | Metallothioneins |
| Reactome | 3 pathways, smallest: Metallothioneins bind metals; Response to metal ions; Cellular responses to stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [P04731](https://www.uniprot.org/uniprotkb/P04731) (Metallothionein-1A):

> Metallothioneins have a high content of cysteine residues that bind various heavy metals; these proteins are transcriptionally regulated by both heavy metals and glucocorticoids.

**Summary**, from NCBI Gene [4489](https://www.ncbi.nlm.nih.gov/gene/4489):

> This gene is a member of the metallothionein family of genes. Proteins encoded by this gene family are low in molecular weight, are cysteine-rich, lack aromatic residues, and bind divalent heavy metal ions. The conserved cysteine residues co-ordinate metal ions using mercaptide linkages. These proteins act as anti-oxidants, protect against hydroxyl free radicals, are important in homeostatic control of metal in the cell, and play a role in detoxification of heavy metals. Disruption of two …

**Accessions** — [HGNC:7393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7393) · Entrez [4489](https://www.ncbi.nlm.nih.gov/gene/4489) · UniProt [P04731](https://www.uniprot.org/uniprotkb/P04731) · Ensembl [ENSG00000205362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205362)

## Data

Gene col 12973: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12973); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12973, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12973]; `tensor/DDL_lfc|DDL_z.npy` [12973]; `embed/gene_vectors.npy` [12973]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12973 or target_col == 12973). Every well: [[MT1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
