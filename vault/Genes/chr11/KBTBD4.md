---
symbol: "KBTBD4"
type: "gene"
col: 4434
ensembl_id: "ENSG00000123444"
name: "kelch repeat and BTB domain containing 4"
location: "11p11.2"
module: 118
arm: "+"
pooled_cpm: 6.82
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# KBTBD4

*kelch repeat and BTB domain containing 4* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +9.7, q 1e-19, up in 25 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.601× (z -6.5, q 3e-08, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBCC]] (+0.72, fdr 1e-05), [[ZNF446]] (+0.71, fdr 1e-05), [[SLC4A1AP]] (+0.68, fdr 7e-06); moves opposite to [[LYPLA1]] (-0.64, fdr 1e-05), [[CPSF6]] (-0.64, fdr 3e-05), [[CHML]] (-0.58, fdr 9e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPAG4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4434.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +9.7 | 1e-19 | 25/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +5.3 | 3e-05 | 17/44 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.3 | 0.004 | 13/36 (NCI-H1573, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.39×** | +4.2 | 0.004 | 8/39 (KATO III, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.8 | 0.016 | 8/28 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +3.5 | 0.040 | 5/22 (PANC-1, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.040 | 8/41 (HEC-1-A, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.040 | 11/46 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.086 | 3/44 (Hs 766T, HOP62, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.12 | 7/41 (HT-29, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4434.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.601×** | -6.5 | 3e-08 | 23/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.624×** | -6.1 | 4e-07 | 19/46 (H4, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.630×** | -5.9 | 5e-07 | 23/47 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.623×** | -5.9 | 7e-07 | 17/37 (J82, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.647×** | -5.6 | 2e-06 | 17/29 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.665×** | -5.3 | 1e-05 | 17/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.713×** | -4.4 | 1e-03 | 8/47 (KATO III, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.708×** | -3.9 | 0.006 | 10/18 (J82, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.014 | 14/47 (A498, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.767×** | -3.4 | 0.035 | 10/47 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.605×** | -3.4 | 0.037 | 8/45 (A498, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.778×** | -3.1 | 0.084 | 6/11 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4434. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.25 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.326× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 7.48 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -10.3) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 5.02 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0834× (z -9.7) |
| [[PANC-1 (line)]] | alt | 7.93 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -14.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 7.32 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.116× (z -9.7) |
| [[SW480 (line)]] | alt | 9.27 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4434), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBCC]] | +0.72 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[ZNF446]] | +0.71 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SYNRG]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[DPF2]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.67 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[SMG8]] | +0.67 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[NGDN]] | +0.66 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[GPATCH1]] | +0.65 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PI4KB]] | +0.64 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[BTN2A1]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[GPANK1]] | +0.63 | +0.52 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPLA1]] | -0.64 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CPSF6]] | -0.64 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[CHML]] | -0.58 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[RSU1]] | -0.58 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[VPS13A]] | -0.55 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[PRKCI]] | -0.55 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[ACSL4]] | -0.55 | -0.40 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPAG4]] | B | SPAG4 activity raises KBTBD4's level | lines that do not express SPAG4 (6) vs lines expressing it (44) | 1.15× lower at baseline in the lines without SPAG4 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with PRDM2; also absent: ZNF222, ADAL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.773). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-45.6, -3.0); signed map (-7.1, -5.0). **Vector** length 60.9, 9.30% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.1 | +0.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.1 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | kelch repeat and BTB domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,572,197-47,578,976 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10450, HSPC252; previously BKLHD4 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVX7](https://www.uniprot.org/uniprotkb/Q9NVX7) (Kelch repeat and BTB domain-containing protein 4):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex which targets CoREST corepressor complex components RCOR1, KDM1A/LSD1 and HDAC2 for proteasomal degradation. RCOR1 is likely to be the primary target while degradation of KDM1A and HDAC2 is likely due to their association with RCOR1. Also targets RCOR3, MIER2 and MIER3 for proteasomal degradation as well as associated proteins ZNF217 and RREB1. Degradation is dependent on the presence of an ELM2 domain in the target …

**Summary**, from NCBI Gene [55709](https://www.ncbi.nlm.nih.gov/gene/55709):

> Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23761](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23761) · Entrez [55709](https://www.ncbi.nlm.nih.gov/gene/55709) · UniProt [Q9NVX7](https://www.uniprot.org/uniprotkb/Q9NVX7) · Ensembl [ENSG00000123444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123444)

## Data

Gene col 4434: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4434); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4434, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4434]; `tensor/DDL_lfc|DDL_z.npy` [4434]; `embed/gene_vectors.npy` [4434]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4434 or target_col == 4434). Every well: [[KBTBD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KBTBD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
