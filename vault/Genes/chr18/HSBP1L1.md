---
symbol: "HSBP1L1"
type: "gene"
col: 13552
ensembl_id: "ENSG00000226742"
name: "heat shock factor binding protein 1 like 1"
location: "18q23"
module: 35
arm: "+"
pooled_cpm: 10.78
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# HSBP1L1

*heat shock factor binding protein 1 like 1* — 18q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.44× (z +8.3, q 6e-14, up in 28 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +4.9, q 2e-04, up in 21 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.278× (z -11.9, q 1e-29, down in 38 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRASP3]] (+0.64, fdr 1e-05), [[TCEAL1]] (+0.64, fdr 1e-05), [[C11orf1]] (+0.63, fdr 1e-05); moves opposite to [[SLX4]] (-0.66, fdr 1e-05), [[EHD4]] (-0.58, fdr 5e-05), [[TMEM104]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HSD11B2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13552.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +8.3 | 6e-14 | 28/31 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +6.6 | 1e-08 | 11/16 (HCT15, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +4.9 | 2e-04 | 21/40 (J82, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +4.7 | 3e-04 | 13/23 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.1 | 0.005 | 17/34 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.9 | 0.007 | 16/31 (SNU-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.41× | +3.2 | 0.12 | 16/39 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.26× | +3.0 | 0.17 | 10/40 (NCI-H23, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13552.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.278×** | -11.9 | 1e-29 | 38/40 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.314×** | -10.7 | 2e-24 | 37/40 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.340×** | -10.0 | 4e-21 | 36/40 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.561×** | -5.3 | 1e-05 | 26/40 (LS 180, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.631×** | -4.3 | 0.002 | 19/40 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -3.5 | 0.051 | 13/39 (SNU-423, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -3.3 | 0.081 | 12/40 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.703×** | -3.3 | 0.081 | 15/37 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.444×** | -3.2 | 0.096 | 15/40 (KATO III, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.447×** | -3.1 | 0.096 | 12/38 (A-427, SNU-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.6 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -11.8) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.128× (z -11.3) |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -14.9) |
| [[COLO 205 (line)]] | alt | 7.25 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0541× (z -9.6) |
| [[KATO III (line)]] | alt | 16.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0654× (z -15.3) |
| [[SNU-423 (line)]] | alt | 6.58 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0953× (z -9.2) |
| [[A-427 (line)]] | wt | 26.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -9.9) |
| [[HCT15 (line)]] | alt | 27.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 9.40 | 0 | 1 (1 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0564× (z -9.7) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -8.5) |
| [[LoVo (line)]] | wt | 10.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0994× (z -11.5) |
| [[PANC-1 (line)]] | alt | 16.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -8.8) |
| [[RKO (line)]] | wt | 17.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -10.5) |
| [[SW480 (line)]] | alt | 5.32 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -8.5) |
| [[A-172 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRASP3]] | +0.64 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.64 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[C11orf1]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[THAP3]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[N4BP2L1]] | +0.61 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[PIGP]] | +0.60 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[ZNF219]] | +0.59 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[STAP2]] | +0.58 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[EIF4EBP3]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[RAB21]] | +0.58 | +0.41 / +0.44 | both halves | 4e-05 |  |
| [[CCDC59]] | +0.57 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CREB3L4]] | +0.57 | +0.49 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLX4]] | -0.66 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[EHD4]] | -0.58 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TMEM104]] | -0.56 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[BLTP2]] | -0.55 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[ODF2]] | -0.55 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[GNB1L]] | -0.54 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[SEPTIN10]] | -0.54 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[RECQL]] | -0.54 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PDCD6]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[TUBG1]] | -0.53 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[ZBED4]] | -0.52 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[ITGB1]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD11B2]] | B | HSD11B2 activity raises HSBP1L1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without HSD11B2 | 0.083 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HSBP1L1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.453). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-2.6, 16.3); signed map (19.2, -14.2). **Vector** length 69.0, 15.6% of its response variance represented; |z| ≥ 3 in 602 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.1 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.8 | -10.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -11.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.7 | -10.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | heat shock factor binding protein 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q23 — chr18:79,964,582-79,970,822 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10967, MGC189743 |
| Matched by | ensembl_id |

UniProt [C9JCN9](https://www.uniprot.org/uniprotkb/C9JCN9) carries no function annotation.

**Summary**, from NCBI Gene [440498](https://www.ncbi.nlm.nih.gov/gene/440498):

> Predicted to enable transcription corepressor activity. Predicted to be involved in cellular heat acclimation. Predicted to be active in cytosol and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37243) · Entrez [440498](https://www.ncbi.nlm.nih.gov/gene/440498) · UniProt [C9JCN9](https://www.uniprot.org/uniprotkb/C9JCN9) · Ensembl [ENSG00000226742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226742)

## Data

Gene col 13552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13552); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13552]; `tensor/DDL_lfc|DDL_z.npy` [13552]; `embed/gene_vectors.npy` [13552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13552 or target_col == 13552). Every well: [[HSBP1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSBP1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
