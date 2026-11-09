---
symbol: "GSTO1"
type: "gene"
col: 7318
ensembl_id: "ENSG00000148834"
name: "glutathione S-transferase omega 1"
location: "10q25.1"
module: 110
arm: "+"
pooled_cpm: 51.46
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# GSTO1

*glutathione S-transferase omega 1* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.70× (z +5.2, q 1e-04, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.324× (z -15.6, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM89A]] (+0.63, fdr 1e-05), [[RUSC2]] (+0.63, fdr 1e-05), [[TM4SF19]] (+0.62, fdr 7e-06); moves opposite to [[PLXNB2]] (-0.61, fdr 1e-05), [[MXRA8]] (-0.53, fdr 4e-05), [[HACD2]] (-0.52, fdr 2e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ITPRIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +5.2 | 1e-04 | 36/47 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.4 | 0.003 | 25/46 (LOX-IMVI, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.53×** | +4.1 | 0.006 | 34/45 (SW 900, A-427, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7318.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.324×** | -15.6 | 0e+00 | 46/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.337×** | -10.6 | 5e-24 | 44/47 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.414×** | -8.6 | 1e-15 | 40/47 (SNU-423, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.454×** | -7.7 | 2e-12 | 41/47 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.516×** | -6.5 | 1e-08 | 34/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.571×** | -4.5 | 6e-04 | 35/47 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.379×** | -4.1 | 0.004 | 33/47 (J82, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.700×** | -3.5 | 0.032 | 28/47 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.681×** | -3.5 | 0.032 | 28/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.700×** | -3.3 | 0.046 | 25/47 (NCI-H23, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 133 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -18.0) |
| [[SNU-423 (line)]] | alt | 119 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.0) |
| [[J82 (line)]] | alt | 61.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.8) |
| [[A-172 (line)]] | wt | 84.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -10.6) |
| [[A549 (line)]] | wt | 52.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 73.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -16.7) |
| [[A498 (line)]] | wt | 59.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -14.1) |
| [[BT-474 (line)]] | alt | 14.4 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.272× (z -8.9) |
| [[H4 (line)]] | wt | 59.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -9.7) |
| [[HOP62 (line)]] | alt | 50.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -14.8) |
| [[HS-578T (line)]] | alt | 41.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -14.5) |
| [[LS 180 (line)]] | wt | 35.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 55.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -18.5) |
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.7) |
| [[SW 900 (line)]] | alt | 48.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -10.3) |
| [[A-427 (line)]] | wt | 33.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 55.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -16.7) |
| [[CFPAC-1 (line)]] | alt | 55.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.6) |
| [[COLO 205 (line)]] | alt | 30.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 45.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -14.4) |
| [[Hs 766T (line)]] | wt | 68.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -9.3) |
| [[HT-29 (line)]] | alt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.3) |
| [[KATO III (line)]] | alt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.1) |
| [[LoVo (line)]] | wt | 36.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 36.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 35.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 43.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 42.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.2) |
| [[PANC-1 (line)]] | alt | 45.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 54.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -17.3) |
| [[SW 1088 (line)]] | alt | 55.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -8.7) |
| [[SW480 (line)]] | alt | 38.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.9) |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM89A]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[RUSC2]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[TM4SF19]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[NBPF9]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[NBPF15]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[MRPL52]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[BFAR]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NOP10]] ⚠ | +0.56 | +0.36 / +0.64 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[EXOSC4]] | +0.55 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[FBXO28]] | +0.55 | +0.37 / +0.66 | both halves | 7e-05 |  |
| [[SMAGP]] | +0.55 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TM4SF19-DYNLT2B]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[POMP]] | +0.54 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNB2]] | -0.61 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[MXRA8]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[HACD2]] | -0.52 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[RAB1B]] | -0.51 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[AGRN]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 | pathway: Metabolism of vitamins and cofactors |
| [[REL]] | -0.50 | -0.56 / -0.49 | both halves | 2e-05 |  |
| [[LMNA]] | -0.50 | -0.60 / -0.40 | both halves | 4e-05 |  |
| [[MYOF]] | -0.49 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[BCL3]] | -0.49 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[GPD2]] | -0.49 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[CELSR3]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[ZMYM3]] | -0.48 | -0.30 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPRIP]] | B | ITPRIP activity raises GSTO1's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.95× lower at baseline in the lines without ITPRIP | 0.034 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[ARHGAP22]] | B | ARHGAP22 activity raises GSTO1's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 1.48× lower at baseline in the lines without ARHGAP22 | 0.049 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[ZNF215]] | B | ZNF215 activity raises GSTO1's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 1.55× lower at baseline in the lines without ZNF215 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[HDAC6]] | B | HDAC6 activity raises GSTO1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HMGA2]] | B | HMGA2 activity raises GSTO1's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 1.39× lower at baseline in the lines without HMGA2 | 0.087 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[C9orf72]] | C | C9orf72's natural level strengthens GSTO1's drug response | C9orf72's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.11; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ELK3]] | C | ELK3 activity raises GSTO1's level | lines that do not express ELK3 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without ELK3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, FSCN1, SUCLG2-DT; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.8, -25.0); signed map (-17.5, 46.8). **Vector** length 95.0, 30.4% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.7 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +2.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | -1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +0.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -2.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | glutathione S-transferase omega 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:104,235,356-104,267,459 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GSTTLp28, P28 |
| Gene groups (HGNC) | Soluble glutathione S-transferases; Oxidoreductases |
| Hallmark sets | XENOBIOTIC_METABOLISM, IL2_STAT5_SIGNALING |
| Reactome | 12 pathways, smallest: Vitamin C (ascorbate) metabolism; Methylation; Glutathione conjugation |
| Matched by | ensembl_id |

**Function**, from UniProt [P78417](https://www.uniprot.org/uniprotkb/P78417) (Glutathione S-transferase omega-1):

> Exhibits glutathione-dependent thiol transferase and dehydroascorbate reductase activities. Has S-(phenacyl)glutathione reductase activity. Also has glutathione S-transferase activity. Participates in the biotransformation of inorganic arsenic and reduces monomethylarsonic acid (MMA) and dimethylarsonic acid.

**Summary**, from NCBI Gene [9446](https://www.ncbi.nlm.nih.gov/gene/9446):

> The protein encoded by this gene is an omega class glutathione S-transferase (GST) with glutathione-dependent thiol transferase and dehydroascorbate reductase activities. GSTs are involved in the metabolism of xenobiotics and carcinogens. The encoded protein acts as a homodimer and is found in the cytoplasm. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:13312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13312) · Entrez [9446](https://www.ncbi.nlm.nih.gov/gene/9446) · UniProt [P78417](https://www.uniprot.org/uniprotkb/P78417) · Ensembl [ENSG00000148834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148834)

## Data

Gene col 7318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7318); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7318]; `tensor/DDL_lfc|DDL_z.npy` [7318]; `embed/gene_vectors.npy` [7318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7318 or target_col == 7318). Every well: [[GSTO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSTO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
