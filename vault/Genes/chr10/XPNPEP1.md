---
symbol: "XPNPEP1"
type: "gene"
col: 2912
ensembl_id: "ENSG00000108039"
name: "X-prolyl aminopeptidase 1"
location: "10q25.1"
module: 164
arm: "+"
pooled_cpm: 61.34
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# XPNPEP1

*X-prolyl aminopeptidase 1* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 1.69× (z +4.6, q 0.001, up in 23 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.747× (z -7.8, q 3e-12, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR45B]] (+0.71, fdr 7e-06), [[UBE2O]] (+0.66, fdr 1e-05), [[YEATS2]] (+0.65, fdr 1e-05); moves opposite to [[AVEN]] (-0.56, fdr 1e-05), [[DNAJB12]] (-0.54, fdr 3e-05), [[ARMCX4]] (-0.53, fdr 4e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM13A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.6 | 0.001 | 23/49 (NCI-H1573, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.6 | 0.001 | 18/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.1 | 0.007 | 21/48 (CFPAC-1, SW480, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.24 | 12/48 (SW480, HCT15, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.21× | +3.1 | 0.24 | 13/48 (CFPAC-1, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.747×** | -7.8 | 3e-12 | 28/48 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -6.4 | 4e-08 | 28/48 (C32, HS-578T, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.799×** | -5.9 | 6e-07 | 24/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.828×** | -4.9 | 1e-04 | 24/48 (SK-MEL-2, LoVo, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.775×** | -4.9 | 1e-04 | 24/48 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.796×** | -4.4 | 0.001 | 26/47 (SW1417, J82, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.808×** | -4.2 | 0.002 | 20/48 (A498, SW48, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.830×** | -3.7 | 0.015 | 18/48 (C32, HCT15, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.840× | -3.3 | 0.054 | 17/48 (C32, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | 0.845× | -3.2 | 0.073 | 22/47 (C32, HCT15, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.860× | -3.0 | 0.14 | 18/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 113 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -22.9) |
| [[AN3 CA (line)]] | alt | 117 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 67.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.269× (z -18.2) |
| [[HCT15 (line)]] | alt | 95.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0581× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.400× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 65.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.455× (z -9.6) |
| [[HT-29 (line)]] | alt | 94.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.456× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1792 (line)]] | alt | 83.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 58.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -10.2) |
| [[RKO (line)]] | wt | 64.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.246× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SW48 (line)]] | wt | 59.0 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.244× (z -9.3) |
| [[A-172 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 72.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 88.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR45B]] | +0.71 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[YEATS2]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TRMU]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PDXP]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.61 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[MMS19]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[PEX3]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[FBXO42]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PDK3]] | +0.59 | +0.62 / +0.49 | both halves | 2e-05 | pathway: HALLMARK_HYPOXIA |
| [[HERC3]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[DNAJB12]] | -0.54 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[ARMCX4]] | -0.53 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[EPC2]] | -0.52 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[UTP20]] | -0.50 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[NEK11]] | -0.50 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[SUCLA2]] | -0.50 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[TTC27]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ERMAP]] | -0.49 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[INO80]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[PARVA]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[C1RL-AS1]] | -0.48 | -0.43 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM13A]] | B | FAM13A activity raises XPNPEP1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without FAM13A | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[NDRG1]] | B | NDRG1 activity raises XPNPEP1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without NDRG1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.4, -16.5); signed map (-37.2, 24.1). **Vector** length 106, 28.1% of its response variance represented; |z| ≥ 3 in 645 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +4.8 | +3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.4 | +0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +0.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.1 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.0 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.0 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -4.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | -3.2 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | X-prolyl aminopeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:109,864,766-109,923,553 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously XPNPEP, XPNPEPL1, XPNPEPL |
| Gene groups (HGNC) | Aminopeptidases; M24 metallopeptidase family |
| Hallmark sets | COMPLEMENT, HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQW7](https://www.uniprot.org/uniprotkb/Q9NQW7) (Xaa-Pro aminopeptidase 1):

> Metalloaminopeptidase that catalyzes the removal of a penultimate prolyl residue from the N-termini of peptides, such as Arg-Pro-Pro. Contributes to the degradation of bradykinin.

**Summary**, from NCBI Gene [7511](https://www.ncbi.nlm.nih.gov/gene/7511):

> This gene encodes the cytosolic form of a metalloaminopeptidase that catalyzes the cleavage of the N-terminal amino acid adjacent to a proline residue. The gene product may play a role in degradation and maturation of tachykinins, neuropeptides, and peptide hormones. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:12822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12822) · Entrez [7511](https://www.ncbi.nlm.nih.gov/gene/7511) · UniProt [Q9NQW7](https://www.uniprot.org/uniprotkb/Q9NQW7) · Ensembl [ENSG00000108039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108039)

## Data

Gene col 2912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2912); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2912]; `tensor/DDL_lfc|DDL_z.npy` [2912]; `embed/gene_vectors.npy` [2912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2912 or target_col == 2912). Every well: [[XPNPEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XPNPEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
