---
symbol: "TBC1D13"
type: "gene"
col: 2821
ensembl_id: "ENSG00000107021"
name: "TBC1 domain family member 13"
location: "9q34.11"
module: 209
arm: "+"
pooled_cpm: 9.21
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# TBC1D13

*TBC1 domain family member 13* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.74× (z +15.3, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.666× (z -6.2, q 3e-07, down in 20 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Isocorydine (drug)]] 0.5 µM in 1 line (COLO 205 0.0573×); [[Altretamine (drug)]] 0.05 µM in 1 line (COLO 205 0.0481×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.129×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HARS2]] (+0.69, fdr 7e-06), [[VPS33B]] (+0.69, fdr 7e-06), [[ESS2]] (+0.66, fdr 1e-05); moves opposite to [[TEX14]] (-0.62, fdr 1e-05), [[CLOCK]] (-0.60, fdr 6e-05), [[DGKH]] (-0.58, fdr 2e-05).
> It is in [[Module 209]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.74×** | +15.3 | 0e+00 | 44/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.65×** | +14.4 | 2e-44 | 45/47 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +11.4 | 7e-28 | 44/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +6.6 | 7e-09 | 25/48 (RKO, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.8 | 2e-04 | 13/47 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.4 | 9e-04 | 14/38 (C32, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +4.3 | 0.001 | 13/44 (A498, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 0.002 | 10/47 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.012 | 11/47 (RKO, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.091 | 4/47 (LoVo, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2821.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Isocorydine (drug)]] 0.5 µM in 1 line (COLO 205 0.0573×); [[Altretamine (drug)]] 0.05 µM in 1 line (COLO 205 0.0481×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.129×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.666×** | -6.2 | 3e-07 | 20/46 (HCT15, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.759×** | -4.2 | 0.007 | 14/47 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.771×** | -3.8 | 0.026 | 11/46 (COLO 205, PANC-1, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.801× | -3.3 | 0.16 | 12/45 (RKO, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 2 | — | [[Isocorydine (drug)]] 0.5 µM 0.0573× (z -11.8) |
| [[RKO (line)]] | wt | 17.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.42× (z +8.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -9.2) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SW480 (line)]] | alt | 9.78 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.71× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.5 µM 0.0506× (z -8.6) |
| [[C-33 A (line)]] | alt | 7.96 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0735× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 7.16 | 0 | 1 | — | [[Altretamine (drug)]] 5 µM 0.0486× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.129× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 9.34 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 9.03 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.101× (z -9.1) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0727× (z -9.0) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HARS2]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[VPS33B]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ESS2]] | +0.66 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[USP30]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[PXMP4]] | +0.64 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[COMMD9]] | +0.63 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[STEEP1]] | +0.63 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[CNEP1R1]] | +0.62 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TERF1]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[FBXO3]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX14]] | -0.62 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CLOCK]] | -0.60 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[DGKH]] | -0.58 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[INTS6]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[IDI2-AS1]] | -0.57 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[TRIM72]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[LINC00910]] | -0.56 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CYCS]] | -0.55 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[LINC01934]] | -0.54 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[FAM151B]] | -0.54 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[BAZ1A]] | -0.54 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[MPDU1]] | -0.54 | -0.49 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TBC1D13's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.9, -11.2); signed map (-31.6, -11.3). **Vector** length 63.5, 9.32% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.7 | +14.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +15.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.3 | +6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +11.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.0 | -6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.4 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.1 | -3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,787,253-128,810,430 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10743 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVG8](https://www.uniprot.org/uniprotkb/Q9NVG8) (TBC1 domain family member 13):

> Acts as a GTPase-activating protein for RAB35. Together with RAB35 may be involved in regulation of insulin-induced glucose transporter SLC2A4/GLUT4 translocation to the plasma membrane in adipocytes.

**Summary**, from NCBI Gene [54662](https://www.ncbi.nlm.nih.gov/gene/54662):

> Predicted to enable GTPase activator activity. Predicted to be involved in intracellular protein transport. Predicted to be located in cytosol and membrane. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25571](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25571) · Entrez [54662](https://www.ncbi.nlm.nih.gov/gene/54662) · UniProt [Q9NVG8](https://www.uniprot.org/uniprotkb/Q9NVG8) · Ensembl [ENSG00000107021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107021)

## Data

Gene col 2821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2821); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2821]; `tensor/DDL_lfc|DDL_z.npy` [2821]; `embed/gene_vectors.npy` [2821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2821 or target_col == 2821). Every well: [[TBC1D13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
