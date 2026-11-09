---
symbol: "NDUFB8"
type: "gene"
col: 9243
ensembl_id: "ENSG00000166136"
name: "NADH:ubiquinone oxidoreductase subunit B8"
location: "10q24.31"
module: 134
arm: "+"
pooled_cpm: 42.98
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# NDUFB8

*NADH:ubiquinone oxidoreductase subunit B8* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.49× (z +8.1, q 3e-13, up in 42 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 5.14×, KATO III 3.65×, NCI-H1573 3.92×, SW480 3.03×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 3.79×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.687× (z -5.6, q 1e-05, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM162A]] (+0.66, fdr 1e-05), [[PIAS2]] (+0.66, fdr 1e-05), [[PEX3]] (+0.65, fdr 1e-05); moves opposite to [[CFAP161]] (-0.52, fdr 1e-04), [[PXDC1]] (-0.50, fdr 3e-04), [[PCBD2]] (-0.50, fdr 6e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GPR155]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9243.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 5.14×, KATO III 3.65×, NCI-H1573 3.92×, SW480 3.03×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 3.79×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.49×** | +8.1 | 3e-13 | 42/45 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.06×** | +7.4 | 3e-11 | 35/42 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.66×** | +5.4 | 1e-05 | 39/46 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.58×** | +4.5 | 8e-04 | 30/44 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.40×** | +3.6 | 0.031 | 24/47 (NCI-H1573, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.687×** | -5.6 | 1e-05 | 37/48 (SK-MEL-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.401×** | -4.3 | 0.004 | 40/48 (HCT15, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.687×** | -4.0 | 0.013 | 29/48 (C32, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -3.5 | 0.079 | 24/48 (C32, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.512× | -3.2 | 0.17 | 23/48 (LoVo, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.752× | -3.0 | 0.24 | 15/48 (C-33 A, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 33.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.14× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.2) |
| [[C32 (line)]] | wt | 107 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -10.7) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -11.2) |
| [[H4 (line)]] | wt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -8.8) |
| [[KATO III (line)]] | alt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 39.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 64.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 47.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 56.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.8) |
| [[SW480 (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM162A]] | +0.66 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[PIAS2]] | +0.66 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[PEX3]] | +0.65 | +0.65 / +0.51 | both halves | 1e-05 | pathway: Protein localization |
| [[CABIN1]] | +0.65 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PDK3]] | +0.63 | +0.65 / +0.43 | both halves | 3e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[BRWD3]] | +0.61 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[DPCD]] | +0.60 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[BNIP3]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ATP5PO]] ⚠ | +0.59 | +0.29 / +0.61 | both halves | 2e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 882; ⚠ in the vector space only through flagged drug-doses |
| [[UQCRQ]] ⚠ | +0.58 | +0.60 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 997; ⚠ in the vector space only through flagged drug-doses |
| [[AP2S1]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[HDAC3]] | +0.58 | +0.62 / +0.36 | both halves | 9e-05 |  |
| [[ATRN]] | +0.58 | +0.60 / +0.34 | both halves | 1e-04 |  |
| [[RALGAPA2]] | +0.57 | +0.55 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP161]] | -0.52 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[PXDC1]] | -0.50 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[PCBD2]] | -0.50 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[ERMAP]] | -0.49 | -0.48 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR155]] | B | GPR155 activity raises NDUFB8's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without GPR155 | 0.017 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[SMAD9]] | B | SMAD9 activity raises NDUFB8's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 1.34× lower at baseline in the lines without SMAD9 | 0.049 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[TET1]] | B | TET1 activity raises NDUFB8's level | lines that do not express TET1 (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without TET1 | 0.098 | ⚠ within organs, on part of the lines; also absent: PLEKHO1, MCAM, KCNK13; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.2, -18.2); signed map (-37.8, 23.5). **Vector** length 64.0, 17.6% of its response variance represented; |z| ≥ 3 in 464 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | -0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | -0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | +1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -3.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,523,740-100,530,000 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASHI, CI-ASHI |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Mitochondrial protein import; Complex I biogenesis; Respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95169](https://www.uniprot.org/uniprotkb/O95169) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4714](https://www.ncbi.nlm.nih.gov/gene/4714):

> Predicted to enable NADH dehydrogenase (ubiquinone) activity. Predicted to be involved in mitochondrial electron transport, NADH to ubiquinone and proton motive force-driven mitochondrial ATP synthesis. Located in mitochondrial inner membrane. Part of respiratory chain complex I. Implicated in nuclear type mitochondrial complex I deficiency 32. Biomarker of Alzheimer's disease and Parkinson's disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7703) · Entrez [4714](https://www.ncbi.nlm.nih.gov/gene/4714) · UniProt [O95169](https://www.uniprot.org/uniprotkb/O95169) · Ensembl [ENSG00000166136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166136)

## Data

Gene col 9243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9243); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9243]; `tensor/DDL_lfc|DDL_z.npy` [9243]; `embed/gene_vectors.npy` [9243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9243 or target_col == 9243). Every well: [[NDUFB8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
