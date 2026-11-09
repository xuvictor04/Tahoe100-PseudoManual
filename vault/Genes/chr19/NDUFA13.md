---
symbol: "NDUFA13"
type: "gene"
col: 11766
ensembl_id: "ENSG00000186010"
name: "NADH:ubiquinone oxidoreductase subunit A13"
location: "19p13.11"
module: 48
arm: "+"
pooled_cpm: 42.16
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/048", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# NDUFA13

*NADH:ubiquinone oxidoreductase subunit A13* — 19p13.11

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.08× (z +9.1, q 4e-17, up in 43 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SNU-423 4.73×, NCI-H1792 4.82×, SW480 3.60×, NCI-H460 3.72×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS9]] (+0.74, fdr 7e-06), [[NDUFB2]] (+0.72, fdr 1e-05), [[COX17]] (+0.71, fdr 7e-06); moves opposite to [[PRELID3B]] (-0.64, fdr 1e-05), [[IPO5]] (-0.61, fdr 1e-05), [[AZIN1]] (-0.60, fdr 9e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IL27RA]] → it (grade C ⚠); 1 goes from it, the strongest it → [[RPL36AL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11766.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SNU-423 4.73×, NCI-H1792 4.82×, SW480 3.60×, NCI-H460 3.72×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.08×** | +9.1 | 4e-17 | 43/47 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.49×** | +7.1 | 3e-10 | 32/40 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.16×** | +6.2 | 8e-08 | 45/47 (NCI-H460, SHP-77, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +6.1 | 2e-07 | 44/47 (A498, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.95×** | +5.0 | 8e-05 | 38/45 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.56×** | +3.6 | 0.028 | 32/48 (SW480, NCI-H1573, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.55×** | +3.6 | 0.030 | 29/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.48×** | +3.2 | 0.098 | 30/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.646× | -3.2 | 0.34 | 32/48 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.663× | -3.0 | 0.34 | 36/48 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.465× | -3.0 | 0.34 | 29/48 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 48.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[COLO 205 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H460 (line)]] | wt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[PANC-1 (line)]] | alt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 14 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS9]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[NDUFB2]] | +0.72 | +0.53 / +0.76 | both halves | 1e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 997 |
| [[COX17]] | +0.71 | +0.69 / +0.73 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 437 |
| [[NDUFB11]] ⚠ | +0.70 | +0.67 / +0.73 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA1]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 999 |
| [[COX7A2]] ⚠ | +0.70 | +0.59 / +0.79 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 731; ⚠ in the vector space only through flagged drug-doses |
| [[RBX1]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 997 |
| [[COX6B1]] | +0.69 | +0.64 / +0.81 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 957 |
| [[NDUFB1]] | +0.68 | +0.56 / +0.75 | both halves | 1e-05 | same gene group; pathway: Aerobic respiration and respiratory electron transport; STRING 998 |
| [[NDUFA4]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 989 |
| [[ZCCHC10]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ATP5MF]] | +0.67 | +0.58 / +0.76 | both halves | 8e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 869 |
| [[ROMO1]] | +0.67 | +0.65 / +0.82 | both halves | 7e-06 | STRING 741 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID3B]] | -0.64 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[IPO5]] | -0.61 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[AZIN1]] | -0.60 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[SPTBN1]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[DNAJC10]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[EIF2AK1]] | -0.57 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[TCP1]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[EIF4H]] | -0.54 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[CS]] | -0.54 | -0.42 / -0.57 | both halves | 4e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[TWF1]] | -0.54 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[HNRNPA1]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[NONO]] | -0.53 | -0.38 / -0.69 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL27RA]] | C | IL27RA activity raises NDUFA13's level | lines that do not express IL27RA (3) vs lines expressing it (47) | 1.34× lower at baseline in the lines without IL27RA | 0.069 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ITGA2B, TMEM132A, CLEC2D; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPL36AL]] | C | NDUFA13's natural level strengthens RPL36AL's drug response | NDUFA13's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.02; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-47.5, -21.8); signed map (-36.2, 9.4). **Vector** length 56.6, 17.1% of its response variance represented; |z| ≥ 3 in 472 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *oxidative phosphorylation* (hallmark, mean cos +0.56 to 24); *Complex IV assembly* (reactome, mean cos +0.53 to 11); *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.4 | +6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.8 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.6 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.3 | +1.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.3 | +2.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | +1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -1.7 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | +0.8 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,515,736-19,529,054 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-39, CDA016, GRIM-19, GRIM19, B16.6 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Reactome | 4 pathways, smallest: Complex I biogenesis; Mitochondrial protein degradation; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0J0](https://www.uniprot.org/uniprotkb/Q9P0J0) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Involved in the interferon/all-trans-retinoic acid (IFN/RA) induced cell death. This apoptotic activity is inhibited by interaction with viral IRF1. Prevents the transactivation of STAT3 …

**Summary**, from NCBI Gene [51079](https://www.ncbi.nlm.nih.gov/gene/51079):

> This gene encodes a subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), which functions in the transfer of electrons from NADH to the respiratory chain. The protein is required for complex I assembly and electron transfer activity. The protein binds the signal transducers and activators of transcription 3 (STAT3) transcription factor, and can function as a tumor suppressor. The human protein purified from mitochondria migrates at approximately 16 kDa. …

**Accessions** — [HGNC:17194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17194) · Entrez [51079](https://www.ncbi.nlm.nih.gov/gene/51079) · UniProt [Q9P0J0](https://www.uniprot.org/uniprotkb/Q9P0J0) · Ensembl [ENSG00000186010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186010)

## Data

Gene col 11766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11766); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11766]; `tensor/DDL_lfc|DDL_z.npy` [11766]; `embed/gene_vectors.npy` [11766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11766 or target_col == 11766). Every well: [[NDUFA13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
