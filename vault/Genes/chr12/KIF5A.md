---
symbol: "KIF5A"
type: "gene"
col: 7938
ensembl_id: "ENSG00000155980"
name: "kinesin family member 5A"
location: "12q13.3"
module: 82
arm: "+"
pooled_cpm: 3.91
n_lines_expressing: 46
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# KIF5A

*kinesin family member 5A* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.53× (z +20.8, q 0e+00, up in 25 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 5 µM in 1 line (RPMI-7951 0.0761×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP6]] (+0.64, fdr 7e-06), [[CELF5]] (+0.61, fdr 1e-05), [[KIF5C]] (+0.61, fdr 1e-05); moves opposite to [[CENPP]] (-0.50, fdr 6e-05), [[LINC01515]] (-0.49, fdr 5e-05), [[TTF2]] (-0.48, fdr 8e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[EFCAB13-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.53×** | +20.8 | 0e+00 | 25/35 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.85×** | +17.3 | 0e+00 | 16/32 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.55×** | +14.7 | 0e+00 | 24/36 (LoVo, A-427, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +10.5 | 1e-23 | 26/43 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +10.5 | 1e-23 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +9.3 | 2e-18 | 7/18 (LoVo, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +8.9 | 5e-17 | 27/42 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +8.2 | 1e-14 | 23/40 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +8.1 | 4e-14 | 23/43 (PANC-1, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +7.6 | 2e-12 | 27/42 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.88×** | +7.4 | 9e-12 | 22/36 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +6.5 | 5e-09 | 10/33 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.3 | 2e-08 | 4/18 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.0 | 7e-08 | 6/43 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +5.2 | 9e-06 | 12/39 (LoVo, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +5.0 | 2e-05 | 9/42 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +4.9 | 3e-05 | 12/41 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +4.8 | 5e-05 | 11/30 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 5 µM in 1 line (RPMI-7951 0.0761×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | 0.730× | -3.5 | 0.13 | 7/37 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.813× | -3.4 | 0.13 | 8/42 (NCI-H661, A-427, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.05 µM |  | 0.731× | -3.4 | 0.13 | 1/33 (hTERT-HPNE) | inconsistent across doses |  |
| [[Furosemide (drug)]] 0.5 µM |  | 0.758× | -3.3 | 0.16 | 5/38 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.765× | -3.1 | 0.19 | 7/41 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.34× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 2.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +8.5) | — |
| [[LoVo (line)]] | wt | 3.03 | 1 | 0 | [[Auranofin (drug)]] 5 µM 17.5× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 3.39 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 21.2× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 6.17 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0761× (z -8.6) |
| [[A-172 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.861 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP6]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[CELF5]] | +0.61 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[KIF5C]] | +0.61 | +0.50 / +0.67 | both halves | 1e-05 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 965 |
| [[RYR1]] | +0.60 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[CDH23]] | +0.59 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[APBB1]] | +0.59 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CRLF1]] | +0.58 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[FEZ1]] | +0.58 | +0.54 / +0.67 | both halves | 1e-05 | STRING 469 |
| [[ABCC11]] | +0.58 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[HNRNPD-DT]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[SLC27A6]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ATP8A2]] | +0.56 | +0.47 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPP]] | -0.50 | -0.38 / -0.38 | both halves | 6e-05 | pathway: RHO GTPase Effectors |
| [[LINC01515]] | -0.49 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[TTF2]] | -0.48 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[KIF24]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KIF5A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[OCIAD2]] | B | OCIAD2 activity lowers KIF5A's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 2.86× higher at baseline in the lines without OCIAD2 | 0.063 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |
| [[ESYT3]] | B | ESYT3 activity strengthens KIF5A's drug response | lines that do not express ESYT3 (13) vs lines expressing it (30) | the lines without ESYT3 respond 0.60× as strongly (z diff +1.06); strongest at Panobinostat 0.5 µM: 1.48x vs 3.11x (z diff +2.3) | 0.063 | ⚠ within organs, on part of the lines; also absent: BEND6, ENSG00000224905, ZNF354C; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFCAB13-DT]] | C | KIF5A activity lowers EFCAB13-DT's level | lines that do not express KIF5A (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without KIF5A | 0.087 | ⚠ few lines (4 vs 46); across organs; also absent: ZDHHC1, ALPK3; maybe low, not absent |
| [[UBE2Q2P1]] | C | KIF5A activity raises UBE2Q2P1's level | lines that do not express KIF5A (4) vs lines expressing it (46) | 2.16× lower at baseline in the lines without KIF5A | 0.098 | ⚠ few lines (4 vs 46); across organs; also absent: ZDHHC1, ALPK3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, 35.6); signed map (25.2, 20.4). **Vector** length 54.9, 7.30% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +4.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -2.5 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | +0.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,546,026-57,586,633 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D12S1889, NKHC, MY050; previously SPG10 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | HYPOXIA |
| Reactome | 19 pathways, smallest: RHO GTPases activate KTN1; Insulin processing; Kinesins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12840](https://www.uniprot.org/uniprotkb/Q12840) (Kinesin heavy chain isoform 5A):

> Microtubule-dependent motor required for slow axonal transport of neurofilament proteins (NFH, NFM and NFL). Can induce formation of neurite-like membrane protrusions in non-neuronal cells in a ZFYVE27-dependent manner. The ZFYVE27-KIF5A complex contributes to the vesicular transport of VAPA, VAPB, SURF4, RAB11A, RAB11B and RTN3 proteins in neurons. Required for anterograde axonal transportation of MAPK8IP3/JIP3 which is essential for MAPK8IP3/JIP3 function in axon elongation.

**Summary**, from NCBI Gene [3798](https://www.ncbi.nlm.nih.gov/gene/3798):

> This gene encodes a member of the kinesin family of proteins. Members of this family are part of a multisubunit complex that functions as a microtubule motor in intracellular organelle transport. Mutations in this gene cause autosomal dominant spastic paraplegia 10. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6323) · Entrez [3798](https://www.ncbi.nlm.nih.gov/gene/3798) · UniProt [Q12840](https://www.uniprot.org/uniprotkb/Q12840) · Ensembl [ENSG00000155980](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155980)

## Data

Gene col 7938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7938); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7938]; `tensor/DDL_lfc|DDL_z.npy` [7938]; `embed/gene_vectors.npy` [7938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7938 or target_col == 7938). Every well: [[KIF5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
