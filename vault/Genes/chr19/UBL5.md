---
symbol: "UBL5"
type: "gene"
col: 12562
ensembl_id: "ENSG00000198258"
name: "ubiquitin like 5"
location: "19p13.2"
module: 48
arm: "+"
pooled_cpm: 53.6
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# UBL5

*ubiquitin like 5* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.31× (z +7.6, q 9e-12, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.608× (z -4.5, q 0.005, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.360×, C-33 A 0.289×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX6A1]] (+0.89, fdr 7e-06), [[COX6C]] (+0.88, fdr 7e-06), [[UQCRQ]] (+0.86, fdr 7e-06, ⚠ UQCRQ in the vector space only through flagged drug-doses), [[ATP5MK]] (+0.84, fdr 7e-06); moves opposite to [[GTF2H3]] (-0.71, fdr 7e-06), [[ZXDB]] (-0.70, fdr 7e-06), [[GUF1]] (-0.67, fdr 8e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +7.6 | 9e-12 | 47/48 (SNU-423, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **3.70×** | +7.6 | 9e-12 | 46/48 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **2.85×** | +6.4 | 2e-08 | 40/42 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.56×** | +6.0 | 3e-07 | 48/48 (NCI-H1573, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.44×** | +5.7 | 1e-06 | 48/48 (A549, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **2.12×** | +4.8 | 2e-04 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.19×** | +4.6 | 2e-04 | 38/44 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **2.06×** | +4.6 | 2e-04 | 48/48 (A549, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **2.06×** | +4.6 | 2e-04 | 43/48 (HOP62, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +4.5 | 4e-04 | 42/47 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.030 | 38/48 (BT-474, HOP62, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.70×** | +3.4 | 0.033 | 32/48 (SW480, NCI-H460, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.66×** | +3.3 | 0.049 | 36/48 (J82, C-33 A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.67×** | +3.2 | 0.060 | 30/48 (SNU-423, A-172, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.068 | 38/48 (J82, A498, …) | top dose only | position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.073 | 35/48 (CFPAC-1, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12562.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.360×, C-33 A 0.289×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.608×** | -4.5 | 0.005 | 39/48 (NCI-H2347, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.365× | -3.3 | 0.23 | 43/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 34.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[SW480 (line)]] | alt | 47.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.78× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 56.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.6) |
| [[HOP62 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.20× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.75× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[NCI-H1792 (line)]] | alt | 35.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 84.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -8.8) |
| [[PANC-1 (line)]] | alt | 53.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[SNU-423 (line)]] | alt | 49.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +8.8) | — |
| [[A-172 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 83.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 59.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6A1]] | +0.89 | +0.90 / +0.89 | both halves | 7e-06 | STRING 424 |
| [[COX6C]] | +0.88 | +0.82 / +0.88 | both halves | 7e-06 | STRING 401 |
| [[UQCRQ]] ⚠ | +0.86 | +0.78 / +0.86 | both halves | 7e-06 | STRING 508; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.84 | +0.78 / +0.85 | both halves | 7e-06 |  |
| [[NDUFA2]] | +0.83 | +0.58 / +0.86 | both halves | 7e-06 | STRING 495 |
| [[NEDD8]] | +0.83 | +0.76 / +0.83 | both halves | 7e-06 | STRING 943 |
| [[UQCR11]] | +0.83 | +0.86 / +0.76 | both halves | 7e-06 | STRING 515 |
| [[COX6B1]] | +0.82 | +0.71 / +0.87 | both halves | 7e-06 | STRING 477 |
| [[ROMO1]] | +0.82 | +0.77 / +0.82 | both halves | 7e-06 | STRING 482 |
| [[NDUFA4]] | +0.80 | +0.74 / +0.83 | both halves | 7e-06 |  |
| [[ATP5F1E]] | +0.80 | +0.75 / +0.82 | both halves | 7e-06 |  |
| [[ATP5PF]] | +0.79 | +0.72 / +0.82 | both halves | 7e-06 |  |
| [[ATOX1]] | +0.79 | +0.69 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.71 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[ZXDB]] | -0.70 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[GUF1]] | -0.67 | -0.65 / -0.58 | both halves | 8e-06 |  |
| [[DCLRE1A]] | -0.67 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[TEX261]] | -0.66 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[IMPACT]] | -0.66 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[BACE1-AS]] | -0.66 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.66 | -0.59 / -0.59 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[PSMG1]] | -0.65 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[SRSF6]] | -0.64 | -0.48 / -0.66 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ZNF460]] | -0.64 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[MAGOHB]] | -0.64 | -0.60 / -0.49 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBL5's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.919). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.2, -22.2); signed map (-34.8, 9.7). **Vector** length 84.7, 39.1% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.70 to 31); *Respiratory electron transport* (reactome, mean cos +0.69 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.71 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +5.5 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +5.0 | +3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | -1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.4 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -5.5 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -5.0 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:9,827,892-9,830,115 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZL1](https://www.uniprot.org/uniprotkb/Q9BZL1) (Ubiquitin-like protein 5):

> Ubiquitin-like protein that plays a role in cell proliferation and sister chromatid cohesion by associating with spliceosomal proteins. Participates thereby in pre-mRNA splicing by maintaining spliceosome integrity. Promotes the functional integrity of the Fanconi anemia DNA repair pathway by interacting with FANCI component and subsequently mediating the formation of FANCI homodimers. Also plays a protective role against ER stress-induced apoptosis.

**Summary**, from NCBI Gene [59286](https://www.ncbi.nlm.nih.gov/gene/59286):

> This gene encodes a member of a group of proteins similar to ubiquitin. The encoded protein is not thought to degrade proteins like ubiquitin but to affect their function through being bound to target proteins by an isopeptide bond. The gene product has been studied as a link to predisposition to obesity based on its expression in Psammomys obesus, the fat sand rat, which is an animal model for obesity studies. Variation in this gene was found to be significantly associated with some metabolic …

**Accessions** — [HGNC:13736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13736) · Entrez [59286](https://www.ncbi.nlm.nih.gov/gene/59286) · UniProt [Q9BZL1](https://www.uniprot.org/uniprotkb/Q9BZL1) · Ensembl [ENSG00000198258](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198258)

## Data

Gene col 12562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12562); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12562]; `tensor/DDL_lfc|DDL_z.npy` [12562]; `embed/gene_vectors.npy` [12562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12562 or target_col == 12562). Every well: [[UBL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
