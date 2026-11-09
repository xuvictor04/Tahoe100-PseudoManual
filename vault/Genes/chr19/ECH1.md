---
symbol: "ECH1"
type: "gene"
col: 2501
ensembl_id: "ENSG00000104823"
name: "enoyl-CoA hydratase 1"
location: "19q13.2"
module: 14
arm: "+"
pooled_cpm: 33.27
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ECH1

*enoyl-CoA hydratase 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.16× (z +10.9, q 6e-25, up in 41 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mifepristone (drug)]] 0.5 µM: 1.55× (z +4.2, q 0.004, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.612× (z -4.6, q 0.002, down in 29 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.675× (z -3.7, q 0.056, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Tadalafil (drug)]] 0.05 µM in 1 line (SW48 0.0447×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 0.373×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DBP]] (+0.64, fdr 9e-06), [[TEF]] (+0.62, fdr 1e-05), [[BDH2]] (+0.62, fdr 7e-06); moves opposite to [[ZNF731P]] (-0.62, fdr 1e-05), [[TTL]] (-0.57, fdr 1e-05), [[NFATC2IP]] (-0.57, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BCAR3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.16×** | +10.9 | 6e-25 | 41/42 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +7.0 | 9e-10 | 26/32 (KATO III, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.1 | 2e-07 | 31/37 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.55×** | +4.2 | 0.004 | 30/47 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.9 | 0.013 | 9/47 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.47×** | +3.7 | 0.024 | 25/45 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.033 | 22/46 (BT-474, A549, …) | top dose only |  |
| [[Mifepristone (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.048 | 20/46 (LoVo, PANC-1, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.076 | 19/47 (PANC-1, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.25× | +3.0 | 0.14 | 19/46 (NCI-H1792, SK-MEL-2, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2501.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Tadalafil (drug)]] 0.05 µM in 1 line (SW48 0.0447×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 0.373×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.612×** | -4.6 | 0.002 | 29/46 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.675×** | -3.7 | 0.056 | 24/47 (HT-29, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.716× | -3.2 | 0.24 | 20/46 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.718× | -3.1 | 0.24 | 21/46 (A-427, KATO III, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.728× | -3.0 | 0.30 | 17/47 (PANC-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 31.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 52.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 55.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +10.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0447× (z -11.9) |
| [[A-427 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBP]] | +0.64 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[TEF]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[BDH2]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[ZNF608]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BHLHE41]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CBX8]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.60 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[AMOT]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NFIX]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[LGALS3]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[SNX2]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CA11]] | +0.56 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.62 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[TTL]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[NFATC2IP]] | -0.57 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ZBED4]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[VKORC1L1]] | -0.55 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[ARPC5L]] | -0.54 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[NBPF15]] | -0.54 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[SRPK1]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TANGO2]] | -0.53 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[NBPF20]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[GATAD2A]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PTPN9]] | -0.52 | -0.56 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAR3]] | B | BCAR3 activity lowers ECH1's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 1.74× higher at baseline in the lines without BCAR3 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.5, 2.6); signed map (29.0, 7.4). **Vector** length 76.1, 18.6% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.3 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +2.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +1.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.4 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | enoyl-CoA hydratase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,815,422-38,831,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HPXEL |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, PEROXISOME, FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Peroxisomal protein import; Mitochondrial protein degradation; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13011](https://www.uniprot.org/uniprotkb/Q13011) (Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase, mitochondrial):

> Auxiliary enzyme in the beta-oxidation of mono- and polyunsaturated fatty acids. Together with the 2,4-dienoyl-CoA reductase (DECR) and the Enoyl-CoA delta isomerase 1 (ECI1) they allow reentrance of the enoyl-CoA into the beta-oxidation cycle. Able to isomerize 3-trans,5-cis-dienoyl-CoA (3E,5Z-dienoyl-CoA) to 2-trans,4-trans-dienoyl-CoA (2E,4E-dienoyl-CoA), a crucial step in the beta-oxidation of unsaturated fatty acids with double bonds at odd position (By similarity). Based on its …

**Summary**, from NCBI Gene [1891](https://www.ncbi.nlm.nih.gov/gene/1891):

> This gene encodes a member of the hydratase/isomerase superfamily. The gene product shows high sequence similarity to enoyl-coenzyme A (CoA) hydratases of several species, particularly within a conserved domain characteristic of these proteins. The encoded protein, which contains a C-terminal peroxisomal targeting sequence, localizes to the peroxisome. The rat ortholog, which localizes to the matrix of both the peroxisome and mitochondria, can isomerize 3-trans,5-cis-dienoyl-CoA to …

**Accessions** — [HGNC:3149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3149) · Entrez [1891](https://www.ncbi.nlm.nih.gov/gene/1891) · UniProt [Q13011](https://www.uniprot.org/uniprotkb/Q13011) · Ensembl [ENSG00000104823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104823)

## Data

Gene col 2501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2501); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2501]; `tensor/DDL_lfc|DDL_z.npy` [2501]; `embed/gene_vectors.npy` [2501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2501 or target_col == 2501). Every well: [[ECH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
