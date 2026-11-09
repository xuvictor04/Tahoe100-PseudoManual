---
symbol: "SHARPIN"
type: "gene"
col: 11039
ensembl_id: "ENSG00000179526"
name: "SHANK associated RH domain interactor"
location: "8q24.3"
module: 30
arm: "+"
pooled_cpm: 19.71
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SHARPIN

*SHANK associated RH domain interactor* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.74× (z +7.1, q 8e-10, up in 31 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.32× (z +5.0, q 1e-04, up in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 4.19×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.551× (z -10.7, q 4e-24, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC45A]] (+0.70, fdr 7e-06), [[ZNHIT3]] (+0.68, fdr 7e-06), [[LCMT1]] (+0.67, fdr 7e-06); moves opposite to [[HNRNPA2B1]] (-0.60, fdr 1e-05), [[SERTAD4]] (-0.55, fdr 5e-05), [[ZFAT]] (-0.54, fdr 8e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[A1BG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11039.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 4.19×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.1 | 8e-10 | 31/39 (HEC-1-A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +6.3 | 1e-07 | 27/35 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.0 | 1e-04 | 20/31 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +5.0 | 1e-04 | 28/48 (RKO, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.3 | 0.002 | 24/43 (J82, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.551×** | -10.7 | 4e-24 | 39/47 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.509×** | -8.6 | 2e-15 | 41/48 (SW 900, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.580×** | -6.9 | 7e-10 | 43/47 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -6.0 | 3e-07 | 31/46 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.485×** | -4.8 | 2e-04 | 20/48 (LoVo, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.707×** | -4.4 | 1e-03 | 21/46 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -4.2 | 0.002 | 24/47 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.589×** | -3.5 | 0.030 | 20/43 (LOX-IMVI, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.739×** | -3.5 | 0.032 | 21/47 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -3.3 | 0.057 | 19/48 (HOP62, NCI-H661, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.773×** | -3.3 | 0.057 | 19/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 31.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.339× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.3) |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.7) |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.19× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 9.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -8.9) |
| [[PANC-1 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.2) |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -8.7) |
| [[A-172 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC45A]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZBTB49]] | +0.65 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[ZNF500]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[DPY30]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.63 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[RTCA]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PSMD9]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TBCB]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[TRIP4]] | +0.62 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RPP21]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA2B1]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[SERTAD4]] | -0.55 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ZFAT]] | -0.54 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[PTBP1]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[SLC12A2]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[THOC6]] | -0.53 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[A1BG]] | B | A1BG activity lowers SHARPIN's level | lines that do not express A1BG (17) vs lines expressing it (33) | 1.17× higher at baseline in the lines without A1BG | 0.093 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-14.6, -3.9); signed map (-34.8, -2.7). **Vector** length 64.8, 12.2% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.7 | +5.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +0.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -10.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | SHANK associated RH domain interactor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,098,633-144,108,124 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434N1923, SIPL1 |
| Gene groups (HGNC) | Zinc fingers RANBP2-type; Linear ubiquitin chain assembly complex |
| Reactome | 8 pathways, smallest: TNFR1-induced proapoptotic signaling; TNFR1-induced NF-kappa-B signaling pathway; Neurexins and neuroligins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0F6](https://www.uniprot.org/uniprotkb/Q9H0F6) (Sharpin):

> Non-catalytic component of the LUBAC complex which conjugates linear polyubiquitin chains in a head-to-tail manner to substrates and plays a key role in NF-kappa-B activation and regulation of inflammation. LUBAC conjugates linear polyubiquitin to IKBKG, RIPK1 and RIPK2 and is involved in activation of the canonical NF-kappa-B and the JNK signaling pathways. Linear ubiquitination mediated by the LUBAC complex interferes with TNF-induced cell death and thereby prevents inflammation. LUBAC is …

**Summary**, from NCBI Gene [81858](https://www.ncbi.nlm.nih.gov/gene/81858):

> Enables polyubiquitin modification-dependent protein binding activity. Involved in defense response to bacterium; protein linear polyubiquitination; and regulation of signal transduction. Located in cytosol. Part of LUBAC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25321) · Entrez [81858](https://www.ncbi.nlm.nih.gov/gene/81858) · UniProt [Q9H0F6](https://www.uniprot.org/uniprotkb/Q9H0F6) · Ensembl [ENSG00000179526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179526)

## Data

Gene col 11039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11039); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11039]; `tensor/DDL_lfc|DDL_z.npy` [11039]; `embed/gene_vectors.npy` [11039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11039 or target_col == 11039). Every well: [[SHARPIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHARPIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
