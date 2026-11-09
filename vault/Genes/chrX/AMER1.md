---
symbol: "AMER1"
type: "gene"
col: 11565
ensembl_id: "ENSG00000184675"
name: "APC membrane recruitment protein 1"
location: "Xq11.2"
module: 5
arm: "+"
pooled_cpm: 4.22
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# AMER1

*APC membrane recruitment protein 1* — Xq11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.46× (z +5.0, q 3e-04, up in 15 of 46 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.29× (z +3.4, q 0.064, up in 7 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.630× (z -6.2, q 2e-07, down in 23 of 40 measured lines) ⚠ cell-cycle shift, explains ~67% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.655× (z -4.0, q 0.015, down in 15 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD40]] (+0.63, fdr 1e-05), [[OTUD4]] (+0.61, fdr 1e-05), [[MRM1]] (+0.61, fdr 2e-05); moves opposite to [[CCNI]] (-0.63, fdr 1e-05), [[ASL]] (-0.58, fdr 7e-05), [[UBE2B]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF618]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.46×** | +5.0 | 3e-04 | 15/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +4.8 | 4e-04 | 1/11 (SW1417) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.5 | 0.001 | 6/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +3.6 | 0.047 | 14/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.064 | 7/36 (CFPAC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.4 | 0.064 | 1/5 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.41×** | +3.2 | 0.099 | 7/43 (A-427, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.38× | +3.1 | 0.15 | 1/47 (SW48) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.630×** | -6.2 | 2e-07 | 23/40 (NCI-H23, NCI-H460, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.655×** | -4.0 | 0.015 | 15/44 (Panc 03.27, MIA PaCa-2, …) | two highest doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.672×** | -3.8 | 0.028 | 11/46 (CFPAC-1, CHP-212, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.680×** | -3.7 | 0.031 | 13/33 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.692×** | -3.5 | 0.047 | 17/44 (SK-MEL-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.689×** | -3.4 | 0.057 | 9/42 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.702×** | -3.4 | 0.057 | 16/47 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.800× | -3.0 | 0.17 | 10/45 (H4, C-33 A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.96 | 0 | 2 (1 ⚠) | — | [[Thymol (drug)]] 0.5 µM 0.103× (z -9.7) |
| [[PANC-1 (line)]] | alt | 3.30 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0980× (z -9.5) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-172 (line)]] | wt | 5.55 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.116× (z -8.6) ⚠ toxic; unreliable plate only |
| [[HOP62 (line)]] | alt | 2.79 | 0 | 1 | — | [[Capmatinib (drug)]] 0.05 µM 0.0579× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 6.33 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -9.9) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H460 (line)]] | wt | 7.22 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[Panc 03.27 (line)]] | alt | 5.74 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0498× (z -11.0) |
| [[RKO (line)]] | wt | 4.64 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0489× (z -9.2) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A-427 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD40]] | +0.63 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[OTUD4]] | +0.61 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[MRM1]] | +0.61 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[RCN1]] | +0.61 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[POMK]] | +0.60 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[MTA2]] | +0.60 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[HENMT1]] | +0.60 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[ZNF239]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[EME2]] | +0.59 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ZNF514]] | +0.59 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[ABCF2]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[TOR1A]] | +0.59 | +0.56 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNI]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ASL]] | -0.58 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[UBE2B]] | -0.57 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NBEAL1]] | -0.56 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[DDT]] | -0.55 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[NOSIP]] | -0.55 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[MFSD11]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[SELENOW]] | -0.52 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[CDKN2D]] | -0.52 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LGALS1]] | -0.52 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[INAFM1]] | -0.52 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[POLR2J4]] | -0.52 | -0.49 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF618]] | B | ZNF618 activity raises AMER1's level | lines that do not express ZNF618 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without ZNF618 | 0.074 | ⚠ within organs, on part of the lines; also absent: NCS1, MRAS, GPR63 |
| [[LINC01139]] | B | LINC01139 activity raises AMER1's level | lines that do not express LINC01139 (24) vs lines expressing it (26) | 1.23× lower at baseline in the lines without LINC01139 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000260289, NTRK3, CTNNA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.9, -27.5); signed map (29.0, -31.0). **Vector** length 57.7, 7.49% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.9 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +3.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +4.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +2.0 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.3 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -3.2 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -2.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | APC membrane recruitment protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq11.2 — chrX:64,185,117-64,205,708 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-403E24.2, FLJ39827, WTX; previously FAM123B |
| Gene groups (HGNC) | APC membrane recruitment proteins |
| Reactome | 24 pathways, smallest: APC truncation mutants have impaired AXIN binding; AXIN missense mutants destabilize the destruction complex; Signaling by AMER1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JTC6](https://www.uniprot.org/uniprotkb/Q5JTC6) (APC membrane recruitment protein 1):

> Regulator of the canonical Wnt signaling pathway. Acts by specifically binding phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2), translocating to the cell membrane and interacting with key regulators of the canonical Wnt signaling pathway, such as components of the beta-catenin destruction complex. Acts both as a positive and negative regulator of the Wnt signaling pathway, depending on the context: acts as a positive regulator by promoting LRP6 phosphorylation. Also acts as a negative …

**Summary**, from NCBI Gene [139285](https://www.ncbi.nlm.nih.gov/gene/139285):

> The protein encoded by this gene upregulates trancriptional activation by the Wilms tumor protein and interacts with many other proteins, including CTNNB1, APC, AXIN1, and AXIN2. Defects in this gene are a cause of osteopathia striata with cranial sclerosis (OSCS). [provided by RefSeq, May 2010]

**Accessions** — [HGNC:26837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26837) · Entrez [139285](https://www.ncbi.nlm.nih.gov/gene/139285) · UniProt [Q5JTC6](https://www.uniprot.org/uniprotkb/Q5JTC6) · Ensembl [ENSG00000184675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184675)

## Data

Gene col 11565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11565); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11565]; `tensor/DDL_lfc|DDL_z.npy` [11565]; `embed/gene_vectors.npy` [11565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11565 or target_col == 11565). Every well: [[AMER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
