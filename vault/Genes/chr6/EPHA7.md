---
symbol: "EPHA7"
type: "gene"
col: 5683
ensembl_id: "ENSG00000135333"
name: "EPH receptor A7"
location: "6q16.1"
module: 9
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 20
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# EPHA7

*EPH receptor A7* — 6q16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.05× (z +23.0, q 0e+00, up in 11 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Mebendazole (drug)]] 5 µM: 0.585× (z -4.7, q 0.002, down in 3 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH10]] (+0.65, fdr 1e-05), [[PIEZO2]] (+0.64, fdr 7e-06), [[UNC5C]] (+0.64, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[EBF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5683.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.05×** | +23.0 | 0e+00 | 11/14 (BT-474, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +11.5 | 3e-28 | 3/12 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +11.4 | 6e-28 | 3/9 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.07×** | +10.1 | 6e-22 | 13/17 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.15×** | +9.8 | 2e-20 | 11/16 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.78×** | +9.2 | 3e-18 | 12/15 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.82×** | +8.6 | 5e-16 | 2/11 (MIA PaCa-2, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +8.3 | 1e-14 | 7/12 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +8.1 | 3e-14 | 8/13 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +6.9 | 3e-10 | 7/13 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +6.9 | 3e-10 | 11/17 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.8 | 4e-10 | 9/16 (BT-474, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +6.0 | 1e-07 | 10/17 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.37×** | +5.6 | 1e-06 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +5.5 | 1e-06 | 3/12 (A498, CHP-212, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +4.7 | 1e-04 | 10/15 (A498, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +4.6 | 1e-04 | 7/16 (NCI-H2347, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.63×** | +4.4 | 3e-04 | 4/17 (NCI-H2347, PANC-1, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +4.2 | 8e-04 | 4/16 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5683.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | **0.585×** | -4.7 | 0.002 | 3/15 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.658×** | -3.8 | 0.044 | 8/15 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.671×** | -3.6 | 0.048 | 1/16 (NCI-H2347) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.663×** | -3.6 | 0.048 | 7/16 (CFPAC-1, SHP-77, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.767×** | -3.4 | 0.063 | 12/16 (SHP-77, SW 900, …) | top dose only |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.668×** | -3.4 | 0.063 | 2/15 (H4, CHP-212) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.770×** | -3.4 | 0.063 | 5/17 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.788× | -3.1 | 0.16 | 3/16 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 55.3 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -17.6) |
| [[A498 (line)]] | wt | 17.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +18.4) | — |
| [[BT-474 (line)]] | alt | 2.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.6× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 3.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.18× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 6.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0452× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 86.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.557 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.457 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH10]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[PIEZO2]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[UNC5C]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[HMCN1]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PCDH10]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[NCAM2]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PCDH17]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 | STRING 437 |
| [[PCDH9]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[DMD]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 | same gene group; pathway: EPH-Ephrin signaling; STRING 688 |
| [[SCN2A]] | +0.60 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[RALYL]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EPHA7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRIA2]] | C | GRIA2 activity raises EPHA7's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 3.26× lower at baseline in the lines without GRIA2 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LINC02197]] | C | LINC02197 activity raises EPHA7's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 2.10× lower at baseline in the lines without LINC02197 | 0.053 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent; co-absent with the target |
| [[DACH1]] | C | DACH1 activity raises EPHA7's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 2.22× lower at baseline in the lines without DACH1 | 0.096 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EBF1]] | B | EPHA7 activity lowers EBF1's level | lines that do not express EPHA7 (30) vs lines expressing it (20) | 1.24× higher at baseline in the lines without EPHA7 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000287683, GRIA2, NTNG1 |
| [[PEG10]] | C | EPHA7 activity raises PEG10's level | lines that do not express EPHA7 (30) vs lines expressing it (20) | 3.94× lower at baseline in the lines without EPHA7 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000287683, GRIA2, NTNG1; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.0, 30.3); signed map (38.6, 31.8). **Vector** length 39.7, 9.15% of its response variance represented; |z| ≥ 3 in 438 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +23.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +6.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +5.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +1.0 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.2 | -3.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.2 | -1.6 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor A7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q16.1 — chr6:93,240,020-93,419,687 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hek11 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15375](https://www.uniprot.org/uniprotkb/Q15375) (Ephrin type-A receptor 7):

> Receptor tyrosine kinase which binds promiscuously GPI-anchored ephrin-A family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Among GPI-anchored ephrin-A ligands, EFNA5 is a cognate/functional ligand for EPHA7 and their interaction regulates brain …

**Summary**, from NCBI Gene [2045](https://www.ncbi.nlm.nih.gov/gene/2045):

> This gene belongs to the ephrin receptor subfamily of the protein-tyrosine kinase family. EPH and EPH-related receptors have been implicated in mediating developmental events, particularly in the nervous system. Receptors in the EPH subfamily typically have a single kinase domain and an extracellular region containing a Cys-rich domain and 2 fibronectin type III repeats. The ephrin receptors are divided into 2 groups based on the similarity of their extracellular domain sequences and their …

**Accessions** — [HGNC:3390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3390) · Entrez [2045](https://www.ncbi.nlm.nih.gov/gene/2045) · UniProt [Q15375](https://www.uniprot.org/uniprotkb/Q15375) · Ensembl [ENSG00000135333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135333)

## Data

Gene col 5683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5683); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5683]; `tensor/DDL_lfc|DDL_z.npy` [5683]; `embed/gene_vectors.npy` [5683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5683 or target_col == 5683). Every well: [[EPHA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
