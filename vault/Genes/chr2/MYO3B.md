---
symbol: "MYO3B"
type: "gene"
col: 996
ensembl_id: "ENSG00000071909"
name: "myosin IIIB"
location: "2q31.1"
module: 150
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# MYO3B

*myosin IIIB* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.88× (z +22.9, q 0e+00, up in 25 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.0410×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC170]] (+0.75, fdr 7e-06), [[LINC02694]] (+0.74, fdr 7e-06), [[LINC01811]] (+0.74, fdr 7e-06).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.88×** | +22.9 | 0e+00 | 25/28 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.46×** | +19.3 | 0e+00 | 22/31 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.74×** | +15.4 | 0e+00 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.25×** | +13.2 | 7e-38 | 7/11 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.83×** | +12.3 | 1e-32 | 36/41 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.77×** | +11.2 | 3e-27 | 3/5 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.57×** | +8.6 | 4e-16 | 16/30 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.1 | 1e-10 | 8/42 (A498, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +6.7 | 1e-09 | 17/42 (HT-29, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +6.6 | 2e-09 | 10/22 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +5.9 | 2e-07 | 13/38 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +5.4 | 3e-06 | 6/18 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.4 | 5e-04 | 1/10 (A498) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.002 | 13/33 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.7 | 0.007 | 2/11 (LoVo, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.021 | 8/37 (C32, A-172, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.041 | 4/42 (NCI-H1792, SHP-77, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.053 | 3/37 (J82, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.064 | 7/29 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.064 | 2/39 (A498, BT-474) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.40×** | +2.9 | 0.078 | 9/40 (HEC-1-A, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 996.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.0410×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rifaximin (drug)]] 0.05 µM |  | 0.675× | -3.3 | 0.54 | 3/36 (NCI-H23, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 8.50 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 5.47× (z +8.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0410× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 1.54 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +10.7) | — |
| [[A-172 (line)]] | wt | 2.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +11.0) | — |
| [[A498 (line)]] | wt | 1.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +10.2) | — |
| [[C32 (line)]] | wt | 4.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +10.1) | — |
| [[LoVo (line)]] | wt | 1.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.0× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 1.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.8× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 1.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.83× (z +9.4) | — |
| [[SW480 (line)]] | alt | 7.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +8.5) | — |
| [[A-427 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC170]] | +0.75 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[LINC02694]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[LINC01811]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.71 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[COL25A1]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[GRM8]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[USH2A]] | +0.66 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[GRM7]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[DLEU7]] | +0.66 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[MEIOC]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYO3B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PKHD1]] | B | PKHD1 activity raises MYO3B's level | lines that do not express PKHD1 (25) vs lines expressing it (25) | 1.42× lower at baseline in the lines without PKHD1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000231317, SLC30A10, SLC24A3; maybe low, not absent |
| [[LIPC]] | B | LIPC activity raises MYO3B's level | lines that do not express LIPC (18) vs lines expressing it (32) | 1.28× lower at baseline in the lines without LIPC | 0.049 | ⚠ within organs, on part of the lines; also absent: TNFSF10, NIHCOLE, HNMT; maybe low, not absent |
| [[EDN2]] | B | EDN2 activity raises MYO3B's level | lines that do not express EDN2 (30) vs lines expressing it (20) | 1.30× lower at baseline in the lines without EDN2 | 0.087 | ⚠ within organs, on part of the lines; also absent: WNT7A, FAM83A, CST6 |
| [[LINC01226]] | B | LINC01226 activity raises MYO3B's level | lines that do not express LINC01226 (16) vs lines expressing it (34) | 1.38× lower at baseline in the lines without LINC01226 | 0.090 | ⚠ within organs, on part of the lines; also absent: LASTR, TRIM29, ENSG00000287003; maybe low, not absent |
| [[RASGEF1B]] | B | RASGEF1B activity raises MYO3B's level | lines that do not express RASGEF1B (10) vs lines expressing it (40) | 1.32× lower at baseline in the lines without RASGEF1B | 0.092 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.2, 27.2); signed map (33.9, 13.4). **Vector** length 57.6, 8.07% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +22.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.8 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | myosin IIIB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:170,178,145-170,655,171 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myosin heavy chains, class III |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXR4](https://www.uniprot.org/uniprotkb/Q8WXR4) (Myosin-IIIb):

> Probable actin-based motor with a protein kinase activity. Required for normal cochlear hair bundle development and hearing. Plays an important role in the early steps of cochlear hair bundle morphogenesis. Influences the number and lengths of stereocilia to be produced and limits the growth of microvilli within the forming auditory hair bundles thereby contributing to the architecture of the hair bundle, including its staircase pattern. Involved in the elongation of actin in stereocilia tips …

**Summary**, from NCBI Gene [140469](https://www.ncbi.nlm.nih.gov/gene/140469):

> This gene encodes one of the class III myosins. Myosins are ATPases, activated by actin, that move along actin filaments in the cell. This class of myosins are characterized by an amino-terminal kinase domain and shown to be present in photoreceptors. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:15576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15576) · Entrez [140469](https://www.ncbi.nlm.nih.gov/gene/140469) · UniProt [Q8WXR4](https://www.uniprot.org/uniprotkb/Q8WXR4) · Ensembl [ENSG00000071909](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071909)

## Data

Gene col 996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 996); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 996]; `tensor/DDL_lfc|DDL_z.npy` [996]; `embed/gene_vectors.npy` [996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 996 or target_col == 996). Every well: [[MYO3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
