---
symbol: "PLCD4"
type: "gene"
col: 3695
ensembl_id: "ENSG00000115556"
name: "phospholipase C delta 4"
location: "2q35"
module: 38
arm: "+"
pooled_cpm: 3.81
n_lines_expressing: 48
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 24
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PLCD4

*phospholipase C delta 4* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.79× (z +24.6, q 0e+00, up in 31 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.527× (z -6.2, q 3e-07, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR9-1HG]] (+0.73, fdr 7e-06), [[PPP1R36]] (+0.72, fdr 7e-06), [[C2CD6]] (+0.72, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SSC5D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.79×** | +24.6 | 0e+00 | 31/31 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.63×** | +13.5 | 2e-39 | 25/34 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.64×** | +12.3 | 1e-32 | 24/32 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +10.6 | 3e-24 | 26/36 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.62×** | +9.2 | 4e-18 | 15/20 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +8.4 | 4e-15 | 4/7 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.32×** | +8.3 | 7e-15 | 22/40 (A-172, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +8.1 | 5e-14 | 21/44 (SW1417, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +7.9 | 2e-13 | 0/5 | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +7.8 | 4e-13 | 24/44 (SW1417, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.19×** | +7.5 | 4e-12 | 16/40 (SW1417, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **2.09×** | +7.3 | 1e-11 | 20/39 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +6.8 | 4e-10 | 17/44 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +6.3 | 1e-08 | 15/38 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.85×** | +6.1 | 4e-08 | 16/44 (SW1417, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.0 | 6e-08 | 12/44 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +5.0 | 2e-05 | 14/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +4.5 | 2e-04 | 8/44 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.527×** | -6.2 | 3e-07 | 21/39 (A-172, SW 900, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.585×** | -5.3 | 3e-05 | 18/44 (RPMI-7951, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dexamethasone (drug)]] 5 µM |  | **0.609×** | -4.9 | 2e-04 | 10/43 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.680×** | -3.8 | 0.024 | 15/37 (Hs 766T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.702×** | -3.5 | 0.050 | 10/42 (NCI-H2030, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.716× | -3.2 | 0.11 | 7/42 (COLO 205, HepG2/C3A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 11.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.111× (z -9.0) |
| [[SW480 (line)]] | alt | 2.59 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +10.0) | [[Bendamustine (drug)]] 5 µM 0.0907× (z -8.9) |
| [[HOP62 (line)]] | alt | 4.86 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 3.76 | 2 | 0 | [[Selinexor (drug)]] 5 µM 11.4× (z +9.7) | — |
| [[A-172 (line)]] | wt | 8.47 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.117× (z -9.1) |
| [[BT-474 (line)]] | alt | 6.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.27× (z +9.3) | — |
| [[C32 (line)]] | wt | 9.10 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0909× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 1.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[HS-578T (line)]] | alt | 3.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 6.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.71× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 5.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 2.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0612× (z -11.8) |
| [[A-427 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.885 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR9-1HG]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[PPP1R36]] | +0.72 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[LINC00654]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[USP50]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[CD200R1]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.72 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[LDHC]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ARL9]] | +0.71 | +0.75 / +0.57 | both halves | 9e-06 |  |
| [[FNDC7]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.70 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.70 | +0.72 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | SSC5D activity raises PLCD4's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without SSC5D | 0.015 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PLCD4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01482]] | B | LINC01482 activity raises PLCD4's level | lines that do not express LINC01482 (5) vs lines expressing it (45) | 1.74× lower at baseline in the lines without LINC01482 | 0.062 | ⚠ within organs, on part of the lines; also absent: MAP7D2, SLC35F4, ENSG00000226965; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.8, -16.9); signed map (15.0, 9.7). **Vector** length 68.7, 10.6% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +24.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.7 | +8.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +7.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C delta 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,607,855-218,637,184 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipases; C2 domain containing phospholipases; EF-hand domain containing |
| Reactome | 2 pathways, smallest: Synthesis of IP3 and IP4 in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRC7](https://www.uniprot.org/uniprotkb/Q9BRC7) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase delta-4):

> Hydrolyzes the phosphatidylinositol 4,5-bisphosphate (PIP2) to generate 2 second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3). DAG mediates the activation of protein kinase C (PKC), while IP3 releases Ca(2+) from intracellular stores. Required for acrosome reaction in sperm during fertilization, probably by acting as an important enzyme for intracellular Ca(2+) mobilization in the zona pellucida-induced acrosome reaction. May play a role in cell growth. …

**Summary**, from NCBI Gene [84812](https://www.ncbi.nlm.nih.gov/gene/84812):

> This gene encodes a member of the delta class of phospholipase C enzymes. Phospholipase C enzymes play a critical role in many cellular processes by hydrolyzing phosphatidylinositol 4,5-bisphosphate into two intracellular second messengers, inositol 1,4,5-trisphosphate and diacylglycerol. Expression of this gene may be a marker for cancer. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:9062](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9062) · Entrez [84812](https://www.ncbi.nlm.nih.gov/gene/84812) · UniProt [Q9BRC7](https://www.uniprot.org/uniprotkb/Q9BRC7) · Ensembl [ENSG00000115556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115556)

## Data

Gene col 3695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3695); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3695]; `tensor/DDL_lfc|DDL_z.npy` [3695]; `embed/gene_vectors.npy` [3695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3695 or target_col == 3695). Every well: [[PLCD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
