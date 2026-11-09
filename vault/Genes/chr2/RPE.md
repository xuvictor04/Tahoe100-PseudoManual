---
symbol: "RPE"
type: "gene"
col: 12446
ensembl_id: "ENSG00000197713"
name: "ribulose-5-phosphate-3-epimerase"
location: "2q34"
module: 4
arm: "+"
pooled_cpm: 34.82
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RPE

*ribulose-5-phosphate-3-epimerase* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.55× (z +5.9, q 2e-06, up in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.36× (z +4.2, q 0.004, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.711× (z -6.6, q 3e-08, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~60% of this change. The strongest without an alert is [[Sodium Salicylate (drug)]] 5 µM: 0.824× (z -3.8, q 0.050, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (MIA PaCa-2 0.169×, LoVo 0.330×, SK-MEL-2 0.321×, NCI-H1792 0.274×, …; ⚠ cell-cycle shift, explains ~60% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HCT15 0.112×, SK-MEL-2 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Bortezomib (drug)]] 5 µM in 1 line (A-427 0.103×; ⚠ toxic; cell-cycle shift, explains ~87% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPS1]] (+0.77, fdr 7e-06), [[MRPL42]] (+0.75, fdr 7e-06), [[GOT2]] (+0.75, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.71, fdr 7e-06), [[TNRC6C]] (-0.69, fdr 7e-06), [[SPATC1]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NUP210]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.55×** | +5.9 | 2e-06 | 31/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +5.5 | 9e-06 | 38/48 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.40×** | +4.6 | 9e-04 | 28/48 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.37×** | +4.2 | 0.003 | 26/48 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.004 | 27/47 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.34×** | +4.0 | 0.007 | 23/47 (PANC-1, HOP62, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.019 | 22/48 (H4, LoVo, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +3.6 | 0.023 | 20/48 (NCI-H2030, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.024 | 18/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.032 | 18/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.057 | 20/48 (PANC-1, HS-578T, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.28×** | +3.2 | 0.057 | 16/38 (NCI-H460, A549, …) | inconsistent across doses | composition shift |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.097 | 14/47 (A-172, SHP-77, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.097 | 16/48 (CFPAC-1, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12446.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (MIA PaCa-2 0.169×, LoVo 0.330×, SK-MEL-2 0.321×, NCI-H1792 0.274×, …; ⚠ cell-cycle shift, explains ~60% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HCT15 0.112×, SK-MEL-2 0.136×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change); [[Bortezomib (drug)]] 5 µM in 1 line (A-427 0.103×; ⚠ toxic; cell-cycle shift, explains ~87% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.711×** | -6.6 | 3e-08 | 36/47 (MIA PaCa-2, LoVo, …) | top dose only | composition shift |
| [[Sodium Salicylate (drug)]] 5 µM |  | **0.824×** | -3.8 | 0.050 | 22/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.841× | -3.4 | 0.14 | 18/48 (NCI-H661, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.3 | 0.14 | 19/48 (SNU-1, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[A-427 (line)]] | wt | 35.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.103× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~87% of this change |
| [[C32 (line)]] | wt | 56.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -8.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HCT15 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[LoVo (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -19.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -11.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H460 (line)]] | wt | 38.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[RKO (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[A-172 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 44.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS1]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 600 |
| [[MRPL42]] | +0.75 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[GOT2]] | +0.75 | +0.71 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[PRKDC]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[PAICS]] | +0.73 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.72 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[RFT1]] | +0.71 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[PRPF19]] | +0.71 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[EMC1]] | +0.71 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[PPT1]] | +0.70 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[PHB1]] | +0.70 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[EEF1E1]] | +0.70 | +0.73 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.71 | -0.63 / -0.73 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.69 | -0.67 / -0.68 | both halves | 7e-06 |  |
| [[SPATC1]] | -0.69 | -0.61 / -0.72 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.68 | -0.61 / -0.73 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.68 | -0.64 / -0.75 | both halves | 7e-06 |  |
| [[ACAP1]] | -0.68 | -0.65 / -0.69 | both halves | 7e-06 |  |
| [[TESK2]] | -0.67 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[STARD10]] | -0.66 | -0.58 / -0.70 | both halves | 8e-06 |  |
| [[TMEM106A]] | -0.66 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[CCNP]] | -0.66 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.66 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[OFD1]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity raises RPE's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.33× lower at baseline in the lines without NUP210 | 0.023 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[TPBG]] | B | TPBG activity strengthens RPE's drug response | lines that do not express TPBG (10) vs lines expressing it (38) | the lines without TPBG respond 0.60× as strongly (z diff +0.72); strongest at Belinostat 5 µM: 1.28x vs 1.65x (z diff +1.8) | 0.068 | ⚠ within organs, on part of the lines; target measured in part of the lines; artifact flags |
| [[DUXAP8]] | B | DUXAP8 activity raises RPE's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without DUXAP8 | 0.069 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.4, -34.0); signed map (-16.2, -45.4). **Vector** length 102, 25.3% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.52 to 8); *Folding of actin by CCT/TriC* (reactome, mean cos +0.57 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.52 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.1 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | +3.3 | +1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +3.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | +2.9 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -11.2 | -6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -0.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | -2.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.1 | -2.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ribulose-5-phosphate-3-epimerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:210,002,565-210,022,260 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 2 pathways, smallest: Pentose phosphate pathway; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AT9](https://www.uniprot.org/uniprotkb/Q96AT9) (Ribulose-phosphate 3-epimerase):

> Catalyzes the reversible epimerization of D-ribulose 5-phosphate to D-xylulose 5-phosphate.

**Summary**, from NCBI Gene [6120](https://www.ncbi.nlm.nih.gov/gene/6120):

> Enables D-ribulose-phosphate 3-epimerase activity; metal ion binding activity; and protein homodimerization activity. Involved in carbohydrate metabolic process and pentose-phosphate shunt. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10293) · Entrez [6120](https://www.ncbi.nlm.nih.gov/gene/6120) · UniProt [Q96AT9](https://www.uniprot.org/uniprotkb/Q96AT9) · Ensembl [ENSG00000197713](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197713)

## Data

Gene col 12446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12446); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12446]; `tensor/DDL_lfc|DDL_z.npy` [12446]; `embed/gene_vectors.npy` [12446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12446 or target_col == 12446). Every well: [[RPE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
