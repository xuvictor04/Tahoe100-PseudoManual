---
symbol: "HLA-H"
type: "gene"
col: 13041
ensembl_id: "ENSG00000206341"
name: "major histocompatibility complex, class I, H (pseudogene)"
location: "6p22.1"
module: 70
arm: "+"
pooled_cpm: 6.11
n_lines_expressing: 42
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# HLA-H

*major histocompatibility complex, class I, H (pseudogene)* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.82× (z +6.4, q 1e-07, up in 18 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.720× (z -8.8, q 6e-16, down in 33 of 40 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.478× (z -5.6, q 7e-06, down in 14 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-C]] (+0.79, fdr 7e-06), [[TAPBP]] (+0.73, fdr 1e-05), [[ERAP1]] (+0.68, fdr 1e-05); moves opposite to [[RBAK-RBAKDN]] (-0.57, fdr 4e-05), [[DHX57]] (-0.56, fdr 5e-05), [[TECPR1]] (-0.56, fdr 5e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HLA-F]] → it (grade B ⚠); 6 go from it, the strongest it → [[RCN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13041.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +6.4 | 1e-07 | 18/33 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.2 | 2e-07 | 17/33 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +6.0 | 4e-07 | 3/10 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.16×** | +5.8 | 1e-06 | 14/38 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +5.6 | 2e-06 | 6/14 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +5.3 | 1e-05 | 14/34 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.74×** | +4.1 | 0.003 | 16/38 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +3.9 | 0.007 | 6/23 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.64×** | +3.7 | 0.013 | 13/38 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.088 | 8/39 (MIA PaCa-2, NCI-H1792, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.1 | 0.088 | 8/38 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13041.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.720×** | -8.8 | 6e-16 | 33/40 (A-427, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.478×** | -5.6 | 7e-06 | 14/38 (A-427, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.538×** | -4.7 | 6e-04 | 14/38 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.620×** | -3.6 | 0.044 | 12/38 (NCI-H2347, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.642×** | -3.3 | 0.094 | 11/38 (NCI-H2347, NCI-H1792, …) | all doses, flat |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.739× | -3.2 | 0.12 | 13/38 (NCI-H1573, Hs 766T, …) | rises with dose | position effect removed |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 0.751× | -3.1 | 0.17 | 8/39 (HOP62, SNU-423, …) | rises with dose | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.659× | -3.0 | 0.17 | 3/37 (COLO 205, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-C]] | +0.79 | +0.70 / +0.76 | both halves | 7e-06 | same gene group; pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| [[TAPBP]] | +0.73 | +0.54 / +0.70 | both halves | 1e-05 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| [[ERAP1]] | +0.68 | +0.50 / +0.64 | both halves | 1e-05 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| [[AP1G2-AS1]] | +0.68 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[C5orf15]] | +0.68 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[HCP5]] | +0.67 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[MED12]] | +0.66 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.65 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TAP1]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 | pathway: Antigen Presentation: Folding, assembly and peptide loading of class I MHC |
| [[APOBEC3B]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[TAF9B]] | +0.64 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[MOV10]] | +0.63 | +0.43 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBAK-RBAKDN]] | -0.57 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DHX57]] | -0.56 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[TECPR1]] | -0.56 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[NDUFAB1]] | -0.55 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[DAP3]] | -0.55 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[PPIL2]] | -0.54 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[GTF2H2]] | -0.54 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[MRPS34]] | -0.53 | -0.36 / -0.32 | both halves | 2e-04 |  |
| [[SNU13]] | -0.53 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[EIF3K]] | -0.52 | -0.30 / -0.44 | both halves | 2e-04 | pathway: Interferon Signaling |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F]] | B | HLA-F activity raises HLA-H's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.24× lower at baseline in the lines without HLA-F | 0.025 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HLA-H's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HLA-K]] | B | HLA-K activity raises HLA-H's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.93× lower at baseline in the lines without HLA-K | 0.075 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[HCP5]] | B | HCP5 activity raises HLA-H's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without HCP5 | 0.087 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[HLA-A]] | C | HLA-A activity raises HLA-H's level | lines that do not express HLA-A (6) vs lines expressing it (44) | 2.80× lower at baseline in the lines without HLA-A | 0.081 | ⚠ within organs, on part of the lines; also absent: PHLDA1, S100A6, HLA-H; co-absent with the target; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RCN1]] | B | HLA-H activity raises RCN1's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without HLA-H | 0.020 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |
| [[AGRN]] | B | HLA-H activity raises AGRN's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without HLA-H | 0.071 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |
| [[APOBEC3F]] | B | HLA-H activity raises APOBEC3F's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without HLA-H | 0.075 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |
| [[ERAP1]] | B | HLA-H activity raises ERAP1's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.67× lower at baseline in the lines without HLA-H | 0.084 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |
| [[LDB1]] | B | HLA-H activity lowers LDB1's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.72× higher at baseline in the lines without HLA-H | 0.097 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |
| [[HLA-A]] | C | HLA-H activity raises HLA-A's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 4.03× lower at baseline in the lines without HLA-H | 0.036 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.550). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.8, 4.0); signed map (24.5, -20.4). **Vector** length 46.5, 6.33% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DAP12 interactions* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +0.2 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.1 | +2.5 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.6 | -4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.3 | -3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class I, H (pseudogene) |
| Locus type | pseudogene |
| Location | 6p22.1 — chr6:29,887,752-29,890,482 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Gene groups (HGNC) | Histocompatibility complex |
| Reactome | 18 pathways, smallest: Endosomal/Vacuolar pathway; Antigen Presentation: Folding, assembly and peptide loading of class I MHC; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell |
| Matched by | ensembl_id |

**Function**, from UniProt [P01893](https://www.uniprot.org/uniprotkb/P01893) (Putative HLA class I histocompatibility antigen, alpha chain H):

> Involved in the presentation of foreign antigens to the immune system.

**Summary**, from NCBI Gene [3136](https://www.ncbi.nlm.nih.gov/gene/3136):

> This major histocompatibility complex gene represents a transcribed pseudogene, possibly derived from HLA-A. This gene displays extensive variation. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:4965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4965) · Entrez [3136](https://www.ncbi.nlm.nih.gov/gene/3136) · UniProt [P01893](https://www.uniprot.org/uniprotkb/P01893) · Ensembl [ENSG00000206341](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206341)

## Data

Gene col 13041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13041); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13041]; `tensor/DDL_lfc|DDL_z.npy` [13041]; `embed/gene_vectors.npy` [13041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13041 or target_col == 13041). Every well: [[HLA-H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
