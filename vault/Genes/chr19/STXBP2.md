---
symbol: "STXBP2"
type: "gene"
col: 1168
ensembl_id: "ENSG00000076944"
name: "syntaxin binding protein 2"
location: "19p13.2"
module: 35
arm: "+"
pooled_cpm: 16.66
n_lines_expressing: 39
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# STXBP2

*syntaxin binding protein 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +8.6, q 3e-15, up in 23 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.571× (z -10.0, q 8e-21, down in 28 of 36 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.623× (z -8.5, q 5e-15, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN1L]] (+0.69, fdr 1e-05), [[FBRS]] (+0.62, fdr 1e-05), [[INPPL1]] (+0.61, fdr 3e-05); moves opposite to [[GGCT]] (-0.58, fdr 3e-05), [[SLC27A2]] (-0.57, fdr 3e-05), [[UBE3D]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +8.6 | 3e-15 | 23/36 (SNU-423, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.1 | 1e-04 | 11/22 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +4.4 | 0.002 | 13/33 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.1 | 0.006 | 11/30 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.006 | 8/32 (NCI-H23, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.008 | 12/35 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.036 | 10/37 (HOP62, SW1417, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.069 | 8/35 (COLO 205, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.14× | +3.2 | 0.089 | 10/36 (RKO, Panc 03.27, …) | top dose only | low cells (technical?) |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.097 | 4/36 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.1 | 0.097 | 2/36 (NCI-H2030, COLO 205) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.11 | 5/36 (KATO III, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1168.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.571×** | -10.0 | 8e-21 | 28/36 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.612×** | -8.8 | 5e-16 | 26/36 (A498, AsPC-1, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.623×** | -8.5 | 5e-15 | 28/36 (A498, SW 900, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.777×** | -6.4 | 2e-08 | 21/37 (HOP62, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.716×** | -6.0 | 3e-07 | 20/36 (SK-MEL-2, AsPC-1, …) | all doses, flat | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.637×** | -4.2 | 0.002 | 15/37 (HCT15, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.799×** | -4.0 | 0.005 | 13/35 (RKO, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.815×** | -3.7 | 0.017 | 9/36 (J82, HEC-1-A, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.873× | -3.5 | 0.035 | 6/37 (NCI-H460, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.416× (z -8.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -12.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1L]] | +0.69 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[FBRS]] | +0.62 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[INPPL1]] | +0.61 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[OTUB1]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZNF687]] | +0.60 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[TRAPPC6B]] | +0.60 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[BECN1]] | +0.59 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[ZNF547]] | +0.59 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[ZNF490]] | +0.59 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[ATN1]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[WDR45]] | +0.58 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[PET100]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 | ⚠ same locus (4.8 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF213-AS1]] | +0.58 | +0.34 / +0.41 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGCT]] | -0.58 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SLC27A2]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[UBE3D]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SERBP1]] | -0.56 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CDIN1]] | -0.56 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CBX3]] | -0.56 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[FXN]] | -0.55 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[LDHB]] | -0.54 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[NPM3]] | -0.53 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[SPIDR]] | -0.52 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[PALS2]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SCML2]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises STXBP2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises STXBP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.544). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-14.7, -21.3); signed map (17.3, -20.7). **Vector** length 61.0, 11.8% of its response variance represented; |z| ≥ 3 in 561 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +5.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.5 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +3.3 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.0 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -6.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.9 | -10.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,636,772-7,647,873 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNC18B, Hunc18b, Unc18-2, MUNC18-2 |
| Gene groups (HGNC) | SM family of SNARE chaperones |
| Reactome | 7 pathways, smallest: Other interleukin signaling; Platelet degranulation; Response to elevated platelet cytosolic Ca2+ |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15833](https://www.uniprot.org/uniprotkb/Q15833) (Syntaxin-binding protein 2):

> Functions in intracellular vesicle trafficking through interaction with SNAREs (soluble N-ethylmaleimide-sensitive factor-attachment protein receptors) which are essential proteins for membrane fusion. By promoting the assembly of functional STX11/SNAP23/VAMP8 SNARE complexes at the plasma membrane, regulates cytotoxic granule exocytosis in natural killer (NK) cells.

**Summary**, from NCBI Gene [6813](https://www.ncbi.nlm.nih.gov/gene/6813):

> This gene encodes a member of the STXBP/unc-18/SEC1 family. The encoded protein is involved in intracellular trafficking, control of SNARE (soluble NSF attachment protein receptor) complex assembly, and the release of cytotoxic granules by natural killer cells. Mutations in this gene are associated with familial hemophagocytic lymphohistiocytosis. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:11445](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11445) · Entrez [6813](https://www.ncbi.nlm.nih.gov/gene/6813) · UniProt [Q15833](https://www.uniprot.org/uniprotkb/Q15833) · Ensembl [ENSG00000076944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076944)

## Data

Gene col 1168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1168); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1168]; `tensor/DDL_lfc|DDL_z.npy` [1168]; `embed/gene_vectors.npy` [1168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1168 or target_col == 1168). Every well: [[STXBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STXBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
