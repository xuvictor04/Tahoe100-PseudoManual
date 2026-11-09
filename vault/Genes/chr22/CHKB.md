---
symbol: "CHKB"
type: "gene"
col: 1912
ensembl_id: "ENSG00000100288"
name: "choline kinase beta"
location: "22q13.33"
module: 20
arm: "-"
pooled_cpm: 16.44
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CHKB

*choline kinase beta* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.51× (z +4.2, q 0.015, up in 18 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.515× (z -9.4, q 2e-18, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPT1B]] (+0.76, fdr 7e-06, ⚠ same locus), [[TERF2IP]] (+0.68, fdr 1e-05), [[RBX1]] (+0.65, fdr 1e-05), [[RBM5]] (+0.64, fdr 1e-05); moves opposite to [[CORO1C]] (-0.66, fdr 1e-05), [[TMED7]] (-0.63, fdr 2e-05), [[PAICS]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CPT1B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 0.015 | 18/45 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.062 | 16/46 (LOX-IMVI, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.062 | 10/45 (NCI-H2030, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.062 | 6/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.5 | 0.062 | 14/42 (NCI-H2030, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.13 | 13/44 (SNU-423, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.515×** | -9.4 | 2e-18 | 37/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.565×** | -8.1 | 1e-13 | 36/47 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.578×** | -7.8 | 1e-12 | 31/47 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -6.5 | 1e-08 | 30/48 (A549, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.655×** | -5.7 | 2e-06 | 25/48 (A498, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -5.6 | 3e-06 | 28/47 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.482×** | -5.4 | 5e-06 | 23/44 (NCI-H1573, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.703×** | -5.0 | 4e-05 | 21/47 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.730×** | -4.5 | 5e-04 | 20/47 (LOX-IMVI, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -4.1 | 0.002 | 20/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.029 | 19/47 (SNU-423, HS-578T, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.633×** | -3.4 | 0.032 | 14/45 (NCI-H460, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.641×** | -3.3 | 0.041 | 12/48 (A549, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.648×** | -3.2 | 0.051 | 12/36 (LOX-IMVI, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 0.05 µM |  | **0.783×** | -3.2 | 0.051 | 9/47 (NCI-H2030, KATO III, …) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.789×** | -3.1 | 0.067 | 9/47 (KATO III, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 14.4 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.302× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 20.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0982× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 28.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0861× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1B]] | +0.76 | +0.75 / +0.72 | both halves | 7e-06 | STRING 960; ⚠ same locus (0.5 kb, same strand: neighbours can correlate without regulation) |
| [[TERF2IP]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[RBX1]] | +0.65 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[RBM5]] | +0.64 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[RFX1]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[WBP4]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[DYRK1B]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[RRAGC]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ZCCHC3]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[UNK]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LRCH3]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[EIF1B]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO1C]] | -0.66 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[TMED7]] | -0.63 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[PAICS]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[GLO1]] | -0.60 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PSMD2]] | -0.60 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[PRELID3B]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[CCT2]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[API5]] | -0.59 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[HSPD1]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[CCT3]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[PHB1]] | -0.59 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[TCP1]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPT1B]] | C | CPT1B activity raises CHKB's level | lines that do not express CPT1B (3) vs lines expressing it (47) | 1.73× lower at baseline in the lines without CPT1B | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLEC2D, FRRS1, ENSG00000266385; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.2, -31.2); signed map (-5.7, 4.3). **Vector** length 73.1, 13.2% of its response variance represented; |z| ≥ 3 in 731 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.6 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.6 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.6 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.5 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.3 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | choline kinase beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,578,959-50,601,455 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHETK; previously CHKL |
| Gene groups (HGNC) | Choline kinase family |
| Reactome | 5 pathways, smallest: Synthesis of PE; Synthesis of PC; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y259](https://www.uniprot.org/uniprotkb/Q9Y259) (Choline/ethanolamine kinase):

> Has a key role in phospholipid metabolism, and catalyzes the first step of phosphatidylethanolamine and phosphatidylcholine biosynthesis.

**Summary**, from NCBI Gene [1120](https://www.ncbi.nlm.nih.gov/gene/1120):

> Choline kinase (CK) and ethanolamine kinase (EK) catalyze the phosphorylation of choline/ethanolamine to phosphocholine/phosphoethanolamine. This is the first enzyme in the biosynthesis of phosphatidylcholine/phosphatidylethanolamine in all animal cells. The highly purified CKs from mammalian sources and their recombinant gene products have been shown to have EK activity also, indicating that both activities reside on the same protein. The choline kinase-like protein encoded by CHKL belongs to …

**Accessions** — [HGNC:1938](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1938) · Entrez [1120](https://www.ncbi.nlm.nih.gov/gene/1120) · UniProt [Q9Y259](https://www.uniprot.org/uniprotkb/Q9Y259) · Ensembl [ENSG00000100288](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100288)

## Data

Gene col 1912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1912); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1912]; `tensor/DDL_lfc|DDL_z.npy` [1912]; `embed/gene_vectors.npy` [1912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1912 or target_col == 1912). Every well: [[CHKB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHKB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
