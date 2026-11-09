---
symbol: "EXOSC5"
type: "gene"
col: 1184
ensembl_id: "ENSG00000077348"
name: "exosome component 5"
location: "19q13.2"
module: 33
arm: "+"
pooled_cpm: 8.1
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# EXOSC5

*exosome component 5* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.52× (z +9.6, q 5e-19, up in 26 of 30 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.59× (z +5.2, q 4e-05, up in 18 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.521× (z -9.7, q 3e-19, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLE1]] (+0.71, fdr 1e-05), [[DHODH]] (+0.70, fdr 7e-06), [[NARS2]] (+0.70, fdr 1e-05); moves opposite to [[CCDC90B-AS1]] (-0.53, fdr 1e-04), [[C2]] (-0.53, fdr 2e-04), [[NPHS1]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.52×** | +9.6 | 5e-19 | 26/30 (NCI-H460, HT-29, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.2 | 1e-10 | 14/21 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.86×** | +6.2 | 1e-07 | 9/16 (SW480, HT-29, …) | all doses, flat | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.59×** | +5.2 | 4e-05 | 18/42 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.61×** | +4.9 | 1e-04 | 15/36 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.6 | 3e-04 | 21/35 (Panc 03.27, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +4.6 | 3e-04 | 19/45 (NCI-H1792, A549, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.50×** | +4.2 | 0.002 | 17/45 (A-172, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.44×** | +3.6 | 0.021 | 11/35 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.65×** | +3.4 | 0.034 | 7/35 (A498, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.84×** | +3.3 | 0.051 | 10/45 (SHP-77, KATO III, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.069 | 5/45 (A498, NCI-H23, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.1 | 0.074 | 1/47 (KATO III) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.081 | 10/42 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.521×** | -9.7 | 3e-19 | 35/43 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -8.5 | 6e-15 | 31/41 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.563×** | -6.0 | 3e-07 | 23/45 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.625×** | -4.9 | 1e-04 | 22/45 (SNU-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.621×** | -4.7 | 2e-04 | 21/44 (A498, AN3 CA, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.638×** | -4.7 | 2e-04 | 20/44 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.693×** | -3.7 | 0.018 | 16/45 (SW1417, A-172, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.716×** | -3.5 | 0.031 | 14/45 (SW48, A549, …) | all doses, flat |  |
| [[Ciclopirox (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.039 | 11/45 (CFPAC-1, SK-MEL-2, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.613×** | -3.4 | 0.042 | 4/47 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.616×** | -3.3 | 0.044 | 7/45 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.734×** | -3.3 | 0.053 | 16/45 (KATO III, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.730×** | -3.2 | 0.065 | 11/44 (SNU-1, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 9.83 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -13.8) |
| [[SW480 (line)]] | alt | 11.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.5) |
| [[PANC-1 (line)]] | alt | 9.08 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -11.5) |
| [[RKO (line)]] | wt | 13.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -13.2) |
| [[A498 (line)]] | wt | 7.33 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.129× (z -10.7) |
| [[C-33 A (line)]] | alt | 10.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -11.7) |
| [[Hs 766T (line)]] | wt | 4.51 | 0 | 1 | — | [[Fusidic acid (drug)]] 0.5 µM 0.0733× (z -9.0) |
| [[KATO III (line)]] | alt | 8.20 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.204× (z -9.4) |
| [[LS 180 (line)]] | wt | 6.45 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 11.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0590× (z -19.1) |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.203× (z -10.3) |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0311× (z -11.8) |
| [[SW48 (line)]] | wt | 11.8 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0634× (z -9.8) |
| [[A-172 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLE1]] | +0.71 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[DHODH]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[NARS2]] | +0.70 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[POLR1B]] | +0.69 | +0.82 / +0.52 | both halves | 1e-05 |  |
| [[RCL1]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 880 |
| [[MRPL4]] | +0.66 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[WDR3]] | +0.66 | +0.78 / +0.50 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 851 |
| [[BRAT1]] | +0.66 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[WDR36]] | +0.66 | +0.73 / +0.49 | both halves | 1e-05 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 735 |
| [[SCAP]] | +0.65 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ASB13]] | +0.65 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[FXN]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | -0.53 | -0.38 / -0.32 | both halves | 1e-04 |  |
| [[C2]] | -0.53 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[NPHS1]] | -0.53 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[ESR2]] | -0.53 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[EFCAB5]] | -0.53 | -0.41 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises EXOSC5's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.52× lower at baseline in the lines without PODXL2 | 0.019 | ⚠ within organs, on part of the lines |
| [[C2]] | C | C2's natural level weakens EXOSC5's drug response | C2's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.22; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.2, -41.7); signed map (-8.0, -51.8). **Vector** length 80.7, 16.8% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.59 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.4 | +4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.7 | +3.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.2 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -9.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,386,371-41,397,362 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hRrp46p, Rrp46p, RRP46, RRP41B, MGC12901, p12B |
| Gene groups (HGNC) | Exosome complex |
| Hallmark sets | MYC_TARGETS_V2, UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQT4](https://www.uniprot.org/uniprotkb/Q9NQT4) (Exosome complex component RRP46):

> Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [56915](https://www.ncbi.nlm.nih.gov/gene/56915):

> Predicted to enable RNA binding activity. Involved in DNA deamination; RNA processing; and mRNA catabolic process. Acts upstream of or within defense response to virus. Located in cytosol; euchromatin; and nucleolus. Part of exosome (RNase complex). [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24662) · Entrez [56915](https://www.ncbi.nlm.nih.gov/gene/56915) · UniProt [Q9NQT4](https://www.uniprot.org/uniprotkb/Q9NQT4) · Ensembl [ENSG00000077348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077348)

## Data

Gene col 1184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1184); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1184]; `tensor/DDL_lfc|DDL_z.npy` [1184]; `embed/gene_vectors.npy` [1184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1184 or target_col == 1184). Every well: [[EXOSC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
