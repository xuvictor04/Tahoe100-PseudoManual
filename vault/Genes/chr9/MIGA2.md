---
symbol: "MIGA2"
type: "gene"
col: 7270
ensembl_id: "ENSG00000148343"
name: "mitoguardin 2"
location: "9q34.11"
module: 3
arm: "+"
pooled_cpm: 12.32
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# MIGA2

*mitoguardin 2* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.34× (z +21.1, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.671× (z -5.7, q 5e-06, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPND]] (+0.73, fdr 1e-05), [[E4F1]] (+0.73, fdr 1e-05), [[TSC2]] (+0.72, fdr 8e-06); moves opposite to [[ZNF300]] (-0.64, fdr 8e-05), [[EIF4G2]] (-0.62, fdr 7e-05), [[NXT2]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BMPR1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.34×** | +21.1 | 0e+00 | 47/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.78×** | +19.1 | 0e+00 | 45/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.34×** | +17.3 | 0e+00 | 46/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +13.3 | 5e-38 | 39/46 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +7.4 | 1e-11 | 27/46 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.9 | 4e-07 | 21/43 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.1 | 3e-05 | 15/40 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.7 | 2e-04 | 19/46 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.003 | 13/44 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.004 | 16/47 (SHP-77, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.016 | 13/47 (HEC-1-A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.026 | 10/47 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7270.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.671×** | -5.7 | 5e-06 | 26/46 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -5.5 | 1e-05 | 26/48 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.788×** | -4.8 | 3e-04 | 18/48 (A498, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.013 | 13/46 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.794× | -3.3 | 0.10 | 6/48 (NCI-H661, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.69× (z +12.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.29× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -9.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 6.05 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.56× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 15.2 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.25× (z +9.1) | [[Harringtonine (drug)]] 0.05 µM 0.215× (z -9.0) |
| [[RKO (line)]] | wt | 30.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 18.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.71× (z +10.5) | — |
| [[SW480 (line)]] | alt | 14.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.02× (z +14.2) | — |
| [[KATO III (line)]] | alt | 14.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.28× (z +10.1) | — |
| [[LoVo (line)]] | wt | 9.73 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.66× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 11.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.22× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 16.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.84× (z +8.8) | — |
| [[H4 (line)]] | wt | 9.51 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.5 µM 0.0734× (z -8.6) |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 9.50 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.67× (z +8.9) | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0865× (z -9.3) |
| [[A-427 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPND]] | +0.73 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[E4F1]] | +0.73 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[TSC2]] | +0.72 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[SPSB3]] | +0.71 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.71 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[RNF41]] | +0.70 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[DHTKD1]] | +0.70 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[RAB40C]] | +0.70 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[PSMD9]] | +0.68 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[PMM1]] | +0.68 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ANKS3]] | +0.68 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[TTC38]] | +0.68 | +0.60 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF300]] | -0.64 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[EIF4G2]] | -0.62 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[NXT2]] | -0.60 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[KRT8P12]] | -0.60 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[ARAP2]] | -0.59 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CRPPA]] | -0.59 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[SLC39A10]] | -0.58 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[KICS2]] | -0.58 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[ADAMTS3]] | -0.58 | -0.37 / -0.50 | both halves | 9e-05 |  |
| [[NCR3LG1]] | -0.58 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[ZNF462]] | -0.57 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[BMPR1B]] | -0.57 | -0.33 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPR1B]] | B | BMPR1B activity lowers MIGA2's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.32× higher at baseline in the lines without BMPR1B | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.3, -2.9); signed map (-35.6, -0.0). **Vector** length 81.2, 15.7% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +21.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +19.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +17.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +7.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +2.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.7 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | mitoguardin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:129,036,621-129,072,082 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14596, FLJ00199; previously C9orf54, FAM73B |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L4E1](https://www.uniprot.org/uniprotkb/Q7L4E1) (Mitoguardin 2):

> Regulator of mitochondrial fusion: acts by forming homo- and heterodimers at the mitochondrial outer membrane and facilitating the formation of PLD6/MitoPLD dimers. May act by regulating phospholipid metabolism via PLD6/MitoPLD.

**Summary**, from NCBI Gene [84895](https://www.ncbi.nlm.nih.gov/gene/84895):

> Enables protein heterodimerization activity and protein homodimerization activity. Involved in mitochondrial fusion. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23621) · Entrez [84895](https://www.ncbi.nlm.nih.gov/gene/84895) · UniProt [Q7L4E1](https://www.uniprot.org/uniprotkb/Q7L4E1) · Ensembl [ENSG00000148343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148343)

## Data

Gene col 7270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7270); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7270]; `tensor/DDL_lfc|DDL_z.npy` [7270]; `embed/gene_vectors.npy` [7270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7270 or target_col == 7270). Every well: [[MIGA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIGA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
