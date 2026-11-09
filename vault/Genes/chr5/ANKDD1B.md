---
symbol: "ANKDD1B"
type: "gene"
col: 12079
ensembl_id: "ENSG00000189045"
name: "ankyrin repeat and death domain containing 1B"
location: "5q13.3"
module: 39
arm: "+"
pooled_cpm: 9.2
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# ANKDD1B

*ankyrin repeat and death domain containing 1B* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.42× (z +10.8, q 1e-24, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.325× (z -9.7, q 1e-19, down in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.348× (z -9.1, q 2e-17, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01191]] (+0.89, fdr 7e-06), [[SLC6A13]] (+0.87, fdr 7e-06), [[MSH4]] (+0.85, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +10.8 | 1e-24 | 37/43 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.49×** | +7.9 | 7e-13 | 31/46 (SW480, RKO, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +6.8 | 2e-09 | 30/45 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.16×** | +6.7 | 3e-09 | 34/47 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.84×** | +5.0 | 7e-05 | 30/46 (A549, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +4.5 | 7e-04 | 18/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.003 | 17/42 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +3.8 | 0.011 | 10/47 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.013 | 16/46 (A-172, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.024 | 16/47 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.040 | 18/45 (C32, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.086 | 16/44 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12079.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.325×** | -9.7 | 1e-19 | 35/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.348×** | -9.1 | 2e-17 | 35/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.374×** | -8.5 | 3e-15 | 31/43 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.484×** | -6.3 | 5e-08 | 32/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.547×** | -5.2 | 2e-05 | 27/45 (SW480, J82, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.556×** | -4.9 | 8e-05 | 22/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.371×** | -4.5 | 5e-04 | 21/47 (H4, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.578×** | -4.5 | 5e-04 | 21/46 (H4, A-427, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.607×** | -4.2 | 0.002 | 21/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.612×** | -4.1 | 0.002 | 22/40 (hTERT-HPNE, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.628×** | -4.0 | 0.003 | 21/46 (NCI-H1792, LoVo, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.684×** | -3.3 | 0.047 | 15/46 (A549, HEC-1-A, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.04 | 1 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 4.97× (z +9.1) | [[Digitoxin (drug)]] 0.5 µM 0.112× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 8.61 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +11.7) | [[Digitoxin (drug)]] 0.05 µM 0.122× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 9.66 | 0 | 2 | — | [[Pemetrexed (drug)]] 5 µM 0.0937× (z -9.1) |
| [[C32 (line)]] | wt | 17.6 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0874× (z -9.4) |
| [[H4 (line)]] | wt | 16.7 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0479× (z -10.5) |
| [[LoVo (line)]] | wt | 9.73 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 6.43 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0874× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0762× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0894× (z -8.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0804× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 6.23 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0998× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -9.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.77 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0625× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0680× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0902× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 12.7 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0724× (z -9.1) |
| [[A-427 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01191]] | +0.89 | +0.88 / +0.75 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.87 | +0.87 / +0.80 | both halves | 7e-06 |  |
| [[MSH4]] | +0.85 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.84 | +0.82 / +0.75 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.83 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[IMPG2]] | +0.83 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.82 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[USP50]] | +0.82 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 |  |
| [[FLACC1]] | +0.81 | +0.85 / +0.79 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.81 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[CFAP70]] | +0.81 | +0.83 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKDD1B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC26A4]] | B | SLC26A4 activity raises ANKDD1B's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.59× lower at baseline in the lines without SLC26A4 | 0.019 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[IMPA1P1]] | B | IMPA1P1 activity raises ANKDD1B's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without IMPA1P1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[DDR2]] | B | DDR2 activity raises ANKDD1B's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without DDR2 | 0.053 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises ANKDD1B's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without FSIP2-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[CD226]] | B | CD226 activity raises ANKDD1B's level | lines that do not express CD226 (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without CD226 | 0.096 | ⚠ within organs, on part of the lines; also absent: FRZB, GALNT16, KLRG1; maybe low, not absent |
| [[FRZB]] | C | FRZB activity raises ANKDD1B's level | lines that do not express FRZB (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without FRZB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.907). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.7, -13.5); signed map (17.4, 7.4). **Vector** length 98.3, 22.7% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.0 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +10.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +4.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.0 | +6.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.6 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -5.6 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.1 | -5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.6 | -4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and death domain containing 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:75,611,182-75,681,773 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [A6NHY2](https://www.uniprot.org/uniprotkb/A6NHY2) carries no function annotation.

**Summary**, from NCBI Gene [728780](https://www.ncbi.nlm.nih.gov/gene/728780):

> Predicted to be involved in signal transduction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32525) · Entrez [728780](https://www.ncbi.nlm.nih.gov/gene/728780) · UniProt [A6NHY2](https://www.uniprot.org/uniprotkb/A6NHY2) · Ensembl [ENSG00000189045](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189045)

## Data

Gene col 12079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12079); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12079]; `tensor/DDL_lfc|DDL_z.npy` [12079]; `embed/gene_vectors.npy` [12079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12079 or target_col == 12079). Every well: [[ANKDD1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKDD1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
