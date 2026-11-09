---
symbol: "TRIM52"
type: "gene"
col: 11441
ensembl_id: "ENSG00000183718"
name: "tripartite motif containing 52"
location: "5q35.3"
module: 42
arm: "+"
pooled_cpm: 25.48
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TRIM52

*tripartite motif containing 52* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.98× (z +13.1, q 2e-36, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.778× (z -4.9, q 6e-04, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OS9]] (+0.60, fdr 1e-05), [[GANAB]] (+0.53, fdr 2e-05), [[MBD1]] (+0.53, fdr 3e-05); moves opposite to [[TTC39C]] (-0.51, fdr 7e-05), [[YDJC]] (-0.46, fdr 7e-05), [[SCMH1]] (-0.46, fdr 2e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +13.1 | 2e-36 | 41/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +11.6 | 2e-28 | 40/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +10.8 | 7e-25 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.1 | 7e-14 | 31/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +6.8 | 2e-09 | 4/48 (MIA PaCa-2, SHP-77, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +6.6 | 4e-09 | 27/48 (HS-578T, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.1 | 2e-05 | 20/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +5.1 | 2e-05 | 23/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 1.16× | +4.0 | 0.004 | 14/48 (CFPAC-1, SW1417, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.20× | +3.4 | 0.038 | 12/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.050 | 11/47 (HepG2/C3A, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.778×** | -4.9 | 6e-04 | 22/48 (H4, HS-578T, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.801×** | -4.3 | 0.005 | 14/47 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **0.799×** | -3.6 | 0.056 | 17/46 (HepG2/C3A, A549, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.825×** | -3.5 | 0.058 | 8/47 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.810×** | -3.4 | 0.080 | 20/47 (NCI-H23, PANC-1, …) | two highest doses | composition shift; noisy plate (z scaled) |
| [[Resveratrol (drug)]] 5 µM |  | 0.890× | -3.2 | 0.12 | 6/48 (COLO 205, SHP-77, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.855× | -3.1 | 0.18 | 6/48 (KATO III, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +10.4) | — |
| [[A549 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.115× (z -8.8) |
| [[Hs 766T (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 41.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 15.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +8.6) | — |
| [[RKO (line)]] | wt | 23.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.86× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 53.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OS9]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[GANAB]] | +0.53 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[MBD1]] | +0.53 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[AMPD2]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[SEC24C]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[NLGN2]] | +0.51 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[CDK5RAP3]] | +0.51 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[RCN3]] | +0.51 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[SH3D21]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[SERTAD3]] | +0.49 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[SUPT5H]] | +0.48 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[ZNF17]] | +0.47 | +0.41 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC39C]] | -0.51 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[YDJC]] | -0.46 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[SCMH1]] | -0.46 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[RPP40]] | -0.46 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[CDIN1]] | -0.45 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[PCNX1]] | -0.45 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[SLC25A13]] | -0.44 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[GCFC2]] | -0.44 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[CFAP97]] | -0.42 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[TRIM47]] | -0.42 | -0.32 / -0.35 | both halves | 2e-04 | same gene group |
| [[CLASP2]] | -0.42 | -0.24 / -0.40 | both halves | 4e-04 |  |
| [[MACIR]] | -0.42 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TRIM52's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.5, -27.7); signed map (-52.5, 2.0). **Vector** length 70.3, 11.7% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.5 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.2 | +1.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.0 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +1.7 | +4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Oxaliplatin (drug)]] 0.05 µM |  | +1.3 | +0.4 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +0.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.2 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.9 | -3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | -2.7 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.4 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 52 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:181,254,077-181,261,150 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF102 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A61](https://www.uniprot.org/uniprotkb/Q96A61) (E3 ubiquitin-protein ligase TRIM52):

> E3 ubiquitin-protein ligase. Positively regulates the NF-kappa-B signaling pathway.; (Microbial infection) Exhibits antiviral activity against Japanese encephalitis virus (JEV). Ubiquitinates the viral non-structural protein 2 (NS2A) and targets it for proteasome-mediated degradation.

**Summary**, from NCBI Gene [84851](https://www.ncbi.nlm.nih.gov/gene/84851):

> Enables transcription coactivator activity and ubiquitin protein ligase activity. Involved in defense response to virus; positive regulation of canonical NF-kappaB signal transduction; and protein autoubiquitination. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19024) · Entrez [84851](https://www.ncbi.nlm.nih.gov/gene/84851) · UniProt [Q96A61](https://www.uniprot.org/uniprotkb/Q96A61) · Ensembl [ENSG00000183718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183718)

## Data

Gene col 11441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11441); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11441]; `tensor/DDL_lfc|DDL_z.npy` [11441]; `embed/gene_vectors.npy` [11441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11441 or target_col == 11441). Every well: [[TRIM52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
