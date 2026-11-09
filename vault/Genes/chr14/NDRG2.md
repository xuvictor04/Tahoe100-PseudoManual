---
symbol: "NDRG2"
type: "gene"
col: 9185
ensembl_id: "ENSG00000165795"
name: "NDRG family member 2"
location: "14q11.2"
module: 14
arm: "+"
pooled_cpm: 2.76
n_lines_expressing: 48
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NDRG2

*NDRG family member 2* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +12.4, q 2e-32, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.442× (z -7.4, q 1e-10, down in 23 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF219]] (+0.66, fdr 7e-06, ⚠ same locus), [[RARG]] (+0.65, fdr 1e-05), [[MAP3K2-DT]] (+0.64, fdr 7e-06), [[CA11]] (+0.61, fdr 2e-05); moves opposite to [[EEFSEC]] (-0.52, fdr 8e-05), [[CA5B]] (-0.51, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IL17RE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +12.4 | 2e-32 | 21/32 (C32, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +12.1 | 3e-31 | 21/33 (A-172, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +10.2 | 3e-22 | 2/2 (A498, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +9.8 | 1e-20 | 6/11 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +7.4 | 2e-11 | 1/2 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +7.0 | 2e-10 | 22/42 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +5.4 | 6e-06 | 19/36 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +4.7 | 2e-04 | 10/41 (A-427, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.72×** | +4.7 | 2e-04 | 11/37 (NCI-H2030, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +4.4 | 5e-04 | 11/33 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 5/44 (A-172, SW1417, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +4.1 | 0.002 | 6/37 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 6/42 (SNU-423, SW480, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.84×** | +3.9 | 0.003 | 6/24 (BT-474, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.008 | 9/42 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.009 | 6/44 (A-427, AsPC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.024 | 6/43 (SW480, NCI-H2030, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.024 | 7/45 (AsPC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9185.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.442×** | -7.4 | 1e-10 | 23/39 (SW1417, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.510×** | -6.1 | 4e-07 | 21/45 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.627×** | -4.2 | 0.005 | 16/37 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.657×** | -3.8 | 0.021 | 12/44 (NCI-H2030, COLO 205, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.691×** | -3.3 | 0.094 | 7/45 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 7.80 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.0906× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 2.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.0× (z +12.8) | — |
| [[LoVo (line)]] | wt | 4.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 2.78 | 0 | 1 | — | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.0459× (z -9.0) |
| [[A-172 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.741 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.717 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF219]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 | ⚠ same locus (19.2 kb, same strand: neighbours can correlate without regulation) |
| [[RARG]] | +0.65 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[MAP3K2-DT]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CA11]] | +0.61 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[IST1]] | +0.61 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[ZFTA]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[PLXNC1]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CES3]] | +0.59 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[BDH2]] | +0.59 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[COL16A1]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LINC01122]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.58 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[CX3CL1]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.52 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[CA5B]] | -0.51 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL17RE]] | B | IL17RE activity raises NDRG2's level | lines that do not express IL17RE (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without IL17RE | 0.035 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises NDRG2's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without SLC44A3 | 0.085 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers NDRG2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.0, 7.1); signed map (40.8, -1.1). **Vector** length 55.4, 8.42% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NDRG family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:21,016,763-21,070,872 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1248, SYLD |
| Gene groups (HGNC) | MicroRNA protein coding host genes; NDRG family |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UN36](https://www.uniprot.org/uniprotkb/Q9UN36) (Protein NDRG2):

> Contributes to the regulation of the Wnt signaling pathway. Down-regulates CTNNB1-mediated transcriptional activation of target genes, such as CCND1, and may thereby act as tumor suppressor. May be involved in dendritic cell and neuron differentiation.

**Summary**, from NCBI Gene [57447](https://www.ncbi.nlm.nih.gov/gene/57447):

> This gene is a member of the N-myc downregulated gene family which belongs to the alpha/beta hydrolase superfamily. The protein encoded by this gene is a cytoplasmic protein that may play a role in neurite outgrowth. This gene may be involved in glioblastoma carcinogenesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:14460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14460) · Entrez [57447](https://www.ncbi.nlm.nih.gov/gene/57447) · UniProt [Q9UN36](https://www.uniprot.org/uniprotkb/Q9UN36) · Ensembl [ENSG00000165795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165795)

## Data

Gene col 9185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9185); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9185]; `tensor/DDL_lfc|DDL_z.npy` [9185]; `embed/gene_vectors.npy` [9185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9185 or target_col == 9185). Every well: [[NDRG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDRG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
