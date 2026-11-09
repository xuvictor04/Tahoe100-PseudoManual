---
symbol: "PICK1"
type: "gene"
col: 1881
ensembl_id: "ENSG00000100151"
name: "protein interacting with PRKCA 1"
location: "22q13.1"
module: 49
arm: "+"
pooled_cpm: 10.37
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# PICK1

*protein interacting with PRKCA 1* — 22q13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.634× (z -9.4, q 3e-18, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AAAS]] (+0.61, fdr 1e-05), [[APBB3]] (+0.58, fdr 1e-05), [[LPIN3]] (+0.58, fdr 3e-05); moves opposite to [[KLF12]] (-0.56, fdr 1e-05), [[SCHIP1]] (-0.55, fdr 2e-05), [[NECTIN3]] (-0.51, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CNKSR1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1881.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | 1.24× | +3.1 | 0.94 | 2/45 (NCI-H1573, H4) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1881.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -9.4 | 3e-18 | 30/41 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.639×** | -6.5 | 2e-08 | 26/45 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.713×** | -4.9 | 2e-04 | 13/45 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.732×** | -4.6 | 8e-04 | 22/42 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.729×** | -4.4 | 0.001 | 19/40 (A-172, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.745×** | -4.3 | 0.002 | 12/45 (SNU-1, SHP-77, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.744×** | -4.2 | 0.003 | 11/20 (HCT15, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.758×** | -4.0 | 0.004 | 11/45 (NCI-H1792, SW 1271, …) | all doses, flat |  |
| [[Arbutin (drug)]] 5 µM |  | **0.769×** | -3.7 | 0.015 | 9/42 (A-172, H4, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **0.781×** | -3.6 | 0.018 | 15/31 (HCT15, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.783×** | -3.6 | 0.018 | 16/44 (CHP-212, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.810× | -3.1 | 0.10 | 7/42 (SNU-1, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.814× | -3.0 | 0.12 | 11/44 (SNU-1, SK-MEL-2, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1881. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.15 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.101× (z -9.1) |
| [[A549 (line)]] | wt | 6.99 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.103× (z -10.3) ⚠ toxic |
| [[HCT15 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[HepG2_C3A (line)]] | wt | 7.69 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.0702× (z -9.0) |
| [[HT-29 (line)]] | alt | 8.67 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0732× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[NCI-H460 (line)]] | wt | 3.21 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0816× (z -11.4) |
| [[A-427 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1881), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAAS]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[APBB3]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[LPIN3]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[TUT1]] | +0.57 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[PARP6]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[MED24]] | +0.55 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[KLHL12]] | +0.55 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[SEC23B]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RUSF1]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[COPG1]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SKIC2]] | +0.53 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[NISCH]] | +0.53 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF12]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SCHIP1]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 | pathway: HALLMARK_MYOGENESIS |
| [[NECTIN3]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ARHGAP21]] | -0.49 | -0.34 / -0.42 | both halves | 1e-04 | same gene group |
| [[PBX3]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[CDK14]] | -0.45 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[ZSWIM6]] | -0.45 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CD44]] | -0.45 | -0.44 / -0.40 | both halves | 4e-05 | pathway: Cell surface interactions at the vascular wall |
| [[SNTB2]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 | same gene group |
| [[ZEB1]] | -0.44 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[DOCK9]] | -0.44 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[IQCJ-SCHIP1]] | -0.44 | -0.36 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNKSR1]] | B | CNKSR1 activity raises PICK1's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 1.72× lower at baseline in the lines without CNKSR1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[CCDC120]] | B | CCDC120 activity raises PICK1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 2.04× lower at baseline in the lines without CCDC120 | 0.024 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[AP1G2]] | B | AP1G2 activity raises PICK1's level | lines that do not express AP1G2 (8) vs lines expressing it (42) | 2.46× lower at baseline in the lines without AP1G2 | 0.031 | ⚠ within organs, on part of the lines; also absent: PRKCZ, LONRF3, CCDC120; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PICK1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.394). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.9, 22.8); signed map (-13.5, -14.9). **Vector** length 54.0, 7.29% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +2.7 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | +2.4 | -3.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.2 | +2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | +1.9 | -1.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +0.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +0.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.3 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.4 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.0 | -4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.7 | -9.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.6 | -4.9 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.6 | -1.7 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.6 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | protein interacting with PRKCA 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,056,311-38,075,701 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1039K5, MGC15204; previously PRKCABP |
| Gene groups (HGNC) | PDZ domain containing; AH domain containing |
| Hallmark sets | MYOGENESIS |
| Reactome | 8 pathways, smallest: Trafficking of GluR2-containing AMPA receptors; Glutamate binding, activation of AMPA receptors and synaptic plasticity; Trafficking of AMPA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRD5](https://www.uniprot.org/uniprotkb/Q9NRD5) (PRKCA-binding protein):

> Probable adapter protein that bind to and organize the subcellular localization of a variety of membrane proteins containing some PDZ recognition sequence. Involved in the clustering of various receptors, possibly by acting at the receptor internalization level. Plays a role in synaptic plasticity by regulating the trafficking and internalization of AMPA receptors. May be regulated upon PRKCA activation. May regulate ASIC1/ASIC3 channel. Regulates actin polymerization by inhibiting the …

**Summary**, from NCBI Gene [9463](https://www.ncbi.nlm.nih.gov/gene/9463):

> The protein encoded by this gene contains a PDZ domain, through which it interacts with protein kinase C, alpha (PRKCA). This protein may function as an adaptor that binds to and organizes the subcellular localization of a variety of membrane proteins. It has been shown to interact with multiple glutamate receptor subtypes, monoamine plasma membrane transporters, as well as non-voltage gated sodium channels, and may target PRKCA to these membrane proteins and thus regulate their distribution …

**Accessions** — [HGNC:9394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9394) · Entrez [9463](https://www.ncbi.nlm.nih.gov/gene/9463) · UniProt [Q9NRD5](https://www.uniprot.org/uniprotkb/Q9NRD5) · Ensembl [ENSG00000100151](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100151)

## Data

Gene col 1881: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1881); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1881, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1881]; `tensor/DDL_lfc|DDL_z.npy` [1881]; `embed/gene_vectors.npy` [1881]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1881 or target_col == 1881). Every well: [[PICK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PICK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
