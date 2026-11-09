---
symbol: "CENPBD1P"
type: "gene"
col: 10879
ensembl_id: "ENSG00000177946"
name: "CENPB DNA-binding domain containing 1, pseudogene"
location: "16q24.3"
module: 7
arm: "+"
pooled_cpm: 3.37
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CENPBD1P

*CENPB DNA-binding domain containing 1, pseudogene* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.11× (z +7.3, q 2e-10, up in 19 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.378× (z -9.5, q 2e-18, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF268]] (+0.81, fdr 7e-06), [[ZNF747]] (+0.76, fdr 7e-06), [[RTL6]] (+0.76, fdr 7e-06); moves opposite to [[SRP54-AS1]] (-0.69, fdr 7e-06), [[CBFA2T2]] (-0.67, fdr 1e-05), [[GMCL1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TTC30A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +7.3 | 2e-10 | 19/34 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +6.4 | 6e-08 | 11/46 (NCI-H1573, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +5.9 | 8e-07 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +5.4 | 8e-06 | 18/42 (SHP-77, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +5.0 | 5e-05 | 14/35 (NCI-H2030, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +4.8 | 1e-04 | 2/8 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.8 | 1e-04 | 8/47 (SK-MEL-2, SNU-423, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +4.4 | 7e-04 | 12/46 (NCI-H1573, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.1 | 0.002 | 8/45 (NCI-H1573, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +4.1 | 0.003 | 10/43 (NCI-H1792, NCI-H2030, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.032 | 6/44 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.4 | 0.033 | 4/17 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.3 | 0.048 | 6/21 (J82, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.37× | +3.0 | 0.10 | 1/45 (MIA PaCa-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.378×** | -9.5 | 2e-18 | 24/42 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.430×** | -8.2 | 5e-14 | 29/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -6.1 | 2e-07 | 18/29 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.549×** | -5.8 | 7e-07 | 20/42 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.641×** | -4.3 | 0.002 | 17/41 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.663×** | -4.0 | 0.006 | 13/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.673×** | -3.9 | 0.009 | 8/46 (BT-474, SW48, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -3.5 | 0.031 | 10/36 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.720×** | -3.2 | 0.082 | 11/44 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.65 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 6.85 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +20.2) | — |
| [[A-427 (line)]] | wt | 8.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0541× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 1.93 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 5 µM 0.0418× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 5.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 4.86 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0704× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 4.02 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0679× (z -8.9) |
| [[SHP-77 (line)]] | alt | 8.48 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.83× (z +8.7) | — |
| [[SW480 (line)]] | alt | 2.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0883× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF268]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[ZNF747]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[RTL6]] | +0.76 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[ZNF518B]] | +0.76 | +0.81 / +0.65 | both halves | 7e-06 |  |
| [[MOCS3]] | +0.75 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.75 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[C7orf25]] | +0.74 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ZBED9]] | +0.74 | +0.81 / +0.55 | both halves | 1e-05 |  |
| [[ZSCAN29]] | +0.73 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[ZNF614]] | +0.73 | +0.72 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54-AS1]] | -0.69 | -0.72 / -0.62 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.67 | -0.74 / -0.52 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.65 | -0.71 / -0.49 | both halves | 1e-05 |  |
| [[GNRH1]] | -0.64 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[PIK3C2A]] | -0.63 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[UQCRH]] | -0.63 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[KYAT1]] | -0.62 | -0.64 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC30A]] | B | TTC30A activity raises CENPBD1P's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without TTC30A | 0.089 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.824). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-33.3, 12.2); signed map (1.8, -29.7). **Vector** length 59.2, 8.31% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | CENPB DNA-binding domain containing 1, pseudogene |
| Locus type | pseudogene |
| Location | 16q24.3 — chr16:89,969,983-89,971,922 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | MGC16385; previously CENPBD1 |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family; Unitary pseudogenes |
| Matched by | ensembl_id |

UniProt [B2RD01](https://www.uniprot.org/uniprotkb/B2RD01) carries no function annotation.

**Summary**, from NCBI Gene [92806](https://www.ncbi.nlm.nih.gov/gene/92806):

> Predicted to enable DNA binding activity. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28272) · Entrez [92806](https://www.ncbi.nlm.nih.gov/gene/92806) · UniProt [B2RD01](https://www.uniprot.org/uniprotkb/B2RD01) · Ensembl [ENSG00000177946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177946)

## Data

Gene col 10879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10879); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10879]; `tensor/DDL_lfc|DDL_z.npy` [10879]; `embed/gene_vectors.npy` [10879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10879 or target_col == 10879). Every well: [[CENPBD1P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPBD1P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
