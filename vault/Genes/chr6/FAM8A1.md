---
symbol: "FAM8A1"
type: "gene"
col: 6012
ensembl_id: "ENSG00000137414"
name: "family with sequence similarity 8 member A1"
location: "6p22.3"
module: 5
arm: "-"
pooled_cpm: 20.6
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# FAM8A1

*family with sequence similarity 8 member A1* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 1.31× (z +6.3, q 1e-07, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.668× (z -6.7, q 1e-08, down in 27 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.712× (z -5.4, q 2e-05, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP11]] (+0.65, fdr 7e-06), [[PJA2]] (+0.63, fdr 7e-06), [[LAPTM4A]] (+0.59, fdr 1e-05); moves opposite to [[MTHFD1L]] (-0.60, fdr 2e-05), [[NPIPB5]] (-0.57, fdr 1e-05), [[MRTO4]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6012.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +6.3 | 1e-07 | 26/48 (J82, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +5.4 | 2e-05 | 20/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +5.2 | 4e-05 | 24/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 8e-04 | 20/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +3.9 | 0.009 | 17/48 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.012 | 11/48 (J82, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.026 | 16/47 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~4% of this change | 1.22× | +3.1 | 0.13 | 18/45 (SW1417, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6012.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.668×** | -6.7 | 1e-08 | 27/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.712×** | -5.4 | 2e-05 | 25/47 (LoVo, J82, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.615×** | -4.2 | 0.005 | 16/47 (RPMI-7951, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.642×** | -3.8 | 0.018 | 14/47 (AsPC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.661×** | -3.6 | 0.033 | 14/47 (Panc 03.27, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.806×** | -3.6 | 0.033 | 15/48 (J82, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bergenin (drug)]] 0.5 µM |  | **0.810×** | -3.5 | 0.039 | 17/47 (SW 1271, C-33 A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.802×** | -3.5 | 0.039 | 13/47 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.797×** | -3.2 | 0.084 | 10/47 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | 0.700× | -3.1 | 0.11 | 8/47 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.834× | -3.0 | 0.13 | 12/47 (LS 180, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6012. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[LS 180 (line)]] | wt | 25.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[CHP-212 (line)]] | wt | 35.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.109× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 18.5 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.209× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[PANC-1 (line)]] | alt | 15.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +8.5) | — |
| [[RKO (line)]] | wt | 9.99 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0859× (z -11.0) |
| [[SW480 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6012), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP11]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[PJA2]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[LAPTM4A]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TMEM30A]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RBL2]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MBIP]] | +0.56 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[COPS4]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[TM9SF2]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[MAGED2]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[MED30]] | +0.53 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[BAG4]] | +0.53 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[RAB14]] | +0.52 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTHFD1L]] | -0.60 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[NPIPB5]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[MRTO4]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[SDAD1]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[NOP56]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[NPIPB12]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CCDC137]] | -0.53 | -0.49 / -0.52 | both halves | 2e-05 |  |
| [[DDX21]] | -0.53 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[DNAJC11]] | -0.52 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.52 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[NPIPB4]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers FAM8A1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (1.9, -31.2); signed map (-52.4, -5.6). **Vector** length 90.9, 18.8% of its response variance represented; |z| ≥ 3 in 832 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.3 | +6.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.9 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 8 member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:17,600,302-17,611,719 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AHCP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBU6](https://www.uniprot.org/uniprotkb/Q9UBU6) (Protein FAM8A1):

> Plays a role in the assembly of the HRD1 complex, a complex involved in the ubiquitin-proteasome-dependent process of ER-associated degradation (ERAD).

**Summary**, from NCBI Gene [51439](https://www.ncbi.nlm.nih.gov/gene/51439):

> Predicted to be involved in ERAD pathway. Part of Hrd1p ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16372](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16372) · Entrez [51439](https://www.ncbi.nlm.nih.gov/gene/51439) · UniProt [Q9UBU6](https://www.uniprot.org/uniprotkb/Q9UBU6) · Ensembl [ENSG00000137414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137414)

## Data

Gene col 6012: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6012); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6012, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6012]; `tensor/DDL_lfc|DDL_z.npy` [6012]; `embed/gene_vectors.npy` [6012]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6012 or target_col == 6012). Every well: [[FAM8A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM8A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
