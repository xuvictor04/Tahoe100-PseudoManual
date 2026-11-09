---
symbol: "RDH14"
type: "gene"
col: 14251
ensembl_id: "ENSG00000240857"
name: "retinol dehydrogenase 14"
location: "2p24.2"
module: 11
arm: "+"
pooled_cpm: 11.48
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# RDH14

*retinol dehydrogenase 14* — 2p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.66× (z +5.7, q 7e-06, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.390× (z -10.6, q 3e-23, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP38]] (+0.75, fdr 7e-06), [[PHAX]] (+0.75, fdr 7e-06), [[NSMCE3]] (+0.74, fdr 1e-05); moves opposite to [[COL18A1]] (-0.60, fdr 2e-05), [[APLP2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MMP14]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14251.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.7 | 7e-06 | 25/46 (A-172, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.3 | 0.005 | 21/43 (A549, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.2 | 0.006 | 20/47 (A549, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.8 | 0.018 | 15/40 (A-172, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | 1.23× | +3.3 | 0.10 | 16/48 (A549, HS-578T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.34× | +3.2 | 0.13 | 17/39 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.0 | 0.20 | 2/48 (MIA PaCa-2, hTERT-HPNE) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14251.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.390×** | -10.6 | 3e-23 | 36/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -7.6 | 1e-11 | 32/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.649×** | -6.8 | 2e-09 | 30/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -6.7 | 3e-09 | 32/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.624×** | -5.3 | 2e-05 | 24/47 (NCI-H460, A549, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.672×** | -4.4 | 8e-04 | 21/47 (NCI-H23, NCI-H460, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.673×** | -4.4 | 8e-04 | 22/47 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -4.0 | 0.005 | 18/47 (SW 900, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.539×** | -3.6 | 0.018 | 12/43 (NCI-H1573, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.731×** | -3.5 | 0.026 | 16/36 (MIA PaCa-2, NCI-H2030, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.729×** | -3.4 | 0.034 | 16/40 (LS 180, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.565×** | -3.3 | 0.039 | 16/47 (HepG2/C3A, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.747×** | -3.3 | 0.048 | 13/47 (NCI-H460, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.751×** | -3.2 | 0.055 | 13/46 (PANC-1, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14251. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 15.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0667× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.225× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -14.1) |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0843× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -10.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 10.4 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -12.1) |
| [[COLO 205 (line)]] | alt | 8.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -9.9) |
| [[H4 (line)]] | wt | 9.41 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0797× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0797× (z -14.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 6.09 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0902× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0547× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[RKO (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -8.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14251), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP38]] | +0.75 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[PHAX]] | +0.75 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.74 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[MRPL46]] | +0.72 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[DAXX]] | +0.72 | +0.42 / +0.76 | both halves | 4e-05 |  |
| [[OBI1]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[CCDC137]] | +0.70 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[OXLD1]] | +0.70 | +0.47 / +0.75 | both halves | 2e-05 |  |
| [[ABRAXAS2]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.68 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[RPP25L]] | +0.68 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[MRPL44]] | +0.68 | +0.49 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL18A1]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[APLP2]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP14]] | B | MMP14 activity lowers RDH14's level | lines that do not express MMP14 (19) vs lines expressing it (31) | 1.21× higher at baseline in the lines without MMP14 | 0.096 | ⚠ within organs, on part of the lines; also absent: IFI16, PTGFR, EVA1A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.2, 4.0); signed map (0.3, -19.1). **Vector** length 73.1, 13.6% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -7.3 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -6.9 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -6.2 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -4.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | retinol dehydrogenase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.2 — chr2:18,554,723-18,560,679 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAN2, SDR7C4 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 3 pathways, smallest: RA biosynthesis pathway; Signaling by Retinoic Acid; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBH5](https://www.uniprot.org/uniprotkb/Q9HBH5) (Retinol dehydrogenase 14):

> Retinol dehydrogenase with a clear preference for NADP. Displays high activity towards 9-cis, 11-cis and all-trans-retinol. Shows a very weak activity towards 13-cis-retinol. Has no activity towards steroid.

**Summary**, from NCBI Gene [57665](https://www.ncbi.nlm.nih.gov/gene/57665):

> Enables all-trans-retinol dehydrogenase (NADP+) activity. Involved in osteoblast differentiation. Located in cytosol; endoplasmic reticulum; and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19979](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19979) · Entrez [57665](https://www.ncbi.nlm.nih.gov/gene/57665) · UniProt [Q9HBH5](https://www.uniprot.org/uniprotkb/Q9HBH5) · Ensembl [ENSG00000240857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240857)

## Data

Gene col 14251: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14251); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14251, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14251]; `tensor/DDL_lfc|DDL_z.npy` [14251]; `embed/gene_vectors.npy` [14251]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14251 or target_col == 14251). Every well: [[RDH14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RDH14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
