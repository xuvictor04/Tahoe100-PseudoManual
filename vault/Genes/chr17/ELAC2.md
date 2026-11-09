---
symbol: "ELAC2"
type: "gene"
col: 128
ensembl_id: "ENSG00000006744"
name: "elaC ribonuclease Z 2"
location: "17p12"
module: 4
arm: "+"
pooled_cpm: 17.03
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ELAC2

*elaC ribonuclease Z 2* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.25× (z +13.4, q 3e-38, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.805× (z -3.6, q 0.096, down in 17 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.214×, A498 0.552×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SW48 0.126×, NCI-H23 0.216×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.107×; ⚠ cell-cycle shift, would explain all of this change); [[Belzutifan (drug)]] 5 µM in 1 line (SHP-77 0.0482×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (COLO 205 0.0725×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPS1]] (+0.81, fdr 7e-06), [[DROSHA]] (+0.78, fdr 7e-06), [[HERC2]] (+0.77, fdr 7e-06); moves opposite to [[ACAP1]] (-0.69, fdr 7e-06), [[RSRP1]] (-0.66, fdr 1e-05), [[KDM5B]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.25×** | +13.4 | 3e-38 | 43/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.10×** | +11.7 | 2e-29 | 18/27 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.04×** | +11.1 | 3e-26 | 41/48 (MIA PaCa-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.95×** | +11.0 | 3e-26 | 39/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.94×** | +11.0 | 7e-26 | 33/39 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +10.6 | 3e-24 | 26/33 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.84×** | +10.1 | 5e-22 | 34/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.80×** | +9.7 | 2e-20 | 32/47 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.67×** | +8.4 | 2e-15 | 32/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +7.4 | 7e-12 | 21/46 (RPMI-7951, C32, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.56×** | +7.1 | 9e-11 | 29/47 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +5.3 | 7e-06 | 21/41 (SW 900, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.1 | 1e-05 | 18/38 (NCI-H460, LS 180, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +5.0 | 2e-05 | 15/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.7 | 8e-05 | 14/48 (HS-578T, NCI-H460, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.34×** | +4.6 | 2e-04 | 18/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.011 | 13/47 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.024 | 10/46 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.039 | 8/48 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.042 | 13/47 (CFPAC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.044 | 8/43 (C32, SNU-423, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 128.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.214×, A498 0.552×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (SW48 0.126×, NCI-H23 0.216×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.107×; ⚠ cell-cycle shift, would explain all of this change); [[Belzutifan (drug)]] 5 µM in 1 line (SHP-77 0.0482×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (COLO 205 0.0725×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.805×** | -3.6 | 0.096 | 17/47 (A498, SNU-1, …) | two highest doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.859× | -3.6 | 0.096 | 12/48 (RKO, A-172, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.878× | -3.1 | 0.39 | 13/48 (COLO 205, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 13.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.18× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.216× (z -9.6) |
| [[SW480 (line)]] | alt | 24.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A498 (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 9.10 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0725× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.104× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 20.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +8.9) | — |
| [[RKO (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 37.4 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0482× (z -11.5) |
| [[SW48 (line)]] | wt | 23.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.126× (z -10.3) |
| [[A-172 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS1]] | +0.81 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[DROSHA]] | +0.78 | +0.66 / +0.76 | both halves | 7e-06 | same gene group; pathway: Gene Silencing by RNA; STRING 512 |
| [[HERC2]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.75 | +0.67 / +0.76 | both halves | 7e-06 | pathway: rRNA processing; STRING 469 |
| [[NUDC]] | +0.74 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[WDR77]] | +0.72 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[LETM1]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 | STRING 427 |
| [[CCT5]] | +0.71 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[PRPF19]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.71 | +0.63 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAP1]] | -0.69 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.66 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.64 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[TESK2]] | -0.64 | -0.63 / -0.57 | both halves | 8e-06 |  |
| [[ZNF821]] | -0.63 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.62 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[TNRC6C]] | -0.62 | -0.60 / -0.57 | both halves | 1e-05 | pathway: Gene Silencing by RNA |
| [[C4orf47]] | -0.61 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[STX5-DT]] | -0.61 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[POLH]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.61 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity lowers ELAC2's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.37× higher at baseline in the lines without AGR2 | 0.052 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.804). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.0, -32.5); signed map (-12.4, -46.9). **Vector** length 93.8, 19.8% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA Aminoacylation* (reactome, mean cos +0.51 to 7); *Folding of actin by CCT/TriC* (reactome, mean cos +0.58 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.3 | +13.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +10.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.9 | +11.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +5.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.0 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | elaC ribonuclease Z 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:12,991,612-13,018,065 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10530, HPC2 |
| Gene groups (HGNC) | MBL fold containing DNA/RNA interacting subfamily; Endoribonucleases |
| Reactome | 8 pathways, smallest: tRNA-derived small RNA (tsRNA or tRNA-related fragment, tRF) biogenesis; tRNA processing in the mitochondrion; rRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ52](https://www.uniprot.org/uniprotkb/Q9BQ52) (Zinc phosphodiesterase ELAC protein 2):

> Zinc phosphodiesterase, which displays mitochondrial tRNA 3'-processing endonuclease activity. Involved in tRNA maturation, by removing a 3'-trailer from precursor tRNA. Associates with mitochondrial DNA complexes at the nucleoids to initiate RNA processing and ribosome assembly.

**Summary**, from NCBI Gene [60528](https://www.ncbi.nlm.nih.gov/gene/60528):

> The protein encoded by this gene has a C-terminal domain with tRNA 3&#8242; processing endoribonuclease activity, which catalyzes the removal of the 3' trailer from precursor tRNAs. The protein also interacts with activated Smad family member 2 (Smad2) and its nuclear partner forkhead box H1 (also known as FAST-1), and reduced expression can suppress transforming growth factor-beta induced growth arrest. Mutations in this gene result in an increased risk of prostate cancer. Multiple transcript …

**Accessions** — [HGNC:14198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14198) · Entrez [60528](https://www.ncbi.nlm.nih.gov/gene/60528) · UniProt [Q9BQ52](https://www.uniprot.org/uniprotkb/Q9BQ52) · Ensembl [ENSG00000006744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006744)

## Data

Gene col 128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 128); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 128]; `tensor/DDL_lfc|DDL_z.npy` [128]; `embed/gene_vectors.npy` [128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 128 or target_col == 128). Every well: [[ELAC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELAC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
