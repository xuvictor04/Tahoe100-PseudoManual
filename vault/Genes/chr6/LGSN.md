---
symbol: "LGSN"
type: "gene"
col: 7070
ensembl_id: "ENSG00000146166"
name: "lengsin, lens protein with glutamine synthetase domain"
location: "6q12"
module: 19
arm: "+"
pooled_cpm: 8.55
n_lines_expressing: 14
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# LGSN

*lengsin, lens protein with glutamine synthetase domain* — 6q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.67× (z +13.6, q 2e-39, up in 3 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (NCI-H23 0.106×, NCI-H2030 0.0687×, NCI-H460 0.121×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H1573 0.105×, SHP-77 0.0838×, NCI-H23 0.142×; ⚠ toxic); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H23 0.102×, NCI-H460 0.131×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0377×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FGF14]] (+0.68, fdr 7e-06), [[HORMAD1]] (+0.66, fdr 1e-05), [[BASP1-AS1]] (+0.66, fdr 1e-05); moves opposite to [[ITGA9-AS1]] (-0.46, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NRXN3]] → it (grade C ⚠); 1 goes from it, the strongest it → [[LRRIQ1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.67×** | +13.6 | 2e-39 | 3/9 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.54×** | +13.2 | 2e-37 | 6/10 (HEC-1-A, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +8.8 | 2e-16 | 1/5 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.27×** | +8.5 | 2e-15 | 7/11 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +8.5 | 2e-15 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.77×** | +7.5 | 5e-12 | 2/11 (HOP62, SHP-77) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +6.3 | 2e-08 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +6.0 | 1e-07 | 6/11 (HEC-1-A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +5.7 | 8e-07 | 2/9 (HEC-1-A, HOP62) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.03×** | +5.2 | 1e-05 | 7/11 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +4.5 | 3e-04 | 1/11 (HEC-1-A) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +4.4 | 5e-04 | 2/10 (NCI-H460, HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +4.4 | 5e-04 | 7/11 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.64×** | +3.7 | 0.010 | 5/11 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.018 | 3/11 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +3.3 | 0.032 | 6/11 (HEC-1-A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.50×** | +3.0 | 0.091 | 1/11 (NCI-H1792) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7070.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 3 lines (NCI-H23 0.106×, NCI-H2030 0.0687×, NCI-H460 0.121×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 3 lines (NCI-H1573 0.105×, SHP-77 0.0838×, NCI-H23 0.142×; ⚠ toxic); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H23 0.102×, NCI-H460 0.131×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.0377×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.630× | -3.5 | 0.28 | 10/11 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.633× | -3.3 | 0.28 | 5/11 (SW 900, NCI-H460, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.657× | -3.2 | 0.30 | 10/11 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 60.5 | 0 | 8 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0377× (z -18.1) |
| [[NCI-H460 (line)]] | wt | 40.3 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0738× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0969× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 28.3 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0993× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 9.57 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.37× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0714× (z -11.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 6.04 | 0 | 2 (1 ⚠) | — | [[Penfluridol (drug)]] 5 µM 0.0586× (z -9.8) |
| [[A549 (line)]] | wt | 57.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 58.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0687× (z -12.3) |
| [[A-172 (line)]] | wt | 0.724 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.796 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.851 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.769 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.866 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.680 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.818 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.675 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGF14]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[HORMAD1]] | +0.66 | +0.65 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[BASP1-AS1]] | +0.66 | +0.57 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[MGAT4C]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[VAV3]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[KCNH5]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[THSD7A]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ANO5]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[BMP5]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[OR3A2]] | +0.58 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[ERBB4]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NOVA1]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA9-AS1]] | -0.46 | -0.53 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRXN3]] | C | NRXN3 activity raises LGSN's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.26× lower at baseline in the lines without NRXN3 | 0.022 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |
| [[COL4A3]] | C | COL4A3 activity raises LGSN's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 2.66× lower at baseline in the lines without COL4A3 | 0.035 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[FGF14]] | C | FGF14 activity raises LGSN's level | lines that do not express FGF14 (28) vs lines expressing it (22) | 3.07× lower at baseline in the lines without FGF14 | 0.048 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, PTPRD, KCNT2; co-absent with the target |
| [[KLHL13]] | C | KLHL13 activity raises LGSN's level | lines that do not express KLHL13 (23) vs lines expressing it (27) | 2.62× lower at baseline in the lines without KLHL13 | 0.050 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; co-absent with the target |
| [[GRAMD1B]] | C | GRAMD1B activity raises LGSN's level | lines that do not express GRAMD1B (31) vs lines expressing it (19) | 3.30× lower at baseline in the lines without GRAMD1B | 0.057 | ⚠ within organs, on part of the lines; also absent: MAGEB2, CD38, ENSG00000253503; co-absent with the target |
| [[PALMD]] | C | PALMD activity raises LGSN's level | lines that do not express PALMD (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without PALMD | 0.079 | ⚠ within organs, on part of the lines; also absent: GPRC5B, FAM110B, SHISAL1; maybe low, not absent; co-absent with the target |
| [[RSPO3]] | C | RSPO3 activity raises LGSN's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 5.81× lower at baseline in the lines without RSPO3 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRIQ1]] | C | LGSN activity raises LRRIQ1's level | lines that do not express LGSN (36) vs lines expressing it (14) | 3.42× lower at baseline in the lines without LGSN | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000289911, LINC03046, RNF212; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.5, 37.6); signed map (39.7, 41.7). **Vector** length 49.2, 19.1% of its response variance represented; |z| ≥ 3 in 330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | lengsin, lens protein with glutamine synthetase domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q12 — chr6:63,275,951-63,319,983 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LGS; previously GLULD1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TDP6](https://www.uniprot.org/uniprotkb/Q5TDP6) (Lengsin):

> May act as a component of the cytoskeleton or as a chaperone for the reorganization of intermediate filament proteins during terminal differentiation in the lens. Does not seem to have enzymatic activity (By similarity).

**Summary**, from NCBI Gene [51557](https://www.ncbi.nlm.nih.gov/gene/51557):

> This gene encodes a protein with similarity to the GS I members of the glutamine synthetase superfamily. The encoded protein is referred to as a pseudo-glutamine synthetase because it has no glutamine synthesis activity and may function as a chaperone protein. This protein is localized to the lens and may be associated with cataract disease. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:21016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21016) · Entrez [51557](https://www.ncbi.nlm.nih.gov/gene/51557) · UniProt [Q5TDP6](https://www.uniprot.org/uniprotkb/Q5TDP6) · Ensembl [ENSG00000146166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146166)

## Data

Gene col 7070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7070); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7070]; `tensor/DDL_lfc|DDL_z.npy` [7070]; `embed/gene_vectors.npy` [7070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7070 or target_col == 7070). Every well: [[LGSN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGSN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
