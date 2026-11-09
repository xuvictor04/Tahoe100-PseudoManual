---
symbol: "DOK6"
type: "gene"
col: 13028
ensembl_id: "ENSG00000206052"
name: "docking protein 6"
location: "18q22.2"
module: 19
arm: "+"
pooled_cpm: 18.19
n_lines_expressing: 20
n_dd_up: 8
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 14
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# DOK6

*docking protein 6* — 18q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +11.4, q 2e-27, up in 4 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.559× (z -6.2, q 4e-07, down in 10 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRD1]] (+0.75, fdr 7e-06), [[GREM2]] (+0.73, fdr 7e-06), [[LINC01035]] (+0.71, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 2 go from it, the strongest it → [[ADGRB3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +11.4 | 2e-27 | 4/17 (NCI-H1573, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +10.6 | 7e-24 | 3/14 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +9.6 | 1e-19 | 3/12 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +8.2 | 4e-14 | 2/14 (LOX-IMVI, NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.004 | 0/17 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.007 | 1/15 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.010 | 7/17 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.2 | 0.098 | 1/17 (LOX-IMVI) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.12 | 0/17 | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.12 | 4/17 (NCI-H23, J82, …) | two highest doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.51× | +3.1 | 0.12 | 1/16 (NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.559×** | -6.2 | 4e-07 | 10/17 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.607×** | -5.3 | 4e-05 | 11/17 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.672×** | -4.2 | 0.005 | 13/17 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.725×** | -3.4 | 0.078 | 10/17 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.726×** | -3.4 | 0.078 | 9/17 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.753× | -3.0 | 0.24 | 9/17 (NCI-H460, HepG2/C3A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 121 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0858× (z -27.7) |
| [[HepG2_C3A (line)]] | wt | 160 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -17.2) |
| [[J82 (line)]] | alt | 22.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 8.65 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +21.2) | — |
| [[A498 (line)]] | wt | 61.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -14.7) |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.8) |
| [[CHP-212 (line)]] | wt | 58.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0422× (z -12.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.137× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 6.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.34× (z +8.6) | — |
| [[A-172 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRD1]] | +0.75 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[GREM2]] | +0.73 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.71 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[NCKAP5-AS2]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[LINC03000]] | +0.67 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LINC01508]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[KCNMB2]] | +0.66 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LIN7A]] | +0.65 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[COL4A6]] | +0.65 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[KCNE4]] | +0.64 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[GTF2I-AS1]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 2, C 12. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DOK6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SOX6]] | B | SOX6 activity raises DOK6's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.21× lower at baseline in the lines without SOX6 | 0.0996 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[PGR]] | C | PGR activity raises DOK6's level | lines that do not express PGR (36) vs lines expressing it (14) | 3.75× lower at baseline in the lines without PGR | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[CDH7]] | C | CDH7 activity raises DOK6's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 3.68× lower at baseline in the lines without CDH7 | 0.027 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises DOK6's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 3.41× lower at baseline in the lines without KCNH5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises DOK6's level | lines that do not express BCHE (35) vs lines expressing it (15) | 2.89× lower at baseline in the lines without BCHE | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises DOK6's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 5.93× lower at baseline in the lines without LINC01035 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises DOK6's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.86× lower at baseline in the lines without DPP10 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[TENM1]] | C | TENM1 activity raises DOK6's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 2.38× lower at baseline in the lines without TENM1 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises DOK6's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.65× lower at baseline in the lines without PDE3A | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[VIPR2]] | C | VIPR2 activity raises DOK6's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without VIPR2 | 0.080 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[LAMB4]] | C | LAMB4 activity raises DOK6's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without LAMB4 | 0.089 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRB3]] | C | DOK6 activity raises ADGRB3's level | lines that do not express DOK6 (30) vs lines expressing it (20) | 4.09× lower at baseline in the lines without DOK6 | 0.042 | ⚠ within organs, on part of the lines; also absent: NEFM, PI15, KCNH5; co-absent with the target |
| [[ACSS3]] | C | DOK6 activity raises ACSS3's level | lines that do not express DOK6 (30) vs lines expressing it (20) | 2.48× lower at baseline in the lines without DOK6 | 0.082 | ⚠ within organs, on part of the lines; also absent: NEFM, PI15, KCNH5; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 35.4); signed map (42.1, 43.4). **Vector** length 57.0, 17.8% of its response variance represented; |z| ≥ 3 in 406 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +0.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | docking protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.2 — chr18:69,400,888-69,849,087 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20785, HsT3226; previously DOK5L |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Docking protein family |
| Reactome | 3 pathways, smallest: RET signaling; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PKX4](https://www.uniprot.org/uniprotkb/Q6PKX4) (Docking protein 6):

> DOK proteins are enzymatically inert adaptor or scaffolding proteins. They provide a docking platform for the assembly of multimolecular signaling complexes. DOK6 promotes Ret-mediated neurite growth. May have a role in brain development and/or maintenance.

**Summary**, from NCBI Gene [220164](https://www.ncbi.nlm.nih.gov/gene/220164):

> DOK6 is a member of the DOK (see DOK1; MIM 602919) family of intracellular adaptors that play a role in the RET (MIM 164761) signaling cascade (Crowder et al., 2004 [PubMed 15286081]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28301) · Entrez [220164](https://www.ncbi.nlm.nih.gov/gene/220164) · UniProt [Q6PKX4](https://www.uniprot.org/uniprotkb/Q6PKX4) · Ensembl [ENSG00000206052](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206052)

## Data

Gene col 13028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13028); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13028]; `tensor/DDL_lfc|DDL_z.npy` [13028]; `embed/gene_vectors.npy` [13028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13028 or target_col == 13028). Every well: [[DOK6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOK6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
