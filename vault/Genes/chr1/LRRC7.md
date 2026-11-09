---
symbol: "LRRC7"
type: "gene"
col: 412
ensembl_id: "ENSG00000033122"
name: "leucine rich repeat containing 7"
location: "1p31.1"
module: 152
arm: "+"
pooled_cpm: 15.96
n_lines_expressing: 35
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# LRRC7

*leucine rich repeat containing 7* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.31× (z +15.4, q 0e+00, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.705× (z -4.5, q 0.003, down in 15 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA3]] (+0.71, fdr 7e-06), [[LRP2]] (+0.65, fdr 1e-05), [[PTPRD]] (+0.61, fdr 1e-05).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[MEF2C-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +15.4 | 0e+00 | 20/29 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +11.2 | 1e-26 | 24/32 (NCI-H23, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.7 | 1e-15 | 9/23 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.5 | 3e-15 | 5/16 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +8.3 | 1e-14 | 23/30 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +6.6 | 3e-09 | 5/32 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +6.0 | 2e-07 | 5/18 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.8 | 1e-04 | 6/28 (hTERT-HPNE, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +4.0 | 0.004 | 10/30 (SNU-1, A-172, …) | top dose only | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.017 | 3/29 (HEC-1-A, NCI-H23, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.080 | 1/30 (PANC-1) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.093 | 11/30 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Oxaprozin (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.093 | 4/29 (HEC-1-A, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.093 | 10/30 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 412.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | **0.705×** | -4.5 | 0.003 | 15/30 (C32, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.711×** | -4.4 | 0.003 | 13/31 (BT-474, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -4.3 | 0.003 | 8/33 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.798×** | -4.1 | 0.006 | 15/33 (SNU-423, C32, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -3.5 | 0.044 | 9/32 (SNU-423, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.764×** | -3.5 | 0.044 | 15/32 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.764×** | -3.5 | 0.044 | 6/32 (NCI-H2347, HS-578T, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.769×** | -3.4 | 0.051 | 9/32 (SNU-423, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.773×** | -3.3 | 0.057 | 11/32 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.782×** | -3.2 | 0.084 | 7/32 (SNU-423, J82, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.775×** | -3.2 | 0.084 | 10/29 (SNU-423, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 174 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -10.0) |
| [[LoVo (line)]] | wt | 4.17 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.41× (z +9.6) | [[Cyclosporin A (drug)]] 0.5 µM 0.121× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 7.44 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.45× (z +9.1) | [[Fluvoxamine (drug)]] 5 µM 0.0589× (z -11.6) |
| [[SNU-423 (line)]] | alt | 258 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.328× (z -10.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 8.79 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.127× (z -9.0) |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0565× (z -9.4) |
| [[C32 (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.219× (z -9.0) ⚠ cell-cycle shift, explains ~21% of this change |
| [[HEC-1-A (line)]] | alt | 4.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.66× (z +8.8) | — |
| [[J82 (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.105× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~14% of this change |
| [[LOX-IMVI (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 5.78 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.09× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0612× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 5.77 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.27× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 6.28 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.47× (z +9.8) | — |
| [[A-427 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.81 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA3]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LRP2]] | +0.65 | +0.53 / +0.72 | both halves | 1e-05 | STRING 459 |
| [[PTPRD]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 | pathway: Neuronal System |
| [[LRAT]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[NREP]] | +0.61 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[NEGR1]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 | STRING 429 |
| [[LINC01583]] | +0.57 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[EFR3B]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[EYA1]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[TMEM45A]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[GRID2]] | +0.56 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[LINGO2]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C-AS1]] | B | LRRC7 activity raises MEF2C-AS1's level | lines that do not express LRRC7 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without LRRC7 | 0.007 | ⚠ within organs, on part of the lines; also absent: RNF150, MAP2, KCTD16; maybe low, not absent |
| [[MEF2C]] | B | LRRC7 activity raises MEF2C's level | lines that do not express LRRC7 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without LRRC7 | 0.027 | ⚠ within organs, on part of the lines; also absent: RNF150, MAP2, KCTD16; maybe low, not absent |
| [[ATRNL1]] | B | LRRC7 activity raises ATRNL1's level | lines that do not express LRRC7 (15) vs lines expressing it (35) | 3.33× lower at baseline in the lines without LRRC7 | 0.060 | ⚠ within organs, on part of the lines; also absent: RNF150, MAP2, KCTD16; maybe low, not absent |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.5, 29.5); signed map (32.1, 41.2). **Vector** length 70.4, 15.5% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +15.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -2.9 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.0 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:69,567,922-70,151,945 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1365, densin-180 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 16 pathways, smallest: Ras activation upon Ca2+ influx through NMDA receptor; Unblocking of NMDA receptors, glutamate binding and activation; Negative regulation of NMDA receptor-mediated neuronal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96NW7](https://www.uniprot.org/uniprotkb/Q96NW7) (Leucine-rich repeat-containing protein 7):

> Adapter protein that is required for correct postsynapse architecture and regulates postsynaptic plasticity through interactions with different partners. Through its interaction with CACNA1C, it enhances trafficking of voltage-dependent L-type calcium channels to the dendritic cell membrane and increases channel postsynaptic clustering, thereby facilitating excitatory calcium signaling (By similarity). It also serves as a scaffold that brings CAMK2A and PPP1CA into close proximity, probably …

**Summary**, from NCBI Gene [57554](https://www.ncbi.nlm.nih.gov/gene/57554):

> Predicted to enable protein kinase binding activity. Predicted to be involved in several processes, including establishment or maintenance of epithelial cell apical/basal polarity; neurotransmitter receptor transport, endosome to postsynaptic membrane; and receptor clustering. Located in cytosol. Implicated in cocaine dependence. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18531) · Entrez [57554](https://www.ncbi.nlm.nih.gov/gene/57554) · UniProt [Q96NW7](https://www.uniprot.org/uniprotkb/Q96NW7) · Ensembl [ENSG00000033122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033122)

## Data

Gene col 412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 412); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 412]; `tensor/DDL_lfc|DDL_z.npy` [412]; `embed/gene_vectors.npy` [412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 412 or target_col == 412). Every well: [[LRRC7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
