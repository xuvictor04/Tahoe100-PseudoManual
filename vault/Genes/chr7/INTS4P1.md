---
symbol: "INTS4P1"
type: "gene"
col: 8984
ensembl_id: "ENSG00000164669"
name: "integrator complex subunit 4 pseudogene 1"
location: "7q11.21"
module: 37
arm: "+"
pooled_cpm: 3.02
n_lines_expressing: 41
n_dd_up: 9
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# INTS4P1

*integrator complex subunit 4 pseudogene 1* — 7q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.79× (z +7.7, q 1e-11, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.339× (z -8.0, q 7e-13, down in 24 of 39 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.418× (z -6.4, q 3e-08, down in 20 of 35 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF528-AS1]] (+0.62, fdr 1e-05), [[GOLGA8N]] (+0.59, fdr 2e-05), [[LINC00159]] (+0.58, fdr 2e-05); moves opposite to [[TRAK1]] (-0.43, fdr 1e-04), [[RAPGEF5]] (-0.43, fdr 2e-04), [[MYO5C]] (-0.43, fdr 1e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[AKAP17A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.79×** | +7.7 | 1e-11 | 21/32 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +7.3 | 1e-10 | 1/6 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +4.6 | 8e-04 | 12/21 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.4 | 0.002 | 9/27 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.019 | 8/28 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.41×** | +3.7 | 0.024 | 8/38 (BT-474, NCI-H460, …) | top dose only | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.026 | 5/37 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.093 | 3/33 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.093 | 4/27 (HOP62, SW480, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.339×** | -8.0 | 7e-13 | 24/39 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.418×** | -6.4 | 3e-08 | 20/35 (NCI-H2030, HOP62, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.544×** | -6.4 | 4e-08 | 19/29 (A-172, BT-474, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.451×** | -5.9 | 6e-07 | 18/32 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.463×** | -5.7 | 1e-06 | 22/35 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.471×** | -5.4 | 8e-06 | 19/31 (MIA PaCa-2, HOP62, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.509×** | -5.0 | 5e-05 | 18/33 (SW480, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.556×** | -4.3 | 1e-03 | 11/17 (MIA PaCa-2, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.559×** | -4.3 | 0.001 | 15/37 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.586×** | -3.9 | 0.005 | 15/25 (MIA PaCa-2, HOP62, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.416×** | -3.4 | 0.035 | 10/22 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pemetrexed (drug)]] 0.05 µM |  | 0.643× | -3.0 | 0.11 | 8/33 (SNU-1, H4, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.459× | -3.0 | 0.11 | 7/30 (RPMI-7951, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 12.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0662× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0688× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 8.19× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.117× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 2.92 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0889× (z -10.1) ⚠ cell-cycle shift, explains ~69% of this change |
| [[Hs 766T (line)]] | wt | 7.23 | 0 | 1 | — | [[Sinomenine (drug)]] 0.05 µM 0.0771× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 9.83 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0270× (z -15.9) |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0876× (z -9.0) |
| [[A-427 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.850 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.841 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.860 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.577 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.410 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF528-AS1]] | +0.62 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[GOLGA8N]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[LINC00159]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ADAM20]] | +0.57 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[SH3BGR]] | +0.57 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[TAGAP-AS1]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ZIM2-AS1]] | +0.53 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[ELOA-AS1]] | +0.53 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ADAM20P1]] | +0.53 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[GTF2IP5]] | +0.53 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[RPL34-DT]] | +0.52 | +0.29 / +0.60 | both halves | 2e-04 |  |
| [[DENND6A-AS1]] | +0.52 | +0.31 / +0.59 | both halves | 2e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK1]] | -0.43 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[RAPGEF5]] | -0.43 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[MYO5C]] | -0.43 | -0.36 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers INTS4P1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RAPGEF5]] | B | RAPGEF5 activity lowers INTS4P1's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 1.92× higher at baseline in the lines without RAPGEF5 | 0.074 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKAP17A]] | B | INTS4P1 activity raises AKAP17A's level | lines that do not express INTS4P1 (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without INTS4P1 | 0.0996 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.524). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.8, -19.5); signed map (8.1, 4.1). **Vector** length 41.0, 4.94% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.0 | +7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +1.3 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.2 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | -3.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.8 | -0.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +0.6 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -1.9 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +0.3 |
|  | [[Lopinavir (drug)]] 5 µM |  | -0.9 | -1.5 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 4 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7q11.21 — chr7:65,141,241-65,212,794 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | FLJ25037; previously INTS4L1 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21925) · Entrez [285905](https://www.ncbi.nlm.nih.gov/gene/285905) · Ensembl [ENSG00000164669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164669)

## Data

Gene col 8984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8984); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8984]; `tensor/DDL_lfc|DDL_z.npy` [8984]; `embed/gene_vectors.npy` [8984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8984 or target_col == 8984). Every well: [[INTS4P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS4P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
