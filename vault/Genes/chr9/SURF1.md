---
symbol: "SURF1"
type: "gene"
col: 7257
ensembl_id: "ENSG00000148290"
name: "SURF1 cytochrome c oxidase assembly factor"
location: "9q34.2"
module: 56
arm: "+"
pooled_cpm: 7.18
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SURF1

*SURF1 cytochrome c oxidase assembly factor* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.13× (z +11.1, q 1e-25, up in 31 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +9.7, q 1e-19, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.523× (z -6.9, q 3e-09, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH5]] (+0.55, fdr 1e-04), [[CCNK]] (+0.55, fdr 4e-05), [[COPB2]] (+0.54, fdr 3e-05); moves opposite to [[INTS7]] (-0.52, fdr 6e-05), [[NOP56]] (-0.50, fdr 1e-04), [[SRSF10]] (-0.50, fdr 6e-04).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.13×** | +11.1 | 1e-25 | 31/31 (HEC-1-A, KATO III, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +9.7 | 1e-19 | 35/44 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.21×** | +8.2 | 5e-14 | 11/13 (HOP62, HT-29, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +7.8 | 1e-12 | 35/46 (A498, SW480, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +7.7 | 2e-12 | 16/21 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.89×** | +6.9 | 7e-10 | 31/47 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.84×** | +6.6 | 4e-09 | 27/47 (SW480, RKO, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.2 | 1e-05 | 22/41 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +4.8 | 1e-04 | 18/45 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.55×** | +4.7 | 1e-04 | 17/35 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +4.5 | 3e-04 | 18/39 (C32, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.4 | 6e-04 | 17/32 (HOP62, AsPC-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.3 | 7e-04 | 23/46 (HOP62, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.001 | 16/47 (HS-578T, A549, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.7 | 0.008 | 10/43 (KATO III, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.523×** | -6.9 | 3e-09 | 25/46 (LoVo, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.577×** | -5.9 | 1e-06 | 25/47 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.598×** | -5.5 | 8e-06 | 24/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -5.0 | 8e-05 | 21/40 (RKO, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.662×** | -4.4 | 0.001 | 19/45 (RKO, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.707×** | -3.3 | 0.082 | 14/44 (LoVo, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 7.41 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0978× (z -9.0) ⚠ toxic; unreliable plate only |
| [[HEC-1-A (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[Hs 766T (line)]] | wt | 6.32 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0833× (z -9.8) |
| [[RKO (line)]] | wt | 5.11 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0558× (z -9.9) |
| [[A-172 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH5]] | +0.55 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[CCNK]] | +0.55 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[COPB2]] | +0.54 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[GOLGA5]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[COX5B]] | +0.53 | +0.43 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 548 |
| [[BMT2]] | +0.52 | +0.19 / +0.56 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TRPT1]] | +0.52 | +0.29 / +0.58 | both halves | 2e-04 |  |
| [[CORO1B]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[HELZ]] | +0.52 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[TMEM134]] | +0.52 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[RTRAF]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[WBP1]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[RAB1A]] | +0.51 | +0.39 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS7]] | -0.52 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[NOP56]] | -0.50 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[SRSF10]] | -0.50 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[CLN6]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[SLC25A13]] | -0.45 | -0.30 / -0.38 | both halves | 2e-04 | pathway: Aerobic respiration and respiratory electron transport |
| [[IPO9]] | -0.44 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[SSB]] | -0.44 | -0.20 / -0.39 | both halves | 7e-04 |  |
| [[SCMH1]] | -0.44 | -0.44 / -0.22 | both halves | 6e-04 |  |
| [[FANCL]] | -0.43 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[GNL3L]] | -0.43 | -0.30 / -0.42 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SURF1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.3, -36.1); signed map (-48.2, 17.7). **Vector** length 45.0, 5.67% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +2.1 | +11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +1.9 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +2.2 |
|  | [[Canagliflozin (drug)]] 0.05 µM |  | +0.8 | +1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.7 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.7 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.6 | -5.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.8 | -0.3 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -0.7 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.7 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | SURF1 cytochrome c oxidase assembly factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:133,351,758-133,356,676 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SHY1 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Hallmark sets | DNA_REPAIR, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15526](https://www.uniprot.org/uniprotkb/Q15526) (Surfeit locus protein 1):

> Component of the MITRAC (mitochondrial translation regulation assembly intermediate of cytochrome c oxidase complex) complex, that regulates cytochrome c oxidase assembly.

**Summary**, from NCBI Gene [6834](https://www.ncbi.nlm.nih.gov/gene/6834):

> This gene encodes a protein localized to the inner mitochondrial membrane and thought to be involved in the biogenesis of the cytochrome c oxidase complex. The protein is a member of the SURF1 family, which includes the related yeast protein SHY1 and rickettsial protein RP733. The gene is located in the surfeit gene cluster, a group of very tightly linked genes that do not share sequence similarity, where it shares a bidirectional promoter with SURF2 on the opposite strand. Defects in this gene …

**Accessions** — [HGNC:11474](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11474) · Entrez [6834](https://www.ncbi.nlm.nih.gov/gene/6834) · UniProt [Q15526](https://www.uniprot.org/uniprotkb/Q15526) · Ensembl [ENSG00000148290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148290)

## Data

Gene col 7257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7257); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7257]; `tensor/DDL_lfc|DDL_z.npy` [7257]; `embed/gene_vectors.npy` [7257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7257 or target_col == 7257). Every well: [[SURF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SURF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
