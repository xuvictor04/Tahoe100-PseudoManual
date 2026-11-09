---
symbol: "CCN4"
type: "gene"
col: 2458
ensembl_id: "ENSG00000104415"
name: "cellular communication network factor 4"
location: "8q24.22"
module: 21
arm: "+"
pooled_cpm: 5.53
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CCN4

*cellular communication network factor 4* — 8q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.67× (z +13.0, q 9e-36, up in 13 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +7.8, q 7e-13, up in 18 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.567× (z -5.6, q 1e-05, down in 19 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR84-AS1]] (+0.66, fdr 7e-06), [[ITGA8]] (+0.63, fdr 1e-05), [[MGP]] (+0.59, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DCN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.67×** | +13.0 | 9e-36 | 13/18 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +12.1 | 5e-31 | 3/6 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +8.3 | 3e-14 | 3/9 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +7.8 | 7e-13 | 18/33 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.010 | 5/28 (NCI-H1792, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.038 | 4/45 (HOP62, A498, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.5 | 0.044 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.056 | 7/44 (KATO III, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +3.2 | 0.089 | 3/17 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.54× | +3.1 | 0.11 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.567×** | -5.6 | 1e-05 | 19/35 (RPMI-7951, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.568×** | -5.4 | 2e-05 | 15/39 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.662×** | -4.1 | 0.008 | 12/44 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -4.0 | 0.009 | 11/45 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.681×** | -3.8 | 0.016 | 12/45 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.692×** | -3.6 | 0.025 | 15/40 (NCI-H1573, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.696×** | -3.6 | 0.027 | 12/43 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.701×** | -3.5 | 0.030 | 12/43 (HT-29, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.708×** | -3.2 | 0.095 | 3/43 (SHP-77, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 64.4 | 10 | 7 (5 ⚠) | [[Dexamethasone (drug)]] 5 µM 7.22× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -13.7) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0558× (z -19.6) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0239× (z -17.9) |
| [[HT-29 (line)]] | alt | 4.74 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0895× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 6.14 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0836× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 3.25 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0470× (z -10.4) |
| [[A-172 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR84-AS1]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ITGA8]] | +0.63 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[MGP]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[C1QTNF7]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[KIAA1614]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[TICAM2-AS1]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SLC13A4]] | +0.55 | +0.40 / +0.52 | both halves | 4e-05 |  |
| [[VCAN-AS1]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ABHD15-AS1]] | +0.55 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[GCNT7]] | +0.55 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[MASP2]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[HSD11B1]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCN]] | B | DCN activity raises CCN4's level | lines that do not express DCN (39) vs lines expressing it (11) | 3.10× lower at baseline in the lines without DCN | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1 |
| [[LOX]] | B | LOX activity raises CCN4's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without LOX | 0.037 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[DCN]] | B | DCN activity weakens CCN4's drug response | lines that do not express DCN (37) vs lines expressing it (8) | the lines without DCN respond 1.00× as strongly (z diff +0.17); strongest at Dinaciclib 0.5 µM: 3.10x vs 0.30x (z diff -8.1) | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1; target measured in part of the lines; both ways; artifact flags |
| [[ADGRG7]] | B | ADGRG7 activity raises CCN4's level | lines that do not express ADGRG7 (40) vs lines expressing it (10) | 3.38× lower at baseline in the lines without ADGRG7 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000287474, ENSG00000253642, ENSG00000287172 |
| [[CA12]] | B | CA12 activity raises CCN4's level | lines that do not express CA12 (29) vs lines expressing it (21) | 1.95× lower at baseline in the lines without CA12 | 0.056 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[OR9Q1]] | B | OR9Q1 activity raises CCN4's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without OR9Q1 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[HTRA3]] | B | HTRA3 activity raises CCN4's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without HTRA3 | 0.076 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.8, 23.2); signed map (24.2, 38.5). **Vector** length 55.5, 7.29% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -3.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | cellular communication network factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.22 — chr8:133,191,039-133,231,690 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WISP-1; previously WISP1-OT1, WISP1-UT1, WISP1 |
| Gene groups (HGNC) | Cellular communication network factors |
| Matched by | ensembl_id |

**Function**, from UniProt [O95388](https://www.uniprot.org/uniprotkb/O95388) (CCN family member 4):

> Downstream regulator in the Wnt/Frizzled-signaling pathway. Associated with cell survival. Attenuates p53-mediated apoptosis in response to DNA damage through activation of AKT kinase. Up-regulates the anti-apoptotic Bcl-X(L) protein. Adheres to skin and melanoma fibroblasts. In vitro binding to skin fibroblasts occurs through the proteoglycans, decorin and biglycan.

**Summary**, from NCBI Gene [8840](https://www.ncbi.nlm.nih.gov/gene/8840):

> This gene encodes a member of the WNT1 inducible signaling pathway (WISP) protein subfamily, which belongs to the connective tissue growth factor (CTGF) family. WNT1 is a member of a family of cysteine-rich, glycosylated signaling proteins that mediate diverse developmental processes. The CTGF family members are characterized by four conserved cysteine-rich domains: insulin-like growth factor-binding domain, von Willebrand factor type C module, thrombospondin domain and C-terminal cystine …

**Accessions** — [HGNC:12769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12769) · Entrez [8840](https://www.ncbi.nlm.nih.gov/gene/8840) · UniProt [O95388](https://www.uniprot.org/uniprotkb/O95388) · Ensembl [ENSG00000104415](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104415)

## Data

Gene col 2458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2458); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2458]; `tensor/DDL_lfc|DDL_z.npy` [2458]; `embed/gene_vectors.npy` [2458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2458 or target_col == 2458). Every well: [[CCN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
