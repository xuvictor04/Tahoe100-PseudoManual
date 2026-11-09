---
symbol: "ANO3"
type: "gene"
col: 5552
ensembl_id: "ENSG00000134343"
name: "anoctamin 3"
location: "11p14.2"
module: 19
arm: "+"
pooled_cpm: 3.2
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ANO3

*anoctamin 3* — 11p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.14× (z +16.7, q 0e+00, up in 17 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.655× (z -4.4, q 0.007, down in 7 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0294×; ⚠ cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0583×); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0721×); [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0984×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGBL1]] (+0.71, fdr 1e-05), [[PCDH15]] (+0.69, fdr 1e-05), [[NXPH1]] (+0.68, fdr 9e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[LINC02994]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5552.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.14×** | +16.7 | 0e+00 | 17/24 (HT-29, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +12.5 | 3e-33 | 2/5 (HT-29, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.53×** | +12.0 | 4e-31 | 4/7 (SK-MEL-2, HT-29, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +11.9 | 3e-30 | 5/14 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.00×** | +10.1 | 4e-22 | 13/31 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.81×** | +8.7 | 4e-16 | 18/42 (SW480, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.02×** | +7.3 | 3e-11 | 19/39 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.9 | 8e-05 | 1/14 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.9 | 8e-05 | 7/42 (A-172, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.4 | 6e-04 | 12/37 (hTERT-HPNE, H4, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.9 | 0.005 | 0/21 | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.012 | 3/31 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.040 | 4/31 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.1 | 0.072 | 1/9 (SNU-423) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.092 | 1/17 (A498) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0294×; ⚠ cell-cycle shift, explains ~21% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0583×); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0721×); [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0984×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.655×** | -4.4 | 0.007 | 7/34 (MIA PaCa-2, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.740× | -3.0 | 0.63 | 9/38 (NCI-H1573, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 12.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0583× (z -11.1) |
| [[HT-29 (line)]] | alt | 8.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0984× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 8.75 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0294× (z -12.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 9.32× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGBL1]] | +0.71 | +0.57 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[PCDH15]] | +0.69 | +0.50 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[NXPH1]] | +0.68 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[AQP4-AS1]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[KCNMB2]] | +0.68 | +0.58 / +0.66 | both halves | 8e-06 | **novel candidate** |
| [[SLCO1C1]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PART1]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[LINC00922]] | +0.67 | +0.54 / +0.75 | both halves | 1e-05 | **novel candidate** |
| [[LINC02755]] | +0.67 | +0.46 / +0.76 | both halves | 2e-05 |  |
| [[IQCM]] | +0.66 | +0.50 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[CNTNAP4]] | +0.64 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[GRM7]] | +0.62 | +0.34 / +0.68 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02994]] | B | LINC02994 activity raises ANO3's level | lines that do not express LINC02994 (33) vs lines expressing it (17) | 2.15× lower at baseline in the lines without LINC02994 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, ANKRD30B, ENSG00000287598 |
| [[PAPPA2]] | B | PAPPA2 activity weakens ANO3's drug response | lines that do not express PAPPA2 (26) vs lines expressing it (17) | the lines without PAPPA2 respond 5.51× as strongly (z diff -1.46); strongest at Homoharringtonine 5 µM: 2.45x vs 0.53x (z diff -6.5) | 0.010 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CDH7]] | B | CDH7 activity raises ANO3's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 1.92× lower at baseline in the lines without CDH7 | 0.014 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9 |
| [[LINC01967]] | B | LINC01967 activity raises ANO3's level | lines that do not express LINC01967 (38) vs lines expressing it (12) | 1.83× lower at baseline in the lines without LINC01967 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, SLC15A5, PCSK1 |
| [[MIR4307HG]] | B | MIR4307HG activity raises ANO3's level | lines that do not express MIR4307HG (35) vs lines expressing it (15) | 1.76× lower at baseline in the lines without MIR4307HG | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000258081, MAGEB2, LINC02438 |
| [[TCF4]] | B | TCF4 activity raises ANO3's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without TCF4 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1 |
| [[GREM2]] | B | GREM2 activity raises ANO3's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.07× lower at baseline in the lines without GREM2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[COP1-DT]] | B | COP1-DT activity raises ANO3's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without COP1-DT | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[LINC01967]] | B | LINC01967 activity weakens ANO3's drug response | lines that do not express LINC01967 (35) vs lines expressing it (8) | (z diff -1.77); strongest at Homoharringtonine 5 µM: 1.83x vs 0.50x (z diff -6.4) | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, SLC15A5, PCSK1; target measured in part of the lines; artifact flags |
| [[TCF4]] | B | TCF4 activity weakens ANO3's drug response | lines that do not express TCF4 (23) vs lines expressing it (20) | the lines without TCF4 respond 2.75× as strongly (z diff -1.13); strongest at Homoharringtonine 5 µM: 2.65x vs 0.67x (z diff -5.5) | 0.065 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; target measured in part of the lines; artifact flags |
| [[PDZRN3]] | B | PDZRN3 activity raises ANO3's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.63× lower at baseline in the lines without PDZRN3 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[KCNK2]] | B | KCNK2 activity weakens ANO3's drug response | lines that do not express KCNK2 (25) vs lines expressing it (18) | the lines without KCNK2 respond 3.77× as strongly (z diff -1.30); strongest at Homoharringtonine 5 µM: 2.55x vs 0.70x (z diff -5.5) | 0.081 | ⚠ within organs, on part of the lines; also absent: KC6, EDNRB, PAPPA2; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.2, 25.6); signed map (42.8, 39.4). **Vector** length 46.1, 5.50% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.3 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -1.4 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | anoctamin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p14.2 — chr11:26,188,842-26,663,289 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GENX-3947, DYT23; previously C11orf25, TMEM16C |
| Gene groups (HGNC) | Anoctamins |
| Reactome | 8 pathways, smallest: Induction of Cell-Cell Fusion; Late SARS-CoV-2 Infection Events; Stimuli-sensing channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYT9](https://www.uniprot.org/uniprotkb/Q9BYT9) (Anoctamin-3):

> Has calcium-dependent phospholipid scramblase activity; scrambles phosphatidylcholine and galactosylceramide (By similarity). Seems to act as potassium channel regulator and may inhibit pain signaling; can facilitate KCNT1/Slack channel activity by promoting its full single-channel conductance at very low sodium concentrations and by increasing its sodium sensitivity (By similarity). Does not exhibit calcium-activated chloride channel (CaCC) activity.

**Summary**, from NCBI Gene [63982](https://www.ncbi.nlm.nih.gov/gene/63982):

> The protein encoded by this gene belongs to the TMEM16 family of predicted membrane proteins, that are also known as anoctamins. While little is known about the function of this gene, mutations in this gene have been associated with some cases of autosomal dominant craniocervical dystonia. Cells from individuals with a mutation in this gene exhibited abnormalities in endoplasmic reticulum-dependent calcium signaling. Studies in rat show that the rat ortholog of this protein interacts with, and …

**Accessions** — [HGNC:14004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14004) · Entrez [63982](https://www.ncbi.nlm.nih.gov/gene/63982) · UniProt [Q9BYT9](https://www.uniprot.org/uniprotkb/Q9BYT9) · Ensembl [ENSG00000134343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134343)

## Data

Gene col 5552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5552); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5552]; `tensor/DDL_lfc|DDL_z.npy` [5552]; `embed/gene_vectors.npy` [5552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5552 or target_col == 5552). Every well: [[ANO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
