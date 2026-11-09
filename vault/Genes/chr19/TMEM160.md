---
symbol: "TMEM160"
type: "gene"
col: 5114
ensembl_id: "ENSG00000130748"
name: "transmembrane protein 160"
location: "19q13.32"
module: 58
arm: "+"
pooled_cpm: 7.54
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# TMEM160

*transmembrane protein 160* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.34× (z +8.0, q 5e-13, up in 13 of 13 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.80× (z +3.3, q 0.070, up in 17 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.371× (z -8.0, q 9e-13, down in 34 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (NCI-H2347 0.0938×, SW 900 0.0774×, SW480 0.160×, SW1417 0.164×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LoVo 0.0262×, SW480 0.100×, Panc 03.27 0.0787×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANTKMT]] (+0.80, fdr 7e-06), [[NDUFA3]] (+0.79, fdr 7e-06), [[NDUFS8]] (+0.78, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.69, fdr 1e-05), [[SRRM2]] (-0.69, fdr 7e-06), [[ZNF564]] (-0.66, fdr 2e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MNX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5114.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **4.34×** | +8.0 | 5e-13 | 13/13 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **5.12×** | +8.0 | 5e-13 | 27/28 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.22×** | +6.1 | 1e-07 | 19/21 (LS 180, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **2.25×** | +4.6 | 6e-04 | 22/34 (HS-578T, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.00×** | +3.9 | 0.009 | 26/46 (LOX-IMVI, CFPAC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.4 | 0.056 | 16/34 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +3.3 | 0.070 | 17/42 (C-33 A, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.81×** | +3.2 | 0.075 | 19/42 (NCI-H2030, NCI-H460, …) | top dose only | position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.49×** | +3.2 | 0.075 | 19/46 (Panc 03.27, A-427, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +3.2 | 0.075 | 13/47 (NCI-H2030, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.71× | +3.1 | 0.11 | 15/46 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | 1.74× | +3.0 | 0.11 | 17/44 (A549, NCI-H2030, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | 1.74× | +3.0 | 0.11 | 10/34 (A-172, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5114.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (NCI-H2347 0.0938×, SW 900 0.0774×, SW480 0.160×, SW1417 0.164×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LoVo 0.0262×, SW480 0.100×, Panc 03.27 0.0787×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.371×** | -8.0 | 9e-13 | 34/42 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.322×** | -6.4 | 4e-08 | 30/39 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.586× | -3.0 | 0.42 | 22/45 (SNU-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5114. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.83 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -11.5) |
| [[HT-29 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -8.7) |
| [[KATO III (line)]] | alt | 6.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -8.6) |
| [[LoVo (line)]] | wt | 5.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0262× (z -12.7) |
| [[LS 180 (line)]] | wt | 8.11 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 16.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 9.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0938× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 8.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0787× (z -8.8) |
| [[SHP-77 (line)]] | alt | 8.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -10.5) |
| [[SW 900 (line)]] | alt | 7.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0774× (z -11.5) |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -10.8) |
| [[A-172 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5114), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTKMT]] | +0.80 | +0.61 / +0.77 | both halves | 7e-06 | STRING 436 |
| [[NDUFA3]] | +0.79 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[NDUFS8]] | +0.78 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[CENPX]] | +0.77 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.75 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[MRPL41]] ⚠ | +0.73 | +0.43 / +0.72 | both halves | 3e-05 | STRING 427; ⚠ in the vector space only through flagged drug-doses |
| [[TMEM256]] | +0.72 | +0.52 / +0.63 | both halves | 1e-05 | STRING 442 |
| [[METRN]] | +0.71 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[MICOS13]] | +0.69 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[SNRPD2]] | +0.69 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | +0.68 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ELOB]] | +0.68 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[NDUFS7]] | +0.67 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.69 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[SRRM2]] | -0.69 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[ZNF564]] | -0.66 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[TUG1]] | -0.64 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.64 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[EIF5]] | -0.63 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[ZNF655]] | -0.63 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[DDX39B]] | -0.62 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[RNF6]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZNF543]] | -0.61 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MMADHC-DT]] | -0.60 | -0.59 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ZXDA]] | -0.60 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[PIEZO1]] | -0.60 | -0.47 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MNX1]] | B | MNX1 activity raises TMEM160's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without MNX1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |
| [[HDAC6]] | B | HDAC6 activity lowers TMEM160's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.835). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.3, -19.1); signed map (-37.0, 6.6). **Vector** length 61.6, 13.7% of its response variance represented; |z| ≥ 3 in 595 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.55 to 12); *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.58 to 12); *Complex I biogenesis* (reactome, mean cos +0.66 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.4 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.3 | +3.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.2 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.3 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 160 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,045,909-47,048,624 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20512 |
| Matched by | ensembl_id |

UniProt [Q9NX00](https://www.uniprot.org/uniprotkb/Q9NX00) carries no function annotation.

**Summary**, from NCBI Gene [54958](https://www.ncbi.nlm.nih.gov/gene/54958):

> Located in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26042) · Entrez [54958](https://www.ncbi.nlm.nih.gov/gene/54958) · UniProt [Q9NX00](https://www.uniprot.org/uniprotkb/Q9NX00) · Ensembl [ENSG00000130748](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130748)

## Data

Gene col 5114: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5114); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5114, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5114]; `tensor/DDL_lfc|DDL_z.npy` [5114]; `embed/gene_vectors.npy` [5114]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5114 or target_col == 5114). Every well: [[TMEM160 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM160.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
