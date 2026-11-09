---
symbol: "SAP30"
type: "gene"
col: 8869
ensembl_id: "ENSG00000164105"
name: "Sin3A associated protein 30"
location: "4q34.1"
module: 79
arm: "+"
pooled_cpm: 22.67
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# SAP30

*Sin3A associated protein 30* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.87× (z +5.7, q 8e-06, up in 33 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Sodium Salicylate (drug)]] 5 µM: 1.33× (z +3.6, q 0.040, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 4.96×, SW480 3.64×; ⚠ cell-cycle shift, explains ~58% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 4.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.721× (z -4.2, q 0.011, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~95% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 0.452× (z -3.8, q 0.032, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.113×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.275×; ⚠ cell-cycle shift, explains ~95% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FUT11]] (+0.71, fdr 7e-06), [[VEGFB]] (+0.67, fdr 7e-06), [[HILPDA]] (+0.66, fdr 7e-06); moves opposite to [[TMX3]] (-0.61, fdr 3e-05), [[NRAS]] (-0.59, fdr 3e-05), [[ABCF2]] (-0.58, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PIAS2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8869.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (LS 180 4.96×, SW480 3.64×; ⚠ cell-cycle shift, explains ~58% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (SW480 4.04×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.87×** | +5.7 | 8e-06 | 33/46 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.70×** | +4.8 | 4e-04 | 32/48 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **1.50×** | +3.7 | 0.040 | 25/46 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Sodium Salicylate (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.040 | 22/48 (A498, HOP62, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.30×** | +3.4 | 0.085 | 29/48 (NCI-H2347, LS 180, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.44×** | +3.3 | 0.089 | 21/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8869.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.113×; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 1 line (LS 180 0.275×; ⚠ cell-cycle shift, explains ~95% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **0.721×** | -4.2 | 0.011 | 28/48 (LS 180, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.618×** | -4.1 | 0.011 | 30/48 (C32, HS-578T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.452×** | -3.8 | 0.032 | 34/48 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.687× | -3.1 | 0.21 | 21/39 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.709× | -3.1 | 0.21 | 21/48 (A498, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.72 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8869. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 16.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.96× (z +9.1) ⚠ cell-cycle shift, explains ~58% of this change | [[Selinexor (drug)]] 5 µM 0.275× (z -10.3) ⚠ cell-cycle shift, explains ~95% of this change |
| [[SW480 (line)]] | alt | 26.0 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.04× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H460 (line)]] | wt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -13.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8869), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUT11]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[VEGFB]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[TRIM7-AS2]] | +0.66 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[SAP30-DT]] | +0.65 | +0.73 / +0.58 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DEPP1]] | +0.65 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MXI1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[KRTCAP2]] | +0.64 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[ING2]] | +0.64 | +0.49 / +0.72 | both halves | 1e-05 | STRING 992 |
| [[KDM3A]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[LAMTOR5]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[PEX3]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX3]] | -0.61 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[NRAS]] | -0.59 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ABCF2]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[PSMD12]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.57 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[CCT2]] | -0.57 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[PSMD1]] | -0.56 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[TUBA8]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[TMEM33]] | -0.56 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[DCTD]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MAPKAP1]] | -0.56 | -0.46 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIAS2]] | C | SAP30's natural level strengthens PIAS2's drug response | SAP30's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.11; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, -17.4); signed map (-32.8, 25.0). **Vector** length 105, 30.9% of its response variance represented; |z| ≥ 3 in 573 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.7 | +4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +3.2 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +2.9 | +3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.0 | +1.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.0 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +0.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.2 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.3 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.2 | -1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | -5.2 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -4.8 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | Sin3A associated protein 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.1 — chr4:173,369,969-173,377,532 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SIN3 histone deacetylase complex subunits |
| Hallmark sets | NOTCH_SIGNALING, GLYCOLYSIS, HYPOXIA, G2M_CHECKPOINT |
| Reactome | 9 pathways, smallest: HDACs deacetylate histones; NoRC negatively regulates rRNA expression; Negative epigenetic regulation of rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [O75446](https://www.uniprot.org/uniprotkb/O75446) (Histone deacetylase complex subunit SAP30):

> Involved in the functional recruitment of the Sin3-histone deacetylase complex (HDAC) to a specific subset of N-CoR corepressor complexes. Capable of transcription repression by N-CoR. Active in deacetylating core histone octamers (when in a complex) but inactive in deacetylating nucleosomal histones.; (Microbial infection) Involved in transcriptional repression of HHV-1 genes TK and gC.

**Summary**, from NCBI Gene [8819](https://www.ncbi.nlm.nih.gov/gene/8819):

> Histone acetylation plays a key role in the regulation of eukaryotic gene expression. Histone acetylation and deacetylation are catalyzed by multisubunit complexes. The protein encoded by this gene is a component of the histone deacetylase complex, which includes SIN3, SAP18, HDAC1, HDAC2, RbAp46, RbAp48, and other polypeptides. This complex is active in deacetylating core histone octamers, but inactive in deacetylating nucleosomal histones. A pseudogene of this gene is located on chromosome 3. …

**Accessions** — [HGNC:10532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10532) · Entrez [8819](https://www.ncbi.nlm.nih.gov/gene/8819) · UniProt [O75446](https://www.uniprot.org/uniprotkb/O75446) · Ensembl [ENSG00000164105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164105)

## Data

Gene col 8869: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8869); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8869, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8869]; `tensor/DDL_lfc|DDL_z.npy` [8869]; `embed/gene_vectors.npy` [8869]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8869 or target_col == 8869). Every well: [[SAP30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAP30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
