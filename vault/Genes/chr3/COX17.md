---
symbol: "COX17"
type: "gene"
col: 6184
ensembl_id: "ENSG00000138495"
name: "cytochrome c oxidase copper chaperone COX17"
location: "3q13.33"
module: 48
arm: "+"
pooled_cpm: 36.25
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# COX17

*cytochrome c oxidase copper chaperone COX17* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.35× (z +7.9, q 1e-12, up in 41 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +4.1, q 0.004, up in 36 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H460 6.04×, NCI-H1573 6.64×, PANC-1 5.59×, HOP62 5.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROMO1]] (+0.79, fdr 7e-06), [[GABARAPL2]] (+0.78, fdr 7e-06), [[NDUFA1]] (+0.77, fdr 7e-06); moves opposite to [[IPO5]] (-0.67, fdr 1e-05), [[PRKDC]] (-0.66, fdr 7e-06), [[PSMG1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SELENOM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6184.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H460 6.04×, NCI-H1573 6.64×, PANC-1 5.59×, HOP62 5.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.35×** | +7.9 | 1e-12 | 41/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.70×** | +6.5 | 2e-08 | 44/47 (NCI-H23, A-172, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.76×** | +6.4 | 3e-08 | 34/37 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +4.2 | 0.003 | 36/44 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.90×** | +4.2 | 0.003 | 39/45 (LS 180, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.004 | 36/47 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.91×** | +3.9 | 0.007 | 32/39 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.69×** | +3.4 | 0.041 | 33/48 (C32, LoVo, …) | inconsistent across doses |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.60× | +3.1 | 0.11 | 33/47 (NCI-H23, Panc 03.27, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.60× | +3.1 | 0.11 | 28/47 (SW1417, KATO III, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.39× | +3.1 | 0.11 | 29/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.687× | -3.5 | 0.14 | 35/48 (LoVo, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.379× | -3.3 | 0.14 | 28/47 (SNU-1, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.603× | -3.3 | 0.14 | 38/48 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.589× | -3.2 | 0.14 | 37/48 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.395× | -3.2 | 0.14 | 35/48 (LoVo, SHP-77, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.616× | -3.2 | 0.14 | 36/48 (SW48, HS-578T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 29.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.70× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1573 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.64× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[PANC-1 (line)]] | alt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[A-172 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROMO1]] | +0.79 | +0.66 / +0.83 | both halves | 7e-06 | STRING 449 |
| [[GABARAPL2]] | +0.78 | +0.68 / +0.83 | both halves | 7e-06 |  |
| [[NDUFA1]] | +0.77 | +0.68 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 638 |
| [[MRPL33]] | +0.76 | +0.73 / +0.78 | both halves | 7e-06 | STRING 524 |
| [[MRPL51]] ⚠ | +0.76 | +0.60 / +0.79 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.74 | +0.57 / +0.82 | both halves | 8e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[RPL36AL]] ⚠ | +0.74 | +0.69 / +0.76 | both halves | 7e-06 | pathway: Protein localization; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5ME]] | +0.73 | +0.58 / +0.81 | both halves | 8e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 610 |
| [[COX4I1]] ⚠ | +0.73 | +0.70 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 616; ⚠ in the vector space only through flagged drug-doses |
| [[UQCRB]] ⚠ | +0.73 | +0.61 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 409; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1E]] | +0.73 | +0.66 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 600 |
| [[COX6B1]] | +0.72 | +0.61 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 760 |
| [[EIF1B]] | +0.72 | +0.65 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR |
| [[TMEM258]] | +0.72 | +0.58 / +0.75 | both halves | 8e-06 | pathway: Protein localization |
| [[ATP5PD]] | +0.72 | +0.57 / +0.80 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 515 |
| [[MIEN1]] | +0.71 | +0.61 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.67 | -0.57 / -0.72 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.66 | -0.60 / -0.70 | both halves | 7e-06 |  |
| [[PSMG1]] | -0.66 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[LRPPRC]] | -0.64 | -0.60 / -0.64 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[MTHFD1]] | -0.64 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[ZNF460]] | -0.64 | -0.49 / -0.69 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.63 | -0.47 / -0.70 | both halves | 2e-05 |  |
| [[PAICS]] | -0.63 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[CCT7]] | -0.63 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[CCT2]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ABCF2]] | -0.62 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[PRELID3B]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SELENOM]] | B | SELENOM activity lowers COX17's level | lines that do not express SELENOM (14) vs lines expressing it (36) | 1.21× higher at baseline in the lines without SELENOM | 0.074 | ⚠ within organs, on part of the lines; also absent: PNMA2, C3orf18, RFPL1S |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.734). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.2, -23.1); signed map (-35.7, 8.9). **Vector** length 73.7, 26.5% of its response variance represented; |z| ≥ 3 in 532 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.65 to 7); *Cytoprotection by HMOX1* (reactome, mean cos +0.58 to 9); *TP53 Regulates Metabolic Genes* (reactome, mean cos +0.56 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.1 | +6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | -0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -4.0 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -3.1 | +6.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase copper chaperone COX17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:119,654,513-119,677,454 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Hallmark sets | DNA_REPAIR, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Complex IV assembly; Mitochondrial protein import; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14061](https://www.uniprot.org/uniprotkb/Q14061) (Cytochrome c oxidase copper chaperone):

> Copper metallochaperone involved in the assembly of cytochrome c oxidase (respiratory chain complex IV, CIV). Binds two copper ions and delivers them to metallochaperones SCO1 and SCO2, which co-chaperone the copper ions to the Cu(A) site on the cytochrome c oxidase subunit II (MT-CO2/COX2), and to metallochaperone COX11 which relays the copper to the Cu(B) site on the cytochrome c oxidase subunit I (MT-CO1/COX1).

**Summary**, from NCBI Gene [10063](https://www.ncbi.nlm.nih.gov/gene/10063):

> Cytochrome c oxidase (COX), the terminal component of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. This component is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, and the nuclear-encoded subunits may function in the regulation and assembly of the complex. This nuclear …

**Accessions** — [HGNC:2264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2264) · Entrez [10063](https://www.ncbi.nlm.nih.gov/gene/10063) · UniProt [Q14061](https://www.uniprot.org/uniprotkb/Q14061) · Ensembl [ENSG00000138495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138495)

## Data

Gene col 6184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6184); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6184]; `tensor/DDL_lfc|DDL_z.npy` [6184]; `embed/gene_vectors.npy` [6184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6184 or target_col == 6184). Every well: [[COX17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
