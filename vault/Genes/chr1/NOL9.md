---
symbol: "NOL9"
type: "gene"
col: 8511
ensembl_id: "ENSG00000162408"
name: "nucleolar protein 9"
location: "1p36.31"
module: 5
arm: "+"
pooled_cpm: 32.79
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NOL9

*nucleolar protein 9* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +11.8, q 2e-29, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Osimertinib (mesylate) (drug)]] 5 µM: 0.824× (z -4.0, q 0.027, down in 11 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.446×); [[Fluvoxamine (drug)]] 5 µM in 1 line (AN3 CA 0.148×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRTO4]] (+0.77, fdr 7e-06), [[POLR1A]] (+0.75, fdr 7e-06), [[LTV1]] (+0.73, fdr 7e-06); moves opposite to [[MPC2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CSRP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +11.8 | 2e-29 | 31/48 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +9.8 | 3e-20 | 37/48 (PANC-1, NCI-H460, …) | all doses, flat | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.59×** | +8.9 | 9e-17 | 36/48 (PANC-1, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.40×** | +8.2 | 4e-14 | 37/48 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +8.1 | 5e-14 | 30/47 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +7.6 | 3e-12 | 29/45 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +7.0 | 3e-10 | 31/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.36×** | +5.4 | 4e-06 | 26/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +5.3 | 6e-06 | 21/48 (Hs 766T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.24×** | +4.4 | 8e-04 | 20/48 (Hs 766T, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 9e-04 | 14/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 19/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 19/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.003 | 16/48 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.7 | 0.009 | 13/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.011 | 16/48 (A-172, A-427, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.036 | 9/48 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.036 | 3/48 (NCI-H460, KATO III, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8511.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.446×); [[Fluvoxamine (drug)]] 5 µM in 1 line (AN3 CA 0.148×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.824×** | -4.0 | 0.027 | 11/48 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~7% of this change | **0.829×** | -3.9 | 0.027 | 19/46 (SW1417, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.878× | -3.8 | 0.027 | 14/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.850× | -3.3 | 0.12 | 15/48 (H4, HOP62, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.809× | -3.1 | 0.21 | 6/48 (J82, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 27.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.0) | — |
| [[A-427 (line)]] | wt | 41.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.446× (z -11.2) |
| [[AN3 CA (line)]] | alt | 43.3 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.148× (z -9.1) |
| [[C32 (line)]] | wt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +13.4) | — |
| [[HT-29 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 44.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.4) | — |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 54.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRTO4]] | +0.77 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.75 | +0.71 / +0.78 | both halves | 7e-06 |  |
| [[LTV1]] | +0.73 | +0.72 / +0.67 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 587 |
| [[SCO1]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[NAA25]] | +0.72 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[DDX31]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[DHX37]] | +0.72 | +0.71 / +0.67 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 544 |
| [[MAK16]] | +0.71 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[WDR4]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[MAPKAPK5]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[UTP4]] | +0.70 | +0.58 / +0.74 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 622 |
| [[BYSL]] | +0.70 | +0.71 / +0.63 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSRP2]] | B | CSRP2 activity raises NOL9's level | lines that do not express CSRP2 (6) vs lines expressing it (44) | 1.13× lower at baseline in the lines without CSRP2 | 0.0998 | ⚠ within organs, on part of the lines; also absent: TPST1, TBKBP1, CYP46A1; maybe low, not absent |
| [[SLC9B2]] | C | SLC9B2 activity raises NOL9's level | lines that do not express SLC9B2 (3) vs lines expressing it (47) | 1.31× lower at baseline in the lines without SLC9B2 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM132A, HOMER3, SOAT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.0, -35.5); signed map (-1.1, -44.8). **Vector** length 82.5, 16.7% of its response variance represented; |z| ≥ 3 in 813 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.59 to 13); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.55 to 11); *ribosome biogenesis* (control, mean cos +0.54 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +9.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.1 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.9 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,521,347-6,554,513 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23323, NET6, Grc3 |
| Gene groups (HGNC) | Large ribosomal subunit biogenesis complex; RNA kinases; DNA kinases |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SY16](https://www.uniprot.org/uniprotkb/Q5SY16) (Polynucleotide 5'-hydroxyl-kinase NOL9):

> Polynucleotide kinase that can phosphorylate the 5'-hydroxyl groups of single-stranded and double-stranded RNA and DNA substrates. Involved in rRNA processing and its kinase activity is required for the processing of the 32S precursor into 5.8S and 28S rRNAs, more specifically for the generation of the major 5.8S(S) form. Required for the efficient pre-rRNA processing of internal transcribed spacer 2 (ITS2). Associates with LAS1L to form an ITS2 pre-rRNA endonuclease-kinase complex and is …

**Summary**, from NCBI Gene [79707](https://www.ncbi.nlm.nih.gov/gene/79707):

> Enables ATP-dependent polydeoxyribonucleotide 5'-hydroxyl-kinase activity. Involved in maturation of 5.8S rRNA. Located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26265) · Entrez [79707](https://www.ncbi.nlm.nih.gov/gene/79707) · UniProt [Q5SY16](https://www.uniprot.org/uniprotkb/Q5SY16) · Ensembl [ENSG00000162408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162408)

## Data

Gene col 8511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8511); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8511]; `tensor/DDL_lfc|DDL_z.npy` [8511]; `embed/gene_vectors.npy` [8511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8511 or target_col == 8511). Every well: [[NOL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
