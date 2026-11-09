---
symbol: "APOE"
type: "gene"
col: 5033
ensembl_id: "ENSG00000130203"
name: "apolipoprotein E"
location: "19q13.32"
module: 21
arm: "+"
pooled_cpm: 9.07
n_lines_expressing: 25
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# APOE

*apolipoprotein E* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.25× (z +10.7, q 7e-24, up in 13 of 13 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +8.4, q 4e-15, up in 16 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.231×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOC1]] (+0.72, fdr 1e-05, ⚠ same locus), [[EFCAB14-AS1]] (+0.64, fdr 1e-04), [[FAM217A]] (+0.64, fdr 2e-05), [[CEP164P1]] (+0.63, fdr 7e-05); moves opposite to [[GTF2H3]] (-0.56, fdr 7e-05), [[CCT7]] (-0.55, fdr 1e-05), [[PDAP1]] (-0.55, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MIA]] → it (grade B ⚠); 3 go from it, the strongest it → [[SERF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5033.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **5.25×** | +10.7 | 7e-24 | 13/13 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.84×** | +9.8 | 5e-20 | 9/9 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.22×** | +8.6 | 2e-15 | 7/11 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +8.4 | 4e-15 | 16/20 (HepG2/C3A, SW 900, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.70×** | +6.4 | 2e-08 | 14/18 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.78×** | +6.3 | 3e-08 | 12/16 (NCI-H2030, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **2.07×** | +4.5 | 6e-04 | 9/16 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | **1.84×** | +3.9 | 0.007 | 7/17 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.82×** | +3.9 | 0.007 | 6/21 (HOP62, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +3.8 | 0.007 | 9/21 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.79×** | +3.7 | 0.010 | 9/22 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.73×** | +3.4 | 0.034 | 8/19 (NCI-H2347, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.69×** | +3.4 | 0.034 | 1/22 (SK-MEL-2) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.45×** | +3.3 | 0.034 | 1/20 (SHP-77) | top dose only | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.53×** | +3.3 | 0.040 | 8/20 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.049 | 3/23 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.0 | 0.091 | 8/21 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~25% here); position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.231×; ⚠ cell-cycle shift, would explain all of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5033. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 337 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A-172 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.971 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5033), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOC1]] | +0.72 | +0.56 / +0.70 | both halves | 1e-05 | same gene group; pathway: NR1H2 and NR1H3-mediated signaling; STRING 999; ⚠ same locus (4.9 kb, same strand: neighbours can correlate without regulation) |
| [[EFCAB14-AS1]] | +0.64 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[FAM217A]] | +0.64 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[CEP164P1]] | +0.63 | +0.38 / +0.66 | both halves | 7e-05 |  |
| [[MIA]] | +0.63 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[C1orf56]] | +0.63 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[CCDC65]] | +0.63 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[HIGD2A]] | +0.63 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[C12orf40]] | +0.62 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[RABAC1]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MIR4458HG]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[PCSK1N]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SEPTIN1]] | +0.61 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.56 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[CCT7]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.55 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[FARSB]] | -0.54 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[PSMG1]] | -0.54 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[NUP188]] | -0.53 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[AKAP11]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[DCLRE1A]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[GTF2A1]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 | pathway: Signaling by Nuclear Receptors |
| [[CCT5]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[CEP41]] | -0.52 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[ALG10]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIA]] | B | MIA activity raises APOE's level | lines that do not express MIA (10) vs lines expressing it (40) | 2.20× lower at baseline in the lines without MIA | 0.088 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERF2]] | B | APOE activity raises SERF2's level | lines that do not express APOE (25) vs lines expressing it (25) | 1.09× lower at baseline in the lines without APOE | 0.086 | ⚠ within organs, on part of the lines; also absent: SYT11, RNF175, GRIA2; maybe low, not absent |
| [[ZNHIT1]] | B | APOE activity raises ZNHIT1's level | lines that do not express APOE (25) vs lines expressing it (25) | 1.03× lower at baseline in the lines without APOE | 0.098 | ⚠ within organs, on part of the lines; also absent: SYT11, RNF175, GRIA2; maybe low, not absent |
| [[LRRC37A16P]] | B | APOE activity raises LRRC37A16P's level | lines that do not express APOE (25) vs lines expressing it (25) | 1.13× lower at baseline in the lines without APOE | 0.098 | ⚠ within organs, on part of the lines; also absent: SYT11, RNF175, GRIA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.6, 29.7); signed map (35.9, 4.7). **Vector** length 29.8, 5.34% of its response variance represented; |z| ≥ 3 in 281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +8.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +1.9 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +1.5 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +1.4 | +10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | -0.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -2.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.7 | -1.8 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:44,905,791-44,909,393 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously AD2 |
| Gene groups (HGNC) | Apolipoproteins |
| Hallmark sets | XENOBIOTIC_METABOLISM, ADIPOGENESIS |
| Reactome | 27 pathways, smallest: Chylomicron remodeling; Chylomicron clearance; Chylomicron assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P02649](https://www.uniprot.org/uniprotkb/P02649) (Apolipoprotein E):

> APOE is an apolipoprotein, a protein associating with lipid particles, that mainly functions in lipoprotein-mediated lipid transport between organs via the plasma and interstitial fluids. APOE is a core component of plasma lipoproteins and is involved in their production, conversion and clearance. Apolipoproteins are amphipathic molecules that interact both with lipids of the lipoprotein particle core and the aqueous environment of the plasma. As such, APOE associates with chylomicrons, …

**Summary**, from NCBI Gene [348](https://www.ncbi.nlm.nih.gov/gene/348):

> The protein encoded by this gene is a major apoprotein of the chylomicron. It binds to a specific liver and peripheral cell receptor, and is essential for the normal catabolism of triglyceride-rich lipoprotein constituents. This gene maps to chromosome 19 in a cluster with the related apolipoprotein C1 and C2 genes. Mutations in this gene result in familial dysbetalipoproteinemia, or type III hyperlipoproteinemia (HLP III), in which increased plasma cholesterol and triglycerides are the …

**Accessions** — [HGNC:613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:613) · Entrez [348](https://www.ncbi.nlm.nih.gov/gene/348) · UniProt [P02649](https://www.uniprot.org/uniprotkb/P02649) · Ensembl [ENSG00000130203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130203)

## Data

Gene col 5033: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5033); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5033, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5033]; `tensor/DDL_lfc|DDL_z.npy` [5033]; `embed/gene_vectors.npy` [5033]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5033 or target_col == 5033). Every well: [[APOE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
